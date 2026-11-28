# Crítica · v7-walkie-luis-enrique-2022 «La voz del míster» · r1

**Andrés (05) · 28/11/2026 · Nota: 79/100 → NO APROBADO. Vuelve a montaje.**

Material revisado: el vídeo **de la cola** (`publicar/cola.json` → `b940744c-…mp4`, 26,0 s), descargado y analizado en el sandbox de Higgsfield (faster-whisper small con marcas por palabra, niveles por segundo y EBU R128), y `tools/reel_v7/v7-walkie-luis-enrique-2022/video_mudo.mp4` (fotogramas cada 0,5 s a tamaño móvil).

## Comprobaciones duras
- **Voz entera** (whisper): «Septiembre de 2022. España entrena (lo escribe «entra») en Las Rozas. Luis Enrique («Andríguez») lo mira desde un andamio, con un walkie-talkie. Cada jugador lleva un altavoz en el chaleco. Vais a oír la voz del míster. Corrige a Koke («Coque»), a Morata, a Gavi («Gaby»), en pleno ejercicio. Sin dejarse la garganta. La corrección que sirve llega en el momento y sin gritar.» Igual que «## Voz»; los nombres se oyen bien, son errores de whisper small. «gritar» acaba a 21,42 s.
- **Cierre nuevo:** «Dale like y síguenos para más vídeos como este» (22,32–25,20 s). En pantalla, «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este». **No se dice «app» en ningún momento.**
- **Caption de la cola:** termina con «¿Te ha servido? Dale like y síguenos para más vídeos como este.» Sin app, producto, lista, lanzamiento, precios, fechas de lanzamiento, cifras de apuntados ni nombre de Biel. **Ojo:** la caption del panel (posts) aún tiene el cierre antes de fuentes y hashtags; tiene que terminar igual que la de la cola.
- **Niveles:** −19,1 LUFS integrados, pico −0,9 dBTP. Voz estable entre −17 y −23 dB RMS por segundo; música suave (Epidemic, piano real) y efectos bajos. Correcto pero **flojo de volumen**: los demás v7 van a −16/−17 LUFS.
- **Datos:** todo con fuente en el guion: septiembre de 2022 en Las Rozas, andamio (EFE; OKDiario; Soccerway), walkie-talkie conectado a altavoces en el chaleco/peto (Soccerway; EFE), «Vais a oír la voz del míster» y «así no me dejo la garganta» (EFE), correcciones a Koke, Morata y Gavi (EFE). «En pleno ejercicio» es inferencia razonable y el guion lo declara. No se dicen altura, número de altavoces ni «el primero». Correcto.
- **Fotos:** Luis Enrique (Lluís from Sabadell, CC BY 2.0), Ciudad del Fútbol (Roberto, CC BY-SA 3.0, escudo difuminado) y walkie (Варвара Каминская, CC BY-SA 4.0, rotulado recreación); «modificadas» en la caption. Sin escudos ni nada que sugiera apoyo a ProTeam.

## Lo que falla
1. **Gancho de «Fecha, lugar».** La voz abre con «Septiembre de 2022. España entrena en Las Rozas.»: es justo el arranque que el criterio prohíbe («nunca "Lugar, año."»). El fotograma 0 es un calendario con «Septiembre»: no hay foto de la historia ni palabra fuerte. Lo raro (un seleccionador subido a un andamio hablando por walkie-talkie) no llega hasta 5,6–7,3 s.
2. **El remate no respira.** «y SIN GRITAR.» está entero desde ~21,0 s, pero «gritar» acaba a 21,42 s y el fundido a negro empieza a 22,04 s: solo 0,6 s quieto después de la voz (hace falta ≥ 1 s). «Dale» entra a 22,32 s, 0,9 s después de «gritar».
3. **Texto cortado en los viajes.** A 7,5 s «…ada» y «Lu / desc / con un» cortados por los bordes; a 12,0 s «a oír / del MÍSTER.»» cortado por la izquierda; a 18,0 s una «C» suelta en el borde derecho. A tamaño móvil se nota.
4. **Volumen bajo:** −19,1 LUFS, 2–3 LU por debajo del resto de la cuenta; en el móvil sonará más flojo que el vídeo anterior del feed.
5. **Pie de créditos ilegible** (~21,5 s): letra diminuta que no se puede leer a tamaño móvil. Los créditos ya van en la caption.
6. Menor: a 3,0 s el rectángulo del campo aparece vacío medio segundo antes de dibujarse los conos.

