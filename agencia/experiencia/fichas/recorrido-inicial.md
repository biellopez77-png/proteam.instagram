# Ficha · Recorrido inicial: ventajas → carta → insignia → equipo → primera semana → app

**Agente:** Irene (P1) · **Fecha:** 22/11/2026 · **Tarea:** `exp-recorrido-inicial` (prioridad normal, prototipo para el 2/12)
**Prototipo navegable:** https://claude.ai/artifact/R8Hw32rspoh6zaaxkFnRdN (móvil 375 y escritorio; selectores «Quién entra», «Tramo», «Insignia», «Simular: todo bien / error al guardar / carga lenta»; casilla «Marcar lo propuesto»). Copia local: `agencia/experiencia/prototipos/recorrido-inicial.html`.
**Base leída:** rama `revision/club-fundador` de proteamapp (commit 5c7a6bd): `routes/_authenticated/onboarding.tsx`, `components/founder/*`, `lib/founder.ts`, `components/planning/create-cycle-dialog.tsx`, `components/planning/tree.tsx` (`EmptyPlanningState`), `routes/_authenticated/coach.planning.index.tsx`, `components/planning/assistant-home.tsx`, `lib/public-account.functions.ts`.

## 1. Qué se conserva (sin tocar funciones)
- **Ventajas:** solo lo que CLUB_FUNDADOR.md permite decir: «Insignia de fundador con tu número», «3 meses gratis» (lista de espera, hasta el 27/11 23:59), «Una persona del equipo te acompaña», «Votas en lo que construimos». Invitaciones: «Muy pronto te contamos cómo funcionan.» (mismo texto que la portada). Sin precio fundador, sin detalles de tickets, sin número de apuntados.
- **Carta:** texto, título «¡Bienvenido al Club Fundador, {0}!», firma animada (`FounderSignature`) y «Biel · creador de ProTeam» de `FounderWelcomeDialog`, sin cambios. El nombre de Biel solo aquí. `mark_founder_welcome_seen` se sigue llamando al cerrar/seguir.
- **Insignia:** flujo del PR #1 completo: 3 pasos, imagen `public/club-fundador/compartir.jpg`, «Compartir» (solo si existe `navigator.share`), «Descargar imagen», campo @ con `normalizeInstagramHandle`, «Ya la he compartido» / «Actualizar solicitud», RPC `request_founder_badge`, toasts, estados `requested` / `verified` / `rejected` con sus textos, aviso «Pulsar «Compartir» no verifica…», verificación manual en `/admin`, rayo.
- **Equipo:** `onboarding.tsx` entero: bloque «3 meses gratis para tu primer equipo» (solo si `eligibleForFirstTeamOffer`), «Unirme con código» (comprobar → vista previa → rol → entrar; solicitud pendiente), «Crear equipo» (deporte → modalidad si es fútbol → nombre, categoría, temporada → código), «Canjear código de activación». Mismas funciones de servidor (`createTeam`, `joinTeamWithCode`, `previewTeamCode`, `selectTeam`, `redeemActivationCode`).
- **Semana:** las 4 plantillas de microciclo que ya existen en `create-cycle-dialog.tsx` (carga · volumen alto; descarga · reducir carga y recuperar; competitiva · preparar el partido; recuperación · descanso activo) y la persistencia por los flujos actuales de ciclos (regla de AGENTS.md: «keep cycle and activity persistence in their existing flows»).
- **App:** la bienvenida diaria actual (`AssistantHome`): Hola, fecha · Semana, Calendario, Nueva sesión, Tu día, Pendiente · Hoy, Próximo partido. Con semana saltada, su estado vacío de hoy («Sin microciclo», «Esta semana no está planificada», «Crear semana»).

## 2. Qué cambia (todo propuesta, decide Biel)
| Cambio | Detalle |
|---|---|
| **Un solo recorrido con 5 tramos** | Club · Carta · Insignia · Equipo · Semana, con raya de progreso a lápiz arriba y botón «Atrás». Ruta sugerida `/bienvenida` para los 3 primeros tramos; Equipo y Semana siguen en `/onboarding`. |
| **Quién lo ve** | Apuntados a la lista de espera: los 5 tramos. Quien no estaba en la lista: empieza en «Equipo» (2 tramos); los 3 primeros aparecen tachados en la raya. Cómo se sabe quién está en la lista: ver dudas. |
| **Todo se puede dejar para luego, menos el equipo** | Carta → «Conseguir mi insignia»; Insignia → «Lo haré luego» («Tu insignia te espera en tu perfil»); Semana → «Ahora no, entrar en la app». Sin equipo no se entra, como hoy. |
| **Carta antes de la verificación** | El plan pone carta (paso 2) antes del verificado (paso 3). Hoy la carta solo se abre al verificar. Propuesta: se ve sin número y con la insignia apagada; cuando se verifica, «Ver mi carta de bienvenida» ya la muestra con «Fundador Nº 011». |
| **Insignia en el recorrido** | El mismo contenido de la ventana de `founder-section.tsx`, a pantalla completa. En revisión no bloquea: «Seguir: crear mi equipo». |
| **Tras crear el equipo** | Además de «Entrar al panel», botón principal «Planificar mi primera semana» y «Copiar código» bajo el código. |
| **«Tu primera semana»** | Elegir «Esta semana» o «La que viene» (lun–dom) y una de las 4 plantillas. Botón «Crear «Semana 1» · semana de carga». Por detrás, con funciones que ya existen: si no hay macrociclo, crear temporada (macro), un bloque (meso) y la semana (micro) con la plantilla elegida. |
| **Bloque del Club en la app** | Tras el 28/11 la pantalla de espera desaparece: la tarjeta de la insignia (`FounderSection`) necesita sitio. Propuesta: en la bienvenida diaria mientras no esté verificada y, después, en el perfil. |
| **Estados de error y carga** | Envío de insignia: «No se ha podido enviar. Inténtalo de nuevo.» dentro del formulario además del toast. Crear equipo: mensaje dentro del formulario. Crear semana: «No hemos podido crear tu semana. Tu equipo sí está guardado. Vuelve a intentarlo o hazlo luego desde Planificación.» Carga lenta: esqueletos en la entrada a la app. |

