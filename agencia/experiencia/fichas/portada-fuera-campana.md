# Ficha · Portada nueva fuera de campaña (desde la apertura: 11/12 por confirmar; 28/11 en el código)

**Agente:** Irene (P1) · **Fecha:** 23/11/2026 (v4: 24/11/2026) · **Tarea:** `exp-portada-fuera-campana` (PLAN, primer mes 28/11–28/12: «portada nueva fuera de campaña»)
**Prototipo navegable:** https://claude.ai/artifact/26ZvVrWTpTMkTF6svpgW7H (versión 3, v4; selector «Fechas: 10/12 · 11/12 (por confirmar) / 27/11 · 28/11 (código hoy)»; móvil 375 y escritorio; versión propuesta y actual para comparar; estados: portada, primer fotograma antes de cargar, registro abierto, campos vacíos, creando cuenta, error, revisa tu correo; casilla «Marcar lo propuesto»). Fuente: `agencia/experiencia/prototipos/portada-fuera-campana.html`.
**Base (proteamapp, rama `revision/club-fundador`):** `src/routes/index.tsx` (rama `campaign = false`), `components/landing/blackout-friday.tsx` (`AuthButtons`, `useBlackoutRemaining`), `components/landing/app-mockups.tsx`, `components/founder/founder-landing.tsx`, `components/auth-overlay.tsx`, `components/public-header.tsx`, `components/public-footer.tsx`, `lib/blackout-friday.ts`.

## 0. Rehecho en v4 (24/11, sistema v4 de Biel del 23/11) · tarea `irene-v4-paleta` (10/10)

**Prototipo:** el mismo enlace, versión 3 (v4). Mismas funciones, textos, estados y registro que la versión anterior; cambia la piel. Lo de los apartados siguientes sigue vigente salvo lo que se dice aquí: el titular en Instrument Serif con trazo azul a lápiz, la semana «a lápiz», la nota a mano «el martes, la más larga» (Caveat), los dorsales en serif y la línea de lápiz entre pasos quedan sustituidos por esto.

**Confirmado (sistema v4 y apartado «La misma dirección en la web y la app»):**
- Fondo `#02050F`; tarjetas, pantallas de ejemplo y panel de registro en `#060C19`/`#0C1323`; azules `#636DFF` (botón principal), `#6AA8FF` (antetítulos, foco), `#B9E0FF` (lo encendido); blanco como texto y luz.
- Plus Jakarta Sans en todo (sin Instrument Serif ni Caveat en esta pantalla: una fuente menos que cargar).
- Ultravioleta `#8B5CF6` una vez: el rayo de la insignia del bloque cerrado del Club (el acceso al Club), con filo blanco. Ninguno en el registro, en el primer fotograma ni en la versión actual.
- Sin rojo: el error del registro en coral suave; el aviso de la versión actual, en ámbar suave.

**Propuesto (cómo se aplica aquí):**
| Elemento | v4 |
|---|---|
| Secciones | Cada sección entra en penumbra y **se enciende al entrar en pantalla** (luz desde arriba y línea de luz hielo en el borde superior; un solo movimiento por sección, `IntersectionObserver`). Con «reducir movimiento», todas encendidas desde el principio. |
| Titular | Mismo texto. Plus Jakarta 800, recortado (−0,035 em). **Un haz azul eléctrico recorre una vez «en un solo sitio»** (1,4 s) y deja debajo una línea de luz hielo. Sin animaciones en bucle. |
| Bloque de portada | Único sitio con **grano muy fino** (ruido SVG al 7 %, sin imagen externa). |
| Semana de ejemplo | Deja de ser un dibujo a lápiz: es una pantalla de la app bajo un foco (`#060C19`, filo hielo arriba). **Solo el martes lleva luz** (barra hielo con halo); el resto en azul apagado y el sábado de partido con un aro. Se quita la nota a mano. Sigue marcada «Ejemplo». |
| Funciones | Las 3 maquetas en `#060C19` con un solo elemento encendido cada una (semana 14, carga «Media», «12 tiros a puerta»). |
| Pasos | Números 1-2-3 en un aro con filo, en azul eléctrico; sin dorsales en serif. |
| Club cerrado | Insignia oscura con doble aro y el **rayo en ultravioleta**; «ya están dentro» en hielo; «¿Eres fundador? Entra y mira tu insignia» como enlace hielo (44 px de alto). |
| Registro | El panel `#060C19` iluminado desde arriba es lo único con luz; la portada detrás, en penumbra con desenfoque. Pestaña activa con línea azul eléctrico; campo con foco con halo. Mismo panel que en «Registro y entrada». |
| Objetos | Móvil boca abajo en «No hemos podido crear tu cuenta.» y móvil boca arriba con el aviso en «Revisa tu correo» (ilustraciones provisionales hasta tener foto propia o con licencia). |
| Primer fotograma | La misma maqueta con huecos en `#0C1323`, sin texto de campaña ni luces. |
| Fechas | Selector: con 10/12 · 11/12 (por confirmar), la portada vale desde el viernes 11/12 a las 00:00 y el Club dice «que se cerró el 10 de diciembre»; con el código, 28/11 y «27 de noviembre». En «Actual (hoy)», el primer fotograma enseña «Blackout Friday» con la fecha de cierre que toque. |

**Rendimiento:** sin imágenes externas, una sola familia de letra, una animación de entrada en el titular y transiciones de opacidad al hacer scroll. Nada en bucle.

**Textos:** ninguno cambia salvo la fecha del bloque del Club («que se cerró el 10 de diciembre», por confirmar). Se quita la nota decorativa «el martes, la más larga».

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
7. (v4) ¿Las secciones se encienden al hacer scroll o se ven todas encendidas desde el principio?
8. (v4) ¿Ultravioleta en el rayo de la insignia del Club cerrado, o portada pública sin ultravioleta?
9. (v4) ¿Foto propia o dibujo para los móviles del registro? Y la fecha del bloque del Club depende de que confirmes el 10/12 · 11/12 (hay que mover `BLACKOUT_FRIDAY_END` y el corte de la migración del 18/11 a la vez).
