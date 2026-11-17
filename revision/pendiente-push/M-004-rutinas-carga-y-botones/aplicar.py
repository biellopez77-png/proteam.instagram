#!/usr/bin/env python3
"""M-004 · Biblioteca de rutinas (src/routes/_authenticated/coach.routines.index.tsx).

1. Mientras carga ya no dice «Encara no has creat cap rutina» (estado vacío falso):
   muestra tres tarjetas grises con aria-busy.
2. Botones «Duplicar» y «Eliminar»: aria-label (antes solo title) y 44 px de zona táctil;
   «Editar» con min-h-11.
Sin textos nuevos (no toca diccionarios). Uso: python3 aplicar.py [raíz de proteamapp]
"""
import pathlib, sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
REL = "src/routes/_authenticated/coach.routines.index.tsx"
EDITS = [
    ('const { data: routines = [] } = useQuery({ queryKey: ["routines"], queryFn: () => listFn() });',
     'const { data: routines = [], isLoading } = useQuery({ queryKey: ["routines"], queryFn: () => listFn() });'),
    ('      {routines.length === 0 ? (\n',
     '      {isLoading ? (\n'
     '        <div aria-busy="true" className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">\n'
     '          {[0, 1, 2].map((i) => <div key={i} className="h-48 animate-pulse rounded-xl border border-border bg-card" />)}\n'
     '        </div>\n'
     '      ) : routines.length === 0 ? (\n'),
    ('className="flex-1 inline-flex items-center justify-center gap-1 text-xs bg-muted hover:bg-foreground hover:text-background rounded-lg py-2 transition"',
     'className="flex-1 inline-flex min-h-11 items-center justify-center gap-1 text-xs bg-muted hover:bg-foreground hover:text-background rounded-lg py-2 transition"'),
    ('<button onClick={() => duplicate(r.id)} className="p-2 rounded-lg hover:bg-muted" title="Duplicar">',
     '<button type="button" onClick={() => duplicate(r.id)} className="inline-flex h-11 w-11 items-center justify-center rounded-lg hover:bg-muted" title="Duplicar" aria-label="Duplicar">'),
    ('<button onClick={() => remove(r.id)} className="p-2 rounded-lg hover:bg-destructive/10 text-destructive" title="Eliminar">',
     '<button type="button" onClick={() => remove(r.id)} className="inline-flex h-11 w-11 items-center justify-center rounded-lg hover:bg-destructive/10 text-destructive" title="Eliminar" aria-label="Eliminar">'),
]
path = ROOT / REL
text = path.read_text(encoding="utf-8")
for old, new in EDITS:
    n = text.count(old)
    if n != 1:
        sys.exit(f"{REL}: el texto aparece {n} veces (se esperaba 1):\n{old[:120]}")
    text = text.replace(old, new)
path.write_text(text, encoding="utf-8")
print("M-004 aplicado")
