# Crítica · v7-no-se-entrena-phog-allen «Solo se juega» · r2

**Andrés (05) · 28/11/2026 · Nota: 90/100 → APROBADO. Programado para el jueves 10/12/2026 a las 18:00 (pub_v3 approve).**

Material revisado: el vídeo de la cola y del panel (`75a9bcd1-…mp4`, 29,4 s), descargado en el sandbox de Higgsfield: 59 fotogramas cada 0,5 s a 270 px, recortes a 360 px en 2,8 / 3,0 / 9,6 / 10,6 / 11,6 / 24,9 s, faster-whisper medium con marcas por palabra y niveles por segundo. El repo es demasiado pesado para bajarlo entero en el turno: el `video_mudo.mp4` nuevo (commit 5d7d8ab) no lo he mirado aparte; puntúo el vídeo de la cola, que es el que se publica.

## Comprobaciones duras
- **Cierre outro2:** «¿Te ha servido? / Dale like y síguenos / para más vídeos como este» en pantalla desde ~25,4 s; whisper: «Dale like y síguenos para más vídeos como este» (25,94–28,80 s). Caption acaba con esa frase (antes de hashtags). Bien.
- **Nada de app, producto, lista ni lanzamiento** en voz, pantalla o caption. Sin precios, sin Biel, sin cifras de apuntados.
- **Voz entera (whisper):** «James Naismith inventó el baloncesto, y a su alumno, Fogg Allen, le dijo: El baloncesto no se puede entrenar, solo se juega. Allen no le hizo caso. 50 temporadas en un banquillo, 746 victorias. De sus equipos salieron Adolf Rapp y **Dean Smith**. El juego se juega, pero alguien tiene que **enseñarlo**.» Las 55 palabras del guion; «Fogg»/«Adolf Rapp» son grafía de whisper, la pronunciación es la buena.
- **Niveles por segundo:** voz −16,6 a −21 dB RMS; huecos de música −27 a −28 dB; cierre −24 dB. −16,7 LUFS, true peak −0,9 dBFS. Música real (Epidemic), efectos bajos.
- **Fotos:** las cuatro de Commons en dominio público, sin logos; Rupp y Smith en fichas dibujadas sin cara, rotuladas como recreación.

## Correcciones del r1, una a una
1. Remate: «enseñarlo» acaba a 24,56 s; «ENSEÑARLO.» ultravioleta, entero y quieto hasta ~25,4 s; fundido; voz del cierre a 25,94 s (1,4 s de aire). **Hecho.**
2. Sello «NO» bajo el subrayado, en la parte vacía de la tarjeta, sin tapar texto (10,0–11,0 s). **Hecho.**
3. «SOLO SE JUEGA.»» dentro de la tarjeta con margen. **Hecho.**
4. Comilla suelta: ya no está. **Hecho.**
5. Viaje 2,6–3,2 s: la ficha «PROFESOR» y la foto de Allen entran durante el viaje; el centro nunca queda vacío. **Hecho.**
6. Tarjeta de la cita apagada antes de que entre el banco (11,5 s). **Hecho.**
7. «Dean Smith»: whisper lo oye bien (19,80–20,52 s). **Hecho.**
8. Mudo nuevo en el repo (5d7d8ab): según Marta; no comprobado por el peso del repo.
9. Foto 1 sin cambiar (era opcional).

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Fotograma 0 ya con la ficha de Naismith y «James»; «INVENTÓ» a 1,2 s. Historia muy buena, remate citable. Pero lo raro (el inventor dice que no se entrena) llega a los 5,5 s, no en 0–3 s. |
| Cada cosa que dice la voz se anima en su momento | 19/20 | Todo en su palabra: INVENTÓ + reglas, línea profesor → alumno, cita palabra a palabra, sello NO, 50 palotes, contador 0→746 con fichas, «COACH F. C. ALLEN», fichas de Rupp y Smith, balón que bota, flecha a la pizarra, ENSEÑARLO en ultravioleta y quieto. |
| Transiciones | 13/15 | Viajes de cámara suaves; el remate ya respira antes del fundido. En 3,5 s y 13,0 s el viaje deja texto medio fuera de cuadro un instante (es movimiento, no corte). |
| Sonido | 14/15 | Voz confiada y clara, aire limpio antes del cierre, música real bajo la voz. |
| Verdad y fuentes | 14/15 | Todo con fuente (Kansan, Encyclopedia.com, Kansapedia, Britannica); cita rotulada. Reserva: foto 1 con referencia Getty en Commons (dominio público). |
| Estética | 14/15 | Paleta y tipografías de v7, nada cortado ni solapado en reposo; pies pequeños pero legibles. |
| **Total** | **90/100** | |

