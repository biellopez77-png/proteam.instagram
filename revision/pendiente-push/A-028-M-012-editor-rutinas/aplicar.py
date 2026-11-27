#!/usr/bin/env python3
"""A-028 + M-012: editor de rutinas (src/components/routine-editor.tsx, commit fb80d88).

A-028 (error): las fechas marcadas en el calendario de la rutina («scheduledDates») que quedan
fuera de «Data d'inici» / «Data de finalització» se guardan igual. `DateMultiPicker` solo limita
las fechas NUEVAS (minDate/maxDate); si el entrenador marca días y después acorta el periodo,
los días de fuera siguen en `scheduled_dates` y `routineDays` (`lib/routine-week.ts`) los pinta
en la semana, en Inicio y en el calendario porque no mira start_date/end_date. Arreglo: al
guardar, solo se envían (y se planifican en el ciclo) las fechas dentro del periodo. SQL 18/11:
19 rutinas, 1 con periodo, 0 afectadas (latente).

M-012 (error de uso):
 - Al borrar un ejercicio con otro desplegado, el desplegado salta a la fila siguiente
   (`openIdx` no se ajusta en `removeEx`).
 - Rutina nueva creada desde un ciclo: si «Desar» guarda la rutina pero falla planificarla en el
   ciclo (`planFn`), el editor sigue en «Nova rutina» y al volver a pulsar «Desar» se crea una
   rutina duplicada. Ahora, si falla ese segundo paso, avisa con el error y abre la rutina ya
   guardada (no se puede duplicar).
 - Botones de desplegar y eliminar ejercicio solo con icono: `aria-expanded` en el de desplegar.
Sin textos nuevos (i18n:check no cambia). 1 archivo.
Uso (en la raíz de proteamapp): python3 aplicar.py [ruta] && bun run build
"""
import pathlib, sys
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src/components/routine-editor.tsx")
s = p.read_text()
subs = [
    # M-012: openIdx sigue a su fila al borrar
    ('  function removeEx(idx: number) { setList(list.filter((_, i) => i !== idx)); }',
     '  function removeEx(idx: number) {\n'
     '    setList(list.filter((_, i) => i !== idx));\n'
     '    setOpenIdx((o) => (o === null || o < idx ? o : o === idx ? null : o - 1));\n'
     '  }'),
    # A-028: solo fechas dentro del periodo
    ('    if (list.some((e) => !e.exercise_id)) return toast.error("Selecciona un exercici de la Biblioteca en totes les files");\n'
     '    try {',
     '    if (list.some((e) => !e.exercise_id)) return toast.error("Selecciona un exercici de la Biblioteca en totes les files");\n'
     '    // The picker only limits new picks: drop days left outside a narrowed period.\n'
     '    const datesInRange = scheduledDates.filter((d) => (!startDate || d.slice(0, 10) >= startDate) && (!endDate || d.slice(0, 10) <= endDate));\n'
     '    try {'),
    ('        scheduled_dates: scheduledDates,\n        start_date: startDate || null,',
     '        scheduled_dates: datesInRange,\n        start_date: startDate || null,'),
    # M-012: no duplicar si falla planificar en el ciclo
    ('      if (!id && planLevel && planId) {\n'
     '        await planFn({ data: {\n'
     '          routine_id: res.id!,\n'
     '          level: planLevel,\n'
     '          id: planId,\n'
     '          dates: scheduledDates,\n'
     '          weekdays: [],\n'
     '          start_time: null,\n'
     '          label: name.trim() || null,\n'
     '          notes: null,\n'
     '        }});',
     '      if (!id && planLevel && planId) {\n'
     '        try {\n'
     '          await planFn({ data: {\n'
     '            routine_id: res.id!,\n'
     '            level: planLevel,\n'
     '            id: planId,\n'
     '            dates: datesInRange,\n'
     '            weekdays: [],\n'
     '            start_time: null,\n'
     '            label: name.trim() || null,\n'
     '            notes: null,\n'
     '          }});\n'
     '        } catch (e) {\n'
     '          // The routine is already saved: open it so a second «Desar» edits it instead of duplicating it.\n'
     '          toast.error(e instanceof Error ? e.message : "Error");\n'
     '          nav({ to: "/coach/routines/$id", params: { id: res.id! } });\n'
     '          return;\n'
     '        }'),
    ('<button onClick={() => setOpenIdx(open ? null : i)} className="p-1.5 rounded hover:bg-muted">',
     '<button type="button" aria-expanded={open} onClick={() => setOpenIdx(open ? null : i)} className="p-1.5 rounded hover:bg-muted">'),
]
for old, new in subs:
    if s.count(old) != 1:
        sys.exit(f"routine-editor.tsx: no aparece exactamente una vez:\n{old}")
    s = s.replace(old, new)
p.write_text(s)
print("A-028 + M-012 aplicados: 1 archivo, sin textos nuevos. Ahora: bun run build")
