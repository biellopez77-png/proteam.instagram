#!/usr/bin/env python3
"""M-022 (20/11, turno 15:17 Madrid) — alta y «Crear equipo» sin zoom en el iPhone (2 archivos, sin BD).

En el iPhone, Safari amplía la página al tocar un campo con letra de menos de 16 px. Los campos
del panel de alta/inicio de sesión (`auth-overlay.tsx`, `Field`) y de «Crear equip» /
«Canjear código» (`onboarding.tsx`, `Field`) usan `text-sm` (14 px): al tocar «Nom» la página
se amplía, el panel queda cortado y hay que pellizcar para ver «Crear compte». El `Input` de
shadcn ya lo evita con `text-base md:text-sm`; aquí se hace igual (`text-base sm:text-sm`):
16 px en el móvil y el mismo aspecto que hoy desde 640 px.
Además «Tornar» en los pasos de deporte y modalitat medía ~28 px de alto (`py-1`): pasa a 44 px
(`min-h-11`), como ya hace M-010 en el paso «Crear equip».

Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
Compatible con M-009/M-010, L-001 y L-007 (no tocan estas líneas).
"""
import pathlib, sys

CHANGES = {
    "src/components/auth-overlay.tsx": [
        ('className="mt-1 w-full rounded-lg border border-input bg-card px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring/40" />',
         'className="mt-1 w-full rounded-lg border border-input bg-card px-3 py-2 text-base focus:outline-none focus:ring-2 focus:ring-ring/40 sm:text-sm" />', 1),
    ],
    "src/routes/_authenticated/onboarding.tsx": [
        ('className="mt-1 w-full rounded-lg border border-border px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring/40" />',
         'className="mt-1 w-full rounded-lg border border-border px-3 py-2 text-base focus:outline-none focus:ring-2 focus:ring-ring/40 sm:text-sm" />', 1),
        ('<button type="button" onClick={onBack} className="w-full text-sm text-muted-foreground py-1">Tornar</button>\n    </div>',
         '<button type="button" onClick={onBack} className="min-h-11 w-full text-sm text-muted-foreground py-1">Tornar</button>\n    </div>', 2),
    ],
}

for path, repl in CHANGES.items():
    p = pathlib.Path(path)
    s = p.read_text(encoding="utf-8")
    for old, new, n in repl:
        found = s.count(old)
        if found != n:
            sys.exit(f"{path}: se esperaban {n} coincidencias y hay {found}: {old[:70]}…")
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")
    print("ok", path)