## Mejoras opcionales (no bloquean)
- Para próximos guiones de este estilo: abrir con la frase rara («El inventor del baloncesto dijo que no se podía entrenar») y poner el nombre después.
- Foto 1 → reserva de Springfield College (c. 1920) si se vuelve a montar.

---

# Crítica · v7-no-se-entrena-phog-allen «Solo se juega» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 79/100 → NO APROBADO. Vuelve a montaje.**

Material revisado: `tools/reel_v7/v7-no-se-entrena-phog-allen/video_mudo.mp4` (60 fotogramas, uno cada 0,5 s, a 270 px, y recortes a 540 px en 9,5 / 10,5 / 19,8 s), `words.js`, `mix.py`, `CREDITOS.md` y el vídeo de la cola (`publicar/cola.json` → `9ac69641-…mp4`, 28,0 s), descargado y analizado en el sandbox de Higgsfield (56 fotogramas cada 0,5 s, faster-whisper small, niveles por segundo). Ojo: el `video_mudo.mp4` del repo aún lleva el cierre viejo («Estamos terminando la app»); el vídeo de la cola ya lleva outro2. Lo que se publicaría es el de la cola, y es el que puntúo.

## Comprobaciones duras
- **Cierre:** el vídeo de la cola acaba en outro2 («¿Te ha servido?» en pantalla; la voz dice «Dale like y síguenos para más vídeos como este», 24,4–27,2 s). Bien. Ni «app» ni producto en la voz ni en la pantalla del vídeo de la cola.
- **Caption de la cola:** correcto, acaba en «¿Te ha servido? Dale like y síguenos para más vídeos como este.» **Pero el post del panel seguía con el caption viejo** («Estamos terminando la app de ProTeam…») y con el vídeo viejo (`d01bc15a`, cierre retirado). Lo he corregido en el panel con el caption de la cola; el vídeo del panel se actualiza con el remontaje.
- **Voz entera:** whisper oye la historia: «James Naismith inventó el baloncesto, y a su alumno, Fog Allen, le dijo: El baloncesto no se puede entrenar, solo se juega. Allen no le hizo caso. 50 temporadas en un banquillo, 746 victorias. De sus equipos salieron Adolf Rapp y Teen Smith. El juego se juega, pero alguien tiene que **enseñar**.» Dos fallos: «Dean» se oye «Teen» (y aislado, «tienesme») con la música debajo; y la última palabra se queda en «enseñar»: la voz acaba en 24,35 s según `words.js`, y la voz del cierre entra a 24,38 s, sin ni una décima de aire. El «-lo» queda tapado por el fundido.
- **Niveles por segundo:** voz entre −17 y −21 dB RMS; pausas de música entre −28,5 y −29,3 dB (2, 11, 16 y 20 s): la voz va ~11 dB por encima. Pico máximo −1,1 dBFS (21 s). Cierre a −24 dB RMS. Efectos discretos. Correcto.
- **Fotos:** las cuatro de Commons, dominio público, sin logos y sin insinuar apoyo de nadie. Rupp y Smith, fichas dibujadas sin cara, rotuladas como recreación. Bien.
- **Música:** real, de Epidemic («Calm Piano, Dreamy, Intro 04»).
- Sin precios, fechas, cifras de apuntados ni el nombre de Biel.

