# v7-camiseta-gris-ferguson · «La camiseta gris» (historia con fotos)
Guion: agencia/fabrica-v7/guiones/v7-camiseta-gris-ferguson.md (Dani A). Montaje v7: Marta B (02), 27/11/2026.

Voz (23,9 s con las pausas, 60 palabras, texto del guion sin cambios): «The Dell, Southampton. Al descanso, el Manchester United pierde tres a cero. Alex Ferguson entra en el vestuario: «Quitaos esa camiseta». Era gris. El club tenía una experta en visión: entre el público, el gris se ve tarde. Salen de azul y blanco... y la segunda parte la ganan uno a cero. Para pasársela a alguien, primero hay que verlo.»
ElevenLabs eleven_v4, voz Mateo (gpMzl7dbkfC9dIxAqQZT), una toma (456 créditos), prompt con «[confident, assured, steady storyteller tone, firm and calm]» y acotaciones para la orden («seca y baja»), «Era gris» (corta) y el remate (lento y firme). Tiempos por palabra: faster-whisper small (words.js): están las 60 palabras. Para que quepan los viajes de cámara, la voz se abre en 5,65 (+0,4 s), 10,63 (+0,5), 15,15 (+0,4) y 19,19 (+0,6, la pausa del remate); words.js lleva esos desplazamientos.

Fotos (Wikimedia Commons, descargadas desde el sandbox de Higgsfield; licencias comprobadas por Dani A con la API de Commons):
- Inside The Dell. - geograph.org.uk - 111405.jpg (marzo de 1997) — Colin Smith (geograph.org.uk) — CC BY-SA 2.0 — https://commons.wikimedia.org/wiki/File:Inside_The_Dell._-_geograph.org.uk_-_111405.jpg — en ficha de prensa «THE DELL · SOUTHAMPTON · 1997»; la franja de vallas publicitarias va desenfocada para que no se lean marcas; B/N con el azul conservado. La obra derivada se comparte con la misma licencia.
- Alex Ferguson mars 1992.JPG (marzo de 1992) — Øyvind Vik — dominio público — https://commons.wikimedia.org/wiki/File:Alex_Ferguson_mars_1992.JPG — recortado con rembg (isnet-general-use, alpha matting), en ficha «ALEX FERGUSON · ENTRENADOR» con el año de la foto en el pie (no es del partido).
- The Dell.jpg (Milton Road End, 2000) — Dan Kerins — CC BY 2.5 — https://commons.wikimedia.org/wiki/File:The_Dell.jpg — encuadrada en el arco y la pared de ladrillo, sin el escudo ni el rótulo del club; en marco «THE DELL · 2000».
- No se usa la reserva (Ferguson, 1996).
Graduadas con tools/reel_v7/bielsa/grade.py (cut.py). Marcadores, camisetas lisas (sin escudo, patrocinador ni marca), vestuario, muestra «GRIS», tarjeta de visión, grada y campo: dibujados y rotulados «recreación». La experta en visión no se nombra en pantalla (solo en el caption).

Ultravioleta #8B5CF6 una sola vez: «VERLO».

Música y efectos (Epidemic Sound, vía Higgsfield): «Musical, Loop, Piano, Intro, Tv» (encadenada consigo misma con fundidos de 1,4 s; no usada en los v7 anteriores); «Swooshes, Whoosh, Soft, Clean» (viajes); «Crowds, Sport, Football, Stadium, Half Time, Audience Walla» (grada lejana y murmullo); «Sheet, Laminated, Slide On Wooden Table 04» (fichas y tarjeta); «Mechanical, Click, Button, Press, Old, Metallic» (clics del marcador); «Communications, Camera, Analogue Film Camera, Shutter Clicks 02» (Ferguson y la ficha de la experta); «Doors, Hardware, Metal, Interior, Reverberant Room, Open» (puerta del vestuario); «Cloth, Impact, Shorts, Drop On Wood» (camisetas); «Footsteps, Human, Cleat Shoes, Football, Walk, Medium, Metal Plate Under Shoe» (tacos); «Objects, Writing, Marker On Whiteboard» (tachón de la primera parte); «Sports, Field, Football, Kick Ball, Soft To Medium» (el pase). Mezcla: mix.py (voz −19, música −31 con ducking; efectos 0,06–0,14).

Render: htmlreel (30 fps) y fundido de 0,6 s al cierre común en 24,1 s; video_mudo.mp4 a crf 26.

Vídeo final: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/9c063427-b149-4b35-b3c8-ba2b753035a9.mp4 (29,7 s: 24,1 s de historia + cierre común; comprobado con whisper: se oyen las 60 palabras; −16,5 LUFS, −0,8 dBTP).

## r2 (27/11/2026, Marta B) tras la crítica de Andrés (80/100)
- Remate: la cámara se para a 23,5 s; «VERLO.» entero en ultravioleta desde 23,9 s y quieto hasta 24,9 s; fundido de 0,5 s a negro (24,9–25,4 s) y después el cierre común tools/reel_v6/outro/outro2.mp4 (sin solape con el logo).
- Sonido: mix_r2.py (misma voz, música y efectos); la voz de outro2 («Dale like y síguenos para más vídeos como este») entra a 25,38 s, 1,5 s después de «verlo»; la música sigue bajando bajo el cierre.
- Jersey de Ferguson: dibujo y rótulo del pecho difuminados (cut.py, blur_chest).
- Vídeo final r2: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/43e36bd4-ec58-49e9-9dd6-7164a4777927.mp4 (29,4 s; whisper: 60 palabras + cierre; −16,9 LUFS, −1,0 dBTP).
