# Ficha · Onboarding (crear o unirse a un equipo): la puerta del día de apertura

**Agente:** Irene (P1) · **Fecha:** 23/11/2026, rehecha en v4 el 23/11 · **Tareas:** `exp-onboarding`, `irene-v4-paleta` (abierta por Irene, prioridad alta: no había tareas P1 pendientes ni comentarios de Biel o Álex en las 8 entregas; el onboarding es un entregable del PLAN que el recorrido inicial dejaba «tal cual»)
**Prototipo navegable:** https://claude.ai/artifact/L2T7StVAojsJDH2sNbXh6H (versión 3 del 24/11 con la propuesta P2 «Cuenta sin equipo», selectores nuevos «Pantalla: /onboarding / Mi cuenta (web)» y «Cuenta sin equipo (P2): Club apagado / Sin bloque»; versión 2, sistema v4; móvil 375 y escritorio; selectores «Versión: Propuesta / Actual (hoy)», «Fechas: 10/12 · 11/12 (por confirmar) / 27/11 · 28/11 (código hoy)», «Cuándo llega: antes del cierre de la lista / desde la apertura», «Quién: primer equipo / ya tiene equipo», «Simular: todo bien / carga lenta / error del servidor / código no válido / unirse pide aprobación»; casilla «Marcar lo propuesto»). Copia local: `agencia/experiencia/prototipos/onboarding.html`.
**Base leída:** rama `revision/club-fundador` de proteamapp (5c7a6bd): `src/routes/_authenticated/onboarding.tsx` (`OnboardingPage`, `JoinWithCode`, `SportPicker`, `VariantPicker`, `CreateTeam`, `RedeemLicense`, `Field`), `lib/teams.functions.ts`, `lib/teams.ts` (`ROLE_SHORT`), `lib/activation-codes.functions.ts`, `lib/public-account.functions.ts` (`eligibleForFirstTeamOffer`), `lib/sport-config/*.ts`, `lib/blackout-friday.ts` (`BLACKOUT_FRIDAY_END`), `lib/i18n/dict/es.json`, migración `20261118000500_prueba_1_mes_tras_lista.sql`.

**Por qué ahora:** sin equipo no se entra en la app, así que el día de apertura (28/11 en el código; 11/12 por confirmar) todo entrenador nuevo pasa por esta pantalla. Hoy tiene tres problemas que se notan el Día 0:
1. **Promete algo que ya no es verdad.** El bloque «3 meses gratis para tu primer equipo» sale a cualquiera sin organización (`eligibleForFirstTeamOffer`), sin mirar la fecha. Pero la migración del 18/11 (decisión de Biel) da 3 meses solo a quien crea su primer equipo antes del 27/11 a las 23:59, y **1 mes** a quien lo crea después. Desde el 28/11 la pantalla promete 3 meses y la base de datos da 1.
2. **Sale en catalán.** `SportPicker`, `VariantPicker`, `CreateTeam` y su éxito tienen los textos escritos sin `t()`: «Quin esport practica el teu equip?», «Crear equip», «Nom de l'equip», «Creant…», «Equip creat», «Entrar al panell», «Tornar», «Canviar»… Además `handball.ts` tiene `displayName: "Handbol"` y la descripción en catalán, y el rol «Assistent» no tiene traducción en `es.json`. Las claves en español ya existen en `es.json` (salvo «Assistent»).
3. **Los errores solo viven en un aviso que desaparece.** Crear equipo muestra `err.message` sin traducir (sale «No s'ha pogut crear l'equip.»), y ningún formulario dice qué campo falla.


## 0. Sistema v4 (23/11): qué cambia respecto a la versión v3
Manda `agencia/sistema-v4/IDENTIDAD.md` y el apartado «La misma dirección en la web y la app» del documento de dirección audiovisual. **Funciones, flujos, campos, llamadas y textos no cambian**; solo la piel y las fechas. El estilo v3 (papel, «Empezamos» en Instrument Serif con trazo a lápiz, oferta como nota de papel, pasos a lápiz) queda retirado en este prototipo.

