# Ficha · Pantalla de espera y portada: bloque del Club Fundador

**Agente:** Irene (P1) · **Fecha:** 22/11/2026 · **Tarea:** `exp-espera-club` (prioridad alta, prototipo para el 24/11)
**Prototipo navegable:** https://claude.ai/artifact/DHjcLazBbp559Dfp5sbVZh (móvil 375 y escritorio; selector de estados; casilla «Marcar lo propuesto»)
**Base:** rama `revision/club-fundador` de proteamapp (PR #1): `access-gate-screen.tsx`, `founder/founder-section.tsx`, `founder/founder-landing.tsx`, `founder/founder-badge.tsx`, `founder/founder-welcome.tsx`, `lib/founder.ts`, `routes/index.tsx`.

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
| Bloque del Club con más presencia: borde en tinta, título en Instrument Serif con «Club Fundador» en azul, etiqueta «CLUB FUNDADOR» | Propuesta visual |
| **Hueco del número**: «FUNDADOR Nº ___» trazado a lápiz; se rellena con el número cuando se asigna | Propuesta |
| **Barra de 3 pasos** (Compartida → En revisión / Sin encontrar → Verificada con rayo) bajo el hueco | Propuesta |
| Botón principal en azul con rayo «Conseguir mi insignia» (antes ShieldCheck) | Propuesta |
| **Orden**: bienvenida → Club → cuenta atrás (hoy el Club va al final) | Propuesta, decide Biel |
| **Estado de carga**: esqueleto mientras llega `founder_members` (hoy no hay) | Propuesta |
| **Estado de error** al cargar la insignia: «No hemos podido cargar tu insignia» + «Reintentar» (hoy `member.error` no se trata) | Propuesta |
| Ventana: hoja inferior en móvil, diálogo centrado en escritorio; error de envío dentro de la ventana además del toast | Propuesta |

### Portada (`founder-landing.tsx`)
| Cambio | Estado |
|---|---|
| Ventajas en lista con filetes y rayo azul en vez de 4 tarjetas con iconos | Propuesta visual |
| Título grande «Club *Fundador*» y la frase «Tu insignia se consigue desde la lista de espera…» como nota a lápiz con flecha | Propuesta visual |
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
`src/components/access-gate-screen.tsx` (orden), `src/components/founder/founder-section.tsx` (bloque, estados de carga y error, hueco del número, barra de pasos), `src/components/founder/founder-landing.tsx` (maquetación, misterio, botón), `src/styles.css` (trazo a lápiz; `founder-pop` ya existe). Sin cambios en `lib/founder.ts`, RPC ni migración.

## 6. Dudas para Biel
1. **@ de Instagram:** `FOUNDER_INSTAGRAM` sigue en `app.proteam` (suspendida desde el 20/11). ¿Cuál es la cuenta provisional? Sin ella, la ventana pide mencionar una cuenta que no existe.
2. ¿Subimos el bloque del Club por encima de la cuenta atrás en la espera?
3. ¿Te vale la frase «No contamos cuántos somos.» como juego de misterio, o prefieres no mencionar el número en absoluto?
4. ¿Botón de registro dentro del bloque del Club en la portada, o solo los que ya hay arriba y abajo?
5. Hueco «Nº ___»: ¿cuándo empiezan a asignarse números (y los del 1 al 10)? Mientras no haya, los verificados verán «Aquí aparecerá tu número cuando lo asignemos.».
6. ¿Quién verifica mientras tanto? (hoy, tú).
