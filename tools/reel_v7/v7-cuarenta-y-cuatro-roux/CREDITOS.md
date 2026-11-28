# v7-cuarenta-y-cuatro-roux · «Un equipo no se ficha» (historia con fotos)
Guion: agencia/fabrica-v7/guiones/v7-cuarenta-y-cuatro-roux.md (Dani A). Montaje v7: Marta A (02), 27/11/2026.

Voz (21,8 s, 51 palabras, texto del guion sin cambios): «En 1961, el Auxerre jugaba en Regional. Lo cogió un entrenador-jugador: Guy Roux. En 1980 lo subió a Primera. Abrió una cantera, y de allí salió Eric Cantona. En 1996 ganó Liga y Copa. Cuarenta y cuatro años en el mismo banquillo. La idea... un equipo no se ficha: se construye.»
ElevenLabs eleven_v4, voz Mateo (gpMzl7dbkfC9dIxAqQZT), una toma (404 créditos). En el prompt, los años en letra y la pronunciación escrita («Oxér», «Gui Ru»). Tiempos por palabra: faster-whisper small (words.json / words.js); están las 51 palabras (lo transcribe «Oxer» y «Rue»; «cuarenta y cuatro» como «44»).

Datos y fuentes: UEFA.com («Roux stands down after 44 years»), Wikipedia («Guy Roux», «AJ Auxerre»), Inside Futbol (2011). Ver el guion.

Fotos (licencias comprobadas el 27/11/2026 en la API de Wikimedia Commons desde el sandbox de Higgsfield). Todas enmarcadas, sin recorte de fondo (cut.py):
- Auxerre_-_Stade_Abbé-Deschamps_(42).jpg — Vicente Auxerre — CC BY-SA 3.0 — recortada (sin el cielo), B/N con el azul; pie «Estadio Abbé-Deschamps, Auxerre (foto actual)» para no darla por de 1961. Ficha «AJ AUXERRE · AUXERRE · 1961».
- Guy_Roux-AJ_Auxerre.jpg (2003) — BaDaJi_ArPiLuRe — CC BY-SA 3.0 — en marco tipo polaroid, B/N con el azul (el chándal); pie «Guy Roux en Auxerre, 2003».
- Eric_Cantona_Cannes_2009.jpg — Georges Biard — CC BY-SA 3.0 — en marco, B/N sin azul; pie «Eric Cantona en Cannes, 2009». CAMBIO SOBRE EL GUION: la propuesta (Cantona,_Eric.jpg, Stan Wiechers) es la foto de una página de revista (Cantona y Beckham con la camiseta del Manchester United y un código QR): la licencia de la foto original no está clara y sale otra persona. Se usa la de Cannes.
- Guy_Roux_2008.jpg (25/8/2008) — Nicolas Richoffer — CC BY-SA 4.0 — recortada a cabeza y hombros, B/N con el azul (la camisa); pie «Guy Roux en 2008».
Graduadas con tools/reel_v7/bielsa/grade.py. Escalera de cuatro peldaños (4.º nivel → Primera), silbato, botas, pizarra con conos y chapas, trofeos genéricos, calendario y banquillo: dibujados y rotulados «dibujo». Sin escudos ni logotipos dibujados.

Ultravioleta #8B5CF6 una sola vez: «CONSTRUYE».

Música y efectos (Epidemic Sound, vía Higgsfield): «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» (encadenada consigo misma tres veces con fundidos de 1,4 s); «Swooshes, Whoosh, Soft, Clean»; «Paper, Friction, Sheet, Laminated, Slide On Wooden Table»; «Games, Board, Playing Pieces, Plastic Token, Single, Play, Drop On Board»; «Communications, Camera, KMZ Zenit 12XP Camera, Shutter 02»; «Objects, Writing, Marker On Paper, Writing 02»; «Objects, Misc, Traffic Cone, Drop 03»; «Metal, Impact, Metal Cup, Rubber Impact, Soft Rattle»; «Objects, Book, Magazine, Thick, Pages, Flip, Fast»; en el cierre, «Musical, Loop, Logo, Calm, Piano 01» bajo (0,22). Mezcla: mix.py (voz −19,0, música −33,4 con ducking, sfx −37,0, pico 0,90); final −17,2 LUFS, −0,9 dBTP.

Vídeo final: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/1565e42c-a41b-4d42-a955-941559021796.mp4 (26,4 s: 22,42 s de historia + cierre sin app, tools/reel_v6/outro/outro2.mp4 con fundido de 0,5 s). Comprobado con whisper small: se oyen las 51 palabras y «Dale like y síguenos para más vídeos como este».
Caption: la del guion con los créditos de foto actualizados (Georges Biard en lugar de Stan Wiechers) y el cierre «¿Te ha servido? Dale like y síguenos para más vídeos como este.».

## r2 (28/11/2026, Marta A · crítica de Andrés 78/100)
Mismas fotos, voz, música, efectos, datos y caption. Cambios en reel.html: gancho desde el fotograma 0 (estadio, ficha «AUXERRE · 1961», escalera con la ficha en «REGIONAL» y sello «44 AÑOS · MISMO BANQUILLO» que se apaga antes de «Lo cogió»); escena de Guy Roux más abajo con la ficha grande («GUY ROUX» / «ENTRENADOR Y JUGADOR»); pizarra y Cantona 220 px más abajo; trofeos más grandes y bajos; calendario 1961→2005 y «44 AÑOS» en «Cuarenta»; créditos del pie a 21 px; la cámara se para a 21,4 s, remate quieto hasta 22,9 s y fundido a NEGRO de 0,5 s; outro2 desde 23,4 s.
Mezcla: mix_r2.py (historia 0–22,38 s de la mezcla r1; «Soft Piano, Strings, Calm, Intro, Logo 01» sigue en su sitio en el respiro y baja bajo el cierre; outro2 y el sting «Musical, Loop, Logo, Calm, Piano 01» (0,22) a 23,40 s; ambas pistas descargadas de nuevo para esta versión). Final −17,3 LUFS, pico −1,0 dBFS, LRA 3,6.
Vídeo final r2: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/0da2e422-500e-4ae2-9d51-1b0d25cf0d44.mp4 (27,4 s). Whisper small: las 51 palabras de la voz y, después, «Dale like y síguenos para más vídeos como este» (23,3–26,6 s).