| Elemento | v3 | v4 |
|---|---|---|
| Fondo y capas | Papel blanco | Fondo `#02050F`; filas, campos y tarjetas en `#060C19`; bloque de la oferta en `#0C1323` (tokens `--background`, `--card` y `--muted` del tema `.dark` de la app) |
| Lo activo | Raya azul a lápiz | **Luz.** En el menú, el bloque de la oferta es lo único iluminado (haz `#6AA8FF`→`#B9E0FF` desde arriba y filete de luz en el borde); las tres vías quedan en penumbra y se encienden al pasar (degradado tenue y título en hielo). En crear: el paso actual lleva un punto de luz hielo; el campo con foco, borde eléctrico con halo; el rol elegido al unirse, borde y halo eléctricos; en el éxito, el código del equipo en una caja con halo hielo |
| Tipografía | Instrument Serif + Manrope | Plus Jakarta Sans en todo (800 en títulos; «3 meses» / «1 mes» en azul hielo `#B9E0FF`). Sin voz serif: es pantalla de app |
| Acción | Azul `#2F6BFF` | Botón principal `#636DFF`; secundario en contorno; enlaces en `#6AA8FF` |
| Ultravioleta `#8B5CF6` | — | **Ninguno**: aquí no hay rayo del verificado ni acceso al Club (el Club vive en el recorrido inicial y en Configuración) |
| Campos de cada deporte | Rectángulo a lápiz | El mismo campo a escala real, en líneas de luz tenue (`#6F7A91`) que se encienden en eléctrico al pasar y en la ficha del deporte elegido |
| Objetos reales | — | Éxito al crear: **un peto bajo el foco** sobre el código del equipo. Error del servidor al crear o al comprobar el código, y oferta que no carga: **móvil boca abajo** sobre la mesa. Ilustraciones provisionales: en producto, foto propia o con licencia (Pau, biblioteca v4). «Código no válido» no lleva objeto: no es un fallo de conexión |
| Error y éxito | Rojo y verde | Sin rojo de alarma ni verde: errores en coral suave `#FF9B8F` (título del aviso y borde del campo); «Tu prueba gratis dura hasta el…» con un punto de luz hielo |
| Catalán en «Actual (hoy)» | Ámbar sobre papel | Ámbar suave `#E9C27A` sobre la misma paleta oscura |
| Movimiento | Trazo que se dibuja | Ninguno salvo el giro de carga y el esqueleto de la oferta (claridad y rendimiento) |
| «Actual (hoy)» | En papel | En la misma paleta oscura, para comparar estructura y textos, no estilo |

**Textos:** no cambia ninguno por el v4; solo la fecha dentro de los textos propuestos (abajo).

**Fechas (supuesto por confirmar, `agencia/sistema-v4/RELANZAMIENTO.md`):**
- Con 10/12 · 11/12: «Cuándo llega» pasa a «Antes del 10/12 23:59» / «Desde el 11/12»; la línea de la oferta dice «Cuentan desde el 11 de diciembre.»; el fin de prueba de ejemplo pasa a «11 de marzo de 2027» (3 meses desde la apertura) o «11 de enero de 2027» (1 mes, equipo creado el día de apertura).
- Con 27/11 · 28/11 (lo que hay hoy en el código y en la migración del 18/11): «Cuentan desde el 28 de noviembre.», 28/02/2027 y 28/12/2026, como en la versión v3.
- El corte lo deciden `BLACKOUT_FRIDAY_END` (pantalla) y la migración `20261118000500_prueba_1_mes_tras_lista.sql` (base de datos). **Si se mueve la fecha hay que moverla en los dos sitios a la vez**, o la pantalla y la base de datos volverán a decir cosas distintas (ver duda 6). No lo toco: va por PR del equipo técnico.

## 0b. Cuenta sin equipo: «Te falta un paso para guardar tu sitio» (24/11, propuesta P2 de Samuel · tarea `t-20261124-p1-cuenta-sin-equipo`)

**Por qué:** en el embudo del 24/11 (`reports/embudo-2026-11-24.md`), 9 de 33 cuentas (27 %) dieron su correo y no crearon el equipo, así que no están en la lista. Es la gente que ya tenemos y la más fácil de recuperar.

