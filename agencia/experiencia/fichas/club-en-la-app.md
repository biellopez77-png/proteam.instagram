# Ficha · El Club Fundador dentro de la app (desde la apertura): dónde viven la insignia y la carta

**Agente:** Irene (P1) · **Fecha:** 23/11/2026, rehecha en v4 el 24/11 · **Tareas:** `exp-club-en-la-app`, `irene-v4-paleta` (abierta por Irene: no había tareas P1 pendientes ni comentarios de Biel o Álex en las 6 entregas en revisión; es el hueco que comparten el recorrido inicial, el verificado y la bienvenida diaria)
**Prototipo navegable:** https://claude.ai/artifact/6yL9QHeddHkjQhkwfmhuhY (versión 2, sistema v4; móvil 375 y escritorio; selectores «Versión: Propuesta / Actual tras la apertura», «Estado» con 8 estados, «Acceso: Pestaña / Pestaña + menú», «Fechas: 10/12–11/12 (por confirmar) / 27/11–28/11 (código)»; casilla «Marcar lo propuesto»; bajo el móvil, una línea explica dónde va el ultravioleta en cada estado). Copia local: `agencia/experiencia/prototipos/club-en-la-app.html`.
**Base:** rama `revision/club-fundador` de proteamapp (PR #1, commit 5c7a6bd): `routes/_authenticated/coach.admin.tsx` (pestañas de Configuración), `components/shell.tsx` (`COACH_MAIN`, `COACH_SECONDARY`), `components/founder/founder-section.tsx`, `founder-welcome.tsx`, `founder-badge.tsx`, `lib/founder.ts`, `components/access-gate-screen.tsx`.

**Por qué ahora:** con la apertura (vie 11/12 por confirmar; 28/11 en el código) la pantalla de espera deja de verse y con ella el único sitio donde viven el bloque del Club (`FounderSection`) y la carta (`FounderWelcomeDialog`). Las fichas del recorrido inicial y del verificado dicen «Tu insignia te espera en tu perfil» y «Ver mi carta de bienvenida… desde tu perfil», pero **el entrenador no tiene perfil**: `/app/profile` es del jugador; el menú del entrenador acaba en Progresión, Configuración y Facturación. Sin un sitio fijo, quien pida la insignia después de la apertura o quiera releer la carta no tiene dónde ir.

## 0. Sistema v4 (24/11): qué cambia respecto a la versión v3
Manda `agencia/sistema-v4/IDENTIDAD.md` y el apartado «La misma dirección en la web y la app» del documento de dirección audiovisual. **Funciones, flujos, llamadas y textos no cambian**; solo la piel y la fecha de referencia. El estilo v3 (papel, Instrument Serif, el hueco del número «a lápiz») queda retirado en este prototipo.

| Elemento | v3 | v4 |
|---|---|---|
| Fondo y capas | Papel blanco | Fondo `#02050F`; menú lateral, barra del móvil, tarjetas de Preferencias, filas de «Lo que tienes», ventanas y carta en `#060C19`; la cabecera del Club en `#0C1323` (tokens del tema `.dark` de la app) |
| Lo activo | Píldora azul en la pestaña, sombra en el menú | **Luz.** La pestaña elegida en `#636DFF` con filo hielo y halo; el elemento del menú elegido en `#0C1323` con filete de luz arriba; dentro de la pestaña del Club, **la cabecera con la insignia es lo único iluminado** (luz que cae desde arriba y filete hielo), en todos los estados con contenido; el campo de Instagram con halo eléctrico al enfocarlo |
| Tipografía | Instrument Serif + Manrope | Plus Jakarta Sans en todo (800 en títulos; cursiva 500 solo en «Biel · creador de ProTeam», bajo la firma) |
| **Ultravioleta `#8B5CF6`, una vez por pantalla** | — | **Verificada (con o sin número):** el rayo de la insignia, con filo blanco. **Sin pedir y rechazada:** el botón «Conseguir mi insignia» (el acceso al Club). **En las otras pestañas de Configuración:** el rayo de la pestaña «Club Fundador». **En revisión, cargando, error y quien no viene de la lista:** ninguno. Con la carta abierta, el ultravioleta pasa a la insignia de la carta y la de detrás se queda en blanco; el rayo del menú lateral (opción «Pestaña + menú») va siempre en hielo |
| Insignia | Roseta azul, rayo blanco; gris sin verificar | Sin verificar: roseta en penumbra (`#121B30`, borde hielo tenue) con el rayo apagado. Verificada: roseta `#636DFF` con halo y rayo ultravioleta (igual que en el verificado) |
| Hueco del número | «Nº ___» a lápiz, inclinado | «Nº» y una línea de luz hielo que se apaga hacia la derecha. Mismo texto |
| Estados | Error en tarjeta blanca; esqueleto gris | Error con **un móvil boca abajo** (ilustración provisional; en producto, foto propia o con licencia, Pau, biblioteca v4); esqueleto en penumbra sin luz. Motivo del rechazo y «Por repetir» en coral suave `#FF9B8F`, «En revisión» en ámbar suave `#E9C27A`; sin rojo |
| Quien no viene de la lista | Bloque «Aquí no falta nada.» dentro de la pantalla | La pantalla es exactamente Configuración con sus 3 pestañas; la explicación pasa a la nota del prototipo, fuera del móvil, para que no parezca un texto de la app |
| Fechas | 28/11 | «Tu prueba empezó el 11 de diciembre.» con las fechas nuevas (lista hasta el jue 10/12 23:59, apertura el vie 11/12, **por confirmar**, `RELANZAMIENTO.md`); con el selector en «código», «28 de noviembre», como hoy |
| «Ver en Facturación» | Sin acción | Aviso que explica que abre `/coach/billing`, que ya existe |

**Lo que no cambia con la paleta:** las 3 pestañas de Configuración y su contenido, el menú y la barra del móvil, los textos y botones de `FounderSection`, la ventana de solicitud del PR #1, la carta de `FounderWelcomeDialog` tal cual (el nombre de Biel solo ahí) y «Lo que tienes» con las mismas 4 ventajas + la carta.

## 1. Qué se conserva (sin tocar)
- **Configuración** con sus 3 pestañas («Preferencias personales», «Partidos y estadística», «Equipo»), su contenido y su orden.
- **Menú del entrenador** (`COACH_MAIN` y `COACH_SECONDARY`) y la barra inferior del móvil de 6 botones, tal cual.
- **`FounderSection`:** consulta `useFounderMember`, estados (`requested`, `verified`, `rejected`), textos de estado, botones «Conseguir mi insignia», «Ver mi solicitud» y «Ver mi carta de bienvenida», la ventana de los 3 pasos, «Compartir», «Descargar imagen», el formulario con `normalizeInstagramHandle` y `request_founder_badge`, los toasts y la nota «Pulsar «Compartir» no verifica la insignia…».
- **La carta** de `FounderWelcomeDialog` tal cual (título, 4 párrafos, firma animada, «Biel · creador de ProTeam», «Entrar») y `mark_founder_welcome_seen` al cerrarla. El nombre de Biel solo dentro de la carta.
- **`FounderBadge`** con el rayo y `founderNumberLabel`.
- Sin cambios en base de datos ni en funciones de servidor.

## 2. Qué cambia (propuesto)
| Propuesta | Por qué |
|---|---|
| **Pestaña «Club Fundador» en Configuración**, la cuarta, con el rayo, solo para quien tiene fila en `founder_members` o viene de la lista de espera | Es el sitio que ya existe para «lo mío» del entrenador. No añade un botón más al menú ni a la barra del móvil |
| **En el móvil, las pestañas pasan a 2 × 2** | Con 4 pestañas en fila, «Club Fundador» quedaría fuera de la pantalla a 375 px |
| **Cabecera del Club:** insignia grande (gris hasta verificar, azul con el rayo después), «ProTeam · Club Fundador», el título y la línea de estado de hoy, y el botón que toca según el estado | Reutiliza los textos y botones de `FounderSection` en una pantalla con aire, en vez de la tarjeta encajada de la espera |
| **Verificada sin número: hueco «Nº ___» a lápiz** | Igual que en la propuesta de la espera. Deja claro que el número llega sin decir cuándo ni cuántos hay |
| **Rechazada: motivo visible** («Motivo: … Súbela de nuevo con la pegatina @Mención.») | Depende de la propuesta del verificado (`review_note`). Si Biel no la aprueba, se queda la línea de hoy |
| **«Lo que tienes»**: solo las ventajas confirmadas y activas, cada una con su estado (Verificada / En revisión / Por repetir / Sin pedir; Activa; Activo; Tuya / Al verificar) | El Club promete reconocimiento y cercanía; hoy el fundador no ve en ningún sitio lo que tiene. Sin precio, sin tickets, sin número de apuntados |
| **«Leer mi carta»** dentro de «Lo que tienes» y «Ver mi carta de bienvenida» arriba | Para releerla cuando quiera. Responde a la duda 5 del recorrido inicial |
| **«Ver en Facturación»** en los 3 meses gratis | Enlaza a `/coach/billing`, que ya existe. No se calcula ninguna fecha aquí |
| **Estados de carga y error** (esqueleto; «No hemos podido cargar tu insignia.» · «Revisa tu conexión. Tu solicitud no se ha perdido.» · «Reintentar») | Hoy, si la consulta falla, el bloque se pinta como «sin solicitar» |
| **Quien no viene de la lista de espera: nada.** Configuración sigue con 3 pestañas; ni insignia apagada ni «te lo perdiste» | Nada de escasez ni de presión |
| **Opcional (selector «Acceso»):** «Club Fundador» con el rayo también en el menú lateral, debajo de Facturación (y en el menú del móvil) | Más a mano, a cambio de un elemento más en el menú. Se decide entre las dos |

La entrada desde el inicio (píldora del Club) está en la ficha de la bienvenida diaria: si se aprueba, la píldora abre esta pestaña.

## 3. Textos
- Pestaña: «Club Fundador».
- Cabecera: «ProTeam · Club Fundador» · «Eres del Club Fundador» / «Consigue tu insignia del Club Fundador» · estados de hoy: «Fundador {0}. Gracias por estar desde el principio.» · «Insignia verificada. Tu número llegará muy pronto.» · «Estamos revisando tu historia.» · «No hemos encontrado tu historia con la mención. Puedes volver a intentarlo.» · «Comparte una historia, menciónanos y entra en el Club Fundador.» · hueco «Nº ___».
- Rechazo (si se aprueba el motivo): «Motivo: {0}» · «Súbela de nuevo con la pegatina @Mención.»
- «Lo que tienes» · «Por estar desde el principio. Solo lo que ya funciona.»
  - «Insignia verificada y numerada» · «Con el rayo y, cuando llegue, tu número.» / «La consigues compartiendo una historia que nos mencione. La revisamos a mano, una a una.» · «Verificada» · «En revisión» · «Por repetir» · «Sin pedir».
  - «3 meses gratis» · «Tu prueba empezó el {fecha de apertura} (11 de diciembre por confirmar; 28 de noviembre en el código). No se cobra nada hasta que acaben los 3 meses y puedes cancelar antes.» · «Ver en Facturación» · «Activa».
  - «Una persona del equipo te acompaña» · «Durante tus 3 meses, escríbenos por correo y te contesta una persona, de tú a tú.» · [dirección de correo pendiente] · «Activo».
  - «Votas en lo que construimos» · «Te llegan las votaciones por correo, en la web y en Instagram.» · «Activo».
  - «Tu carta de bienvenida» · «Para volver a leerla cuando quieras.» / «Se abre cuando tu insignia esté verificada.» · «Leer mi carta» · «Tuya» · «Al verificar».
- Error: «No hemos podido cargar tu insignia.» · «Revisa tu conexión. Tu solicitud no se ha perdido.» · «Reintentar».
- Todos los textos nuevos van con `t()` y en los 7 idiomas (regla del escáner i18n de `AGENTS.md`).

## 4. Fuera a propósito
Número de apuntados o cualquier recuento; precio fundador congelado (sin importe y sin forma de guardarlo en Stripe: entra en «Lo que tienes» solo cuando exista); tickets regalo (sin construir); nombre de Biel fuera de la carta; «plazas», «últimos» o escasez; promesas sobre lo que cambia cada voto o sobre plazos de verificación.

## 5. Componentes afectados (para R1–R4)
- `src/routes/_authenticated/coach.admin.tsx`: cuarta pestaña `founder` en la lista de pestañas, visible solo si `useFounderMember` devuelve fila (o según la regla de la duda 1); `section === "founder"` pinta el nuevo `FounderPanel`. Pestañas en 2 × 2 por debajo de `sm`.
- Nuevo `src/components/founder/founder-panel.tsx`: cabecera + «Lo que tienes»; reutiliza `FounderBadge`, `founderNumberLabel`, `FounderWelcomeDialog` y la ventana de solicitud. **Sacar la ventana y el formulario de `founder-section.tsx` a un componente compartido** (ya lo pedía la ficha del recorrido inicial) para no duplicar la lógica.
- `founder-section.tsx`: añadir el estado de error (`member.isError`) y el de carga, que hoy no existen; vale para la espera y para el panel.
- `src/components/shell.tsx`: solo si se elige «Pestaña + menú», un elemento en `COACH_SECONDARY` que lleve a `/coach/admin` con la pestaña del Club abierta (p. ej. `?section=founder`; hoy la pestaña vive en un `useState`, habría que leerla de la búsqueda de la ruta).
- `src/lib/i18n/dict/*.json`: los textos nuevos en los 7 idiomas.
- Depende de fusionar el PR #1 y de aplicar su migración.

## 6. Dudas para Biel
1. **¿Quién ve la pestaña?** ¿Solo quien ya tiene fila en `founder_members` (ha pedido la insignia) o todo el que estaba en la lista de espera? Lo segundo necesita saber quién estaba en la lista (misma duda 1 del recorrido inicial).
2. **¿Se puede pedir la insignia después de la apertura (11/12 por confirmar; 28/11 en el código)?** Si sí, «Conseguir mi insignia» sigue en la pestaña; si no, quien no la pidió solo vería las demás ventajas.
3. **¿Pestaña en Configuración, o también en el menú?** (selector «Acceso» del prototipo).
4. **¿Qué correo enseñamos para el soporte de tú a tú?** Lucía atiende por Gmail; hace falta la dirección que quieres que se vea.
5. **¿«Lo que tienes» te vale con estas 4 ventajas + la carta?** El precio congelado y los tickets entrarán cuando existan.
6. Sigue pendiente el **@ provisional** de Instagram (`FOUNDER_INSTAGRAM` sigue en `app.proteam`, suspendida): afecta a la ventana de solicitud.
7. **(v4) ¿Ultravioleta en el botón «Conseguir mi insignia» dentro de la app?** Lo he puesto como el acceso al Club, igual que en la pantalla de espera. La alternativa es dejarlo en `#636DFF` y reservar el ultravioleta solo para el rayo verificado.
8. **(v4) Objetos reales:** el móvil boca abajo del error es un dibujo provisional; ¿foto propia o dibujo para los estados de la app? (misma duda que en onboarding y verificado).
