# Crítica · v7-sexto-hombre-auerbach «El sexto no es el sexto mejor» · r3

**Andrés (05) · 28/11/2026 · Nota: 86/100 → NO APROBADO por un suspenso automático (texto cortado en la portada, 0,0–2,0 s). Vuelve a montaje** solo para eso: el final ya está bien, y el audio no se toca.

Material revisado: el vídeo **de la cola** (`publicar/cola.json` → `87ca6635-…mp4`, 26,5 s), descargado y analizado en el sandbox de Higgsfield (faster-whisper small con marcas por palabra, niveles por segundo y por 0,5 s, EBU R128), y `tools/reel_v7/v7-sexto-hombre-auerbach/video_mudo.mp4` (53 fotogramas, uno cada 0,5 s, a tamaño móvil; recortes a 1080 px y fotogramas cada 0,2 s en 0–4 s).

## Comprobaciones duras
- **Voz entera:** «Reda Werbach [Red Auerbach] tenía uno de sus mejores jugadores en el banquillo. Frank Ramsey no salía de titular. Cuando los titulares se cansaban, entraba él, fresco, a correr. Con Ramsey, los Celtics ganaron siete anillos. El premio al mejor suplente de la NBA lleva el nombre de su sucesor, John Havlitek [Havlicek]. El sexto hombre no es el sexto mejor.» (0,00–21,18 s). Igual que la voz del guion; los nombres se entienden al oído.
- **Cierre nuevo:** «Dale like y síguenos para más vídeos como este» (22,46–25,68 s). En pantalla: «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este». **No se dice «app» ni hay producto, lista ni lanzamiento.**
- **Niveles:** −16,9 LUFS integrados, true peak −1,1 dBFS. Voz −15/−20 dB por segundo; hueco del remate 21,5–22,0 s a −34/−38 dB (solo música); cierre −17/−21 dB. Música suave bajo la voz, efectos bajos.
- **Caption de la cola y del panel:** idénticos; acaban con «¿Te ha servido? Dale like y síguenos para más vídeos como este.» antes de fuentes y etiquetas. Sin precios, fechas, cifras de apuntados ni nombre de Biel.
- **Correcciones de r2:** hechas. «mejor.» acaba a 21,18 s; «El sexto hombre / no es el sexto mejor.» con el 6 ultravioleta está entero y quieto de ~21,2 a 22,3 s (fotogramas 21,0 / 21,5 / 22,0 / 22,3 s), se apaga y solo entonces entra el logo (22,5 s): ya no hay solape. «Dale» entra 1,28 s después de «mejor». Mudo nuevo con outro2 en el repo.

## Lo que falla: texto cortado en el primer fotograma
- De **0,0 a 2,0 s**, el rótulo «BANQUILLO: RECREACIÓN» (reel.html, línea 44, `x="575" text-anchor="end"`) asoma por el borde derecho, a la altura del tercio inferior (y ≈ 1050 px en 1080×1920), y **la «N» final queda fuera del encuadre**. Es pequeño, pero está en la portada, la escena de gancho, y además aparece antes de que exista el banquillo (que se dibuja con «banquillo», ~2,6 s). Es «texto cortado»: suspenso automático por regla, aunque el resto sume más de 85.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | Foto de Auerbach entera en el fotograma 0 y buen giro (el premio lleva el nombre del sucesor). El gancho es la decisión, no un lugar y un año. |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Todo entra con su palabra: estrella en «mejores», banco en «banquillo», pizarra en «titular», reloj y barras en «se cansaban», estela en «fresco», anillos 1→7, trofeo, placa y foto en «Havlicek», 6 en «sexto». |
| Transiciones | 14/15 | Viajes suaves, sin destellos ni texto viejo; final quieto → apagado → fundido a outro2 limpio. |
| Sonido | 14/15 | Voz clara y confiada, música real suave, efectos bajos; el cierre ya respira (1,28 s). |
| Verdad y fuentes | 14/15 | Sin cambios desde r2: NESN, NYT vía Pulse, NBC Sports Boston, NBA (13/12/2022). |
| Estética | 9/15 | Paleta, tipos y ultravioleta único, bien; trofeo con su rótulo de recreación visible. Pero texto cortado en la portada. |
| **Total** | **86/100** | **Suspenso automático: texto cortado (0,0–2,0 s).** |

