#!/usr/bin/env python3
"""Aplica el apartado «Análisis» del admin en una copia de proteamapp.

Uso (desde la raíz de proteamapp):
    python3 <ruta>/T-admin-analisis/aplicar.py
    bun run build && bunx vitest run src/lib/admin-analytics.test.ts

Hace tres cosas y para con error si algo no cuadra (no deja nada a medias en admin.tsx):
1. Copia los archivos nuevos de `archivos/` (no pisa archivos que ya existan).
2. Cambia `src/routes/_authenticated/admin.tsx`: pestaña «Anàlisi» y su sección.
3. Añade las claves nuevas a los 7 diccionarios (solo las que falten).
"""
import json
import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path.cwd()
if not (ROOT / "src/routes/_authenticated/admin.tsx").exists():
    sys.exit("Ejecuta el script desde la raíz de proteamapp.")

# 1. Archivos nuevos
for src in (HERE / "archivos").rglob("*"):
    if src.is_file():
        dst = ROOT / src.relative_to(HERE / "archivos")
        if dst.exists():
            sys.exit(f"Ya existe {dst}: revisa a mano antes de seguir.")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print("nuevo:", dst.relative_to(ROOT))

# 2. admin.tsx
admin = ROOT / "src/routes/_authenticated/admin.tsx"
text = admin.read_text(encoding="utf-8")
CAMBIOS = [
    ('Copy, Ban, Lock, UserCog, Mail, Save } from "lucide-react";',
     'Copy, Ban, Lock, UserCog, Mail, Save, ChartColumn } from "lucide-react";'),
    ('import { Button } from "@/components/ui/button";\n',
     'import { Button } from "@/components/ui/button";\nimport { AnalyticsSection } from "@/components/admin/analytics-section";\n'),
    ('useState<"accounts" | "teams" | "codes" | "security">("accounts")',
     'useState<"analytics" | "accounts" | "teams" | "codes" | "security">("accounts")'),
    ('<nav className="flex gap-2" aria-label="Seccions d\'administració">\n',
     '<nav className="flex flex-wrap gap-2" aria-label="Seccions d\'administració">\n'
     '        <Button variant={tab === "analytics" ? "default" : "outline"} aria-pressed={tab === "analytics"} onClick={() => setTab("analytics")}><ChartColumn /> Anàlisi</Button>\n'),
    ('{tab === "accounts" ? <AccountsSection',
     '{tab === "analytics" ? <AnalyticsSection /> : tab === "accounts" ? <AccountsSection'),
]
for old, new in CAMBIOS:
    n = text.count(old)
    if n != 1:
        sys.exit(f"admin.tsx: esperaba 1 coincidencia y hay {n} de:\n{old}")
    text = text.replace(old, new)
admin.write_text(text, encoding="utf-8")
print("cambiado: src/routes/_authenticated/admin.tsx")

# 3. Diccionarios
claves = json.loads((HERE / "i18n-claves.json").read_text(encoding="utf-8"))
for lang, entries in claves.items():
    path = ROOT / f"src/lib/i18n/dict/{lang}.json"
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    nuevas = {k: v for k, v in entries.items() if k not in data}
    if not nuevas:
        print(f"{lang}: sin claves nuevas")
        continue
    m = re.match(r"\{\n([ \t]+)\"", raw)
    indent = m.group(1) if m else "  "
    # Inserta antes de la llave final sin reformatear el resto del archivo.
    body = raw.rstrip()
    if not body.endswith("}"):
        sys.exit(f"{path}: formato inesperado")
    lines = ",\n".join(f"{indent}{json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}" for k, v in nuevas.items())
    head = body[:-1].rstrip()
    sep = "," if not head.endswith("{") else ""
    out = f"{head}{sep}\n{lines}\n}}" + ("\n" if raw.endswith("\n") else "")
    json.loads(out)  # comprobación
    path.write_text(out, encoding="utf-8")
    print(f"{lang}: {len(nuevas)} claves nuevas")

print("\nListo. Ahora: bun run build (i18n:check + vite build) y bunx vitest run src/lib/admin-analytics.test.ts")
