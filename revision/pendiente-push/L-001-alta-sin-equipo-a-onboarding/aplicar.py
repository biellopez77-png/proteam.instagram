#!/usr/bin/env python3
"""L-001 (1 archivo: src/routes/_authenticated/teams.tsx). Uso: python3 aplicar.py <ruta proteamapp>

Lanzamiento (tarea t-lanz-R1-registro). Tras crear la cuenta, `AuthForm.routeByRole`
(auth-overlay.tsx) y el enlace del correo (`emailRedirectTo` ".../teams") llevan a
/teams. Un entrenador recién registrado no tiene equipos y ve «¿A qué equipo quieres
entrar? Elige un equipo», una tarjeta «Añadir equipo — Consulta el precio del equipo
adicional» que lleva a /pricing y, abajo, «Todavía no tienes equipos · Configurar acceso».
Nada dice «crea tu equipo para entrar en la lista de espera». BD 17/11: 18 altas, 9 sin
equipo; 5 de ellas con correo confirmado y sesión iniciada (se quedaron en esta pantalla).
`getPublicAccountSummary` ya calcula `destination: "/onboarding"` para 0 equipos, pero
/teams no lo usa.

Arreglo: con 0 equipos (consulta terminada y sin error) /teams redirige a /onboarding
(«Crear mi primer equipo» / «Unirme con código»), y la tarjeta de precio del equipo
adicional no se enseña a quien aún no tiene ninguno. Sin textos nuevos ni BD.
"""
import sys, pathlib
f = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "src/routes/_authenticated/teams.tsx"
s = f.read_text()

def rep(old, new):
    global s
    assert s.count(old) == 1, f"no único / no encontrado:\n{old[:120]}"
    s = s.replace(old, new)

rep('import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";\n',
    'import { useEffect } from "react";\nimport { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";\n')
rep('  async function signOut() {\n',
    '  const noTeams = !query.isLoading && !query.isError && (query.data?.teams.length ?? 0) === 0;\n'
    '  // Without teams there is nothing to choose: go straight to create or join one.\n'
    '  useEffect(() => { if (noTeams) navigate({ to: "/onboarding", replace: true }); }, [noTeams, navigate]);\n'
    '  async function signOut() {\n')
rep('        <Link to="/pricing" className=', '        {!noTeams && <Link to="/pricing" className=')
rep('        </Link>\n      </div>}', '        </Link>}\n      </div>}')
f.write_text(s)
print("L-001 aplicado en", f)
