# M-026 — Panel de detalle de un ciclo: «Duplicar» que no hace nada y fechas al revés

**Qué pasa hoy (commit 488db5e):** el panel lateral de un macro/meso/microciclo enseña siempre «Duplicar», pero cada página solo sabe duplicar un nivel. Planificació › Setmanes › ⋯ de un mesocicle › Editar › Duplicar: no pasa nada. Igual con el macro desde su página, el meso desde su página y la semana desde «Detall complet». Además «Desar canvis» deja enviar una fecha de fin anterior a la de inicio y el error llega del servidor.

**Qué cambia:**
- `detail-drawer.tsx`: prop nueva `duplicateLevels`; el botón solo sale en esos niveles. Aviso bajo las fechas y botón «Desar canvis» desactivado si fin < inicio (`aria-invalid`).
- `coach.planning.index.tsx`: duplica macro **y** meso (usa el `duplicateMeso` que ya existe en la página).
- `coach.planning.macro.$id.tsx`: `duplicateLevels={["meso"]}`. `coach.planning.meso.$id.tsx`: `duplicateLevels={["micro"]}`. `micro.$id`: sin cambios (el botón deja de salir).

Sin textos nuevos (el aviso es la clave «La data de fi és anterior a la d'inici.», ya en los 7 diccionarios, línea 2402). Sin BD.

**Aplicar:** en la raíz de proteamapp, `python3 aplicar.py && bun run build`. El script aborta sin escribir nada si algún fragmento no aparece exactamente una vez.

**Probar:** Planificació › Setmanes › ⋯ › Editar en un mesocicle › Duplicar → aparece «(còpia)». En «Detall complet» de una semana › editar → no hay «Duplicar». Poner «Fi» antes de «Inici» → aviso rojo y «Desar canvis» gris.