## Correcciones (para Marta, 02)
1. **Rótulo «BANQUILLO: RECREACIÓN» (0,0–2,0 s):** que no asome cortado. Lo más limpio: que tenga `opacity:0` hasta que se dibuje el banco (con «banquillo», ~2,6 s) y que, cuando se vea, quepa entero en el encuadre (muévelo a la izquierda, p. ej. bajo el banco, o con `text-anchor="start"`). Comprueba los fotogramas 0,0–4,0 s cada 0,2 s: ningún texto tocando el borde.
2. **Solo vídeo:** re-render del mudo y remux con **el mismo audio** del r3 (`87ca6635`; no remezcles). Duración y tiempos, idénticos.
3. **Repo y cola:** `video_mudo.mp4` nuevo; nuevo vídeo a cloudfront; `files` de `publicar/cola.json` (r3 a `files_old`; sigue en «revisión») y vídeo del panel.
4. Después, nueva tarea «Auditar v7 v7-sexto-hombre-auerbach». Con eso arreglado, la pieza pasa (86 sin el suspenso).

---

## Crítica anterior (r2)

### Crítica · v7-sexto-hombre-auerbach «El sexto no es el sexto mejor» · r2

**Andrés (05) · 27/11/2026 · Nota: 84/100 → NO APROBADO. Vuelve a montaje** (se queda a un punto: lo que falla es el final).

Material revisado: el vídeo **de la cola** (`publicar/cola.json` → `e7db5b4a-…mp4`, 25,0 s, cierre outro2), descargado y analizado en el sandbox de Higgsfield (fotogramas cada 0,5 s y cada 0,1 s en el final, faster-whisper small con marcas por palabra, niveles cada 0,5 s y EBU R128). También el `video_mudo.mp4` del repo y el vídeo de la tarea (`12c26708-…mp4`): **esos dos llevan todavía el cierre retirado** («Estamos terminando la app de ProTeam. Síguenos para no perderte nada»); no deben usarse en ningún sitio.

## Comprobaciones duras (vídeo de la cola)
- **Voz entera:** whisper oye toda la historia: «Red Auerbach (lo escribe «Reddauerback») tenía uno de sus mejores jugadores en el banquillo. Frank Ramsey no salía de titular. Cuando los titulares se cansaban, entraba él, fresco, a correr. Con Ramsey, los Celtics ganaron siete anillos. El premio al mejor suplente de la NBA lleva el nombre de su sucesor, John Havlicek (lo escribe «Havlitek»). El sexto hombre no es el sexto mejor.» Cierre: «Dale like y síguenos para más vídeos como este» (21,42–24,14 s). **No se dice «app» en ningún momento.**
- **Niveles:** −16,9 LUFS integrados; pico −1,0 dBFS. Voz entre −16 y −20 dB RMS (por 0,5 s); los huecos de solo música, entre −33 y −35 dB (3,5 / 6,0 / 10,0 / 13,0 s): música unos 15 dB bajo la voz. El cierre, a −23/−26 dB con el sting.
- **Cierre en pantalla:** «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este». Correcto.
- **Caption de la cola:** acaba con «¿Te ha servido? Dale like y síguenos para más vídeos como este.» Sin app. El del panel aún llevaba el cierre de la app y el vídeo viejo: **corregido hoy** (vídeo de la cola y caption de la cola).
- **Correcciones de r1:** las 6 están hechas. «23» dentro de la ficha y «RAMSEY» debajo; el rótulo «TROFEO GENÉRICO: RECREACIÓN» encima del trofeo y visible toda la escena; reloj grande junto a las fichas y barras que bajan; viaje de 10,0–10,5 s con las escenas anteriores apagadas; foto de Auerbach entera a 0,0 s; créditos más grandes.
- Fotos de dominio público (Commons), sin logotipos ni nadie que respalde nada; música Epidemic real; sin precios, fechas, cifras de apuntados ni el nombre de Biel.

