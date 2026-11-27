#!/usr/bin/env python3
"""L-004 (1 archivo: src/lib/billing.functions.ts). Uso: python3 aplicar.py <ruta proteamapp>
TOCA PAGOS → rama `revision/pago-dominio-pro-team-app` + PR para Biel (no a main).

Tarea t-estr-R1-dia0 (día 28, entrada con tarjeta). `requireAllowedOrigin` solo acepta
localhost, proteamapp.lovable.app, la vista previa y lo que haya en el secreto
PAYMENTS_ALLOWED_ORIGINS. El dominio público, https://pro-team.app, no está en la lista
fija. Si ese secreto no lo incluye, el 28 los 15 equipos de la lista, al pulsar pagar desde
pro-team.app, reciben «Origen de pagament no autoritzat.» y no pueden empezar la prueba
(lo mismo con «Gestionar en Stripe», `createBillingPortal`). BD 18/11: 0 suscripciones de
Stripe creadas nunca (`organization_billing.stripe_subscription_id` vacío en las 23 filas),
así que el pago desde el dominio público no se ha probado.

Arreglo: añadir https://pro-team.app y https://www.pro-team.app a la lista fija.
"""
import sys, pathlib
f = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "src/lib/billing.functions.ts"
s = f.read_text()
old = '  "https://proteamapp.lovable.app",\n'
assert s.count(old) == 1, "no encontrado"
s = s.replace(old, old + '  "https://pro-team.app",\n  "https://www.pro-team.app",\n')
f.write_text(s)
print("L-004 aplicado en", f)
