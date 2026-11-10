#!/usr/bin/env python3
"""Gera README.md / README.en.md / README.es.md e guia/index.html, guia/en/, guia/es/ a partir do motores.json.

Textos PT: motores.json (vindo do catalogo.json) + i18n/pt.json. EN/ES: i18n/en.json e i18n/es.json
(gerados pelo traduzir.py). Chave sem tradução cai no PT e o script avisa.
Uso: python3 gerar.py
"""
import html
import json
import os
import sys
from datetime import datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
SLUG = "motores-de-video"
REPO = f"https://github.com/inematds/{SLUG}"
PAGES = f"https://inematds.github.io/{SLUG}/guia/"
LANGS = ("pt", "en", "es")
CAMPOS = ("nome", "oque", "serve", "formato", "avatar", "acionamento", "nota_exemplos")
FALTAS = {"en": set(), "es": set()}


def carregar():
    dados = json.load(open(os.path.join(AQUI, "motores.json"), encoding="utf-8"))
    pt = json.load(open(os.path.join(AQUI, "i18n", "pt.json"), encoding="utf-8"))
    trad = {}
    for l in ("en", "es"):
        p = os.path.join(AQUI, "i18n", f"{l}.json")
        trad[l] = json.load(open(p, encoding="utf-8")).get("textos", {}) if os.path.exists(p) else {}
    return dados, pt, trad


class Txt:
    def __init__(self, lang, pt, trad):
        self.lang, self.pt, self.t = lang, pt, trad.get(lang, {})

    def _pt(self, chave):
        obj = self.pt
        for parte in chave.split("."):
            obj = obj[int(parte)] if isinstance(obj, list) else obj[parte]
        return obj

    def __call__(self, chave):
        base = self._pt(chave)
        if self.lang == "pt" or not isinstance(base, str):
            return base
        if chave in self.t:
            return self.t[chave]
        FALTAS[self.lang].add(chave)
        return base

    def motor(self, m, campo):
        v = m.get(campo)
        if not v or self.lang == "pt":
            return v
        k = f"motores.{m['id']}.{campo}"
        if k in self.t:
            return self.t[k]
        FALTAS[self.lang].add(k)
        return v

    def grupo(self, g):
        if self.lang == "pt":
            return g["nome"]
        k = f"grupos.{g['id']}"
        if k not in self.t:
            FALTAS[self.lang].add(k)
        return self.t.get(k, g["nome"])

    def lista(self, chave):
        """lista de listas (esc, passos, fluxo...) com as partes traduzíveis trocadas."""
        base = self._pt(chave)
        saida = []
        for i, item in enumerate(base):
            if isinstance(item, list):
                saida.append([item[j] if self._pula(chave, j) else self(f"{chave}.{i}.{j}")
                              for j in range(len(item))])
            else:
                saida.append(self(f"{chave}.{i}"))
        return saida

    @staticmethod
    def _pula(chave, j):
        return (chave.endswith("esc") and j == 1) or (chave.endswith("passos") and j == 2) or \
               (chave.endswith("processo") and j == 0) or (chave.endswith("arquivos") and j == 0)

    def data(self, iso):
        try:
            d = datetime.strptime(iso, "%Y-%m-%d")
        except ValueError:
            return iso
        return d.strftime("%Y-%m-%d") if self.lang == "en" else d.strftime("%d/%m/%Y")


def e(s):
    return html.escape(s or "", quote=True)


def repo_curto(url):
    return url.replace("https://github.com/", "github.com/")


