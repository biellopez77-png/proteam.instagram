# A-030 + M-014 · Informe PDF de tests físicos

Aplicar desde la raíz de proteamapp: `python3 <ruta>/aplicar.py .` y después `bun run build`.

| Antes | Después |
|---|---|
| El PDF de tests cuenta a los entrenadores en «Plantilla» y «Sense marca»; el individual les da una página vacía | Solo jugadores, igual que la pantalla |
| Un test «menos es mejor» hecho sin programarlo (p. ej. 5-10-5 Shuttle) se ordena como «más es mejor» | Dirección del catálogo y, si hay, de la asignación |
| De 00:00 a 01:00/02:00 el test de ayer sigue en «Propers i d'avui» y en «Tests programats» del PDF | «Hoy» en hora local (`todayISO`) |
| Fecha de la tarjeta leída en UTC | Fecha local |

Archivos: `src/routes/_authenticated/coach.tests.tsx`, `src/lib/reports/tests-report.ts`. Sin BD.
