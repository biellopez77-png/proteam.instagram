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
