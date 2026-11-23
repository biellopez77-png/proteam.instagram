# Ficha · Onboarding (crear o unirse a un equipo): la puerta del 28/11

**Agente:** Irene (P1) · **Fecha:** 23/11/2026 · **Tarea:** `exp-onboarding` (abierta por Irene, prioridad alta: no había tareas P1 pendientes ni comentarios de Biel o Álex en las 8 entregas; el onboarding es un entregable del PLAN que el recorrido inicial dejaba «tal cual»)
**Prototipo navegable:** https://claude.ai/artifact/L2T7StVAojsJDH2sNbXh6H (móvil 375 y escritorio; selectores «Versión: Propuesta / Actual (hoy)», «Cuándo llega: antes del 27/11 23:59 / desde el 28/11», «Quién: primer equipo / ya tiene equipo», «Simular: todo bien / carga lenta / error del servidor / código no válido / unirse pide aprobación»; casilla «Marcar lo propuesto»). Copia local: `agencia/experiencia/prototipos/onboarding.html`.
**Base leída:** rama `revision/club-fundador` de proteamapp (5c7a6bd): `src/routes/_authenticated/onboarding.tsx` (`OnboardingPage`, `JoinWithCode`, `SportPicker`, `VariantPicker`, `CreateTeam`, `RedeemLicense`, `Field`), `lib/teams.functions.ts`, `lib/teams.ts` (`ROLE_SHORT`), `lib/activation-codes.functions.ts`, `lib/public-account.functions.ts` (`eligibleForFirstTeamOffer`), `lib/sport-config/*.ts`, `lib/blackout-friday.ts` (`BLACKOUT_FRIDAY_END`), `lib/i18n/dict/es.json`, migración `20261118000500_prueba_1_mes_tras_lista.sql`.

**Por qué ahora:** sin equipo no se entra en la app, así que el 28/11 todo entrenador nuevo pasa por esta pantalla. Hoy tiene tres problemas que se notan el Día 0:
1. **Promete algo que ya no es verdad.** El bloque «3 meses gratis para tu primer equipo» sale a cualquiera sin organización (`eligibleForFirstTeamOffer`), sin mirar la fecha. Pero la migración del 18/11 (decisión de Biel) da 3 meses solo a quien crea su primer equipo antes del 27/11 a las 23:59, y **1 mes** a quien lo crea después. Desde el 28/11 la pantalla promete 3 meses y la base de datos da 1.
2. **Sale en catalán.** `SportPicker`, `VariantPicker`, `CreateTeam` y su éxito tienen los textos escritos sin `t()`: «Quin esport practica el teu equip?», «Crear equip», «Nom de l'equip», «Creant…», «Equip creat», «Entrar al panell», «Tornar», «Canviar»… Además `handball.ts` tiene `displayName: "Handbol"` y la descripción en catalán, y el rol «Assistent» no tiene traducción en `es.json`. Las claves en español ya existen en `es.json` (salvo «Assistent»).
3. **Los errores solo viven en un aviso que desaparece.** Crear equipo muestra `err.message` sin traducir (sale «No s'ha pogut crear l'equip.»), y ningún formulario dice qué campo falla.

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
| **Oferta según la fecha (arreglo para el 28/11)** | Antes del 27/11 23:59: «3 meses gratis» + texto actual + «Cuentan desde el 28 de noviembre.» Desde el 28/11: «1 mes gratis para tu primer equipo» + «Crea tu primer equipo y prueba la app completa durante un mes, sin pagar al crearlo.» Ver la duda 1 sobre de dónde sale la fecha. |
| **Fin de la prueba en el éxito** | `createTeam` ya devuelve `trialEndsAt` y no se enseña. Tras crear el primer equipo: «Tu prueba gratis dura hasta el {fecha}.» (28/02/2027 para la lista; un mes después para el resto). |
| **«Copiar código»** | Bajo el código del equipo, como en la ficha del recorrido inicial. Toast «Código copiado». Más «Podrás ver el código cuando quieras en Configuración → Equipo.» |
| **Pasos a lápiz** | En crear: «Deporte — Modalidad — Datos» (o «Deporte — Datos» si no es fútbol), hechos en azul y el actual en tinta. |
| **Deportes con su campo dibujado** | Cada deporte con un rectángulo a lápiz a escala de sus medidas reales (105 × 68, 28 × 15, 40 × 20, 65 × 45). Filas con línea fina, no tarjetas. |
| **Errores dentro del formulario** | Debajo del campo: «Escribe el nombre del equipo.» · «Escribe la temporada como 2026-27.» Caja de error encima del botón (además del toast): ver textos. |
| **Ayuda en el código** | «Lo encuentras en el mensaje que te ha enviado tu club o tu entrenador.»; ejemplo con el formato real (`NOMBRE-8 caracteres`, p. ej. «ALEVINB-4F7A21C9») en vez de «EQUIP-XXXX»; «Escribe al menos 4 caracteres para comprobarlo.» mientras el botón está desactivado. |
| **Carga y error de la oferta** | Carga: tres rayas de esqueleto en el sitio del bloque (hoy aparece de golpe y empuja las opciones). Error: «No hemos podido comprobar tu oferta ahora. Puedes crear el equipo igualmente: la oferta se aplica sola al crearlo.» (cierto: la decide la base de datos). |
| **Estilo v3** | «Empezamos» en Instrument Serif con trazo azul a lápiz; oferta como nota de papel con borde a lápiz; un solo azul para la acción principal; mucho aire. Escritorio: la misma columna centrada de hoy. |