**Confirmado (código, rama `revision/club-fundador`, 5c7a6bd):**
- Una cuenta sin equipo llega a **`/onboarding`**: es el `destination` de `getPublicAccountSummary` con 0 equipos (`lib/public-account.functions.ts`), y `/teams` sin equipos redirige aquí (`routes/_authenticated/teams.tsx`). Desde la web llega también a **«Mi cuenta»** (`components/public-account-panel.tsx`), que hoy le enseña la oferta, «Todavía no perteneces a ningún equipo.» y «Crear o unirme a un equipo». Coincide con la analítica de Samuel; R1 puede confirmarlo con datos si hace falta.
- Sin equipo no hay lista: la portada ya lo dice («Crea tu cuenta y tu equipo. Entras en la lista de espera.», `routes/index.tsx`) y la pantalla de espera (`AccessGateScreen`, con el bloque del Club `FounderSection`) solo sale dentro de `/coach`, que exige equipo. **Hoy una cuenta sin equipo no ve el Club en ningún sitio.**
- La insignia apagada ya existe: `FounderBadge` con `muted` (gris al 35 %, rayo blanco).

**Propuesto (marcado en el prototipo):**
| Dónde | Qué |
|---|---|
| `/onboarding`, menú, con la lista abierta y `eligibleForFirstTeamOffer` | El bloque de la oferta pasa a ser el del **Club apagado**: insignia en gris (como está diseñada), «Te falta un paso para guardar tu sitio», dos puntos «Cuenta · Equipo» con «Cuenta» hecho y la luz hielo (con un pulso lento) en «Equipo», debajo la oferta de siempre en pequeño («3 meses gratis para tu primer equipo», el texto actual y «Cuentan desde el {día de apertura}.») y **un solo botón «Crear mi equipo»**, que hace lo mismo que hoy «Crear mi primer equipo» (va a elegir deporte). Las tres vías de abajo no cambian. |
| Éxito al crear el equipo | Bajo «Copiar código», la insignia **se enciende** (de gris a azul de la app, 1,1 s; quieta con «reducir movimiento») junto a «Ya estás en la lista de espera» (texto que ya existe en la pantalla de espera). El peto se queda. |
| «Mi cuenta» en la web | El mismo bloque del Club apagado en lugar del bloque de la oferta, con «Crear mi equipo» → `/onboarding`. Se conservan «Tus equipos», «Todavía no perteneces a ningún equipo.», «¿Quieres crear tu equipo?», «Crear o unirme a un equipo», «Entrar en la aplicación» y «Cerrar sesión». |
| Cuándo no sale | Desde la apertura (ya no hay lista: vuelve la oferta de 1 mes de la versión v4), con «Ya tiene equipo», mientras carga (esqueleto) y si falla la carga (el móvil boca abajo con el aviso de siempre). |

- **Luz:** en el menú el bloque sigue siendo lo único iluminado; dentro, la insignia está apagada y la luz cae en el paso que falta y en el botón. Al crear, la luz pasa a la insignia.
- **Ultravioleta:** ninguno. La insignia aún no está pedida ni verificada; el ultravioleta llega después, en la pantalla de espera («Conseguir mi insignia»), como en la ficha `espera-y-portada-club-fundador.md`.
- **Estados en el prototipo:** menú (lista abierta / desde la apertura), crear → éxito con la insignia encendida, «Mi cuenta» sin equipo y con equipo, carga lenta, error del servidor; vacío = la propia cuenta sin equipos. Móvil 375 y escritorio.
- **Textos nuevos:** «Te falta un paso para guardar tu sitio» · «Cuenta» · «Equipo» · «Crear mi equipo» (los tres primeros, con su traducción en los 7 idiomas de `lib/i18n/dict/`). Reutilizados: «Ya estás en la lista de espera» y todos los de la oferta.
- **Componentes:** `routes/_authenticated/onboarding.tsx` (bloque de la oferta y éxito de `CreateTeam`), `components/public-account-panel.tsx` (bloque `eligibleForFirstTeamOffer`), `components/founder/founder-badge.tsx` (solo se usa, con `muted`). El corte «lista abierta» es el mismo `BLACKOUT_FRIDAY_END` de la duda 1. **Sin cambios** en servidor, base de datos ni flujos.
- **Cómo se mide (Samuel):** cuentas sin equipo (hoy 9) y cuántas crean el equipo después; el clic en «Crear mi equipo» lo mediría R1.

