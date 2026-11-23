# Ficha · Registro y entrada (panel «Crear cuenta / Iniciar sesión» y contraseña nueva): la primera puerta del 28/11

**Agente:** Irene (P1) · **Fecha:** 23/11/2026 · **Tarea:** `exp-registro-entrada` (abierta por Irene, prioridad alta: no había tareas P1 pendientes ni comentarios de Biel o Álex en las 10 entregas; es la única puerta del Día 0 sin ficha, y va antes del onboarding)
**Prototipo navegable:** https://claude.ai/artifact/JGyTmYkiSFQGr1Tw3a7mAS (móvil 375 y escritorio; selectores «Versión: Propuesta / Actual (hoy)», «Cuándo: antes del 28/11 / desde el 28/11», «Pantalla: Crear cuenta / Iniciar sesión / Revisa tu correo / He olvidado la contraseña / Contraseña nueva», «Simular al pulsar: todo bien / campos vacíos / se queda cargando / email o contraseña mal / email sin confirmar / email ya registrado / demasiados correos / sin conexión / enlace caducado»; casilla «Marcar lo propuesto»). Copia local: `agencia/experiencia/prototipos/registro-entrada.html`.
**Base leída:** rama `revision/club-fundador` de proteamapp (5c7a6bd): `src/components/auth-overlay.tsx` (`AuthForm`, `AuthOverlay`, `Field`), `src/routes/auth.tsx` (solo redirige), `src/routes/reset-password.tsx`, `src/lib/platform-admin.ts` (`passwordProblems`, `MIN_PASSWORD_LENGTH = 14`), `src/components/public-account-panel.tsx` (reutiliza `AuthForm`), `src/routes/index.tsx` (`registerLabel`, `AuthOverlay`), `src/lib/i18n/translate.ts` y `dict/es.json`.

**Por qué ahora:** el 28/11 todo entrenador nuevo y todo apuntado a la lista pasa por este panel antes que por nada. Lo que se ve hoy:
1. **Los errores de la cuenta salen en inglés.** `AuthForm` muestra `t(err.message)`, pero «Invalid login credentials», «Email not confirmed», «User already registered» o «Email rate limit exceeded» no están en `es.json`: el aviso sale tal cual, en inglés, y desaparece a los pocos segundos.
2. **El panel no sabe de dónde vienes.** El botón de la portada dice «Apúntate a la lista de espera» (antes del 28) o «Empieza tu mes de prueba» (después), pero el panel siempre abre con «Entrena, compite, evoluciona.» y «Crear cuenta».
3. **Recuperar la contraseña es un enlace que lanza un aviso.** Si el email está vacío solo sale un aviso; si no, otro aviso y nada más en pantalla.
4. **`/reset-password` está entero en catalán** («Establir una contrasenya nova», «Desar contrasenya»…) sin `t()`, y pide las reglas de los administradores (`passwordProblems`: 14 caracteres, mayúscula, minúscula, número y símbolo), mientras que al crear la cuenta bastan 8. Un entrenador que olvida su contraseña se encuentra de golpe con otras reglas, y los errores también salen en catalán.

## 1. Qué se conserva (sin tocar)
- **El panel sobre la portada:** `?auth=register` / `?auth=login`, `/auth` redirige igual, cierre con la X, tocando fuera o con Escape, `role="dialog"`.
- **Las dos pestañas** «Iniciar sesión» y «Crear cuenta», y el mismo `AuthForm` en el panel de cuenta (`public-account-panel.tsx`).
- **Los campos:** Nombre, Apellidos (`options.data: { name, surname }`), Email, Contraseña (`minLength 8` al crear).
- **Las llamadas:** `signInWithPassword`, `signUp` con `emailRedirectTo`, `resetPasswordForEmail` con `redirectTo /reset-password`, `updateUser` en `/reset-password`.
- **A dónde lleva:** `routeByRole` (`next` seguro, `/admin` o `/teams`) y, sin sesión tras registrarse, «Revisa tu correo» con el email.
- **Textos que ya existen en `es.json`:** «Iniciar sesión» · «Crear cuenta» · «Nombre» · «Apellidos» · «Email» · «Contraseña» · «Entrar» · «¿Has olvidado tu contraseña?» · «Enviando enlace…» · «Revisa tu correo» · «Te hemos enviado un enlace para confirmar tu cuenta. Ábrelo y después inicia sesión.» · «Escribe tu email para recibir el enlace.» · «Si la dirección existe, hemos enviado un enlace para restablecer la contraseña.» · «Entrena, compite, evoluciona.» · «Cerrar panel» · «Cuenta ProTeam».

