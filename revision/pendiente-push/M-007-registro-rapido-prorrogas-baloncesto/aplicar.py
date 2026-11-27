#!/usr/bin/env python3
"""M-007: «Registre ràpid» de la ficha del partido (src/components/match-quick-log.tsx).
En baloncesto hay 4 cuartos + 2 prórrogas (periodCount = 6, sport-config/basketball.ts
`hasOvertime: true`) y se pintan 6 botones de periodo, pero:
  1) el periodo inicial se recorta a 4: `useState(Math.min(Math.max(defaultPeriod || 1, 1), 4))`
     → si el partido está en la prórroga, las acciones se guardan en el 4.º cuarto sin avisar;
  2) el desplegable de «Últimes accions» solo ofrece `[1, 2, 3, 4]` → una acción de prórroga
     se ve como «1a» y no se puede devolver a su prórroga.
Hoy sin datos afectados (SQL: 0 equipos de baloncesto con acciones; máx. periodo 2 en
balonmano), pero el 28 entran equipos de los 3 deportes. Arreglo: usar periodCount.
Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
"""
import pathlib, sys
p = pathlib.Path("src/components/match-quick-log.tsx")
s = p.read_text()
subs = [
    ("useState(Math.min(Math.max(defaultPeriod || 1, 1), 4));",
     "useState(Math.min(Math.max(defaultPeriod || 1, 1), periodCount));"),
    ("{[1, 2, 3, 4].map((p) => (",
     "{Array.from({ length: Math.max(periodCount, e.period) }, (_, i) => i + 1).map((p) => ("),
]
for old, new in subs:
    if s.count(old) != 1:
        sys.exit(f"match-quick-log.tsx: no aparece exactamente una vez: {old}")
    s = s.replace(old, new)
p.write_text(s)
print("M-007 aplicado: 1 archivo, sin textos nuevos. Ahora: bun run build")
