#!/usr/bin/env python3
"""M-008: convocatoria en la ficha del partido, pestaña «Previa»
(src/routes/_authenticated/coach.matches.$id.tsx). En el móvil los botones «Convocar» y
«Titular» de cada jugador miden ~22 px de alto (`text-[10px] px-2 py-1`) y «Convocar tothom»
/ «Buidar» ~26 px (`py-1`): con 14-16 jugadores y prisa antes del partido es fácil tocar el
de al lado. Ya llevan aria-pressed. Arreglo: mínimo 44 px de alto (min-h-11) y texto de 11 px;
la fila del jugador sigue cabiendo a 375 px (nombre con truncate). Sin textos nuevos.
Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
"""
import pathlib, sys
p = pathlib.Path("src/routes/_authenticated/coach.matches.$id.tsx")
s = p.read_text()
subs = [
    ('className={`shrink-0 text-[10px] px-2 py-1 rounded-lg border ${on ?',
     'className={`shrink-0 min-h-11 text-[11px] px-2.5 rounded-lg border ${on ?'),
    ('className={`shrink-0 text-[10px] px-2 py-1 rounded-lg border ${st ?',
     'className={`shrink-0 min-h-11 text-[11px] px-2.5 rounded-lg border ${st ?'),
    ('className="rounded-lg border border-border px-2.5 py-1 text-[11px] font-medium">',
     'className="min-h-11 rounded-lg border border-border px-3 text-[11px] font-medium">'),
    ('className="rounded-lg border border-border px-2.5 py-1 text-[11px] font-medium text-muted-foreground">',
     'className="min-h-11 rounded-lg border border-border px-3 text-[11px] font-medium text-muted-foreground">'),
]
for old, new in subs:
    if s.count(old) != 1:
        sys.exit(f"coach.matches.$id.tsx: no aparece exactamente una vez: {old}")
    s = s.replace(old, new)
p.write_text(s)
print("M-008 aplicado: 1 archivo, sin textos nuevos. Ahora: bun run build")