## Verdad y fuentes
Todo lo que dice la voz tiene fuente en el guion: alumno de Naismith (Britannica, Kansapedia); la frase «You can't coach basketball, you just play it» (University Daily Kansan, Encyclopedia.com), dada como traducción y rotulada «cita según…»; 50 temporadas y 746 victorias (Kansapedia, Wikipedia); Rupp y Dean Smith (Britannica, Encyclopedia.com); «padre del entrenamiento de baloncesto» (Britannica), solo en rótulo y caption. No se dan derrotas ni el año de la frase, como pide el guion. Única reserva: la foto 1 (Dr. James Naismith.jpg) figura en Commons con una referencia de Getty como origen; es dominio público, pero la reserva de Springfield College (c. 1920) es más limpia.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Historia muy buena (el inventor dice que no se entrena). El gancho arranca con un nombre y la sorpresa llega a los 6 s. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Muy bien: «INVENTÓ» con el folio de las reglas, la línea profesor → alumno, la cita palabra a palabra, el sello «NO» en «no le hizo caso», 50 palotes y contador 1→50, 746 con fichas, el equipo de 1924 con «COACH F. C. ALLEN» señalado, las fichas de Rupp y Smith, el balón que bota en «se juega» y la flecha a la pizarra. Pero «ENSEÑARLO», el remate ultravioleta, se enciende a ~23,8 s y el logo del cierre ya asoma encima a 24,0 s: no se ve nunca solo y quieto. |
| Transiciones | 10/15 | 2,6–3,2 s: el viaje deja el encuadre casi vacío (solo la ficha pequeña de Naismith a la izquierda). 11,5–12,0 s: restos de la tarjeta de la cita en el borde izquierdo mientras entra el banco. Y el fundido al cierre pisa el remate (23,8–24,3 s). |
| Sonido | 11/15 | Voz confiada y clara, música real y baja, efectos discretos. Pero la voz del cierre arranca pegada a «enseñarlo» (24,35 → 24,38 s) y se come el «-lo»; «Dean» se pierde bajo la música (19,7–20,0 s). |
| Verdad y fuentes | 14/15 | Todo con fuente; la cita, como traducción y con origen rotulado. |
| Estética | 11/15 | Paleta y tipografías bien, fotos con licencia. Pero: «SOLO SE JUEGA.»» se sale por el borde derecho de la tarjeta (8,8–11,0 s; el «»» cruza el marco); el sello «NO» tapa «baloncesto» («balonces[to]», 10,0–11,0 s): texto solapado; una comilla «"» pequeña suelta en la esquina superior izquierda de la tarjeta (6,0–11,0 s). |
| **Total** | **79/100** | Además, el texto solapado por el sello y el que se sale de la tarjeta bastan para suspender. |

## Correcciones (para Marta, 02)
1. **(Bloqueante) Remate y cierre.** Que «ENSEÑARLO» quede entero, encendido y quieto al menos 1,0 s después de la última sílaba (la voz acaba en 24,35 s): fundido de 0,5 s al cierre desde ~25,4 s, no antes. La voz del cierre no puede pisar «enseñarlo»: deja ≥ 0,6 s de música entre las dos voces. Comprueba con whisper que se oye «enseñarlo» entero.
2. **(Bloqueante) Sello «NO» (10,0–11,0 s).** Que no tape texto: que caiga en la parte vacía de la tarjeta, bajo el subrayado (entre «SOLO SE JUEGA» y el pie), o encima de la tarjeta ya apartada, pero sin solapar «baloncesto».
3. **(Bloqueante) «SOLO SE JUEGA.»» (8,8–11,0 s).** Que quepa en la tarjeta con ≥ 40 px de margen: bájalo de tamaño (~88 px) o ensancha la tarjeta.
4. **Comilla suelta.** Quita la «"» pequeña de la esquina superior izquierda de la tarjeta de la cita (6,0–11,0 s).
5. **Viaje de 2,6–3,2 s.** Que no se vea el encuadre vacío: viaje más corto o la foto de Allen entrando antes, para que siempre haya algo en el centro.
6. **Restos a 11,5–12,0 s.** Apaga la tarjeta de la cita antes de que entre el banco.
7. **«Dean» (19,7–20,0 s).** Ducking más hondo de la música ahí o +1,5 dB de voz, hasta que whisper oiga «Dean Smith» con la música.
8. **Repo:** sube el `video_mudo.mp4` nuevo con outro2 (el del repo aún tiene el cierre retirado).
9. (Mejora) Cambia la foto 1 por la reserva de Springfield College (c. 1920) si no te cuesta; si no, déjala.

Lo demás se queda igual: la voz, la música, los efectos y todas las animaciones por palabra están bien. Cuando esté montado, vuelvo a auditar lo cambiado más un repaso completo de fotogramas.
