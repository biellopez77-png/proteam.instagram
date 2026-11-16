# SKILL · Video Retention Analysis (06 Performance & Learning)
**Para qué:** interpretar retención, saltos y tiempo de reproducción cruzándolos con lo que se ve en cada segundo del Reel.

## Herramientas y límite
Windsor: `media_reel_avg_watch_time` y `media_reel_skip_rate` (saltos en 3 s). **No hay curva segundo a segundo** por la API: solo existe si Biel aporta una captura de las estadísticas de Instagram; entonces se transcribe a `intel/videos/<id>/retencion.json` con la nota «leída de captura, aproximada». `intel/videos/<id>/` da la línea de tiempo creativa.

## Procedimiento
1. **Tres números por Reel:** % de saltos en 3 s · tiempo medio en segundos · proporción tiempo medio / duración.
2. **Sitúa el tiempo medio sobre la línea de tiempo** del vídeo (`informe.md`, `transcripcion.json`): ¿qué plano, qué frase y qué texto había en ese segundo?, ¿qué pasa justo antes? Eso es una **pista**, no una causa.
3. **Lectura del primer tramo** (saltos en 3 s): describe con las láminas qué se ve en 0,0 · 0,5 · 1,0 · 2,0 · 3,0 s y cuándo está completo el hook.
4. **Clasifica el patrón:**
   - Saltos altos (> 50 %) y media baja → problema de apertura.
   - Saltos contenidos y media baja → se cae el desarrollo; mira el tramo entre 3 s y el tiempo medio (tramos sin movimiento, densidad de voz sin cambio visual).
   - Media alta y pocos guardados o compartidos → entretiene pero no deja nada.
   - Media cercana a la duración → revisar si el final sostiene o es corto de más.
5. **Con curva aportada:** marca cada caída > 5 puntos en 1 s con su segundo y mira ese tramo en modo `window`.
6. **Formula hipótesis comprobables:** «Si el tiempo medio (6,0 s) cae en el plano fijo 00:04–00:07, acortarlo a 1,5 s debería subir la media». Pasa a la tabla de experimentos; no es un hecho hasta que se pruebe.
7. **Compara por proporción**, entre Reels de duración parecida (±5 s).

## Ejemplo con datos reales
u01: 58,5 % de saltos en 3 s y 6,0 s de 30,7 s (19 %). Patrón: apertura (abría en negro con texto pequeño). Hipótesis E1: cara reconocible y texto grande en el fotograma 0. u04 la aplica (verificado en la lámina detalle_001); su dato se lee a las 24–48 h.

## Control
¿He dicho «pista» o «hipótesis» donde no hay prueba? ¿Tengo curva real o solo media? ¿He mirado el segundo señalado en las láminas?
