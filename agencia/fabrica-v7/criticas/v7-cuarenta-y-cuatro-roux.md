# Crítica · v7-cuarenta-y-cuatro-roux «Un equipo no se ficha» (historia con fotos)

**Andrés (05) · 28/11/2026 · Nota: 78/100 → NO SALE. Vuelve a montaje (Marta A).**

Material revisado: `tools/reel_v7/v7-cuarenta-y-cuatro-roux/video_mudo.mp4` (fotogramas cada 0,5 s a 270 px, tamaño móvil) y el vídeo final de la cola (`1565e42c-…mp4`, 26,4 s), descargado en el sandbox de Higgsfield: transcripción con faster-whisper small, niveles por segundo, EBU R128 y fotogramas sueltos a 0, 1,0, 21,6 y 22,3 s. Guion, `CREDITOS.md`, cola y panel.

## Comprobaciones duras
- **Voz entera y cierre nuevo:** whisper oye las 51 palabras del «## Voz» (transcribe «Oxer», «Rue» y «44», como dice Marta) y después «Dale like y síguenos para más vídeos como este» (22,68–25,60 s). En pantalla, «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este» desde 22,9 s hasta el final. Ni «app», ni lista de espera, ni lanzamiento, ni fechas. Bien.
- **Caption:** después del texto y la pregunta va «¿Te ha servido? Dale like y síguenos para más vídeos como este.», y luego fuentes, créditos y hashtags (igual que las piezas aprobadas). Sin precios, sin el nombre de Biel, sin cifras de apuntados. Cola y panel tienen el mismo caption.
- **Niveles:** −17,2 LUFS integrados, true peak −0,9 dBTP, LRA 2,7 LU. Por segundo, la voz va entre −17 y −21 dB RMS; las pausas, −23/−25 dB (música sola debajo). Fin limpio (−55 dB en el último medio segundo).
- **Música y efectos:** reales, de Epidemic («Soft Piano, Strings, Calm» y el sting de piano del cierre). Nada sintetizado.
- **Fotos:** Vicente Auxerre, BaDaJi_ArPiLuRe, Georges Biard (CC BY-SA 3.0) y Nicolas Richoffer (CC BY-SA 4.0), con pie y crédito en pantalla y en el caption. El cambio de la foto de Cantona (la de revista con Beckham y un QR por la de Cannes 2009) está bien hecho. El estadio va rotulado «foto actual». Sin escudos ni logotipos; nada sugiere que Roux, Cantona o el Auxerre apoyen ProTeam.
- **Texto solapado (bloqueante):** de **22,4 a 22,9 s** el logo «ProTeam» del cierre entra en **fundido cruzado encima del remate** «UN EQUIPO NO SE FICHA: SE CONSTRUYE.» y de la escalera (fotograma de 22,5 s: «ProTeam» sobre el peldaño «PRIMERA»). Es el mismo fallo que hizo suspender `v7-puerta-de-atras-carril` y `v7-techo-forest-clough`.