## Lo que está bien
Cada cosa entra con su palabra: «2022.», polaroid de Las Rozas, torre de andamio que sube tramo a tramo con «andamio,», walkie con sus tres arcos en «WALKIE-TALKIE.», los once chalecos que se encienden con «altavoz», el bocadillo de radio con «MÍSTER.», KOKE/MORATA/GAVI en la pizarra en su nombre, megáfono tachado en «garganta», reloj y «EN EL MOMENTO...» en ultravioleta (única vez). Remate citable. Fundido a negro y cierre sin solapes.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 12/20 | Historia muy buena y remate citable, pero abre con «Septiembre de 2022.» y el fotograma 0 es un calendario; lo raro llega a 5,6 s. |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Todo entra con su palabra; solo el campo vacío a 3,0 s. |
| Transiciones | 11/15 | Viajes suaves, pero arrastran texto cortado (7,5 / 12,0 / 18,0 s). |
| Sonido | 12/15 | Voz clara y confiada, música y efectos reales y bajos; −19,1 LUFS y cierre pegado al remate. |
| Verdad y fuentes | 14/15 | Todo con fuente; «en pleno ejercicio» es inferencia (declarada). |
| Estética | 12/15 | Paleta, tipografías y fotos con licencia bien; textos cortados en viajes, pie ilegible, remate que respira poco. |
| **Total** | **79/100** | |

## Correcciones (para Marta, 02)
1. **Gancho nuevo (voz nueva, misma voz Mateo):** que abra con la decisión rara, no con la fecha. Propuesta: «Luis Enrique entrenaba a España subido a un andamio. Con un walkie-talkie. Cada jugador lleva un altavoz en el chaleco. Las Rozas, septiembre de 2022. «Vais a oír la voz del míster.» Corrige a Koke, a Morata, a Gavi, en pleno ejercicio. Sin dejarse la garganta. La corrección que sirve llega en el momento... y sin gritar.» (mismas palabras y fuentes, solo cambia el orden; la fecha y el lugar pasan a la cuarta frase).
2. **Fotograma 0 con el gancho:** a 0,0 s ya deben verse la ficha de Luis Enrique junto a la torre de andamio y la palabra «ANDAMIO» (o «Luis Enrique» + andamio). El calendario y la polaroid de Las Rozas pasan a la frase de la fecha.
3. **Remate entero y quieto ≥ 1 s** después de «gritar», con la cámara parada; fundido a negro de 0,5 s después y outro2 desde negro, con «Dale» ~1,3–1,5 s después de «gritar».
4. **Nada cortado en los viajes:** que los textos se apaguen antes de salir por el borde (7,5 / 12,0 / 18,0 s).
5. **Loudness a −16/−17 LUFS**, pico ≤ −1,0 dBTP (sube la voz; música y efectos en la misma proporción).
6. Quita el pie de créditos de pantalla (siguen en la caption) o súbelo a 17 px y quieto ≥ 2 s. Que los conos se dibujen con el campo (sin rectángulo vacío).
7. Caption del panel igual que la de la cola (que termine en «¿Te ha servido? Dale like y síguenos para más vídeos como este.»).
8. Sube el `video_mudo.mp4` nuevo, el vídeo nuevo a cloudfront, `files` de `publicar/cola.json` (sigue en «revisión») y el panel. Después, tarea «Auditar v7 v7-walkie-luis-enrique-2022».
