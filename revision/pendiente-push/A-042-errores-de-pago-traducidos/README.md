# A-042 · Errores de pago en el idioma del entrenador

Auditoría de traducciones (20/11 14:21 Madrid, commit 488db5e, leído con `read_file` de Lovable). Irá como PR (toca Stripe y, desde el 20/11, nada se publica sin Biel).

| Dónde | Antes | Después |
|---|---|---|
| `src/lib/stripe.server.ts` `getStripeErrorMessage` (usado en `createOrganizationCheckout` y `createBillingPortal` de `billing.functions.ts`) | Devuelve al entrenador el texto crudo del error: inglés de Stripe o «STRIPE_LIVE_API_KEY is not configured» (nombre de una clave interna). Si no hay texto, «Stripe request failed», que en `es.json` vale «Stripe request failed» | Apunta el error real en el registro del servidor (`console.error("[stripe]")`) y devuelve «No s'ha pogut connectar amb el sistema de pagament. Torna-ho a provar.», traducido en los 7 idiomas |
| `src/routes/pricing.tsx` (vuelta del pago, `toast.error(t(result.error))`) | «No s'ha pogut comprovar l'estat del pagament. Torna-ho a provar.» (de `getCheckoutResult`) no está en ningún diccionario: sale en catalán en es, en, fr, pt, de e it | Traducido en los 6 idiomas |
| `src/routes/pricing.tsx` | El `session_id` se borra de la dirección antes de mirar el resultado: el «Torna-ho a provar» no sirve, recargar no reintenta | La dirección solo se limpia si la comprobación ha ido bien |

Aplicar: `python3 aplicar.py` desde la raíz de proteamapp (idempotente; se para si el código no coincide), `bun run build`, rama `revision/errores-pago-traducidos`, PR.
Probado sobre copias de los 7 diccionarios de 488db5e (el formato JSON se conserva byte a byte salvo las 2 claves nuevas por idioma) y sobre los bloques exactos de `stripe.server.ts` y `pricing.tsx`. Falta `bun run build` (sin acceso a proteamapp).

Cómo probarlo: en la vista previa (Stripe de prueba) con el idioma en inglés, abrir `/pricing?checkout=return&session_id=cs_test_noexiste` → aviso en inglés, y al recargar vuelve a comprobar. Con una clave de Stripe mal puesta en la vista previa, «Suscribirse» enseña la frase traducida y no el nombre de la clave.
