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