## Lo que falla: el remate no se ve
- «mejor.» se dice entre 20,98 y 21,18 s. En pantalla, «sexto mejor.» termina de escribirse a ~21,0 s y **a 21,1 s ya entra el logo «ProTeam» encima del «6»** (fotogramas cada 0,1 s de 20,6 a 21,6 s): el remate completo no llega a estar ni 0,2 s limpio y quieto, y durante el fundido el logo y la frase se pisan (texto solapado de 21,1 a 21,4 s).
- La voz del cierre entra a 21,42 s, 0,24 s después de «mejor»: la última idea no respira.
- Es el mismo fallo que hoy se le marcó a Rangnick, y la frase final es la tesis del vídeo.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | Buen gancho y buen giro (el premio lleva el nombre del sucesor). |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Ahora «se cansaban» se ve (reloj y barras). Todo entra con su palabra. |
| Transiciones | 11/15 | Viajes suaves y sin destellos; el de 10,0 s ya no arrastra texto viejo. Pero el fundido al cierre empieza encima del remate. |
| Sonido | 13/15 | Voz clara y confiada, música suave unos 15 dB debajo, efectos bajos. El cierre entra pegado a «mejor» (0,24 s). |
| Verdad y fuentes | 14/15 | Todo con fuente (NESN, NYT vía Pulse, NBC Sports Boston, NBA). |
| Estética | 11/15 | Los textos de r1 están arreglados, pero el logo «ProTeam» se monta sobre el «6» y la frase final durante el fundido. |
| **Total** | **84/100** | |

## Correcciones (para Marta, 02)
1. **Remate entero y quieto ≥ 1 s.** «El sexto hombre / no es el sexto mejor.» con el «6» ultravioleta, completo y con la cámara parada desde que acaba «mejor» (21,18 s) hasta ~22,2 s. Solo después, el fundido de 0,5 s al cierre (como en el r2 de Phog Allen).
2. **Fundido sin solapes.** Que el logo «ProTeam» del cierre no aparezca mientras el remate sigue en pantalla: primero se apaga el remate (a fondo) y luego entra el cierre, o fundido de 0,5 s que empiece después del punto 1.
3. **Audio:** la misma voz, la misma música y los mismos efectos; retrasa el audio de outro2 y el sting para que la voz del cierre entre ~0,3 s después del inicio del fundido (≈ 1,2–1,3 s después de «mejor»). Mantén −16/−17 LUFS y pico ≤ −1,0 dBTP.
4. **Repo:** sube el `video_mudo.mp4` nuevo, con outro2 (el que hay en `tools/reel_v7/v7-sexto-hombre-auerbach/` lleva todavía el cierre de la app). Nuevo vídeo a cloudfront y `files` de `publicar/cola.json` (sigue en «revisión»). Actualiza también el vídeo del panel.
5. Después, nueva tarea «Auditar v7 v7-sexto-hombre-auerbach».

---

## Crítica anterior (r1)

# Crítica · v7-sexto-hombre-auerbach «El sexto no es el sexto mejor» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 82/100 → NO APROBADO. Vuelve a montaje** (además, cae en un suspenso automático: hay texto solapado y texto que se sale de su ficha).

Material revisado: `tools/reel_v7/v7-sexto-hombre-auerbach/video_mudo.mp4` (54 fotogramas, uno cada 0,5 s, a 360 px de ancho, y recortes a 1080 px donde hacía falta) y el vídeo final de cloudfront (`5096bbec-…mp4`, 27,1 s), descargado y analizado en el sandbox de Higgsfield.

## Comprobaciones duras
- **Voz entera:** faster-whisper small oye la historia completa: «Reda Werbach tenía uno de sus mejores jugadores en el banquillo. Frank Ramsey no salía de titular. Cuando los titulares se cansaban, entraba él, fresco, a correr. Con Ramsey, los Celtics ganaron siete anillos. El premio al mejor suplente de la NBA lleva el nombre de su sucesor, John Havlitek. El sexto hombre no es el sexto mejor.» Une «Red Auerbach» y se come la «a» de «tenía a uno» (lo mismo que anotó Marta con small; medium sí la oye). Al oído, los nombres se entienden. El cierre común se oye entero (21,7–25,4 s).
- **Niveles:** pico de muestra −1,0 dBFS (solo 2 muestras por encima de −1 dB, a 0,1 s y 4,2 s). La voz va entre −10 y −14 dB RMS (por 100 ms), y los huecos de solo música, entre −29 y −38 (por ejemplo, −32,8 dB a 3,4–3,7 s): la voz va unos 15 dB por encima. En la pausa del remate (18,7–19,0 s) hay −21 dB: es el sello y la música que sostiene, sin picos. Los efectos no tapan la voz.
- **Destellos:** no hay ninguno. El salto máximo de luminancia media entre fotogramas es de 4,0/255. El cambio más grande entre fotogramas (10,4–10,63 s) es el viaje de la pizarra a la foto del equipo.
- **Texto:** **FALLA.** Dos fallos (ver correcciones 1 y 2).
- **Fotos:** las 4 son de dominio público (Commons, comprobadas el 25/11 según CREDITOS.md). Ninguna sugiere que alguien apoye ProTeam, y no salen logotipos de los Celtics ni de la NBA. El trofeo es genérico y va rotulado como recreación, aunque luego el rótulo queda tapado (corrección 2).
- **Música:** real, de Epidemic («Musical, Loop, Piano, Sentimental, Fast 02»), no sintetizada.
- Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel.

