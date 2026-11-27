# Crítica · v7-partido-secreto-mclendon «El partido secreto» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 84/100 → NO SALE (a remontaje con Marta, tarea «Montar v7 v7-partido-secreto-mclendon»).** Se queda a un punto: la historia, los datos y las fotos están bien; falla el final (el remate no respira) y dos detalles visuales.

Material revisado: el vídeo de la cola (`publicar/cola.json` → `b6996647-…mp4`, 27,7 s, 1080×1920, 30 fps, H.264 + AAC), descargado en el sandbox de Higgsfield: 55 fotogramas, uno cada 0,5 s, a 270 px de ancho (tamaño móvil), y el tramo 22,9–24,3 s a 10 fps. Ojo: `tools/reel_v7/v7-partido-secreto-mclendon/video_mudo.mp4` del repo es el antiguo (29,8 s, cierre común); el vídeo que he auditado es el de la cola, ya con outro2.

## Comprobaciones duras
- **Sin app, producto, lista de espera ni lanzamiento:** ni en la voz ni en pantalla ni en el caption de la cola. El cierre es outro2: en pantalla «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este»; en la voz, «Dale like y síguenos para más vídeos como este» (24,18–26,88 s). Caption de la cola termina con el cierre nuevo.
- **Panel:** el post del panel aún tenía el caption viejo («Estamos terminando la app de ProTeam…») y el vídeo viejo (`c4b3d95b`). Corregido por Andrés: caption = el de la cola, vídeo = `b6996647`. **No debe salir nada desde el panel con el caption viejo.**
- **Voz entera (faster-whisper small):** «Darham, Carolina del Norte, un domingo por la mañana. Casi toda la ciudad está en la iglesia. La policía también. John MacLendon atranca las puertas de su gimnasio. Sus seagwells negros. En frente, estudiantes de medicina de Duke, blancos. La ley lo prohíbe. 88 a 44. Luego mezclan los dos equipos y juegan otra vez. Juntos.» Están todas; «Sus Eagles» sale pegado («seagwells», 11,04–11,86 s).
- **Niveles:** −17,4 LUFS integrados, pico −1,5 dBFS, LRA 3,8 LU. Voz entre −16 y −21 dB RMS por medio segundo; huecos solo con música entre −28 y −33. Efectos bajos. Música real (Epidemic, jazz suave de piano), no sintetizada.
- **Fotos:** Jack Delano 1940 (dominio público), Duke Chapel de Gregw824 (dominio público), gimnasio McLendon–McDougald de RDUpedia (CC BY-SA 3.0, rotulado «HOY … FOTO (2011)»). Ninguna sugiere apoyo a ProTeam; sin escudos ni logotipos. McLendon en silueta sin cara.
- Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel. Ultravioleta solo en «JUNTOS».

## Verdad y fuentes
Todo lo que dice la voz está en las fuentes del guion (Ellsworth en NYT Magazine 1996 vía NCCU, The Chronicle, NC DNCR, Duke Today): domingo 12/03/1944 en Durham; la ciudad y la policía en la iglesia; puertas atrancadas; Eagles negros contra estudiantes blancos de medicina de Duke; ilegal por Jim Crow; 88-44; después mezclaron los equipos y jugaron otro partido. El calendario «MARZO · DOMINGO 12» es correcto. Caption bien.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Gran historia con remate. Pero arranca con «Durham, Carolina del Norte»: contexto, no gancho. La intriga (ciudad en la iglesia, puertas atrancadas) llega a los 4–8 s. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Calendario en «domingo», campanario y gorra en el banco en «policía», puertas y tranca en «atranca», fichas en dos tandas, tarjeta MEDICINA · DUKE, sello PROHIBIDO, marcador hasta 88–44, JUNTOS. Fallan: el marcador sube por separado y deja leer «87 – 0» y «88 – 5» (18,0–18,5 s); y la foto 1 (0–3,5 s) ya enseña el cartel «COLORED WAITING ROOM», que es justo la foto de «La ley lo prohíbe»: se adelanta el golpe y la imagen se repite. |
| Transiciones | 11/15 | Viajes suaves por la pared. Pero el final es brusco: «JUNTOS» está entero solo de ~23,5 a ~23,8 s y a 23,9 s ya entra el fundido a outro2. El remate no se queda quieto ni 0,5 s. |
| Sonido | 12/15 | Voz confiada y clara, música suave y efectos bajos. «Juntos» acaba a 23,90 s y la voz del cierre entra a 24,18 s: 0,28 s, el remate no respira. «Sus Eagles» suena pegado. |
| Verdad y fuentes | 15/15 | Todo comprobado. |
| Estética | 13/15 | Paleta, tipografías y ultravioleta una vez, correctos; nada cortado salvo en los viajes. El pie de créditos (22–24 s) y los pies de foto no se leen en el móvil. |
| **Total** | **84/100** | |

## Correcciones para el remontaje (Marta)
1. **Final (23,3–24,9 s):** «JUNTOS» entero y quieto al menos 1,0 s (de ~23,4 a ~24,4 s), cámara parada; fundido de 0,5 s a outro2 desde ~24,4 s; la voz del cierre entra ~0,3 s después del inicio del fundido (≈24,7 s). En la mezcla, mueve outro2 y su sting a la vez (como en Reep y Luis Enrique).
2. **Foto 1 (0–3,5 s):** recorta la estación de Durham para que no se vea el cartel «COLORED WAITING ROOM» (quédate con el autobús y el andén, mitad derecha), o usa otra foto de Durham de 1940. El cartel debe aparecer por primera vez en «La ley lo prohíbe».
3. **Marcador (17,9–19,3 s):** que los dos números suban a la vez y en proporción (0–0 → 44–22 → 88–44), para que no se lea «87 – 0» ni «88 – 5».
4. **Pie de créditos y pies de foto:** a 17 px como mínimo y que el pie final dure ≥ 1,5 s quieto (puede ir junto al remate).
5. **Voz (opcional):** si se puede sin tomar otra voz, abrir 0,1–0,15 s entre «Sus» y «Eagles» en la mezcla; si no, se queda.
6. **Gancho (para la próxima, no obligatorio aquí):** abrir con lo que intriga («Un domingo de 1944, un entrenador atranca las puertas de su gimnasio…») y dar el lugar después.
7. Sube el `video_mudo.mp4` nuevo al repo (el del repo es el de 29,8 s con el cierre común) y pon el vídeo nuevo en la cola y en el panel.
