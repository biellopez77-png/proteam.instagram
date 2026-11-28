# Crítica · v7-carta-villas-boas-robson «La carta al vecino» (historia con fotos)

**Andrés (05) · 28/11/2026 · Nota: 78/100 → NO SALE (a remontaje con Marta, tarea «Montar v7 v7-carta-villas-boas-robson»).** La historia es de las mejores del lote (un chaval escribe al míster y años después le gana una final al jugador por el que preguntaba) y los datos están bien. Falla el gancho: abre con «Oporto, años noventa.», justo el arranque «Lugar, año.» que el criterio prohíbe. También hay textos cortados en los viajes, una ficha que se pinta encima de otra a 19,0 s y un remate que solo se queda quieto medio segundo.

Material revisado: el vídeo de la cola (`publicar/cola.json` → `f3e2302d-…mp4`, 25,7 s, 1080×1920, 30 fps, AAC 48 kHz), descargado en el sandbox de Higgsfield; `tools/reel_v7/v7-carta-villas-boas-robson/video_mudo.mp4` (25,67 s, con outro2): 51 fotogramas, uno cada 0,5 s, a 270 px (tamaño móvil), y fotogramas sueltos a 9,5 / 13,5 / 19,0 / 21,0 / 21,4 s a 540 px.

## Comprobaciones duras
- **App, producto, lista de espera o lanzamiento:** no aparecen ni en la voz, ni en pantalla, ni en el caption. ✔
- **Cierre outro2:** en pantalla («ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este») y en la voz («Dale like y síguenos para más vídeos como este», 21,90–24,80 s). El caption de la cola termina con el cierre. ✔
- **Panel:** el caption del post terminaba con los hashtags, no con el cierre. Lo he corregido: ahora es igual que el de la cola, que termina con el cierre y dice «modificadas» en los créditos.
- **Voz entera (faster-whisper small):** «Oporto, años 90. Un chaval de 16 años escribe a su vecino. Bobby Robson, entrenador del Oporto. Le pregunta por qué no juega Domingos. Robson le mete en el club y le manda a formarse como entrenador. En 2011 ese chaval gana la Europa League con 33 años. El entrenador rival, Domingos. Escucha al que pregunta.» Coincide con «## Voz» (57 palabras; whisper pone los números en cifra). «pregunta» acaba a 21,08 s.
- **Niveles:** −15,8 LUFS integrados, true peak −1,0 dBFS, LRA 2,3 LU. RMS por segundo entre −13,5 y −21 dB con voz; −32 dB en el negro (21 s). Música real de Epidemic (piano y pizzicato), suave bajo la voz, y efectos bajos. ✔
- **Fotos:** Threeohsix (CC BY-SA 4.0), Rob Bogaerts/Anefo (CC0), Miguel Silva Rodrigues (CC BY 2.0) y Vladimir Maiorov (CC BY-SA 1.0). Tienen el escudo, el logo del trofeo y las vallas difuminados o fuera de cuadro, y nada sugiere que alguien apoye ProTeam. ✔
- No hay precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel. El ultravioleta sale una sola vez, en «33 AÑOS». ✔

## Verdad y fuentes
Todo lo que se dice está en las fuentes del guion:
- El bloque compartido con Robson: Wikipedia y The Irish Times.
- La carta a los 16 por Domingos: Al Jazeera/Reuters 2011, The Irish Times y UEFA 17/05/2011.
- Que Robson le metió en el club y le mandó a los cursos: UEFA (palabras de Villas-Boas), Al Jazeera y Wikipedia.
- La Europa League 2011 con 33 años y 213 días, 1–0 al Braga en Dublín: UEFA 13/05/2011 y Guinness.
- Domingos Paciência como entrenador del Braga: Al Jazeera, The Irish Times y UEFA.

«Años noventa» encaja: Robson entrenó al Oporto de 1994 a 1996 y Villas-Boas cumplió 16 en 1993. En pantalla, «DUBLÍN · 18-05-2011», «1–0» y el contador 16 → 33 «de la carta a la final» son correctos. Lo dibujado va rotulado como «recreación» o «dibujo». Caption correcto. 15/15.

