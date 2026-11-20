#!/usr/bin/env python3
"""M-026 — Panel de detalle de un ciclo (detail-drawer.tsx).

1. «Duplicar» solo aparece en los niveles que la página sabe duplicar. Antes se
   veía siempre y en varios casos no hacía nada (Planificación > Setmanes >
   ⋯ > Editar un mesocicle > Duplicar; el macro desde su página; el meso desde
   su página; la semana desde «Detall complet»).
   En Planificación (índice) se añade el duplicado del mesocicle, que ya existía
   en la misma página (`duplicateMeso`).
2. «Desar canvis» se desactiva si la fecha de fin es anterior a la de inicio y
   se avisa bajo las fechas (texto ya traducido en los 7 idiomas, línea 2402
   de los diccionarios). Antes se enviaba y volvía un error del servidor.

Uso (en la raíz de proteamapp):  python3 aplicar.py  &&  bun run build
Sin textos nuevos. 4 archivos, sin BD.
"""
import pathlib, sys

R = "src/routes/_authenticated/"
EDITS = {
  "src/components/planning/detail-drawer.tsx": [
    ("  onClose, onSelect, onSaveMacro, onSaveMeso, onSaveMicro, onDelete, onDuplicate,\n}: {",
     "  onClose, onSelect, onSaveMacro, onSaveMeso, onSaveMicro, onDelete, onDuplicate, duplicateLevels = [],\n}: {"),
    ("  onDuplicate: (s: Selection) => void;\n}) {",
     "  onDuplicate: (s: Selection) => void;\n"
     "  /** Levels this page really duplicates; the button is hidden for the rest. */\n"
     "  duplicateLevels?: Selection[\"level\"][];\n}) {"),
    ("  const pct = progressPct(current.start_date, current.end_date);\n",
     "  const pct = progressPct(current.start_date, current.end_date);\n"
     "  const datesInvalid = !!current.start_date && !!current.end_date && current.end_date < current.start_date;\n"),
    ('<input id="d-end" type="date" disabled={!isStaff} className={`${field} mt-1`} value={current.end_date}',
     '<input id="d-end" type="date" disabled={!isStaff} className={`${field} mt-1`} value={current.end_date}\n'
     '                aria-invalid={datesInvalid || undefined} aria-describedby={datesInvalid ? "d-dates-error" : undefined}'),
    ("                }} />\n            </div>\n          </div>\n\n          {draftMacro && (",
     "                }} />\n            </div>\n          </div>\n"
     "          {datesInvalid && (\n"
     "            <p id=\"d-dates-error\" role=\"alert\" className=\"-mt-3 text-xs text-destructive\">La data de fi és anterior a la d'inici.</p>\n"
     "          )}\n\n          {draftMacro && ("),
    ("<button onClick={save} disabled={saving || !current.name.trim()}",
     "<button onClick={save} disabled={saving || !current.name.trim() || datesInvalid}"),
    ("              <button onClick={() => onDuplicate(selection)}\n"
     "                className=\"inline-flex items-center gap-1.5 rounded-xl border border-border px-3 py-2 text-sm\">\n"
     "                <Copy className=\"h-3.5 w-3.5\" aria-hidden=\"true\" />Duplicar\n"
     "              </button>\n",
     "              {duplicateLevels.includes(selection.level) && (\n"
     "                <button onClick={() => onDuplicate(selection)}\n"
     "                  className=\"inline-flex items-center gap-1.5 rounded-xl border border-border px-3 py-2 text-sm\">\n"
     "                  <Copy className=\"h-3.5 w-3.5\" aria-hidden=\"true\" />Duplicar\n"
     "                </button>\n"
     "              )}\n"),
  ],
  R + "coach.planning.index.tsx": [
    ('onDelete={confirmDelete} onDuplicate={(s) => { if (s.level === "macro") void duplicateMacro(s.id); }} />',
     'onDelete={confirmDelete} duplicateLevels={["macro", "meso"]}\n'
     '          onDuplicate={(s) => {\n'
     '            if (s.level === "macro") void duplicateMacro(s.id);\n'
     '            else if (s.level === "meso") { const me = allMesos.find((m) => m.id === s.id); if (me) void duplicateMeso(me); }\n'
     '          }} />'),
  ],
  R + "coach.planning.macro.$id.tsx": [
    ('onDuplicate={(s) => { const me = mesos.find((m) => m.id === s.id); if (s.level === "meso" && me) void duplicateMeso(me); }} />',
     'duplicateLevels={["meso"]}\n'
     '          onDuplicate={(s) => { const me = mesos.find((m) => m.id === s.id); if (s.level === "meso" && me) void duplicateMeso(me); }} />'),
  ],
  R + "coach.planning.meso.$id.tsx": [
    ('onDuplicate={(s) => { const mi = micros.find((m) => m.id === s.id); if (s.level === "micro" && mi) void duplicateMicro(mi); }} />',
     'duplicateLevels={["micro"]}\n'
     '          onDuplicate={(s) => { const mi = micros.find((m) => m.id === s.id); if (s.level === "micro" && mi) void duplicateMicro(mi); }} />'),
  ],
}

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
out = {}
for rel, edits in EDITS.items():
    p = root / rel
    s = p.read_text()
    for old, new in edits:
        n = s.count(old)
        if n != 1:
            sys.exit(f"ABORTO: {rel}: fragmento encontrado {n} veces:\n{old[:120]}")
        s = s.replace(old, new)
    out[p] = s
for p, s in out.items():
    p.write_text(s)
    print("ok", p)
