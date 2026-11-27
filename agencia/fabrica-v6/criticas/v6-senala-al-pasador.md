# Crítica · v6-senala-al-pasador «Una cena, cortesía del entrenador» · Andrés (05) · 24/11

**Vídeo:** tools/reel_v6/v6-senala-al-pasador/final.mp4 (commit 04d7d7e) · 1080×1920 · 43,9 s · voz hasta 42,3 s
**Método:** 44 fotogramas (1/s) a tamaño móvil + fotogramas extra en 11,5 · 12,5 · 13,2 · 13,6 · 18,4 · 18,8 · 19,3 · 21,8 · 23,3 · 24,2 · 28,3 · 40,6 s; tiempos de voz por palabra (times.js, Scribe) contra la locución del guion (coincide palabra por palabra, 116 palabras); loudness con ebur128.

## Nota: 83/100 → **APRUEBA** (ninguna condición eliminatoria)

| Criterio | Nota | Por qué |
|---|---|---|
| Historia y gancho real | 23/25 | «Doscientos dólares» con el cheque contando a 200 $ y los sobres llenando la rejilla hasta ≈180 es un gancho real y emotivo; la nota en cursiva cierra la historia en 13 s. |
| Claridad para un entrenador de base | 17/20 | La regla se ve en la pista y la hoja TRAS PASE / SIN PASE (8 · 12, rotulada EJEMPLO) se entiende sola. El 879 apenas se queda quieto (~0,5 s) y los subtítulos de 30–38 s resumen la voz en vez de seguirla. |
| Pizarra y transiciones | 15/20 | La pista se dibuja, la flecha de vuelta va en UV y la partida «+3» funciona. Fallan: rótulo «Dean Smith» encima del texto de la nota (13–14,5 s), salidas que pisan la cabecera (19 s y 23 s), línea de fondo cruzando el subtítulo (28 s) y el cierre es corte a logo, no la hoja convertida en tarjeta. |
| Verdad y fuentes | 14/15 | Todo casa con el guion y sus fuentes (PBS NewsHour, CNNMoney, Rivals, The Daily Tar Heel). «Recreación» en cheque y nota, «EJEMPLO» en la hoja, créditos de foto en pantalla (DoD DP; Prößdorf CC BY-SA 4.0). Pie con «Datos: PBS · CNNMoney» en 0–19 s. |
| Estética v4 | 8/10 | Fondo, duotono azul, Plus Jakarta + Instrument Serif bien. UV una vez (flecha B→A, 22,3–24 s). El «Team» del wordmark final en índigo se acerca al UV (mismo comentario que en v6-reloj-24; es del cierre común). |
| Sonido | 6/10 | Voz cálida y clara, pausas de «Siempre.» y «Nadie lo ve.» respetadas. Integrado −23,1 LUFS (pico −4,4 dBFS): bajo para Reels. |

## Comprobación de datos (voz → fuente)
- 200 $, marzo de 2015, unos 180 exjugadores, carta con cheque (0–7 s) → CNNMoney (≈180; SI vía PBS cuenta 184; «unos» lo cubre) ✔
- Nota «Enjoy a dinner out, compliments of Coach Dean Smith» (9–13 s) → PBS NewsHour ✔ (rotulada «Recreación de la nota»)
- Murió en febrero de 2015; North Carolina 1961–1997 (12–15 s) → PBS, CNNMoney ✔
- 36 temporadas, 879 victorias (15–19 s) → CNNMoney (879-254) y PBS ✔
- Regla de señalar al pasador (19–24 s) → Rivals (Inside Carolina), The Daily Tar Heel ✔
- Hoja 8 · 12 y partidillo 3/1: propuesta, rotulada EJEMPLO / «cifras de ejemplo» ✔
- Sin fechas de lanzamiento ni ofertas ✔ · Fotos con licencia y crédito en pantalla ✔

## Marcas de tiempo y correcciones (para la próxima versión o si se remonta)
1. **13,2–14,5 s · solape.** El rótulo «Dean Smith» entra encima de «Enjoy a dinner out, compliments of…», que sigue al ~40 %: las dos tipografías se mezclan y no se lee ninguna. → Bajar la nota a ≤ 10 % (o desenfocarla) antes de que entre el rótulo, o subir el rótulo cuando la nota ya se haya ido.
2. **18,4–19,3 s · el 879 se ve quieto ~0,5 s** y al salir el «36» pasa por encima de «HISTORIAS · BALONCESTO». → Que el contador llegue a 879 al terminar «nueve» (≈18,0 s) y aguante 0,8 s; salida con máscara bajo la cabecera.
3. **23–24 s · la foto de penetración sale por arriba-izquierda pisando la cabecera.** → Misma máscara (cabecera por encima de la capa de fotos).
4. **28–29 s · la línea de fondo de la pista cruza el subtítulo** «¿Y el pase? Nadie lo ve.» (parece tachado). → Subir la pista 40–60 px o acortarla para que acabe por encima de y ≈ 1.580 px.
5. **21,7–22,3 s · la flecha UV llega ~0,6 s tarde** respecto a «señala» (21,67 s). → Adelantar el trazo para que empiece con la palabra.
6. **40,5–41 s · cierre.** El guion pide que la hoja se convierta en tarjeta antes del logo; ahora es corte a wordmark estático. Puente «esto se apunta» perdido.
7. **Sonido.** Subir a −14/−15 LUFS integrados con limitador a −1 dBTP.
8. (Menor) **30–38 s:** los subtítulos resumen («tu segundo apunta las canastas tras pase», «Martes, partidillo: tras pase vale 3») y la voz dice otra frase; aceptable, pero mejor que el texto siga a la voz.

Ninguna de estas es eliminatoria: el texto no se corta, los datos están todos con fuente y la pizarra se mueve con la voz. Con 1, 2 y 7 corregidos pasaría de 88.
