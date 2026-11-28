# Crítica · v7-libreta-reep-1950 «La libreta de Swindon» (historia con fotos)

**Andrés (05) · 28/11/2026 · Nota: 81/100 → NO SALE (a remontaje con Marta A, tarea «Montar v7 v7-libreta-reep-1950»).** Historia limpia, datos bien atados y buen remate. Falla el arranque: abre con «Swindon, 1950.» (lugar y año, lo que el criterio prohíbe como gancho) y el fotograma 0 es casi pared vacía con «Swindon,» a medio aparecer. El final va justo: el remate solo está quieto 0,65 s y el «Dale» entra 0,9 s después de «no».

Material revisado: vídeo de la cola (`publicar/cola.json` → `cc56321e-…mp4`, 26,7 s), descargado en el sandbox de Higgsfield y transcrito con faster-whisper small; `tools/reel_v7/v7-libreta-reep-1950/video_mudo.mp4` (26,7 s, 1080×1920, 30 fps): 53 fotogramas, uno cada 0,5 s, a 270 px, y sueltos a 0,0 / 1,5 / 22,3 s a 540 px.

## Comprobaciones duras
- Sin app, producto, lista de espera ni lanzamiento en voz, pantalla ni caption. ✔
- Cierre outro2 en pantalla («ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este») y en voz (22,88–25,82 s). Caption termina con «¿Te ha servido? Dale like y síguenos para más vídeos como este.» ✔
- **Voz entera (whisper):** «Swindon, 1950. En la grada, un contable de la RAF se desespera. Su equipo ataca sin parar y falla y falla. En el descanso saca un lápiz y una libreta y apunta qué pasa con cada balón. Se llamaba Charles Rip [Reep]. Acabó anotando más de 2.000 partidos, la memoria te engaña. La libreta, no.» Las 55 palabras del guion. ✔
- **Niveles:** −17,7 LUFS integrados, true peak −0,9 dBFS, LRA 2,8 LU. Voz entre −18 y −21 dB RMS por segundo; huecos −23 a −25; el negro de 22 s, −33,6. Música real (Epidemic, orquesta/piano/coro) suave; efectos bajos (pico −1,0 a 8 s en las cruces de la pizarra, aceptable). ✔
- Fotos: Andrew Smith (CC BY-SA 2.0), Jonas Petersson (CC BY-SA 4.0), Steve Daniels (CC BY-SA 2.0), marcadas «modificada». Nada sugiere apoyo a ProTeam. Sin precios, nombre de Biel ni cifras. Ultravioleta solo en «2.000+». ✔

## Verdad y fuentes
Contable y Wing Commander de la RAF (Forces News; SPA; WSC), Swindon–Bristol Rovers en el County Ground en marzo de 1950 (Forces News; SPA; WSC: 18/03/1950), libreta en el descanso / al empezar la segunda parte (SPA; Forces News), más de dos mil partidos (SPA 2.200; WSC casi 2.500). Todo cuadra. Detalle: la postal de 2011 lleva la etiqueta «HOY»; el pie dice «COUNTY GROUND · 2011», así que «HOY» sobra (no es de hoy).

## Línea de tiempo (lo que se ve)
- **0,0 s:** pared casi vacía con «Swindon,» apareciendo en gris; sin foto ni palabra fuerte. ✘ La postal y «1950.» llegan a ~1 s.
- 0,5–2,3: postal del County Ground «SWINDON · 1950» con «FOTO DE 2006» y matasellos; «1950.» grande. ✔ (el rótulo de 2006 está bien puesto).
- 2,5–3,0: viaje; «Swindon, 950.» sale por el borde durante el movimiento (aceptable, es viaje).
- 3,0–6,0: grada con silueta, ficha «CONTABLE · RAF» que se escribe en su palabra; «RAF» en azul. ✔
- 6,5–9,6: pizarra; tres ataques en «ataca sin parar», cruz en cada «falla». ✔ Muy bien sincronizado.
- 10,0–12,4: «DESCANSO», foto del lápiz y la libreta, hoja «2.ª PARTE». ✔
- 12,8–14,7: los símbolos se escriben línea a línea con el balón. ✔
- 15,0–16,4: ficha «CHARLES REEP · SIN FOTO», subrayado. ✔
- 16,5–17,5: «Acabó anotando» con la pila empezando muy abajo: medio segundo con la pantalla casi vacía. (leve)
- 17,5–19,0: contador 1.083 → 1.924 → «2.000+» ultravioleta y pila de libretas. ✔
- 19,4–22,0: postal «COUNTY GROUND · 2011 · HOY», libreta abierta, «memoria» se desenfoca, «LIBRETA» nítida, «no.» a 21,82–22,00. ✔
- **22,0–22,65:** remate quieto solo 0,65 s; créditos del pie a ~15 px y solo ~0,6 s en pantalla (no se leen). ✘
- 22,65–23,15: fundido a negro. 23,15–26,7: outro2. «Dale» a 22,88 s, 0,9 s después de «no». ✘ (corto)

## Nota
| criterio | nota | por qué |
|---|---|---|
| Historia real y gancho | 13/20 | Historia y remate muy buenos («La memoria te engaña; la libreta, no»), pero abre con «Swindon, 1950.» (lugar, año) y el fotograma 0 está vacío. |
| Cada cosa que dice la voz se anima | 18/20 | Casi todo en su palabra; solo el hueco de «Acabó anotando». |
| Transiciones | 12/15 | Viajes suaves; el final va corto (0,65 s quieto, cierre pegado). |
| Sonido | 14/15 | Voz clara y segura, música real, efectos bajos. |
| Verdad y fuentes | 14/15 | Todo con fuente; «HOY» en una foto de 2011. |
| Estética | 10/15 | Fotograma 0 vacío; créditos ilegibles; resto limpio. |
| **Total** | **81/100** | |

## Correcciones (Marta A)
1. **Gancho (obligatorio):** voz nueva con la primera frase cambiada de sitio, sin tocar el resto: «En la grada, un contable de la RAF se desespera. Swindon, 1950. Su equipo ataca sin parar…» (o, si encaja mejor, «Un contable de la RAF apuntó más de dos mil partidos a lápiz.» como primera frase, y sigue «Swindon, 1950. En la grada…»). Misma voz Mateo, mismo prompt; comprobar con whisper.
2. **Fotograma 0:** ya entero, sin fundido de entrada: silueta en la grada y ficha «CONTABLE · RAF» (o la palabra fuerte de la frase nueva) visibles desde 0,0 s.
3. **Remate:** «La LIBRETA, no.» quieto ≥ 1,0 s con la cámara parada; fundido a negro 0,5 s después; «Dale» de outro2 ~1,5 s después de «no» (mover outro2 y su sting a la vez en mix.py).
4. Quitar la etiqueta «HOY» de la postal de 2011 (basta «COUNTY GROUND · 2011»).
5. Créditos del pie: o a ≥ 17 px y quietos ≥ 2 s, o fuera de pantalla (ya están en el caption).
6. Opcional: que la pila de libretas arranque ya visible en «Acabó anotando» para no dejar la pantalla vacía 0,5 s.
7. Subir el video_mudo.mp4 nuevo al repo y actualizar a la vez la cola (`files`, guardando el actual en `files_old`) y el panel. Caption sin cambios.
