# Crítica · v7-sistema-lobanovski «Veintidós piezas» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 80/100 → NO APROBADO. Vuelve a montaje.**

Material revisado: `tools/reel_v7/v7-sistema-lobanovski/video_mudo.mp4` (56 fotogramas, uno cada 0,5 s, a 270 px de ancho, y recortes a 540 px donde hacía falta), `reel.html`, `mix.py`, `CREDITOS.md` y el vídeo final de cloudfront (`24f62949-…mp4`, 28,1 s), descargado y analizado en el sandbox de Higgsfield.

## Comprobaciones duras
- **Voz entera:** faster-whisper small oye las 58 palabras de la historia: «Valeriy Lobanovsky estudió ingeniería térmica. En una fiesta conoció a un estadístico, Anatoly Zelenshov. Juntos contaron cada tiro, cada pase y cada error de sus jugadores. Para él, el fútbol eran 22 piezas, dos sistemas de 11. Con esas cifras, el dínamo de Kiev ganó dos recopas. Porque un equipo vale más que la suma de sus 11.» «Zelentsov» se oye «Zelenshov»: se entiende. El cierre común se oye entero (22,7–26,4 s).
- **Niveles:** −18,4 LUFS integrados, true peak −1,0 dBFS. La voz va entre −19 y −21 dB RMS, y las pausas de solo música, entre −30 y −35 dB: la voz va unos 12–13 dB por encima, como pide el formato. El pico de muestra (−1,1 dBFS a 8,97 s) es el arranque de «cada», no un efecto. Los efectos no asoman.
- **Pausa del remate:** `mix.py` abre la voz 0,5 s en 19,25 s y `words.js` ya lleva el desplazamiento: «Porque» suena a 19,84 s y entra en pantalla a 20,0 s. Cuadra.
- **Destellos:** ninguno. Los viajes no tienen saltos de luz.
- **Fotos:** las 3 son CC0 (Nationaal Archief / Anefo, comprobadas el 25/11). No se insinúa apoyo de nadie, y no salen escudos del Dinamo ni logos de la UEFA. Zelentsov va como tarjeta dibujada, sin cara. Bien.
- **Música:** real, de Epidemic («Soft Piano, Strings, Calm, Logo 02/03»).
- Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel.

## Verdad y fuentes
La voz está bien sostenida por fuentes: ingeniería térmica (Wilson/The Guardian, Engelsberg, Breaking the Lines), la fiesta con Zelentsov (Wilson, Engelsberg), tiros, pases y errores contados (Engelsberg), 22 elementos en dos subsistemas de 11 (Wilson; Breaking the Lines), las Recopas de 1975 y 1986, las dos por 3-0 (Wikipedia, UEFA), y la idea final (Wilson).
**Pero la pizarra final dice lo contrario que la voz.** En `reel.html` la «SUMA» está a la izquierda (x=210), el «EQUIPO» a la derecha (x=770) y el trazo `#gt` es `M440 300 L540 380 L440 460`, o sea, un «>» que abre hacia la izquierda. En pantalla se lee «SUMA > EQUIPO» (21,0–22,4 s), justo cuando la voz dice «un equipo vale más que la suma». El guion pide «EQUIPO > SUMA». Es el remate y el único ultravioleta del vídeo: es lo que se queda en la cabeza.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Buena historia (un ingeniero térmico y un estadístico en una fiesta), pero el gancho arranca con el nombre y tarda 3 s en sorprender. |
| Cada cosa que dice la voz se anima en su momento | 16/20 | Muy bien: el termómetro que sube en «térmica», las copas que chocan en «fiesta», la tarjeta que se escribe letra a letra en «Zelentsov», un palote por palabra en TIRO · PASE · ERROR, 22 fichas y la red de 11 en «dos sistemas de once», trofeos 1975 y 1986 en «dos Recopas». Lo flojo: el contador se lee como «7», «14 PIEZAS:» y «21 PIEZAS:» (13,0–13,9 s) mientras la voz ya dice «piezas»; el rótulo «TROFEOS GENÉRICOS: RECREACIÓN» está a la vista desde 16,0 s, antes que los trofeos (18,1 s). |
| Transiciones | 13/15 | Viajes suaves en las pausas y sin destellos. En 19,3–19,8 s la cámara llega a una pizarra vacía y se queda ahí medio segundo. |
| Sonido | 13/15 | Voz confiada y clara, música suave a ~12 dB y efectos discretos. Pico −1,0 dBTP; el arranque de «cada» (8,97 s) es lo único que sobresale. |
| Verdad y fuentes | 10/15 | Todo con fuente, pero el signo de la pizarra invierte la idea final. |
| Estética | 12/15 | La paleta, las tipografías y las fotos están bien. La segunda línea de la frase final crece alineada a la izquierda pegada al borde («vale», «vale más», 20,4–21,4 s, a ~10 px del borde) y luego salta al centro. El retrato inicial y la foto de la tribuna (0,0 y 7,0–7,5 s) quedan casi a sangre por la izquierda. Los créditos del pie, ilegibles en el móvil. |
| **Total** | **80/100** | |

## Correcciones (para Marta, 02)
1. **(Bloqueante) Signo de la pizarra.** Que se lea «EQUIPO > SUMA». O cambias el trazo `#gt` a `M540 300 L440 380 L540 460` («<» entre SUMA y EQUIPO), o intercambias las x de `tS` (770) y `tE` (210) y mueves la red y los unos de sitio. Prefiero lo segundo: EQUIPO a la izquierda, «>» ultravioleta, SUMA a la derecha, como dice la voz.
2. **Segunda línea de la frase final (20,4–22,4 s).** Que crezca centrada desde el principio, igual que la primera, con al menos 60 px de margen a cada lado, y sin salto al centro al completarse.
3. **Contador de las 22 fichas (13,0–13,9 s).** Que «PIEZAS:» no aparezca hasta que el contador llegue a 22. Mientras cuenta, solo el número.
4. **Rótulo de recreación de los trofeos.** Que entre con los trofeos (18,1 s), no a 16,0 s.
5. **Pausa de 19,3–19,8 s.** Que la cámara se quede en los trofeos durante la pausa de «Recopas...» (como pide el guion) y viaje a la pizarra en el último tramo, para llegar con «Porque», no antes.
6. **Márgenes de las fotos.** El retrato del primer fotograma y la foto de la tribuna a ≥ 40 px del borde izquierdo.
7. (Mejora) Créditos del pie a ≥ 17 px, como en el remontaje de Auerbach.

El audio está bien: se puede reutilizar tal cual (voz, música, efectos y la apertura de 0,5 s), siempre que los tiempos de pantalla no cambien.

Cuando esté montado, vuelvo a auditar solo lo cambiado más un repaso completo de fotogramas.