**Dudas para Biel (P2):**
8. ¿Sale el Club apagado a quien tiene cuenta y no equipo? Es propuesta de Samuel; decides tú.
9. Botón: «Crear mi equipo» (Samuel) o «Crear mi primer equipo» (el de hoy).
10. ¿Lo ve también quien viene a **unirse** con un código (un jugador o un ayudante)? Hoy `eligibleForFirstTeamOffer` no distingue: lo vería cualquiera sin equipo. Si no, haría falta saber a qué viene antes de enseñarlo.
11. ¿Va también en «Mi cuenta» de la web o solo en `/onboarding`?

## 1. Qué se conserva (sin tocar)
- **Las cuatro vías y su orden:** bloque de oferta con «Crear mi primer equipo» (solo si `eligibleForFirstTeamOffer`), «Unirme con código», «Crear equipo», «Canjear código de activación».
- **Unirse:** comprobar código → vista previa del equipo (nombre · deporte · categoría · temporada) → «Entro como» si hay más de un rol → «Entrar en el equipo» → `selectTeam` y a `/coach` o `/app`; si pide aprobación, «Solicitud enviada» con «Ir a mis equipos». Botón desactivado con menos de 4 caracteres.
- **Crear:** deporte → modalidad (solo fútbol: Fútbol / Fútbol 7) → nombre, categoría, temporada (`currentSeason()`) → código → «Entrar al panel». Mismo `createTeam` con `sport_type` y `sport_code`.
- **Canjear:** código `PT-XXXX-XXXX-XXXX`, nombre del equipo si el código permite crearlo, categoría, temporada → `redeemActivationCode` → «Licencia activada.» y a `/teams`.
- **Funciones de servidor y base de datos, sin cambios.** La oferta la decide la base de datos al crear el equipo; la pantalla solo tiene que contarlo bien.
- Todos los textos en español que ya existen (los de `es.json`), incluidos «Crea tu primer equipo y disfruta de acceso completo durante tres meses, sin pagar al crearlo.» y los subtítulos de las opciones.

## 2. Qué cambia (propuesto)
| Cambio | Detalle |
|---|---|
| **Textos en español (arreglo, no diseño)** | Pasar por `t()` todo lo de `SportPicker`, `VariantPicker`, `CreateTeam` y su éxito; `config.displayName` y `config.shortDescription` también por `t()` (o corregir `handball.ts`); añadir «Assistent» → «Asistente» en `es.json`; traducir `err.message` en `CreateTeam` como ya hace `JoinWithCode`. **Se puede hacer antes del 28/11 aunque no se haga nada más.** |
| **Oferta según la fecha (arreglo para la apertura)** | Antes del cierre de la lista (hoy en el código, 27/11 23:59; por confirmar, 10/12 23:59): «3 meses gratis» + texto actual + «Cuentan desde el {día de apertura}.» Desde la apertura: «1 mes gratis para tu primer equipo» + «Crea tu primer equipo y prueba la app completa durante un mes, sin pagar al crearlo.» Ver la duda 1 sobre de dónde sale la fecha. |
| **Fin de la prueba en el éxito** | `createTeam` ya devuelve `trialEndsAt` y no se enseña. Tras crear el primer equipo: «Tu prueba gratis dura hasta el {fecha}.» (3 meses desde la apertura para la lista: 28/02/2027 con el código de hoy, 11/03/2027 si la apertura pasa al 11/12; un mes después de crear el equipo para el resto). |
| **«Copiar código»** | Bajo el código del equipo, como en la ficha del recorrido inicial. Toast «Código copiado». Más «Podrás ver el código cuando quieras en Configuración → Equipo.» |
| **Pasos** | En crear: «Deporte — Modalidad — Datos» (o «Deporte — Datos» si no es fútbol); hechos en gris claro y el actual con su punto de luz. |
| **Deportes con su campo dibujado** | Cada deporte con su campo a escala de sus medidas reales (105 × 68, 28 × 15, 40 × 20, 65 × 45), en líneas de luz. Filas con línea fina, no tarjetas. |
| **Errores dentro del formulario** | Debajo del campo: «Escribe el nombre del equipo.» · «Escribe la temporada como 2026-27.» Caja de error encima del botón (además del toast): ver textos. |
| **Ayuda en el código** | «Lo encuentras en el mensaje que te ha enviado tu club o tu entrenador.»; ejemplo con el formato real (`NOMBRE-8 caracteres`, p. ej. «ALEVINB-4F7A21C9») en vez de «EQUIP-XXXX»; «Escribe al menos 4 caracteres para comprobarlo.» mientras el botón está desactivado. |
| **Carga y error de la oferta** | Carga: tres rayas de esqueleto en el sitio del bloque (hoy aparece de golpe y empuja las opciones). Error: «No hemos podido comprobar tu oferta ahora. Puedes crear el equipo igualmente: la oferta se aplica sola al crearlo.» (cierto: la decide la base de datos). |
| **Estilo v4** (sustituye al v3) | Ver apartado 0: oferta iluminada como lo único activo del menú, vías en penumbra, pasos con luz, peto con el código al crear, móvil boca abajo en los errores de conexión, sin ultravioleta. Escritorio: la misma columna centrada de hoy (máx. 448 px). |

