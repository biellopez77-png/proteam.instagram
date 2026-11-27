#!/usr/bin/env python3
"""A-027 + M-011 (plantillas semanales de horario). Ejecutar en la raíz de proteamapp.

A-027: al editar una plantilla, `saveScheduleTemplate` borraba todas sus franjas y las
volvía a crear con ids nuevos. Como `microcycle_links.template_row_id` es ON DELETE SET NULL,
las actividades ya creadas perdían su franja y «volver al horario de la plantilla»
(`resetActivityToTemplate`) respondía «Aquesta activitat no prové de cap plantilla».
Además el borrado no comprobaba errores. Ahora se conservan los ids de las franjas que
siguen, solo se borran las quitadas (comprobando el error) y las nuevas se insertan.

M-011: el diálogo «Aplicar plantilla setmanal» decía «Encara no hi ha plantilles» mientras
cargaba, y el editor dejaba guardar una franja con la hora de fin anterior a la de inicio
(el servidor la convertía en 60 min sin avisar): ahora «Desar plantilla» se desactiva y el
campo «Fi» se marca en rojo (aria-invalid). Sin textos nuevos ni BD.
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

CHANGES = {
    "src/lib/schedule-templates.functions.ts": [
        (
            "  physical_min: z.number().int().min(0).max(240).nullable().default(30),\n});",
            "  physical_min: z.number().int().min(0).max(240).nullable().default(30),\n"
            "  /** Existing row id when editing: keeps the link of activities already created. */\n"
            "  id: uuid.optional(),\n});",
        ),
        (
            "    let id = data.id;\n\n    if (id) {",
            "    let id = data.id;\n    const known = new Set<string>();\n\n    if (id) {",
        ),
        (
            '      if (error) throw new Error(error.message);\n'
            '      await sb.from("schedule_template_rows").delete().eq("template_id", id).eq("team_id", m.team_id);\n'
            '    } else {',
            '      if (error) throw new Error(error.message);\n'
            '      // Keep the rows that still exist: activities already created remember their\n'
            '      // row (template_row_id, ON DELETE SET NULL) and lose it if it is re-created.\n'
            '      const { data: cur, error: ce } = await sb\n'
            '        .from("schedule_template_rows")\n'
            '        .select("id")\n'
            '        .eq("template_id", id)\n'
            '        .eq("team_id", m.team_id);\n'
            '      if (ce) throw new Error(ce.message);\n'
            '      for (const r of (cur ?? []) as { id: string }[]) known.add(r.id);\n'
            '      const gone = [...known].filter((rid) => !data.rows.some((r) => r.id === rid));\n'
            '      if (gone.length) {\n'
            '        const { error: de } = await sb\n'
            '          .from("schedule_template_rows")\n'
            '          .delete()\n'
            '          .in("id", gone)\n'
            '          .eq("template_id", id)\n'
            '          .eq("team_id", m.team_id);\n'
            '        if (de) throw new Error(de.message);\n'
            '      }\n'
            '    } else {',
        ),
        (
            '      const { error } = await sb.from("schedule_template_rows").insert(\n'
            '        data.rows.map((r, i) => ({\n'
            '          template_id: id,',
            '      const payload = data.rows.map((r, i) => ({\n'
            '          ...(r.id && known.has(r.id) ? { id: r.id } : {}),\n'
            '          template_id: id,',
        ),
        (
            '          sort_idx: i,\n'
            '        })) as never,\n'
            '      );\n'
            '      if (error) throw new Error(error.message);\n'
            '    }',
            '          sort_idx: i,\n'
            '        }));\n'
            '      const kept = payload.filter((p) => "id" in p);\n'
            '      const added = payload.filter((p) => !("id" in p));\n'
            '      if (kept.length) {\n'
            '        const { error } = await sb.from("schedule_template_rows").upsert(kept as never, { onConflict: "id" });\n'
            '        if (error) throw new Error(error.message);\n'
            '      }\n'
            '      if (added.length) {\n'
            '        const { error } = await sb.from("schedule_template_rows").insert(added as never);\n'
            '        if (error) throw new Error(error.message);\n'
            '      }\n'
            '    }',
        ),
    ],
    "src/components/planning/schedule-template-editor.tsx": [
        (
            "export type DraftRow = {\n  weekday: Weekday;",
            "export type DraftRow = {\n  /** Saved row id (editing an existing template). */\n  id?: string;\n  weekday: Weekday;",
        ),
        (
            '                    className={`${field} mt-1`}\n'
            '                    value={r.end_time ?? ""}',
            '                    aria-invalid={!!r.start_time && !!r.end_time && r.end_time <= r.start_time}\n'
            '                    className={`${field} mt-1 aria-[invalid=true]:border-destructive`}\n'
            '                    value={r.end_time ?? ""}',
        ),
        (
            "            disabled={pending || !name.trim()}",
            "            disabled={\n"
            "              pending ||\n"
            "              !name.trim() ||\n"
            "              rows.some((r) => !!r.start_time && !!r.end_time && r.end_time <= r.start_time)\n"
            "            }",
        ),
    ],
    "src/routes/_authenticated/coach.schedule.tsx": [
        (
            "                          ? own.map((r) => ({\n"
            "                              weekday: r.weekday as Weekday,",
            "                          ? own.map((r) => ({\n"
            "                              id: r.id,\n"
            "                              weekday: r.weekday as Weekday,",
        ),
    ],
    "src/components/planning/apply-template-dialog.tsx": [
        (
            "  const { data } = useQuery({\n    queryKey: [\"schedule-templates\"],",
            "  const { data, isLoading } = useQuery({\n    queryKey: [\"schedule-templates\"],",
        ),
        (
            "        {templates.length === 0 ? (",
            "        {isLoading ? (\n"
            "          <p className=\"text-sm text-muted-foreground\">Carregant…</p>\n"
            "        ) : templates.length === 0 ? (",
        ),
    ],
}

def main() -> int:
    texts = {}
    for rel, subs in CHANGES.items():
        p = ROOT / rel
        t = p.read_text(encoding="utf-8")
        for old, new in subs:
            n = t.count(old)
            if n != 1:
                print(f"ERROR {rel}: el fragmento aparece {n} veces:\n{old[:120]}")
                return 1
            t = t.replace(old, new)
        texts[p] = t
    for p, t in texts.items():
        p.write_text(t, encoding="utf-8")
        print("ok", p)
    return 0

if __name__ == "__main__":
    sys.exit(main())
