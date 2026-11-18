#!/usr/bin/env python3
"""M-009 y M-010 (turno 18/11 14:17 Madrid). Ejecutar desde la raíz de proteamapp:
    python3 <ruta>/aplicar.py && bun run build
M-009 (src/routes/_authenticated/onboarding.tsx): el formulario «Crear equip» solo marca
`required`; un nombre de 1 letra o una temporada de 1 carácter pasan al servidor y
`createTeamSchema` (teams.functions.ts: name min 2 / max 80, category max 60, season min 2 / max 20)
devuelve un ZodError cuyo `message` es el JSON de los fallos, que `CreateTeam.submit` enseña tal cual
(`toast.error(err.message)`). Se ponen los mismos límites en los campos (el navegador avisa en su idioma)
y los botones del paso pasan a 44 px.
M-010 (src/components/auth-overlay.tsx): «Nom»/«Cognoms» sin autocompletar del móvil, enlace
«Has oblidat la contrasenya?» de ~16 px de alto y botón de cerrar de ~36 px.
Sin textos nuevos, sin BD."""
import pathlib, sys

def sub(path, pairs):
    p = pathlib.Path(path); s = p.read_text(encoding="utf-8")
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            sys.exit(f"{path}: se esperaba 1 aparición y hay {n}: {old[:70]!r}")
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8"); print("OK", path)

sub("src/routes/_authenticated/onboarding.tsx", [
    ('<Field label="Nom de l\'equip" value={name} onChange={setName} required />',
     '<Field label="Nom de l\'equip" value={name} onChange={setName} required minLength={2} maxLength={80} />'),
    ('<Field label="Categoria" value={category} onChange={setCategory} placeholder="Cadet, Juvenil…" />',
     '<Field label="Categoria" value={category} onChange={setCategory} placeholder="Cadet, Juvenil…" maxLength={60} />'),
    ('<Field label="Temporada" value={season} onChange={setSeason} required />',
     '<Field label="Temporada" value={season} onChange={setSeason} required minLength={2} maxLength={20} />'),
    ('<button type="button" onClick={onChangeSport} className="text-sm text-primary font-medium shrink-0">Canviar</button>',
     '<button type="button" onClick={onChangeSport} className="min-h-11 px-2 text-sm text-primary font-medium shrink-0">Canviar</button>'),
    ('<button type="submit" disabled={loading} className="w-full bg-primary text-primary-foreground py-3 rounded-xl font-medium disabled:opacity-50">\n        {loading ? "Creant…" : "Crear equip"}',
     '<button type="submit" disabled={loading} className="min-h-11 w-full bg-primary text-primary-foreground py-3 rounded-xl font-medium disabled:opacity-50">\n        {loading ? "Creant…" : "Crear equip"}'),
    ('<button type="button" onClick={onBack} className="w-full text-sm text-muted-foreground py-1">Tornar</button>\n    </form>',
     '<button type="button" onClick={onBack} className="min-h-11 w-full text-sm text-muted-foreground py-1">Tornar</button>\n    </form>'),
])

sub("src/components/auth-overlay.tsx", [
    ('<Field label={t("Nom")} value={name} onChange={setName} required />',
     '<Field label={t("Nom")} value={name} onChange={setName} required autoComplete="given-name" />'),
    ('<Field label={t("Cognoms")} value={surname} onChange={setSurname} required />',
     '<Field label={t("Cognoms")} value={surname} onChange={setSurname} required autoComplete="family-name" />'),
    ('className="w-full text-xs text-muted-foreground underline underline-offset-2 disabled:opacity-50">',
     'className="min-h-11 w-full text-xs text-muted-foreground underline underline-offset-2 disabled:opacity-50">'),
    ('className="rounded-xl p-2 text-muted-foreground transition hover:bg-muted hover:text-foreground">',
     'className="grid h-11 w-11 place-items-center rounded-xl text-muted-foreground transition hover:bg-muted hover:text-foreground">'),
])
