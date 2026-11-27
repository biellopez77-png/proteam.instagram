# SKILL · Creative Learning System (06 Performance & Learning)
**Para qué:** que cada resultado y cada crítica acaben en un cambio concreto que los demás aplican, o en un experimento.

## Herramientas
`agencia/APRENDIZAJES.md` (lo leen todos antes de crear), `agencia/aprendizaje/` (fichas), `agencia/criticas/`, oficina (`learnings`, `tasks`, `meta/office.winner`), hoja de Plan y Análisis.

## Ciclo
1. **Recoger** (diario): métricas 24/48 h, críticas de 05, correcciones de Biel en «Contenido», respuestas a Stories, análisis de `intel/`.
2. **Ficha de la pieza** (11 campos del agente) en `agencia/aprendizaje/AAAA-MM-DD-<id>.md`.
3. **Clasificar las críticas de 05:** confirmada (los datos o una segunda pieza la respaldan) · probable · subjetiva · descartada. Y al revés: **lo que la auditoría no vio** y los datos sí (se añade a la lista de comprobación de 05).
4. **Convertir en aprendizaje**, con nivel: hecho (con cifra y pieza) · interpretación · hipótesis · recomendación.
5. **Decidir el destino de cada aprendizaje:**
   - Recomendación firme → instrucción para un agente concreto, redactada como acción comprobable («02: el vídeo acaba ≤ 0,8 s después de la última palabra») y añadida a los bloqueantes o listas de control si procede.
   - Hipótesis → experimento: una variable, piezas, métrica, fecha de lectura.
   - Error repetido (≥ 2 veces) → entra en el **registro de errores** con su comprobación preventiva.
6. **Publicar:** reescribir `APRENDIZAJES.md` (reglas de Biel · hechos · recomendaciones vigentes · experimentos · clasificación de críticas · registro de errores · pendiente de comprobar). Máximo 12 recomendaciones vigentes: si entra una, se revisa cuál sale.
7. **Repartir:** una tarea por agente con «desde mañana haces distinto: …»; aprendizajes en la oficina como `hecho` o `hipotesis` con `evidence`. Las reglas (`regla`) solo las pone Biel.
8. **Cerrar el ciclo:** en la siguiente lectura, comprobar si la instrucción se aplicó (mirando la pieza y su análisis) y qué pasó. Recomendación que no mejora nada en tres lecturas, se retira.

## Formato de una recomendación
`Problema · evidencia (pieza, cifra, lámina) · cambio · quién · cómo se comprueba · cuándo se revisa`.

## Ejemplo real
Problema: cola de 1,6 s sin voz al final de u04 (voz 00:23,70; vídeo 00:25,30; medido). Cambio: 02 termina ≤ 0,8 s tras la última palabra. Comprobación: `transcripcion.json` frente a duración en el análisis de cada Reel. Revisión: tras tres Reels, mirar si sube la proporción de retención [hipótesis].

## Control
¿Cada aprendizaje tiene nivel y evidencia? ¿Cada recomendación tiene dueño y comprobación? ¿He contradicho una regla de Biel? (No se puede: se le propone.)
