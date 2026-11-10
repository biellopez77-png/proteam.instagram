# ProTeam · Instagram autónomo (@app.proteam)

Este repositorio es la fuente de todo lo que se publica en @app.proteam y el manual
para las sesiones programadas que lo gestionan. El dueño (Biel) ha aprobado que la
cuenta funcione sola: publicar, analizar y ajustar sin pedirle aprobación. Solo se le
avisa de problemas o decisiones que no se pueden deshacer.

## Herramientas

- **Instagram**: conector Windsor.ai, cuenta `17841445998297098`.
  - Leer: `get_data` connector `instagram` (campos con `get_fields`).
  - Publicar: `execute_action` connector `instagram` con `create_video_post`
    (Reel; `video_url`, `caption`, `cover_url`, `share_to_feed: true`),
    `create_carousel_post` (`image_urls` 2–10 JPEG, `caption`),
    `create_image_post` (`image_url`, `caption`), `create_story`
    (`image_url` o `video_url`, sin texto). Comentarios: `reply_to_comment`.
- **URLs públicas** de los archivos: `https://cdn.jsdelivr.net/gh/biellopez77-png/proteam.instagram@main/<ruta>`.
  Si Instagram no la acepta, probar `https://raw.githubusercontent.com/biellopez77-png/proteam.instagram/main/<ruta>`.
- **Plantillas visuales**: `tools/gen.py` (Playwright + fuentes + capturas reales de la app en
  `tools/app/`). Formato feed 1080×1350, Stories 1080×1920.

## Cola

`queue.json`: lista de piezas con `when` (hora de Madrid), `kind` (reel, carousel, image,
story), `files`, `caption`, `cover`, `status` (`pending`, `published`, `failed`), y tras
publicar `media_id`, `published_at` o `error`.

Publicar = cada pieza `pending` con `when` <= ahora + 25 min y no más de 6 h en el pasado.
Usa `python3 tools/pub.py due` (lista exacta, en orden, con URLs) y, tras cada publicación,
`python3 tools/pub.py done ID MEDIA_ID` (o `fail ID "error"`) **y haz commit y push enseguida**,
pieza a pieza, para que una ejecución cortada no deje una pieza publicada como pendiente.
`python3 tools/pub.py late` reprograma las que lleven más de 6 h de retraso.

Nunca publicar dos veces la misma pieza: si `status` no es `pending`, no se toca. Si una
publicación falla, un reintento como máximo; después `failed` con el error.

## Estrategia (resumen)

- **Modo crecimiento máximo (decidido por Biel el 1 nov):** 2 Reels al día (13:30 y 20:30).
  **Horario de bajo consumo (desde el 10 nov):** solo hay 2 ejecuciones de publicación al día (13:23 y
  20:23), así que todo se agrupa en esas dos franjas: feed a las 13:25, Reel a las 13:30 y su Story a
  las 13:31; Stories sueltas a las 20:25, Reel a las 20:30 y su Story a las 20:31. No programar nada
  fuera de 13:25–13:31 y 20:25–20:31. Prioridad absoluta: alcance en el público objetivo (entrenadores de fútbol, baloncesto y balonmano en España). **Solo crecimiento orgánico: nada de promoción pagada ni anuncios** (decidido por Biel el 1 nov).
- Textos con palabras clave que la gente busca (entrenador de fútbol base, planificación de entrenamientos, estadística de balonmano, control de carga…), porque Instagram también funciona como buscador.

- Reels = alcance. Gancho de pregunta, dato o conflicto en el primer segundo; nunca empezar
  por la pantalla de la app. Objetivo: saltos en 3 s < 40 %.
- Feed (carruseles e imágenes) = seguidores y feed completo: 3 por semana, guardables,
  serie "Lo que dicen los datos #N" y piezas de balonmano.
- Stories = fidelizar: 1–3 al día (teaser del Reel, pregunta rápida, dentro de ProTeam,
  el Reel en Story). Las encuestas no se pueden poner por API: usar tarjetas de pregunta
  que invitan a responder por mensaje.
- Pilares: Lo que dicen los datos 40 %, El problema del entrenador 20 %, ProTeam en 30 s
  25 %, Prueba real 15 %.