## 3. Textos (es)
**Existentes, se conservan:** «Empezamos» · «Para entrar en la app necesitas formar parte de un equipo.» · «3 meses gratis para tu primer equipo» · «Crea tu primer equipo y disfruta de acceso completo durante tres meses, sin pagar al crearlo.» · «Crear mi primer equipo» · «Unirme con código» · «Introduce el código que te ha dado tu club o entrenador. Si requiere aprobación, la revisarán.» · «Crear equipo» · «Crea tu equipo, invita a los jugadores y elige después el plan mensual o anual.» · «Canjear código de activación» · «Código de equipo» · «Comprobar código» · «Comprobando…» · «Entro como» · «Entrar en el equipo» · «Entrando…» · «¡Ya estás en el equipo!» · «Solicitud enviada» · «El equipo revisará tu solicitud. Cuando la aprueben podrás entrar desde «Mis equipos».» · «Ir a mis equipos» · «Volver» · «¿Qué deporte practica tu equipo?» · «Elige el deporte antes de crear el equipo. Podrás cambiarlo después desde la configuración.» · «¿Qué modalidad juega el equipo?» · «La modalidad define el campo, las posiciones, las alineaciones y las estadísticas de todo el equipo.» · «Balonmano» · «Pista de 40 × 20 m, dos partes y siete jugadores en pista.» · «Cambiar» · «Nombre del equipo» · «Categoría» · «Temporada» · «Creando…» · «¡Equipo creado!» · «Equipo creado» · «Comparte este código con tus jugadores:» · «Entrar al panel» · «Código» · «Nombre del equipo, si el código permite crearlo» · «Activar licencia» · «Validando…» · «Licencia activada.» · «Este código no es válido.» · «Este código ha caducado.» · «Este código ha llegado al límite de usos.» · «No se ha podido validar el código.»

**Nuevos (propuestos):**
- Oferta: «Para tu primer equipo» · «Cuentan desde el 28 de noviembre.» · «1 mes gratis para tu primer equipo» · «Crea tu primer equipo y prueba la app completa durante un mes, sin pagar al crearlo.» · «No hemos podido comprobar tu oferta ahora. Puedes crear el equipo igualmente: la oferta se aplica sola al crearlo.»
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

## 6. Fuera a propósito
Precio, tarjeta y condiciones de pago; Club Fundador e insignia (viven en el recorrido inicial y en Configuración); número de apuntados; el nombre de Biel.
