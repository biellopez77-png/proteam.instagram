# Crítica · v7-contar-rivales-rangnick «¿Trece? ¿Catorce?» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 78/100 → NO APROBADO. Vuelve a montaje.**

Material revisado: el vídeo de la cola (`publicar/cola.json` → `27b74c02-…mp4`, 23,9 s, cierre outro2), descargado y analizado en el sandbox de Higgsfield (48 fotogramas cada 0,5 s a 270 px, tira de 19,0–20,6 s cada 0,2 s y fotograma a 540 px en 15,2 s; faster-whisper small con tiempos por palabra; niveles por segundo; EBU R128). También el `video_mudo.mp4` del repo (26,0 s), `mix.py`, `CREDITOS.md` y el guion. Ojo: el vídeo de la tarea (`9db5fc13`) y el `video_mudo.mp4` del repo llevan aún el cierre retirado («Estamos terminando la app»); lo que se publicaría es el de la cola, y es el que puntúo.

## Comprobaciones duras
- **Cierre:** el vídeo de la cola acaba en outro2: «¿Te ha servido?» en pantalla y la voz «Dale like y síguenos para más vídeos como este» (20,34–23,08 s). Ni «app» ni producto en la voz ni en la pantalla. Bien.
- **Caption de la cola:** correcto, termina en «¿Te ha servido? Dale like y síguenos para más vídeos como este.» Sin enlace ni «app». **El post del panel seguía con el caption viejo** («Estamos terminando la app de ProTeam…») y con el vídeo `9db5fc13`: lo he corregido con el caption y el vídeo de la cola.
- **Voz entera:** whisper oye toda la historia: «Ralph Ragnick juega y entra en el club de su ciudad, el Victoria Bucknang. Un amistoso contra el dínamo de Kiev de Lobanovsky. En un saque de banda, se para a contar a los rivales. 13, 14, son 11. Pero presionan el balón sin dejar respirar. No son más, llegan todos a la vez.» («entra» por «entrena», como ya anotó Marta; whisper medium oye «entrena».)
- **Niveles:** −17,0 LUFS, true peak −1,0 dBFS. Voz entre −16 y −21 dB RMS por segundo; música sola en las pausas entre −34 y −41 dB (14,4; 17,2; 20,2 s): la voz va 15–20 dB por encima. Efectos discretos. Música real (Epidemic, «Calm Piano, Dreamy, Intro 03»).
- **Fotos:** las cuatro de Commons con licencia (CC BY-SA 4.0 ×2, CC0 ×2), acreditadas; Rangnick sin escudo ni patrocinador; nada sugiere que nadie apoye ProTeam.
- Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel.

## Verdad y fuentes
Todo con fuente en el guion: jugador-entrenador del Viktoria Backnang (The Independent, Wikipedia, Sky Sports); amistoso contra el Dinamo de Lobanovski (The Independent, GOAL, Sky Sports); contar en un saque de banda, «¿13 o 14?» (cita de Rangnick en The Independent); presión sin respiro (The Independent). «Son once» y el remate van como idea, sin comillas. El año (1983) solo en el caption, con sus fuentes (Wikipedia dice 1984: está anotado en el guion). Bien.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Anécdota muy buena y muy de entrenador. Pero el vídeo arranca con nombre y biografía («Ralf Rangnick juega y entrena…»): lo sorprendente (se para a contar rivales) no llega hasta los 9 s. |
| Cada cosa que dice la voz se anima en su momento | 15/20 | Muy bien: JUEGA Y ENTRENA con los sellos JUGADOR/ENTRENADOR, alfiler en Backnang, AMISTOSO, Dinamo y Lobanovski en ficha, balón por la banda, CONTAR con el contador 2→6→10, fichas fantasma con 13?/14?, el «11» que se fija, PRESIONAN con el círculo que se cierra y las once flechas. Pero el remate «A LA VEZ.», el único ultravioleta, se completa a ~20,0 s y a 20,2 s ya está fundiéndose bajo el logo: no se ve nunca entero y quieto. |
| Transiciones | 9/15 | Viajes de cámara suaves, pero: 5,0 s, fotograma casi vacío (solo fondo) en el viaje a «Un amistoso»; 4,5 s, «JUEGA Y ENTRENA» y la ficha cortados por el borde izquierdo durante el viaje; y el fundido al cierre arranca a ~19,8 s, mientras aún se escribe «A LA VEZ», con el logo ProTeam asomando encima del campo y de las flechas (19,8–20,2 s). |
| Sonido | 11/15 | Voz confiada y clara, música real bajo la voz, efectos bajos. Pero la voz del cierre entra a 20,34 s, 0,24 s después de «vez» (20,10 s): el remate no respira. En el montaje anterior (`mix.py`, OUT = 20,4) había 0,6 s más; el recorte a 23,9 s se los ha comido. |
| Verdad y fuentes | 14/15 | Todo con fuente; cita del caption fiel a The Independent. |
| Estética | 13/15 | Paleta, tipografías y fotos bien; campo y contador limpios y legibles a tamaño móvil. Pegas: solape del logo sobre el campo en el fundido final; en 15,0 s «SON» entra encima de «¿Catorce?» aún visible (fundido cruzado de 0,2 s). |
| **Total** | **78/100** | Por debajo de 85. |

## Correcciones (para Marta, 02)
1. **(Bloqueante) Remate quieto.** «A LA VEZ.» entero, encendido en ultravioleta y quieto al menos 1,0 s después de «vez» (la voz acaba en 20,10 s en el vídeo de la cola): la cámara parada desde ~19,9 s y el fundido de 0,5 s al cierre desde ~21,1 s, no antes. Que el logo ProTeam no aparezca hasta que el campo y «A LA VEZ» se hayan ido (sin solape).
2. **(Bloqueante) Aire antes del cierre.** La voz de outro2 no puede entrar antes de ~0,6 s después de «vez». Con el punto 1, que entre con el fundido (≥ 21,1 s).
3. **Viaje de 4,5–5,2 s.** Que no quede el encuadre vacío a 5,0 s: viaje más corto o la tarjeta AMISTOSO / la foto del Dinamo entrando durante el viaje (como en el remontaje de Phog Allen). Si «JUEGA Y ENTRENA» sale cortado por el borde en pleno viaje, que se apague antes.
4. **«SON ONCE.» (15,0 s).** Apaga del todo «¿Trece? ¿Catorce?» antes de que entre «SON», o que «SON ONCE» entre en otra línea sin pisarlo.
5. **(Mejora, opcional) Gancho.** Si se rehace el arranque, que la primera imagen ya sea el campo con el contador o «se para a contar a los rivales» en pantalla; si no, mantener la voz y meter desde 0,0 s un rótulo pequeño «¿Cuántos rivales hay?» sobre el campo. No es obligatorio para aprobar.
6. **Repo y panel:** sube el `video_mudo.mp4` nuevo (el del repo aún lleva el cierre retirado de la app) y el vídeo nuevo a la cola en «revisión». Caption: el de la cola, ya correcto.