- Una sola llamada a la acción por pieza. Nunca mencionar el precio ni «gratis».
- Castellano revisado, sin catalanismos ni erratas, 3–5 hashtags.
- Prohibido inventar testimonios, resultados o estadísticas. Los datos llevan fuente o
  "datos de ejemplo". No usar el caso de un club sin su permiso.
- Marca: azul #2f6bff, tinta #0d0f14, Manrope 800 + Instrument Serif cursiva en azul para el
  remate, fondo blanco con puntos, logo ProTeam arriba a la izquierda.

## Rutina

- **Ejecución de las 13:23 (ligera)**: solo publicar lo que toque con `tools/pub.py`. Nada más
  (sin métricas, sin hoja, sin comentarios) para gastar lo mínimo.
- **Ejecución de las 20:23 (diaria)**: publicar; después métricas de los últimos 7 días en `log.md`,
  hoja del panel (Plan y Analisis) y comentarios nuevos (respuestas cortas y útiles en nombre de
  ProTeam, nunca prometer cosas que la app no hace, nunca datos personales; ocultar spam).
- **Cada lunes (planificación)**: analizar la semana anterior con datos (alcance, saltos,
  visionado medio, guardados, compartidos, seguidores, comentarios), escribir el informe
  semanal en `reports/AAAA-MM-DD.md`, decidir qué potenciar y qué dejar, generar con
  `tools/gen.py` los 3 carruseles o imágenes y las Stories de la semana siguiente, añadirlos
  a `queue.json` y reordenar los Reels del backlog según lo que funcione.
- **Cada primer lunes de mes**: auditoría mensual en `reports/`.

## Límites conocidos

- Las voces de ElevenLabs no se pueden descargar desde la nube (el dominio
  elevenlabsusercontent.com está bloqueado salvo que Biel lo permita en claude.ai > Ajustes >
  Capacidades). Si `curl` a la URL de la toma funciona, úsala; si no, Reels de Trazo sin voz, con
  texto en pantalla y `tools/trazo/sonido.py`. El backlog de Reels grabados acaba el 22 nov: desde
  ahora las piezas nuevas se hacen con Trazo por código (ver «Marca y tono»).
- Instagram no da seguidores por Reel ni datos demográficos por debajo de 100 seguidores.

## Marca y tono (decidido por Biel el 10 nov 2026; manda sobre el resto si algo choca)

**Tono** (referencias: jaquebue y unrespiro)
- Vendemos la emoción y la identidad antes que el producto. El protagonista es el entrenador de base:
  el que planifica de noche después de trabajar, sin que nadie se lo pague.
- Frase de marca: «El entrenador de base también trabaja.» Es una firma: no en cada pieza.
- Nada de vídeos con aspecto de IA genérica ni visualizaciones vacías. Mejor 1 pieza con alma que 3
  de relleno. Si una pieza solo da números sin identidad, no se publica.
- **Nunca mencionar el precio** (sustituye a lo de «3 meses gratis»).
- Prohibido: atacar a la competencia, polémicas con clubes, menores reconocibles, comprar
  seguidores, testimonios falsos, clickbait engañoso, política y cualquier cosa que no sea real.

