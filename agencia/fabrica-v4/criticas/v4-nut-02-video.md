# Crítica de vídeo v4-nut-02 · «Lo que pesó la semana»

## Primera vuelta · **68/100 · SUSPENSO** (suspenso directo: texto cortado y pisado) → vuelve a montaje

Andrés (05) · 24/11 · criterio v4 (Biel, 24/11) · vídeo `tools/reel_v5/piezas/v4-nut-02/final.mp4` (1080×1920, 25 fps, 14,60 s) · spec `piezas/v4-nut-02/spec.json` · concepto `agencia/fabrica-v4/conceptos/v4-nut-02.md` · fase: Nutrición · sáb 5/12.
Método: un fotograma por segundo a 360 px de ancho (móvil) + hoja a 5 fps de 4,6 a 9,6 s; muestreo a 10 fps para el violeta; sonido en ventanas de 0,1 s (RMS/pico) con ffmpeg + numpy y EBU R128; licencias contra `banco/INVENTARIO.csv`.

**Diagnóstico de fondo:** el vídeo está renderizado con el motor anterior a los cambios de esta mañana (parada en la figura central con `labSize`, pies que nunca se ven cortados, mezcla con techo −6 dBFS, silencio de 0,7 s, acorde UV +10 dB, caída final). Casi todos los fallos de legibilidad y de sonido se van con **volver a renderizar** con el `build.py` actual y tres cambios de spec.

| Criterio | Peso | Nota | Por qué |
|---|---|---|---|
| Idea editorial clara | 25 | 19 | CARGA → 7×90 = 630 → la semana → «no pesan lo mismo» es una idea limpia y útil: el entrenador se lleva una herramienta de libreta. Resta: la frase UV («Dos sesiones de 90 minutos no pesan lo mismo») no la demuestran los datos que se ven (la retícula enseña 90, 75 y 45 min, no dos sesiones de 90); y la suma de la semana, que es el título, no aparece. |
| Legibilidad en móvil | 20 | 9 | Se leen bien CARGA, «no es lo que dura.», 7×90, «= 630 de carga.», 630 y 180 en la retícula, la frase serif y el cierre. Pero en la retícula los pies se cortan y se pisan (ver marcas), el **600 solo se lee ≈0,2 s** (6,6 s) y las letras de fondo MAR/JUE/VIE aparecen cortadas («AR / E / E», «R») de 7,0 a 8,4 s. Pies de p. 01 y p. 02 («Es lo que dura por lo que pesa.», «sRPE (Foster)…») y entradilla de p. 05 en mono pequeño: ≈8 px en móvil, no se leen. |
| Ritmo y sonido | 15 | 7 | Estructura buena (paneo con rampa, desenfoque, paso de página, resolución en el cierre 12,8–13,3 s). Pero **satura**: pico **+3,5 dBFS a 0,01 s** (arranque) y **+0,7 dBFS a 2,5 s** (corte a 7×90). Silencio solo de 9,0 a 9,1 s (≈0,2 s a −50 dB) y en el cambio de página, no antes de la frase. Acorde UV de −19 a −15 dB (+4, pide +10). Acaba a −22 dB sin caída a −50. −18,0 LUFS. |
| Encaje de fase | 15 | 13 | Nutrición en su sitio: duele («no es lo que dura») y deja ver el después (medir la semana) sin enseñar la app ni hablar de fechas. Territorio 6 bien traído a la revista. Resta: el cierre «para el que mide la semana.» es correcto pero frío para nutrición. |
| Identidad | 15 | 12 | Duotono, grano, Jakarta 800 / Instrument Serif / Plex Mono, folios p. 01 → p. 02 → pp. 03–04 → p. 05, créditos reales. **Un solo ultravioleta** (subrayado de «lo mismo.», 11,0–12,5 s) y la línea del cierre es azul. No parece plantilla. Restan: el UV queda quieto solo ≈0,7 s antes del paso de página (pide ≥1 s: d = 3,2 < 3,5); 7×90 se ve fantasma detrás de la Fig. 1 en el encadenado (5,4 s); `letras` de fondo, que MOTOR.md desaconseja. |
| Verdad | 10 | 8 | sRPE de Foster, real y bien explicado (0–10, a los 30 min). Sin precio ni apuntados. Fotos con licencia verificada (DP, CC BY-SA 3.0/4.0). Restan: Fig. 1 es `ENTRENADOR_ENTRENADORA_INDICA_FOTO_001` = **Cindy Parlow Cone** (persona conocida; aquí solo se ve el brazo, no es suspenso directo, pero ya la sacamos de E02); p. 05 es una jugadora profesional de la Bundesliga (Thüringer HC) con la cara reconocible a pantalla completa 3,5 s; las tres sesiones son un ejemplo de cálculo y en pantalla parecen datos de un equipo. |
| **Total** | 100 | **68** | |

### Suspensos directos
3D: no · **texto cortado o pisado: sí** (pies de la retícula y letras de fondo, 5,6–8,6 s) · más de un ultravioleta: no (solo 11,0–12,5 s) · datos inventados/precio/apuntados: no · famosos o fotos sin licencia: no (Cindy Parlow Cone sin cara visible: cambiarla igualmente) · plantilla genérica: no.