## 3. Textos (es)
**Existentes, se conservan:** «Empezamos» · «Para entrar en la app necesitas formar parte de un equipo.» · «3 meses gratis para tu primer equipo» · «Crea tu primer equipo y disfruta de acceso completo durante tres meses, sin pagar al crearlo.» · «Crear mi primer equipo» · «Unirme con código» · «Introduce el código que te ha dado tu club o entrenador. Si requiere aprobación, la revisarán.» · «Crear equipo» · «Crea tu equipo, invita a los jugadores y elige después el plan mensual o anual.» · «Canjear código de activación» · «Código de equipo» · «Comprobar código» · «Comprobando…» · «Entro como» · «Entrar en el equipo» · «Entrando…» · «¡Ya estás en el equipo!» · «Solicitud enviada» · «El equipo revisará tu solicitud. Cuando la aprueben podrás entrar desde «Mis equipos».» · «Ir a mis equipos» · «Volver» · «¿Qué deporte practica tu equipo?» · «Elige el deporte antes de crear el equipo. Podrás cambiarlo después desde la configuración.» · «¿Qué modalidad juega el equipo?» · «La modalidad define el campo, las posiciones, las alineaciones y las estadísticas de todo el equipo.» · «Balonmano» · «Pista de 40 × 20 m, dos partes y siete jugadores en pista.» · «Cambiar» · «Nombre del equipo» · «Categoría» · «Temporada» · «Creando…» · «¡Equipo creado!» · «Equipo creado» · «Comparte este código con tus jugadores:» · «Entrar al panel» · «Código» · «Nombre del equipo, si el código permite crearlo» · «Activar licencia» · «Validando…» · «Licencia activada.» · «Este código no es válido.» · «Este código ha caducado.» · «Este código ha llegado al límite de usos.» · «No se ha podido validar el código.»

**Nuevos (propuestos):**
- Oferta: «Para tu primer equipo» · «Cuentan desde el 11 de diciembre.» (o «…28 de noviembre.» si no se mueve la fecha) · «1 mes gratis para tu primer equipo» · «Crea tu primer equipo y prueba la app completa durante un mes, sin pagar al crearlo.» · «No hemos podido comprobar tu oferta ahora. Puedes crear el equipo igualmente: la oferta se aplica sola al crearlo.»
- Pasos: «Deporte» · «Modalidad» · «Datos» · «opcional» (en Categoría).
- Unirse: «Lo encuentras en el mensaje que te ha enviado tu club o tu entrenador.» · «Escribe al menos 4 caracteres para comprobarlo.» · «Revisa las letras y los números o pide el código otra vez.» · «No hemos podido comprobar el código.» · «Vuelve a intentarlo en un momento.» · «Asistente».
- Crear: «Escribe el nombre del equipo.» · «Escribe la temporada como 2026-27.» · «No se ha podido crear el equipo.» · «Revisa tu conexión y vuelve a intentarlo; no se ha guardado nada.» (mismo texto que la ficha del recorrido inicial).
- Éxito: «Copiar código» · «Código copiado» · «Tu prueba gratis dura hasta el {0}.» · «Podrás ver el código cuando quieras en Configuración → Equipo.»
- Canjear: «Si tu club te ha dado un código de licencia, escríbelo aquí.» · «Revisa que esté bien escrito; si sigue fallando, pide uno nuevo a tu club.»
- Todos los nuevos necesitan su traducción en los 7 idiomas de `lib/i18n/dict/`.