## 2. Qué cambia (propuesto)
| Cambio | Detalle |
|---|---|
| **Errores en español (arreglo, no diseño)** | Añadir a `es.json` (y a los 7 idiomas) los mensajes de Supabase que pueden salir aquí, con texto que dice qué pasa y qué hacer (ver §3). **Se puede hacer antes del 28/11 aunque no se haga nada más.** Mejor aún: mapear por `error.code` (`invalid_credentials`, `email_not_confirmed`, `user_already_exists`, `over_email_send_rate_limit`) en vez de por el texto en inglés. |
| **Error dentro del panel** | Además del aviso, una caja de error encima del botón que se queda hasta que el usuario cambia algo, con su salida: «Crear una contraseña nueva», «Iniciar sesión», «Reenviar el correo». |
| **Errores por campo** | `noValidate` y mensajes propios debajo del campo («Escribe tu nombre.» · «A este email le falta algo: revisa la @ y el dominio.» · «Tiene que tener al menos 8 caracteres.»); foco en el primero que falla. Hoy los marca el navegador, cada uno a su manera. |
| **Título según de dónde viene** | Antes del 28/11, al crear cuenta: «Lista de espera» · «Apúntate a la lista» · «Crea tu cuenta para entrar en la lista de espera de ProTeam.» Desde el 28/11: «Mes de prueba» · «Empieza tu mes de prueba» · «Crea tu cuenta. En el paso siguiente creas tu equipo o te unes al de tu club.» Al iniciar sesión: «Entra en ProTeam» + «Entrena, compite, evoluciona.» (el lema de hoy). Mismo corte que `registerLabel` en `index.tsx`. Sin ofertas, precios ni plazos dentro del panel: ya los cuenta la portada y el onboarding. |
| **Mostrar / Ocultar contraseña** | Botón de texto dentro del campo. Ayuda «Al menos 8 caracteres.» al crear cuenta. |
| **«He olvidado mi contraseña» como paso** | Pantalla propia en el panel: «Crea una nueva» + email + «Enviar enlace» → «Mira tu correo» con el email y «El enlace sirve una sola vez. Si caduca, pide otro aquí.» + «Volver a iniciar sesión». Misma llamada `resetPasswordForEmail`. |
| **«Revisa tu correo» más útil** | Conserva el texto y el email; añade «Si no lo ves en unos minutos, mira en spam o en promociones.», «Reenviar el correo» (ver duda 3) y «Me he equivocado de email» (vuelve a «Crear cuenta» con los datos). |
| **Sesión iniciada sin género** | «¡Bienvenido!» → «Sesión iniciada.» (o «Hola de nuevo»). |
| **`/reset-password` en español** | Todo por `t()`. Las reglas, a la vista y en verde según se cumplen, en vez de una lista de errores en ámbar después. Enlace caducado o sin sesión: «Este enlace ya no sirve» + explicación + «Pedir otro enlace» (abre el paso de olvidar la contraseña). Al guardar: «Contraseña guardada» + «Iniciar sesión». |
| **Estilo v3** | Hoja blanca, título en Instrument Serif con trazo azul a lápiz, pestañas con raya azul en vez de cápsula gris, un solo azul para la acción, sobre dibujado a lápiz en «Revisa tu correo». Escritorio: el mismo panel centrado de hoy (máx. 448 px). |

## 3. Textos (es) nuevos, propuestos
- **Títulos:** «Lista de espera» · «Apúntate a la lista» · «Crea tu cuenta para entrar en la lista de espera de ProTeam.» · «Mes de prueba» · «Empieza tu mes de prueba» (ya existe en la portada) · «Crea tu cuenta. En el paso siguiente creas tu equipo o te unes al de tu club.» · «Entra en ProTeam».
- **Campos:** «Mostrar» · «Ocultar» · «Mostrar contraseña» / «Ocultar contraseña» (aria) · «Al menos 8 caracteres.» · «Escribe tu nombre.» · «Escribe tus apellidos.» · «Escribe tu email.» · «A este email le falta algo: revisa la @ y el dominio.» · «Escribe tu contraseña.» · «Tiene que tener al menos 8 caracteres.»
- **Botones con carga:** «Creando tu cuenta…» · «Entrando…» · «Enviando…».
- **Errores:**
  - Credenciales: «El email o la contraseña no coinciden.» + «Revisa que el email esté bien escrito. Si no recuerdas la contraseña, crea una nueva.» + «Crear una contraseña nueva».
  - Sin confirmar: «Aún no has confirmado tu email.» + «Busca el correo de ProTeam (también en spam) y abre el enlace. Después vuelve a entrar.» + «Reenviar el correo».
  - Ya registrado: «Ya hay una cuenta con este email.» + «Entra con tu contraseña o crea una nueva si no la recuerdas.» + «Iniciar sesión» · «Crear una contraseña nueva».
  - Demasiados correos: «Has pedido varios correos seguidos.» + «Espera unos minutos antes de pedir otro; el último que te llegue es el que vale.»
  - Sin conexión: «No hay conexión.» + «Revisa tu conexión y vuelve a intentarlo; no se ha guardado nada.» (mismo texto que onboarding y recorrido inicial).
