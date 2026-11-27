# v7-no-se-entrena-phog-allen · «Solo se juega» (historia con fotos)
Guion: agencia/fabrica-v7/guiones/v7-no-se-entrena-phog-allen.md (Dani B). Montaje v7: Marta A (02), 27/11/2026.

Voz (24,4 s con las pausas, 55 palabras, texto del guion sin cambios): «James Naismith inventó el baloncesto. Y a su alumno, Phog Allen, le dijo: "El baloncesto no se puede entrenar. Solo se juega". Allen no le hizo caso. Cincuenta temporadas en un banquillo. Setecientas cuarenta y seis victorias. De sus equipos salieron Adolph Rupp y Dean Smith... El juego se juega. Pero alguien tiene que enseñarlo.»
ElevenLabs eleven_v4, voz Mateo (gpMzl7dbkfC9dIxAqQZT), una toma (388 créditos), prompt con «[confident, assured, steady storyteller tone, firm and calm]»; en el prompt, «Néismiz», «Fog Alen» y «Alen» para la pronunciación (en pantalla, siempre la grafía real). Tiempos por palabra: faster-whisper small (words.js); están las 55 palabras (whisper escribe «Fog», «Adolf», «Rapp», «50», «746»: en words.js van «Phog», «Adolph», «Rupp», «Cincuenta», «Setecientas cuarenta y seis»). Para que quepan los viajes de cámara, la voz se abre 0,45 s en 2,64 s; 0,4 s en 5,16 y 10,58 s; 0,6 s en 15,46 s y 0,4 s en 18,7 s (la pausa del remate); words.js lleva esos desplazamientos.

Fotos (Wikimedia Commons, descargadas desde el sandbox de Higgsfield; licencias comprobadas por Dani B con la API de Commons):
- Dr. James Naismith.jpg (con balón y cesta, antes de 1939) — autor desconocido — dominio público — https://commons.wikimedia.org/wiki/File:Dr._James_Naismith.jpg — recortada con rembg (isnet-general-use, alpha matting), en ficha de prensa «SPRINGFIELD · KANSAS».
- Naismith Rules of Basketball 1892 first draft.jpg (borrador mecanografiado, dic. 1891) — James Naismith — dominio público — https://commons.wikimedia.org/wiki/File:Naismith_Rules_of_Basketball_1892_first_draft.jpg — solo la primera hoja, como un folio que se desliza.
- Phog Allen 1953.jpg — autor desconocido — dominio público — https://commons.wikimedia.org/wiki/File:Phog_Allen_1953.jpg — foto de periódico en ficha «ALUMNO · KANSAS» (sin recorte: el tramado no da para rembg).
- Kansas basketball team photo by Squires Studios, 1924.jpg — Squires Studio — dominio público — https://commons.wikimedia.org/wiki/File:Kansas_basketball_team_photo_by_Squires_Studios,_1924.jpg — solo la foto (sin titular ni pie del periódico); «COACH F. C. ALLEN» señalado en el segundo de los tres hombres de traje de la tercera fila, según el pie original («Third row: Baker, Trainer Kelley, Coach F. C. Allen, Capt. Charles Black, Assistant Coach John Bunn…»).
- No se usan las reservas.
Graduadas con tools/reel_v7/bielsa/grade.py (cut.py). Banco y 50 marcas, contador de victorias con fichas, sello «NO», fichas de Rupp y Smith (sin cara, con silbato) y pizarra: dibujados y rotulados «recreación».

Ultravioleta #8B5CF6 una sola vez: «ENSEÑARLO».

Música y efectos (Epidemic Sound, vía Higgsfield): «Musical, Loop, Calm Piano, Dreamy, Intro 04» (encadenada consigo misma con fundidos de 1,4 s; distinta a las de los v7 anteriores); «Swooshes, Whoosh, Soft, Clean»; «Sheet, Laminated, Slide On Wooden Table 04»; «Communications, Camera, Analogue Film Camera, Shutter Clicks 02»; «Office Supplies, Rubber Stamp, Document 01» (NO); «Objects, Writing, Pen, Marker, Write, Short, Small»; «Objects, Writing, Pencil On Paper, Letter H» (50 marcas); «Games, MIsc, Poker Chips, Single, Drop On Table» (746); «Whistles, Mechanical, Sport, Referee Whistle, 10 Metres Distance» (dos silbatos lejanos); «Sports, Court, Basketball, Indoor, Ball Bounce, Soft 01»; «Objects, Writing, Marker On Whiteboard». Mezcla: mix.py (voz −19, música −31 con ducking).

Render: htmlreel (30 fps) y fundido de 0,6 s al cierre común en 24,5 s.

Vídeo final: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/d01bc15a-1617-456b-a9f6-f7ff3547f94c.mp4 (30,1 s: 24,5 s de historia + cierre común; comprobado con whisper: se oyen las 55 palabras; −16,5 LUFS, −0,9 dBTP).