# ───────────────────────────── guia ─────────────────────────────
CSS = """
  :root{
    --bg:#0c0c10; --bg2:#14141b; --card:#16161e; --line:#272730;
    --txt:#e9e9ee; --mut:#9a9aa6; --amb:#FACC15; --amb2:#f0c070; --sky:#38bdf8; --pro:#cbd5e1;
    --ambs:rgba(250,204,21,.12); --link:#FACC15;
    color-scheme:dark;
  }
  body.light{
    --bg:#f6f7f9; --bg2:#eceef2; --card:#ffffff; --line:#e1e3ea;
    --txt:#1a1a22; --mut:#5b5b68; --amb:#a16207; --amb2:#a16207; --sky:#0369a1; --pro:#b45309;
    --ambs:rgba(250,204,21,.28); --link:#854d0e;
    color-scheme:light;
  }
  body.light .hero .glow{opacity:.5}
  body.light pre{background:#0e0e14;color:#d6d6e0}
  body.light pre .c{color:#8a8a98}
  body.light .btn{background:#FACC15;color:#1a1206}
  body.light .btn.ghost{background:transparent;color:var(--txt)}
  body.light nav{background:rgba(246,247,249,.85)}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;background:var(--bg);color:var(--txt);font:16px/1.65 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
  h1,h2,h3{font-family:Sora,sans-serif;line-height:1.15;margin:0}
  a{color:var(--link);text-decoration:none}
  code,pre{font-family:"JetBrains Mono",monospace}
  .wrap{max-width:1160px;margin:0 auto;padding:0 22px}
  .mut{color:var(--mut)} .amb{color:var(--amb)}
  .chip{display:inline-block;font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--amb);font-weight:600;font-family:Sora}
  nav{position:sticky;top:0;z-index:30;backdrop-filter:blur(12px);background:rgba(12,12,16,.78);border-bottom:1px solid var(--line)}
  nav .wrap{display:flex;align-items:center;gap:22px;height:60px}
  nav .brand{display:flex;align-items:center;gap:8px;font-family:Sora;font-weight:800;letter-spacing:-.02em;color:var(--amb);white-space:nowrap}
  nav .brand .emoji{font-size:1.25rem}
  nav .sep{color:var(--mut);opacity:.45}
  nav .inema{color:var(--sky);font-weight:600;font-size:.88rem;font-family:Sora}
  nav .pro{color:var(--pro);font-weight:600;font-size:.88rem;font-family:Sora}
  nav .clubpro{display:inline-flex;align-items:center;gap:6px}
  nav .links{margin-left:auto;display:flex;align-items:center;gap:20px;font-size:.92rem}
  nav .links a.sec{color:var(--mut)} nav .links a.sec:hover{color:var(--txt)}
  .lang{display:inline-flex;gap:2px;font-family:Sora;font-size:.78rem}
  .lang a{color:var(--mut);padding:.2em .45em;border-radius:6px} .lang a.on{color:var(--amb);background:var(--ambs)}
  .tgl{background:var(--bg2);border:1px solid var(--line);color:var(--txt);width:38px;height:38px;border-radius:10px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;font-size:1.05rem}
  .tgl:hover{border-color:var(--amb)}
  .btn{display:inline-block;background:var(--amb);color:#1a1206;font-weight:600;padding:.6em 1.05em;border-radius:10px;font-family:Sora}
  .btn.ghost{background:transparent;color:var(--txt);border:1px solid var(--line)}
  @media(max-width:900px){nav .links a.sec{display:none}}
  @media(max-width:560px){nav .wrap{gap:8px;padding:8px 14px;height:auto;flex-wrap:wrap} nav .links{gap:8px;margin-left:0;width:100%;justify-content:space-between} nav .btn{padding:.45em .7em;font-size:.82rem} .tgl{width:34px;height:34px}}
  .hero{position:relative;overflow:hidden;border-bottom:1px solid var(--line)}
  .hero .glow{position:absolute;inset:-40% -20% auto auto;width:70%;height:600px;background:radial-gradient(closest-side,rgba(250,204,21,.18),transparent 70%);pointer-events:none}
  .hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;padding:74px 22px}
  .hero h1{font-size:clamp(2.2rem,5vw,3.5rem);font-weight:800;letter-spacing:-.025em}
  .hero p.lead{font-size:1.18rem;color:var(--mut);margin:1.1em 0 1.6em;max-width:34ch}
  .hero .cta{display:flex;gap:12px;flex-wrap:wrap}
  .hero figure{margin:0;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px -30px #000}
  .hero figure img{width:100%;height:auto;display:block}
  .resumo{padding:38px 0 34px;border-bottom:1px solid var(--line)}
  .resumo p{font-size:1.12rem;line-height:1.7;max-width:74ch;margin:.55em 0 0}
  @media(max-width:780px){.hero .wrap{grid-template-columns:1fr;padding:48px 16px} .wrap{padding:0 16px}}
  section{padding:62px 0;border-bottom:1px solid var(--line);scroll-margin-top:64px}
  section h2{font-size:clamp(1.5rem,3.4vw,2.1rem);font-weight:800;letter-spacing:-.02em}
  section .sub{color:var(--mut);margin:.6em 0 2em;max-width:62ch}
  .grid{display:grid;gap:16px}
  .g3{grid-template-columns:repeat(3,1fr)}
  @media(max-width:820px){.g3{grid-template-columns:1fr 1fr}}
  @media(max-width:540px){.g3{grid-template-columns:1fr}}
  .card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;min-width:0}
  .card h3{font-size:1.05rem;margin-bottom:.4em}
  .card p{color:var(--mut);font-size:.95rem;margin:0}
  .termos{display:grid;grid-template-columns:repeat(3,1fr);gap:10px 18px;margin:0}
  @media(max-width:820px){.termos{grid-template-columns:1fr 1fr}}
  @media(max-width:540px){.termos{grid-template-columns:1fr}}
  .termos div{border-left:2px solid var(--line);padding:2px 0 2px 12px;min-width:0}
  .termos dt{font-family:Sora;font-weight:600;font-size:.92rem}
  .termos dd{margin:.15em 0 0;color:var(--mut);font-size:.9rem}
  .esc{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
  @media(max-width:820px){.esc{grid-template-columns:1fr 1fr}}
  @media(max-width:540px){.esc{grid-template-columns:1fr}}
  .esc a{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;color:var(--txt)}
  .esc a:hover{border-color:var(--amb)}
  .esc a span{display:block;color:var(--mut);font-size:.95rem}
  .esc a b{display:block;font-family:Sora;color:var(--amb);margin-top:.35em}
  .grupo{margin:44px 0 18px;display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
  .grupo h3{font-size:1.3rem}
  .grupo span{color:var(--mut);font-size:.9rem}
  .mots{display:grid;grid-template-columns:1fr 1fr;gap:18px}
  @media(max-width:980px){.mots{grid-template-columns:1fr}}
  .mot{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;min-width:0;scroll-margin-top:80px}
  .mot .mh{display:flex;gap:10px;align-items:center}
  .mot .mh .em{font-size:1.35rem}
  .mot h4{font-family:Sora;font-size:1.12rem;margin:0;line-height:1.25}
  .mot .tags{display:flex;flex-wrap:wrap;gap:6px;margin:.75em 0 .2em}
  .tag{font-family:Sora;font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--line);border-radius:999px;padding:.2em .7em;color:var(--mut)}
  .mot p.oq{margin:.6em 0 .9em}
  .mot dl{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;margin:0 0 1em;font-size:.94rem}
  .mot dt{color:var(--mut);font-family:Sora;font-size:.8rem;letter-spacing:.04em;padding-top:.15em}
  .mot dd{margin:0;min-width:0;overflow-wrap:anywhere}
  @media(max-width:460px){.mot dl{grid-template-columns:1fr} .mot dt{padding-top:.5em}}
  .exl{font-family:Sora;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--amb);margin:.4em 0 .6em}
  .exs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
  @media(max-width:520px){.exs{grid-template-columns:1fr}}
  .vx{display:block;color:var(--txt);border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--bg2)}
  .vx:hover{border-color:var(--amb)}
  .vx img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block;background:#000}
  .vx .vt{display:block;padding:8px 10px 2px;font-size:.88rem;line-height:1.35}
  .vx .vm{display:block;padding:0 10px 9px;font-size:.8rem;color:var(--mut)}
  .nota{color:var(--mut);font-size:.9rem;margin:.6em 0 0}
  .flow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:10px}
  .flow span{background:var(--bg2);border:1px solid var(--line);border-radius:999px;padding:.45em .9em;font-size:.85rem;font-family:Sora;font-weight:600}
  .flow .arr{color:var(--amb);border:none;background:none;padding:0 .1em}
  pre{background:#0a0a0e;border:1px solid var(--line);border-radius:12px;padding:16px 18px;overflow:auto;font-size:.86rem;line-height:1.6;color:#d6d6e0;white-space:pre-wrap;overflow-wrap:anywhere}
  pre .k{color:var(--amb2)}
  .step{display:grid;grid-template-columns:46px minmax(0,1fr);gap:16px;margin-bottom:26px}
  .step>div{min-width:0}
  .step .b{width:46px;height:46px;border-radius:12px;background:#FACC15;color:#1a1206;font-family:Sora;font-weight:800;font-size:1.25rem;display:flex;align-items:center;justify-content:center}
  .step h3{font-size:1.12rem;margin-bottom:.3em}
  .step p{color:var(--mut);margin:.2em 0 .7em}
  footer{padding:46px 0;text-align:center;color:var(--mut);font-size:.9rem}
  .pill{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:.3em .8em;font-size:.78rem;color:var(--mut);margin:4px}
"""


