# Ficha · Carta de bienvenida del Club Fundador: la hoja, la firma y cuándo se abre

**Prototipo:** https://claude.ai/artifact/PXfLe9pZvzBBnrsTuo4MVn (móvil 375 y escritorio; propuesta y actual del PR #1 para comparar; primera vez y releer; con nombre y número, con nombre sin número, sin nombre; estados cargando, error al cargar, error al guardar «leída» y vacío —sin verificar—; con y sin animación). Fuente: `agencia/experiencia/prototipos/carta-bienvenida.html`.
**Fecha:** 23/11 · Irene (P1) · Primer mes (el 28/11 la carta ya funciona tal cual; esto la mejora sin cambiar su lógica).
**Base:** rama `revision/club-fundador` de proteamapp: `src/components/founder/founder-welcome.tsx`, `founder-badge.tsx` (`FounderBadge`, `FounderSignature`), `founder-section.tsx`, `src/lib/founder.ts` (`shouldShowFounderWelcome`, `founderNumberLabel`), `src/styles.css` (`.founder-signature`, `.founder-pop`), migración `20261120010000_club_fundador.sql` (`welcome_seen_at`, `mark_founder_welcome_seen`).

## 0. Rehecha en v4 (24/11, sistema v4 de Biel del 23/11) · tarea `irene-v4-paleta` (7/10)

**Prototipo:** el mismo enlace, versión 2 (v4). Mismas funciones, mismos textos y mismos estados que la versión v3; cambia la piel. Lo de los apartados siguientes sigue vigente salvo lo que se dice aquí (el «Instrument Serif para el título», el «lápiz azul» y la «sombra de papel» de la tabla quedan sustituidos por esto).

