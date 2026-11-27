# Crítica · v7-tacos-berna-1954 «Los tacos de Berna» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 83/100 → NO APROBADO (suspenso automático: texto cortado). Vuelve a montaje.**

Material revisado: `tools/reel_v7/v7-tacos-berna-1954/video_mudo.mp4` (61 fotogramas, uno cada 0,5 s, a 270 px de ancho, y recortes a tamaño completo donde hacía falta), `reel.html`, `words.js`, `CREDITOS.md`, el guion y el vídeo final de cloudfront (`015b942e-…mp4`, 30,7 s), descargado y analizado en el sandbox de Higgsfield.

## Comprobaciones duras
- **Voz entera:** faster-whisper small oye toda la historia: «Hungría llevaba cuatro años sin perder. En el Mundial del 54 había goleado a Alemania, 8-3. En la final de Berna, llovió. Fritz Walter, su capitán, jugaba mejor cuanto peor estaba el campo. Y sus botas llevaban tacos de rosca. Los cambiaron por unos más largos. Alemania ganó 3-2. No eliges el campo. Eliges cómo llegas.» Y el cierre común (25,4–29,6 s).
- **Niveles:** −15,9 LUFS integrados, true peak −1,2 dBTP. La voz va entre −16 y −22 dB RMS por segundo; las pausas solo con música, entre −31 y −32,5 dB (2, 14 y 19 s): la voz va 12–15 dB por encima. Los picos de −1,3/−1,6 dBFS están en el cierre (25–26 s), no en efectos. La lluvia y los clics de rosca no asoman.
- **Destellos:** ninguno. El salto máximo de luminancia media entre fotogramas es de 7,1/255 (viaje de 14,5 s).
- **Fotos:** Comet Photo AG (CC BY-SA 4.0) y Sandstein (CC BY 3.0), con crédito en el pie y en el caption. Sin logos de marca (el rótulo del reloj está fuera de encuadre; la bota es genérica, sin rayas). Nada sugiere que nadie apoye ProTeam.
- **Música:** real, de Epidemic («Orchestra, Epic, Dreamy, Suspense»), una sola pista.
- Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel.
- **Texto cortado → SUSPENSO AUTOMÁTICO.** «TRES A DOS…» (línea `f2`, 20,9–22,0 s) mide más que el ancho del vídeo: la T empieza en la columna 0 y el travesaño queda cortado por el borde izquierdo (a 21,6 s, recorte a tamaño completo); a la derecha acaba a 1035–1040 px. A 20,95 s se ve «TRES» pegado al borde y a 21,0 s, en la hoja de contactos, la frase entera desborda por la izquierda.

## Verdad y fuentes
Todo lo que dice la voz tiene fuente en el guion: cuatro años sin perder y el 8-3 (The Irish Times, Ashdown 2018), la lluvia en Berna (DPMA; The Irish Times; Deutsches Fußballmuseum), «Fritz-Walter-Wetter» (Fußballmuseum; DPMA), los tacos de rosca cambiados por otros más largos (DPMA; The Irish Times) y el 3-2. El remate va sin comillas, como idea. Bien.
Detalle: el reloj de Wankdorf (7,5–10,0 s) ya enseña «2 · Ungarn / 3 · Deutschland» antes de «Alemania ganó tres a dos». No es falso (es el reloj de la final), pero destripa el giro diez segundos antes.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | Historia buena y poco contada; el gancho «cuatro años sin perder» funciona. El remate se queda corto en pantalla (ver transiciones). |
| Cada cosa que dice la voz se anima en su momento | 16/20 | Muy bien: el calendario que pasa 1950→1954 y «0 DERROTAS», tablillas 8–3 con ocho y tres fichas, lluvia en «llovió», círculo sobre Walter, barras CAMPO/WALTER que se cruzan en «peor», seis tacos que entran girando y el TACO CORTO → TACO LARGO. Flojo: el marcador está vacío de 3,0 a 5,9 s (tres segundos con tablillas en blanco y media pantalla vacía debajo); el reloj con el 2-3 adelanta el resultado; la bota del remate (22–25 s) es de otro dibujo que la suela de antes. |
| Transiciones | 13/15 | Viajes suaves en las pausas, sin destellos. Pero «llegas» acaba a 24,9 s y el fundido al cierre empieza a 25,1 s: «CÓMO LLEGAS.» completo solo se ve ~0,5 s. |
| Sonido | 13/15 | Voz confiada y clara, música suave a 12–15 dB, efectos bajos y reales. True peak −1,2 dBTP. |
| Verdad y fuentes | 14/15 | Todo con fuente; resta el spoiler del reloj, que confunde el orden del relato. |
| Estética | 10/15 | Paleta, tipografías y fotos, bien; ultravioleta una sola vez (CÓMO LLEGAS). Pero «TRES A DOS…» cortado por la izquierda (bloqueante), tercio inferior vacío en 3,0–7,0 s y 15,0–22,0 s, y créditos del pie ilegibles en el móvil. |
| **Total** | **83/100** | Suspenso automático por texto cortado. |

## Correcciones (para Marta, 02)
1. **(Bloqueante) «TRES A DOS…» dentro del cuadro.** En `line('f2',…)` baja el tamaño (p. ej. 110–120 px en lugar del actual) o pártela en dos líneas («TRES A DOS…» con «A DOS…» debajo), con ≥ 60 px de margen a cada lado durante toda la deriva de cámara (20,4–22,1 s). Comprueba con un fotograma a tamaño completo a 21,0 y 21,6 s.
2. **Remate visible.** Que «CÓMO LLEGAS.» quede entero y quieto al menos 1,2 s antes del fundido: alarga la historia (cierre a ~26,0 s) en vez de cortar a 25,1 s. El audio puede alargarse con 0,8–1 s de música antes de la cola del cierre.
3. **Reloj sin spoiler.** Encuadra la polaroid del reloj solo en la esfera (sin «2 / 3» ni «Ungarn / Deutschland»), o tapa el marcador con las gotas, y deja el 3-2 para su escena.
4. **Marcador vacío (3,0–5,9 s).** Que el marcador entre con «Mundial» y que las tablillas no esperen en blanco tres segundos: por ejemplo, que «MUNDIAL 1954» y los nombres entren a 3,3 s y las tablillas aparezcan a 5,4 s («Alemania»), justo antes del «ocho».
5. **Tercio inferior.** Sube un poco las escenas 2 y 5/6 o llena el hueco (las fichas del 8-3 más abajo y grandes; la regla de tacos más alta) para que no quede media pantalla vacía.
6. (Mejora) La bota del remate, del mismo dibujo que la suela (o la suela de lado con los tacos largos).
7. (Mejora) Créditos del pie a ≥ 17 px, como en los remontajes de Auerbach y Lobanovski.

El audio está bien (voz, música, efectos y aperturas): se puede reutilizar, ajustando solo el final si se alarga el remate (corrección 2).
Cuando esté montado, vuelvo a auditar lo cambiado y repaso todos los fotogramas.