- **Correo enviado:** «Si no lo ves en unos minutos, mira en spam o en promociones.» · «Reenviar el correo» · «Correo reenviado.» · «Me he equivocado de email».
- **Olvidé la contraseña:** «Contraseña» · «Crea una nueva» · «Escribe el email de tu cuenta y te mandamos un enlace para cambiarla.» · «Enviar enlace» · «Mira tu correo» · «Si hay una cuenta con este email, te hemos enviado un enlace para crear una contraseña nueva:» · «El enlace sirve una sola vez. Si caduca, pide otro aquí.» · «Volver a iniciar sesión» · «Volver».
- **Contraseña nueva:** «Elige tu contraseña nueva» · «Contraseña nueva» · «Repítela» · reglas («14 caracteres o más» · «Mayúscula y minúscula» · «Un número» · «Un símbolo (- . ! ?)»; cambian si se acepta la duda 1) · «A la contraseña le falta algo.» + «Mira la lista: lo que no está en verde es lo que falta.» · «No coincide con la de arriba.» · «Guardar contraseña» · «Guardando…» · «Contraseña guardada» · «Contraseña actualizada.» · «Ahora entra con tu email y la contraseña nueva.» · «Este enlace ya no sirve» · «Los enlaces para cambiar la contraseña caducan al rato y solo valen una vez. Pide otro y ábrelo en cuanto te llegue.» · «Pedir otro enlace».
- **Otros:** «Sesión iniciada.» Título de la pestaña de `/reset-password`: «Contraseña nueva — ProTeam».
- Todos necesitan su traducción en los 7 idiomas de `lib/i18n/dict/`.

## 4. Componentes del código afectados
- `src/components/auth-overlay.tsx`:
  - `AuthForm`: nuevo modo `forgot` (y su estado «enviado») junto a `login` / `register`; caja de error en estado (`error: { title, body, actions }`) que se limpia al escribir; `noValidate` + validación propia por campo; botón Mostrar/Ocultar en `Field`; traducción por `error.code` con texto de reserva; «Reenviar el correo» en `awaitConfirm` (duda 3); «Me he equivocado de email».
  - `AuthOverlay`: recibir de dónde viene (`intent: "waitlist" | "trial" | "login"`, o la fecha) para el título; el `h2` pasa a `aria-labelledby`.
- `src/routes/index.tsx`: pasar a `AuthOverlay` el mismo `campaign` que ya decide `registerLabel`.
- `src/routes/reset-password.tsx`: `t()` en todo (también `head`), reglas como lista viva, estado «enlace caducado» con botón a `/?auth=login` en modo olvido, estado «guardada».
- `src/lib/platform-admin.ts`: solo si se acepta la duda 1 (una regla para entrenadores, otra para administradores); hoy sus mensajes tampoco pasan por `t()` salvo el primero.
- `src/components/public-account-panel.tsx`: nada propio; hereda los cambios de `AuthForm` (su título «Inicia sesión» se queda).
- `src/lib/i18n/dict/*.json`: textos nuevos y mensajes de error.
- **Sin cambios:** Supabase, tablas, correos, `routeByRole`, `/auth`.

## 5. Dudas para Biel
1. **¿Qué reglas pide la contraseña nueva a un entrenador?** Al crearla bastan 8 caracteres; al restablecerla se piden 14 con mayúscula, minúscula, número y símbolo (son las de los administradores). Propongo que el entrenador tenga la misma regla en los dos sitios (8, o la que decidáis) y que la de 14 se quede para administradores. Es una decisión de seguridad: la toma el equipo técnico contigo; el prototipo enseña la regla actual.
2. **¿Arreglamos ya los errores en inglés y `/reset-password` en catalán antes del 28/11?** Son textos, sin tocar funciones. El resto (título según de dónde viene, paso de olvido, estilo) puede ir en el primer mes.
3. **«Reenviar el correo» de confirmación.** No existe hoy; sería `supabase.auth.resend({ type: "signup", email })`, una llamada nueva aunque sin tocar la base de datos. ¿Lo añadimos o dejamos solo el consejo de mirar en spam?
4. **Apuntarse antes del 28: ¿cuándo está uno «en la lista»?** ¿Al crear la cuenta o al confirmar el email? Según la respuesta, «Revisa tu correo» puede decir «Confirma tu email para quedar en la lista» (hoy no lo digo para no prometer algo que no sé).
5. **Email ya registrado.** Si en Supabase está activa la confirmación por email, registrarse con un email que ya existe puede no dar error (devuelve un usuario sin identidades) y el panel enseñaría «Revisa tu correo» sin enviar nada. ¿Lo comprueba el equipo técnico (`data.user.identities.length === 0`) para enseñar «Ya hay una cuenta con este email»?

## 6. Fuera a propósito
Precio, ofertas, tarjeta y plazos (viven en la portada y el onboarding); Club Fundador, insignia y número de apuntados; el nombre de Biel; entrar con Google u otras cuentas (no existe hoy).
