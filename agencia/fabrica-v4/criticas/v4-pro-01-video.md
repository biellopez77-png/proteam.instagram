# Crítica de vídeo v4-pro-01 · «Domingo, 23:40»

## Primera vuelta · **67/100 · SUSPENSO** (suspensos directos: cara de un entrenador conocido + texto cortado y pisado) → vuelve a montaje

Andrés (05) · 24/11 · criterio v4 (Biel, 24/11) · vídeo `tools/reel_v5/piezas/v4-pro-01/final.mp4` (1080×1920, 25 fps, 14,20 s, commit 9c521ca) · spec `piezas/v4-pro-01/spec.json` · concepto `agencia/fabrica-v4/conceptos/v4-pro-01.md` · fase: Problema · mié 2/12.
Método: un fotograma por segundo a 360 px de ancho (móvil) + hojas a 5 fps de 2,4 a 6,4 s y de 8,2 a 9,8 s; muestreo a 10 fps para el violeta; sonido en ventanas de 0,1 s (RMS/pico) con ffmpeg + numpy y EBU R128; licencias contra `banco/INVENTARIO.csv`.

Páginas en el vídeo: p. 01 DOMINGO 0,0–2,5 · pp. 02–03 retícula 2,5–5,8 · p. 04 RUIDO 5,8–8,3 · p. 05 frase UV 8,3–11,9 · cierre 11,9–14,2.

**Diagnóstico de fondo:** la idea es de las mejores de Problema y el montaje respira revista. Lo tumban dos cosas que se arreglan en el spec: la Fig. 4 es **Mike Montgomery** (entrenador muy conocido: Stanford, Golden State Warriors) con la cara de perfil a buen tamaño, y la retícula sigue enseñando pies cortados y pisados. Además, la mezcla no cumple la de `build.py` actual (pico −0,4 dBFS, sin caída final): parece renderizado con el motor anterior. Volver a renderizar después de los cambios.

| Criterio | Peso | Nota | Por qué |
|---|---|---|---|
| Idea editorial clara | 25 | 20 | DOMINGO 23:40 → la libreta, la mesa, la pizarra → RUIDO en la cabeza → «Todo está apuntado. *Nada está en el mismo sitio.*» Idea limpia, de entrenador, y el cierre «para el que lo apunta todo» la remata. Resta: el gancho «23:40» va en mono diminuto y no se ve; la Fig. 4 dice «La jugada, ya borrada» y lo que se ve es un señor de traje, no una pizarra borrada (la pizarra queda fuera del encuadre). |
| Legibilidad en móvil | 20 | 9 | DOMINGO se lee entero 0,0–2,4 s; RUIDO, «en la cabeza.», el pie de p. 04 (40 px), la frase y el cierre, bien. Pero: pie de la Fig. 1 y «23:40 · La semana aún no ha cerrado» ≈7 px en móvil, ilegibles (falta `capSize`); en la retícula los pies salen **cortados** («FIG. 3 — / EN LA ME» 2,6–2,8 s; «S CAMBIOS, / TA» 3,4 s; «3 — LAS NOTAS, / A MESA» 3,6 s; «4 — LA JUGADA, / ORRADA» 5,0 s) y **pisados** con doble imagen de Fig. 2 sobre Fig. 3 (3,0–3,6 s: «EN LA MES» encima de «N LA LIBRETA»); el pie de la Fig. 3 solo se lee entero ≈0,3 s (3,4–3,6) y el de la Fig. 4 llega desenfocado (3,8–4,0). Folio de p. 05 tapado por los balones claros (8,3–11,9). |
| Ritmo y sonido | 15 | 8 | Buena estructura: paneo con rampa, empuje con desenfoque a 5,4–5,8, paso de página, frase que entra 9,0–9,6 y resolución en el cierre. Pero **pico −0,4 dBFS a 5,8 s** (corte a RUIDO; −0,7 a 5,9) y −3,1 dBFS a 12,4 s (techo −6). El silencio está en 7,9–8,1 s (≈0,3 s a −51 dB), antes del cambio de página, no antes de la frase (pide 0,7 s). Acorde UV 10,0–10,4 s: de −19 a −14,9 dB (+4, pide +10). Acaba a −24 dB sin caída a −50. Integrado −17,9 LUFS. |
| Encaje de fase | 15 | 14 | Problema en estado puro: «esto me pasa a mí», sin app, sin fecha, sin precio. El domingo por la noche es exactamente el territorio 5 del calendario. |
| Identidad | 15 | 12 | Duotono, grano, Jakarta 800 / Instrument Serif / Plex Mono, folios p. 01 → pp. 02–03 → p. 04 → p. 05, créditos reales al pie, destello de DOMINGO azul y línea del cierre azul. **Un solo ultravioleta**: subrayado de «el mismo sitio.» 10,3–11,8 s. No parece plantilla. Restan: el subrayado se completa a 11,1 y queda quieto ≈0,7 s antes del paso (pide ≥1 s); «en la cabeza.» se ve fantasma sobre los balones (8,3–8,6); ningún `letras` (bien). |
| Verdad | 10 | 4 | Sin precio, sin apuntados, nada inventado. Licencias verificadas (CC BY 4.0, CC BY-SA 3.0/4.0, CC BY 2.0, DP). **Fig. 4 = `STAFF_PIZARRA_JUGADA_FOTO_001` = Mike Montgomery** (archivo de origen «Mike_Montgomery_diagramming_play.jpg»), cara reconocible 3,8–5,6 s: regla de famosos. Ojo también a `STAFF_BANQUILLO_ASISTENTES_FOTO_001` = Leon Rice (entrenador de Boise State): dentro de las letras de RUIDO no se reconoce, pasa, pero no la uséis a sangre. |
| **Total** | 100 | **67** | |

