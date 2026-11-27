# v7-partido-secreto-mclendon · «El partido secreto» (historia con fotos)
Guion: agencia/fabrica-v7/guiones/v7-partido-secreto-mclendon.md (Dani B). Montaje v7: Marta A (02), 27/11/2026.

Voz (23,9 s, 59 palabras del guion sin cambios): «Durham, Carolina del Norte. Un domingo por la mañana. Casi toda la ciudad está en la iglesia; la policía, también. John McLendon atranca las puertas de su gimnasio. Sus Eagles, negros. Enfrente, estudiantes de medicina de Duke, blancos. La ley lo prohíbe. Ochenta y ocho a cuarenta y cuatro. Luego mezclan los dos equipos... y juegan otra vez. Juntos.»
ElevenLabs eleven_v4, voz Mateo (gpMzl7dbkfC9dIxAqQZT), una toma (440 créditos). En el prompt, para la pronunciación: «Dárham», «Macléndon», «Íguels», «Diuk»; «[lower, dry]» antes de «La ley lo prohíbe». Tiempos por palabra: faster-whisper small (words.js); están todas las palabras («88 a 44» y «En frente» en la transcripción).

Datos y fuentes: Scott Ellsworth (The New York Times Magazine, 1996, vía NCCU), The Chronicle (Duke), NC DNCR, Duke Today. Ver el guion.

Fotos (licencias comprobadas el 27/11/2026 en la API de Wikimedia Commons desde el sandbox de Higgsfield):
- At_the_bus_station_in_Durham,_North_Carolina._1940.jpg — Jack Delano (FSA/OWI, Library of Congress) — dominio público — https://commons.wikimedia.org/wiki/File:At_the_bus_station_in_Durham,_North_Carolina._1940.jpg — completa, B/N; rotulada «Durham · Carolina del Norte · 1940».
- Duke_Chapel.jpg — Gregw824 (English Wikipedia) — dominio público — https://commons.wikimedia.org/wiki/File:Duke_Chapel.jpg — recortada a la torre y en marco, rotulada solo «Durham». Se probó el recorte con rembg (isnet-general-use, alpha matting) y se comía la base del edificio: va en marco.
- “COLORED WAITING ROOM” and “HITLER’S LOVE LIFE REVEALED” - Jim Crow in Durham, North Carolina (cropped).jpg — Jack Delano (FSA/OWI, Library of Congress) — dominio público — https://commons.wikimedia.org/wiki/File:%E2%80%9CCOLORED_WAITING_ROOM%E2%80%9D_and_%E2%80%9CHITLER%E2%80%99S_LOVE_LIFE_REVEALED%E2%80%9D_-_Jim_Crow_in_Durham,_North_Carolina_(cropped).jpg — recortada al cartel (sin el titular del periódico ni caras).
- NCCU_McLendon–McDougald_Gymnasium_basketball.jpg — RDUpedia — CC BY-SA 3.0 — https://commons.wikimedia.org/wiki/File:NCCU_McLendon%E2%80%93McDougald_Gymnasium_basketball.jpg — recortada (sin el logo del centro de la pista) y graduada (obra derivada, misma licencia); rotulada «Hoy: gimnasio McLendon–McDougald».
Graduadas con tools/reel_v7/bielsa/grade.py (cut.py; las de 1940 en B/N). Calendario, campanario, banco y gorra, silueta de McLendon (sin cara), puertas y tranca, pista y fichas, tarjeta de medicina, sello y marcador: dibujados y rotulados «recreación». Sin escudos.

Ultravioleta #8B5CF6 una sola vez: «JUNTOS».

Música y efectos (Epidemic Sound, vía Higgsfield): «Musical, Loop, Jazz, Soft, Piano» y «Musical, Loop, Jazz, Soft, Piano, Bass» (encadenadas con 1,4 s; distintas de las de los v7 anteriores); «Swooshes, Whoosh, Soft, Clean»; «Paper, Friction, Sheet, Laminated, Slide On Wooden Table»; «Objects, Book, Flip Page»; «Ambience, Town, Village, Distant Church Bells»; «Doors, Wood, Close, Then Bolt Lock»; «Games, Misc, Chips, Token, Plastic, Down On Table»; «Office Supplies, Rubber Stamp, Document 01»; «Mechanical, Click, Switches, Button, Push, Small 02»; «Games, MIsc, Poker Chips, Stack, Shuffle». Mezcla: mix.py (voz −19, música −31 con ducking; resultado voz −19,0, música −33,3, sfx −34,4, pico 0,90).

Vídeo: video_mudo.mp4 (29,8 s: 24,2 s de historia + fundido de 0,6 s al cierre común), render a 30 fps con tools/blackout/htmlreel.py.
