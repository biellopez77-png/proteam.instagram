#!/usr/bin/env python3
"""M-016 · Barra inferior del móvil (entrenador): «Més» se marca cuando la página
actual no está en la barra (Competició, Progressió, Configuració), dice si el menú
está abierto, Escape cierra el menú lateral y las etiquetas usan todo el ancho
de la columna. Ejecutar desde la raíz de proteamapp: python3 <ruta>/aplicar.py"""
from pathlib import Path

def sub(path, pairs):
    p = Path(path); s = p.read_text()
    for old, new in pairs:
        n = s.count(old)
        assert n == 1, f"{path}: esperaba 1 coincidencia y hay {n}: {old[:70]!r}"
        s = s.replace(old, new)
    p.write_text(s); print("ok", path)

sub("src/components/shell.tsx", [
    ('import { useState } from "react";',
     'import { useEffect, useState } from "react";'),
    ('const exactActive = { exact: true } as const;\n',
     'const exactActive = { exact: true } as const;\n\n'
     '/** Escape closes the mobile navigation drawer (keyboard and switch users). */\n'
     'function useEscapeToClose(open: boolean, setOpen: (open: boolean) => void) {\n'
     '  useEffect(() => {\n'
     '    if (!open) return;\n'
     '    const onKey = (e: KeyboardEvent) => { if (e.key === "Escape") setOpen(false); };\n'
     '    window.addEventListener("keydown", onKey);\n'
     '    return () => window.removeEventListener("keydown", onKey);\n'
     '  }, [open, setOpen]);\n'
     '}\n'),
    ('  const [open, setOpen] = useState(false);\n  const pathname = useRouterState',
     '  const [open, setOpen] = useState(false);\n  useEscapeToClose(open, setOpen);\n  const pathname = useRouterState'),
    ('  const [open, setOpen] = useState(false);\n  const [collapsed, setCollapsed] = useState(false);',
     '  const [open, setOpen] = useState(false);\n  useEscapeToClose(open, setOpen);\n  const [collapsed, setCollapsed] = useState(false);'),
    ('  const activeTab = COACH_TABS.find((t) => isTabActive(t, pathname));\n',
     '  const activeTab = COACH_TABS.find((t) => isTabActive(t, pathname));\n'
     '  // Tabs that do not fit in the mobile bar live behind «Més»: highlight it so the coach still sees where they are.\n'
     '  const inMore = !!activeTab && !COACH_MAIN.slice(0, 5).includes(activeTab);\n'),
    ('className={`flex min-w-0 flex-col items-center gap-1 px-1 py-2 text-[10px] ${active ? "text-primary" : "text-muted-foreground"}`}',
     'className={`flex min-w-0 flex-col items-center gap-1 px-0 py-2 text-[10px] ${active ? "text-primary" : "text-muted-foreground"}`}'),
    ('<button type="button" onClick={() => setOpen(true)} className="flex min-w-0 flex-col items-center gap-1 px-1 py-2 text-[10px] text-muted-foreground"><MoreHorizontal className="h-5 w-5" aria-hidden="true" /><span>{translate("Més")}</span></button>',
     '<button type="button" onClick={() => setOpen(true)} aria-haspopup="dialog" aria-expanded={open} data-active={inMore ? "true" : undefined} className={`flex min-w-0 flex-col items-center gap-1 px-0 py-2 text-[10px] ${inMore ? "text-primary" : "text-muted-foreground"}`}><MoreHorizontal className="h-5 w-5" aria-hidden="true" /><span className="truncate">{translate("Més")}</span></button>'),
])

sub("src/styles.css", [
    ('.mobile-bottom-nav [aria-current="page"] { color: var(--foreground); }',
     '.mobile-bottom-nav [aria-current="page"], .mobile-bottom-nav [data-active="true"] { color: var(--foreground); }'),
    ('.mobile-bottom-nav [aria-current="page"] svg {',
     '.mobile-bottom-nav [aria-current="page"] svg,\n.mobile-bottom-nav [data-active="true"] svg {'),
])
