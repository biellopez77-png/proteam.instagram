#!/usr/bin/env python3
"""M-006: en el directo (src/routes/_authenticated/coach.matches.live.$id.tsx, línea 918
del commit 578c7aa) el botón grande del reloj lleva `data-i18n-skip` (línea 914), así que la
capa de traducción del DOM (src/lib/i18n/index.tsx, SKIP_SELECTOR) no toca su texto:
«Pausar», «Reanudar» y «Guardando…» salen siempre en castellano, también en catalán
(«Reprendre», «Desant…»), inglés, francés, portugués, alemán e italiano. Es el botón que
más se toca en el banquillo. Arreglo: pasar los tres textos por t(); las claves ya existen
en los 7 diccionarios. No se toca el aria-label (posible gancho de pruebas).
Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
"""
import pathlib, sys
p = pathlib.Path("src/routes/_authenticated/coach.matches.live.$id.tsx")
s = p.read_text()
old = '{clockBusy ? "Guardando…" : running ? "Pausar" : "Reanudar"}'
new = '{clockBusy ? t("Guardando…") : running ? t("Pausar") : t("Reanudar")}'
if s.count(old) != 1:
    sys.exit("coach.matches.live.$id.tsx: el fragmento no aparece exactamente una vez")
p.write_text(s.replace(old, new))
print("M-006 aplicado: 1 archivo, sin textos nuevos. Ahora: bun run build")
