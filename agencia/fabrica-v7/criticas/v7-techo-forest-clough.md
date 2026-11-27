# Crítica · v7-techo-forest-clough «El techo no lo pone la categoría» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 76/100 → NO SALE (a remontaje con Marta, tarea «Montar v7 v7-techo-forest-clough»).** Historia, datos y fotos, bien. Falla el final: el remate no se llega a leer y el logo de outro2 entra en fundido cruzado encima de «La categoría no pone tu techo» (texto solapado = suspenso automático). Además el vídeo arranca con medio segundo de pared vacía.

Material revisado: el vídeo de la cola (`publicar/cola.json` → `3a37f267-…mp4`, 27,1 s, 1080×1920, 30 fps, H.264 + AAC), descargado en el sandbox de Higgsfield: 54 fotogramas, uno cada 0,5 s, a 216 px (tamaño móvil), y fotogramas sueltos a 0,0 / 0,3 / 20,8 / 22,9 / 23,2 / 23,4 s a 360 px.
Ojo: `tools/reel_v7/v7-techo-forest-clough/video_mudo.mp4` del repo es el ANTIGUO (29,2 s) y acaba con el cierre retirado («Estamos terminando la app. Síguenos para no perderte nada»). Hay que sustituirlo.

## Comprobaciones duras
- **Vídeo de la cola:** sin app, producto, lista de espera ni lanzamiento en voz ni en pantalla. Cierre outro2 en pantalla («ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este») y en voz («Dale like y síguenos para más vídeos como este», 23,54–26,28 s). Caption de la cola: termina con el cierre nuevo. ✔
- **Panel:** el post `v7-techo-forest-clough` aún tenía el caption viejo («Estamos terminando la app de ProTeam…») y el vídeo viejo (`8e7e13db`). Corregido por Andrés: caption = el de la cola, vídeo = `3a37f267`. **No debe salir nada con el caption viejo.**
- **Repo:** `video_mudo.mp4` con el cierre de la app (ver arriba). ✘ (no sale a redes, pero hay que cambiarlo).
- **Voz entera (faster-whisper small):** «1977. El Nottingham Forest de Brian Clough sube de segunda por los pelos. Un año después, recién ascendido, es campeón de Inglaterra. Y no se para ahí. Copa de Europa en 1979 y otra en 1980. Dos finales, dos goles. Francis y Robertson. La categoría no pone tu techo. Lo pone lo que entrenas cada semana.» Están todas las palabras; «Clough» y «Robertson» bien.
- **Niveles:** −17,0 LUFS integrados, true peak −0,9 dBFS, LRA 3,8 LU. Voz entre −17 y −21 dB RMS por segundo; huecos con música entre −24 y −25. Música real (Epidemic, orquesta/piano/coro), suave bajo la voz; efectos bajos. ✔
- **Fotos:** Anefo/Hans van Dijk (CC0) ×2, Alan Murray-Rust (CC BY-SA 2.0), John Sutton (CC BY-SA 2.0). Sin escudos ni patrocinadores visibles; nada sugiere apoyo a ProTeam. ✔
- Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel. Ultravioleta solo en «techo». ✔

## Verdad y fuentes
Todo lo que dice la voz está en las fuentes del guion: ascenso de 1977 con 52 puntos, quinto peor botín de un ascendido (FourFourTwo) → «por los pelos» es justo; Liga 1977/78 recién ascendido (FourFourTwo; UEFA 2016); Copa de Europa 1979 en Múnich ante el Malmö y 1980 en Madrid ante el Hamburgo (UEFA 2015; FourFourTwo); las dos finales 1–0, gol de Francis en 1979 y de Robertson en 1980 (UEFA 2015; Wikipedia «1979 European Cup final»; Sky Sports; FourFourTwo). Placas «MÚNICH 1979» / «MADRID 1980» y marcadores «1–0», correctos. El remate es idea, no cita. Caption correcto.

