# Crítica v7 · v7-golpe-ciento-uno-spurs · «El golpe ciento uno»
**Andrés (05), 24/11/2026.** Vídeo final (23,5 s): https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/f035264d-d401-4da8-9621-306021b0c5c3.mp4 · mudo: tools/reel_v7/v7-golpe-ciento-uno-spurs/video_mudo.mp4 · guion: agencia/fabrica-v7/guiones/v7-golpe-ciento-uno-spurs.md

Revisado: 47 fotogramas (uno cada 0,5 s) a 270 px de ancho; tramos de viaje a 10 fps (5,1–5,9 · 6,75–7,55 · 12,9–14,5 s); diferencia entre fotogramas en todo el vídeo (máximo salto de luminancia 5,7/255: sin destellos); vídeo final descargado y transcrito con faster-whisper (small, es) en el sandbox de Higgsfield; niveles por segundo y por décima; licencias de las cuatro fotos consultadas otra vez en la API de Wikimedia Commons.

## Nota: 86/100 → APROBADO (≥ 85)

| criterio | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | «La misma frase estaba en cinco idiomas» engancha y la parábola del cantero se cierra sola con «fueron todos los anteriores». Buen arco curiosidad → tensión (100, nada) → alivio (101). El gancho tarda 3 s en llegar al dato («cinco idiomas» a 4,2 s). |
| Cada cosa que dice la voz se anima | 18/20 | Taquillas en «vestuario» (0,5 s), ficha de Duncan en «Spurs» (1,0), foto y ficha de Popovich (1,5–2,0), cinco cartelas una a una y «cinco idiomas» (3,5–5,0), foto del cantero y ficha de Riis (5,5–6,5), contador 1→100 durante «golpea… cien veces» (7,4–9,5), lupa en «ni una grieta» (10,0–10,5), «101» en «ciento uno» (11,5), grieta ultravioleta y mitades que se separan en «se parte en dos» (12,4–13,5), marca 101 en «ese golpe» (15,0–15,5), las 100 rayitas se encienden en «todos los anteriores» (16,0–17,5). El mazo apenas se mueve mientras sube el contador: se lee como dibujo quieto. |
| Transiciones | 12/15 | Tres viajes de 0,9 s con `power2.inOut`, desenfoque ≤ 4 px, sin destellos ni cortes; fundido limpio al cierre (18,0 s). Pero los viajes no respetan del todo la pausa: el de 4,95 s empieza antes de que acabe «idiomas» (5,10) y llega después de «Habla» (5,74 → 5,85); el de 6,75 s sale antes del final de «cantero» (6,88) y llega 0,3 s tarde a «Golpea» (7,34 → 7,65), con el contador ya en marcha a mitad del viaje; el de 13,45 s sale antes de que acabe «dos» (13,52) y llega 0,3 s tarde a «Y sabe» (14,04 → 14,35): el remate de la piedra partida casi no tiene respiro. El viaje de 6,75 s es muy largo (≈1 960 px en vertical) y se nota rápido. |
| Sonido | 12/15 | Voz confiada; whisper saca las 49 palabras («Greg», «101» y «se parten dos», por elisión). −19,3 LUFS integrados, pico −1,0 dBFS, LRA 3,1. En las pausas el fondo queda en −27/−33 dB RMS frente a −14/−19 de la voz: 10–14 dB por debajo. Efectos discretos, sin picos sobre la voz; golpes de maza muy bajos (8,0–8,4 s ≈ −33/−44 dB). Música real de Epidemic (piano y cuerdas), encadenada sin cortes. Pega: 2–3 LU más bajo que los otros v7 (−16/−17 LUFS). |
| Verdad y fuentes | 15/15 | Todo lo que dice la voz está en el guion con fuente: cinco idiomas (Bleacher Report, 20/10/2014: español, francés, portugués y latín + inglés junto a la taquilla de Duncan), lema de Popovich, texto de Riis (1901) con el «perhaps a hundred times» traducido como «quizá cien veces». Caption «desde los noventa» = 17 años en 2013 (CBS Sports). No afirma piedra y martillo reales en el vestuario. Licencias comprobadas hoy: Keith Allison CC BY-SA 2.0; «Mike» CC BY-SA 2.0 (Popovich); J. W. Chapman-Taylor, dominio público; Jacob Riis, Library of Congress, dominio público. Créditos en el caption. |
| Estética | 12/15 | Paleta y tipografías del formato; B/N con el azul conservado; ultravioleta una sola vez (grieta). Recortes limpios, nada cortado en reposo. Pegas: de 7,6 a 17,6 s el tercio inferior de la pantalla queda vacío (piedra, contador y rayitas viven en el 60 % superior); pie de créditos (17,0–18,0 s) ilegible en móvil; las fichas de foto llevan texto de ~5 px. |

Bloqueantes: ninguno (sin nombre de Biel, sin fechas ni precios, sin cifras de apuntados, fotos con licencia y sin sugerir apoyo a ProTeam, sin texto cortado ni solapado en reposo, música real de Epidemic).

## Correcciones (para la próxima versión; no bloquean)
1. Viajes: que empiecen al final de la palabra (5,12 · 6,90 · 13,55 s) y lleguen antes de la siguiente; con viajes tan largos, 0,8 s o acercar las escenas en la pared.
2. 13,5 s: dejar 0,4 s quieta la piedra partida antes de salir.
3. 7,4–9,5 s: que el mazo golpee (subir y caer) a ritmo del contador.
4. 7,6–17,6 s: bajar la composición o subir el tamaño de la piedra y las rayitas para llenar el tercio inferior.
5. Mezcla: normalizar a −16/−17 LUFS como el resto de v7, con techo −1,5 dBTP.
6. Pie de créditos a ≥ 22 px en 1080 o solo en el caption.

Programado: `pub_v3.py approve v7-golpe-ciento-uno-spurs 2026-11-28T18:00:00+01:00` (25/11 v7-bielsa, 26/11 v7-peor-verano-2003 y 27/11 v7-boot-room-anfield ocupan las 18:00).
