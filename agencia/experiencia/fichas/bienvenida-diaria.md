# Ficha · Bienvenida diaria nueva, igual de rápida

**Agente:** Irene (P1) · **Fecha:** 23/11/2026 · **Tarea:** `exp-bienvenida-diaria` (prioridad normal, prototipo para el 9/12)
**Prototipo navegable:** https://claude.ai/artifact/X763axsDEFo2W8dd26FYaL (móvil 375 y escritorio; selectores «Versión: Nueva / Actual (hoy)», «Día», «Datos: bien / carga lenta / error», «Insignia», «Apertura: primera del día / vuelve tras 30 min»; casilla «Marcar lo propuesto»; botón «Repetir entrada»). Copia local: `agencia/experiencia/prototipos/bienvenida-diaria.html`.
**Base leída:** proteamapp `main` (488db5e): `components/home/home-intro.tsx` (`HomeIntro`, `INTRO_PHRASES`, `INTRO_TIMING`, `useHomeIntro`), `components/planning/assistant-home.tsx` (`AssistantHome`, `finishIntro`, `TargetLink`, `DismissMenu`), `lib/assistant.functions.ts`, `lib/assistant-model.ts`, `lib/i18n/dict/es.json`. Rama `revision/club-fundador` (5c7a6bd): `components/founder/founder-badge.tsx`, `lib/founder.ts`.

## 1. Diagnóstico (lo que hay hoy)
- Al abrir la app sale `HomeIntro`, una capa a pantalla completa encima del inicio: brillo → frase al azar palabra a palabra (desde 0,4 s) → «Hola, {nombre}» (2,6 s) → sube y encoge (3,4 s) → «Tareas pendientes» y las tareas una a una (desde ≈3,95 s) → «Ir al inicio» hace zoom hacia «Pendiente · Hoy». «Omitir» aparece a los 0,8 s. Si no hay nada pendiente: «Todo al día ✓» y se va sola a los ≈5 s.
- Debajo, la cabecera del inicio repite «Hola, {nombre}», la fecha y la semana, y los botones Calendario y Nueva sesión.
- Resultado: el entrenador espera unos 4 s para tocar una tarea, ve el saludo dos veces y la capa tapa las acciones rápidas.
- La animación es cuidada, pero visualmente es una tarjeta genérica (fuente de la app, cajas con borde y brillo azul).

## 2. Qué se conserva (sin tocar funciones)
- **Acciones:** Calendario (`/coach/calendar`), Nueva sesión (`/coach/court`) y «Pendiente · Hoy»: mismos destinos (`TargetLink`), mismo máximo de 3 con «Ver todo ({n})» / «Ver menos», mismo menú `DismissMenu` («Recuérdamelo mañana», «En una semana», «No aplica») y misma persistencia (`dismissPriority`).
- **Datos:** `getCoachPriorities` y `useTodayProgress` / `useWeekProgress`, sin consultas nuevas. Las tareas del prototipo son ejemplos escritos con las plantillas reales (`Preparar «{0}» antes de empezar`, `{0} jugadores con incidencias activas`, `Registrar lo ocurrido en «{0}»`, `Definir el objetivo de {0}`, `Dejar listo el partido contra {0}`, `Planificar {0}`).
- **Frases:** las 8 de `INTRO_PHRASES`, una al azar por apertura.
- **Cuándo sale:** la regla de `useHomeIntro` (una vez por apertura y al volver tras más de 30 min oculta), igual que ahora.
- **Estados ya existentes:** carga (esqueleto), error («No se han podido cargar las prioridades.» + «Reintentar»), vacío («Nada pendiente hoy. A entrenar.»), sin microciclo («Sin microciclo», «Esta semana no está planificada», «Crear semana»).
- **Movimiento reducido:** con `prefers-reduced-motion` todo es un fundido corto (regla `.motion-short` de AGENTS.md).
- **Resto del inicio:** franja de la semana, Tu día, Próximas tareas, Próximo partido e Indicadores, sin cambios.

