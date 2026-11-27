# v7-lenguaje-corporal-auriemma · «Da igual lo bueno que seas» (historia con fotos)
Guion: agencia/fabrica-v7/guiones/v7-lenguaje-corporal-auriemma.md (Dani B). Montaje v7: Marta B (02), 27/11/2026.

Voz (20,78 s, 60 palabras, texto del guion sin cambios): «Más de cien partidos seguidos sin perder. Es el UConn femenino de Geno Auriemma. Aun así, sentó en el banquillo a su estrella, Breanna Stewart. Según él, se portaba como una niña de doce años. Con mal lenguaje corporal no juegas. Nunca. Da igual lo bueno que seas... El talento te pone en la lista; la actitud, en la pista.»
ElevenLabs eleven_v4, voz Mateo (gpMzl7dbkfC9dIxAqQZT), una toma (382 créditos). En el prompt, «Yucón», «Yino Oriema» y «Brianna Stiuart» para que se lean como pide el guion. Tiempos por palabra: faster-whisper small (words.json / words.js); están las 60 palabras (whisper escribe «100», «yucon», «Gino Oriema» y «12»: se oyen como en el guion). Pausa del «...» antes del remate: 0,30 s.

Datos y fuentes: NBC Connecticut (24/03/2017), KARE 11, FootballScoop; apoyo The Daily Orange y Patch (ver el guion). «Más de cien» sin cifra exacta (las fuentes dicen 108 o 109). La frase final es nuestra y no se atribuye a Auriemma.

Fotos (Wikimedia Commons, descargadas el 27/11/2026 desde el sandbox de Higgsfield; autor y licencia comprobados en la API de Commons):
- Geno-Auriemma-UConn-vs-Texas-3-23-08.jpg (23/03/2008) — Aaron V. (recorte de Blueag9) — CC BY 2.0 — recortada y graduada (B/N con el azul) en ficha «GENO AURIEMMA · UCONN». Marcada «modificada».
- Harry A. Gampel Pavilion - University of Connecticut - DSC09954.JPG — Daderot — CC0 — graduada, postal «UCONN · GAMPEL PAVILION».
- Breanna Stewart 2015.jpg (Wade Trophy, 335×562) — Sphilbrick — CC BY-SA 4.0 — graduada, tarjeta con estrella dibujada. Marcada «modificada».
- UConn Huskies at Minnesota Golden Gophers women's basketball (Nov. 19, 2023) 070 (53345964171).jpg — John McClellan (John Mac) — CC BY-SA 2.0 — recortada y graduada, rótulo «UCONN, 2023». Marcada «modificada».
Preparación: cut.py. Se probó rembg (u2net_human_seg) en Auriemma y Stewart: el recorte arrastraba caras del público y abría un hueco en el trofeo, así que las cuatro van enmarcadas.
Dibujados y rotulados: fichas «W» y contador «100+» («recreación»), banquillo, pizarra con siluetas (sin cara), sello, lista y pista («dibujo»).

Ultravioleta #8B5CF6 una sola vez: sello «NUNCA». Cierre: fundido a negro de 0,5 s desde 21,38 s (0,6 s después de la voz) al cierre común tools/reel_v6/outro/outro2.mp4; la voz del cierre entra a 21,68 s.

Música y efectos (Epidemic Sound, vía Higgsfield): «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» y «… Logo 02», encadenadas con fundido de 1,4 s (distintas de la del último v7, «Orchestra, Piano, Choir, Sentimental»); «Swooshes, Whoosh, Soft, Clean»; «Games, Misc, Chips, Tokens, Plastic, Multiple, Down On Table»; «Paper, Friction, Sheet, Laminated, Slide On Wooden Table»; «Communications, Camera, KMZ Zenit 12XP Camera, Shutter 03»; «Objects, Writing, Marker On Whiteboard»; «Wood, Impact, Soft Knock On Tree Log»; «Office Supplies, Rubber Stamp, Document 01»; en el cierre, «Musical, Loop, Logo, Calm, Piano 01» bajo (0,22). Mezcla: mix.py (voz −19,0, música −33,3 con ducking, sfx −38,1, pico 0,90); final −17,0 LUFS, −1,0 dBTP.

Vídeo final: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/21a4223e-c0d6-4953-96a7-1c3dd03c06fa.mp4 (25,4 s: historia hasta 21,88 s con fundido desde 21,38 s al cierre outro2, sin app). Comprobado con whisper small: se oye la voz entera y «Dale like y síguenos para más vídeos como este».
Caption: la del guion; el bloque de fuentes y los hashtags van antes para que termine con «¿Te ha servido? Dale like y síguenos para más vídeos como este.».