def card_motor(m, T, por_id):
    nome = T.motor(m, "nome")
    tags = "".join(f'<span class="tag">{e(x)}</span>' for x in [T.motor(m, "formato")] if x and x != "—")
    if m.get("repo"):
        repo = f'<a href="{e(m["repo"])}" target="_blank" rel="noopener">{e(repo_curto(m["repo"]))}</a>'
    else:
        repo = e(T("ui.privado"))
    for extra in m.get("repo_extra") or []:
        repo += f' · {e(extra["nome"])}: ' + (f'<a href="{e(extra["url"])}" target="_blank" rel="noopener">{e(repo_curto(extra["url"]))}</a>' if extra.get("url") else e(T("ui.privado")))
    linhas = [("ui.l_serve", T.motor(m, "serve")), ("ui.l_avatar", T.motor(m, "avatar")), ("ui.l_acion", T.motor(m, "acionamento"))]
    dl = "".join(f"<dt>{e(T(k))}</dt><dd>{e(v)}</dd>" for k, v in linhas if v and v != "—")
    dl += f"<dt>{e(T('ui.l_repo'))}</dt><dd>{repo}</dd>"
    ex = m.get("exemplos") or []
    blocos = ""
    if ex:
        vids = "".join(
            f'<a class="vx" href="{e(x["url"])}" target="_blank" rel="noopener">'
            f'<img src="https://i.ytimg.com/vi/{e(x["video_id"])}/hqdefault.jpg" alt="{e(x["titulo"])}" loading="lazy" width="480" height="270">'
            f'<span class="vt">{e(x["titulo"])}</span>'
            f'<span class="vm">{e(x["canal_nome"])} · {e(T.data(x["data"]))} · {e(x["formato"])}</span></a>'
            for x in ex)
        blocos = f'<div class="exl">{e(T("ui.l_ex"))}</div><div class="exs">{vids}</div>'
    nota = T.motor(m, "nota_exemplos")
    if nota:
        blocos += f'<p class="nota">{e(nota)}</p>'
    elif 0 < len(ex) < 3:
        blocos += f'<p class="nota">{e(T("ui.menos_ex").replace("{k}", str(len(ex))))}</p>'
    elif not ex:
        blocos += f'<p class="nota">{e(T("ui.sem_ex"))}</p>'
    return (f'<article class="mot" id="m-{e(m["id"])}"><div class="mh"><span class="em">{m.get("emoji", "")}</span>'
            f'<h4>{e(nome)}</h4></div><div class="tags">{tags}</div><p class="oq">{e(T.motor(m, "oque"))}</p>'
            f'<dl>{dl}</dl>{blocos}</article>')


