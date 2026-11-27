# Ficha · Pantalla de espera y portada: bloque del Club Fundador

**Agente:** Irene (P1) · **Fecha:** 22/11/2026, rehecha en v4 el 23/11, cabecera móvil y sobres del día 0 el 24/11 · **Tareas:** `exp-espera-club`, `irene-v4-paleta`, `t-20261124-p1-portada-movil`, `t-20261124-p1-sobres-dia0`
**Prototipo navegable:** https://claude.ai/artifact/DHjcLazBbp559Dfp5sbVZh (versión 4, sistema v4; pantallas «Espera (app)», «Portada (web)», «Cabecera móvil (web)» y «Sobres del día 0 (app)»; móvil 375 y escritorio; selector de estados; selector de fechas; casilla «Marcar lo propuesto»)
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