## Verdad y fuentes
Cada frase tiene fuente en el guion: entrenador-jugador en 1961 con el club en la Division d'Honneur, cuarto nivel y fútbol regional (Wikipedia; UEFA.com); Primera en 1980 (Wikipedia; AJ Auxerre; Gulf News); centro de formación y Cantona como canterano (Wikipedia; Goal), sin dar el año; Liga y Copa de 1995–96 (UEFA.com; Wikipedia; Inside Futbol); 44 años, 1961–2005 (UEFA.com, «Roux stands down after 44 years»). El caption dice «una Liga y cuatro Copas»: correcto (1994, 1996, 2003 y 2005). Único matiz: «Cuarenta y cuatro años en el mismo banquillo» pasa por encima del año fuera (2000–01); el guion lo sabe y no dice «seguidos». Aceptable.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 12/20 | La historia es muy buena para entrenadores de base y el remate se cita solo. Pero el gancho es justo lo que el criterio prohíbe: abre con el año («En 1961,») y **de 0,0 a 1,5 s solo se ve «En 1961,» sobre la pared vacía**; la primera foto llega a 1,5 s. El dato que engancha (44 años, de Regional a campeón) está en el caption, no en los primeros 3 s. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Muy bien: la ficha se posa en «REGIONAL» (3,0 s), silbato y botas con «entrenador-jugador», «GUY ROUX.» en su palabra, la ficha sube peldaño a peldaño con el contador 1961→1980 hasta «PRIMERA» (8,5 s), las chapas salen de la pizarra y de ahí sale Cantona, los trofeos se encienden con «Liga» y «Copa», «44 AÑOS» y el banquillo, «FICHA» tachada y «CONSTRUYE» en ultravioleta. Flojo: con «Cuarenta y cuatro» (15,7–16,2 s) el calendario aún va por 1998 y «44 AÑOS» entra a ~16,4 s; el primer segundo y medio no anima nada. |
| Transiciones | 11/15 | Los viajes de cámara son suaves y caen en las pausas. El final no: el remate no se queda solo y quieto; el logo del cierre entra en fundido cruzado sobre él (22,4–22,9 s) en lugar de fundido a negro. |
| Sonido | 13/15 | Voz confiada y clara, pronunciación francesa bien resuelta, piano y cuerdas suaves debajo, efectos bajos. −17,2 LUFS y −0,9 dBTP. La voz del cierre entra a 0,88 s del remate: bien. |
| Verdad y fuentes | 14/15 | Todo con fuente; el «mismo banquillo» simplifica el año fuera. |
| Estética | 11/15 | Paleta, tipografías y ultravioleta una sola vez (CONSTRUYE), bien. Pero el **tercio inferior está vacío** en 0–2 s, 4–6,5 s, 10–12,5 s y 13–15 s (la mitad de abajo de la pantalla, solo pared), y el logo se solapa con el remate. Los créditos del pie final (21,0–22,4 s) se leen a duras penas a tamaño móvil. |
| **Total** | **78/100** | No sale (mínimo 85 y hay texto solapado). |

## Correcciones para Marta A (por orden)
1. **Final sin solape (obligatoria):** «UN EQUIPO NO SE FICHA: SE CONSTRUYE.» entero y quieto, con la cámara parada, al menos 1,0 s después de «construye» (acaba a 21,80 s) → hasta ~22,8 s; luego **fundido a NEGRO de 0,5 s** y outro2 desde negro (como `v7-pantalla-gladiator-guardiola-2009` y `v7-sistema-lobanovski` r3). Mover a la vez en `mix.py` el audio de outro2 y el sting (voz del cierre ~0,3 s después del fin del fundido). Ningún fotograma con el logo encima del remate.
2. **Gancho (obligatoria):** el fotograma 0 tiene que enseñar ya la historia. Opción barata, sin voz nueva: desde el fotograma 0, la foto del estadio con la ficha «AUXERRE · 1961» y la escalera con la ficha azul en «REGIONAL», más un sello grande «44 AÑOS · MISMO BANQUILLO» que se apaga al llegar a «Lo cogió» (3,8 s). Opción mejor (si Dani da el visto bueno y hay créditos): nueva primera frase con la decisión rara delante, p. ej. «Cogió al Auxerre en Regional y no se fue en cuarenta y cuatro años.», y luego la escalera. En cualquier caso, nada de pared vacía en 0–1,5 s.
3. **Llenar el tercio inferior:** bajar o agrandar las escenas de 0–2 s, 4–6,5 s (Roux con silbato y botas: subir la ficha «GUY ROUX · ENTRENADOR-JUGADOR» bajo la foto, más grande), 10–12,5 s (pizarra + Cantona: bajarlos 200–300 px) y 13–15 s (trofeos más grandes y más abajo).
4. **«44 AÑOS» en su palabra:** que el calendario llegue a 2005 y «44 AÑOS» entre con «Cuarenta» (15,7 s), no 0,7 s después.
5. **Créditos del pie a ≥ 17 px** y quietos ≥ 1,5 s (antes del fundido a negro).
6. Después: `video_mudo.mp4` nuevo en el repo, vídeo nuevo en la cola (`files_old` con 1565e42c) y en el panel a la vez; whisper otra vez (51 palabras + cierre).

Voz, música, efectos, fotos, datos y caption: no hay que tocarlos (salvo la opción 2b del gancho).