def guia(lang, dados, pt, trad):
    T = Txt(lang, pt, trad)
    pre = "" if lang == "pt" else "../"
    sufixo = "" if lang == "pt" else f"-{lang}"
    n = len(dados["motores"])
    por_id = {m["id"]: m for m in dados["motores"]}
    seletor = {
        "pt": '<a class="on" href="./">PT</a><a href="en/">EN</a><a href="es/">ES</a>',
        "en": '<a href="../">PT</a><a class="on" href="./">EN</a><a href="../es/">ES</a>',
        "es": '<a href="../">PT</a><a href="../en/">EN</a><a class="on" href="./">ES</a>',
    }[lang]
    html_lang = {"pt": "pt-BR", "en": "en", "es": "es"}[lang]
    esc = "".join(
        f'<a href="#m-{e(mid)}"><span>{e(txt)}</span><b>{e(T.motor(por_id[mid], "nome"))}</b></a>'
        for txt, mid in T.lista("ui.esc") if mid in por_id)
    grupos = ""
    for g in dados["grupos"]:
        ms = [m for m in dados["motores"] if m["grupo"] == g["id"]]
        if not ms:
            continue
        grupos += (f'<div class="grupo"><h3>{e(T.grupo(g))}</h3><span>{len(ms)}</span></div>'
                   f'<div class="mots">{"".join(card_motor(m, T, por_id) for m in ms)}</div>')
    fluxo = '<span class="arr">→</span>'.join(f"<span>{e(x)}</span>" for x in T.lista("ui.fluxo"))
    passos = ""
    for i, (tit, txt, cmd) in enumerate(T.lista("ui.passos"), 1):
        passos += (f'<div class="step"><div class="b">{i}</div><div><h3>{e(tit)}</h3><p>{e(txt)}</p>'
                   f'<pre><span class="k">{e(cmd)}</span></pre></div></div>')
    ex_total = sum(len(m.get("exemplos") or []) for m in dados["motores"])
    termos = "".join(f"<div><dt>{e(t)}</dt><dd>{e(d)}</dd></div>" for t, d in T.lista("ui.termos"))
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(T("ui.titulo_pagina"))}</title>
<meta name="description" content="{e(T("ui.meta"))}">
<link rel="alternate" hreflang="pt-BR" href="{PAGES}">
<link rel="alternate" hreflang="en" href="{PAGES}en/">
<link rel="alternate" hreflang="es" href="{PAGES}es/">
<meta property="og:image" content="{PAGES}assets/banner{sufixo}.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<!-- gerado por gerar.py a partir do motores.json; não edite à mão -->
<nav><div class="wrap">
  <a class="brand" href="#top"><span class="emoji">🎞️</span> {SLUG}</a>
  <span class="sep">|</span>
  <span class="clubpro"><a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a><span class="sep">-</span><a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a></span>
  <div class="links">
    <a class="sec" href="#escolher">{e(T("ui.nav_escolher"))}</a>
    <a class="sec" href="#motores">{e(T("ui.nav_motores"))}</a>
    <a class="sec" href="#fluxo">{e(T("ui.nav_fluxo"))}</a>
    <a class="sec" href="#guia">{e(T("ui.nav_guia"))}</a>
    <span class="lang">{seletor}</span>
    <button class="tgl" id="themeToggle" aria-label="{e(T("ui.tema"))}" title="{e(T("ui.tema"))}">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">GitHub</a>
  </div>
