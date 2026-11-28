# Ficha · Pantalla de espera y portada: bloque del Club Fundador

**Agente:** Irene (P1) · **Fecha:** 22/11/2026, rehecha en v4 el 23/11, cabecera móvil y sobres del día 0 el 24/11, banquillo y foco de cierre el 27/11 · **Tareas:** `exp-espera-club`, `irene-v4-paleta`, `t-20261124-p1-portada-movil`, `t-20261124-p1-sobres-dia0`, `t-20261127-p1-banquillo`, `t-20261127-p1-foco-cierre`
**Prototipo navegable:** https://claude.ai/artifact/DHjcLazBbp559Dfp5sbVZh (versión 7, sistema v4; pantallas «Espera (app)», «Portada (web)», «Cabecera móvil (web)», «Sobres del día 0 (app)», «Banquillo (app)» y «Foco de cierre (web y app)»; móvil 375 y escritorio; selector de estados; selector de fechas; casilla «Marcar lo propuesto»)
**Fuente del prototipo:** `agencia/experiencia/prototipos/club-fundador-espera.html`
**Base:** rama `revision/club-fundador` de proteamapp (PR #1): `access-gate-screen.tsx`, `founder/founder-section.tsx`, `founder/founder-landing.tsx`, `founder/founder-badge.tsx`, `founder/founder-welcome.tsx`, `lib/founder.ts`, `routes/index.tsx`.

## 0. Sistema v4 (23/11): qué cambia respecto a la versión del 22/11
Manda `agencia/sistema-v4/IDENTIDAD.md` y el apartado «La misma dirección en la web y la app» del documento de dirección audiovisual. El estilo v3 (papel blanco, tinta, lápiz) queda retirado en este prototipo. **Funciones, flujos, botones y textos no cambian**, salvo las fechas (abajo).

| Elemento | v3 (22/11) | v4 (23/11) |
|---|---|---|
| Fondo y capas | Papel blanco | `#02050F` de fondo; tarjetas en `#060C19`; bloque del Club en `#0C1323` (los tokens `--background`, `--card` y `--muted` del tema `.dark` de la app) |
| Tipografía | Manrope + Instrument Serif | Plus Jakarta Sans en todo (la de la app). En la portada web, «*Fundador*» en Instrument Serif cursiva como única voz puntual; en la app, solo jerarquía |
| Lo activo | Borde en tinta | **Luz**: el bloque del Club es el único iluminado (haz `#6AA8FF`→`#B9E0FF` desde arriba y filete de luz); bienvenida y cuenta atrás en penumbra. En la barra de pasos, el paso actual lleva la luz |
| Ultravioleta `#8B5CF6` | — | **Una vez por pantalla.** Espera sin verificar o rechazada: el botón «Conseguir mi insignia» (acceso al Club). Verificada: el rayo de la insignia (rayo ultravioleta sobre disco blanco), y el botón pasa a contorno. En revisión: ninguno (no hay acción). Portada: el rayo de la insignia grande; la del bloque de misterio va en azul |
| Insignia | Azul → `#16336f` | Misma geometría de `founder-badge.tsx`; degradado `#636DFF` → `#16205A`; apagada (gris al 35 %) hasta verificar |
| Hueco del número | Trazo a lápiz | Ranura vacía con línea discontinua que se **enciende** (blanco con halo hielo) al asignar el número |
| Estados vacío y error | Icono / texto | **Objeto real**: error al cargar con un móvil boca abajo sobre la mesa; portada fuera de campaña con una libreta de banquillo bajo un foco. En el prototipo son ilustraciones provisionales: en producto, foto propia o con licencia (Pau, biblioteca v4) |
| Rojo | Rojo de aviso | Sin rojo de alarma: errores en coral suave `#FF9B8F` sobre fondo tenue, solo para el mensaje |
| Movimiento | — | Solo el `founder-pop` existente al verificar y el esqueleto de carga; nada más (claridad y rendimiento) |

**Fechas (supuesto por confirmar, RELANZAMIENTO.md):** el prototipo enseña por defecto lista hasta el **jueves 10/12 a las 23:59** y apertura el **viernes 11/12**, con un selector para ver las del código actual (27/11 y 28/11). Textos que cambian si Biel lo confirma: «El 11 te abrimos la puerta.» · «Tu prueba gratuita de 3 meses empieza el 11 de diciembre a las 00:00.» · ventaja «Empiezan el 11 de diciembre.» · «3 meses gratis si te apuntas antes del 10 de diciembre a las 23:59.» · «La lista de espera se cerró el 10 de diciembre.» · cuenta atrás al 11/12 00:00. En código: `access-gate-screen.tsx`, `founder-landing.tsx`, `BLACKOUT_FRIDAY_END` y la migración de prueba (por PR, no lo toco).

**Arreglo del prototipo:** en la versión 2 los botones dentro de la ventana (cerrar, compartir, descargar) ya responden; en la 1 la ventana bloqueaba los clics.

## 0b. Cabecera de la portada en el móvil (24/11, propuesta P1 de Samuel)
Origen: `reports/embudo-2026-11-24.md` (apartado 3, P1). Datos de Samuel: el 82 % de las visitas de la semana entraron desde el móvil (245 de 298) y 298 visitantes dieron 33 cuentas (11 %). Base en código: `src/routes/index.tsx` (sección `sport-hero`) y `landing/blackout-friday.tsx` (`AuthButtons`, `BlackoutCountdown`). En el prototipo: pantalla «Cabecera móvil (web)», con «Propuesta» y «Actual (hoy)» y una línea discontinua donde acaba la primera pantalla (aprox.: 375×667 y 390×844 con las barras de Safari).

**Lo que se ve hoy en la primera pantalla del móvil (código):** «ProTeam» grande, «Hecho en el banquillo, no en una oficina.», «Blackout Friday», la frase de la oferta, la cuenta atrás gigante (text-5xl) y dos botones. En un móvil pequeño, «Iniciar sesión» queda en el borde y la cuenta atrás ocupa el centro: es lo que más pesa y no es una acción.

| Elemento | Propuesta | Estado |
|---|---|---|
| Barra de arriba | «ProTeam» a la izquierda y «Iniciar sesión» a la derecha (mismo enlace `?auth=login`) | Propuesta: «Iniciar sesión» sale de la pareja de botones para que quede uno solo |
| Línea pequeña | «Hecho en el banquillo, no en una oficina.» (texto actual) | Se conserva |
| Titular | «La lista se cierra el **jueves 10 de diciembre**.» La fecha en azul hielo; un haz recorre la fecha una vez (1,4 s; nada con «reducir movimiento») | Propuesta. Sustituye a «Blackout Friday» en la cabecera |
| Frase de misterio | «Lo que hay dentro se abre al día siguiente.» (de Samuel) | Propuesta |
| Botón | Uno solo, en blanco (la luz = lo activo), a todo el ancho, 54 px de alto. Texto: «Apúntate a la lista de espera» (el actual) o «Entrar en la lista» (Samuel); selector en el prototipo | Propuesta, decide Biel |
| Oferta | Sin línea de oferta en la primera pantalla (Samuel). Opción en el selector: «3 meses gratis si te apuntas antes del 10 de diciembre a las 23:59.» (texto ya aprobado del bloque del Club) | Decide Biel |
| Cuenta atrás | Debajo, con «Quedan», más pequeña y en penumbra (55 %); en un móvil pequeño queda fuera de la primera pantalla | Propuesta |
| Club Fundador y funciones | Bajan sin cambios (el Club con su rayo en ultravioleta) | Se conservan |
| Ultravioleta | Ninguno en la primera pantalla: lo activo es el botón y va en blanco. El ultravioleta sigue en el rayo del Club, más abajo | Propuesta |
| Textura | Grano muy fino solo en el bloque de cabecera (documento de dirección, «La misma dirección en la web y la app») | Propuesta |
| Escritorio | Misma cabecera centrada (titular a 60 px); la cuenta atrás asoma debajo | Propuesta |

**Estados del prototipo:**
- *Primera pantalla*: lo de arriba.
- *Primer fotograma (antes de cargar)*: la frase, la fecha y el botón ya vienen en el HTML (no dependen de la hora), así que se ven desde el primer instante; solo la cuenta atrás espera, con su hueco reservado para que nada salte (como hoy).
- *Error al abrir el registro*: si falla, mensaje dentro de la cabecera con el móvil boca abajo (objeto real provisional) en coral suave: «No hemos podido abrir el registro. Revisa tu conexión y vuelve a intentarlo.» Texto nuevo.
- *Vacío / lista cerrada*: desde el cierre la portada pasa a la rama fuera de campaña (`campaign=false`), que es otra ficha (`portada-fuera-campana.md`); esta cabecera no se ve.

**Textos nuevos (para `t()`):** «La lista se cierra el jueves 10 de diciembre.» · «Lo que hay dentro se abre al día siguiente.» · (opcional) «Entrar en la lista» · «No hemos podido abrir el registro. Revisa tu conexión y vuelve a intentarlo.». Con las fechas del código serían «…el viernes 27 de noviembre.» (el 27/11/2026 es viernes; el 10/12/2026, jueves).

**Componentes:** `src/routes/index.tsx` (sección `sport-hero`: orden, titular, un botón; la cuenta atrás baja), `landing/blackout-friday.tsx` (`AuthButtons` con variante de un botón, o el botón suelto; `BlackoutCountdown` con tamaño «sm» en penumbra), la cabecera pública para «Iniciar sesión». Sin cambios en registro, funciones de servidor ni base de datos. El `head.description` («Blackout Friday…») ya está anotado en `portada-fuera-campana.md`.

**Cómo se mide (Samuel):** cuentas nuevas ÷ visitantes de la portada cada martes y viernes, frente al 11 %. Hoy la web no registra el clic en el botón (apartado 4 del informe): si Biel quiere medir el clic, es una tarea para R1, no de diseño.

**Lo que no aparece:** número de apuntados, escasez o plazas, precio, nombre de Biel.

## 0c. Sobres del día 0 en la pantalla de espera (24/11, propuesta P3 de Samuel)
Origen: `reports/embudo-2026-11-24.md` (apartado 3, P3). Datos de Samuel: desde el 20/11 no entra nadie (sin Instagram), y ninguno de los 23 equipos de la lista tiene más de un miembro: es gente que se apuntó y no ha vuelto. La propuesta da un motivo para volver a la espera sin enseñar ninguna cifra. Base en código: `src/components/access-gate-screen.tsx` (rama `revision/club-fundador`, commit 5c7a6bd): bienvenida → cuenta atrás → `FounderSection`. En el prototipo: pantalla «Sobres del día 0 (app)», con selector de estado y de insignia (sin pedir / verificada).

**Confirmado (no cambia):** todo lo de la espera (bienvenida, bloque del Club con su flujo y sus estados, cuenta atrás y sus textos). Lo que va dentro de cada sobre ya existe o ya está aprobado: la insignia verificada y numerada (CLUB_FUNDADOR.md, ventaja 1, PR #1), las 4 plantillas de semana de `create-cycle-dialog.tsx` y la carta de bienvenida (ventaja 7, PR #1; en el plan, paso 2 del recorrido inicial).

| Elemento | Propuesta | Estado |
|---|---|---|
| Dónde | Sección nueva entre el bloque del Club y la cuenta atrás: «Lo que se abre el día 0» · «Lo que hay dentro, sobre a sobre.» · «Cada semana se abre uno. El último, el día que entras.» | Propuesta |
| Sobre 1 · «Tu insignia» | Se abre el **martes 1/12**. Dentro: la insignia del Club Fundador «verificada y con tu número. Ninguno se repite.» y «No hace falta esperar al día 0: se consigue ya, desde esta pantalla, compartiendo una historia.» → «Conseguir mi insignia» abre la ventana de siempre. Con la insignia en revisión: «Estamos revisando tu historia.»; verificada: «Ya es tuya. Tu número llegará muy pronto.» | Propuesta (contenido aprobado) |
| Sobre 2 · «Tu primera semana» | Se abre el **martes 8/12** (festivo). Dentro: «Planifica una semana. Solo una. El 11 eliges cuándo empieza y qué tipo de semana es. Después la llenas de sesiones desde la app.» y las 4 plantillas que ya existen (Semana de carga · Volumen alto; Semana de descarga · Reducir carga y recuperar; Semana competitiva · Preparar el partido; Semana de recuperación · Descanso activo) | Propuesta. Las plantillas existen; el paso «Tu primera semana» al entrar es propuesta del recorrido inicial (sin aprobar) |
| Sobre 3 · «Tu carta» | Se abre el **viernes 11/12, al entrar** (no se abre en la espera: es el paso «Carta» del recorrido inicial). Cerrado, al tocarlo: «Este sobre se abre el viernes 11, cuando entres.» | Propuesta |
| Línea de abajo | «El primer sobre se abre el martes 1 de diciembre.» → «Próximo sobre: martes 8 de diciembre.» → «El último se abre el viernes 11 de diciembre, cuando entres.» + «Te avisamos por correo.» (solo si Lucía envía el aviso) | Propuesta |
| Luz | Los sobres abiertos son lo activo: luz desde arriba, filo hielo y la hoja blanca asomando. El siguiente, solo un filo de luz y su número; los demás, en penumbra. El bloque del Club sigue siendo el más iluminado | Propuesta |
| Ultravioleta | Ninguno nuevo en la pantalla: sigue en el Club («Conseguir mi insignia» o el rayo verificado). Dentro del sobre 1 (ventana aparte), «Conseguir mi insignia» o el rayo verificado | Propuesta |
| Objetos reales | Sobres cerrados (sello con su número, no con el rayo: el rayo es solo del verificado); móvil boca abajo en el error. Ilustraciones provisionales | Propuesta |
| Movimiento | Al llegar el día de un sobre, la solapa se abre una vez (0,7 s); nada con «reducir movimiento» | Propuesta |
| Cómo se abren | Por fecha, en el navegador (hora de Madrid), con una lista fija de tres fechas. Sin servidor, base de datos ni migración | Propuesta |

**Estados del prototipo:** *Hoy (vacío)*: los tres cerrados y «El primer sobre se abre el martes 1 de diciembre.» · *Mar 1/12* y *mar 8/12*: uno y dos abiertos · *Cargando*: tres esqueletos (solo si la fecha viniera del servidor; con la fecha del navegador no hace falta) · *Error al abrir el sobre*: móvil boca abajo, «No hemos podido abrir el sobre» + «Revisa tu conexión y vuelve a intentarlo. Lo que había dentro sigue ahí.» + «Reintentar» · *Actual (hoy, sin sobres)*. Con las fechas del código (apertura el 28/11) la sección no sale: no queda ninguna semana; la propuesta depende de que Biel confirme el 11/12.

**Textos nuevos (para `t()`):** «Lo que se abre el día 0» · «Lo que hay dentro, sobre a sobre.» · «Cada semana se abre uno. El último, el día que entras.» · «Sobre {0}» · «Tu insignia» · «Tu primera semana» · «Tu carta» · «Se abre el {0}» · «Abierto · tócalo» · «El primer sobre se abre el {0}.» · «Próximo sobre: {0}.» · «El último se abre el viernes 11 de diciembre, cuando entres.» · «Te avisamos por correo.» · «Este sobre se abre el {0}.» · «Este sobre se abre el viernes 11, cuando entres.» · «La insignia del Club Fundador: verificada y con tu número. Ninguno se repite.» · «No hace falta esperar al día 0: se consigue ya, desde esta pantalla, compartiendo una historia.» · «Ya es tuya. Tu número llegará muy pronto.» · «Planifica una semana. Solo una.» (ya existe en el recorrido inicial) · «El 11 eliges cuándo empieza y qué tipo de semana es. Después la llenas de sesiones desde la app.» · «No hemos podido abrir el sobre» · «Revisa tu conexión y vuelve a intentarlo. Lo que había dentro sigue ahí.». Los nombres de las plantillas están hoy en catalán sin `t()` en `create-cycle-dialog.tsx` (ya anotado en `recorrido-inicial.md`).

**Componentes:** `access-gate-screen.tsx` (colocar la sección entre `FounderSection` y la cuenta atrás) y un componente nuevo `founder/day-zero-envelopes.tsx` con las tres fechas y sus contenidos; el sobre 1 reutiliza `FounderBadge` y abre el mismo diálogo de `FounderSection`. Sin cambios en `lib/founder.ts`, RPC ni base de datos.

**Dependencias (no son de diseño):** el aviso por correo de cada sobre es de Lucía (borrador, con el OK de Biel); medir las vueltas los días de sobre (visitas directas y desde Gmail) es de Samuel; construirlo, por PR de R1–R4.

**Lo que no aparece:** número de apuntados, escasez o plazas, precio, detalles de los tickets, nombre de Biel (la carta va cerrada; dentro de la app sí lo lleva, como hoy).

## 0d. «Tu banquillo no está completo» en la pantalla de espera (27/11, propuesta P4 de Samuel)
Origen: `reports/embudo-2026-11-27.md` (P4). Dato de Samuel: 0 de 24 equipos de la lista tienen más de un miembro y desde el 20/11 no entra nadie de fuera. La propuesta pide a quien ya está dentro que traiga a su cuerpo técnico, usando lo que ya existe para unirse a un equipo. En el prototipo: pantalla «Banquillo (app)», con selector de estado.

**Confirmado en el código (proteamapp, `main` 49f42a9 y rama `revision/club-fundador` 5c7a6bd):**
- Al crear el equipo ya se genera un código (`create_team_with_offer`, migración `20261118000500`), pero **solo sirve para jugadores** (`allowed_roles = ['player']`). Con ese código no puede entrar un 2.º entrenador como staff: no vale para esta tarjeta.
- Ya existe el «código de staff»: en `/coach/admin` → Códigos, el botón «Nou codi per a staff» llama a `createInviteCode` con `allowed_roles = [assistant_coach, fitness_coach, delegate, physio]` y `requires_approval = true` (solo el administrador del equipo).
- Quien lo usa entra por `/onboarding` → «Unirme con código» (`previewTeamCode` + `joinTeamWithCode`), elige su rol y queda **pendiente**; el administrador acepta o rechaza con `resolveJoinRequest` (lista con `listJoinRequests`).
- **Bloqueo hoy:** todo `/coach` (también `/coach/admin`) queda detrás de la pantalla de espera (`coach.tsx` → `AccessGateScreen`) hasta el día 0. Antes de abrir, el administrador no puede crear el código de staff ni aceptar a nadie desde la app.
- Qué ve quien entra antes de abrir: si es staff, al aceptar le lleva a `/coach` → la misma pantalla de espera (es la misma organización; `isAdmin` = falso). Esa pantalla ya enseña el Club a todo el que la ve (`FounderSection` sin condición).
- Aparte (para R1, no es de diseño): un **jugador** que entra con el código del equipo antes de abrir va a `/app`, que no tiene la pantalla de espera: entra en la app del jugador antes del día 0.

| Elemento | Propuesta | Estado |
|---|---|---|
| Dónde | Tarjeta nueva bajo el bloque del Club (antes de los sobres, si salen, y de la cuenta atrás). Solo para el administrador del equipo (`isAdmin`) | Propuesta |
| Textos | «Tu banquillo» · «Tu banquillo no está completo.» · «Tu banquillo entra contigo el día 0.»; con alguien dentro: «Entráis juntos el día 0.»; con los tres sitios: «Tu banquillo está completo.» · «Solo lo ve tu equipo.» | Propuesta |
| Sitios | Tres sitios del banquillo (objeto real, ilustración provisional): «Tú · Entrenador/a principal» encendido; «Sitio libre · 2.º entrenador/a» y «Sitio libre · Preparador/a físico/a» en penumbra. Delegado/a y fisioterapeuta también pueden entrar con el código (ocupan el sitio libre que toque; duda 18) | Propuesta |
| Botón | Uno solo, «Invitar a mi cuerpo técnico» (contorno, no compite con el Club). Abre una ventana con el código de staff; la primera vez lo crea (`createInviteCode` con los mismos parámetros que «Nou codi per a staff»), después enseña el mismo | Propuesta (función existente) |
| Ventana | «Invita a tu cuerpo técnico» · «Comparte este código con tu 2.º entrenador/a o tu preparador/a físico/a. Entra en el equipo cuando tú lo aceptes.» · «Código para tu cuerpo técnico» · «Compartir» (menú del móvil) y «Copiar código» · pasos «Comparte el código.» / «Crea su cuenta en ProTeam y elige «Unirme con código».» / «Tú aceptas su entrada desde esta pantalla.» · «Este código es solo para el cuerpo técnico (2.º entrenador/a, preparador/a físico/a, delegado/a o fisioterapeuta). El de tus jugadores es otro.» | Propuesta |
| Pide entrar | Su sitio pasa a filo de luz con «Laura · Pide entrar» y debajo «**Laura** quiere entrar como 2.º entrenador/a.» con «Aceptar» y «Rechazar» (`resolveJoinRequest`). Al aceptar, su sitio se enciende (0,9 s, nada con «reducir movimiento») y aviso «Laura ya está en tu banquillo.»; al rechazar, «Solicitud rechazada.» | Propuesta (función existente) |
| Quien entra | Ve la misma espera con «Estás en el banquillo de {equipo}.» · «Entráis juntos el día 0.», los sitios ocupados encendidos (él como «Tú») y sin botón | Propuesta |
| Luz y ultravioleta | Los sitios ocupados son lo activo (luz desde arriba y filo hielo); los libres, en penumbra; el que pide entrar, solo el filo. El Club sigue siendo el bloque más iluminado. Ningún ultravioleta nuevo: sigue en el Club | Propuesta |
| Cifras | Nunca el total de la lista ni de equipos: solo las personas de tu banquillo, con su nombre. Sin ventajas nuevas | Regla |

**Estados del prototipo:** *Solo tú (vacío)* · *Código ya creado* · *Laura pide entrar* · *Un sitio encendido* · *Banquillo completo* · *Lo que ve quien entra* · *Cargando* (tres esqueletos) · *Error al cargar el banquillo* (móvil boca abajo, «No hemos podido cargar tu banquillo» + «Revisa tu conexión y vuelve a intentarlo. Quien ya estaba dentro sigue dentro.» + «Reintentar») · *Error al crear el código* (en la ventana: «No hemos podido crear el código. Revisa tu conexión y vuelve a intentarlo.» + «Reintentar») · *Error al aceptar* («No hemos podido aceptar su entrada. Inténtalo de nuevo.») · *Actual (hoy, sin banquillo)*. Funciona igual con las dos fechas (10–11/12 o 27–28/11).

**Textos nuevos (para `t()`):** los de las filas de arriba. Los roles usan los nombres de `ROLE_LABELS` traducidos (hoy en catalán: «Entrenador/a assistent», «Preparador/a físic/a»); en el prototipo, «2.º entrenador/a» y «Preparador/a físico/a» (duda 17). Los mensajes de error de `loadCode` («Aquest codi no és vàlid.», etc.) están en catalán fijo: anotado para R4.

**Componentes:** `access-gate-screen.tsx` (colocar la tarjeta tras `FounderSection` cuando `isAdmin`) y un componente nuevo `founder/bench-card.tsx` que usa `listTeamMembers`, `listInviteCodes`/`createInviteCode`, `listJoinRequests` y `resolveJoinRequest`. Necesita el `teamId` del equipo (hoy la pantalla de espera solo recibe `organizationId`). Sin funciones de servidor, tablas ni migraciones nuevas. Construirlo, por PR de R1–R4.

**Medir (Samuel):** equipos de la lista con más de un miembro antes y después; clics en «Invitar a mi cuerpo técnico», códigos de staff creados y solicitudes aceptadas.

## 0e. Foco de cierre y la línea de lo que cambia al cerrar (27/11, propuestas P5 y P6 de Samuel; rehecho el 28/11 sin fechas)
Origen: `reports/embudo-2026-11-27.md` (P5 y P6). Dato de Samuel: la cuenta atrás es hoy lo más grande de la primera pantalla y desde el 20/11 no ha movido a nadie. En el prototipo: pantalla «Foco de cierre (web y app)», con «Dónde» (portada o espera), los campos de fecha que pone Biel, «Línea bajo el botón (solo si hay cierre)», «Botón y oferta» y el selector de estados.

**28/11 · rehecho tras la revisión de Álex.** `agencia/PLAN.md` (Biel, 27/11) manda: la Fase 1 no tiene fecha de fin y el paso a la Fase 2 lo decide Biel. Por eso el foco ya no lleva escrito el 10/12, el 11/12 ni «13 días»:
- Las fechas son un **dato que pone Biel**: campos «Cierre de la lista», «Desde (empieza la cuenta)» y «Apertura». En producto serían constantes que se rellenan el día que Biel active la Fase 2 (hoy, `BLACKOUT_FRIDAY_END` sigue en el 27/11 en el código).
- **Sin fecha**: en el titular sale un hueco «[fecha de cierre]», la puerta queda apagada y no se cuentan días («Sin fecha de cierre.» · «Mientras no haya cierre, la portada no cuenta días ni enseña el foco: se queda como en la Fase 1.»). En la espera, «Se abre el [fecha de apertura].» con la puerta apagada.
- Los estados ya no son «13 / 7 días» sino **«Recién empezada»**, **«A mitad del plazo»**, «Queda 1 día», «Último día», «Cerrada» y **«Sin fecha»**; sin fechas, los días salen como «Quedan N días» en un hueco; con fechas, se calculan.
- La luz se reparte entre «Desde» y el cierre (antes, el 23/11 fijo). Sin «Desde», el foco se queda a media luz.
- **P6 depende de que exista un cierre:** sin fecha de cierre, la línea no sale (en el prototipo se ve una nota: «Línea de P6 oculta: solo sale si hay fecha de cierre y Biel confirma 3 meses antes y 1 después.»).
- Prioridad baja: no hace falta hasta la Fase 2. Las demás pantallas de este prototipo (cabecera, sobres, portada) siguen con su selector 10–11/12 / 27–28/11; quitarles la fecha es otra tarea.

**Confirmado en el código (proteamapp, `main` 49f42a9 y rama `revision/club-fundador` 5c7a6bd):**
- Al crear el equipo ya se genera un código (`create_team_with_offer`, migración `20261118000500`), pero **solo sirve para jugadores** (`allowed_roles = ['player']`). Con ese código no puede entrar un 2.º entrenador como staff: no vale para esta tarjeta.
- Ya existe el «código de staff»: en `/coach/admin` → Códigos, el botón «Nou codi per a staff» llama a `createInviteCode` con `allowed_roles = [assistant_coach, fitness_coach, delegate, physio]` y `requires_approval = true` (solo el administrador del equipo).
- Quien lo usa entra por `/onboarding` → «Unirme con código» (`previewTeamCode` + `joinTeamWithCode`), elige su rol y queda **pendiente**; el administrador acepta o rechaza con `resolveJoinRequest` (lista con `listJoinRequests`).
- **Bloqueo hoy:** todo `/coach` (también `/coach/admin`) queda detrás de la pantalla de espera (`coach.tsx` → `AccessGateScreen`) hasta el día 0. Antes de abrir, el administrador no puede crear el código de staff ni aceptar a nadie desde la app.
- Qué ve quien entra antes de abrir: si es staff, al aceptar le lleva a `/coach` → la misma pantalla de espera (es la misma organización; `isAdmin` = falso). Esa pantalla ya enseña el Club a todo el que la ve (`FounderSection` sin condición).
- Aparte (para R1, no es de diseño): un **jugador** que entra con el código del equipo antes de abrir va a `/app`, que no tiene la pantalla de espera: entra en la app del jugador antes del día 0.

| Elemento | Propuesta | Estado |
|---|---|---|
| Dónde | Tarjeta nueva bajo el bloque del Club (antes de los sobres, si salen, y de la cuenta atrás). Solo para el administrador del equipo (`isAdmin`) | Propuesta |
| Textos | «Tu banquillo» · «Tu banquillo no está completo.» · «Tu banquillo entra contigo el día 0.»; con alguien dentro: «Entráis juntos el día 0.»; con los tres sitios: «Tu banquillo está completo.» · «Solo lo ve tu equipo.» | Propuesta |
| Sitios | Tres sitios del banquillo (objeto real, ilustración provisional): «Tú · Entrenador/a principal» encendido; «Sitio libre · 2.º entrenador/a» y «Sitio libre · Preparador/a físico/a» en penumbra. Delegado/a y fisioterapeuta también pueden entrar con el código (ocupan el sitio libre que toque; duda 18) | Propuesta |
| Botón | Uno solo, «Invitar a mi cuerpo técnico» (contorno, no compite con el Club). Abre una ventana con el código de staff; la primera vez lo crea (`createInviteCode` con los mismos parámetros que «Nou codi per a staff»), después enseña el mismo | Propuesta (función existente) |
| Ventana | «Invita a tu cuerpo técnico» · «Comparte este código con tu 2.º entrenador/a o tu preparador/a físico/a. Entra en el equipo cuando tú lo aceptes.» · «Código para tu cuerpo técnico» · «Compartir» (menú del móvil) y «Copiar código» · pasos «Comparte el código.» / «Crea su cuenta en ProTeam y elige «Unirme con código».» / «Tú aceptas su entrada desde esta pantalla.» · «Este código es solo para el cuerpo técnico (2.º entrenador/a, preparador/a físico/a, delegado/a o fisioterapeuta). El de tus jugadores es otro.» | Propuesta |
| Pide entrar | Su sitio pasa a filo de luz con «Laura · Pide entrar» y debajo «**Laura** quiere entrar como 2.º entrenador/a.» con «Aceptar» y «Rechazar» (`resolveJoinRequest`). Al aceptar, su sitio se enciende (0,9 s, nada con «reducir movimiento») y aviso «Laura ya está en tu banquillo.»; al rechazar, «Solicitud rechazada.» | Propuesta (función existente) |
| Quien entra | Ve la misma espera con «Estás en el banquillo de {equipo}.» · «Entráis juntos el día 0.», los sitios ocupados encendidos (él como «Tú») y sin botón | Propuesta |
| Luz y ultravioleta | Los sitios ocupados son lo activo (luz desde arriba y filo hielo); los libres, en penumbra; el que pide entrar, solo el filo. El Club sigue siendo el bloque más iluminado. Ningún ultravioleta nuevo: sigue en el Club | Propuesta |
| Cifras | Nunca el total de la lista ni de equipos: solo las personas de tu banquillo, con su nombre. Sin ventajas nuevas | Regla |

**Estados del prototipo:** *Solo tú (vacío)* · *Código ya creado* · *Laura pide entrar* · *Un sitio encendido* · *Banquillo completo* · *Lo que ve quien entra* · *Cargando* (tres esqueletos) · *Error al cargar el banquillo* (móvil boca abajo, «No hemos podido cargar tu banquillo» + «Revisa tu conexión y vuelve a intentarlo. Quien ya estaba dentro sigue dentro.» + «Reintentar») · *Error al crear el código* (en la ventana: «No hemos podido crear el código. Revisa tu conexión y vuelve a intentarlo.» + «Reintentar») · *Error al aceptar* («No hemos podido aceptar su entrada. Inténtalo de nuevo.») · *Actual (hoy, sin banquillo)*. Funciona igual con las dos fechas (10–11/12 o 27–28/11).

**Textos nuevos (para `t()`):** los de las filas de arriba. Los roles usan los nombres de `ROLE_LABELS` traducidos (hoy en catalán: «Entrenador/a assistent», «Preparador/a físic/a»); en el prototipo, «2.º entrenador/a» y «Preparador/a físico/a» (duda 17). Los mensajes de error de `loadCode` («Aquest codi no és vàlid.», etc.) están en catalán fijo: anotado para R4.

**Componentes:** `access-gate-screen.tsx` (colocar la tarjeta tras `FounderSection` cuando `isAdmin`) y un componente nuevo `founder/bench-card.tsx` que usa `listTeamMembers`, `listInviteCodes`/`createInviteCode`, `listJoinRequests` y `resolveJoinRequest`. Necesita el `teamId` del equipo (hoy la pantalla de espera solo recibe `organizationId`). Sin funciones de servidor, tablas ni migraciones nuevas. Construirlo, por PR de R1–R4.

**Medir (Samuel):** equipos de la lista con más de un miembro antes y después; clics en «Invitar a mi cuerpo técnico», códigos de staff creados y solicitudes aceptadas.

## 0e. Foco de cierre y la línea de lo que cambia al cerrar (27/11, propuestas P5 y P6 de Samuel)
Origen: `reports/embudo-2026-11-27.md` (P5 y P6). Dato de Samuel: la cuenta atrás es hoy lo más grande de la primera pantalla y desde el 20/11 no ha movido a nadie. En el prototipo: pantalla «Foco de cierre (web y app)», con «Dónde» (portada o espera), «Línea bajo el botón», «Botón y oferta», selector de estado y de fechas.

**Confirmado en el código (proteamapp `main` 49f42a9):**
- Portada: `BlackoutCountdown` (`landing/blackout-friday.tsx`) cuenta hasta `BLACKOUT_FRIDAY_END` (`lib/blackout-friday.ts`, hoy 27/11 23:59) en `text-5xl`–`text-8xl`; se actualiza cada segundo en el navegador y no carga nada del servidor.
- Espera: `access-gate-screen.tsx` cuenta hasta `startsAt` (la **apertura**, no el cierre), y solo aparece cuando llegan `now` y `startsAt`. Quien ve la espera ya está dentro: el cierre de la lista no le cambia nada.
- P6: la migración `20261118000500_prueba_1_mes_tras_lista.sql` da 3 meses desde la apertura al **primer equipo** creado antes del cierre y, después, `now() + interval '1 month'` («1 mes de prueba», que es el texto que ya usa la portada fuera de campaña). CLUB_FUNDADOR.md, ventaja 2: «3 meses gratis», «Sí, tal cual».

| Elemento | Propuesta | Estado |
|---|---|---|
| Portada: dónde | Sustituye a la cuenta atrás de números (en la cabecera móvil, el bloque «Quedan» en penumbra), bajo el botón. La cabecera (titular con la fecha, frase de misterio y un botón) no cambia | Propuesta |
| Portada: el foco | Una puerta de vestuario bajo un foco (objeto real, ilustración provisional). Cada día cae menos luz: el cono se estrecha y se apaga en proporción a los días que quedan. Debajo, en pequeño, «QUEDAN N DÍAS» / «QUEDA 1 DÍA»; «Se cierra el **{fecha de cierre}** a las 23:59.» y «Cuando se apague, la lista se cierra.». La luz se reparte entre «Desde» y el cierre, las dos fechas que pone Biel | Propuesta |
| Portada: el último día | Sin cono: solo el filo de luz bajo la puerta, que respira (2,4 s; quieto con «reducir movimiento»). «ÚLTIMO DÍA» · «Se cierra **hoy** a las 23:59.» | Propuesta |
| Portada: al cerrar | Foco apagado y «La lista se cerró el {fecha de cierre}.»; en producto la portada pasa a la de fuera de campaña (`campaign=false`, otra ficha) | Propuesta |
| P6: línea bajo el botón | «Hasta el cierre, **3 meses gratis** para tu primer equipo. Después, 1.» (Samuel). Variante en el selector: «…Después, 1 mes de prueba.» (más clara; usa el texto que la portada ya dice fuera de campaña). Sin precio, plazas ni cifras | Propuesta; **solo sale si hay fecha de cierre** y Biel confirma 3 meses antes y 1 después |
| Espera (app) | **Cambio de Irene sobre P5:** como la espera cuenta hasta la apertura y quien la ve ya está dentro, la luz va al revés: cada día hay más luz en la puerta y el último día la puerta está encendida. «FALTAN N DÍAS» · «Se abre el **{fecha de apertura}**.» · «Cada día hay más luz en la puerta. Cuando se encienda del todo, entras.»; último día: «Esta noche a las 00:00 se abre la puerta.». Va dentro de la tarjeta «Ya estás en la lista de espera», en lugar de los números; los textos de esa tarjeta no cambian | Propuesta, decide Biel (duda 21) |
| Luz y ultravioleta | La luz del foco es azul hielo y blanca, nunca ultravioleta; el ultravioleta sigue en el Club (una vez por pantalla). El titular conserva su haz | Propuesta |
| Accesibilidad | El foco es decorativo (`aria-hidden`); el bloque lleva `role="timer"` con «Quedan N días para el cierre de la lista: {fecha} a las 23:59» y se actualiza una vez por minuto, no por segundo | Propuesta |
| Rendimiento | Un SVG en línea de unos 2 kB que se calcula con la fecha del navegador (como hoy): sin imágenes, servidor ni base de datos. Una sola transición de 1,2 s en el cono | Propuesta |

**Estados del prototipo:** portada: *Hoy (con las fechas que pongas)* · *Recién empezada: mucha luz* · *A mitad del plazo* · *Queda 1 día* · *Último día: solo el filo* · *Lista cerrada: apagado* · *Sin fecha de cierre (Fase 1)* (puerta apagada, sin días y sin la línea de P6) · *Primer fotograma (antes de cargar)* · *Error al abrir el registro* (móvil boca abajo) · *Actual (hoy, cuenta atrás)*. Espera: *Hoy* · *Recién empezada: poca luz* · *A mitad del plazo* · *Falta 1 día* · *Último día: la puerta encendida* · *Sin fecha de apertura* · *Cargando la fecha* · *Error al cargar la fecha* («No hemos podido cargar la fecha. Revisa tu conexión y vuelve a intentarlo.» + «Reintentar») · *Actual*.

**Textos nuevos (para `t()`):** «Quedan {0} días» · «Queda 1 día» · «Último día» · «Se cierra el {0} a las 23:59.» · «Se cierra hoy a las 23:59.» · «Cuando se apague, la lista se cierra.» · «La lista se cerró el {0}.» · «Hasta el cierre, 3 meses gratis para tu primer equipo. Después, 1.» (o «Después, 1 mes de prueba.») · «Faltan {0} días» · «Falta 1 día» · «Se abre el {0}.» · «Cada día hay más luz en la puerta. Cuando se encienda del todo, entras.» · «Esta noche a las 00:00 se abre la puerta.» · «No hemos podido cargar la fecha. Revisa tu conexión y vuelve a intentarlo.».

**Componentes:** `landing/blackout-friday.tsx` (un `ClosingLight` nuevo junto a `BlackoutCountdown`, que recibe los días que quedan; la línea de P6 bajo `AuthButtons` solo en campaña), `src/routes/index.tsx` (cabecera), `access-gate-screen.tsx` (sustituir la rejilla de números por la versión de la espera, con estados de carga y error). El inicio de la cuenta («Desde») sería una constante junto a `BLACKOUT_FRIDAY_END`; las dos se rellenan cuando Biel ponga las fechas, y si no hay cierre el foco y la línea de P6 no se pintan. Sin servidor, tablas ni migraciones. Construirlo, por PR de R1–R4.

**Medir (Samuel):** cuentas nuevas ÷ visitantes de la portada (hoy 11 %) y vueltas a la portada de quien ya tiene cuenta, cada martes y viernes.

**Lo que no aparece:** número de apuntados, plazas, precio, nombre de Biel.

## 1. Qué se conserva (sin tocar)
- Flujo completo de la insignia: botón → ventana con 3 pasos → imagen `public/club-fundador/compartir.jpg` → «Compartir» (solo si `navigator.share` existe) y «Descargar imagen» → campo de usuario de Instagram → «Ya la he compartido» / «Actualizar solicitud» → RPC `request_founder_badge`.
- Estados `requested`, `verified`, `rejected` y sus textos actuales; normalización del @ (`normalizeInstagramHandle`); toast «¡Recibido! Revisamos tu historia y te avisamos.».
- Verificación manual desde `/admin`; el aviso «Pulsar «Compartir» no verifica la insignia: siempre comprobamos la historia.».
- Carta de bienvenida (`FounderWelcomeDialog`): se abre una vez al verificar y luego desde «Ver mi carta de bienvenida». Su diseño final va en el recorrido inicial (otra tarea).
- Insignia con **rayo** (`FounderBadge`), apagada hasta verificar y con `founder-pop` al verificarse. Número solo cuando está asignado (`founderNumberLabel`, «Nº 011»).
- Tarjeta de bienvenida y cuenta atrás de la espera con sus textos; cuenta atrás al 28/11 00:00.
- Portada: el bloque solo se ve en campaña (`campaign && <FounderLandingSection />`). Mismas 4 ventajas y la fila «Invitaciones para tus amigos · Muy pronto te contamos cómo funcionan.».

## 2. Qué cambia
### Pantalla de espera (`access-gate-screen.tsx` + `founder-section.tsx`)
| Cambio | Estado |
|---|---|
| Bloque del Club con más presencia: iluminado (v4), título en Plus Jakarta Sans 800 con «Club Fundador» en azul hielo, etiqueta «CLUB FUNDADOR» | Propuesta visual |
| **Hueco del número**: «FUNDADOR ___» vacío; se enciende con el número cuando se asigna | Propuesta |
| **Barra de 3 pasos** (Compartida → En revisión / Sin encontrar → Verificada con rayo) bajo el hueco | Propuesta |
| Botón principal en ultravioleta con rayo «Conseguir mi insignia» (antes ShieldCheck) | Propuesta |
| **Orden**: bienvenida → Club → cuenta atrás (hoy el Club va al final) | Propuesta, decide Biel |
| **Estado de carga**: esqueleto mientras llega `founder_members` (hoy no hay) | Propuesta |
| **Estado de error** al cargar la insignia: «No hemos podido cargar tu insignia» + «Reintentar» (hoy `member.error` no se trata) | Propuesta |
| Ventana: hoja inferior en móvil, diálogo centrado en escritorio; error de envío dentro de la ventana además del toast | Propuesta |

### Portada (`founder-landing.tsx`)
| Cambio | Estado |
|---|---|
| Ventajas en lista con filetes y rayo azul en vez de 4 tarjetas con iconos | Propuesta visual |
| Título grande «Club *Fundador*» y la frase «Tu insignia se consigue desde la lista de espera…» como nota con filete de luz | Propuesta visual |
| Bloque de misterio: «**No contamos cuántos somos.** Cada insignia lleva su número y ninguno se repite.» | Propuesta (expectación sin número de apuntados) |
| Botón «Apuntarme a la lista de espera» dentro del bloque (reutiliza `AuthButtons`) + «3 meses gratis si te apuntas antes del 27 de noviembre a las 23:59.» | Propuesta |
| Estado «lista cerrada» (si la portada siguiera visible tras el 27/11): «La lista de espera se cerró el 27 de noviembre. Si ya estás dentro, entra con tu cuenta para conseguir tu insignia.» | Propuesta |

## 3. Textos nuevos (todos para `t()` / i18n)
- «Fundador» · «Cada insignia lleva su número. Ninguno se repite.» · «Aquí aparecerá tu número cuando lo asignemos.» · «Tu número. Ninguno se repite.»
- «Compartida» · «En revisión» · «Sin encontrar» · «Verificada»
- «No hemos podido cargar tu insignia» · «Revisa tu conexión y vuelve a intentarlo. Tu solicitud, si la enviaste, sigue guardada.» · «Reintentar»
- Portada: «No contamos cuántos somos.» · «Cada insignia lleva su número y ninguno se repite.» · «Apuntarme a la lista de espera» · «3 meses gratis si te apuntas antes del 27 de noviembre a las 23:59.» · texto de lista cerrada (arriba).

## 4. Lo que NO aparece (a propósito)
- Número de apuntados (decisión de Biel: misterio).
- Precio fundador congelado: sin importe y sin existir en Stripe.
- Detalles de los 3 tickets regalo: condiciones cerradas pero sin construir; se mantiene solo «Muy pronto».
- Nombre de Biel en la portada (solo dentro, en la carta).
- Plazas limitadas o escasez.

## 5. Componentes afectados
`src/components/access-gate-screen.tsx` (orden), `src/components/founder/founder-section.tsx` (bloque, estados de carga y error, hueco del número, barra de pasos), `src/components/founder/founder-landing.tsx` (maquetación, misterio, botón), `src/styles.css` (haz de luz del bloque y ultravioleta `#8B5CF6` como token nuevo; `founder-pop` ya existe). Sin cambios en `lib/founder.ts`, RPC ni migración.

## 6. Dudas para Biel
0. **Fechas:** ¿confirmas lista hasta el 10/12 23:59 y apertura el 11/12? Sin eso, el prototipo enseña las dos versiones.
0b. **Tema:** ¿la espera y la portada pasan a modo oscuro por defecto? Hoy la app arranca en claro y el oscuro es opcional (se decide aparte).
1. **@ de Instagram:** `FOUNDER_INSTAGRAM` sigue en `app.proteam` (suspendida desde el 20/11). ¿Cuál es la cuenta provisional? Sin ella, la ventana pide mencionar una cuenta que no existe.
2. ¿Subimos el bloque del Club por encima de la cuenta atrás en la espera?
3. ¿Te vale la frase «No contamos cuántos somos.» como juego de misterio, o prefieres no mencionar el número en absoluto?
4. ¿Botón de registro dentro del bloque del Club en la portada, o solo los que ya hay arriba y abajo?
5. Hueco «Nº ___»: ¿cuándo empiezan a asignarse números (y los del 1 al 10)? Mientras no haya, los verificados verán «Aquí aparecerá tu número cuando lo asignemos.».
6. ¿Quién verifica mientras tanto? (hoy, tú).
7. **Cabecera móvil (24/11):** ¿una sola frase con la fecha y un solo botón en la primera pantalla del móvil, con «Iniciar sesión» arriba y la cuenta atrás debajo en penumbra?
8. ¿Botón «Apúntate a la lista de espera» (el actual) o «Entrar en la lista»?
9. ¿Sin la línea de «3 meses gratis» en la primera pantalla, o la dejamos bajo el botón? (Sin ella, la oferta aparece más abajo, en el Club.)
10. ¿Se deja de llamar «Blackout Friday» a la campaña ahora que el cierre es el 10/12? La cabecera nueva no lo nombra; la descripción para Google y la etiqueta de la cuenta atrás todavía sí.
11. **Sobres del día 0 (24/11):** ¿salen en la espera, entre el Club y la cuenta atrás? Solo tienen sentido con la apertura el 11/12.
12. ¿Este orden y estas fechas: 1 «Tu insignia» (mar 1/12), 2 «Tu primera semana» (mar 8/12, festivo) y 3 «Tu carta» (vie 11/12, al entrar)? ¿O el 8/12 pasa al miércoles 9?
13. El sobre 2 enseña el paso «Tu primera semana» del recorrido inicial, que aún no está aprobado: ¿lo enseñamos ya o cambiamos su contenido?
14. ¿Lucía avisa por correo de cada sobre? Si no, se quita «Te avisamos por correo.».
15. **Banquillo (27/11):** ¿sale la tarjeta «Tu banquillo no está completo» bajo el Club, solo para el administrador del equipo?
16. El código del equipo que ya existe solo vale para jugadores. ¿Usamos el código de staff (el de «Nou codi per a staff», con aprobación) y dejamos que el administrador lo cree y acepte desde la espera? Sin eso, nadie del cuerpo técnico puede entrar antes del día 0.
17. Nombres de los sitios: ¿«2.º entrenador/a» y «Preparador/a físico/a», o los de la app («Entrenador/a asistente», «Preparador/a físico/a»)?
18. ¿Delegado/a y fisioterapeuta también caben en el banquillo (el código lo permite) o la tarjeta solo invita a 2.º entrenador/a y preparador/a?
19. ¿El cuerpo técnico que entra antes de abrir también puede conseguir su insignia del Club, o la tarjeta debe decir que el Club es solo de quien se apuntó?
20. **Foco de cierre (27/11):** ¿la cuenta atrás de números pasa a ser el foco sobre la puerta en la portada, con los días en pequeño?
21. En la espera la cuenta atrás va a la apertura, no al cierre. ¿Te vale la luz al revés (la puerta se enciende) o la espera se queda con los números?
22. Cuando haya cierre (Fase 2), ¿sigue siendo 3 meses antes y 1 mes de prueba después? Sin cierre o sin eso, la línea de P6 no sale.
23. ¿«Después, 1.» (Samuel) o «Después, 1 mes de prueba.»?
24. **Fechas del foco (28/11):** cuando actives la Fase 2, ¿qué fecha de cierre, de apertura y desde cuándo cuenta la luz? Hasta entonces el foco no sale.
