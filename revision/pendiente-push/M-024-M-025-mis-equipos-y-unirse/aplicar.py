#!/usr/bin/env python3
"""M-024 + M-025 (mejora continua: registro e inicio del entrenador, 20/11 19:17 Madrid).

M-024 — «Tus equipos» (`src/routes/_authenticated/teams.tsx`, commit 488db5e):
- Cada tarjeta enseña el rol interno en inglés: `team.role.replaceAll("_", " ")`
  → «team admin · 12 miembros» (BD 20/11: 34 entrenadores son team_admin).
  Ahora `t(ROLE_SHORT[team.role])` («Admin», «Entrenador»…, claves que ya usa
  `onboarding.tsx` en «Entro como»).
- Si `listMyTeams` falla (sin cobertura), `query.isError` no se trata: sale
  «Todavía no tienes equipos» + «Configurar acceso» y la tarjeta «Añadir equipo».
  Un entrenador con equipo puede acabar creando otro duplicado. Ahora aviso con
  «Reintentar».
- `choose` (useMutation de `selectTeam`) no tiene `onError`: si falla, tocar el
  equipo no hace nada. Ahora sale el error.

M-025 — «Unirme con código» (`src/routes/_authenticated/onboarding.tsx`, `JoinWithCode`):
- El campo del código no está en un `<form>`: la tecla «Ir»/Intro del móvil no
  hace nada y el jugador tiene que cerrar el teclado para ver el botón.
  Ahora es un formulario: Intro comprueba el código y, ya comprobado, entra.
- Sin `autoCapitalize/autoCorrect/spellCheck`: el corrector del móvil «arregla»
  códigos como `HANDBO-K7P2QX-…`. Se apagan.

Sin BD. 2 archivos + 2 claves en los 7 diccionarios (si no existen ya).
Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import json, pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

TR = {
    "No se han podido cargar tus equipos. Revisa la conexión y vuelve a intentarlo.": {
        "ca": "No s'han pogut carregar els teus equips. Revisa la connexió i torna-ho a provar.",
        "en": "We couldn't load your teams. Check your connection and try again.",
        "fr": "Impossible de charger vos équipes. Vérifiez la connexion et réessayez.",
        "pt": "Não foi possível carregar as tuas equipas. Verifica a ligação e tenta de novo.",
        "de": "Deine Teams konnten nicht geladen werden. Prüfe die Verbindung und versuche es erneut.",
        "it": "Non è stato possibile caricare le tue squadre. Controlla la connessione e riprova.",
    },
    "Reintentar": {
        "ca": "Torna-ho a provar", "en": "Try again", "fr": "Réessayer",
        "pt": "Tentar de novo", "de": "Erneut versuchen", "it": "Riprova",
    },
}

ERR = "No se han podido cargar tus equipos. Revisa la conexión y vuelve a intentarlo."

EDITS = {
    "src/routes/_authenticated/teams.tsx": [
        ('import { STAFF_ROLES } from "@/lib/teams";',
         'import { ROLE_SHORT, STAFF_ROLES } from "@/lib/teams";\nimport { toast } from "sonner";'),
        ('''    onSuccess: async ({ role }) => {
      await qc.invalidateQueries();
      navigate({ to: STAFF_ROLES.includes(role) ? "/coach" : "/app", replace: true });
    },
  });''',
         '''    onSuccess: async ({ role }) => {
      await qc.invalidateQueries();
      navigate({ to: STAFF_ROLES.includes(role) ? "/coach" : "/app", replace: true });
    },
    onError: (e) => toast.error(e instanceof Error ? t(e.message) : t("Error")),
  });'''),
        ('{query.isLoading ? <p className="text-sm text-muted-foreground">Cargando equipos…</p> : <div className="grid gap-3 md:grid-cols-2 lg:grid-cols-3">',
         '{query.isLoading ? <p className="text-sm text-muted-foreground">Cargando equipos…</p> : query.isError ? <div role="alert" className="rounded-lg border border-border bg-card p-6"><p className="text-sm">{t("' + ERR + '")}</p><Button className="mt-4" variant="outline" onClick={() => query.refetch()}>{t("Reintentar")}</Button></div> : <div className="grid gap-3 md:grid-cols-2 lg:grid-cols-3">'),
        ('{team.role.replaceAll("_", " ")}', '{t(ROLE_SHORT[team.role])}'),
        ('{!query.isLoading && (query.data?.teams.length ?? 0) === 0 && <div',
         '{!query.isLoading && !query.isError && (query.data?.teams.length ?? 0) === 0 && <div'),
    ],
    "src/routes/_authenticated/onboarding.tsx": [
        ('''    <div className="mt-8 bg-card border border-border rounded-2xl p-5 space-y-4">
      <p className="font-display font-bold">{t("Código de equipo")}</p>''',
         '''    <form
      onSubmit={(e) => {
        e.preventDefault();
        if (loading) return;
        if (!preview) { if (code.trim().length >= 4) void check(); }
        else if (role) void join();
      }}
      className="mt-8 bg-card border border-border rounded-2xl p-5 space-y-4"
    >
      <p className="font-display font-bold">{t("Código de equipo")}</p>'''),
        ('''        placeholder="EQUIP-XXXX"
''',
         '''        placeholder="EQUIP-XXXX"
        autoCapitalize="characters"
        autoComplete="off"
        autoCorrect="off"
        spellCheck={false}
        enterKeyHint="go"
'''),
        ('<button onClick={check} disabled={loading || code.length < 4}',
         '<button type="submit" disabled={loading || code.trim().length < 4}'),
        ('<button onClick={join} disabled={loading || !role}',
         '<button type="submit" disabled={loading || !role}'),
        ('''      <button onClick={onBack} className="min-h-11 w-full text-sm text-muted-foreground">{t("Volver")}</button>
    </div>
  );
}

function SportPicker''',
         '''      <button type="button" onClick={onBack} className="min-h-11 w-full text-sm text-muted-foreground">{t("Volver")}</button>
    </form>
  );
}

function SportPicker'''),
    ],
}

for rel, reps in EDITS.items():
    p = root / rel
    code = p.read_text(encoding="utf-8")
    for old, new in reps:
        if code.count(old) != 1:
            sys.exit(f"{rel} ha cambiado (no encuentro una vez: {old[:70]!r}); revisar a mano")
        code = code.replace(old, new)
    p.write_text(code, encoding="utf-8")
    print(f"{rel}: {len(reps)} cambios")

for lang in ["es", "ca", "en", "fr", "pt", "de", "it"]:
    p = root / "src/lib/i18n/dict" / f"{lang}.json"
    if not p.exists():
        continue  # el harness de prueba no trae diccionarios
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    added = 0
    for key, tr in TR.items():
        if d.get(key):
            continue
        d[key] = key if lang == "es" else tr[lang]
        added += 1
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    print(f"{lang}: {added} claves añadidas")
