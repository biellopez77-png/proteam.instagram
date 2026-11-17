#!/usr/bin/env python3
"""M-005: en «Afegir jugador» (src/components/team/add-player-form.tsx) el selector
«Només perfil esportiu (sense accés)» / «Jugador amb usuari» no dice al lector de pantalla
cuál está elegido (sin aria-pressed) y sus botones miden ~32 px de alto (py-2 + text-xs),
por debajo de 44 px: en el móvil, con prisa, es fácil tocar el otro y crear al jugador
sin el modo que se quería. Sin textos nuevos ni cambios de función.
Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
"""
import pathlib, sys
p = pathlib.Path("src/components/team/add-player-form.tsx")
s = p.read_text()
old = '''              onClick={() => setMode(k)}
              className={`flex-1 py-2 text-xs rounded-md transition ${'''
new = '''              onClick={() => setMode(k)}
              aria-pressed={mode === k}
              className={`flex-1 min-h-11 py-2 text-xs rounded-md transition ${'''
if s.count(old) != 1:
    sys.exit("add-player-form.tsx: el fragmento no aparece exactamente una vez")
p.write_text(s.replace(old, new))
print("M-005 aplicado: 1 archivo. Ahora: bun run build")
