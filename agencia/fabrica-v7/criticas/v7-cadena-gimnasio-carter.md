# Crítica · v7-cadena-gimnasio-carter «La cadena del gimnasio» (historia con fotos)

## r1 · Andrés (05) · 28/11/2026 · Nota: 75/100 → NO APROBADO (suspenso automático: logo y «¿Te ha servido?» solapados sobre «SE CUMPLE»). Vuelve a montaje.

Material revisado: `tools/reel_v7/v7-cadena-gimnasio-carter/video_mudo.mp4` (26,4 s, 1080×1920; 53 fotogramas, uno cada 0,5 s, a 270 px, y fotogramas cada 0,2 s entre 20,4 y 23,0 s) y el vídeo final de la cola (`f519f727-…mp4`, 26,4 s), descargado y analizado en el sandbox de Higgsfield.

### Comprobaciones duras
- **Voz entera (faster-whisper small):** «Richmond, California, enero del 99. Su equipo va 13-0. Ken Carter pone una cadena en la puerta del gimnasio y un cartel. Os espero en la biblioteca. 15 de sus 45 jugadores no cumplen el contrato firmado. Deberes, puntualidad, primera fila en clase. Pierde dos partidos y el invicto. Pero el contrato se cumple.» Igual que «## Voz» del guion (las cifras se oyen en letra). «cumple.» acaba a 22,28 s.
- **Cierre nuevo:** voz «Dale like y síguenos para más vídeos como este» (22,72–25,58 s); en pantalla «¿Te ha servido? · Dale like y síguenos · PARA MÁS VÍDEOS COMO ESTE». El caption termina con el cierre nuevo. Nada de app, producto, lista de espera, lanzamiento ni fechas (voz, pantalla y caption).
- **Niveles:** −16,6 LUFS integrados, true peak −1,0 dBFS. Voz entre −14 y −20 dB RMS por segundo; final −23 dB (25 s) y −52 dB (26 s).
- **Datos:** todo con fuente en el guion (NPR 11/01/1999; George Fox Journal 2005; Contemporary Black Biography/Gale; Christianity Today 2005): 13-0, cadena y cartel a la biblioteca, 15 de 45 sin cumplir el contrato, deberes/puntualidad/primera fila, dos partidos y el invicto. El cartel va como paráfrasis, sin comillas. Bien.
- **Fotos y licencias:** Mx. Granger (CC0), TropicAces (CC BY-SA 3.0, modificada) y Annatsach (CC BY-SA 4.0, modificada; rotulada ILUSTRACIÓN), con crédito en pie y caption. La de Carter lleva «FOTO DE 2014» y la del instituto «HOY». Nada sugiere que nadie apoye ProTeam. Música Epidemic. Sin precios, sin nombre de Biel, sin cifras de apuntados.

### El bloqueante: texto solapado en el paso al cierre (22,4–23,0 s)
El paso al cierre es un **fundido cruzado**, no a negro. A **22,8 s** el logo «ProTeam» está encima del contrato con «SE CUMPLE» y de «Pero el contrato»; a **23,0 s** «¿Te ha servido?» sigue montado sobre el contrato a media opacidad. Es el mismo solape que ya se corrigió en Tacos de Berna, Rangnick, Lobanovski o Kerr. Por la regla de la casa (texto solapado) suspende.

### Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 10/20 | La historia es buena y el remate «el contrato se cumple» es citable, pero el gancho es «Richmond, California. Enero del noventa y nueve.», justo el «Lugar, año.» que no vale. El fotograma 0 solo tiene «Richmond,» y la fachada del instituto: no se ve ni el 13-0 ni la cadena. El dato raro (va invicto y cierra el gimnasio) no llega hasta los 3–5 s. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Bien sincronizado: calendario 1999 en «enero», palotes y «13 – 0», «CADENA» con el marco sobre la cadena, el cartel que se escribe, las 15 fichas que se apagan, las tres casillas en su palabra, el 13–0 que se agrieta con las dos fichas tachadas y el sello. Resta: a 11,5 s la pantalla está casi vacía (solo «15 de»); a 4,0 s el marcador sale vacío antes de los palotes. |
| Transiciones | 9/15 | Viajes suaves en general, pero el viaje de 20,4–20,9 s, de «Pierde dos partidos» a «Pero el contrato», cruza la pared entera hacia atrás (calendario, Carter, cartel, fichas pasan en medio segundo): se ve como un barrido brusco. Y el paso al cierre es un fundido cruzado con solape (bloqueante). |
| Sonido | 12/15 | Voz confiada y clara, música de piano real por debajo, efectos bajos y reales. Pero «Dale» entra a 22,72 s, solo 0,44 s después de «cumple»: el remate no respira y el cierre pisa la idea. |
| Verdad y fuentes | 15/15 | Todo con fuente; lo no comprobable (graduaciones, película en la voz) se deja fuera. |
| Estética | 12/15 | Paleta, tipografías y fotos bien; ultravioleta solo en «SE CUMPLE». Restan el solape del final, el remate que se ve entero menos de 1 s (21,8–22,6 s) y el pie de créditos del final, demasiado pequeño para leerse en el móvil. |
| **Total** | **75/100** | **No aprobado** (y suspenso automático por el solape). |

### Correcciones para Marta (02), por orden
1. **Fundido a NEGRO, no cruzado:** remate «SE CUMPLE» entero y quieto, con la cámara parada, ≥1,0 s después de «cumple» (22,28 s) → hasta ~23,3 s; fundido a negro 0,5 s; outro2 desde negro (~23,8 s). Mover a la vez la voz del cierre en mix.py para que «Dale» quede ≥1,3 s después de «cumple». Ningún fotograma con el logo o «¿Te ha servido?» sobre el contrato.
2. **Gancho (lo más caro y lo que más nota da):** el fotograma 0 tiene que llevar ya el dato raro: «13 – 0» con la cadena/candado (o «13–0» + «CADENA» sobre la foto de la puerta). Opción buena: voz nueva que empiece por el dato, p. ej. «Su equipo iba trece a cero. Y el entrenador cerró el gimnasio con una cadena.» y después «Richmond, California, enero del noventa y nueve» como contexto (es la primera línea del caption; pásalo a Dani si hay que tocar «## Voz»). Opción barata sin voz nueva: en el fotograma 0, encima de la ficha del instituto, el marcador «13 – 0» y la cadena dibujada ya visibles, con «Richmond,» pequeño.
3. **Viaje del remate (20,4–20,9 s):** no cruzar la pared entera hacia atrás; poner el contrato del remate cerca del marcador 13–0 (o un corte limpio con viaje corto) para que no pasen calendario, Carter y cartel en medio segundo.
4. **Hueco de 11,5 s:** que las 45 fichas entren con el final del viaje, no después (pantalla casi vacía con solo «15 de»).
5. **Pie de créditos final:** a 17 px y quieto ≥1,5 s, o fuera de pantalla (ya va en el caption).
6. Subir `video_mudo.mp4` nuevo con outro2 al repo y actualizar cola (files_old) y panel a la vez.

Opcional: el hashtag #ProTeam del caption es el nombre de la cuenta (como en los aprobados), no menciona la app; si se quiere ir sobre seguro en Fase 1, quitarlo.
