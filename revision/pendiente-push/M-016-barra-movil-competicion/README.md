# M-016 · Barra inferior del móvil: «Competició» sin marcar

**Qué falla (375 px, entrenador).** La barra inferior (`src/components/shell.tsx`, `CoachShell`, `COACH_MAIN.slice(0, 5)`) solo enseña Inici, Planificació, Calendari, Jugadors y Físic; Competició, Progressió y Configuració están detrás de «Més». Cuando el entrenador está en `/coach/matches` (o en un partido, progresión o ajustes) **ningún botón de la barra sale marcado** y la cabecera es lo único que dice dónde está. «Més» tampoco dice si el menú está abierto (`aria-expanded`) y el menú lateral no se cierra con Escape (ni en el entrenador ni en el jugador).

Además, a 375 px cada columna mide 56,5 px y los enlaces quitan 8 px de relleno (`px-1`): «Planificación» (52,8 px a 10 px de Plus Jakarta Sans), «Planification» (51,1) y «Planeamento» (51,7) salen cortados con «…». Sin el relleno caben (medido con Playwright y la fuente real).

**Arreglo (2 archivos, sin BD ni textos nuevos).** `aplicar.py`:
- «Més» se pinta como activo (mismo círculo azul) cuando la página actual es una de las que viven en el menú; `aria-haspopup="dialog"` y `aria-expanded`.
- Escape cierra el menú lateral (`useEscapeToClose`, entrenador y jugador).
- Enlaces de la barra con `px-0`.
- `styles.css`: la regla del círculo activo también vale para `[data-active="true"]`.

**Cómo aplicarlo.** En proteamapp: `python3 …/aplicar.py`, `bun run build`, `git diff` (solo `shell.tsx` y `styles.css`), commit en `main`, push y `deploy_project`.

**Cómo probarlo.** Móvil a 375 px → Competició desde «Més»: el botón «Més» queda marcado. Abrir «Més» y pulsar Escape (teclado) → se cierra. En castellano, «Planificación» se lee entero.

Propuesta aparte (P-018, para Biel): poner Competició en la barra y mandar Calendari a «Més», o la inversa en día de partido.
