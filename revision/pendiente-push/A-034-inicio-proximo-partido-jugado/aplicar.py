#!/usr/bin/env python3
"""A-034 (mejora continua, registro e inicio del entrenador, 20/11 8:17 Madrid).

Error: en el Inicio del entrenador, la tarjeta «Proper partit» (`assistant-home.tsx`,
fila 3) toma `context.nextMatch` de `getCoachPriorities`
(`src/lib/assistant.functions.ts`, `const nextMatch = matches.find((x) => x.match_date >= today)`).
No mira el estado: el día de partido, cuando el partido ya está jugado
(`status = 'played'`, 14 de 18 partidos en BD), el Inicio sigue diciendo
«Proper partit: <rival que acabas de jugar>» con el botón «Preparar partit»
hasta medianoche, y el partido de verdad siguiente no aparece. El resto del
mismo archivo ya excluye los jugados (bloque 3: `v.status !== "played"`).
`nextMatch` también decide si se avisa de lesiones (`upcoming`), que con este
fallo se activaba por un partido ya jugado.

Arreglo (1 archivo, 1 línea, sin BD ni textos): excluir `played` en `nextMatch`.

Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
src = root / "src/lib/assistant.functions.ts"
code = src.read_text(encoding="utf-8")
old = '    const nextMatch = matches.find((x) => x.match_date >= today) ?? null;'
new = '    const nextMatch = matches.find((x) => x.status !== "played" && x.match_date >= today) ?? null;'
if code.count(old) != 1:
    sys.exit("assistant.functions.ts ha cambiado (no encuentro la línea de nextMatch); revisar a mano")
src.write_text(code.replace(old, new), encoding="utf-8")
print("assistant.functions.ts: «Proper partit» ya no muestra un partido jugado")