</div></nav>

<header class="hero" id="top">
  <div class="glow"></div>
  <div class="wrap">
    <div>
      <span class="chip">{e(T("ui.hero_chip"))}</span>
      <h1>{T("ui.hero_h1")}</h1>
      <p class="lead">{e(T("ui.hero_lead").replace("{n}", str(n)))}</p>
      <div class="cta">
        <a class="btn" href="#motores">{e(T("ui.cta_motores"))}</a>
        <a class="btn ghost" href="{REPO}" target="_blank" rel="noopener">{e(T("ui.cta_github"))}</a>
      </div>
    </div>
    <figure><img src="{pre}assets/banner{sufixo}.jpg" alt="{e(T("ui.hero_alt"))}" width="1400" height="788"></figure>
  </div>
</header>

<section id="resumo" class="resumo"><div class="wrap">
  <span class="chip">{e(T("ui.resumo_chip"))}</span>
  <p>{e(T("ui.resumo"))}</p>
</div></section>

<section id="oque"><div class="wrap">
  <span class="chip">{e(T("ui.oque_chip"))}</span>
  <h2>{e(T("ui.oque_h2"))}</h2>
  <p class="sub">{e(T("ui.oque_sub"))}</p>
  <figure style="margin:0 0 26px;border-radius:16px;overflow:hidden;border:1px solid var(--line)"><img src="{pre}assets/banner-grade{sufixo}.jpg" alt="{e(T("ui.grade_alt"))}" loading="lazy" style="width:100%;height:auto;display:block" width="1400" height="788"></figure>
  <div class="grid g3">
    <div class="card"><h3>🗂️ {e(T("ui.p1_t"))}</h3><p>{e(T("ui.p1_x"))}</p></div>
    <div class="card"><h3>▶️ {e(T("ui.p2_t"))}</h3><p>{e(T("ui.p2_x").replace("{total}", str(ex_total)))}</p></div>
    <div class="card"><h3>🔄 {e(T("ui.p3_t"))}</h3><p>{e(T("ui.p3_x"))}</p></div>
  </div>
  <h3 style="margin:34px 0 14px;font-size:1.15rem">{e(T("ui.termos_t"))}</h3>
  <dl class="termos">{termos}</dl>
