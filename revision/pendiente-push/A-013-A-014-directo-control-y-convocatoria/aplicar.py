#!/usr/bin/env python3
"""A-013 + A-014 (1 archivo: src/lib/live-match.functions.ts). Uso: python3 aplicar.py <ruta proteamapp>

A-013: tomar el control del directo era «leer y luego escribir sin condición»: dos
miembros del staff pulsando a la vez acababan los dos como operador. Ahora el update
solo se aplica si `live_operator_id` sigue siendo el que se leyó; si no, el mismo
error de siempre («Un altre membre del staff ja està registrant aquest partit.»).

A-014: `saveCallups` borraba toda la convocatoria y la volvía a insertar: se perdían
porteros (`is_goalkeeper`), estado en pista y exclusiones, y si el insert fallaba el
partido se quedaba sin convocatoria. Ahora hace upsert (UNIQUE match_id,player_id ya
existe en BD) y después borra solo a quien ya no está convocado.
"""
import sys, pathlib
f = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "src/lib/live-match.functions.ts"
s = f.read_text()

def rep(old, new):
    global s
    assert s.count(old) == 1, f"no único / no encontrado:\n{old[:120]}"
    s = s.replace(old, new)

# 1) helper tras operatorStale
rep('''  return Date.now() - new Date(at).getTime() > OPERATOR_TIMEOUT_SEC * 1000;
}
''', '''  return Date.now() - new Date(at).getTime() > OPERATOR_TIMEOUT_SEC * 1000;
}

/**
 * Takes live control only if the operator is still the one read in `cur`, so two
 * staff members pressing at the same time can never both become the operator.
 */
async function takeControl(
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  context: any,
  matchId: string,
  teamId: string,
  cur: { live_operator_id: string | null },
) {
  let q = context.supabase
    .from("matches")
    .update({
      live_operator_id: context.userId,
      live_operator_at: new Date().toISOString(),
    } as never)
    .eq("id", matchId)
    .eq("team_id", teamId);
  q = cur.live_operator_id
    ? q.eq("live_operator_id", cur.live_operator_id)
    : q.is("live_operator_id", null);
  const { data, error } = await q.select("id");
  if (error) throw new Error(error.message);
  if (!(data as unknown[] | null)?.length) {
    throw new Error("Un altre membre del staff ja està registrant aquest partit.");
  }
}
''')

# 2) requireOperator
rep('''  if (cur.live_operator_id !== context.userId) {
    await context.supabase
      .from("matches")
      .update({
        live_operator_id: context.userId,
        live_operator_at: new Date().toISOString(),
      } as never)
      .eq("id", matchId)
      .eq("team_id", m.team_id);
  }
  return m;''', '''  if (cur.live_operator_id !== context.userId) {
    await takeControl(context, matchId, m.team_id, cur);
  }
  return m;''')

# 3) claimMatchControl
rep('''    const { error } = await context.supabase
      .from("matches")
      .update({
        live_operator_id: context.userId,
        live_operator_at: new Date().toISOString(),
      } as never)
      .eq("id", data.match_id)
      .eq("team_id", m.team_id);
    if (error) throw new Error(error.message);
    return { ok: true, operator_id: context.userId };''', '''    await takeControl(context, data.match_id, m.team_id, cur);
    return { ok: true, operator_id: context.userId };''')

# 4) saveCallups
rep('''    await context.supabase
      .from("match_callups")
      .delete()
      .eq("match_id", data.match_id)
      .eq("team_id", m.team_id);
    if (called.length) {
      const starters = new Set(starterIds);
      const rows = called.map((pid) => ({
        match_id: data.match_id,
        team_id: m.team_id,
        player_id: pid,
        called: true,
        starter: starters.has(pid),
      }));
      const { error } = await context.supabase.from("match_callups").insert(rows as never);
      if (error) throw new Error(error.message);
    }
    return { ok: true };''', '''    // Upsert first, then drop only who is no longer called: goalkeepers, live
    // status and exclusions of players who stay are kept, and a failed write
    // never leaves the match without a call-up.
    if (called.length) {
      const starters = new Set(starterIds);
      const rows = called.map((pid) => ({
        match_id: data.match_id,
        team_id: m.team_id,
        player_id: pid,
        called: true,
        starter: starters.has(pid),
      }));
      const { error } = await context.supabase
        .from("match_callups")
        .upsert(rows as never, { onConflict: "match_id,player_id" });
      if (error) throw new Error(error.message);
    }
    let removed = context.supabase
      .from("match_callups")
      .delete()
      .eq("match_id", data.match_id)
      .eq("team_id", m.team_id);
    if (called.length) removed = removed.not("player_id", "in", `(${called.join(",")})`);
    const { error: removeError } = await removed;
    if (removeError) throw new Error(removeError.message);
    return { ok: true };''')

f.write_text(s)
print("OK", f)