## Línea de tiempo (lo que se ve)
- **0,0–1,6 s:** «Oporto,» + postal de la maqueta de Das Antas, y luego «años noventa.» y el rótulo ESTÁDIO DAS ANTAS. El primer fotograma tiene foto y palabra, ✔. Pero el gancho es «Lugar, época» y no el dato raro, ✘.
- **1,5 s:** viaje con «rto, años noventa.» y el rótulo cortados por el borde izquierdo. ✘ (leve)
- 2,0–4,6: bloque de pisos, se enciende una ventana, «16 AÑOS», la hoja se escribe sola y «vecino:» en su palabra. ✔
- 5,0–7,3: ficha de Bobby Robson en «Bobby», con «ENTRENADOR DEL OPORTO» en su palabra. ✔
- 7,5–9,4: «Le pregunta…», la pregunta se escribe en la hoja y la ficha «9 · DOMINGOS» aparece en el banquillo. ✔
- **9,5 s:** viaje con «Doming…» y la hoja cortados por el borde derecho. ✘ (leve)
- 10,0–13,2: la ficha de Robson se gira y sale la acreditación «FC OPORTO · OBSERVACIÓN» en «club»; sellos ESCOCIA / INGLATERRA / TÍTULO en «formarse como entrenador». ✔
- **13,5 s:** viaje con la acreditación cortada por arriba y «En 2011,» casi invisible sobre la pared vacía. ✘ (leve)
- 14,0–17,2: portada «DUBLÍN · 18-05-2011», marcador 1–0, ficha de Villas-Boas y contador 16 → 22 → 33, con «33 AÑOS.» ultravioleta en su palabra. ✔ Muy bien.
- **17,5 s:** viaje con «…ague», «3» y «S.» cortados. ✘ (leve)
- 18,0–19,8: «¿El entrenador rival?» y la ficha de Villas-Boas «33 años» VS… **A 19,0 s la ficha «9 · DOMINGOS» entra deslizándose ENCIMA de «VILLAS-BOAS» y de «VS» (los textos se pisan unos 0,3 s).** ✘ Después «DOMINGOS…» en grande. ✔
- 20,1–21,1: «Escucha al que pregunta.» palabra a palabra, la hoja de la pregunta vuelve y «pregunta.» sale en azul. ✔
- **21,0–21,6:** remate completo y quieto solo ~0,55 s (de 21,08 a 21,64 s). El pie de créditos (~8 px a 1080, ilegible en el móvil) sale ~0,6 s. ✘
- 21,64–22,14: fundido a negro, limpio. ✔ 22,1–25,7: outro2 limpio. ✔
- La voz del cierre («Dale») entra 0,82 s después de «pregunta»: no llega al segundo que pedimos.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 12/20 | Historia redonda, distinción clara (escuchar al que pregunta ≠ apartarlo) y remate citable. Pero el gancho es «Oporto, años noventa.», el «Lugar, año.» que el criterio prohíbe. El dato raro (un chaval de 16 escribe al míster de su equipo) no llega hasta los 2,2 s. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Casi todo cae en su palabra: ventana, 16 AÑOS, vecino, ficha de Robson, pregunta, Domingos, club, sellos, Dublín, contador 33 y DOMINGOS…. «En 2011» (13,6 s) cae en pleno viaje, sobre la pared vacía. Además, el guion pedía alejar la cámara al final para ver toda la pared y no se hace. |
| Transiciones | 10/15 | Los viajes y el fundido a negro final son suaves. Pero cuatro viajes dejan texto cortado por el borde (1,5 / 9,5 / 13,5 / 17,5 s), la ficha de Domingos se pinta encima de la de Villas-Boas y el remate solo está quieto ~0,55 s (pedimos ≥ 1,0 s). |
| Sonido | 13/15 | La voz es confiada y clara, la música real y suave y los efectos bajos: −15,8 LUFS y −1,0 dBTP. Pero «Dale» entra a 0,82 s de «pregunta» y el remate no respira. |
| Verdad y fuentes | 15/15 | Todo comprobado. |
| Estética | 11/15 | Paleta, tipografías y fotos con licencia bien, sin escudos y con el ultravioleta una sola vez. Fallan los textos cortados en los viajes, el solapado de las fichas a 19,0 s y el pie de créditos final ilegible. |
| **Total** | **78/100** | |

## Correcciones para el remontaje (Marta)
1. **Gancho (0–2 s), lo principal.** Hay que quitar «Oporto, años noventa.» de la primera frase. Propuesta de voz (Dani A tiene que meterla en el guion como «## Revisión viral»): «Con dieciséis años, un chaval escribe a su vecino: Bobby Robson, entrenador del Oporto. Le pregunta por qué no juega Domingos…» y el resto igual. En el fotograma 0 tienen que estar ya «16 AÑOS» y la hoja de libreta (o la ficha de Robson). La postal «OPORTO · AÑOS 90» pasa a la segunda frase como rótulo, sin voz de lugar y año. Si se regraba, que sea con el mismo prompt y la misma voz (Mateo, eleven_v4).
2. **Ficha de Domingos (18,8–19,3 s).** Que entre por su hueco a la derecha del «VS» sin pasar por encima de «VILLAS-BOAS» ni de «VS». Puede entrar desde la derecha o desde abajo, o aparecer en su sitio con un pequeño escalado.
3. **Viajes sin texto cortado (1,5 / 9,5 / 13,5 / 17,5 s).** Apaga los textos y fichas de la escena antes de que empiece el viaje, como en Coerver o en Haskins, y enciende los de la siguiente cuando la cámara ya haya llegado. Que «En 2011,» no se escriba sobre la pared vacía: que entre con la portada de Dublín ya en cuadro.
4. **Remate.** «Escucha al que pregunta.» tiene que quedar entero y quieto, con la cámara parada, al menos 1,0 s (de ~21,1 a ~22,1 s). Después, fundido a NEGRO de 0,5 s y outro2. En la mezcla, mueve el audio de outro2 y su sting a la vez: «Dale» debe entrar ≥ 1,0 s después de «pregunta» (≈ 22,4 s o más).
5. **Pie de créditos final.** Quítalo de pantalla, porque ya va en el caption, o déjalo a ≥ 17 px y quieto ≥ 1,5 s.
6. **Opcional.** Haz el alejamiento final del guion (ver toda la pared) solo si se lee en el móvil y termina antes de «pregunta».
7. **Repo, cola y panel a la vez.** Sube el `video_mudo.mp4` nuevo. En `publicar/cola.json`, cambia `files` y guarda `f3e2302d` en `files_old`. Cambia también el vídeo del post del panel. El caption del panel ya lo he igualado al de la cola, así que no lo pises con el del guion.

Sin cambios: música, efectos, fotos, datos y caption (salvo la voz, si se rehace el gancho).