</div></section>

<section id="escolher"><div class="wrap">
  <span class="chip">{e(T("ui.esc_chip"))}</span>
  <h2>{e(T("ui.esc_h2"))}</h2>
  <p class="sub">{e(T("ui.esc_sub"))}</p>
  <div class="esc">{esc}</div>
</div></section>

<section id="motores"><div class="wrap">
  <span class="chip">{e(T("ui.mot_chip"))}</span>
  <h2>{e(T("ui.mot_h2").replace("{n}", str(n)))}</h2>
  <p class="sub">{e(T("ui.mot_sub").replace("{data}", T.data(dados["gerado_em"])))}</p>
  {grupos}
</div></section>

<section id="fluxo"><div class="wrap">
  <span class="chip">{e(T("ui.fluxo_chip"))}</span>
  <h2>{e(T("ui.fluxo_h2"))}</h2>
  <p class="sub">{e(T("ui.fluxo_sub"))}</p>
  <div class="flow">{fluxo}</div>
</div></section>

<section id="guia"><div class="wrap">
  <span class="chip">{e(T("ui.guia_chip"))}</span>
  <h2>{e(T("ui.guia_h2"))}</h2>
  <p class="sub">{e(T("ui.guia_sub"))}</p>
  {passos}
</div></section>

<footer>
  <div class="wrap">
    <div class="pill">Python 3</div><div class="pill">JSON</div><div class="pill">GitHub Pages</div>
    <p style="margin-top:18px">{SLUG} · {e(T("ui.rodape"))} · <a href="{REPO}">{repo_curto(REPO)}</a> · <a href="https://inema.club">INEMA.CLUB</a></p>
  </div>
</footer>

<script>
  (function(){{
    var KEY='{SLUG}-theme', b=document.body, t=document.getElementById('themeToggle');
    try{{ if(localStorage.getItem(KEY)==='light'){{ b.classList.add('light'); t.textContent='☀️'; }} }}catch(err){{}}
    t.addEventListener('click',function(){{
      var light=b.classList.toggle('light');
      t.textContent=light?'☀️':'🌙';
      try{{ localStorage.setItem(KEY, light?'light':'dark'); }}catch(err){{}}
    }});
  }})();
