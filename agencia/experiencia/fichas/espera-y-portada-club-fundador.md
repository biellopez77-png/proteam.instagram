# Ficha · Pantalla de espera y portada: bloque del Club Fundador

**Agente:** Irene (P1) · **Fecha:** 22/11/2026, rehecha en v4 el 23/11 · **Tareas:** `exp-espera-club`, `irene-v4-paleta`
**Prototipo navegable:** https://claude.ai/artifact/DHjcLazBbp559Dfp5sbVZh (versión 2, sistema v4; móvil 375 y escritorio; selector de estados; selector de fechas; casilla «Marcar lo propuesto»)
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
