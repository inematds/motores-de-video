#!/usr/bin/env python3
"""Relê o histórico de publicações do yt-pubx e regrava motores.json.

Para cada motor do catalogo.json escolhe até 3 vídeos PÚBLICOS, recentes e variados
(canal, formato e assunto diferentes), identificando o motor pela pasta de origem do MP4,
pelo canal ou pelo registro de produções. Depois roda o gerar.py (README + guia).

Uso:
  python3 atualizar-exemplos.py                 # lê os caminhos padrão
  python3 atualizar-exemplos.py --historico H --producoes P
  python3 atualizar-exemplos.py --sem-gerar     # só o motores.json

Só leitura de arquivos locais: não chama o YouTube nem nenhuma API.
O motores.json guarda apenas id, link, título, canal, data e formato de cada vídeo
(nunca o caminho do arquivo de origem).
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
HIST_PADRAO = os.environ.get("YTPUBX_HISTORICO", os.path.expanduser("~/.local/share/yt-pubx/historico.jsonl"))
PROD_PADRAO = os.environ.get("PRODUCOES_VIDEO", os.path.expanduser("~/projetos/wifi/PRODUCOES-VIDEO.md"))
POR_MOTOR = 3


def ler_historico(caminho):
    linhas = []
    with open(caminho, encoding="utf-8") as f:
        for n, l in enumerate(f, 1):
            l = l.strip()
            if not l:
                continue
            try:
                linhas.append(json.loads(l))
            except json.JSONDecodeError:
                print(f"aviso: linha {n} do histórico ilegível, pulada", file=sys.stderr)
    removidos = {r.get("removido") for r in linhas if r.get("removido")}
    videos = []
    for r in linhas:
        vid = r.get("video_id")
        if not vid or vid in removidos:
            continue
        priv = r.get("privacy")
        status = priv.get("privacyStatus") if isinstance(priv, dict) else priv
        if status != "public":
            continue
        videos.append(r)
    return videos


def ler_producoes(caminho):
    """Mapa ferramenta -> ids do YouTube, a partir da tabela do registro de produções."""
    mapa = {}
    if not caminho or not os.path.exists(caminho):
        return mapa
    for linha in open(caminho, encoding="utf-8"):
        if not linha.startswith("|"):
            continue
        cols = [c.strip() for c in linha.split("|")]
        if len(cols) < 7:
            continue
        tipo = (cols[2] + " " + cols[3]).lower()
        ids = re.findall(r"(?:watch\?v=|shorts/|youtu\.be/)([A-Za-z0-9_-]{11})", linha)
        if "refazvideo" in tipo:
            chave = "refazvideo"
        elif "explicavideo" in tipo:
            chave = "explicavideo"
        else:
            continue
        mapa.setdefault(chave, set()).update(ids)
    return mapa


_DIM = {}


def dimensoes(caminho):
    """Largura x altura do MP4 de origem, se ele ainda existir na máquina (ffprobe local)."""
    if caminho in _DIM:
        return _DIM[caminho]
    dim = None
    if caminho and os.path.exists(caminho):
        try:
            out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                  "stream=width,height", "-of", "csv=p=0", caminho],
                                 capture_output=True, text=True, timeout=20).stdout.strip()
            w, h = out.split(",")[:2]
            dim = (int(w), int(h))
        except Exception:
            dim = None
    _DIM[caminho] = dim
    return dim


def formato_do_video(r, formato_motor):
    if "16:9" not in formato_motor and "9:16" in formato_motor:
        return "9:16"
    if "9:16" not in formato_motor and "16:9" in formato_motor:
        return "16:9"
    dim = dimensoes(r.get("origem") or "")
    if dim:
        return "9:16" if dim[1] > dim[0] else "16:9"
    txt = (r.get("origem") or "") + " " + (r.get("titulo") or "")
    return "9:16" if re.search(r"916|9x16|9-16|#shorts?\b", txt, re.I) else "16:9"


def assunto(titulo):
    t = re.sub(r"#\w+", "", titulo or "").lower()
    palavras = re.findall(r"\w+", t)
    return " ".join(palavras[:3])


def candidatos(motor, videos, producoes):
    regras = motor.get("regras") or {}
    origens = regras.get("origem") or []
    canais = regras.get("canal") or []
    ids_prod = set()
    for k in regras.get("producoes") or []:
        ids_prod |= producoes.get(k, set())
    so_canais = regras.get("so_canais") or []
    excluir = set(motor.get("excluir") or [])
    excl_tit = [s.lower() for s in motor.get("excluir_titulo") or []]
    saida = []
    for r in videos:
        o = r.get("origem") or ""
        casa = (any(p in o for p in origens) or r.get("canal") in canais or r["video_id"] in ids_prod)
        if not casa or r["video_id"] in excluir or (so_canais and r.get("canal") not in so_canais):
            continue
        if any(s in (r.get("titulo") or "").lower() for s in excl_tit):
            continue
        saida.append(r)
    saida.sort(key=lambda r: r.get("data") or "", reverse=True)
    return saida


def escolher(motor, cands, todos):
    por_id = {r["video_id"]: r for r in todos}
    escolhidos = [por_id[i] for i in motor.get("fixar") or [] if i in por_id][:POR_MOTOR]
    fmt_motor = motor.get("formato", "")

    def ja(r):
        return any(e["video_id"] == r["video_id"] for e in escolhidos)

    def novo_assunto(r):
        return assunto(r["titulo"]) not in {assunto(e["titulo"]) for e in escolhidos}

    passes = [
        lambda r: novo_assunto(r) and formato_do_video(r, fmt_motor) not in {formato_do_video(e, fmt_motor) for e in escolhidos}
        and r.get("canal") not in {e.get("canal") for e in escolhidos},
        lambda r: novo_assunto(r) and formato_do_video(r, fmt_motor) not in {formato_do_video(e, fmt_motor) for e in escolhidos},
        lambda r: assunto(r["titulo"]) not in {assunto(e["titulo"]) for e in escolhidos}
        and (r.get("canal"), formato_do_video(r, fmt_motor)) not in {(e.get("canal"), formato_do_video(e, fmt_motor)) for e in escolhidos},
        lambda r: assunto(r["titulo"]) not in {assunto(e["titulo"]) for e in escolhidos},
        lambda r: True,
    ]
    for teste in passes:
        for r in cands:
            if len(escolhidos) >= POR_MOTOR:
                break
            if not ja(r) and teste(r):
                escolhidos.append(r)
    escolhidos.sort(key=lambda r: r.get("data") or "", reverse=True)
    return escolhidos


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--historico", default=HIST_PADRAO)
    ap.add_argument("--producoes", default=PROD_PADRAO)
    ap.add_argument("--sem-gerar", action="store_true")
    a = ap.parse_args()

    cat = json.load(open(os.path.join(AQUI, "catalogo.json"), encoding="utf-8"))
    # regras que não podem ir para o repo público (ex.: nome de pasta que cita terceiro) ficam
    # em regras.locais.json, fora do git: {"<id do motor>": {"origem": ["..."]}}
    locais = os.path.join(AQUI, "regras.locais.json")
    if os.path.exists(locais):
        extra = json.load(open(locais, encoding="utf-8"))
        for m in cat["motores"]:
            for k, v in (extra.get(m["id"]) or {}).items():
                m.setdefault("regras", {}).setdefault(k, [])
                m["regras"][k] = list(m["regras"][k]) + list(v)
    destino = os.path.join(AQUI, "motores.json")
    if not os.path.exists(a.historico):
        print(f"histórico não encontrado ({a.historico}); motores.json mantido como está.")
        return 0

    videos = ler_historico(a.historico)
    producoes = ler_producoes(a.producoes)
    canais = cat.get("canais", {})
    motores = []
    for m in cat["motores"]:
        cands = candidatos(m, videos, producoes)
        ex = []
        for r in escolher(m, cands, videos):
            c = r.get("canal")
            ex.append({
                "video_id": r["video_id"],
                "url": "https://www.youtube.com/watch?v=" + r["video_id"],
                "titulo": re.sub(r"\s+", " ", r.get("titulo") or "").strip(),
                "canal": c,
                "canal_nome": canais.get(c, {}).get("nome", c),
                "data": (r.get("data") or "")[:10],
                "formato": formato_do_video(r, m.get("formato", "")),
            })
        saida = {k: v for k, v in m.items() if k not in ("regras", "excluir", "excluir_titulo", "fixar", "nota_regras")}
        saida["exemplos"] = ex
        motores.append(saida)
        print(f"{m['id']:22s} {len(cands):4d} candidatos -> {len(ex)} exemplos")

    out = {
        "gerado_em": datetime.now().strftime("%Y-%m-%d"),
        "fonte_exemplos": "histórico de publicações do yt-pubx (só vídeos públicos, não reconferidos no ar)",
        "canais": canais,
        "grupos": cat["grupos"],
        "motores": motores,
    }
    tmp = destino + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, destino)
    print(f"gravado {destino}")
    if not a.sem_gerar:
        return subprocess.call([sys.executable, os.path.join(AQUI, "gerar.py")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