</script>
</body>
</html>
"""


# ───────────────────────────── README ─────────────────────────────
def readme(lang, dados, pt, trad):
    T = Txt(lang, pt, trad)
    url = PAGES if lang == "pt" else f"{PAGES}{lang}/"
    sufixo = "" if lang == "pt" else f"-{lang}"
    h_oque = {"pt": "O que é", "en": "What it is", "es": "Qué es"}[lang]
    L = [f"# {SLUG}", "", f"[![{SLUG}](guia/assets/banner{sufixo}.jpg)]({url})", "", pt["readme"]["seletor"], "",
         f"## {h_oque}", "", T("ui.resumo"), "",
         f"## {T('readme.h_guia')}", "", T("readme.guia_txt").replace("{url}", url), "",
         f"## {T('readme.h_motores')}", "",
         T("ui.mot_sub").replace("{data}", T.data(dados["gerado_em"])), ""]
    for g in dados["grupos"]:
        ms = [m for m in dados["motores"] if m["grupo"] == g["id"]]
        if not ms:
            continue
        L += [f"### {T.grupo(g)}", ""]
        for m in ms:
            L += [f"#### {m.get('emoji', '')} {T.motor(m, 'nome')}", "", T.motor(m, "oque"), ""]
            for k, campo in (("ui.l_serve", "serve"), ("ui.l_formato", "formato"), ("ui.l_avatar", "avatar"), ("ui.l_acion", "acionamento")):
                v = T.motor(m, campo)
                if v and v != "—":
                    L.append(f"- **{T(k)}:** {v}")
            repo = f"[{repo_curto(m['repo'])}]({m['repo']})" if m.get("repo") else T("ui.privado")
            for extra in m.get("repo_extra") or []:
                repo += f" · {extra['nome']}: " + (f"[{repo_curto(extra['url'])}]({extra['url']})" if extra.get("url") else T("ui.privado"))
            L.append(f"- **{T('ui.l_repo')}:** {repo}")
            ex = m.get("exemplos") or []
            if ex:
                L.append(f"- **{T('ui.l_ex')}:**")
                for x in ex:
                    L.append(f"  - [{x['titulo'].replace('[', '(').replace(']', ')')}]({x['url']}) — {x['canal_nome']}, {T.data(x['data'])}, {x['formato']}")
            nota = T.motor(m, "nota_exemplos")
            if nota:
                L.append(f"- {nota}")
            elif 0 < len(ex) < 3:
                L.append(f"- {T('ui.menos_ex').replace('{k}', str(len(ex)))}")
            L.append("")
    L += [f"## {T('readme.h_processo')}", "", T("readme.processo_legenda"), ""]
    for i, (quem, txt) in enumerate(T.lista("readme.processo"), 1):
        L.append(f"{i}. {quem} {txt}")
    L += ["", T("readme.processo_nota"), "", f"## {T('readme.h_arquivos')}", "", "| | |", "|---|---|"]
    for arq, txt in T.lista("readme.arquivos"):
        L.append(f"| `{arq}` | {txt} |")
    L += ["", f"## {T('readme.h_licenca')}", "", T("readme.licenca"), ""]
    return "\n".join(L)


def main():
    dados, pt, trad = carregar()
    for lang in LANGS:
        pasta = os.path.join(AQUI, "guia") if lang == "pt" else os.path.join(AQUI, "guia", lang)
        os.makedirs(pasta, exist_ok=True)
        with open(os.path.join(pasta, "index.html"), "w", encoding="utf-8") as f:
            f.write(guia(lang, dados, pt, trad))
        nome = "README.md" if lang == "pt" else f"README.{lang}.md"
        with open(os.path.join(AQUI, nome), "w", encoding="utf-8") as f:
            f.write(readme(lang, dados, pt, trad))
    for lang, faltas in FALTAS.items():
        if faltas:
            print(f"aviso: {lang} sem tradução para {len(faltas)} textos (rode python3 traduzir.py): {sorted(faltas)[:5]}")
    print("gerados: README.md, README.en.md, README.es.md, guia/index.html, guia/en/, guia/es/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
