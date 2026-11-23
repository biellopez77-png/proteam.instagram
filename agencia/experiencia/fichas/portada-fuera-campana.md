# Ficha · Portada nueva fuera de campaña (desde el 28/11)

**Agente:** Irene (P1) · **Fecha:** 23/11/2026 · **Tarea:** `exp-portada-fuera-campana` (PLAN, primer mes 28/11–28/12: «portada nueva fuera de campaña»)
**Prototipo navegable:** https://claude.ai/artifact/26ZvVrWTpTMkTF6svpgW7H (móvil 375 y escritorio; versión propuesta y actual para comparar; estados: portada, primer fotograma antes de cargar, registro abierto, campos vacíos, creando cuenta, error, revisa tu correo; casilla «Marcar lo propuesto»). Fuente: `agencia/experiencia/prototipos/portada-fuera-campana.html`.
**Base (proteamapp, rama `revision/club-fundador`):** `src/routes/index.tsx` (rama `campaign = false`), `components/landing/blackout-friday.tsx` (`AuthButtons`, `useBlackoutRemaining`), `components/landing/app-mockups.tsx`, `components/founder/founder-landing.tsx`, `components/auth-overlay.tsx`, `components/public-header.tsx`, `components/public-footer.tsx`, `lib/blackout-friday.ts`.

## 1. Qué se conserva (sin tocar)
- Todos los textos de la rama fuera de campaña: «Hecho en el banquillo, no en una oficina.», «La app para entrenadores de fútbol, baloncesto y balonmano. Prueba 1 mes gratis.», «Empieza tu mes de prueba», «Iniciar sesión», «Empieza hoy».
- Las 3 funciones con su título y texto («Prepara. Compite. Mejora.» / «Prepara y valora cada sesión» / «Tu equipo, en datos. Sin humo.»), los 3 pasos de «Así funciona la prueba» y la cita «Sabemos lo que es planificar a las once de la noche, después del curro.» — «El equipo de ProTeam, entrenadores como tú».
- `AuthButtons` → `?auth=register` / `?auth=login`; `AuthOverlay` entero (pestañas, campos Nombre, Apellidos, Email, Contraseña con `minLength 8`, toasts, estado «Revisa tu correo»).
- `PublicFooter`, rutas `/futbol`, `/baloncesto`, `/balonmano`, `/pricing`, JSON-LD con `PRICE_OFFERS`.
- **Sin precio en pantalla** (regla de Biel del 18/11 en `lib/blackout-friday.ts`: «Nunca se pone el precio»).
- El bloque `FounderLandingSection` sigue solo en campaña; fuera de campaña se propone otro más pequeño (abajo).

## 2. Qué cambia (todo es propuesta; decide Biel)
| Cambio | Detalle | Tipo |
|---|---|---|
| Titular | H1 en Instrument Serif: «La semana de tu equipo, *en un solo sitio*.» con trazo azul a lápiz. Hoy el H1 repite «ProTeam» justo debajo de la marca. | Texto + visual |
| Semana de ejemplo | Una semana dibujada en el hero (L–D, 3 sesiones con minutos, partido el sábado), marcada «Ejemplo». Sustituye al hueco vacío del hero; reutiliza el estilo de `PlanningMock`. | Visual |
| Línea bajo el botón | «No se cobra nada antes y puedes cancelar.» (sale del paso 2 actual, no es condición nueva). | Texto |
| Enlaces a deportes | Fútbol · Baloncesto · Balonmano bajo el botón, a las rutas que ya existen. | Navegación |
| Ancla `#producto` y `#como-funciona` | `public-header.tsx` enlaza a `/#producto` y `/#como-funciona`, pero `index.tsx` no tiene esos `id`. Añadirlos a las secciones de funciones y de pasos. | Arreglo |
| Funciones | Etiquetas «Producto» y «Cómo funciona»; se quitan los dorsales 01/02/03 de las funciones (no son una secuencia). Los pasos sí llevan 1-2-3. Mockups de `app-mockups.tsx` más sobrios (papel, filetes, un azul). | Visual |
| Club Fundador cerrado | Bloque pequeño con el rayo: «Los primeros *ya están dentro*.» + «Entraron por la lista de espera, que se cerró el 27 de noviembre. Cada fundador tiene su insignia con su número. **No contamos cuántos son.**» + enlace «¿Eres fundador? Entra y mira tu insignia» (→ `?auth=login`). Sin ventajas nuevas ni número de apuntados. | Texto + componente |
| Primer fotograma | Hoy `campaign = !mounted \|\| remaining !== null`: antes de hidratar, **siempre** se pinta la versión de campaña. Desde el 28/11 cada visita enseña «Blackout Friday» y el hueco de la cuenta atrás y luego salta a «ProTeam». Propuesta: `campaign = mounted ? remaining !== null : blackoutActive(Date.now())` (en el servidor ya se sabe la fecha) o, si no, primer fotograma neutro con huecos en gris. | Arreglo |
| Descripción para Google | `head.description` lleva fijo «Blackout Friday: apúntate a la lista de espera y consigue 3 meses gratis.». Desde el 28/11 debería decir lo de la prueba de 1 mes (sin precio). | Arreglo |
| Registro: error | Además del toast, aviso dentro del panel: «No hemos podido crear tu cuenta. Revisa tu conexión y vuelve a intentarlo. Lo que has escrito sigue aquí.» Si el servidor da un motivo (`err.message`), se enseña ese. | Estado |
| Registro: vacío y espera | Mensaje por campo («Escribe tu nombre.», «Escribe tus apellidos.», «Escribe tu email.», «La contraseña necesita al menos 8 caracteres.»), pista «Al menos 8 caracteres.» y botón «Creando tu cuenta…» desactivado mientras espera. | Estado |
| Línea bajo «Crear cuenta» | «Después creas tu equipo. El mes de prueba empieza al añadir tu tarjeta.» — **verificar** que el mes empieza al añadir la tarjeta (el paso 2 lo da a entender); si no, se quita. | Texto, a confirmar |

