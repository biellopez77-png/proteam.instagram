# Producción autónoma de un Reel (paso a paso)

> **Desde el 16/11:** este paso a paso técnico sigue valiendo, con tres cambios que mandan sobre lo que diga abajo: (1) las instrucciones de cada persona son las de `agentes/` y sus procedimientos los de `skills/`; (2) el control de calidad del montaje ya no son «6 fotogramas»: todo Reel se analiza con `tools/video_intel.py` (analyze en modo detalle, voz y rasgos), Marta mira todas las láminas y Andrés audita el vídeo real con marcas de tiempo (`../intel/README.md`); (3) la nota de Andrés usa la escala nueva de `../oficina/PROTOCOLO.md` §6.


Lo usa la tarea programada «Agencia ProTeam · producir Reel» y cualquier sesión que tenga que sacar un Reel sin Biel.
Plantilla técnica: `tools/reel2/` (Reel 2, aprobado por Biel). Cada Reel nuevo va en su propia carpeta: `tools/reelNN/`.

## Antes de nada: la oficina
Este paso a paso es el turno de Dani (01), Marta (02), Pau (03) y Andrés (05). Aplica `oficina/PROTOCOLO.md` entero: ENTRADA antes del punto 0 (reglas, instrucciones, pausa, encargos y decisiones de Biel), estado de cada persona en cada fase y SALIDA al terminar (ficha de revisión de la pieza, log, agenda).

## 0. Hueco y número
- `queue.json`: busca el próximo hueco de Reel libre de la parrilla (9:30, 11:30, 13:30, 17:30, 20:30 o 22:30, hora de Madrid; ver `oficina/PROTOCOLO.md`) que empiece al menos 3 h después de ahora y que no tenga ya un Reel `pending`. Las piezas `borrador` no ocupan hueco.
- Id: `uNN`, el siguiente libre después del mayor `u` que haya.
- Fechas: hasta el 27/11, con la oferta (MARCA.md). Desde el 28/11, sin oferta.

## 1. Guion (Agente 01 · skill proteam-content-lab)
- Elige un hook sin usar de `agencia/HOOKS_BANCO.md` (prioriza el Top 30) y márcalo como `[usado uNN]`.
- El tema y la conclusión no deben repetir nada de `HISTORIAL.md`.
- Escribe el guion (60–80 palabras de voz, una sola idea) en `agencia/guiones/AAAA-MM-DD-uNN-<slug>.md`.
- Puntúalo con los 8 criterios y no sigas si la media baja de 4.
- El cierre de campaña es fijo: «La app de ProTeam…» + «Únete a la lista de espera antes del 28 de noviembre y consigue tres meses gratis».

## 1b. Crítica del guion (Agente 05 · skill proteam-critical-lab)
MODO GUION sobre el guion: veredicto + nota sobre 100 con desglose. Si < 75, aplica la cirugía creativa y vuelve a puntuar (máx. 2 vueltas); si sigue < 75, cambia de hook o de idea. Guarda la crítica en `agencia/criticas/AAAA-MM-DD-uNN-guion.md`. Lee antes `agencia/APRENDIZAJES.md`.

## 2. Dirección (Agente 02 · skill proteam-creative-direction)
- Escribe el documento A–F en `agencia/produccion/…`.
- El concepto visual tiene que ser distinto de los «Recursos visuales ya usados» (HISTORIAL).
- El cierre de campaña se mantiene: UI de la lista de espera igual que en u01/u02, «hasta el 28.11» sobre foto y «3 meses gratis.» en serif azul.

