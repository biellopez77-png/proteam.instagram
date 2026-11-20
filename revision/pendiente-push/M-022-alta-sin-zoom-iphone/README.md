# M-022 — Alta y «Crear equipo»: el iPhone amplía la página al tocar un campo

Turno 20/11 15:17 Madrid (auditoría: móvil a 375 px). Código leído con `read_file` de Lovable, commit 488db5e.

**Qué pasa.** Safari del iPhone amplía la página al enfocar un campo con letra de menos de 16 px. No hay ninguna regla global que lo evite (`src/styles.css`: el viewport es `width=device-width, initial-scale=1` en `__root.tsx` y no hay `font-size: 16px` para móvil). Los campos de:
- `src/components/auth-overlay.tsx`, `Field` (panel «Apúntate a la lista de espera» / «Iniciar sesión»): `text-sm` = 14 px.
- `src/routes/_authenticated/onboarding.tsx`, `Field` («Crear equip», «Canjear código»): `text-sm` = 14 px.

Al tocar «Nom» en un iPhone la página se amplía, el panel queda cortado por los lados y hay que pellizcar para ver «Crear compte». Es el primer contacto de los apuntados de la lista. El `Input` de shadcn (`components/ui/input.tsx`) ya lo hace bien: `text-base md:text-sm`.

Además, «Tornar» en los pasos «Quin esport…» y «Quina modalitat…» (`SportPicker`, `VariantPicker`) mide ~28 px de alto (`py-1`), por debajo de 44 px.

**Arreglo (2 archivos, 4 líneas).** `text-base sm:text-sm` en los dos `Field` (16 px en el móvil, igual que hoy desde 640 px) y `min-h-11` en los dos «Tornar».

**Aplicar.** En proteamapp: `python3 aplicar.py`, `bun run build`, y (regla del 20/11) rama `revision/m-022-alta-sin-zoom` + PR para Biel.
