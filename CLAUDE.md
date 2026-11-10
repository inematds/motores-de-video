# CLAUDE.md — motores-de-video

Índice explicado dos motores de vídeo do INEMA (repo público `inematds/motores-de-video`, guia em
https://inematds.github.io/motores-de-video/guia/). Não guarda código de motor nenhum.

## Regras

- **Fonte = `catalogo.json` + `i18n/pt.json`.** README PT/EN/ES e `guia/` são GERADOS (`gerar.py`); não editar à mão.
- **Fluxo:** editar `catalogo.json` → `python3 traduzir.py` (só chaves novas, pelo `inema-traduz`) → `python3 atualizar-exemplos.py` (relê o histórico do yt-pubx e roda o `gerar.py`) → conferir → commit + push.
- **Nada privado no repo:** o `motores.json` guarda só id, link, título, canal, data e formato do vídeo — nunca o caminho do MP4 de origem. Repo privado aparece como "repositório privado", sem link. Não citar fonte, autor ou canal de terceiros (o "Vigia de canal" fica com nome neutro; a regra que identifica os vídeos dele mora em `regras.locais.json`, fora do git).
- **Vitrine só com vídeo aprovado:** vídeo reprovado, refeito ou trocado entra em `excluir` do motor no `catalogo.json`; para escolher a dedo, `fixar`.
- **Autor dos commits:** `inematds <inematds@gmail.com>`. Publicar = `git push` (Pages por Actions; push de `.github/workflows` pelo remoto SSH).

## Self-learning

When I correct you, or you catch yourself making a mistake: before continuing, add the lesson as a one-line rule at the TOP of the Lessons section below, so it never happens again.

## Lessons

- Pasta de origem `output/explica-<id>` mistura explicavideo e refazvideo: separar pelo registro de produções (coluna Ferramenta), não pelo nome da pasta. (09/11/2026)
