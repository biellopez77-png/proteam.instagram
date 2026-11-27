# v7-chocolate-wenger-1996 · «Tienen hambre» (historia con fotos)
Guion: agencia/fabrica-v7/guiones/v7-chocolate-wenger-1996.md (Dani A). Montaje v7: Marta B (02), 27/11/2026.

Voz (25,2 s con las pausas, 59 palabras, texto del guion; en el prompt «1996» se escribió «mil novecientos noventa y seis» y «Arsène Wenger» como «Arsén Wénguer»; en pantalla, la grafía correcta): «1996. Arsène Wenger dirige su primer partido con el Arsenal. En el descanso, nadie habla. Pregunta al fisio qué pasa. «Tienen hambre». Les había quitado el chocolate de antes del partido. Ganan dos a cero, y en el autobús de vuelta cantan: «¡Queremos nuestras chocolatinas!». Y Wenger les pone pescado, brócoli y agua... El partido empieza en el plato.»
ElevenLabs eleven_v4, voz Mateo (gpMzl7dbkfC9dIxAqQZT), una toma (462 créditos), prompt con «[confident, assured, steady storyteller tone, firm and calm]». Tiempos por palabra: faster-whisper small (words.js); están todas las palabras. La voz se abre 0,3 s en 5,6, 13,42, 18,56 y 21,8 s para que quepan los viajes de cámara; words.js lleva esos desplazamientos.

Fotos (Wikimedia Commons, descargadas desde el sandbox de Higgsfield; licencias comprobadas con la API de Commons el 27/11/2026):
- Ewood Park 2011.jpg — Ronnie Macdonald from Chelmsford, United Kingdom — CC BY 2.0 — https://commons.wikimedia.org/wiki/File:Ewood_Park_2011.jpg — sin la mitad del techo, en ficha con «EWOOD PARK, BLACKBURN · FOTO DE 2011» y el sello «PARTIDO 1».
- Arsene Wenger 2009.jpg — Gordon Flood from Trim, Ireland — CC BY 2.0 — https://commons.wikimedia.org/wiki/File:Arsene_Wenger_2009.jpg — recortado con rembg, rotulado «FOTO DE 2009».
- Arsene Wenger directs the troops (7100604771).jpg — Ronnie Macdonald from Chelmsford, United Kingdom — CC BY 2.0 — https://commons.wikimedia.org/wiki/File:Arsene_Wenger_directs_the_troops_(7100604771).jpg — encuadrada solo en Wenger (sin las vallas publicitarias), en polaroid, rotulada «FOTO DE 2012».
- Broccoli florets on ice.jpg — Jeffery Martin — CC0 — https://commons.wikimedia.org/wiki/File:Broccoli_florets_on_ice.jpg — un círculo dentro del plato dibujado.
- No se usa la reserva.
Recorte y etalonaje (obra derivada; se mantienen crédito y licencia): cut.py con tools/reel_v7/bielsa/grade.py. Vestuario con camisetas genéricas (sin escudos), maletín, bandeja, chocolatina sin marca, marcador, autobús, plato, pescado, vaso y campo: dibujados y rotulados «recreación».

Ultravioleta #8B5CF6 una sola vez: «EN EL PLATO» del remate.

Música y efectos (Epidemic Sound, vía Higgsfield): «Musical, Loop, Piano, Sentimental, Fast 01» (encadenada consigo misma con un fundido de 1,4 s; distinta a las de los v7 anteriores); «Swooshes, Whoosh, Soft, Clean»; «Paper, Friction, Sheet, Laminated, Slide On Wooden Table»; «Objects, Office, Stamp Hand, Press, Mark, Short»; «Ambience, Room Tone, Medium Sized Locker Room» (muy baja); «Wood, Friction, Chair, Creaking, Big Room» (banco); «Mechanical, Latch, Briefcase, Handle, Slide Open, Close» (maletín); «Objects, Writing, Marker On Paper, Writing 01»; «Objects, Packaging, Candy, In Wrapper, Movement»; «Games, Misc, Playing Card, Single, Turn Over On Table, Flip» (tablillas); «Vehicles, Generic By, Bus, Pass By, Medium Speed, Asphalt»; «Communications, Camera, Analogue Film Camera, Shutter Clicks 02»; «Ceramics, Impact, Plate, Put Down, Clink»; «Water, Pour, Into Glass 03». Mezcla: mix.py (voz −19, música −31 con ducking).

Render: htmlreel (30 fps) y fundido de 0,6 s al cierre común en 25,4 s. Hoja de contacto (1 fps) revisada a tamaño móvil; corregidos antes del render: «PRIMER PARTIDO» pisaba la foto de Wenger (ahora en dos líneas) y «HAMBRE» se cortaba en el bocadillo.

Vídeo final: https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/e2d34f17-309c-4ed7-90ce-8c3f9f39b1e9.mp4 (31,0 s: 25,4 s de historia + cierre común; comprobado con whisper: se oyen todas las palabras de la voz; −17,7 LUFS, −1,0 dBTP).
