#!/usr/bin/env python3
"""S-001: el servidor decide si un pago puede ir en modo prueba (sandbox).

Uso (en la raíz de proteamapp, rama revision/pago-sandbox-solo-en-pruebas):
    python3 <ruta>/aplicar.py && bun run build
Toca solo src/lib/billing.functions.ts.
"""
import pathlib, sys

p = pathlib.Path("src/lib/billing.functions.ts")
s = p.read_text()

def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"S-001: esperaba {count} coincidencia(s) y hay {n}: {old[:70]!r}")
    s = s.replace(old, new)

# 1) Importar getRequest (el mismo que usa auth-middleware.ts).
rep('import { createServerFn } from "@tanstack/react-start";\n',
    'import { createServerFn } from "@tanstack/react-start";\nimport { getRequest } from "@tanstack/react-start/server";\n')

# 2) Función que mira el dominio REAL de la petición (no el que manda el navegador).
rep('async function resolveOrCreateCustomer(',
'''// El modo prueba de Stripe (tarjeta 4242) solo se acepta desde la vista previa o en local.
// Desde pro-team.app o proteamapp.lovable.app siempre es "live": si no, cualquiera podría
// llamar a la función con environment "sandbox", pagar con una tarjeta de prueba y el
// webhook de prueba le dejaría la organización como suscrita (comparten base de datos).
function requestHost() {
  const request = getRequest();
  const forwarded = request?.headers.get("x-forwarded-host")?.split(",")[0]?.trim();
  const host = forwarded || request?.headers.get("host") || (request?.url ? new URL(request.url).host : "");
  return host.toLowerCase().replace(/:\\d+$/, "");
}

function requireEnvironmentForHost(environment: "sandbox" | "live") {
  if (environment === "live") return;
  const host = requestHost();
  const sandboxHost = host === "localhost" || host === "127.0.0.1"
    || host.startsWith("id-preview--") || host.endsWith(".lovableproject.com");
  if (!sandboxHost) throw new Error("Entorno de pago no válido.");
}

async function resolveOrCreateCustomer(''')

# 3) Comprobarlo en el pago y en el portal de facturación.
rep('''    await requireOrganizationAdmin(context as never, data.organizationId);
    const origin = requireAllowedOrigin(data.origin);
''', '''    await requireOrganizationAdmin(context as never, data.organizationId);
    requireEnvironmentForHost(data.environment);
    const origin = requireAllowedOrigin(data.origin);
''', count=2)

p.write_text(s)
print("S-001 aplicado en", p)
