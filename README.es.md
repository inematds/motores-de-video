# motores-de-video

[![motores-de-video](guia/assets/banner-es.jpg)](https://inematds.github.io/motores-de-video/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Este repositorio es un índice: explica, en una página, cada motor que INEMA usa para producir videos: explicativos, reels, radares diarios y videos hechos con código. Sirve para quienes quieren saber qué motor usar o estudiar uno de ellos. Cada motor incluye qué hace, para qué tipo de video sirve, el formato, si usa avatar, cómo se activa, el enlace al código y hasta 3 videos reales publicados en YouTube. No hace falta instalar nada para leerlo.

## 📖 Guía de uso

Página completa (motores en tarjetas, con videos): **https://inematds.github.io/motores-de-video/guia/es/**

## Los motores

Ejemplos actualizados el 09/11/2026. Los enlaces vienen del historial de publicaciones y abren en YouTube.

### Explicativos con avatar

#### 🎬 explicavideos (explicavideo)

Motor base de los videos explicativos: el guion se convierte en escenas con ilustraciones, capítulos y subtítulos, y el avatar de Nei habla el texto. Tiene un perfil viral, con un gancho al inicio e imágenes impactantes.

- **Sirve para:** Explicar un tema, una herramienta o un proyecto del INEMA, desde un video largo hasta un clip corto.
- **Formato:** 16:9 y 9:16
- **Avatar:** Sí — avatar y voz de Nei a través del estudio HeyGen (hay una versión sin avatar, con voz local)
- **Cómo se activa:** Terminal (sesión con el agente) o bot: /explicavideo <assunto> en inemaccbot
- **Repositorio:** [github.com/inematds/explicavideos](https://github.com/inematds/explicavideos)
- **Ejemplos publicados:**
  - [Esqueça todas as IAs: chegou o novo rei — Claude Fable 5.2 nos números: custo, esforço #shorts](https://www.youtube.com/watch?v=cgZSgxjXaWs) — INEMA Tec, 09/11/2026, 9:16
  - [Seu time de bots pela assinatura que você já paga: 193 de 193 testes, sem API (kit grátis)](https://www.youtube.com/watch?v=lA9BHfoVZDo) — INEMA FTD, 09/11/2026, 16:9
  - [Do chat ao agente em 4 degraus: aprenda do zero, ainda em 2026, sem programar #shorts](https://www.youtube.com/watch?v=FSf-jUT_n6U) — INEMA TDS, 09/11/2026, 9:16

#### 🔁 refazvideo

Guía paso a paso para que un agente de IA rehaga un video de referencia como un explicativo propio, en portugués: lo descarga, lo transcribe, escribe un guion nuevo, muestra una vista previa y solo genera el avatar después del "puedes hacerlo".

- **Sirve para:** Explicar en portugués un tema que apareció en un buen video, sin grabarse.
- **Formato:** 16:9 y 9:16
- **Avatar:** Sí — avatar y voz de Nei (HeyGen); renderiza en explicavideos
- **Cómo se activa:** Terminal (sesión con el agente), con vista previa y aprobación antes del avatar
- **Repositorio:** [github.com/inematds/refazvideo](https://github.com/inematds/refazvideo)
- **Ejemplos publicados:**
  - [IA sem censura: como funciona, onde usar e quanto custa](https://www.youtube.com/watch?v=ZsnxZmxcOSQ) — INEMA Tec, 09/11/2026, 16:9
  - [Como criar agentes de IA que aprendem com os próprios erros](https://www.youtube.com/watch?v=bnLvmYcP4PI) — INEMA FTD, 08/11/2026, 16:9
  - [MovieFlow: uma frase vira um filme (13 modelos de IA) #shorts](https://www.youtube.com/watch?v=WizdRuVKl1U) — INEMA FTD, 06/11/2026, 9:16

#### 🗺️ r7exp

Explicativo visual que enseña opciones: un gráfico que funciona como mapa, la misma persona recorriendo cada escenario, paneles que aparecen en el momento de la palabra hablada y, al final, lo que puedes hacer.

- **Sirve para:** Temas con caminos o escenarios ("qué futuro", "qué elección"), donde hay que explicar cada opción.
- **Formato:** 16:9 completo + un reel 9:16 por opción
- **Avatar:** Sí — avatar de Nei (media pantalla al principio, después en una esquina)
- **Cómo se activa:** Terminal (sesión con el agente); motor aún en prototipo
- **Repositorio:** [github.com/inematds/r7exp](https://github.com/inematds/r7exp)
- **Ejemplos publicados:**
  - [A IA descobre. E você? #shorts](https://www.youtube.com/watch?v=0aE_BstdJkY) — INEMA Futuros, 04/11/2026, 9:16
  - [A IA resolveu 100 anos de ciência? As 3 descobertas explicadas no mapa](https://www.youtube.com/watch?v=PJIsN8MMHVE) — INEMA Futuros, 29/10/2026, 16:9
  - [PHP2Shell: seu site está exposto? Veja como se proteger](https://www.youtube.com/watch?v=YkqpuErgrqE) — INEMA TDS, 23/10/2026, 16:9

#### 🌎 Traducción de video EN/ES

Adapta un video listo al inglés y al español con el mismo formato que el portugués: guion e indicaciones traducidos por el traductor central, avatar y voz de Nei en el nuevo idioma, montaje en explicavideos. En español, cada video entra en una fila que publica poco a poco en el canal Inema Espanhol.

- **Sirve para:** Versiones EN/ES de explicativos, reels y clases.
- **Formato:** 16:9 y 9:16 (igual al original)
- **Avatar:** Sí — avatar y voz de Nei en el idioma
- **Cómo se activa:** Terminal (sesión) + fila-espanhol con temporizador (1 video cada 2 h, hasta 8 por día)
- **Repositorio:** [github.com/inematds/explicavideos](https://github.com/inematds/explicavideos) · fila-espanhol: repositorio privado
- **Ejemplos publicados:**
  - [REA: tu agente de IA sin trabas para adaptar programas en tu computadora](https://www.youtube.com/watch?v=S1uTys1xGnc) — Inema Espanhol, 17/10/2026, 16:9
  - [IA Cultivada: por qué tu IA repite errores y cómo hacer que mejore](https://www.youtube.com/watch?v=hzuNcPqHOEI) — Inema Espanhol, 14/10/2026, 16:9
  - [Codex + Claude: uno planifica, el otro critica #Shorts](https://www.youtube.com/watch?v=L3-LqTC_qeI) — Inema Espanhol, 14/10/2026, 9:16

### Reels virales 9:16

#### ⚡ r7ex

Línea de producción de reels con un guion de 7 etapas que activan al público, desde el gancho con un número hasta la invitación a comentar, y acabado de noticiero: título animado al inicio, paneles al ritmo de la voz, contador y subtítulos que se iluminan con la voz.

- **Sirve para:** Reel viral de 40 a 50 segundos a partir de una tesis o una opinión contundente.
- **Formato:** 9:16
- **Avatar:** Sí — Nei en media pantalla durante el gancho, después en una esquina (HeyGen)
- **Cómo se activa:** Terminal (/r7ex) o bot: /r7ex <tema> en inemaccbot; publicación por cola con temporizador
- **Repositorio:** [github.com/inematds/r7ex](https://github.com/inematds/r7ex)
- **Ejemplos publicados:**
  - [Para de criar app de IA: os 13 negócios com IA do pior ao melhor #shorts](https://www.youtube.com/watch?v=9xtleXd3Kaw) — INEMA FTD, 08/11/2026, 9:16
  - [Seu prompt não é cadeado: 5 travas para o agente de IA #shorts](https://www.youtube.com/watch?v=CxjmcmF-GWg) — INEMA Tec, 08/11/2026, 9:16
  - [Ex-chefe do Google avisa: NÃO estamos prontos para a IA #shorts](https://www.youtube.com/watch?v=0VdykM91Gzw) — INEMA Futuros, 08/11/2026, 9:16

#### 🧩 rtex

Reel de "N piezas": un tema por video, gancho fuerte en la escena inicial, los pasos del método y, al final, una pregunta de opinión para que el público responda. Un validador, un crítico automático y el control de calidad revisan el formato antes de publicar.

- **Sirve para:** Reel de método o lista ("las 3 piezas de…") que invita a comentar.
- **Formato:** 9:16 (60–90 s)
- **Avatar:** Sí — avatar de Nei a través del estudio HeyGen
- **Cómo se activa:** Terminal o bot: /rtex <tema> en inemaccbot; cola con temporizador
- **Repositorio:** [github.com/inematds/rtex](https://github.com/inematds/rtex)
- **Ejemplos publicados:**
  - [Seu design virou colagem: coloque critério antes do efeito #shorts](https://www.youtube.com/watch?v=DLPw-sI_TJI) — INEMA FTD, 09/11/2026, 9:16
  - [Pare de pedir slide assim pro Claude: 3 peças pra ter a sua cara #shorts](https://www.youtube.com/watch?v=mz2WjAoNwok) — INEMA Tec, 06/11/2026, 9:16
  - [Pare de disparar em volume para lista fria: prospecte por sinal com IA #shorts](https://www.youtube.com/watch?v=dydHb8BkkJk) — INEMA TDS, 05/11/2026, 9:16

#### 🖌️ rtexjp

Crea reels ilustrados en azul marino a partir de un roteiro.json: genera la voz en la propia computadora, dibuja cada escena, mezcla la música y revisa el formato automáticamente. Sin grabar y sin un servicio de avatar pago.

- **Sirve para:** Reel con el formato rtex cuando no hay un avatar grabado: todo ilustrado.
- **Formato:** 9:16
- **Avatar:** Personaje ilustrado de Nei (sin HeyGen), voz local
- **Cómo se activa:** Terminal o bot: /rtexjp <tema> en inemaccbot
- **Repositorio:** [github.com/inematds/rtexjp](https://github.com/inematds/rtexjp)
- **Ejemplos publicados:**
  - [Você paga 200 dólares. A IA custa até 5 mil. #shorts](https://www.youtube.com/watch?v=UKqxVXTDVfI) — INEMA TDS, 05/11/2026, 9:16
  - [E se a China fechar a torneira da IA grátis? #shorts](https://www.youtube.com/watch?v=78O5l2Coiv4) — INEMA TDS, 05/11/2026, 9:16
- Por ahora, solo se encontraron 2 ejemplos en el historial.

#### 7️⃣ reel7etapas (antecesor de r7ex)

El primer modelo de reel en 7 etapas para activar al público (gancho, deseo, miedo, facilidad, descubrimiento, beneficio, comentario), con una imagen por etapa y montaje en Python. Desde el 18/10/2026, el formato estándar es r7ex; el repositorio conserva el motor antiguo y el historial.

- **Sirve para:** Referencia del guion de 7 etapas; los reels nuevos se hacen con r7ex.
- **Formato:** 9:16
- **Avatar:** Sí — avatar de Nei (HeyGen)
- **Cómo se activa:** Terminal (/reel7etapas) — reemplazado por r7ex
- **Repositorio:** [github.com/inematds/reel7etapas](https://github.com/inematds/reel7etapas)
- **Ejemplos publicados:**
  - [Sua empresa vai ter funcionário que não é gente: aprenda a gerir IA #shorts](https://www.youtube.com/watch?v=cMhIavjhdh0) — INEMA FTD, 18/10/2026, 9:16
  - [Seu agente de IA precisa aprender o seu jeito: conheça a regra 5-4-3](https://www.youtube.com/watch?v=J-ohqu_8V7o) — INEMA Tec, 18/10/2026, 9:16
  - [Como um Tesla poderia voar? Entenda a ideia dos propulsores de ar](https://www.youtube.com/watch?v=qWffH0fDNeE) — INEMA TDS, 17/10/2026, 9:16

### Radares diarios automáticos

#### 💰 finviral

Analiza las transcripciones de los videos de los mayores influencers de finanzas, separa cifras, hechos y polémicas, y arma un video con cifras grandes animadas, la fuente de cada dato en pantalla y Nei comentando. Sin recomendaciones de inversión.

- **Sirve para:** Resumen diario de lo que se habló de finanzas; los fines de semana, "La semana explicada".
- **Formato:** 9:16 diario + 16:9 largo los fines de semana
- **Avatar:** Sí — Nei comentando (HeyGen)
- **Cómo se activa:** Temporizador: de lunes a viernes a las 02:00, balance el sábado
- **Repositorio:** [github.com/inematds/finviral](https://github.com/inematds/finviral)
- **Ejemplos publicados:**
  - [US$ 3 trilhões somem de Wall Street: a bolha da IA vai estourar?](https://www.youtube.com/watch?v=lVnzzTdXz9I) — INEMA TIA, 09/11/2026, 9:16
  - [Selic parada em 13,75%: o que esperar até dezembro, explicado](https://www.youtube.com/watch?v=pZ2ZCs_Udyo) — INEMA TIA, 08/11/2026, 16:9
  - [Financiamento de imóvel vai de 11% a 15% após a eleição: o que muda](https://www.youtube.com/watch?v=4x2j7Xbq5ng) — INEMA TIA, 06/11/2026, 9:16

#### 🩺 saudeviral

El mismo radar para médicos, nutricionistas y psicólogos con mayor audiencia: todo se reporta y se atribuye, y lo que no tiene consenso en medicina lleva el sello "SIN CONSENSO". No reemplaza una consulta médica.

- **Sirve para:** Resumen diario de lo que dijeron los influencers de salud.
- **Formato:** 9:16 diario + 16:9 largo los fines de semana
- **Avatar:** Sí — Nei comentando (HeyGen)
- **Cómo se activa:** Temporizador: de lunes a viernes a las 05:00, balance el sábado
- **Repositorio:** [github.com/inematds/saudeviral](https://github.com/inematds/saudeviral)
- **Ejemplos publicados:**
  - [Seu tipo sanguíneo muda o risco de câncer? O radar da saúde](https://www.youtube.com/watch?v=fN8iKWuTbmg) — INEMA TIA, 09/11/2026, 9:16
  - [Borderline, luto do vivo e 1.800 degraus | A semana explicada](https://www.youtube.com/watch?v=xgvdLWqTtQw) — INEMA TIA, 08/11/2026, 16:9
  - [US$ 16 bi em propaganda falsa? A semana da saúde explicada](https://www.youtube.com/watch?v=1BjYFTybiGY) — Saúde Diária, 24/10/2026, 16:9

#### ⚖️ advviral

Radar de lo que dijeron los mayores abogados de YouTube sobre derechos: consumidores, pensiones, trabajo, deudas, vivienda, familia y estafas. Nada se convierte en consejo para tu caso, y las propuestas de ley se identifican como propuestas.

- **Sirve para:** Resumen diario de derechos, en lenguaje sencillo.
- **Formato:** 9:16 diario + 16:9 largo los fines de semana
- **Avatar:** Sí — Nei comentando (HeyGen)
- **Cómo se activa:** Temporizador: de lunes a viernes a las 08:00, balance el sábado
- **Repositorio:** [github.com/inematds/advviral](https://github.com/inematds/advviral)
- **Ejemplos publicados:**
  - [Processos contra o INSS mais que dobraram: por que tanta gente vai à Justiça](https://www.youtube.com/watch?v=TE9-6B4NbxM) — INEMA TIA, 09/11/2026, 9:16
  - [Ataque hacker de US$ 49 mi à cripto: quem paga? | A semana explicada](https://www.youtube.com/watch?v=glv2cyDDECc) — INEMA TIA, 08/11/2026, 16:9
  - [Carro de leilão sem aviso: loja teve que dar 30% de desconto](https://www.youtube.com/watch?v=R7FmcEOA1jo) — Saúde Diária, 13/10/2026, 16:9

#### ⚽ futviral

Resumen de lo que dijeron los 10 mayores canales de fútbol: Brasileirão, fútbol europeo, mercado de fichajes y negocios, con sellos (RUMOR, EN NEGOCIACIÓN, CERRADO, POLÉMICA). Los rumores se tratan como rumores y no se incluyen apuestas.

- **Sirve para:** Radar diario de fútbol.
- **Formato:** 9:16 diario + 16:9 largo los fines de semana
- **Avatar:** Sí — Nei comentando (HeyGen)
- **Cómo se activa:** Temporizador: se genera a las 9 h, se publica al mediodía
- **Repositorio:** [github.com/inematds/futviral](https://github.com/inematds/futviral)
- **Ejemplos publicados:**
  - [Grêmio na zona de rebaixamento e na final de R$ 78 milhões](https://www.youtube.com/watch?v=7VM2auexshA) — Inema Club24, 09/11/2026, 9:16
  - [FUTVIRAL: Flamengo pode ser campeão no Allianz e Vasco decide hoje](https://www.youtube.com/watch?v=d-J-JeG8dTU) — Inema Club24, 08/11/2026, 9:16
  - [Flamengo a 2 vitórias do título no Allianz? A semana explicada](https://www.youtube.com/watch?v=aVWqhfVehwA) — Inema Club24, 08/11/2026, 16:9

#### 🧾 contaviral

Resumen de lo que dijeron los 10 mayores canales de contabilidad e impuestos: leyes y resoluciones, Reforma Tributaria, MEI y Simples, impuesto sobre la renta y obligaciones fiscales, con sellos (CAMBIÓ LA REGLA, PROPUESTA, PLAZO, ALERTA).

- **Sirve para:** Radar diario contable y tributario.
- **Formato:** 9:16 diario + 16:9 largo los fines de semana
- **Avatar:** Sí — Nei comentando (HeyGen)
- **Cómo se activa:** Temporizador: se genera a las 10 h, se publica a las 13 h
- **Repositorio:** [github.com/inematds/contaviral](https://github.com/inematds/contaviral)
- **Ejemplos publicados:**
  - [Perdão do MEI: quem parcelou pode parar? E o Seletivo só em fevereiro](https://www.youtube.com/watch?v=0EG5d9CgNLo) — INEMA TIA, 09/11/2026, 9:16
  - [CBS a 11,34%? A alíquota que assustou e o que mais mudou na semana](https://www.youtube.com/watch?v=noBpqjKgdNQ) — INEMA TIA, 08/11/2026, 9:16
  - [CBS de 11,34%, inflação e perdão do MEI: a semana contábil explicada](https://www.youtube.com/watch?v=qsYlEy48vaY) — INEMA TIA, 08/11/2026, 16:9

### Otras líneas y series

#### 🌪️ eventosextremospub (clima)

Convierte alertas de tiempo severo en un video de "sala de crisis": descarga datos públicos (alertas del INMET por municipio, satélite GOES-19, pronóstico de Open-Meteo), lo anima todo en un mapa 3D del sur de Brasil y muestra la fuente de cada cifra.

- **Sirve para:** Clima del día, pronóstico y alertas de la semana.
- **Formato:** 9:16
- **Avatar:** Sí — Nei desde el estudio HeyGen
- **Cómo se activa:** Temporizadores a lo largo del día (Clima 24 h, Pronóstico del Día, Clima del DÍA, alertas)
- **Repositorio:** [github.com/inematds/eventosextremospub](https://github.com/inematds/eventosextremospub)
- **Ejemplos publicados:**
  - [O clima no mundo 09/11: duna cai sobre barracas em Gaza, enxurrada no Iraque #Shorts](https://www.youtube.com/watch?v=i11SMouAllE) — Eventos Extremos INEMA, 09/11/2026, 9:16
  - [654 cidades em alerta de tempestade amanhã · Alerta da semana 09/11 #Shorts](https://www.youtube.com/watch?v=E8xsGn0xRXQ) — Eventos Extremos INEMA, 09/11/2026, 9:16
  - [Clima do dia 09/11: geada em novembro e 0,8 °C na serra catarinense #Shorts](https://www.youtube.com/watch?v=eN05Dt_jM0M) — Eventos Extremos INEMA, 09/11/2026, 9:16

#### 👀 Vigia de canal

Cada día revisa un canal de referencia; si hay un video nuevo, crea un video explicativo inspirado en el contenido, con la voz de Nei, y lo publica directamente. Si no hay video nuevo, no hace nada y nunca repite un video.

- **Sirve para:** Videos explicativos automáticos sobre agentes y automatización con IA.
- **Formato:** 16:9 + 9:16 (menos de 2 min)
- **Avatar:** Sí — avatar y voz de Nei
- **Cómo se activa:** Temporizador diario a las 14h
- **Repositorio:** repositorio privado
- **Ejemplos publicados:**
  - [5 palavras e o projeto no ar: por que o prompt curto funciona melhor #shorts](https://www.youtube.com/watch?v=Lw-LdQiyUpA) — INEMA LOOPY, 07/11/2026, 9:16
  - [Prompt de 5 palavras e zero código: 7 hábitos de quem está no topo da IA](https://www.youtube.com/watch?v=T6d1k8fgVHQ) — INEMA LOOPY, 07/11/2026, 16:9
  - [A IA desligou 25 apps da TV e achou um minerador escondido: 3 usos que quase ninguém faz](https://www.youtube.com/watch?v=hageCcHOcLE) — INEMA LOOPY, 06/11/2026, 9:16

#### 🏙️ historia-timelapse

Timelapse 3D de la historia de una ciudad: relieve real, edificios de OpenStreetMap que aparecen en el año en que se ocupó el barrio, contador de población del IBGE y tarjetas con el número, la explicación y la fuente.

- **Sirve para:** Historia de ciudades en video; se publica por fases (solo música, narrado, con avatar).
- **Formato:** 16:9
- **Avatar:** Opcional — fase 3 con avatar de Nei
- **Cómo se activa:** Terminal (skill historia-timelapse); cola de publicación
- **Repositorio:** [github.com/inematds/historia-timelapse](https://github.com/inematds/historia-timelapse)
- **Ejemplos publicados:**
  - [Porto Alegre de 1772 a 2024: 252 anos em um timelapse 3D com luz realista](https://www.youtube.com/watch?v=WzPVdaal1OY) — Aventuras INEMA, 24/10/2026, 16:9
  - [O centro de Itaguaí em 3D: da Matriz de 1729 à cidade do futuro](https://www.youtube.com/watch?v=dalR1xWPFlE) — Aventuras INEMA, 23/10/2026, 16:9
  - [Rio de Janeiro de 1500 a 2024: 524 anos de história em timelapse 3D](https://www.youtube.com/watch?v=Ij4KsTN_SB0) — Aventuras INEMA, 23/10/2026, 16:9

#### 🏔️ aventurasinemavideo (Memórias de Aventura)

Transforma artículos reales del archivo de INEMA Aventura (2001 a 2012), con los relatos y las fotos de los propios aventureros, en películas narradas de 1 a 3 minutos: fotos restauradas con movimiento y narración con la voz de Nei.

- **Sirve para:** La serie Memórias de Aventura.
- **Formato:** 16:9
- **Avatar:** No — fotos del archivo + narración
- **Cómo se activa:** Terminal / lote, con publicación en el canal Aventuras INEMA
- **Repositorio:** [github.com/inematds/aventurasinemavideo](https://github.com/inematds/aventurasinemavideo)
- **Ejemplos publicados:**
  - [Beto Monteiro vence sob calor de 35°C na Fórmula Truck | Memórias de Aventura #166](https://www.youtube.com/watch?v=vjsykS5_9HU) — Aventuras INEMA, 09/11/2026, 16:9
  - [Allam Khodair: de 4º a vencedor na Stock Car 2010 | Memórias de Aventura #165](https://www.youtube.com/watch?v=PLPcwWAQgqE) — Aventuras INEMA, 09/11/2026, 16:9
  - [De Curitiba ao Alasca de moto: 34 mil km em 1997 | Memórias de Aventura #164](https://www.youtube.com/watch?v=iqrvHLIET2Y) — Aventuras INEMA, 09/11/2026, 16:9

#### 🔥 gitbombando

Cada día crea el reel "Bombando no GitHub": los 10 proyectos que más ganaron estrellas, en cuenta regresiva, con tarjeta, foto del propietario, una explicación sencilla en portugués y el número de estrellas. También genera dos carruseles.

- **Sirve para:** Novedades de GitHub Trending en 1 minuto.
- **Formato:** 9:16
- **Avatar:** Sí — avatar de Nei (HeyGen)
- **Cómo se activa:** Temporizador: genera a las 9h y publica a las 11h
- **Repositorio:** [github.com/inematds/gitbombando](https://github.com/inematds/gitbombando)
- **Ejemplos publicados:**
  - [Caça-apelidos dispara ao topo do GitHub com +4.294 estrelas em um dia #Shorts](https://www.youtube.com/watch?v=W3Mds0R28_A) — INEMA Tec, 09/11/2026, 9:16
  - [Cloudflare segue no topo e um caça-apelidos invade o pódio: +2.085 estrelas no GitHub #Shorts](https://www.youtube.com/watch?v=vXoQJMnVT1w) — INEMA Tec, 08/11/2026, 9:16
  - [17.100 estrelas em 7 dias: o controle remoto de todas as IAs lidera o GitHub #Shorts](https://www.youtube.com/watch?v=3FXsmsRC0YA) — INEMA Tec, 08/11/2026, 9:16

### Video hecho con código (sin cámara)

#### 💻 video-codigo

Skill para Claude Code y Codex en la que cada cuadro se escribe con código (HTML, Canvas o SVG) y se convierte en MP4. La voz, si la hay, se genera en la computadora y cada imagen aparece en el momento de la palabra.

- **Sirve para:** Lanzamiento, anuncio, video explicativo o película de producto sin cámara ni editor.
- **Formato:** 16:9 y 9:16 del mismo proyecto
- **Avatar:** No (rostro opcional, hasta media pantalla)
- **Cómo se activa:** Terminal (skill en Claude Code o Codex)
- **Repositorio:** [github.com/inematds/video-codigo](https://github.com/inematds/video-codigo)
- **Ejemplos publicados:**
  - [Lead que espera esfria: do WhatsApp à venda em 1 minuto, feito com código #Shorts](https://www.youtube.com/watch?v=4ILX66Hddtk) — INEMA FTD, 06/11/2026, 9:16
  - [Do WhatsApp à venda: filme de produto feito 100% com código](https://www.youtube.com/watch?v=tWv1mEIK62c) — INEMA FTD, 06/11/2026, 16:9
  - [Um filme feito só com código e música | INEMA.CLUB #Shorts](https://www.youtube.com/watch?v=3JmREUS97-o) — INEMA FTD, 06/11/2026, 9:16

#### 🪐 reel-ciencia-3d

Kit con una skill para Claude Code que transforma una pregunta "¿Y si…?" en un reel de ciencia de unos 60 segundos, hecho solo con código (HyperFrames y Three.js), con la fuente de cada número y voz local.

- **Sirve para:** Divulgación científica en videos cortos, sin errores en los números.
- **Formato:** 9:16 (~60 s)
- **Avatar:** No
- **Cómo se activa:** Terminal (skill en Claude Code)
- **Repositorio:** [github.com/inematds/reel-ciencia-3d](https://github.com/inematds/reel-ciencia-3d)
- **Ejemplos publicados:**
  - [E se o Sol sumisse agora? Animação 3D feita só com código](https://www.youtube.com/watch?v=FDtJim4xHjY) — INEMA FTD, 06/11/2026, 9:16
  - [E se a Lua sumisse? Animação 3D feita só com código](https://www.youtube.com/watch?v=nUsGrdZ-8MY) — INEMA FTD, 06/11/2026, 9:16
  - [E se a Terra não tivesse inclinação? Animação 3D feita só com código](https://www.youtube.com/watch?v=BmSeV6r0FdQ) — INEMA FTD, 06/11/2026, 9:16

#### 🎙️ video-sem-rosto

Kit que enseña a Claude Code a crear explicativos horizontales sin grabar nada: voz clonada generada en el computador, la página real del sitio, imágenes 3D y subtítulos sincronizados.

- **Sirve para:** Explicar una herramienta, un repositorio o una novedad sin aparecer en cámara.
- **Formato:** 16:9
- **Avatar:** No
- **Cómo se activa:** Terminal (skill en Claude Code)
- **Repositorio:** [github.com/inematds/video-sem-rosto](https://github.com/inematds/video-sem-rosto)
- Todavía no hay videos publicados en YouTube con este motor; los videos de demostración están en la guía del proyecto.

#### 🎓 videos-cursos-inema

Motor que convierte un curso INEMA (sitio estático) en una serie de videos narrados y animados, con tres partes seleccionables: landing, un video por ruta de aprendizaje y una clase completa por módulo.

- **Sirve para:** Videos promocionales y clases de un curso.
- **Formato:** 16:9 (y 9:16 con --vertical)
- **Avatar:** No — narración con voz clonada local
- **Cómo se activa:** Terminal (skill videos-cursos-inema)
- **Repositorio:** [github.com/inematds/videos-cursos-inema](https://github.com/inematds/videos-cursos-inema)
- No aparece ningún video de este motor en el historial de publicaciones; la guía del proyecto muestra el ejemplo del curso FEP.

### Apoyo

#### 🔊 inemavox

Suite de voz con IA local que todos los motores usan por debajo: descarga videos, transcribe, genera voz (TTS), dobla y corta, con los modelos ejecutándose en la tarjeta gráfica, sin costo de API.

- **Sirve para:** Voz, transcripción, descarga y música/efectos para los otros motores.
- **Cómo se activa:** Terminal (scripts) o API local
- **Repositorio:** [github.com/inematds/inemavox](https://github.com/inematds/inemavox)
- Motor de apoyo: no publica videos propios.

## El proceso, de principio a fin

🧠 = sesión con Nei · ⚙️ = script (sin gastar tokens) · 🤖 = `claude -p`

1. 🧠 Motor nuevo o cambio de texto: edita `catalogo.json` (texto en PT, regla que identifica los videos, `excluir`/`fixar`).
2. ⚙️ `python3 traduzir.py` — traduce a EN/ES solo las claves nuevas, mediante el traductor central `inema-traduz`, y guarda `i18n/en.json` y `i18n/es.json`.
3. ⚙️ `python3 atualizar-exemplos.py` — lee el historial de yt-pubx (`~/.local/share/yt-pubx/historico.jsonl`) y, si existe, el registro de producciones (separa explicavideo de refazvideo); elige hasta 3 videos públicos, recientes y variados por motor y guarda `motores.json`.
4. ⚙️ El mismo comando ejecuta `python3 gerar.py`, que vuelve a generar `README.md`, `README.en.md`, `README.es.md` y `guia/index.html`, `guia/en/`, `guia/es/` a partir de `motores.json`.
5. 🧠 Revisa la página y el README; `git push`. GitHub Pages (Actions) publica desde la rama `main`.

Los ejemplos no se vuelven a revisar en YouTube: el script solo lee archivos locales. Los videos rechazados o reemplazados se agregan a `excluir` en `catalogo.json`.

## Archivos

| | |
|---|---|
| `catalogo.json` | fuente editada a mano: textos de los motores, canales, reglas de identificación |
| `motores.json` | datos del índice generados por el script (motores + ejemplos) |
| `atualizar-exemplos.py` | vuelve a leer el historial y genera motores.json |
| `gerar.py` | genera los READMEs y la guía a partir de motores.json |
| `traduzir.py` | traduce los textos nuevos a EN/ES (inema-traduz) |
| `i18n/` | textos de la página y de los motores en PT, EN y ES |

## Licencia

MIT. Proyecto de [INEMA.CLUB](https://inema.club).
