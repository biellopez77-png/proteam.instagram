# S-001 — El pago en modo prueba solo desde la vista previa (PR, toca pagos)

**Qué pasa hoy.** `createOrganizationCheckout` y `createBillingPortal` (`src/lib/billing.functions.ts`) aceptan el campo `environment` que manda el navegador (`z.enum(["sandbox","live"])`). Cualquier entrenador con cuenta puede llamar a la función desde pro-team.app con `environment: "sandbox"` (la clave pública de prueba está en `.env.development`), abrir el Checkout de prueba y pagar con la tarjeta 4242. El webhook (`src/routes/api/public/payments/webhook.ts`, `?env=sandbox`) escribe en la misma tabla `organization_billing` `billing_source = "stripe"` y `subscription_status = "active"/"trialing"` sin mirar el entorno, y `getAccessGate` (`access-gate.functions.ts`) solo mira `billing_source`. Resultado: acceso de pago sin pagar. Solo es explotable si el webhook de prueba está dado de alta en Stripe (hoy `payment_webhook_events` está vacía: no ha llegado ningún evento de ningún entorno).

**Arreglo.** El servidor mira el dominio real de la petición (`getRequest()`, cabeceras `x-forwarded-host`/`host`) y solo acepta `sandbox` desde `localhost`, `id-preview--…` o `*.lovableproject.com`. En pro-team.app y proteamapp.lovable.app solo vale `live`. 1 archivo, sin base de datos.

**Cómo probarlo.**
1. `python3 aplicar.py && bun run build`.
2. En la vista previa: «Continuar al pago» sigue abriendo el Checkout de prueba (4242).
3. En pro-team.app (después de publicar): el pago normal sigue funcionando (live). Llamar a la función con `environment: "sandbox"` devuelve «Entorno de pago no válido.».
4. Comprobar en los registros que `x-forwarded-host` llega con pro-team.app (si Lovable no lo pasa, `host` sirve igual).

Va por PR (rama `revision/pago-sandbox-solo-en-pruebas`) porque toca pagos.