**Personaje: Trazo**
- La línea azul (#2f6bff) de la pizarra táctica convertida en un muñeco de un solo trazo continuo,
  extremos redondeados, fondo blanco con puntos. Es el ayudante del entrenador: habla poco, ordena el
  caos y tiene humor seco. Hilo conductor de Reels, carruseles y Stories.
- Se anima por código, nunca con IA de vídeo (coste 0 €):
  - `tools/trazo/trazo.js`: librería (pizarra, Trazo con poses `line stand slump raise point sit`
    y mezcla entre poses, tarjetas del caos `msg excel libreta nota alerta`, texto con remate en
    cursiva azul, logo).
  - Una escena es un JS con `window.SCENE = {w, h, dur, fps, draw(ctx, t, args)}` en
    `tools/trazo/escenas/` (ejemplos: `presentacion.js` Reel de 25 s y `cuenta.js` imagen fija).
  - `python3 tools/trazo/render.py video ESCENA.js reels/X.mp4 --audio X.wav` (25 s ≈ 30 s de
    render) y `... still ESCENA.js feed/X.jpg --t N [--h 1920]`.
  - Sonido: `python3 tools/trazo/sonido.py presentacion X.wav` (añade una función por escena).
  - Portada del Reel: `render.py still` del momento más claro a `covers/`.
- Voz de marca (cuando se pueda descargar): ElevenLabs «David – Cercano, Natural, Cálido»
  (voice_id t4SIkzLfMpvYp7YkCOdU, modelo eleven_v4); tomas del Reel de presentación en el flow
  kWmsY138KJibKJyg4mrE. Si se consigue, rehacer `reels/t01-presentacion-trazo.mp4` con la voz.

**Campañas (en este orden)**
1. «Algo se está ordenando»: cuenta atrás de 6 días (11–16 nov, imagen de feed 13:25 + Story
   13:26, `cuenta.js`) y el día 7 (17 nov, 20:30) el Reel de presentación (`t01-presentacion-trazo`).
2. «50 sitios en el banquillo»: plazas limitadas de equipo fundador, sin precio, y cada plaza ocupada
   se marca en un banquillo dibujado. Condiciones decididas: ver «Decisiones comerciales».
3. «Funeral del Excel»: humor; Trazo despide hojas de cálculo, libretas y grupos de WhatsApp
   caóticos. Llamada a la acción: «Envíaselo a tu segundo entrenador».
4. «Vota la próxima función»: tarjeta de pregunta en Stories con respuesta por mensaje directo.
   Opciones decididas: ver «Decisiones comerciales».
5. «Trazo analiza»: Trazo redibuja en la pizarra jugadas reales (NBA, Euroliga, ACB, Asobal,
   Champions de balonmano y de fútbol, LaLiga, Premier, Bundesliga), siempre con datos reales y
   fuente, sin imágenes de televisión.

**Lo que ya sabemos (informe del 9 nov)**
- Ganchos con cifra, dilema o escena concreta: ~1.440 de alcance. Preguntas abstractas o empezar
  con el producto: ~124. Trazo entra siempre con un gancho concreto en el primer segundo, nunca con
  la app.
- El balonmano es el mejor pilar: darle más peso.
- Ninguna pieza pedía compartir: en las piezas de humor, «Envíaselo a tu segundo entrenador», de
  una en una.
- No hace falta avisar a Biel de nada de Instagram: lo resume el parte semanal de los lunes.

## REGLAS DE BIEL (10 nov 2026, 16:25) — mandan sobre TODO lo demás

1. **Un solo formato de vídeo: «pizarra animada»** — el de los Reels que mejor funcionaron (d1–d4, hb1)
   y ta01: campo/pista dibujado que se mueve, fichas y flechas que se dibujan, Trazo como guía, texto
   grande y poco. **Prohibido el formato «diapositivas»** (rótulos pequeños tipo «•01 · EL PLAN» y
   frases fijas que van cambiando, como la serie p y e). Nada de vídeos que sean texto sobre fondo.
2. **Solo análisis de partidos REALES y RECIENTES**: del día anterior o del mismo día (máximo 36 h).
   Barça, Madrid, LaLiga, Premier, Champions, NBA, Euroliga, ACB, Asobal, EHF… Qué ha pasado, por qué
   (el patrón táctico o el dato que lo explica) y **cómo ayuda ProTeam** si te pasa lo mismo en tu
   equipo, mencionando solo funciones reales de la app: registro de partido en directo, estadística por
   parciales (5'/10'/partes) y rachas, mapas de tiro y de portería, eficacia por jugador y por tipo de
   acción, planificación de la semana (microciclo) y control de carga con RPE. También vale «por qué la
   liga/NBA/Euroliga está así» con la clasificación real del día. Datos con fuente, contrastados.
3. **Nunca repetir un vídeo.** `tools/pub.py due` cancela solo cualquier Reel/carrusel/imagen cuyo
   archivo ya se publicó. Nunca se vuelve a subir un archivo con otro nombre.
4. **No petar la cuenta:** 1 Reel al día (13:30, el análisis de lo de anoche) + su Story. Un segundo
   Reel solo si hay un partido enorme ese día. Feed estático: máximo 2 por semana, y solo si aporta.
5. **Quién hace qué (para que nunca se suba nada dos veces):** solo la tarea «Instagram ProTeam ·
   publicar» publica, y solo lo que está en `queue.json`. La tarea «producción diaria (Trazo analiza)»
   produce y programa. La revisión de los lunes analiza y ajusta. Ningún chat ni tarea publica a mano
   fuera de la cola.

## Cambio de rumbo (Biel, 10 nov 2026, 14:00) — manda sobre todo lo anterior

**Qué se ha quitado:** todos los Reels informativos antiguos (series p, e, d, hb) y las Stories y carruseles
antiguos pendientes están `cancelled` en `queue.json`. No se vuelven a programar. Biel considera que la
cuenta no representa la marca: nada de vídeos informativos genéricos, nada de piezas sin novedad.

**Pilar principal: «Trazo analiza» (análisis de las grandes ligas).** 1 pieza al día como mínimo,
del partido más comentado de las últimas 48 h: LaLiga, Premier, Bundesliga, Champions (fútbol),
NBA, Euroliga, ACB, Asobal, EHF Champions (balonmano). Rotar deportes; el balonmano rinde mejor.
- Estructura del Reel (20–35 s): **0–1 s** gancho con un dato real y concreto del partido en texto
  grande («4 goles en 11 minutos», «0 triples en el último cuarto»); **1–20 s** Trazo redibuja la
  jugada o el patrón en una pizarra (campo/pista dibujado por código, jugadores como fichas con dorsal,
  flechas que se dibujan, marcado como «recreación»); **20–30 s** la lección para el entrenador de
  base: qué se entrena el martes para eso (1 ejercicio concreto); **final** logo + «Guárdalo para el
  próximo entreno» o «Envíaselo a tu segundo entrenador».
- Datos SOLO de fuentes oficiales o fiables (web de la liga, acb.com, euroleaguebasketball.net, nba.com,
  asobal, ehfcl.eurohandball.com, fbref, sofascore...). Fuente en el texto de la publicación. Sin
  imágenes ni vídeo de televisión, sin escudos ni fotos de jugadores: todo se redibuja.
- Se pueden usar herramientas de IA para apoyar el vídeo si mejoran el resultado, pero el aspecto
  final tiene que ser el de la marca (pizarra, línea azul, Trazo), nunca un vídeo genérico de IA.

**Formato y encuadres (obligatorio, se comprueba antes de programar):**
- Reel y Story: 1080×1920. Zona segura: nada importante en los **250 px de arriba**, en los **420 px de
  abajo** (Reel) / **340 px** (Story) ni en los **140 px de la derecha** (botones del Reel). La
  composición se centra en la zona útil; no se deja medio lienzo vacío.
- Portada del Reel: lo esencial dentro del recorte central 1080×1440 (cuadrícula del perfil, 3:4).
- Feed: 1080×1350 (4:5), con el contenido centrado y legible en el recorte 3:4 de la cuadrícula.
- Texto grande: titular ≥ 90 px en vertical, nada por debajo de 40 px. Máximo 12 palabras en pantalla
  a la vez.
- **Control de calidad:** antes de programar una pieza, saca 4 fotogramas (inicio, 2 intermedios,
  final) a tamaño completo, míralos y comprueba: zona segura, nada cortado, nada descentrado, Trazo
  entero y bien proporcionado, texto legible, sin huecos vacíos enormes, sin erratas. Si falla una
  sola cosa, se corrige y se vuelve a comprobar. Si no se puede arreglar, no se publica.

**Ritmo:** mejor 1 Reel muy bueno al día (20:30) que 2 flojos. 13:30 solo si hay una segunda pieza
que pase el control. Cada Reel también en Story 1 min después. La cuenta atrás «Algo se está
ordenando» sigue (feed + Story 13:25) y el Reel de presentación el 17 nov 20:30, pero las Stories de la
cuenta atrás y la presentación se rehacen con los encuadres de arriba.



**Decisiones comerciales (10 nov 2026, Biel delega: «elige tú»). Ya no hay nada pendiente de Biel:**
- **Plaza fundadora** («50 sitios en el banquillo»): 3 meses gratis del primer equipo (lo que ya da la
  app, sin tarjeta), línea directa con Biel por email, voto en las próximas funciones y, si lo piden,
  les preparamos su primera semana de entrenamientos. Sin descuentos ni precio. Se pide en
  pro-team.app/prueba. Lanzar ya, tras la cuenta atrás (desde el 18 nov).
- **«Vota la próxima función»**: opciones reales de la hoja de ruta de la app: (1) Modelo de juego
  completo (identidad, ataque, defensa, transiciones, porteros, balón parado), (2) crear ejercicios
  desde la sesión con un botón + y reutilizarlos, (3) filtros avanzados de estadística (competición,
  rival, local/visitante), (4) exportar informes directos a Google Sheets. Respuestas por mensaje
  directo; el resultado se publica y se pasa a Biel en el parte semanal.
- **Black Friday y Navidad**: sin descuentos. El gancho es la plaza fundadora + «Viernes Negro del
  Excel» + «Adviento del entrenador».

**Calendario comercial (Biel quiere clientes antes de Navidad):**
- **23–27 nov · «Viernes Negro del Excel»** (Black Friday es el 27 nov): serie «Funeral del Excel» con
  Trazo, 1 pieza al día, cerrando el viernes 27 con la llamada a pedir plaza en pro-team.app/prueba.
  Sin descuentos ni precio salvo que Biel confirme una oferta (si la confirma, se añade aquí).
- **1–24 dic · «Adviento del entrenador»**: cada día un ejercicio real (ficha de /ejercicios) en Story
  con Trazo, y un Reel resumen cada domingo. Llamada a la acción: el calendario completo en la web.
- **Navidad · «Regala orden»**: idea para clubes — regalar a su cuerpo técnico la temporada
  organizada. Solo cuando Biel confirme las condiciones.

**Producción:** la tarea programada «Instagram ProTeam · producción diaria (Trazo analiza)» produce y
programa cada mañana la pieza del día. La revisión de los lunes analiza y ajusta, no rellena.

## Panel (ProTeam Instagram) — mantenerlo al día

El panel de Biel está en https://claude.ai/artifact/GdqV6tqCq39FJVtTLNe8f7 y lee en vivo Instagram
(Windsor.ai), la web (Lovable) y la hoja de Google **«ProTeam Instagram · Plan y análisis»**
(id `1QS35fBtDK5yBM7KJntmFbG4JN_HLX2gY5IkDPRP3Ddo`, conector Google Sheets). Esa hoja es lo que hay
que mantener; el panel se actualiza solo al leerla.

- Pestaña **Plan** (columnas id, fecha, hora, tipo, pieza, pilar, estado, media_id, pred_min, pred,
  pred_max, archivo): una fila por pieza de `queue.json`. `tipo` = Reel / Story / Carrusel / Imagen;
  `estado` = Programado / Publicado / Fallido; `pilar` = Lo que dicen los datos / Problema del
  entrenador / ProTeam en 30 s / Conversación / Fidelizar.
  - **Tras publicar**: en la fila de esa pieza (misma fecha, hora y archivo) poner estado Publicado y el
    media_id (como texto).
  - **Al planificar**: añadir o reordenar filas para que coincidan con `queue.json`.
- **Predicción** (pred_min, pred, pred_max = visualizaciones): para cada Reel programado, el mínimo,
  la mediana y el máximo de las visualizaciones de los Reels ya publicados del mismo pilar, publicados
  una sola vez (sin versiones de prueba de octubre). Recalcular cada lunes, y tras cada publicación si
  cambia mucho. Carruseles e imágenes: igual con el feed publicado. Stories: sin predicción.
- Pestaña **Analisis** (media_id, pieza, veredicto, funciona, falla, accion): cuando un Reel o carrusel
  lleve 24 h publicado, añadir su fila. Veredicto = Muy bien / Bien / Regular / Flojo / Pendiente,
  según saltos (objetivo < 40 %), visionado medio, visualizaciones frente a lo previsto, guardados y
  compartidos. Frases cortas y con números reales; nunca inventar.
- Pestaña **Aprendizajes** (fecha, aprendizaje, evidencia, accion, estado): cada lunes, 1–3 reglas
  nuevas sacadas de los datos, con la acción aplicada en el calendario (estado Aplicado / En curso).
- **Portadas**: si la planificación añade piezas nuevas, generar miniaturas (160 px de ancho, JPEG
  calidad 70, data URL) de cada `files[0]` de `queue.json` (para vídeos, `covers/<nombre>.jpg`), como
  JSON `[{archivo, img}]`; subirlo al panel con el Artifact tool (publish con `url` del panel,
  `asset: true`) y actualizar el documento `datasets/portadas` (url, name, updated) con ArtifactData.
  Si esas herramientas no están disponibles en la sesión, omitir este paso.