## 2b. Arranque de cada Reel (Marta, 16/11 · bucle diario de Samuel; provisional hasta que u04 tenga 24 h)
Antes de montar, comprueba estas cinco cosas. Salen de u04 y u03 (36–38 % de saltos en 3 s) frente a u02 y u01 (71 % y 58,5 %, unas 180 vistas). Datos del 16/11 a las 22:42; u04 llevaba 5 h y u03 2 h.
1. **Fotograma 0:** cara o escena reconocible a pantalla completa con el texto grande ya puesto. Nunca negro, nunca texto pequeño.
2. **Voz:** entra en 0,1 s y lo primero que dice es la pérdida concreta del entrenador (lo que tenía y ya no tiene), no una frase general.
3. **Duración:** 24–25 s como mucho en los Reels con voz.
4. **Ficha para guardar a la vista** (qué apuntar, tres pasos), al menos 3 s en pantalla.
5. **Prohibido** abrir con una frase de marca o motivación y cerrar sin nada que guardar (lo de u02 y u01).
En el documento de producción de cada Reel se escribe una línea «Arranque: 1 ✔ 2 ✔ 3 ✔ 4 ✔ 5 ✔» y, si Samuel tiene un experimento abierto, qué única cosa cambia respecto a u04. Si los datos de 24 h desmienten a u04, Samuel cambia este apartado.

## 3. Recursos (Agente 03 · skill proteam-resource-bank)
- Las personas y los equipos son siempre reconocibles, de primer nivel. Saca primero lo que ya haya en `banco/` y busca el resto en Commons, por nombre propio, desde el sandbox de Higgsfield.
- Copia lo que vayas a usar a `tools/reelNN/img/` y apúntalo en `banco/INVENTARIO.csv` con el estado `usada en uNN`.

## 4. Voz (siempre Mateo)
- **Desde el 16/11 16:55 los turnos descargan el audio directamente**: `curl -L -o voz.mp3 '<url de creative_get_generations>'` (Biel permitió elevenlabsusercontent.com). Ya no hace falta el sandbox ni el truco del PNG; la transcripción con faster-whisper puede hacerse aquí (`pip install faster-whisper`) o en el sandbox.
- ElevenLabs: `creative_generate_speech`, voice_id `Rie0luvrYhyKLba1lK3c` (Mateo original; desde el 16/11 está desactivada: si falla, usa `gpMzl7dbkfC9dIxAqQZT`, «Mateo – News & Digital Stories» de la biblioteca, sin preguntar), modelo `eleven_v4`, flow `hBYtrq1HJVmwM1XJaheU`. Salen 2 tomas.
- Escribe «Pro Team» para que lo pronuncie bien y los números en letra («veintiocho», «tres»).
- URLs con `creative_get_generations`.
- Descarga desde el sandbox de Higgsfield (`sandbox_exec`), porque el contenedor local no llega a elevenlabsusercontent.com:
  - Transcribe allí con faster-whisper (`word_timestamps=True`) e imprime los tiempos de cada palabra.
  - Para traer el audio: pásalo a ogg/opus a 64k y mételo en un PNG en escala de grises de 1024 de ancho (4 bytes de longitud + bytes). Devuélvelo con `image_paths` (máximo 512 KB por llamada).
  - El archivo llega a `~/.claude/projects/*/tool-results/mcp-Higgsfield-blob-*.png`. Decodifícalo con PIL.
- Elige la toma más fluida y pronunciada.
- Copia `tools/reel2/voz.py` y `mkt.py` y adáptalos: cuerpo con atempo ×1,1 y CTA a ×1,0.
  - Pausas solo sobre silencios reales y nunca `silenceremove`.
  - Pausa antes del CTA de ~0,2 s como máximo: Biel no quiere pausitas.
- `mkt.py` genera `times.js` con snap por energía. Todas las animaciones van colgadas de `times.js`.

## 5. Montaje
- Parte de `tools/reel2/reel.html` y cambia bloques, fotos y textos según el documento del Agente 02.
- Respeta MARCA.md:
  - Manrope + Instrument Serif itálica azul.
  - Oscuro, o papel para los bloques editoriales.
  - Zona segura y nada en los márgenes.
- Fotogramas de control: `cd tools/blackout && FPS=30 python3 htmlreel.py still tools/reelNN/reel.html <prefijo> t1 t2 …`. Mira la hoja de contacto con Read.
- Render: `FPS=30 python3 htmlreel.py video tools/reelNN/reel.html <ruta>/v.mp4 <END>` en segundo plano, unos 5 minutos.