### Suspensos directos
3D: no · **texto cortado o pisado: sí** (pies de la retícula, 2,6–5,0 s) · más de un ultravioleta: no (solo 10,3–11,8 s) · datos inventados/precio/apuntados: no · **caras de famosos: sí** (Mike Montgomery, Fig. 4, 3,8–5,6 s) · fotos sin licencia: no · plantilla genérica: no.

### Marcas de tiempo
- **0,0–2,5 · p. 01** cronómetro + DOMINGO entero y legible desde el primer fotograma. Pie «Fig. 1 — El partido acabó a las doce» y «23:40 · La semana aún no ha cerrado» en mono gris diminuto: no se leen. 0,3 s: golpe −8 dBFS; 1,0 s: −6,3.
- **2,5–2,6 · encadenado** DOMINGO y el pie de la Fig. 1 fantasma bajo «FIG. 2 — LOS CAMBIOS».
- **2,6–2,8** «FIG. 3 — / EN LA ME» cortado en el borde derecho.
- **3,0–3,6 · doble imagen**: la Fig. 2 se superpone a la Fig. 3 y los pies se pisan («EN LA MES|N LA LIBRETA»); a 3,4 «S CAMBIOS, / TA» cortado a la izquierda.
- **3,4–3,6** Fig. 3 «Las notas, en la mesa» entera: solo ≈0,3 s.
- **3,8–5,2 · Fig. 4** Mike Montgomery de perfil, cara reconocible; pie desenfocado a 3,8–4,0, legible 4,2–4,8, **cortado** a 5,0 («4 — LA JUGADA, / ORRADA»).
- **5,2–5,8 · empuje** con desenfoque; **5,8 s pico −0,4 dBFS** al entrar RUIDO.
- **5,8–8,3 · p. 04** RUIDO hueco con el banquillo dentro, «en la cabeza.» y el pie a 40 px: todo legible. Silencio 7,9–8,1 (≈0,3 s).
- **8,3–8,6** «en la cabeza.» fantasma sobre los balones; folio tapado por la foto.
- **8,8–9,6** «TODO ESTÁ APUNTADO.» y *Nada está en / el mismo sitio.* entran y se leen bien.
- **10,3–11,8 · ultravioleta** subrayado de «el mismo sitio.» (completo 11,1); acorde +4 dB.
- **11,9–14,2 · cierre** «ProTeam», *para el que lo apunta todo.* desde 12,6; línea azul; −3,1 dBFS a 12,4; acaba a −24 dB.

## Correcciones concretas (para Marta, `piezas/v4-pro-01/spec.json`)
1. **p. 2 (`paginas[1]`, `reticula`), `figs[2].foto`**: quitar `STAFF_PIZARRA_JUGADA_FOTO_001` (Mike Montgomery). Mejor una pizarra sin persona reconocible y que se vea «ya borrada»; del banco: `STAFF_TRABAJO_FOTO_002` (charla con pizarra, Fabien Thouvenin, CC BY-SA 4.0) o `ENTRENADOR_TIEMPO_MUERTO_PIZARRA_FOTO_001` (CC0) **si** en el recorte no queda ninguna cara protagonista ni conocida (comprobad el archivo de Commons). No usar `STAFF_PIZARRA_TIEMPO_MUERTO_FOTO_001` (ya señalada en v4-pro-04).
2. **Volver a renderizar** con el `tools/reel_v5/motor/build.py` actual (pies que solo aparecen enteros, parada en la figura central con `labSize`, techo −6 dBFS, silencio antes de la frase, acorde UV +10 dB, caída final). Comprobar en el vídeo, no solo en la hoja: de 2,5 a 5,8 s ningún pie cortado ni pisado, ninguna doble imagen entre figuras, y cada pie legible ≥0,6 s (el de la Fig. 3 ≥0,8 s). Si con `d: 3.3` no llega, subir `paginas[1].d` a 4,0.
3. **p. 1 (`paginas[0]`, `palabra`)**: añadir `"capSize": 36` para que «23:40 · La semana aún no ha cerrado» y el pie de la Fig. 1 se lean en móvil. El 23:40 es el gancho: que se vea.
4. **p. 4 (`paginas[3]`, `frase`)**: subir `"d"` de 3,6 a 3,9 para ≥1 s de ultravioleta quieto. Revisar `pos` para que el folio no quede sobre la parte clara de los balones (p. ej. `"pos": "45% 62%"`) o bajar la foto.
5. **Sonido** (tras el nuevo render): pico ≤ −6 dBFS, también en 5,8 s (corte a RUIDO) y 12,4 s (cierre); silencio de 0,7 s justo antes de que entre «Nada está en el mismo sitio.» (≈8,8 s), no en el cambio de página; acorde UV ≈ +10 dB sobre el zumbido; caída final a −50 dB.
6. **Encadenado p. 04 → p. 05**: que «en la cabeza.» no quede fantasma sobre la foto (corte más seco o fundido a negro breve).
7. Subir `media/v4-pro-01.mp4` y `.jpg` al panel cuando apruebe.