### Marcas de tiempo
- **0,0–2,5 · p. 01** CARGA con los conos dentro, entero y legible; «no es lo que dura.» bien. Pie «Es lo que dura / por lo que pesa.» en mono diminuto: es la tesis y no se lee. **0,01 s: pico +3,5 dBFS** (satura al arrancar).
- **2,5 · corte a 7×90**: golpe a +0,7 dBFS, satura.
- **2,5–5,3 · p. 02** 7×90 y «= 630 de carga.» muy legibles. «Esfuerzo percibido × minutos» y el pie de Foster, ilegibles en móvil.
- **5,4 · encadenado**: 7×90 y «= 630» se ven fantasma a través de la Fig. 1.
- **5,6–6,2 · Fig. 1** «Martes · 90 min / RPE 7 → 630» legible; a la derecha el pie de Jueves entra cortado («JUEVES · / RPE 8 →»).
- **6,2–6,4 · pisado**: «·ARTES · 90 MIN / PE 7 → 630» encima de «JUEVES · 75 / RPE 8 → 600».
- **6,6 · Fig. 2** «Jueves · 75 min / RPE 8 → 600» limpio ≈0,2 s; no hay parada.
- **6,8–7,0 · cortado**: «5 MIN / 0» y «VIEI / RPI» en los bordes.
- **7,0–8,4 · Fig. 3** «Viernes · 45 min / RPE 4 → 180» legible; detrás, «MAR/JUE/VIE» cortado («AR / E / E», luego «R»).
- **8,4–8,6 · cortado**: «ERNES · 45 MIN / E 4 → 180», luego «45 MIN / 180» por debajo del encuadre.
- **8,8–9,2 · empuje con desenfoque** y paso a p. 05; silencio de ≈0,2 s (9,0–9,1).
- **9,2–12,5 · p. 05** jugadora en suspensión a sangre; entradilla en mono pequeño; «no pesan / lo mismo.» legible; subrayado violeta 11,0–12,5 (quieto 11,4–12,1, ≈0,7 s). Acorde +4 dB.
- **12,5–14,6 · cierre** «ProTeam / para el que mide la semana.» con línea azul; resolución 12,8–13,3 s; acaba a −22 dB.

## Correcciones concretas (para Marta, `piezas/v4-nut-02/spec.json`)
1. **Volver a renderizar** con el `tools/reel_v5/motor/build.py` actual (el de E02 segunda vuelta): parada en la figura central con `labSize`, pies que solo aparecen enteros, techo −6 dBFS, silencio de 0,7 s, acorde UV +10 dB, caída final. Comprobar después: pico ≤ −6 dBFS, también en 0,0 s y en 2,5 s.
2. **p. 3 (`paginas[2]`, `reticula`)**: quitar `"letras"`. Subir `"d"` a 4,6 para que la parada en Jueves dure ≥0,8 s. En la hoja (`build.py v4-nut-02 --still`) y en el vídeo, ningún pie cortado ni pisado de 5,4 a 9,0 s, y 630 / 600 / 180 legibles ≥0,6 s cada uno.
3. **p. 3, `figs[0].foto`**: cambiar `ENTRENADOR_ENTRENADORA_INDICA_FOTO_001` (Cindy Parlow Cone) por una foto sin persona conocida (p. ej. `OBJETO_BALON_LINEA_FOTO_001` o un plano de entrenamiento sin caras).
4. **p. 3, pies**: dejar claro que es un ejemplo: `figs[0].lab` → «Ejemplo · Martes · 90 min\nRPE 7 → 630» (o un `cap` de página «Una semana de ejemplo»).
5. **Que los datos demuestren la frase UV**: cambiar `paginas[2].figs[1].lab` a «Jueves · 90 min\nRPE 4 → 360» (90 y 90 minutos → 630 y 360: la imagen prueba «no pesan lo mismo»). En **p. 4 (`paginas[3]`, `frase`)** añadir `"preSize": 44` y subir `"d"` a 3,7 (≥1 s de UV quieto).
6. **p. 4, `foto`**: la jugadora de la Bundesliga sale con la cara reconocible a pantalla completa; cambiar por un pabellón sin caras protagonistas o por un plano de grada/pista vacía.
7. **p. 1 (`dentro`)**: añadir `"capSize": 40` para que «Es lo que dura / por lo que pesa.» se lea. **p. 2 (`cifra`)**: si el tipo admite `capSize`, 36–40; si no, acortar `cap` a «sRPE (Foster): del 0 al 10,\na los 30 min de acabar.» y pedir al motor `capSize` en `cifra`.
8. Opcional (idea): añadir al final de la retícula o en el pie de p. 4 la suma de la semana (con el cambio del punto 5: 630 + 360 + 180 = «1.170 la semana») para que el título tenga su número.
9. Subir `media/v4-nut-02.mp4` y `.jpg` al panel cuando apruebe.
