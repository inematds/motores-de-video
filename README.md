# motores-de-video

[![motores-de-video](guia/assets/banner.jpg)](https://inematds.github.io/motores-de-video/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

Este repositório é um índice: ele explica, em uma página, cada motor que o INEMA usa para produzir vídeos — explicativos, reels, radares diários, vídeos feitos em código. Serve para quem quer saber qual motor usar, ou estudar um deles. Cada motor tem o que faz, para que tipo de vídeo serve, o formato, se usa avatar, como é acionado, o link do código e até 3 vídeos reais publicados no YouTube. Para ler, não precisa instalar nada.

## 📖 Guia de uso

Página completa (motores em cartões, com os vídeos): **https://inematds.github.io/motores-de-video/guia/**

## Os motores

Exemplos atualizados em 09/11/2026. Os links vêm do histórico de publicações e abrem no YouTube.

### Explicativos com avatar

#### 🎬 explicavideos (explicavideo)

Motor base dos vídeos explicativos: o roteiro vira cenas com ilustrações, capítulos e legenda, e o avatar do Nei fala o texto. Tem um perfil viral, com gancho na abertura e imagens de impacto.

- **Serve para:** Explicar um assunto, uma ferramenta ou um projeto do INEMA, do vídeo longo ao corte curto.
- **Formato:** 16:9 e 9:16
- **Avatar:** Sim — avatar e voz do Nei pelo estúdio HeyGen (há versão sem avatar, com voz local)
- **Como é acionado:** Terminal (sessão com o agente) ou bot: /explicavideo <assunto> no inemaccbot
- **Repositório:** [github.com/inematds/explicavideos](https://github.com/inematds/explicavideos)
- **Exemplos publicados:**
  - [Esqueça todas as IAs: chegou o novo rei — Claude Fable 5.2 nos números: custo, esforço #shorts](https://www.youtube.com/watch?v=cgZSgxjXaWs) — INEMA Tec, 09/11/2026, 9:16
  - [Seu time de bots pela assinatura que você já paga: 193 de 193 testes, sem API (kit grátis)](https://www.youtube.com/watch?v=lA9BHfoVZDo) — INEMA FTD, 09/11/2026, 16:9
  - [Do chat ao agente em 4 degraus: aprenda do zero, ainda em 2026, sem programar #shorts](https://www.youtube.com/watch?v=FSf-jUT_n6U) — INEMA TDS, 09/11/2026, 9:16

#### 🔁 refazvideo

Passo a passo para um agente de IA refazer um vídeo de referência como explicativo próprio, em português: baixa, transcreve, escreve um roteiro novo, mostra uma prévia e só gera o avatar depois do "pode fazer".

- **Serve para:** Explicar em português um assunto que apareceu num bom vídeo, sem gravar a si mesmo.
- **Formato:** 16:9 e 9:16
- **Avatar:** Sim — avatar e voz do Nei (HeyGen); renderiza no explicavideos
- **Como é acionado:** Terminal (sessão com o agente), com prévia e OK antes do avatar
- **Repositório:** [github.com/inematds/refazvideo](https://github.com/inematds/refazvideo)
- **Exemplos publicados:**
  - [IA sem censura: como funciona, onde usar e quanto custa](https://www.youtube.com/watch?v=ZsnxZmxcOSQ) — INEMA Tec, 09/11/2026, 16:9
  - [Como criar agentes de IA que aprendem com os próprios erros](https://www.youtube.com/watch?v=bnLvmYcP4PI) — INEMA FTD, 08/11/2026, 16:9
  - [MovieFlow: uma frase vira um filme (13 modelos de IA) #shorts](https://www.youtube.com/watch?v=WizdRuVKl1U) — INEMA FTD, 06/11/2026, 9:16

#### 🗺️ r7exp

Explicativo visual que ensina opções: um gráfico que funciona como mapa, a mesma pessoa atravessando cada cenário, painéis que entram na palavra falada e, no fim, o que você pode fazer.

- **Serve para:** Temas com caminhos ou cenários ("qual futuro", "qual escolha"), em que cada opção precisa ser explicada.
- **Formato:** 16:9 completo + um reel 9:16 por opção
- **Avatar:** Sim — avatar do Nei (meia tela no começo, depois no canto)
- **Como é acionado:** Terminal (sessão com o agente); motor ainda em protótipo
- **Repositório:** [github.com/inematds/r7exp](https://github.com/inematds/r7exp)
- **Exemplos publicados:**
  - [A IA descobre. E você? #shorts](https://www.youtube.com/watch?v=0aE_BstdJkY) — INEMA Futuros, 04/11/2026, 9:16
  - [A IA resolveu 100 anos de ciência? As 3 descobertas explicadas no mapa](https://www.youtube.com/watch?v=PJIsN8MMHVE) — INEMA Futuros, 29/10/2026, 16:9
  - [PHP2Shell: seu site está exposto? Veja como se proteger](https://www.youtube.com/watch?v=YkqpuErgrqE) — INEMA TDS, 23/10/2026, 16:9

#### 🌎 Tradução de vídeo EN/ES

Leva um vídeo pronto para inglês e espanhol no mesmo formato do português: roteiro e deixas traduzidos pelo tradutor central, avatar e voz do Nei no idioma novo, montagem no explicavideos. Em espanhol, cada vídeo entra numa fila que publica aos poucos no canal Inema Espanhol.

- **Serve para:** Versões EN/ES de explicativos, reels e aulas.
- **Formato:** 16:9 e 9:16 (igual ao original)
- **Avatar:** Sim — avatar e voz do Nei no idioma
- **Como é acionado:** Terminal (sessão) + fila-espanhol com timer (1 vídeo a cada 2 h, até 8 por dia)
- **Repositório:** [github.com/inematds/explicavideos](https://github.com/inematds/explicavideos) · fila-espanhol: repositório privado
- **Exemplos publicados:**
  - [REA: tu agente de IA sin trabas para adaptar programas en tu computadora](https://www.youtube.com/watch?v=S1uTys1xGnc) — Inema Espanhol, 17/10/2026, 16:9
  - [IA Cultivada: por qué tu IA repite errores y cómo hacer que mejore](https://www.youtube.com/watch?v=hzuNcPqHOEI) — Inema Espanhol, 14/10/2026, 16:9
  - [Codex + Claude: uno planifica, el otro critica #Shorts](https://www.youtube.com/watch?v=L3-LqTC_qeI) — Inema Espanhol, 14/10/2026, 9:16

### Reels virais 9:16

#### ⚡ r7ex

Linha de produção de reels com roteiro de 7 etapas de gatilho, do gancho com número ao pedido de comentário, e acabamento de telejornal: título desenhado na abertura, painéis no tempo da fala, contador e legenda que acende com a voz.

- **Serve para:** Reel viral de 40 a 50 segundos a partir de uma tese ou opinião forte.
- **Formato:** 9:16
- **Avatar:** Sim — Nei em meia tela no gancho, depois no canto (HeyGen)
- **Como é acionado:** Terminal (/r7ex) ou bot: /r7ex <tema> no inemaccbot; publicação por fila com timer
- **Repositório:** [github.com/inematds/r7ex](https://github.com/inematds/r7ex)
- **Exemplos publicados:**
  - [Para de criar app de IA: os 13 negócios com IA do pior ao melhor #shorts](https://www.youtube.com/watch?v=9xtleXd3Kaw) — INEMA FTD, 08/11/2026, 9:16
  - [Seu prompt não é cadeado: 5 travas para o agente de IA #shorts](https://www.youtube.com/watch?v=CxjmcmF-GWg) — INEMA Tec, 08/11/2026, 9:16
  - [Ex-chefe do Google avisa: NÃO estamos prontos para a IA #shorts](https://www.youtube.com/watch?v=0VdykM91Gzw) — INEMA Futuros, 08/11/2026, 9:16

#### 🧩 rtex

Reel de "N peças": um tema por vídeo, gancho forte no quadro de abertura, os passos do método e, no fim, uma pergunta de opinião para o público responder. Validador, crítico automático e QA conferem o formato antes de publicar.

- **Serve para:** Reel de método ou lista ("as 3 peças de…") que puxa comentário.
- **Formato:** 9:16 (60–90 s)
- **Avatar:** Sim — avatar do Nei pelo estúdio HeyGen
- **Como é acionado:** Terminal ou bot: /rtex <tema> no inemaccbot; fila com timer
- **Repositório:** [github.com/inematds/rtex](https://github.com/inematds/rtex)
- **Exemplos publicados:**
  - [Seu design virou colagem: coloque critério antes do efeito #shorts](https://www.youtube.com/watch?v=DLPw-sI_TJI) — INEMA FTD, 09/11/2026, 9:16
  - [Pare de pedir slide assim pro Claude: 3 peças pra ter a sua cara #shorts](https://www.youtube.com/watch?v=mz2WjAoNwok) — INEMA Tec, 06/11/2026, 9:16
  - [Pare de disparar em volume para lista fria: prospecte por sinal com IA #shorts](https://www.youtube.com/watch?v=dydHb8BkkJk) — INEMA TDS, 05/11/2026, 9:16

#### 🖌️ rtexjp

Monta reels ilustrados em azul-marinho a partir de um roteiro.json: gera a voz no próprio computador, desenha cada cena, mistura a trilha e confere sozinho o formato. Sem gravar e sem serviço de avatar pago.

- **Serve para:** Reel no padrão rtex quando não há avatar gravado: tudo ilustrado.
- **Formato:** 9:16
- **Avatar:** Personagem ilustrado do Nei (sem HeyGen), voz local
- **Como é acionado:** Terminal ou bot: /rtexjp <tema> no inemaccbot
- **Repositório:** [github.com/inematds/rtexjp](https://github.com/inematds/rtexjp)
- **Exemplos publicados:**
  - [Você paga 200 dólares. A IA custa até 5 mil. #shorts](https://www.youtube.com/watch?v=UKqxVXTDVfI) — INEMA TDS, 05/11/2026, 9:16
  - [E se a China fechar a torneira da IA grátis? #shorts](https://www.youtube.com/watch?v=78O5l2Coiv4) — INEMA TDS, 05/11/2026, 9:16
- Só 2 exemplo(s) identificado(s) no histórico.

#### 7️⃣ reel7etapas (antecessor do r7ex)

O primeiro modelo de reel em 7 etapas de gatilho (gancho, desejo, medo, facilidade, descoberta, benefício, comentário), com uma imagem por etapa e montagem em Python. Desde 18/10/2026 o padrão é o r7ex; o repositório guarda o motor antigo e o histórico.

- **Serve para:** Referência do roteiro de 7 etapas; reels novos saem pelo r7ex.
- **Formato:** 9:16
- **Avatar:** Sim — avatar do Nei (HeyGen)
- **Como é acionado:** Terminal (/reel7etapas) — substituído pelo r7ex
- **Repositório:** [github.com/inematds/reel7etapas](https://github.com/inematds/reel7etapas)
- **Exemplos publicados:**
  - [Sua empresa vai ter funcionário que não é gente: aprenda a gerir IA #shorts](https://www.youtube.com/watch?v=cMhIavjhdh0) — INEMA FTD, 18/10/2026, 9:16
  - [Seu agente de IA precisa aprender o seu jeito: conheça a regra 5-4-3](https://www.youtube.com/watch?v=J-ohqu_8V7o) — INEMA Tec, 18/10/2026, 9:16
  - [Como um Tesla poderia voar? Entenda a ideia dos propulsores de ar](https://www.youtube.com/watch?v=qWffH0fDNeE) — INEMA TDS, 17/10/2026, 9:16

### Radares diários automáticos

#### 💰 finviral

Assiste por transcrição aos vídeos dos maiores influenciadores de finanças, separa números, fatos e polêmicas e monta um vídeo com números grandes animados, a fonte de cada dado na tela e o Nei comentando. Sem recomendação de investimento.

- **Serve para:** Resumo diário do que se falou de finanças; no fim de semana, "A semana explicada".
- **Formato:** 9:16 diário + 16:9 longo no fim de semana
- **Avatar:** Sim — Nei comentando (HeyGen)
- **Como é acionado:** Timer: segunda a sexta 02:00, balanço no sábado
- **Repositório:** [github.com/inematds/finviral](https://github.com/inematds/finviral)
- **Exemplos publicados:**
  - [US$ 3 trilhões somem de Wall Street: a bolha da IA vai estourar?](https://www.youtube.com/watch?v=lVnzzTdXz9I) — INEMA TIA, 09/11/2026, 9:16
  - [Selic parada em 13,75%: o que esperar até dezembro, explicado](https://www.youtube.com/watch?v=pZ2ZCs_Udyo) — INEMA TIA, 08/11/2026, 16:9
  - [Financiamento de imóvel vai de 11% a 15% após a eleição: o que muda](https://www.youtube.com/watch?v=4x2j7Xbq5ng) — INEMA TIA, 06/11/2026, 9:16

#### 🩺 saudeviral

O mesmo radar para médicos, nutricionistas e psicólogos de maior audiência: tudo relatado e atribuído, e o que não tem consenso na medicina sai com o carimbo "SEM CONSENSO". Não substitui consulta médica.

- **Serve para:** Resumo diário do que os influenciadores de saúde disseram.
- **Formato:** 9:16 diário + 16:9 longo no fim de semana
- **Avatar:** Sim — Nei comentando (HeyGen)
- **Como é acionado:** Timer: segunda a sexta 05:00, balanço no sábado
- **Repositório:** [github.com/inematds/saudeviral](https://github.com/inematds/saudeviral)
- **Exemplos publicados:**
  - [Seu tipo sanguíneo muda o risco de câncer? O radar da saúde](https://www.youtube.com/watch?v=fN8iKWuTbmg) — INEMA TIA, 09/11/2026, 9:16
  - [Borderline, luto do vivo e 1.800 degraus | A semana explicada](https://www.youtube.com/watch?v=xgvdLWqTtQw) — INEMA TIA, 08/11/2026, 16:9
  - [US$ 16 bi em propaganda falsa? A semana da saúde explicada](https://www.youtube.com/watch?v=1BjYFTybiGY) — Saúde Diária, 24/10/2026, 16:9

#### ⚖️ advviral

Radar do que os maiores advogados do YouTube disseram sobre direitos: consumidor, previdência, trabalho, dívidas, imóvel, família e golpes. Nada vira conselho para o seu caso, e proposta de lei é chamada de proposta.

- **Serve para:** Resumo diário de direitos, em linguagem simples.
- **Formato:** 9:16 diário + 16:9 longo no fim de semana
- **Avatar:** Sim — Nei comentando (HeyGen)
- **Como é acionado:** Timer: segunda a sexta 08:00, balanço no sábado
- **Repositório:** [github.com/inematds/advviral](https://github.com/inematds/advviral)
- **Exemplos publicados:**
  - [Processos contra o INSS mais que dobraram: por que tanta gente vai à Justiça](https://www.youtube.com/watch?v=TE9-6B4NbxM) — INEMA TIA, 09/11/2026, 9:16
  - [Ataque hacker de US$ 49 mi à cripto: quem paga? | A semana explicada](https://www.youtube.com/watch?v=glv2cyDDECc) — INEMA TIA, 08/11/2026, 16:9
  - [Carro de leilão sem aviso: loja teve que dar 30% de desconto](https://www.youtube.com/watch?v=R7FmcEOA1jo) — Saúde Diária, 13/10/2026, 16:9

#### ⚽ futviral

Resumo do que os 10 maiores canais de futebol disseram: Brasileirão, futebol europeu, mercado da bola e negócios, com carimbos (RUMOR, NEGOCIANDO, FECHADO, POLÊMICA). Rumor é tratado como rumor e aposta não entra.

- **Serve para:** Radar diário de futebol.
- **Formato:** 9:16 diário + 16:9 longo no fim de semana
- **Avatar:** Sim — Nei comentando (HeyGen)
- **Como é acionado:** Timer: gera às 9h, publica ao meio-dia
- **Repositório:** [github.com/inematds/futviral](https://github.com/inematds/futviral)
- **Exemplos publicados:**
  - [Grêmio na zona de rebaixamento e na final de R$ 78 milhões](https://www.youtube.com/watch?v=7VM2auexshA) — Inema Club24, 09/11/2026, 9:16
  - [FUTVIRAL: Flamengo pode ser campeão no Allianz e Vasco decide hoje](https://www.youtube.com/watch?v=d-J-JeG8dTU) — Inema Club24, 08/11/2026, 9:16
  - [Flamengo a 2 vitórias do título no Allianz? A semana explicada](https://www.youtube.com/watch?v=aVWqhfVehwA) — Inema Club24, 08/11/2026, 16:9

#### 🧾 contaviral

Resumo do que os 10 maiores canais de contabilidade e tributos disseram: leis e portarias, Reforma Tributária, MEI e Simples, imposto de renda e obrigações fiscais, com carimbos (MUDOU A REGRA, PROPOSTA, PRAZO, ALERTA).

- **Serve para:** Radar diário contábil e tributário.
- **Formato:** 9:16 diário + 16:9 longo no fim de semana
- **Avatar:** Sim — Nei comentando (HeyGen)
- **Como é acionado:** Timer: gera às 10h, publica às 13h
- **Repositório:** [github.com/inematds/contaviral](https://github.com/inematds/contaviral)
- **Exemplos publicados:**
  - [Perdão do MEI: quem parcelou pode parar? E o Seletivo só em fevereiro](https://www.youtube.com/watch?v=0EG5d9CgNLo) — INEMA TIA, 09/11/2026, 9:16
  - [CBS a 11,34%? A alíquota que assustou e o que mais mudou na semana](https://www.youtube.com/watch?v=noBpqjKgdNQ) — INEMA TIA, 08/11/2026, 9:16
  - [CBS de 11,34%, inflação e perdão do MEI: a semana contábil explicada](https://www.youtube.com/watch?v=qsYlEy48vaY) — INEMA TIA, 08/11/2026, 16:9

### Outras linhas automáticas

#### 🌪️ eventosextremospub (clima)

Transforma alertas de tempo severo num vídeo de "sala de crise": baixa dados públicos (alertas do INMET por município, satélite GOES-19, previsão do Open-Meteo), anima tudo num mapa 3D do Sul do Brasil e mostra a fonte de cada número.

- **Serve para:** Clima do dia, previsão e alertas da semana.
- **Formato:** 9:16
- **Avatar:** Sim — Nei pelo estúdio HeyGen
- **Como é acionado:** Timers ao longo do dia (Clima 24 h, Previsão do Dia, Clima do DIA, alertas)
- **Repositório:** [github.com/inematds/eventosextremospub](https://github.com/inematds/eventosextremospub)
- **Exemplos publicados:**
  - [O clima no mundo 09/11: duna cai sobre barracas em Gaza, enxurrada no Iraque #Shorts](https://www.youtube.com/watch?v=i11SMouAllE) — Eventos Extremos INEMA, 09/11/2026, 9:16
  - [654 cidades em alerta de tempestade amanhã · Alerta da semana 09/11 #Shorts](https://www.youtube.com/watch?v=E8xsGn0xRXQ) — Eventos Extremos INEMA, 09/11/2026, 9:16
  - [Clima do dia 09/11: geada em novembro e 0,8 °C na serra catarinense #Shorts](https://www.youtube.com/watch?v=eN05Dt_jM0M) — Eventos Extremos INEMA, 09/11/2026, 9:16

#### 👀 Vigia de canal

Todo dia olha um canal de referência; se houver vídeo novo, faz um explicavideo inspirado no conteúdo, na voz do Nei, e publica direto. Sem vídeo novo, não faz nada, e nunca repete um vídeo.

- **Serve para:** Explicativos automáticos sobre agentes e automação com IA.
- **Formato:** 16:9 + 9:16 (menos de 2 min)
- **Avatar:** Sim — avatar e voz do Nei
- **Como é acionado:** Timer diário às 14h
- **Repositório:** repositório privado
- **Exemplos publicados:**
  - [5 palavras e o projeto no ar: por que o prompt curto funciona melhor #shorts](https://www.youtube.com/watch?v=Lw-LdQiyUpA) — INEMA LOOPY, 07/11/2026, 9:16
  - [Prompt de 5 palavras e zero código: 7 hábitos de quem está no topo da IA](https://www.youtube.com/watch?v=T6d1k8fgVHQ) — INEMA LOOPY, 07/11/2026, 16:9
  - [A IA desligou 25 apps da TV e achou um minerador escondido: 3 usos que quase ninguém faz](https://www.youtube.com/watch?v=hageCcHOcLE) — INEMA LOOPY, 06/11/2026, 9:16

#### 🏙️ historia-timelapse

Timelapse 3D da história de uma cidade: relevo real, prédios do OpenStreetMap nascendo no ano em que o bairro foi ocupado, contador de população do IBGE e cartões com número, explicação e fonte.

- **Serve para:** História de cidades em vídeo; sai em fases (só música, narrada, com avatar).
- **Formato:** 16:9
- **Avatar:** Opcional — fase 3 com avatar do Nei
- **Como é acionado:** Terminal (skill historia-timelapse); fila de publicação
- **Repositório:** [github.com/inematds/historia-timelapse](https://github.com/inematds/historia-timelapse)
- **Exemplos publicados:**
  - [Porto Alegre de 1772 a 2024: 252 anos em um timelapse 3D com luz realista](https://www.youtube.com/watch?v=WzPVdaal1OY) — Aventuras INEMA, 24/10/2026, 16:9
  - [O centro de Itaguaí em 3D: da Matriz de 1729 à cidade do futuro](https://www.youtube.com/watch?v=dalR1xWPFlE) — Aventuras INEMA, 23/10/2026, 16:9
  - [Rio de Janeiro de 1500 a 2024: 524 anos de história em timelapse 3D](https://www.youtube.com/watch?v=Ij4KsTN_SB0) — Aventuras INEMA, 23/10/2026, 16:9

#### 🏔️ aventurasinemavideo (Memórias de Aventura)

Transforma matérias reais do acervo do INEMA Aventura (2001 a 2012), com o relato e as fotos dos próprios aventureiros, em filmes narrados de 1 a 3 minutos: fotos restauradas com movimento e narração na voz do Nei.

- **Serve para:** A série Memórias de Aventura.
- **Formato:** 16:9
- **Avatar:** Não — fotos do acervo + narração
- **Como é acionado:** Terminal / lote, com publicação no canal Aventuras INEMA
- **Repositório:** [github.com/inematds/aventurasinemavideo](https://github.com/inematds/aventurasinemavideo)
- **Exemplos publicados:**
  - [Beto Monteiro vence sob calor de 35°C na Fórmula Truck | Memórias de Aventura #166](https://www.youtube.com/watch?v=vjsykS5_9HU) — Aventuras INEMA, 09/11/2026, 16:9
  - [Allam Khodair: de 4º a vencedor na Stock Car 2010 | Memórias de Aventura #165](https://www.youtube.com/watch?v=PLPcwWAQgqE) — Aventuras INEMA, 09/11/2026, 16:9
  - [De Curitiba ao Alasca de moto: 34 mil km em 1997 | Memórias de Aventura #164](https://www.youtube.com/watch?v=iqrvHLIET2Y) — Aventuras INEMA, 09/11/2026, 16:9

#### 🔥 gitbombando

Todo dia faz o reel "Bombando no GitHub": os 10 projetos que mais ganharam estrelas, em contagem regressiva, com cartão, foto do dono, o que faz em português simples e o número de estrelas. Também gera dois carrosséis.

- **Serve para:** Novidades do GitHub Trending em 1 minuto.
- **Formato:** 9:16
- **Avatar:** Sim — avatar do Nei (HeyGen)
- **Como é acionado:** Timer: gera às 9h, publica às 11h
- **Repositório:** [github.com/inematds/gitbombando](https://github.com/inematds/gitbombando)
- **Exemplos publicados:**
  - [Caça-apelidos dispara ao topo do GitHub com +4.294 estrelas em um dia #Shorts](https://www.youtube.com/watch?v=W3Mds0R28_A) — INEMA Tec, 09/11/2026, 9:16
  - [Cloudflare segue no topo e um caça-apelidos invade o pódio: +2.085 estrelas no GitHub #Shorts](https://www.youtube.com/watch?v=vXoQJMnVT1w) — INEMA Tec, 08/11/2026, 9:16
  - [17.100 estrelas em 7 dias: o controle remoto de todas as IAs lidera o GitHub #Shorts](https://www.youtube.com/watch?v=3FXsmsRC0YA) — INEMA Tec, 08/11/2026, 9:16

### Vídeo feito em código (sem câmera)

#### 💻 video-codigo

Skill para o Claude Code e o Codex em que cada quadro é escrito em código (HTML, Canvas ou SVG) e vira MP4. A voz, quando há, é gerada no computador e cada imagem entra no instante da palavra.

- **Serve para:** Lançamento, anúncio, explicativo ou filme de produto sem câmera e sem editor.
- **Formato:** 16:9 e 9:16 do mesmo projeto
- **Avatar:** Não (rosto opcional, até meia tela)
- **Como é acionado:** Terminal (skill no Claude Code ou Codex)
- **Repositório:** [github.com/inematds/video-codigo](https://github.com/inematds/video-codigo)
- **Exemplos publicados:**
  - [Lead que espera esfria: do WhatsApp à venda em 1 minuto, feito com código #Shorts](https://www.youtube.com/watch?v=4ILX66Hddtk) — INEMA FTD, 06/11/2026, 9:16
  - [Do WhatsApp à venda: filme de produto feito 100% com código](https://www.youtube.com/watch?v=tWv1mEIK62c) — INEMA FTD, 06/11/2026, 16:9
  - [Um filme feito só com código e música | INEMA.CLUB #Shorts](https://www.youtube.com/watch?v=3JmREUS97-o) — INEMA FTD, 06/11/2026, 9:16

#### 🪐 reel-ciencia-3d

Kit com skill para o Claude Code que transforma uma pergunta "E se…?" num reel de ciência de cerca de 60 segundos, feito só com código (HyperFrames e Three.js), com a fonte de cada número e voz local.

- **Serve para:** Divulgação científica em vídeo curto, sem errar número.
- **Formato:** 9:16 (~60 s)
- **Avatar:** Não
- **Como é acionado:** Terminal (skill no Claude Code)
- **Repositório:** [github.com/inematds/reel-ciencia-3d](https://github.com/inematds/reel-ciencia-3d)
- **Exemplos publicados:**
  - [E se o Sol sumisse agora? Animação 3D feita só com código](https://www.youtube.com/watch?v=FDtJim4xHjY) — INEMA FTD, 06/11/2026, 9:16
  - [E se a Lua sumisse? Animação 3D feita só com código](https://www.youtube.com/watch?v=nUsGrdZ-8MY) — INEMA FTD, 06/11/2026, 9:16
  - [E se a Terra não tivesse inclinação? Animação 3D feita só com código](https://www.youtube.com/watch?v=BmSeV6r0FdQ) — INEMA FTD, 06/11/2026, 9:16

#### 🎙️ video-sem-rosto

Kit que ensina o Claude Code a fazer explicativos na horizontal sem gravar nada: voz clonada gerada no computador, a página real do site, imagens 3D e legenda sincronizada.

- **Serve para:** Explicar uma ferramenta, um repositório ou uma novidade sem aparecer.
- **Formato:** 16:9
- **Avatar:** Não
- **Como é acionado:** Terminal (skill no Claude Code)
- **Repositório:** [github.com/inematds/video-sem-rosto](https://github.com/inematds/video-sem-rosto)
- Ainda sem vídeo publicado no YouTube por este motor; os vídeos de demonstração estão no guia do projeto.

#### 🎓 videos-cursos-inema

Motor que transforma um curso INEMA (site estático) numa série de vídeos narrados e animados, em três partes selecionáveis: landing, um vídeo por trilha e uma aula completa por módulo.

- **Serve para:** Vídeos de divulgação e aulas de um curso.
- **Formato:** 16:9 (e 9:16 com --vertical)
- **Avatar:** Não — narração com voz clonada local
- **Como é acionado:** Terminal (skill videos-cursos-inema)
- **Repositório:** [github.com/inematds/videos-cursos-inema](https://github.com/inematds/videos-cursos-inema)
- Nenhum vídeo deste motor aparece no histórico de publicações; o guia do projeto mostra o exemplo do curso FEP.

### Apoio

#### 🔊 inemavox

Suíte de voz com IA local que todos os motores usam por baixo: baixa vídeos, transcreve, gera voz (TTS), dubla e corta, com os modelos rodando na placa de vídeo, sem custo de API.

- **Serve para:** Voz, transcrição, download e música/efeitos para os outros motores.
- **Como é acionado:** Terminal (scripts) ou API local
- **Repositório:** [github.com/inematds/inemavox](https://github.com/inematds/inemavox)
- Motor de apoio: não publica vídeo próprio.

## O processo, do início ao fim

🧠 = sessão com o Nei · ⚙️ = script (sem gastar tokens) · 🤖 = `claude -p`

1. 🧠 Motor novo ou mudança de texto: editar `catalogo.json` (texto em PT, regra que identifica os vídeos, `excluir`/`fixar`).
2. ⚙️ `python3 traduzir.py` — traduz para EN/ES só as chaves novas, pelo tradutor central `inema-traduz`, e grava `i18n/en.json` e `i18n/es.json`.
3. ⚙️ `python3 atualizar-exemplos.py` — lê o histórico do yt-pubx (`~/.local/share/yt-pubx/historico.jsonl`) e, se existir, o registro de produções (separa explicavideo de refazvideo); escolhe até 3 vídeos públicos, recentes e variados por motor e grava `motores.json`.
4. ⚙️ O mesmo comando roda `python3 gerar.py`, que regrava `README.md`, `README.en.md`, `README.es.md` e `guia/index.html`, `guia/en/`, `guia/es/` a partir do `motores.json`.
5. 🧠 Conferir a página e o README; `git push`. O GitHub Pages (Actions) publica a partir da branch `main`.

Os exemplos não são reconferidos no YouTube: o script só lê arquivos locais. Vídeo reprovado ou trocado entra em `excluir` no `catalogo.json`.

## Arquivos

| | |
|---|---|
| `catalogo.json` | fonte editada à mão: textos dos motores, canais, regras de identificação |
| `motores.json` | dados do índice gerados pelo script (motores + exemplos) |
| `atualizar-exemplos.py` | relê o histórico e regrava o motores.json |
| `gerar.py` | gera os READMEs e o guia a partir do motores.json |
| `traduzir.py` | traduz os textos novos para EN/ES (inema-traduz) |
| `i18n/` | textos da página e dos motores em PT, EN e ES |

## Licença

MIT. Projeto do [INEMA.CLUB](https://inema.club).
