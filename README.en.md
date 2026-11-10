# motores-de-video

[![motores-de-video](guia/assets/banner-en.jpg)](https://inematds.github.io/motores-de-video/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

This repository is an index. It explains, on one page, each engine INEMA uses to make videos: explainers, reels, daily radar updates, and videos made with code. Use it to find the right engine or learn about one. Each engine entry explains what it does, what kind of video it is for, its format, whether it uses an avatar, how it is triggered, links to its code, and up to 3 real videos published on YouTube. You don’t need to install anything to read it.

## 📖 User guide

Full page (engines in cards, with videos): **https://inematds.github.io/motores-de-video/guia/en/**

## The engines

Examples updated on 2026-11-09. Links come from the publication history and open on YouTube.

### Explainers with an avatar

#### 🎬 explicavideos (explicavideo)

The base engine for explainer videos: the script becomes scenes with illustrations, chapters, and captions, while Nei's avatar speaks the text. It has a viral profile, with a strong opening hook and striking images.

- **Best for:** Explain a topic, tool, or INEMA project, from a long video to a short clip.
- **Format:** 16:9 and 9:16
- **Avatar:** Yes — Nei's avatar and voice from the HeyGen studio (there is also a version without an avatar, using a local voice)
- **How it is triggered:** Terminal (agent session) or bot: /explicavideo <assunto> in inemaccbot
- **Repository:** [github.com/inematds/explicavideos](https://github.com/inematds/explicavideos)
- **Published examples:**
  - [Esqueça todas as IAs: chegou o novo rei — Claude Fable 5.2 nos números: custo, esforço #shorts](https://www.youtube.com/watch?v=cgZSgxjXaWs) — INEMA Tec, 2026-11-09, 9:16
  - [Seu time de bots pela assinatura que você já paga: 193 de 193 testes, sem API (kit grátis)](https://www.youtube.com/watch?v=lA9BHfoVZDo) — INEMA FTD, 2026-11-09, 16:9
  - [Do chat ao agente em 4 degraus: aprenda do zero, ainda em 2026, sem programar #shorts](https://www.youtube.com/watch?v=FSf-jUT_n6U) — INEMA TDS, 2026-11-09, 9:16

#### 🔁 refazvideo

A step-by-step process for an AI agent to remake a reference video as its own explainer in Portuguese: it downloads and transcribes the video, writes a new script, shows a preview, and only generates the avatar after you say "go ahead".

- **Best for:** Explain a topic from a good video in Portuguese, without filming yourself.
- **Format:** 16:9 and 9:16
- **Avatar:** Yes — Nei's avatar and voice (HeyGen); rendered with explicavideos
- **How it is triggered:** Terminal (agent session), with a preview and approval before generating the avatar
- **Repository:** [github.com/inematds/refazvideo](https://github.com/inematds/refazvideo)
- **Published examples:**
  - [IA sem censura: como funciona, onde usar e quanto custa](https://www.youtube.com/watch?v=ZsnxZmxcOSQ) — INEMA Tec, 2026-11-09, 16:9
  - [Como criar agentes de IA que aprendem com os próprios erros](https://www.youtube.com/watch?v=bnLvmYcP4PI) — INEMA FTD, 2026-11-08, 16:9
  - [MovieFlow: uma frase vira um filme (13 modelos de IA) #shorts](https://www.youtube.com/watch?v=WizdRuVKl1U) — INEMA FTD, 2026-11-06, 9:16

#### 🗺️ r7exp

A visual explainer that teaches options: a chart that works like a map, the same person moving through each scenario, panels that appear in time with the spoken words, and, at the end, what you can do.

- **Best for:** Topics with different paths or scenarios ("which future", "which choice"), where each option needs an explanation.
- **Format:** Full 16:9 video + one 9:16 reel per option
- **Avatar:** Yes — Nei's avatar (half-screen at the start, then in the corner)
- **How it is triggered:** Terminal (agent session); engine still in prototype
- **Repository:** [github.com/inematds/r7exp](https://github.com/inematds/r7exp)
- **Published examples:**
  - [A IA descobre. E você? #shorts](https://www.youtube.com/watch?v=0aE_BstdJkY) — INEMA Futuros, 2026-11-04, 9:16
  - [A IA resolveu 100 anos de ciência? As 3 descobertas explicadas no mapa](https://www.youtube.com/watch?v=PJIsN8MMHVE) — INEMA Futuros, 2026-10-29, 16:9
  - [PHP2Shell: seu site está exposto? Veja como se proteger](https://www.youtube.com/watch?v=YkqpuErgrqE) — INEMA TDS, 2026-10-23, 16:9

#### 🌎 Video translation EN/ES

Adapts a finished video into English and Spanish in the same format as the Portuguese version: the script and cues are translated by the central translator, Nei’s avatar and voice speak the new language, and explicavideos handles the edit. In Spanish, each video joins a queue that publishes gradually on the Inema Espanhol channel.

- **Best for:** EN/ES versions of explainers, reels, and lessons.
- **Format:** 16:9 and 9:16 (same as the original)
- **Avatar:** Yes — Nei’s avatar and voice in the target language
- **How it is triggered:** Terminal (session) + fila-espanhol with a timer (1 video every 2 h, up to 8 per day)
- **Repository:** [github.com/inematds/explicavideos](https://github.com/inematds/explicavideos) · fila-espanhol: private repository
- **Published examples:**
  - [REA: tu agente de IA sin trabas para adaptar programas en tu computadora](https://www.youtube.com/watch?v=S1uTys1xGnc) — Inema Espanhol, 2026-10-17, 16:9
  - [IA Cultivada: por qué tu IA repite errores y cómo hacer que mejore](https://www.youtube.com/watch?v=hzuNcPqHOEI) — Inema Espanhol, 2026-10-14, 16:9
  - [Codex + Claude: uno planifica, el otro critica #Shorts](https://www.youtube.com/watch?v=L3-LqTC_qeI) — Inema Espanhol, 2026-10-14, 9:16

### Viral 9:16 reels

#### ⚡ r7ex

A reel production line with a 7-step hook script, from an opening hook with a number to a request for comments, finished in a TV news style: a designed title at the opening, panels timed to the speech, a counter, and captions that light up with the voice.

- **Best for:** A viral 40 to 50 second reel based on a strong thesis or opinion.
- **Format:** 9:16
- **Avatar:** Yes — Nei on half-screen for the hook, then in the corner (HeyGen)
- **How it is triggered:** Terminal (/r7ex) or bot: /r7ex <tema> in inemaccbot; queued publishing with a timer
- **Repository:** [github.com/inematds/r7ex](https://github.com/inematds/r7ex)
- **Published examples:**
  - [Para de criar app de IA: os 13 negócios com IA do pior ao melhor #shorts](https://www.youtube.com/watch?v=9xtleXd3Kaw) — INEMA FTD, 2026-11-08, 9:16
  - [Seu prompt não é cadeado: 5 travas para o agente de IA #shorts](https://www.youtube.com/watch?v=CxjmcmF-GWg) — INEMA Tec, 2026-11-08, 9:16
  - [Ex-chefe do Google avisa: NÃO estamos prontos para a IA #shorts](https://www.youtube.com/watch?v=0VdykM91Gzw) — INEMA Futuros, 2026-11-08, 9:16

#### 🧩 rtex

An "N pieces" reel: one topic per video, a strong hook in the opening frame, the method's steps, and, at the end, an opinion question for the audience to answer. A validator, automated critic, and QA check the format before publishing.

- **Best for:** A method or list reel ("the 3 pieces of…") designed to prompt comments.
- **Format:** 9:16 (60–90 s)
- **Avatar:** Yes — Nei's avatar from the HeyGen studio
- **How it is triggered:** Terminal or bot: /rtex <tema> in inemaccbot; queued with a timer
- **Repository:** [github.com/inematds/rtex](https://github.com/inematds/rtex)
- **Published examples:**
  - [Seu design virou colagem: coloque critério antes do efeito #shorts](https://www.youtube.com/watch?v=DLPw-sI_TJI) — INEMA FTD, 2026-11-09, 9:16
  - [Pare de pedir slide assim pro Claude: 3 peças pra ter a sua cara #shorts](https://www.youtube.com/watch?v=mz2WjAoNwok) — INEMA Tec, 2026-11-06, 9:16
  - [Pare de disparar em volume para lista fria: prospecte por sinal com IA #shorts](https://www.youtube.com/watch?v=dydHb8BkkJk) — INEMA TDS, 2026-11-05, 9:16

#### 🖌️ rtexjp

Creates illustrated reels in navy blue from a roteiro.json script: generates the voice on the computer, draws each scene, mixes the soundtrack, and checks the format automatically. No recording and no paid avatar service.

- **Best for:** An rtex-style reel when there is no recorded avatar: everything is illustrated.
- **Format:** 9:16
- **Avatar:** Illustrated character of Nei (no HeyGen), local voice
- **How it is triggered:** Terminal or bot: /rtexjp <tema> in inemaccbot
- **Repository:** [github.com/inematds/rtexjp](https://github.com/inematds/rtexjp)
- **Published examples:**
  - [Você paga 200 dólares. A IA custa até 5 mil. #shorts](https://www.youtube.com/watch?v=UKqxVXTDVfI) — INEMA TDS, 2026-11-05, 9:16
  - [E se a China fechar a torneira da IA grátis? #shorts](https://www.youtube.com/watch?v=78O5l2Coiv4) — INEMA TDS, 2026-11-05, 9:16
- For now, only 2 examples were found in the history.

#### 7️⃣ reel7etapas (predecessor to r7ex)

The first 7-step hook reel model (hook, desire, fear, ease, discovery, benefit, comment), with one image per step and editing in Python. Since 18/10/2026, r7ex has been the standard; the repository keeps the old engine and its history.

- **Best for:** A reference for the 7-step script; new reels are made with r7ex.
- **Format:** 9:16
- **Avatar:** Yes — Nei’s avatar (HeyGen)
- **How it is triggered:** Terminal (/reel7etapas) — replaced by r7ex
- **Repository:** [github.com/inematds/reel7etapas](https://github.com/inematds/reel7etapas)
- **Published examples:**
  - [Vem aí demissão em massa de gerentes? A IA vai cobrar preparo #shorts](https://www.youtube.com/watch?v=xpDV5qQe5oE) — INEMA FTD, 2026-10-18, 9:16
- Older engine: this example shows the previous format, which led to r7ex. To see the current format, check the r7ex examples.

### Automated daily radar reports

#### 💰 finviral

Reviews videos from leading finance influencers using transcripts, separates figures, facts, and controversies, then creates a video with large animated numbers, the source of each figure on screen, and commentary from Nei. No investment recommendations.

- **Best for:** Daily summary of finance discussions; “The week explained” on weekends.
- **Format:** Daily 9:16 + long 16:9 video on weekends
- **Avatar:** Yes — Nei commenting (HeyGen)
- **How it is triggered:** Timer: Monday to Friday at 02:00, weekly recap on Saturday
- **Repository:** [github.com/inematds/finviral](https://github.com/inematds/finviral)
- **Published examples:**
  - [US$ 3 trilhões somem de Wall Street: a bolha da IA vai estourar?](https://www.youtube.com/watch?v=lVnzzTdXz9I) — INEMA TIA, 2026-11-09, 9:16
  - [Selic parada em 13,75%: o que esperar até dezembro, explicado](https://www.youtube.com/watch?v=pZ2ZCs_Udyo) — INEMA TIA, 2026-11-08, 16:9
  - [Financiamento de imóvel vai de 11% a 15% após a eleição: o que muda](https://www.youtube.com/watch?v=4x2j7Xbq5ng) — INEMA TIA, 2026-11-06, 9:16

#### 🩺 saudeviral

The same radar for doctors, nutritionists, and psychologists with the largest audiences: everything is reported and attributed, and topics without medical consensus are labeled “NO CONSENSUS.” Does not replace a medical consultation.

- **Best for:** Daily summary of what health influencers said.
- **Format:** Daily 9:16 + long 16:9 video on weekends
- **Avatar:** Yes — Nei commenting (HeyGen)
- **How it is triggered:** Timer: Monday to Friday at 05:00, weekly recap on Saturday
- **Repository:** [github.com/inematds/saudeviral](https://github.com/inematds/saudeviral)
- **Published examples:**
  - [Seu tipo sanguíneo muda o risco de câncer? O radar da saúde](https://www.youtube.com/watch?v=fN8iKWuTbmg) — INEMA TIA, 2026-11-09, 9:16
  - [Borderline, luto do vivo e 1.800 degraus | A semana explicada](https://www.youtube.com/watch?v=xgvdLWqTtQw) — INEMA TIA, 2026-11-08, 16:9
  - [Luto de quem está vivo, borderline e a gema do ovo: a semana da saúde](https://www.youtube.com/watch?v=BC4_4tpDUYE) — INEMA TIA, 2026-11-08, 9:16

#### ⚖️ advviral

Tracks what leading YouTube lawyers say about rights: consumer, social security, employment, debt, property, family, and scams. Nothing is presented as advice for your specific case, and proposed laws are clearly labeled as proposals.

- **Best for:** Daily summary of rights in plain language.
- **Format:** Daily 9:16 + long 16:9 video on weekends
- **Avatar:** Yes — Nei commenting (HeyGen)
- **How it is triggered:** Timer: Monday to Friday at 08:00, weekly recap on Saturday
- **Repository:** [github.com/inematds/advviral](https://github.com/inematds/advviral)
- **Published examples:**
  - [Processos contra o INSS mais que dobraram: por que tanta gente vai à Justiça](https://www.youtube.com/watch?v=TE9-6B4NbxM) — INEMA TIA, 2026-11-09, 9:16
  - [Ataque hacker de US$ 49 mi à cripto: quem paga? | A semana explicada](https://www.youtube.com/watch?v=glv2cyDDECc) — INEMA TIA, 2026-11-08, 16:9
  - [Aposentadoria com 15 anos paga só 60% da média, e mais 4 direitos](https://www.youtube.com/watch?v=pB4iDtByzyc) — INEMA TIA, 2026-11-07, 16:9

#### ⚽ futviral

Summarizes what the 10 largest football channels said: Brasileirão, European football, transfers, and business, with labels (RUMOR, IN NEGOTIATIONS, CONFIRMED, CONTROVERSY). Rumors are treated as rumors, and betting is excluded.

- **Best for:** Daily football radar.
- **Format:** Daily 9:16 + long 16:9 video on weekends
- **Avatar:** Yes — Nei commenting (HeyGen)
- **How it is triggered:** Timer: generates at 9 a.m., publishes at noon
- **Repository:** [github.com/inematds/futviral](https://github.com/inematds/futviral)
- **Published examples:**
  - [Grêmio na zona de rebaixamento e na final de R$ 78 milhões](https://www.youtube.com/watch?v=7VM2auexshA) — Inema Club24, 2026-11-09, 9:16
  - [FUTVIRAL: Flamengo pode ser campeão no Allianz e Vasco decide hoje](https://www.youtube.com/watch?v=d-J-JeG8dTU) — Inema Club24, 2026-11-08, 9:16
  - [Flamengo a 2 vitórias do título no Allianz? A semana explicada](https://www.youtube.com/watch?v=aVWqhfVehwA) — Inema Club24, 2026-11-08, 16:9

#### 🧾 contaviral

Summarizes what the 10 largest accounting and tax channels said: laws and regulations, Tax Reform, MEI and Simples, income tax, and tax obligations, with labels (RULE CHANGED, PROPOSAL, DEADLINE, ALERT).

- **Best for:** Daily accounting and tax radar.
- **Format:** Daily 9:16 + long 16:9 video on weekends
- **Avatar:** Yes — Nei commenting (HeyGen)
- **How it is triggered:** Timer: generates at 10 a.m., publishes at 1 p.m.
- **Repository:** [github.com/inematds/contaviral](https://github.com/inematds/contaviral)
- **Published examples:**
  - [Perdão do MEI: quem parcelou pode parar? E o Seletivo só em fevereiro](https://www.youtube.com/watch?v=0EG5d9CgNLo) — INEMA TIA, 2026-11-09, 9:16
  - [CBS a 11,34%? A alíquota que assustou e o que mais mudou na semana](https://www.youtube.com/watch?v=noBpqjKgdNQ) — INEMA TIA, 2026-11-08, 9:16
  - [CBS de 11,34%, inflação e perdão do MEI: a semana contábil explicada](https://www.youtube.com/watch?v=qsYlEy48vaY) — INEMA TIA, 2026-11-08, 16:9

### Other lines and series

#### 🌪️ eventosextremospub (weather)

Turns severe weather alerts into a “crisis room” video: downloads public data (INMET alerts by municipality, GOES-19 satellite data, Open-Meteo forecasts), animates it all on a 3D map of southern Brazil, and shows the source of every figure.

- **Best for:** Daily weather, forecasts, and weekly alerts.
- **Format:** 9:16
- **Avatar:** Yes — Nei through the HeyGen studio
- **How it is triggered:** Timers throughout the day (Weather 24 h, Daily Forecast, Weather of the DAY, alerts)
- **Repository:** [github.com/inematds/eventosextremospub](https://github.com/inematds/eventosextremospub)
- **Published examples:**
  - [O clima no mundo 09/11: duna cai sobre barracas em Gaza, enxurrada no Iraque #Shorts](https://www.youtube.com/watch?v=i11SMouAllE) — Eventos Extremos INEMA, 2026-11-09, 9:16
  - [654 cidades em alerta de tempestade amanhã · Alerta da semana 09/11 #Shorts](https://www.youtube.com/watch?v=E8xsGn0xRXQ) — Eventos Extremos INEMA, 2026-11-09, 9:16
  - [Clima do dia 09/11: geada em novembro e 0,8 °C na serra catarinense #Shorts](https://www.youtube.com/watch?v=eN05Dt_jM0M) — Eventos Extremos INEMA, 2026-11-09, 9:16

#### 👀 Channel Watcher

Checks a reference channel every day. If there is a new video, it creates an explainer video inspired by the content, in Nei’s voice, and publishes it directly. If there is no new video, it does nothing and never repeats a video.

- **Best for:** Automatic explainers whenever new content appears in the reference, without anyone asking.
- **Format:** 16:9 + 9:16 (under 2 min)
- **Avatar:** Yes — Nei’s avatar and voice
- **How it is triggered:** Daily timer at 14:00
- **Repository:** private repository
- **Published examples:**
  - [5 palavras e o projeto no ar: por que o prompt curto funciona melhor #shorts](https://www.youtube.com/watch?v=Lw-LdQiyUpA) — INEMA LOOPY, 2026-11-07, 9:16
  - [Prompt de 5 palavras e zero código: 7 hábitos de quem está no topo da IA](https://www.youtube.com/watch?v=T6d1k8fgVHQ) — INEMA LOOPY, 2026-11-07, 16:9
  - [A IA desligou 25 apps da TV e achou um minerador escondido: 3 usos que quase ninguém faz](https://www.youtube.com/watch?v=hageCcHOcLE) — INEMA LOOPY, 2026-11-06, 9:16

#### 🏙️ historia-timelapse

A 3D timelapse of a city’s history: real terrain, OpenStreetMap buildings appearing in the year the neighborhood was first occupied, an IBGE population counter, and cards with figures, explanations, and sources.

- **Best for:** City history in video, released in phases (music only, narrated, with avatar).
- **Format:** 16:9
- **Avatar:** Optional — phase 3 with Nei’s avatar
- **How it is triggered:** Terminal (skill historia-timelapse); publishing queue
- **Repository:** [github.com/inematds/historia-timelapse](https://github.com/inematds/historia-timelapse)
- **Published examples:**
  - [Porto Alegre de 1772 a 2024: 252 anos em um timelapse 3D com luz realista](https://www.youtube.com/watch?v=WzPVdaal1OY) — Aventuras INEMA, 2026-10-24, 16:9
  - [O centro de Itaguaí em 3D: da Matriz de 1729 à cidade do futuro](https://www.youtube.com/watch?v=dalR1xWPFlE) — Aventuras INEMA, 2026-10-23, 16:9
  - [Rio de Janeiro de 1500 a 2024: 524 anos de história em timelapse 3D](https://www.youtube.com/watch?v=Ij4KsTN_SB0) — Aventuras INEMA, 2026-10-23, 16:9

#### 🏔️ aventurasinemavideo (Adventure Memories)

Turns real stories from the INEMA Aventura archive (2001 to 2012), using adventurers’ own accounts and photos, into narrated films lasting 1 to 3 minutes: restored photos with motion and narration in Nei’s voice.

- **Best for:** The Adventure Memories series.
- **Format:** 16:9
- **Avatar:** No — archive photos + narration
- **How it is triggered:** Terminal / batch, with publishing to the Aventuras INEMA channel
- **Repository:** [github.com/inematds/aventurasinemavideo](https://github.com/inematds/aventurasinemavideo)
- **Published examples:**
  - [Beto Monteiro vence sob calor de 35°C na Fórmula Truck | Memórias de Aventura #166](https://www.youtube.com/watch?v=vjsykS5_9HU) — Aventuras INEMA, 2026-11-09, 16:9
  - [Allam Khodair: de 4º a vencedor na Stock Car 2010 | Memórias de Aventura #165](https://www.youtube.com/watch?v=PLPcwWAQgqE) — Aventuras INEMA, 2026-11-09, 16:9
  - [De Curitiba ao Alasca de moto: 34 mil km em 1997 | Memórias de Aventura #164](https://www.youtube.com/watch?v=iqrvHLIET2Y) — Aventuras INEMA, 2026-11-09, 16:9

#### 🔥 gitbombando

Every day, it makes the “Trending on GitHub” reel: the 10 projects that gained the most stars, in countdown order, with a card, the owner’s photo, a plain-English explanation, and the star count. It also creates two carousels.

- **Best for:** GitHub Trending updates in 1 minute.
- **Format:** 9:16
- **Avatar:** Yes — Nei’s avatar (HeyGen)
- **How it is triggered:** Timer: generates at 9:00, publishes at 11:00
- **Repository:** [github.com/inematds/gitbombando](https://github.com/inematds/gitbombando)
- **Published examples:**
  - [Caça-apelidos dispara ao topo do GitHub com +4.294 estrelas em um dia #Shorts](https://www.youtube.com/watch?v=W3Mds0R28_A) — INEMA Tec, 2026-11-09, 9:16
  - [Cloudflare segue no topo e um caça-apelidos invade o pódio: +2.085 estrelas no GitHub #Shorts](https://www.youtube.com/watch?v=vXoQJMnVT1w) — INEMA Tec, 2026-11-08, 9:16
  - [17.100 estrelas em 7 dias: o controle remoto de todas as IAs lidera o GitHub #Shorts](https://www.youtube.com/watch?v=3FXsmsRC0YA) — INEMA Tec, 2026-11-08, 9:16

### Videos made with code (no camera)

#### 💻 video-codigo

A skill for Claude Code and Codex where every frame is written in code (HTML, Canvas, or SVG) and turned into an MP4. When there is a voiceover, it is generated on the computer, and each image appears at the exact moment the word is spoken.

- **Best for:** A launch, announcement, explainer, or product film without a camera or editor.
- **Format:** 16:9 and 9:16 from the same project
- **Avatar:** No (a face is optional, up to half the screen)
- **How it is triggered:** Terminal (skill in Claude Code or Codex)
- **Repository:** [github.com/inematds/video-codigo](https://github.com/inematds/video-codigo)
- **Published examples:**
  - [Lead que espera esfria: do WhatsApp à venda em 1 minuto, feito com código #Shorts](https://www.youtube.com/watch?v=4ILX66Hddtk) — INEMA FTD, 2026-11-06, 9:16
  - [Do WhatsApp à venda: filme de produto feito 100% com código](https://www.youtube.com/watch?v=tWv1mEIK62c) — INEMA FTD, 2026-11-06, 16:9
- For now, only 2 examples were found in the history.

#### 🪐 reel-ciencia-3d

A kit with a skill for Claude Code that turns an “What if…?” question into a science reel of about 60 seconds, made entirely with code (HyperFrames and Three.js), with a source for every figure and a locally generated voice.

- **Best for:** Short science videos, with accurate figures.
- **Format:** 9:16 (~60 s)
- **Avatar:** No
- **How it is triggered:** Terminal (skill in Claude Code)
- **Repository:** [github.com/inematds/reel-ciencia-3d](https://github.com/inematds/reel-ciencia-3d)
- **Published examples:**
  - [E se o Sol sumisse agora? Animação 3D feita só com código](https://www.youtube.com/watch?v=FDtJim4xHjY) — INEMA FTD, 2026-11-06, 9:16
  - [E se a Lua sumisse? Animação 3D feita só com código](https://www.youtube.com/watch?v=nUsGrdZ-8MY) — INEMA FTD, 2026-11-06, 9:16
  - [E se a Terra não tivesse inclinação? Animação 3D feita só com código](https://www.youtube.com/watch?v=BmSeV6r0FdQ) — INEMA FTD, 2026-11-06, 9:16

#### 🎙️ video-sem-rosto

A kit that teaches Claude Code to make landscape explainers without filming: cloned voice generated on your computer, the real website page, 3D images, and synced captions.

- **Best for:** Explain a tool, a repository, or a new release without appearing on camera.
- **Format:** 16:9
- **Avatar:** No
- **How it is triggered:** Terminal (skill in Claude Code)
- **Repository:** [github.com/inematds/video-sem-rosto](https://github.com/inematds/video-sem-rosto)
- No videos from this engine have been published on YouTube yet; demo videos are in the project guide.

#### 🎓 videos-cursos-inema

An engine that turns an INEMA course (static website) into a narrated, animated video series in three selectable parts: landing page, one video per learning path, and a complete lesson for each module.

- **Best for:** Promotional videos and lessons for a course.
- **Format:** 16:9 (and 9:16 with --vertical)
- **Avatar:** No — narration with a locally cloned voice
- **How it is triggered:** Terminal (videos-cursos-inema skill)
- **Repository:** [github.com/inematds/videos-cursos-inema](https://github.com/inematds/videos-cursos-inema)
- No videos from this engine appear in the publication history; the project guide shows the FEP course example.

### Support

#### 🔊 inemavox

A local AI voice suite used behind the scenes by all the engines: downloads videos, transcribes, generates speech (TTS), dubs, and trims, with models running on your graphics card and no API costs.

- **Best for:** Voice, transcription, downloads, and music/sound effects for the other engines.
- **How it is triggered:** Terminal (scripts) or local API
- **Repository:** [github.com/inematds/inemavox](https://github.com/inematds/inemavox)
- Support engine: it does not publish its own videos.

## The process, start to finish

🧠 = session with Nei · ⚙️ = script (no tokens used) · 🤖 = `claude -p`

1. 🧠 New engine or text change: edit `catalogo.json` (text in PT, video identification rule, `excluir`/`fixar`).
2. ⚙️ `python3 traduzir.py` — translates only new keys into EN/ES using the central `inema-traduz` translator, then writes `i18n/en.json` and `i18n/es.json`.
3. ⚙️ `python3 atualizar-exemplos.py` — reads the yt-pubx history (`~/.local/share/yt-pubx/historico.jsonl`) and, if available, the production log (separating explicavideo from refazvideo); selects up to 3 recent, varied public videos per engine and writes `motores.json`.
4. ⚙️ The same command runs `python3 gerar.py`, which regenerates `README.md`, `README.en.md`, `README.es.md`, `guia/index.html`, `guia/en/`, and `guia/es/` from `motores.json`.
5. 🧠 Check the page and README; `git push`. GitHub Pages (Actions) publishes from the `main` branch.

The examples are not checked again on YouTube: the script only reads local files. Add a rejected or replaced video to `excluir` in `catalogo.json`.

## Files

| | |
|---|---|
| `catalogo.json` | manually edited source: engine text, channels, identification rules |
| `motores.json` | index data generated by the script (engines + examples) |
| `atualizar-exemplos.py` | rereads the history and rewrites motores.json |
| `gerar.py` | generates the READMEs and guide from motores.json |
| `traduzir.py` | translates new text into EN/ES (inema-traduz) |
| `i18n/` | page and engine text in PT, EN, and ES |

## License

MIT. A project by [INEMA.CLUB](https://inema.club).