## 3. Textos nuevos (todos para `t()` y los 7 idiomas)
- Raya: «Club» · «Carta» · «Insignia» · «Equipo» · «Semana» · «Atrás».
- Club: «Ya estás dentro» · «Bienvenido al Club Fundador» · «Estás en ProTeam desde el principio. Esto es lo que tienes por haberte apuntado a la lista de espera.» · «Verificada y numerada. Ningún número se repite. Se consigue compartiendo una historia: te lo explicamos en un momento.» · «Para tu primer equipo, por apuntarte antes del 27 de noviembre a las 23:59.» · «Soporte de tú a tú durante los tres primeros meses.» · «Encuestas y votaciones solo para fundadores.» · «Seguir» · «Son cuatro pasos más. Puedes dejar cualquiera para luego, menos crear tu equipo.»
- Carta: «Conseguir mi insignia» · «Podrás volver a leerla desde tu perfil, en «Ver mi carta de bienvenida».»
- Insignia: «Tu insignia» · «Una insignia con tu número» · «Lo haré luego» · «Tu insignia te espera en tu perfil.» · «Seguir: crear mi equipo» · «Solicitud enviada como @{0}. Te avisaremos cuando esté verificada. Mientras, sigue: no hace falta esperar.»
- Equipo: «Paso {0} de {1}» · «Planificar mi primera semana» · «Copiar código» · «Código copiado» · «No se ha podido crear el equipo. Revisa tu conexión y vuelve a intentarlo; no se ha guardado nada.»
- Semana: «Tu primera semana» · «Planifica una semana. Solo una.» · «Elige cuándo empieza y qué tipo de semana es. Después la llenas de sesiones desde la app.» · «La que viene» · «Plantilla» · «Crear «Semana 1» · {0}» · «Creando tu semana…» · «Semana 1 creada» · «Ahora no, entrar en la app» · «El partido lo añades después desde Partidos; la semana se ordena a su alrededor.» · texto de error (arriba).
- Las tareas de «Pendiente · Hoy» del prototipo («Invita a tus jugadores con el código…», «Añade la primera sesión de la semana») son ejemplo: salen de `getCoachPriorities`, no se inventan.

## 4. Lo que NO aparece (a propósito)
Número de apuntados; importe o mención del precio fundador congelado (no existe en Stripe); condiciones de los tickets; nombre de Biel fuera de la carta; plazas limitadas o escasez.

## 5. Componentes del código afectados
- `src/routes/_authenticated/onboarding.tsx`: raya de progreso, «Paso x de y», tras crear: «Planificar mi primera semana» y «Copiar código». **Ojo:** `SportPicker`, `VariantPicker`, `CreateTeam` y el éxito («Equip creat», «Entrar al panell», «Tornar», «Pròximament») tienen textos en catalán sin `t()`; un entrenador en español los ve en catalán. Arreglarlo con `t()` (las claves ya existen en `es.json`) aunque no se haga nada más.
- `src/lib/sport-config/handball.ts`: `displayName: "Handbol"` y descripción en catalán sin traducir.
- Nueva ruta `src/routes/_authenticated/bienvenida.tsx` (Club, Carta, Insignia) que reutiliza `FounderBadge`, `FounderSignature` y la lógica de `FounderSection` (sacar el formulario a un componente compartido para no duplicarlo).
- `src/components/founder/founder-welcome.tsx`: aceptar `inline` (sin diálogo) y número nulo antes de verificar.
- `src/components/founder/founder-section.tsx`: extraer el formulario; colocar la tarjeta en la bienvenida diaria / perfil.
- Primera semana: componente nuevo que llama a la creación de ciclos existente (macro → meso → micro) con valores por defecto; aplicar la plantilla semanal si el equipo la tiene. Sin cambios en base de datos.
- `src/components/planning/assistant-home.tsx`: solo el hueco para la tarjeta del Club (si Biel lo aprueba).
- Redirección: decidir quién entra en `/bienvenida` (ver dudas) en el guard de `_authenticated` o en `getPublicAccountSummary().destination`.

## 6. Dudas para Biel
1. **¿Cómo sabemos que alguien estaba en la lista de espera?** ¿Toda cuenta creada antes del 28/11 00:00, o hace falta otra marca? Sin eso no se puede decidir quién ve los 3 primeros tramos.
2. **Carta antes de verificar:** ¿te vale que se lea sin número y con la insignia apagada, o prefieres que siga abriéndose solo al verificar (y entonces el tramo 2 sería solo para verificados)?
3. **Primera semana:** crear temporada, bloque y semana de golpe con nombres por defecto («Temporada 2026-27», «Bloque 1», «Semana 1»): ¿de acuerdo, o prefieres llevar al usuario a Planificación con su estado vacío de hoy?
4. ¿Esta semana (23–29/11, ya casi pasada el día 28) o solo «la que viene»? En el prototipo están las dos y por defecto la que viene.
5. **Dónde vive la insignia tras el 28/11:** ¿bienvenida diaria hasta verificar y luego perfil?
6. Quien entra con código (jugador o segundo entrenador): en el prototipo se salta «Semana» y va a la app. ¿Correcto?
7. Sigue pendiente el **@ provisional** de Instagram: los pasos aún dicen @app.proteam (`FOUNDER_INSTAGRAM`).
