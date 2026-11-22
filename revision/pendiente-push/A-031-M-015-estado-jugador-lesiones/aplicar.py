#!/usr/bin/env python3
"""A-031 + M-015 (turno 18/11 19:17 Madrid). Ejecutar desde la raíz de proteamapp:
    python3 aplicar.py && bun run build

A-031: la ficha «Registres del jugador» (`player-status.functions.ts`) solo mira la tabla
`injuries` para la disponibilidad, pero «+ Afegir lesió» de la sesión de pista
(`court/incident-dialogs.tsx`, AddInjuryButton) guarda la lesión en `court_incidents`
(type «lesio», status «oberta»). Resultado: un jugador con lesión abierta sale en verde
«Sense restricció registrada». Ahora las lesiones de sesión «oberta» cuentan como lesión
activa y las «seguiment» como recuperación (las dos palabras ya están en ACTIVE_INJURY /
RECOVERING_INJURY de `player-status.ts`). Sin textos nuevos ni BD.

M-015: el botón «Quines dades el componen» de cada indicador medía ~16 px de alto
(text-[11px] sin relleno): ahora 44 px de zona táctil sin cambiar el aspecto.
"""
import pathlib, sys

def sub(path, old, new):
    p = pathlib.Path(path)
    s = p.read_text()
    if s.count(old) != 1:
        sys.exit(f"{path}: el fragmento no aparece exactamente una vez")
    p.write_text(s.replace(old, new))
    print("ok", path)

sub("src/lib/player-status.functions.ts",
"""        injuries: injuryRows.filter((i) => i.player_id === pid),
""",
"""        injuries: [
          ...injuryRows.filter((i) => i.player_id === pid),
          // «Afegir lesió» de la sessió desa la lesió com a incidència, no a `injuries`.
          ...incidentRows
            .filter((i) => i.player_id === pid && i.type === "lesio" && (i.status === "oberta" || i.status === "seguiment"))
            .map((i) => ({
              status: i.status,
              start_date: i.incident_date,
              expected_return: null,
              title: i.injury_description ?? i.description ?? null,
            })),
        ],
""")

sub("src/components/player-status-card.tsx",
"""        className="mt-2 inline-flex items-center gap-1 text-[11px] text-muted-foreground underline underline-offset-2"
""",
"""        className="-mx-1 mt-1 inline-flex min-h-11 items-center gap-1 px-1 text-[11px] text-muted-foreground underline underline-offset-2"
""")