**Confirmado (no cambia):** las palabras de Biel, la firma `FounderSignature` (trazo y tiempos), cuándo se abre (`shouldShowFounderWelcome`), `mark_founder_welcome_seen` al cerrar, el número solo cuando está asignado y el nombre de `user_metadata.name`. El código de hoy (PR #1) sigue sin cambios; la vista «Actual» ahora lo enseña en el tema oscuro de la app.

**Propuesto en v4:**
- **Sala a oscuras y una lámpara:** la app detrás en penumbra (#02050F con velo); la hoja en #060C19 es lo único iluminado, con la luz desde arriba (degradado hielo muy suave y un filo de luz en el borde superior). Móvil: pantalla completa; escritorio: 560 px, radio 10 px.
- **La luz señala lo activo dentro de la hoja:** el nombre subrayado con una línea de luz hielo (#B9E0FF) y la firma dibujada en azul eléctrico (#6AA8FF) con un halo leve; mismos tiempos y la misma quietud con `prefers-reduced-motion`. El margen de libreta pasa a una línea de luz muy tenue.
- **Ultravioleta una vez por pantalla:** el rayo de la insignia del membrete (40 px, roseta azul y rayo #8B5CF6 con filo blanco). «Entrar» va en azul ProTeam #636DFF; «Cerrar» (releer) en contorno. En «sin verificar», la insignia queda apagada y el ultravioleta pasa a «Conseguir mi insignia» (el acceso al Club, como en la pestaña). En carga y error, ninguno.
- **Tipografía:** Plus Jakarta Sans en todo (título en 800); Instrument Serif cursiva solo en el nombre, como única voz. «Biel · creador de ProTeam» pasa a Plus Jakarta Sans 600.
- **Objetos reales en estados:** error al cargar con un **móvil boca abajo**; sin verificar con un **sobre cerrado** bajo una luz baja. Dibujos provisionales hasta tener foto propia o con licencia.
- Avisos sin rojo: el aviso simulado de «Error al guardar» va en superficie #121B30; el fundador sigue sin ver ningún aviso.
- **Fechas:** la carta no depende del relanzamiento; la fecha de la carta es `reviewed_at`. El ejemplo «24 de noviembre de 2026» vale con las fechas nuevas (lista hasta el jue 10/12, apertura el vie 11/12, por confirmar), porque se verifica durante la lista.
- Corregido un fallo del prototipo v3: en escritorio, los estados de error y vacío salían fuera de la hoja.

**Dudas nuevas para Biel (v4):**
6. ¿El ultravioleta en el rayo del membrete o en la firma? Propongo el rayo (es la regla de la app: el rayo del verificado) y la firma en azul eléctrico.
7. Objetos: el móvil boca abajo y el sobre son dibujos provisionales. ¿Foto propia o con licencia (`banco/fotos`) o dibujo?

**Por qué ahora:** la carta es la ventaja 7 del Club (CLUB_FUNDADOR.md) y es el único sitio donde aparece Biel. Las fichas del recorrido inicial, del verificado y del Club en la app la dejan «tal cual» y remiten aquí su diseño. Hoy es un diálogo genérico: en un móvil de 375 px la insignia de 96 px y el título empujan la firma y «Entrar» bajo el pliegue, y al releerla desde Configuración el botón sigue diciendo «Entrar».

## Se conserva (confirmado, PR #1)
- **Las palabras de Biel, sin tocar una coma:** título «¡Bienvenido al Club Fundador, {0}!» / «¡Bienvenido al Club Fundador!», los 4 párrafos («Soy Biel, creador de ProTeam. Gracias por estar aquí desde el principio.» · «ProTeam nace en el banquillo y queremos que crezca contigo: con lo que uses, con lo que eches de menos y con lo que nos cuentes.» · «Tu confianza es lo que da sentido a todo esto. Gracias por formar parte de este camino.» · «Nos vemos dentro de ProTeam.»), «Biel · creador de ProTeam» y «Entrar».
- **La firma** `FounderSignature`: mismo trazo, mismos tiempos (0,4 s de espera, 2,2 s de trazo, punto y cola) y estática con `prefers-reduced-motion`.
- **Cuándo se abre:** sola, una vez, cuando `status = 'verified'` y `welcome_seen_at` es nulo (`shouldShowFounderWelcome`). Al cerrarla (Entrar, X, Escape o tocar fuera) se llama a `mark_founder_welcome_seen` y se invalida `["founder-member"]`.
- **El número** solo cuando está asignado, con `founderNumberLabel` («Nº 011»). Nadie tiene número todavía.
- **El nombre** sale del primer nombre de `user_metadata.name`, como hoy en `access-gate-screen.tsx`.

## Qué cambia (propuesta)
| Cambio | Por qué |
|---|---|
| **Una hoja, no un diálogo.** Móvil: ocupa la pantalla, con el texto que se desplaza y el pie («Entrar») fijo abajo. Escritorio: hoja de 560 px sobre la app atenuada, radio pequeño (6 px), sombra de papel | Es una carta, no un aviso. En 375 px hoy hay que desplazarse para ver la firma y el botón; con el pie fijo «Entrar» siempre está a mano |
| **Membrete** pequeño arriba: insignia de 40 px (sin número dentro) + «ProTeam · Club Fundador» + «Fundador Nº 011» en azul; sin número, «Insignia verificada» | Libera la altura que ocupa la roseta de 96 px y deja el número legible (en la roseta grande, el número va en blanco y pequeño) |
| **Fecha de la carta:** «Verificada el 24 de noviembre de 2026», de `reviewed_at` | Da a la carta su fecha real. No es un dato nuevo: ya existe en `founder_members` |
| **Título en Instrument Serif**, con el nombre en cursiva y un subrayado a lápiz azul que se dibuja (0,7 s, mismo `pathLength` que la firma) | Sistema v3: la serif para lo que emociona, un solo azul, lápiz |
| **Margen a lápiz** a la izquierda (1 px, color `--rule`), como una hoja de libreta | Detalle del banquillo; no compite con el texto |
| Sin número asignado: línea bajo la firma «Tu número llegará muy pronto.» | Mismo texto que ya usa `FounderSection` para ese estado |
| «Entrar» se puede pulsar desde el primer segundo; la firma se dibuja a la vez | La animación nunca bloquea |
| Pie, primera vez: «Podrás volver a leerla en Configuración · Club Fundador.» | Dice dónde vive (ficha club-en-la-app) |
| **Al releer** (desde la pestaña Club Fundador): «Cerrar» en lugar de «Entrar», y sin la nota del pie | «Entrar» no tiene sentido cuando ya estás dentro |
| Error al guardar «leída»: sin aviso al fundador; un reintento silencioso de `mark_founder_welcome_seen` | Hoy el fallo no se gestiona. Si vuelve a fallar, la carta se abrirá otra vez en la próxima visita, que es un mal menor |

## Estados
- **Carta** (con nombre y número / con nombre sin número / sin nombre): ver arriba.
- **Cargando:** solo si `founder_members` tarda más de 300 ms; esqueleto de membrete, título y párrafos, sin texto.
- **Error al cargar:** «No hemos podido abrir tu carta.» · «Revisa tu conexión y vuelve a intentarlo. Tu insignia sigue verificada.» · «Reintentar» · «Cerrar». No se llama a `mark_founder_welcome_seen`.
- **Vacío (sin verificar):** si alguien llega a «Leer mi carta» sin estar verificado: «Tu carta se abre cuando tu insignia esté verificada.» · «Comparte la historia del Club, menciónanos y la revisamos a mano.» · «Conseguir mi insignia» · «Cerrar».

## Textos nuevos (todos con `t()`)
«ProTeam · Club Fundador» · «Fundador {0}» · «Insignia verificada» · «Verificada el {0}» · «Tu número llegará muy pronto.» (ya existe) · «Podrás volver a leerla en Configuración · Club Fundador.» · «Cerrar» · «Cerrar la carta» (etiqueta de la X) · «No hemos podido abrir tu carta.» · «Revisa tu conexión y vuelve a intentarlo. Tu insignia sigue verificada.» · «Reintentar» · «Tu carta se abre cuando tu insignia esté verificada.» · «Comparte la historia del Club, menciónanos y la revisamos a mano.» · «Conseguir mi insignia» (ya existe).

## Qué no sale en la carta
Número de apuntados o cualquier recuento; precio fundador o importes; tickets regalo; lista de ventajas (ya está en «Lo que tienes» de la pestaña Club Fundador); el nombre de Biel fuera de esta hoja.

## Componentes del código afectados
- `src/components/founder/founder-welcome.tsx`: nueva maqueta (hoja). Nueva prop `mode: "first" | "again"` (o `reread?: boolean`) para el botón «Cerrar»; nueva prop `verifiedAt?: string | null` para la fecha. `DialogContent` con clases propias: pantalla completa en móvil (`inset-0 h-[100dvh] max-w-none rounded-none`) y `sm:max-w-[560px]`. Reintento silencioso en `close()`.
- `src/components/founder/founder-badge.tsx`: sin cambios (`FounderBadge size={40} number={null}` en el membrete; `FounderSignature` igual).
- `src/components/founder/founder-section.tsx` y la futura pestaña Club Fundador: pasar `verifiedAt={member.data?.reviewed_at}` y `mode="again"` cuando se abre desde «Ver mi carta de bienvenida».
- `src/styles.css`: el subrayado del nombre reutiliza `@keyframes founder-sign`; regla `prefers-reduced-motion` ampliada a ese trazo.
- Fecha con `Intl.DateTimeFormat("es-ES", { day: "numeric", month: "long", year: "numeric" })` según el idioma de `useI18n`.
- Base de datos y RPC: **sin cambios**.

## Dudas para Biel
1. **¿Te vale la carta como hoja** (pantalla completa en el móvil) en lugar del diálogo actual?
2. **Título y entrenadoras:** «¡Bienvenido…» queda en masculino para una entrenadora. ¿Lo dejas así, o prefieres «Te damos la bienvenida al Club Fundador, {0}» (o «¡Bienvenido/a…»)? No lo he cambiado: son tus palabras.
3. **Fecha:** ¿«Verificada el 24 de noviembre de 2026» o sin fecha?
4. **Día 0 (28/11, «carta en la entrada» en el PLAN):** ¿la carta solo para verificados, como hoy, o para todos los de la lista de espera (sin número y sin insignia encendida)? Enlaza con la duda 2 del recorrido inicial.
5. **La firma:** es un dibujo recreado, no tu firma escaneada. ¿Quieres darnos tu firma real (una foto en papel blanco) para trazarla igual?
