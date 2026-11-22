# A-041 — Inicio: «N jugadores tienen el test de … pendiente de revisión» con ejercicios de rutina

Turno 20/11 13:17 Madrid (auditoría: jugadores, tests y carga RPE). Código leído con `read_file` de Lovable, commit 488db5e.

**Qué pasa.** `src/components/physical/review-alert.tsx` (líneas 20-21) recorre todos los grupos de `groupMarks`, también los ejercicios de rutina (`source: "routine"`, `physical-marks.functions.ts` `loadMarks` → `routineExerciseMarks`), y les aplica la revisión por defecto de 30 días (`DEFAULT_REVIEW_DAYS`). Resultado en el equipo real (SELECT de hoy): 303 de 303 pares jugador-ejercicio de rutina tienen la última marca hace más de 30 días, ninguno tiene frecuencia propia (`physical_review_settings` con `rutina:%` = 0), y el aviso de Inicio enseña siempre «10 jugadores tienen el test de Mobilitat de tronc pendiente de revisión», «…de Abducció en quadrupèdia…», «…d'Elevació de glutis…»: ejercicios de movilidad que no son tests ni se «revisan».

**Arreglo (1 archivo, 1 línea).** Los ejercicios de rutina solo cuentan para el aviso si el entrenador les ha puesto una frecuencia en Evolución; tests, valoraciones y 4RM siguen igual. La pantalla Evolución no cambia.

**Aplicar.** En proteamapp: `git apply cambio.patch`, `bun run build`, commit en `main`, push y `deploy_project`.