## Línea de tiempo (lo que se ve)
- **0,0–0,5 s:** pared vacía, sin nada escrito. «1977.» aparece a ~0,5 s. ✘ (gancho)
- 0,5–2,0: «1977.» + sello «2.ª DIVISIÓN». ✔
- 2,3–4,1: ficha de Clough; título «El Nottingham Forest / de Brian Clough» palabra a palabra. ✔
- 4,1–5,7: escalera, ficha FOREST sube rozando; «POR LOS PELOS.» en su palabra. ✔
- 6,2–8,0: calendario 1977 → 1978 en «Un año después». ✔
- 8,3–9,8: postal del City Ground, tabla «1. FOREST», «CAMPEÓN de Inglaterra». ✔
- 10,2–15,0: viaje en «Y no se para ahí», copa MÚNICH 1979 en «1979», segunda copa MADRID 1980 y «×2» en «1980». ✔
- 15,8–19,0: foto de Francis, Clough y Robertson; dos «1–0» en «dos goles»; FRANCIS y ROBERTSON subrayados en su nombre. ✔
- 19,4–21,1: estatua, línea del techo, «techo.» en ultravioleta. ✔
- 21,4–23,3: «Lo pone lo que entrenas», casillas L–D, «cada semana.»: **«semana» se escribe a 23,2 s y a 23,4 s ya está el logo de ProTeam encima.** ✘
- **23,3–23,6 s:** fundido CRUZADO: «ProTeam» se pinta sobre la polaroid y sobre «La categoría no pone tu» (fotograma a 23,4 s). ✘ texto solapado.
- 23,5–27,1: outro2 limpio.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Historia muy buena y clara para entrenadores (de Segunda a dos Copas de Europa). Pero el primer fotograma es pared vacía: en el feed se ve un rectángulo azul oscuro durante 0,5 s. |
| Cada cosa que dice la voz se anima en su momento | 16/20 | Casi todo cae en su palabra (sello, escalera, calendario, tabla, copas, 1–0, nombres, techo). Falla el remate: «cada semana.» está en pantalla ~0,2 s antes de que entre el cierre; la frase más importante no se lee. |
| Transiciones | 9/15 | Viajes suaves por la pared. El final es brusco y sucio: sin remate quieto, sin fundido a negro y con fundido cruzado al logo encima del texto. |
| Sonido | 12/15 | Voz confiada y clara, música real suave, efectos bajos, −17 LUFS. Pero «semana» acaba a 23,28 s y «Dale» entra a 23,54 s: 0,26 s; el remate no respira. |
| Verdad y fuentes | 15/15 | Todo comprobado. |
| Estética | 8/15 | Paleta, tipografías y ultravioleta una vez, bien. Pero: logo de outro2 solapado sobre texto (suspenso automático); pie de créditos final (~22,6–23,3 s) ilegible en móvil y solo visible medio segundo; los checks de la pizarra tapan las letras L, M, X. |
| **Total** | **76/100** | Además suspende por texto solapado. |

## Correcciones para el remontaje (Marta)
1. **Final (21,4–25 s), lo principal:** que «Lo pone lo que entrenas cada semana.» quede entero y quieto al menos 1,0 s (de ~23,3 a ~24,3 s), con la cámara ya parada (el alejamiento a ×0,92 tiene que terminar antes de «semana»). Después, fundido a NEGRO de 0,5 s (nada de fundido cruzado: el logo no puede pintarse encima de la polaroid ni del texto) y outro2 desde ~24,8 s. En la mezcla, mueve el audio de outro2 y su sting a la vez: la voz del cierre debe entrar ≥ 1,0 s después de que acabe «semana» (≈24,4–24,9 s), como en Reep, Luis Enrique o McLendon r2.
2. **Gancho (0,0–0,5 s):** que el primer fotograma ya tenga «1977.» (aunque sea a mitad de entrada), sin pared vacía. Si hace falta, adelanta la animación del 1977 o recorta 0,3–0,4 s de cola de vídeo al principio sin mover la voz (la voz empieza a 0,0).
3. **Pie de créditos final:** quítalo de pantalla (los créditos ya van en el caption) o déjalo ≥ 17 px y quieto ≥ 1,5 s. Ahora es ilegible.
4. **Pizarra L–D:** que el check no tape la letra (ponlo debajo o a un lado, o que la letra quede encima a menos opacidad del check).
5. **Repo:** sube el `video_mudo.mp4` nuevo con outro2 (el que hay acaba con «Estamos terminando la app»).
6. **Cola y panel a la vez:** al subir el vídeo nuevo, cambia `files` en `publicar/cola.json` (guarda `3a37f267` en `files_old`) y el vídeo del post del panel. El caption del panel ya está corregido por Andrés; no lo vuelvas a pisar con el del guion.

Sin cambios: voz, música, efectos, fotos, datos y caption.
