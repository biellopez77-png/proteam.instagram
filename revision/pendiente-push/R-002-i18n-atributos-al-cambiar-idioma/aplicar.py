#!/usr/bin/env python3
"""R-002 · Capa de traducción del DOM (src/lib/i18n/index.tsx): el MutationObserver
reaccionaba a sus propios cambios de atributos (title, placeholder, aria-label, alt).
Cada traducción se procesaba dos veces y, peor, el texto ya traducido pasaba a ser
el «original»: al cambiar de idioma sin recargar, esos atributos se quedaban en el
idioma anterior. Ejecutar desde la raíz de proteamapp: python3 <ruta>/aplicar.py"""
from pathlib import Path

def sub(path, pairs):
    p = Path(path); s = p.read_text()
    if "appliedAttr" in s:
        print("ya aplicado", path); return
    for old, new in pairs:
        n = s.count(old)
        assert n == 1, f"{path}: esperaba 1 coincidencia y hay {n}: {old[:70]!r}"
        s = s.replace(old, new)
    p.write_text(s); print("ok", path)

sub("src/lib/i18n/index.tsx", [
    ("const originalAttr = new WeakMap<Element, Record<string, string>>();\n",
     "const originalAttr = new WeakMap<Element, Record<string, string>>();\n"
     "/** Attribute values written by this layer, to ignore our own mutation records. */\n"
     "const appliedAttr = new WeakMap<Element, Record<string, string>>();\n"),
    ("    const next = lookup(dict, trimmed) ?? source;\n"
     "    if (el.getAttribute(a) !== next) el.setAttribute(a, next);\n",
     "    const next = lookup(dict, trimmed) ?? source;\n"
     "    let applied = appliedAttr.get(el);\n"
     "    if (!applied) {\n"
     "      applied = {};\n"
     "      appliedAttr.set(el, applied);\n"
     "    }\n"
     "    applied[a] = next;\n"
     "    if (el.getAttribute(a) !== next) el.setAttribute(a, next);\n"),
    ("          const store = originalAttr.get(el);\n"
     "          if (store && r.attributeName) delete store[r.attributeName];\n",
     "          const name = r.attributeName;\n"
     "          // Our own setAttribute also fires a record: keep the original source text.\n"
     "          if (name && el.getAttribute(name) === appliedAttr.get(el)?.[name]) continue;\n"
     "          const store = originalAttr.get(el);\n"
     "          if (store && name) delete store[name];\n"),
])