## 3. Qué cambia (todo propuesta, decide Biel)
| Cambio | Detalle |
|---|---|
| **Sin capa encima** | La bienvenida pasa a ser la cabecera del inicio. Todo se puede tocar desde el primer fotograma; la entrada termina en 0,9 s (hoy, ≈4 s hasta ver las tareas). Desaparecen el saludo duplicado, «Omitir», «Ir al inicio» y el zoom de salida. |
| **Saludo editorial (estilo v3)** | Línea de fecha a lápiz en versalitas («LUNES 23 DE NOVIEMBRE · SEMANA 12» + píldora del tipo de semana), la frase del día en cursiva (Instrument Serif), «Hola, {nombre}.» grande en Instrument Serif y un trazo azul a lápiz que se dibuja bajo el nombre (0,45 s). Blanco, tinta, un azul, aire. |
| **Entrada** | Palabras con fundido y un poco de desenfoque (como hoy, pero 0,5 s en total), tareas con 60 ms entre una y otra. Solo opacidad, transform y filter. |
| **Vuelta tras 30 min** | Sin palabras animadas ni trazo: fundido de 0,2 s. La personalidad se guarda para la primera apertura. |
| **Línea «Hoy»** | «Hoy: **entrenamiento a las 19:00** · 4 pendientes.» o «Hoy: **partido contra CD Ribera a las 12:00** · 2 pendientes.» Sale de la primera actividad de `useTodayProgress(today)` y del número de tareas de hoy. Sin microciclo: «Esta semana no está planificada. Sin microciclo, la app no puede ordenar tu día.» + botón «Crear semana». |
| **Píldora del Club Fundador** | Con el rayo de `FounderBadge`. Verificada: «Club Fundador · Nº 011» (`founderNumberLabel`). En revisión: «Tu insignia · en revisión». Sin solicitar: «Consigue tu insignia del Club Fundador» (abre la tarjeta de `FounderSection`). Si no viene de la lista de espera: nada. Responde a la duda 5 del recorrido inicial («dónde vive la insignia tras el 28/11»). |
| **Vacío con lápiz** | Una marca de visto dibujada a lápiz azul junto a «Nada pendiente hoy. A entrenar.» y «Lo de los próximos días está más abajo.» |
| **«Después:»** | Bajo la lista, una línea con la siguiente tarea de los próximos 4 días (lo que hoy enseña la capa con `soonLimit`). |
| **Escritorio** | Dos columnas: saludo y acciones a la izquierda, «Pendiente · Hoy» a la derecha. Debajo, el resto del inicio. |

## 4. Textos nuevos (todos para `t()` y los 7 idiomas)
- «Hola, {0}.» (con punto; la clave actual `Hola, {0}` se puede reutilizar sin punto si Biel prefiere).
- «Hoy: {0} · {1}.» · «entrenamiento a las {0}» · «partido contra {0} a las {1}» · «nada pendiente» · «1 pendiente» · «{0} pendientes».
- «Sin microciclo, la app no puede ordenar tu día.»
- «Club Fundador · {0}» · «Tu insignia» · «en revisión» · «Consigue tu insignia del Club Fundador» (ya existe en el PR #1).
- «Lo de los próximos días está más abajo.» · «Después: {0}».
- Los textos de los toasts del prototipo («Vuelve mañana», «Vuelve en una semana», «Quitada de la lista», «En la app: …») son solo de la maqueta; hoy el menú no enseña toast y no se propone añadirlo.

## 5. Lo que NO aparece (a propósito)
Número de apuntados; precio fundador; tickets; nombre de Biel; ninguna función nueva (no hay consultas, rutas ni tablas nuevas).

## 6. Componentes del código afectados
- `src/components/home/home-intro.tsx`: `HomeIntro` deja de ser un portal a pantalla completa y pasa a ser `HomeWelcome` (cabecera en línea). Se conservan `INTRO_PHRASES`, `useHomeIntro` (decide «primera apertura» o «vuelta») y `prefersReduced`. `INTRO_TIMING` se acorta (palabras 0,5 s, trazo a los 0,42 s, tareas a 60 ms). Se pueden quitar `INTRO_TASKS_ID`, `TASKS_VT_NAME`, el brillo `intro-glow` y `intro-shine` si se aprueba.
- `src/components/planning/assistant-home.tsx`: la fila 1 (`header`) y el bloque «Pendiente · Hoy» se mueven a la nueva cabecera; `finishIntro` (View Transitions + FLIP) ya no hace falta; `introTasks` / `soonLimit` alimentan «Después:». `stagger()` sigue para el resto de tarjetas.
- `src/styles.css`: quitar `intro-glow`, `intro-shine`, `intro-task` y las reglas de view transition `home-tasks` si ya no se usan; añadir el trazo a lápiz (SVG con `pathLength=1` y `stroke-dashoffset`).
- Si se aprueba la píldora: `FounderBadge`/rayo y `founderNumberLabel` de `components/founder` y `lib/founder.ts` (rama `revision/club-fundador`, PR #1); depende de fusionar ese PR.
- i18n: claves nuevas del punto 4 en los 7 diccionarios, con marcadores posicionales (regla de AGENTS.md).

## 7. Dudas para Biel
1. **¿Quitamos la capa a pantalla completa?** Es el cambio grande: se gana velocidad (0 s para tocar contra ≈4 s) a cambio de perder el momento «película» de ahora. Alternativa intermedia: mantener la capa solo en la primera apertura del día y acortarla a 1,2 s.
2. **Píldora del Club en el inicio:** ¿te vale que la insignia viva aquí (y no solo en el perfil) para quien la tiene o la está pidiendo? ¿Y para quien no viene de la lista, nada?
3. **Línea «Hoy»:** ¿la quieres, o prefieres que el inicio no resuma y vaya directo a las tareas?
4. **Frases:** ¿mantenemos las 8 actuales o Lucía/Álex escriben unas nuevas con más voz de vestuario?
5. **Saludo neutro:** varias frases son en masculino («¿Listo para otro día?», «Vamos allá, entrenador»). ¿Las cambiamos por formas neutras («¿Otro día más?», «Vamos allá») para entrenadoras?
6. Sigue pendiente el **@ provisional** de Instagram (`FOUNDER_INSTAGRAM`), que afecta a la tarjeta que abre la píldora.
