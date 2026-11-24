# Formato v7 · «historia con fotos» (Biel, 24/11; manda sobre v4, v5 y v6)

Modelo: Bielsa (`tools/reel_v7/bielsa/reel3.html`, `words3.js`, `mix3.py`; vídeo sin audio `video3_mudo.mp4`).
Visto bueno de Biel del 24/11: «genera contenido con este estilo a partir de ahora». Con tres condiciones:
- las transiciones, suaves y fluidas;
- los efectos de sonido, más bajos y reales;
- la música, que no parezca de IA: suave pero que transmita;
- la voz, más confiada.

## Qué es
- **Duración y voz:** 15–25 s de voz (35–60 palabras) y después el cierre común de ProTeam (`tools/reel_v6/outro/outro.mp4`).
- **Historia:** real, de un entrenador o de un equipo, con un dato que sorprende. Frases cortas, y cada frase nombra algo que se puede ver.
- **Un solo plano:** la cámara recorre una pared grande (`wall2.jpg`, 2600×6400) de escena en escena, sin cortes.
- **Animación por palabra:** cada cosa que dice la voz se anima en el momento en que la dice. Ejemplos:
  - «espiar» → visor REC;
  - «PowerPoint» → diapositiva (rotulada «recreación»);
  - «51 partidos» → contador y 51 fichas;
  - «4 horas» → reloj que dibuja el arco;
  - «método» → pizarra con flechas;
  - «El Loco» → sello.
- **Fotos:** reales y con licencia (Commons u otra licencia clara). Van recortadas (rembg), en B/N con solo el azul conservado (`tools/reel_v7/bielsa/grade.py`), con sombra, marco, ficha de prensa o portada de revista. Si no hay foto, el objeto se dibuja.
- **Texto:** Instrument Serif para la frase y Plus Jakarta Sans 800 para la palabra fuerte, que aparece palabra a palabra (desenfoque → nítido, 0,36 s). Ultravioleta #8B5CF6 una sola vez.
- **Paleta:** fondo #02050F, tarjetas #0C1323, azules #636DFF, #6AA8FF y #B9E0FF.

## Transiciones (obligatorio)
- Viaje de cámara de 0,9 s con `power2.inOut`. Zoom de respiración ×0,9, nunca más.
- Desenfoque de movimiento de 4 px como máximo, y solo a mucha velocidad.
- Sin destellos ni cortes. Fundido de 0,6 s al cierre.
- El viaje empieza en la pausa entre frases (mira los tiempos de la voz) y llega antes de la palabra siguiente.
- Los elementos de cada escena entran ya con la cámara llegando: fundido y movimiento corto (≤ 0,5 s).
- Durante la escena, la cámara deriva despacio (`sine.out`).

## Voz (más confiada)
- ElevenLabs `creative_generate_speech`, `eleven_v4`, voz Mateo `gpMzl7dbkfC9dIxAqQZT`, `generations_count` 1.
- El prompt empieza por `[confident, assured, steady storyteller tone, firm and calm]`.
- Puntos y comas marcan las pausas. Una pausa con «...» antes del remate.
- Tiempos por palabra: faster-whisper en el sandbox de Higgsfield (`mcp__Higgsfield__sandbox_exec`). Lo hace el script `wt.py` de `tools/reel_v7/README_AUDIO.md` y da `words.js` con `window.WORDS=[[palabra,ini,fin],…]`.
- Comprueba que la transcripción tiene todas las palabras. Si falta alguna, genera otra toma.

## Música y efectos (reales, no sintetizados)
Fuente: Epidemic Sound desde Higgsfield: `search_sound_effects`, después `download_sound_effect` (quality high).
- **Música:** busca «Musical, Loop» con soft piano / strings / calm / emotional / cinematic. Escoge pistas en la misma tonalidad si encadenas dos, y una pista distinta por vídeo cuando se pueda.
  - Va unos 12 dB por debajo de la voz (RMS de voz −19, música −31), con un ducking suave (ataque 80 ms, suelta 400 ms, −42 %).
  - Encadena con fundidos de 1,4 s y nunca cortes.
- **Efectos:** reales y discretos, uno por elemento que entra:
  - papel que desliza
  - obturador
  - cartas o fichas
  - reloj
  - rotulador
  - sello
  - aire muy suave en cada viaje

  Ganancias de 0,07 a 0,22 sobre la voz normalizada. Nunca tapan la voz.
- Los dominios de Epidemic y de Wikimedia no se pueden descargar desde nuestro contenedor. Descarga y mezcla en el sandbox de Higgsfield con `tools/reel_v7/bielsa/mix3.py` como plantilla. Cambia los tiempos y los archivos.

## Montaje y entrega
1. Render sin audio a 30 fps con `tools/blackout/htmlreel.py video` (FPS=30) y fundido al outro con xfade → `tools/reel_v7/<id>/video_mudo.mp4`. Haz commit y push.
2. En el sandbox de Higgsfield:
   - descarga `video_mudo.mp4` (raw.githubusercontent.com, por el hash del commit), la voz (URL de ElevenLabs), la cola del outro (`tools/reel_v6/outro/tail.mp3`, a los +0,3 s del inicio del outro) y los sonidos de Epidemic;
   - mezcla y multiplexa (AAC 256k);
   - comprueba con whisper que la voz se entiende entera;
   - sube el vídeo con `media_upload` (PUT en el mismo comando) y confirma con `media_confirm`.
   La URL pública de cloudfront es el archivo que se publica.
3. Cola: entrada en `publicar/cola.json` con `files: [<URL cloudfront>]` (pub_v3 acepta URL absolutas), `state: "revisión"` y caption con fuentes, créditos de fotos y «Música y efectos: Epidemic Sound». Cierre del caption: «Estamos terminando la app de ProTeam. Síguenos para no perderte nada: muy pronto, novedades.»
4. Andrés audita. Si la nota es ≥ 85, `python3 tools/pub_v3.py approve <id> <AAAA-MM-DD>T18:00:00+01:00` (hueco de las 18:00 del siguiente día libre). Laura la publica en Instagram y el turno de TikTok la programa en Metricool.

## Reglas que no cambian
- Nada inventado: cada dato tiene una fuente en el guion.
- Sin precio, sin fechas de lanzamiento y sin cifras de apuntados.
- Sin el nombre de Biel.
- Caras reales solo de fotos con licencia, y nunca dando a entender que esa persona apoya ProTeam.
- Nada en 3D.