## Verdad y fuentes
Cada frase tiene fuente en el guion: Ramsey como «lift from the bench» y uno de los mejores (NESN; Wikipedia), entrar cuando los titulares necesitaban aire (NYT vía Pulse; NBC Sports Boston), siete títulos (NBC Sports Boston), John Havlicek Trophy al Sexto Hombre del Año (NBA, comunicado del 13/12/2022) y Havlicek como sucesor en ese papel (Wikipedia; Pulse). El remate es una idea, no una cita, y no va entre comillas. Bien.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | Buen gancho (un titular en el banquillo) y buen giro (el premio lleva el nombre del sucesor). El remate cierra la idea. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Foto de Auerbach en «Red Auerbach», Ramsey con estrella en «mejores jugadores», banco que se dibuja en «banquillo», pizarra en «titular», ficha que entra con estela en «fresco», anillos 1→7 en «siete anillos», trofeo en «premio», placa y foto en «Havlicek», «6» en «sexto». Lo flojo: «se cansaban» (7,5–8,0 s) solo vuelve grises las fichas y saca un reloj diminuto (abajo a la izquierda); las barras de energía casi no se ven en el móvil. |
| Transiciones | 12/15 | Viajes suaves y sin destellos, pero el de 10,1–10,7 s (pizarra → foto del equipo) cruza media pared y deja ver de pasada «BANQUILLO.» y «FRESCO» de las escenas anteriores. El primer fotograma (0,0 s) arranca con la foto de Auerbach medio fuera por la izquierda: la portada sale torcida. |
| Sonido | 13/15 | Voz confiada y clara. Música suave, unos 15 dB bajo la voz. Efectos bajos. Pico −1,0 dBFS. |
| Verdad y fuentes | 14/15 | Todo con fuente. |
| Estética | 9/15 | La paleta, las tipografías y el ultravioleta (una sola vez, en el «6») están bien, pero hay dos fallos de texto (abajo). |
| **Total** | **82/100** | Y cae en un suspenso automático por texto solapado o desbordado. |

## Correcciones (para Marta, 02)
1. **«RAMSEY» se sale de su ficha (4,0–10,2 s).** En la pizarra, la palabra es más ancha que el círculo: la «R» y la «Y» pisan el borde o quedan fuera (a 5,5 s, en 1080 px: círculo de unos 120 px y texto de unos 125 px). Solución: baja el cuerpo a unos 70 %, o pon «23» o «R» dentro de la ficha y «RAMSEY» debajo, como «BANQUILLO». Así queda también cuando entra en pista con la estela (8,5–10,2 s).
2. **El rótulo «TROFEO GENÉRICO: RECREACIÓN» queda tapado (15,5–19,0 s).** Cuando entra la placa blanca «JOHN HAVLICEK TROPHY», esta cae justo encima del rótulo y solo asoma «ON» a la derecha de la placa (x≈515, y≈1250 a 18,5 s). Además de ser texto solapado, deja el trofeo sin su aviso de recreación justo cuando se nombra el premio real. Solución: sube el rótulo por encima del trofeo o bájalo bajo la placa, y que se lea durante toda la escena.
3. **«se cansaban» (7,4–8,2 s):** haz visible el cansancio a tamaño móvil. Que las barras de energía sean más gruesas y bajen claramente, o que el reloj sea más grande y esté junto a las fichas (no en la esquina).
4. **Viaje de 10,1–10,7 s:** que no pase por encima de las escenas anteriores, o que las apague antes de salir (fundido de 0,3 s de «BANQUILLO.» y «FRESCO»), para que no reaparezca texto viejo en el trayecto.
5. **Primer fotograma:** que el vídeo empiece con la cámara ya parada sobre la foto de Auerbach (o con la foto entera en el encuadre a 0,0 s), porque es la portada que ve la gente al pasar.
6. Opcional: en el pie de créditos final (20,5–21,5 s), el tamaño es casi ilegible en el móvil. Súbelo un punto si cabe.

Después de corregir: render del mudo, nueva mezcla con la misma voz y la misma música (el sonido está bien), subida a cloudfront y actualización de `files` en `publicar/cola.json` (sigue en «revisión»). Después, nueva tarea «Auditar v7 v7-sexto-hombre-auerbach».
