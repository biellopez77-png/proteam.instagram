# A-027 + M-011 · Plantillas semanales de horario

Turno 18/11 15:17 Madrid (auditoría de planificación). Código leído con `read_file` de Lovable (commit fb80d88).

| | Antes | Después |
|---|---|---|
| A-027 | Editar y guardar una plantilla borraba todas sus franjas y las creaba de nuevo (`schedule-templates.functions.ts`, `saveScheduleTemplate`). Las actividades ya creadas perdían su franja (`microcycle_links.template_row_id` es `ON DELETE SET NULL`) y «volver al horario de la plantilla» fallaba con «Aquesta activitat no prové de cap plantilla». El borrado no miraba errores. BD 18/11: 7 de 42 actividades de plantilla ya sin franja, todas de semanas pasadas | Se conservan los ids de las franjas que siguen (`upsert` por `id`), solo se borran las quitadas (comprobando el error) y las nuevas se insertan |
| M-011 | «Aplicar plantilla setmanal» (`apply-template-dialog.tsx`) decía «Encara no hi ha plantilles» mientras cargaba. El editor dejaba guardar «Fi» anterior a «Inici» y el servidor lo convertía en 60 min sin avisar | «Carregant…» mientras carga; «Desar plantilla» desactivado y «Fi» en rojo (`aria-invalid`) si la hora de fin no es posterior |

4 archivos, sin BD ni textos nuevos («Carregant…» ya existe). RLS: «Staff manage schedule template rows» es `ALL` (permite el `upsert`).

Aplicar en proteamapp: `python3 aplicar.py .` → `bun run build` → commit en `main` → push → `deploy_project`.
Probar: editar una plantilla ya aplicada cambiando una hora → en una semana pasada, «volver al horario de la plantilla» sigue funcionando.
