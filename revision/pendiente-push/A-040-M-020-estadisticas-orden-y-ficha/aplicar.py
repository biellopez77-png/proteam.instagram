#!/usr/bin/env python3
"""A-040 + M-020 (20/11, turno 12:17 Madrid) — src/components/match-stats.tsx (1 archivo, sin BD).

A-040: en la tabla de estadísticas del partido, al pulsar las cabeceras «Exc.», «As.», «At.»,
«1v1 A», «1v1 D», «CA p.» o «% CA» el botón queda marcado (aria-pressed) pero la lista se
sigue ordenando por goles: `value()` solo conocía minutos, %, recuperaciones, pérdidas y
lanzamientos. Ahora cada columna ordena por su propio número (paradas, exclusiones…).
M-020: la ficha del jugador no se cerraba con Escape, no era un diálogo para lectores de
pantalla y su X medía 32 px; «Columnes» sin aria-expanded y los chips sin aria-pressed.

Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
"""
import pathlib, sys

p = pathlib.Path("src/components/match-stats.tsx")
s = p.read_text(encoding="utf-8")

REPL = [
    # A-040: orden por la columna pulsada
    (
        """type ColId = (typeof COLUMNS)[number]["id"];
""",
        """type ColId = (typeof COLUMNS)[number]["id"];

/** Number used to sort the table by a column (higher first). */
function sortValue(a: PlayerAgg, id: ColId): number {
  switch (id) {
    case "minutes": return a.seconds;
    case "goals": return a.goals;
    case "shots": return a.shots;
    case "pct": return a.effectiveness;
    case "steals": return a.steals;
    case "turnovers": return a.turnovers;
    case "exclusions": return a.exclusions;
    case "duel_off": return a.one_v_one_won;
    case "duel_def": return a.duel_def_won;
    case "assists": return a.assists;
    case "saves": return a.saves;
    case "gk_fb": return a.gk_fb_ok;
    case "gk_fb_pct": return a.gk_fb_att ? a.gk_fb_pct : -1;
  }
}
""",
    ),
    (
        """        (a, b) => {
          const value = (r: PlayerAgg) => sort === "minutes" ? r.seconds : sort === "pct" ? r.effectiveness : sort === "steals" ? r.steals : sort === "turnovers" ? r.turnovers : sort === "shots" ? r.shots : r.goals;
          return value(b) - value(a);
        },""",
        """        (a, b) => sortValue(b, sort) - sortValue(a, sort) || b.goals - a.goals,""",
    ),
    # M-020: «Columnes» y chips con estado para lectores de pantalla
    (
        """          onClick={() => setConfig((v) => !v)}
          className="inline-flex items-center gap-1 rounded-lg border border-border px-2 py-1 text-[11px] text-muted-foreground\"""",
        """          onClick={() => setConfig((v) => !v)}
          aria-expanded={config}
          className="inline-flex items-center gap-1 rounded-lg border border-border px-2 py-1 text-[11px] text-muted-foreground\"""",
    ),
    (
        """              onClick={() => toggle(c.id)}
              className=""",
        """              onClick={() => toggle(c.id)}
              aria-pressed={cols.includes(c.id)}
              className=""",
    ),
    # M-020: ficha del jugador como diálogo, Escape y X de 44 px
    (
        """  const faced = agg.saves + agg.goals_against;""",
        """  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);
  const faced = agg.saves + agg.goals_against;""",
    ),
    (
        """      <div className="max-h-[92vh] w-full overflow-y-auto overscroll-contain rounded-t-3xl border border-border bg-card p-4 sm:max-w-2xl sm:rounded-3xl">""",
        """      <div
        role="dialog"
        aria-modal="true"
        aria-label={`${player.name} ${player.surname}`}
        className="max-h-[92vh] w-full overflow-y-auto overscroll-contain rounded-t-3xl border border-border bg-card p-4 sm:max-w-2xl sm:rounded-3xl"
      >""",
    ),
    (
        """            aria-label="Tancar"
            className="shrink-0 rounded-lg border border-border p-2\"""",
        """            aria-label="Tancar"
            className="inline-flex h-11 w-11 shrink-0 items-center justify-center rounded-lg border border-border\"""",
    ),
]

for old, new in REPL:
    if s.count(old) != 1:
        sys.exit(f"No encuentro exactamente una vez:\n{old[:120]}")
    s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
print("A-040 + M-020 aplicados en", p)