## 3. Textos nuevos (para `t()` / i18n)
- «La semana de tu equipo, en un solo sitio.» · «No se cobra nada antes y puedes cancelar.» · «Producto» · «Cómo funciona» · «Ejemplo» · «Semana 14 · Cadete A» · «3 sesiones · 1 partido» · «Partido» · «Descanso»
- «Club Fundador» · «Los primeros ya están dentro.» · «Entraron por la lista de espera, que se cerró el 27 de noviembre. Cada fundador tiene su insignia con su número.» · «No contamos cuántos son.» · «¿Eres fundador? Entra y mira tu insignia»
- «No hemos podido crear tu cuenta.» · «Revisa tu conexión y vuelve a intentarlo. Lo que has escrito sigue aquí.» · «Escribe tu nombre.» · «Escribe tus apellidos.» · «Escribe tu email.» · «La contraseña necesita al menos 8 caracteres.» · «Al menos 8 caracteres.» · «Creando tu cuenta…» · «Después creas tu equipo. El mes de prueba empieza al añadir tu tarjeta.»
- Nota a lápiz del ejemplo (decorativa, `aria-hidden`): «el martes, la más larga».

## 4. Lo que no sale en la portada
Precio o importes (ni el fundador ni el normal), número de apuntados o de fundadores, nombre de Biel, tickets regalo, plazas limitadas o escasez, cuenta atrás.

## 5. Componentes afectados (para el equipo técnico, por PR)
- `src/routes/index.tsx`: H1 y subtítulo fuera de campaña, `id="producto"` / `id="como-funciona"`, cálculo de `campaign` en el primer render, `head.description` según fecha, bloque del Club cerrado (`!campaign && <FounderClosedSection />`).
- Nuevo `components/founder/founder-closed.tsx` (reutiliza `FounderBadge` con rayo, apagado, sin número).
- `components/landing/app-mockups.tsx`: nuevo `WeekMock` para el hero (o reutilizar `PlanningMock`).
- `components/landing/blackout-friday.tsx`: línea «No se cobra nada antes…» opcional en `AuthButtons` (prop `note`).
- `components/auth-overlay.tsx`: error dentro del panel, mensajes por campo y estado de envío. Ojo: sus claves están en catalán («Crear compte», «Contrasenya»…) y pasan por el diccionario; los textos nuevos, en castellano con `t()`.
- Sin tocar: `PublicFooter`, rutas de deportes, `/pricing`, Stripe.

## 6. Dudas para Biel
1. ¿Titular nuevo («La semana de tu equipo, en un solo sitio.») o se queda «ProTeam»?
2. ¿Bloque del Club Fundador cerrado en la portada? ¿Hasta cuándo (fin del primer mes, siempre)?
3. ¿Semana de ejemplo neutra (como ahora) o una por deporte según desde dónde llegue la visita?
4. ¿Enlaces a deportes en el hero o solo en el pie?
5. ¿La portada nueva entra el 28/11 a las 00:00 o durante el primer mes? (Los arreglos del primer fotograma y de la descripción convendría tenerlos el 28/11 sí o sí.)
6. ¿El mes de prueba empieza al añadir la tarjeta? Si no es así, se quita la línea bajo «Crear cuenta».
