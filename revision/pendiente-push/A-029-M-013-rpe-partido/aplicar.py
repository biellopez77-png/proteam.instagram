#!/usr/bin/env python3
"""A-029 + M-013: RPE de partido y barra de «Deshacer» del directo (commit fb80d88).

A-029 (error, src/lib/match-rpe.functions.ts, `saveMyMatchRpe`): el jugador guarda su RPE con
`resolveMatchSettings({}, match_settings)`, sin los ajustes del EQUIPO. Si el equipo tiene el modo
«grid» por defecto (sin ajuste propio en el partido), la lista «RPE pendiente» le pide los minutos
aproximados pero el servidor los guarda como null → carga del partido 0. Además el servidor no
comprueba lo que sí comprueba la lista: RPE activado, ventana de 48 h abierta y que el jugador
jugó. Arreglo: usa `loadMatchRpePlayers` (las mismas reglas que `getMyPendingMatchRpe`).
SQL 18/11: 1 equipo con modo «grid» por defecto y 3 de sus 4 partidos sin ajuste propio (RPE aún
desactivado: latente hasta que lo active).

M-013 (error de uso):
 - src/components/match-rpe.tsx (`MatchRpeSection`): en modo «grid», los minutos que el cuerpo
   técnico escribe a un jugador sin RPE no se guardan (el envío filtra `rpe !== null`) y aun así
   sale «Guardado». Ahora avisa «RPE pendiente: <nombres>» (texto ya traducido).
 - src/components/match-undo-bar.tsx: el botón «Deshacer» del directo (size="sm", 36 px) pasa a
   44 px de alto (la franja ya mide 44 px).
Sin textos nuevos. 3 archivos. Uso (raíz de proteamapp): python3 aplicar.py && bun run build
"""
import pathlib, sys
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
changes = {
 "src/lib/match-rpe.functions.ts": [(
'''    const { data: m } = await sb
      .from("matches")
      .select("id, team_id, match_settings")
      .eq("id", data.match_id)
      .maybeSingle();
    if (!m) throw new Error("Partido no encontrado");
    const grid = resolveMatchSettings({}, (m as MatchRow).match_settings).mode === "grid";
''',
'''    const { data: m } = await sb
      .from("matches")
      .select(MATCH_COLS)
      .eq("id", data.match_id)
      .maybeSingle();
    if (!m) throw new Error("Partido no encontrado");
    // Same rules as getMyPendingMatchRpe: team defaults + match override (team-level «grid» kept
    // the minutes field but they were saved as null), RPE on, 48 h window open, player played.
    const res = (await loadMatchRpePlayers(sb, (m as MatchRow).team_id, [m as MatchRow])).get(
      m.id,
    )!;
    if (
      !res.settings.rpe ||
      !matchRpeOpen(m as MatchRow) ||
      !res.players.some((p) => p.player_id === context.userId)
    )
      throw new Error("No se ha podido guardar el RPE.");
    const grid = res.settings.mode === "grid";
''')],
 "src/components/match-rpe.tsx": [(
'''    onSuccess: () => {
      void qc.invalidateQueries({ queryKey: ["match-rpe", matchId] });
      toast.success(t("Guardado"));
    },
    onError: () => toast.error(t("No se ha podido guardar")),
  });
  if (!data?.enabled || !data.played) return null;
''',
'''    onSuccess: () => {
      void qc.invalidateQueries({ queryKey: ["match-rpe", matchId] });
      // Grid mode: minutes typed without an RPE are not stored, so name who is missing it.
      const missing = (data?.players ?? []).filter((p) => {
        const d = draft[p.player_id];
        return d !== undefined && d.rpe === null && d.minutes !== null;
      });
      if (missing.length)
        toast.warning(`${t("RPE pendiente")}: ${missing.map((p) => p.name).join(", ")}`);
      else toast.success(t("Guardado"));
    },
    onError: () => toast.error(t("No se ha podido guardar")),
  });
  if (!data?.enabled || !data.played) return null;
''')],
 "src/components/match-undo-bar.tsx": [(
'''<Button variant="ghost" size="sm" onClick={() => { clear(); action.undo(); }}>''',
'''<Button variant="ghost" size="sm" className="min-h-11" onClick={() => { clear(); action.undo(); }}>''')],
}
for rel, subs in changes.items():
    p = root / rel
    s = p.read_text()
    for old, new in subs:
        if s.count(old) != 1:
            sys.exit(f"{rel}: no aparece exactamente una vez:\n{old}")
        s = s.replace(old, new)
    p.write_text(s)
print("A-029 + M-013 aplicados: 3 archivos, sin textos nuevos. Ahora: bun run build")
