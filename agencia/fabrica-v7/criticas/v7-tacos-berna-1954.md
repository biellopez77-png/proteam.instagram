# Crítica · v7-tacos-berna-1954 «Los tacos de Berna» (historia con fotos)

## r2 · Andrés (05) · 28/11/2026 · Nota: 86/100 → NO APROBADO (suspenso automático: texto solapado en el paso al cierre). Vuelve a montaje.

Material revisado: `tools/reel_v7/v7-tacos-berna-1954/video_mudo.mp4` (30,0 s; 60 fotogramas, uno cada 0,5 s, a 270 px, y fotogramas a tamaño móvil en 0,0 · 21,2 · 25,4 · 25,8 · 26,1 · 26,3 · 28,0 s) y el vídeo final de la cola (`b8db7439-…mp4`, 30,0 s), descargado y analizado en el sandbox de Higgsfield.

### Comprobaciones duras
- **Voz entera (faster-whisper small):** «Hungría llevaba cuatro años sin perder. En el Mundial del 54 había goleado a Alemania, 8-3. En la final de Berna, llovió. Fritz Walter, su capitán, jugaba mejor cuanto peor estaba el campo. Y sus botas llevaban tacos de rosca. Los cambiaron por unos más largos. Alemania ganó 3-2. No eliges el campo. Eliges cómo llegas.» Igual que el guion. «llegas» acaba a 24,92 s.
- **Cierre nuevo:** voz «Dale like y síguenos para más vídeos como este» (25,94–29,16 s); en pantalla «¿Te ha servido? Dale like y síguenos · PARA MÁS VÍDEOS COMO ESTE». Nada de app, producto, lista de espera ni lanzamiento (ni en voz, ni en pantalla, ni en el caption). El caption lleva el cierre nuevo (después van fuentes, créditos y hashtags, como en los v7 ya aprobados).
- **Niveles:** −16,0 LUFS integrados, true peak −1,6 dBFS. Voz entre −15 y −22 dB RMS por segundo; pausas solo con música a −30/−32 dB (2, 14, 19, 25 s). Efectos bajos.
- **Destellos:** ninguno. El cambio más brusco (salida de la foto de Walter, 14,4–14,6 s) baja la luminancia de 61 a 21 en ~0,4 s, en rampa (máx. ~7/255 por fotograma).
- **Fotos y licencias:** Comet Photo AG (CC BY-SA 4.0) y Sandstein (CC BY 3.0), crédito en el pie (ahora legible, ~17 px) y en el caption. Nada sugiere que nadie apoye ProTeam. Música real (Epidemic).
- Sin precios, sin nombre de Biel, sin cifras de apuntados.

### Lo arreglado desde la r1 (83/100)
1. «TRES A DOS…» ya cabe: a 21,2 s va de ~60 a ~470 px (sobre 540), con margen. ✔
2. «CÓMO LLEGAS.» entero y quieto de ~24,5 a 26,1 s. ✔
3. Reloj de Wankdorf solo con la mitad alta de la esfera: ya no destripa el 3-2. ✔
4. El marcador entra con «Mundial» y las tablillas con «Alemania». ✔
5. Bota del remate de lado con «TACOS LARGOS». ✔  6. Créditos del pie legibles. ✔

### El bloqueante nuevo: texto solapado (26,1–26,5 s)
El paso al cierre es un fundido cruzado, no un fundido a negro. A **26,3 s** el logo «ProTeam» aparece encima de «No eliges el *campo.*», con las dos capas a media opacidad (fotograma a tamaño móvil). Es exactamente el solape que se corrigió en Rangnick, Reglas de Jordan, Lobanovski o Kerr con el fundido a negro. Por la regla de la casa (texto solapado) suspende.

### Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 18/20 | Primer fotograma ya con la foto de Hungría celebrando, «Hungría» y el calendario 1950; «cuatro años sin perder» es el dato raro. Remate citable. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Calendario 1950→1954 y «0 DERROTAS», tablillas 8–3 con fichas, lluvia en «llovió», círculo sobre Walter, barras CAMPO/WALTER que se cruzan en «peor», tacos que entran girando y TACO CORTO → TACO LARGO, 3–2 en su palabra. Resta: a 3,0 s el fotograma está casi vacío (llega el marcador aún sin nada) y en 3,5–5,0 y 7,5–10,0 s media pantalla de abajo sigue vacía. |
| Transiciones | 11/15 | Viajes de cámara suaves en las pausas, sin destellos. Pero el paso al cierre es un fundido cruzado que monta el logo sobre el remate (bloqueante). |
| Sonido | 14/15 | Voz confiada y clara, música suave 12–15 dB por debajo, efectos bajos y reales. La voz del cierre («Dale», 25,94 s) entra antes de que se vea el cierre (el remate sigue en pantalla hasta 26,1 s). |
| Verdad y fuentes | 15/15 | Todo con fuente en el guion (The Irish Times, DPMA, Deutsches Fußballmuseum); el reloj ya no adelanta el resultado. |
| Estética | 11/15 | Paleta, tipografías y fotos, bien; ultravioleta una sola vez (CÓMO LLEGAS). Resta el solape del logo con el remate y los tercios inferiores vacíos. |
| **Total** | **86/100** | **Suspenso automático por texto solapado.** Con el fundido a negro se aprueba. |

### Correcciones (para Marta, 02)
1. **(Bloqueante) Fundido a negro, no cruzado.** Remate quieto hasta 26,0 s; fundido a NEGRO de 0,5 s (xfade `fadeblack`) 26,0–26,5 s; outro2 desde negro a 26,5 s. Que en ningún fotograma se vean a la vez el logo y el texto del remate (comprueba 26,0 · 26,25 · 26,5 s a tamaño completo).
2. **Voz del cierre detrás de la imagen.** Mueve el audio de outro2 (y el sting) para que «Dale» entre a ~26,7 s, con el cierre ya en pantalla. El vídeo pasará a ~30,8 s; nada más del audio cambia.
3. (Mejora) A 3,0 s, que el marcador «MUNDIAL 1954» ya esté entrando cuando acaba el viaje (sin el fotograma casi negro).
4. (Mejora, opcional) Bajar un poco el marcador del 8–3 y el reloj para que no quede media pantalla vacía debajo.
5. Sube el `video_mudo.mp4` nuevo, la cola (`files_old` con b8db7439) y el panel a la vez.

Cuando esté, audito solo 25,0–31,0 s y repaso la hoja de contactos entera.

---

## r1 · Andrés (05) · 27/11/2026 · Nota: 83/100 → NO APROBADO (suspenso automático: texto cortado)
Resumen: «TRES A DOS…» desbordaba por la izquierda (20,9–22,0 s); «CÓMO LLEGAS.» completo solo ~0,5 s; el reloj de Wankdorf enseñaba el 2-3 antes de tiempo; marcador vacío 3,0–5,9 s; tercio inferior vacío; créditos del pie ilegibles. Audio, fuentes y fotos, bien. Todo corregido en la r2 salvo el tercio inferior (parcial).
