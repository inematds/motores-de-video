#!/usr/bin/env python3
"""Traduz para EN e ES os textos novos ou alterados do índice, pelo tradutor central do INEMA.

Fonte: catalogo.json (textos dos motores e grupos) + i18n/pt.json (textos da página e do README).
Destino: i18n/en.json e i18n/es.json. Só as chaves que faltam ou cujo texto em PT mudou vão
para o tradutor (`inema-traduz`, pela assinatura). As respostas são validadas: mesmas chaves,
mesmos marcadores {n}/{data}/{k}/{url} e as mesmas tags HTML.

Uso:  python3 traduzir.py [--lang en|es] [--lote 25]
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CAMPOS_MOTOR = ("nome", "oque", "serve", "formato", "avatar", "acionamento", "nota_exemplos")
NOMES = {"en": "inglês (público global)", "es": "espanhol (América Latina)"}


def achatar(obj, prefixo=""):
    """dict/list aninhado -> {caminho: texto}."""
    saida = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            saida.update(achatar(v, f"{prefixo}{k}."))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            saida.update(achatar(v, f"{prefixo}{i}."))
    elif isinstance(obj, str):
        saida[prefixo.rstrip(".")] = obj
    return saida


def fonte_pt():
    cat = json.load(open(os.path.join(AQUI, "catalogo.json"), encoding="utf-8"))
    pt = json.load(open(os.path.join(AQUI, "i18n", "pt.json"), encoding="utf-8"))
    src = {}
    for m in cat["motores"]:
        for c in CAMPOS_MOTOR:
            if m.get(c):
                src[f"motores.{m['id']}.{c}"] = m[c]
    for g in cat["grupos"]:
        src[f"grupos.{g['id']}"] = g["nome"]
    for k, v in achatar(pt["ui"], "ui.").items():
        if k in ("ui.html_lang", "ui.data_fmt") or re.match(r"ui\.esc\.\d+\.1$", k) or re.match(r"ui\.passos\.\d+\.2$", k):
            continue  # ids de motor, comandos e formatos ficam iguais em todos os idiomas
        src[k] = v
    for k, v in achatar(pt["readme"], "readme.").items():
        if re.match(r"readme\.(processo\.\d+\.0|arquivos\.\d+\.0)$", k) or k == "readme.seletor":
            continue
        src[k] = v
    return src


def marcas(s):
    return sorted(re.findall(r"\{[a-z]+\}|</?[a-z]+[^>]*>|`[^`]*`", s))


def h(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:10]


def pedir(lang, lote):
    corpo = json.dumps(lote, ensure_ascii=False, indent=1)
    pedido = (
        f"Traduza os valores deste JSON do português do Brasil para {NOMES[lang]}. "
        "É a página que explica os motores de vídeo do INEMA (inema.club), um projeto educativo de IA. "
        "Regras: devolva SÓ o JSON, com exatamente as mesmas chaves; não traduza nomes de projeto, "
        "nomes de arquivo, comandos, nomes de canal, siglas (INMET, IBGE, MEI, CBS, IBS), nem o que está "
        "entre crases; mantenha {n}, {data}, {k}, {url}, {total} e as tags HTML iguais; mantenha 16:9, 9:16 e horários; "
        "tom simples e direto, frases curtas.\n\n" + corpo
    )
    r = subprocess.run(["inema-traduz"], input=pedido, capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-400:])
    txt = r.stdout.strip()
    m = re.search(r"\{.*\}", txt, re.S)
    if not m:
        raise RuntimeError("resposta sem JSON")
    return json.loads(m.group(0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "es"], action="append")
    ap.add_argument("--lote", type=int, default=25)
    a = ap.parse_args()
    src = fonte_pt()
    rc = 0
    for lang in a.lang or ["en", "es"]:
        caminho = os.path.join(AQUI, "i18n", f"{lang}.json")
        dados = json.load(open(caminho, encoding="utf-8")) if os.path.exists(caminho) else {}
        trad = dados.get("textos", {})
        hashes = dados.get("_fonte", {})
        falta = {k: v for k, v in src.items() if k not in trad or hashes.get(k) != h(v)}
        print(f"{lang}: {len(falta)} de {len(src)} textos para traduzir")
        chaves = list(falta)
        for i in range(0, len(chaves), a.lote):
            lote = {k: falta[k] for k in chaves[i:i + a.lote]}
            for tentativa in (1, 2):
                try:
                    resp = pedir(lang, lote)
                except Exception as e:
                    print(f"  lote {i // a.lote + 1}: falhou ({e}); tentativa {tentativa}", file=sys.stderr)
                    continue
                ok = 0
                for k, v in lote.items():
                    t = resp.get(k)
                    if isinstance(t, str) and t.strip() and marcas(t) == marcas(v):
                        trad[k] = t.strip()
                        hashes[k] = h(v)
                        ok += 1
                lote = {k: v for k, v in lote.items() if hashes.get(k) != h(v)}
                print(f"  lote {i // a.lote + 1}: {ok} ok, {len(lote)} pendentes")
                if not lote:
                    break
            if lote:
                rc = 1
            tmp = caminho + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump({"_fonte": hashes, "textos": trad}, f, ensure_ascii=False, indent=1, sort_keys=True)
                f.write("\n")
            os.replace(tmp, caminho)
        sobra = [k for k in trad if k not in src]
        if sobra:
            print(f"  {lang}: {len(sobra)} chaves antigas sem uso (mantidas)")
    return rc


if __name__ == "__main__":
    sys.exit(main())