## 6. Música (siempre nueva, mismo estilo)
- ElevenLabs `creative_generate_in_flow`: node_type `music`, modelo `eleven_music_v2_5`, flow `hBYtrq1HJVmwM1XJaheU`, 2 variaciones.
- Prompt base, que hay que variar en cada Reel (tonalidad, textura del pad, patrón de hi-hats) para que nunca suene igual: «Instrumental dark minimal trap beat at ~143 BPM, punchy deep 808 sub-bass, crisp fast hi-hats with rolls, tight snare, sparse moody synth pad, modern sports-motivational energy, no vocals; short breakdown then the beat drops back in hard; ~32 seconds».
- Descárgala con el mismo truco del PNG.
- Analízala con librosa (tempo, golpes y silencio).
- Alinéala: desplázala para que el regreso del beat caiga en la palabra de impacto. Si se queda corta, repite 4 compases cortando en golpe de beat, con 30 ms de fundido cruzado. Fundido de salida de 1,2 s al final.
- Iguala el nivel al de `tools/reel2/musica_r1.ogg` (la referencia).

## 7. Mezcla y control de calidad
- Voz: `loudnorm=I=-15:TP=-1.5:LRA=9`, en su propio paso.
- `sfx.py`: efectos al 0,32 con `amix normalize=0` y `alimiter 0.95`, sin `apad`.
- Música: entra con un segundo `amix`. Salen dos archivos: `reels/final/uNN-con-musica.mp4` y `reels/final/uNN-sin-musica.mp4`.
- El archivo de la cola es `reels/uNN-<slug>.mp4` (con música, h264, menos de 20 MB). Portada en `covers/uNN-<slug>.jpg`.
- Comprobaciones obligatorias:
  1. Nivel de audio segundo a segundo hasta el final.
  2. Saltos entre fotogramas: ningún fotograma suelto con una diferencia muy alta entre dos bajas; los únicos cortes son los cortes secos previstos.
  3. Nada de más de 2 s de imagen quieta.
  4. Seis fotogramas a tamaño completo revisados con Read.
- Si algo falla, se corrige y se vuelve a renderizar.

## 7b. Auditoría prepublicación (Agente 05)
MODO PREPUBLICACIÓN sobre el vídeo final (mira 8–10 fotogramas clave y escucha el plan de audio: tiempos de voz/música/SFX). Nota sobre 100. Si < 75 o hay un fallo objetivo (corte, texto ilegible, dato dudoso, CTA mal), corrige y vuelve a renderizar. Guarda en `agencia/criticas/AAAA-MM-DD-uNN-final.md` e incluye la nota en el mensaje a Biel.

## 8. Publicación, oficina y panel
- En la entrada de `queue.json` pon también `title` (el hook) y `score` (nota de Andrés). Después sincroniza «Contenido» de la oficina (`oficina/PROTOCOLO.md`, SALIDA): es donde Biel lo ve y lo corrige.
- `queue.json`: entrada `uNN` con `kind` reel, `status` pending, `campana` "unrespiro", `share_to_feed` false, `cover` y caption.
  - El caption lleva el gancho, 2–3 líneas, el CTA y «Enlace en la bio», más 4–5 hashtags.
- Panel (https://claude.ai/artifact/GdqV6tqCq39FJVtTLNe8f7):
  - Ejecuta `tools/panel_videos.py prep` y sube la vista previa con Artifact (`asset: true`).
  - Ejecuta `panel_videos.py add`, sube `panel_videos.json` y actualiza `datasets/videos` con ArtifactData (`if_version`).
  - Portada en `datasets/portadas`: descarga el blob, añade una miniatura de 160 px como data URL, súbelo y actualiza.
- Hoja `1QS35fBtDK5yBM7KJntmFbG4JN_HLX2gY5IkDPRP3Ddo`, pestaña Plan: añade la fila (id, fecha, hora, Reel, pieza, «Lista de espera», Programado, archivo).
- `agencia/HISTORIAL.md`: añade la fila del Reel.
- `git add -A`, commit (termina en «Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>»), `git pull --rebase` y `git push`.

## 9. Mensaje a Biel (corto)
El hook, el concepto visual en una línea, la hora a la que sale y que lo tiene en el panel para corregirlo antes.
Si algo no se ha podido hacer (por ejemplo, créditos de ElevenLabs agotados), dilo y no publiques un Reel incompleto.