## 4. Componentes del código afectados
- `src/routes/_authenticated/onboarding.tsx`: `t()` en `SportPicker`, `VariantPicker`, `CreateTeam` (formulario y éxito); bloque de oferta según la fecha; esqueleto mientras carga `public-account-summary` y mensaje si falla; pasos; errores por campo y caja de error; «Copiar código»; fecha de fin de prueba con `res.trialEndsAt`; ayuda y placeholder del código; `Option` como fila con línea fina.
- `src/lib/sport-config/handball.ts`: `displayName` y `shortDescription` en castellano o pasados por `t()` donde se pintan (ojo: `displayName` también se guarda como `_sport_label` al crear el equipo en `teams.functions.ts`; ver duda 3).
- `src/lib/i18n/dict/*.json`: «Assistent» y los textos nuevos.
- Opcional (duda 1): `src/lib/public-account.functions.ts` devolviendo qué oferta toca (`firstTeamOffer: "waitlist_3m" | "trial_1m" | null`) con el mismo corte que la base de datos.
- **Sin cambios:** `teams.functions.ts`, `activation-codes.functions.ts`, migraciones y base de datos.

## 5. Dudas para Biel
1. **¿De dónde sale la fecha de la oferta?** Opción A (rápida): la pantalla compara con `BLACKOUT_FRIDAY_END` (27/11 23:59, ya existe en `lib/blackout-friday.ts`). Opción B (más segura): el servidor dice qué oferta toca, con el mismo corte que la migración. Propongo A para el 28/11 y B después.
2. **¿Arreglamos ya los textos en catalán y el bloque de la oferta antes del 28/11?** Son cambios de texto, sin tocar funciones. El resto (estilo, pasos, errores, «Copiar código») puede ir en el primer mes.
3. **«Handbol» en equipos ya creados.** Si un equipo de balonmano se creó con `_sport_label = "Handbol"`, ¿lo corregimos en la base de datos o solo en lo que se ve? (No toco datos: decide el equipo técnico.)
4. **¿Enseñamos la fecha de fin de prueba al crear el equipo?** Es dato real que ya devuelve el servidor; ayuda a que nadie se lleve una sorpresa.
5. **«Fútbol» y «Fútbol 7».** En la modalidad, el de once se llama solo «Fútbol». ¿Lo dejamos así o «Fútbol 11»? No lo cambio sin tu OK.
6. **(v4) Fechas nuevas.** Si la lista cierra el 10/12 a las 23:59 y se abre el 11/12, ¿los 3 meses de quien viene de la lista cuentan desde el 11/12 (fin el 11/03/2027)? Hace falta mover a la vez `BLACKOUT_FRIDAY_END` y el corte de la migración del 18/11; si solo se mueve uno, entre el 28/11 y el 10/12 la pantalla prometería 3 meses y la base de datos daría 1 (o al revés).
7. **(v4) Objetos reales.** El peto con el código y el móvil boca abajo son ilustraciones provisionales. ¿Foto propia de Pau (biblioteca v4) o se quedan como dibujo sencillo en la app por peso y rendimiento?

## 6. Fuera a propósito
Precio, tarjeta y condiciones de pago; el Club Fundador más allá del bloque apagado de la propuesta P2 (la insignia se pide en la pantalla de espera); número de apuntados; el nombre de Biel.
