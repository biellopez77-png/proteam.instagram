# v7-tres-filas-summitt · «Las tres primeras filas» (historia con fotos)
Guion: agencia/fabrica-v7/guiones/v7-tres-filas-summitt.md (Dani B). Montaje v7: Marta A (02), 27/11/2026.

Voz (19,2 s con las pausas, 52 palabras, texto del guion sin cambios): «Pat Summitt ganó ocho títulos nacionales con Tennessee. Y una de sus reglas no era de la pista. Era del aula: sus jugadoras, en las tres primeras filas de clase. Si una faltaba, banquillo. Todas las que terminaron su etapa se graduaron... Lo que exiges fuera de la pista se ve dentro.»
ElevenLabs eleven_v4, voz Mateo (gpMzl7dbkfC9dIxAqQZT), una toma (345 créditos), prompt con «[confident, assured, steady storyteller tone, firm and calm]» y el texto con su grafía real (la voz dice «Sámit» y «Ténesi» sin tocar el texto). Tiempos por palabra: faster-whisper small (words.js); están las 52 palabras (whisper escribe «Samit»: en words.js va «Summitt»). Para que quepan los viajes de cámara, la voz se abre 0,5 s en 3,40 s, 0,4 s en 5,94 s, 0,45 s en 11,95 s y 0,55 s en 14,57 s (la pausa del remate); words.js lleva esos desplazamientos.

Fotos (Wikimedia Commons, descargadas desde el sandbox de Higgsfield; licencias comprobadas por Dani B con la API de Commons):
- Pat-Summitt-Texas-vs-Tennessee-Dec-14-08.jpg (14/12/2008) — aaronisnotcool (Flickr) — CC BY 2.0 — https://commons.wikimedia.org/wiki/File:Pat-Summitt-Texas-vs-Tennessee-Dec-14-08.jpg — encuadrada sobre Summitt y recortada con rembg (isnet-general-use, alpha matting; fuera el halo de la gorra del policía de detrás), con ficha «PAT SUMMITT · TENNESSEE · ENTRENADORA».
- Tennessee Volunteers Basketball Thompson-Boling Arena.jpg — TN 66 — CC0 — https://commons.wikimedia.org/wiki/File:Tennessee_Volunteers_Basketball_Thompson-Boling_Arena.jpg — en polaroid, recortada sin el rótulo grande del parqué de la izquierda; una línea de banda dibujada se traza encima.
- Pat-Summitt-Walter-Reed-Center-06-24-08-2.jpg (24/06/2008; recorte de User:Blueag9) — Staff Sgt. Christina M. O'Connell (Ejército de EE. UU.) — dominio público — https://commons.wikimedia.org/wiki/File:Pat-Summitt-Walter-Reed-Center-06-24-08-2.jpg — a tamaño medio (350 px de ancho de marco, sin ampliar a pantalla completa), en ficha «PAT SUMMITT · 2008». El recorte solo muestra a Summitt, así que la ficha no dice «equipo campeón».
- No se usan las reservas.
Graduadas con tools/reel_v7/bielsa/grade.py (cut.py). Trofeos, aula, pupitres, mochilas, banquillo, birretes y pista del final: dibujados, genéricos (sin logos de Tennessee ni de la NCAA) y rotulados «recreación».

Ultravioleta #8B5CF6 una sola vez: la palabra «FUERA» del remate.

Música y efectos (Epidemic Sound, vía Higgsfield): «Musical, Loop, Logo, Calm, Piano 02» (encadenada consigo misma con fundidos de 1,4 s; distinta a las de los v7 anteriores); «Swooshes, Whoosh, Soft, Clean»; «Sheet, Laminated, Slide On Wooden Table 04»; «Flask, Metal, Empty, Set Down On Surface 04» (los ocho trofeos); «Communications, Camera, Analogue Film Camera, Shutter Clicks 02»; «Objects, Writing, Pen, Marker, Write, Short, Small» (línea de banda y tachón); «Objects, Writing, Chalk, Draw Lines On Blackboard 01»; «Chair, Small, Wooden, Down On Hard Ground 02» (filas 1, 2 y 3); «Office Supplies, Rubber Stamp, Document 01». Mezcla: mix.py (voz −19, música −31 con ducking).

Render: htmlreel (30 fps; en este contenedor Chromium se cuelga con las banderas de swiftshader, así que se renderizó sin ellas: la página no usa WebGL) y fundido de 0,6 s al cierre común en 19,4 s.

Vídeo final: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/a5f5ed71-9933-44db-a627-091d6f37eea9.mp4 (25,0 s: 19,4 s de historia + cierre común; comprobado con whisper: se oyen las 52 palabras; −17,2 LUFS, −1,0 dBTP).
