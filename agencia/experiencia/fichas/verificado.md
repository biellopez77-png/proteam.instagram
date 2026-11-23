# Ficha · Verificado: cola de verificación en /admin y el momento del rayo

**Agente:** Irene (P1) · **Fecha:** 23/11/2026 · **Tarea:** `exp-verificado` (abierta por Irene: «verificado» es un entregable suyo en `agencia/experiencia/PLAN.md` y no tenía tarea; las 5 entregas anteriores siguen en revisión sin comentarios)
**Prototipo navegable:** https://claude.ai/artifact/CghzH9okSKD4Sa6ekJFq9U (móvil 375 y escritorio; selector «Lado»: quien verifica en `/admin` o el fundador; selector «Estado»; casilla «Marcar lo propuesto»). Copia local: `agencia/experiencia/prototipos/verificado.html`.
**Base:** rama `revision/club-fundador` de proteamapp (PR #1, commit 5c7a6bd): `components/admin/founder-admin-section.tsx`, `routes/_authenticated/admin.tsx` (pestaña «Club Fundador»), `supabase/migrations/20261120010000_club_fundador.sql`, `components/founder/founder-section.tsx`, `founder-welcome.tsx`, `founder-badge.tsx`, `lib/founder.ts`.

**Por qué ahora:** hasta el 27/11 a las 23:59 habrá solicitudes y la verificación es a mano (Biel o quien él diga). Una historia de Instagram dura 24 horas: si la cola no avisa, se pierden historias y hay que pedir a la gente que la vuelva a subir. Y desde el 28/11, con la app abierta, quien se verifique ya no pasa por la pantalla de espera, que es el único sitio donde hoy se abre la carta.

## 1. Qué se conserva (sin tocar)
- **Verificación manual.** Se abre el Instagram del usuario desde `/admin`, se comprueba la historia con la mención y se pulsa Verificar o Rechazar. Pulsar «Compartir» nunca verifica.
- **Funciones de servidor del PR #1, sin cambios:** `admin_list_founder_members` (pendientes primero, la más antigua arriba), `admin_review_founder_badge(_user_id, _approve, _note)` (nota de hasta 300 caracteres), `admin_assign_founder_number` (sin número: siguiente libre desde el 11, con bloqueo y `UNIQUE`; 1–10 solo a mano), `admin_clear_founder_number`.
- **Numeración:** 1–10 reservados (el 1 es de Biel); «Siguiente número» desde el 11; el número solo después de verificar (`founder_number_only_verified`). Nadie tiene número todavía.
- **Filtros de la cola:** por revisar, verificadas, rechazadas y todas, con su recuento (solo lo ve quien verifica; nunca sale de `/admin`).
- **Para el fundador:** los textos de estado de `FounderSection` («Estamos revisando tu historia.», «No hemos encontrado tu historia con la mención. Puedes volver a intentarlo.», «Insignia verificada. Tu número llegará muy pronto.», «Fundador {0}. Gracias por estar desde el principio.»), los botones «Ver mi solicitud», «Conseguir mi insignia» y «Ver mi carta de bienvenida», y la carta de `FounderWelcomeDialog` tal cual (título, 4 párrafos, firma animada, «Biel · creador de ProTeam», «Entrar»). El nombre de Biel solo dentro de la carta.
- **Regla de la carta:** se abre sola una vez al verificarse (`shouldShowFounderWelcome`) y al cerrarla se llama a `mark_founder_welcome_seen`.
- Insignia con **rayo**; el número aparece en ella solo cuando existe («Nº 011»).

## 2. Qué cambia (todo propuesto)

### En `/admin` → Club Fundador
| Cambio | Por qué |
|---|---|
| **Reloj de 24 horas** en cada solicitud por revisar: «Caduca hacia las 18:40 · quedan 2 h» (ámbar con menos de 4 h); pasadas 24 h desde el envío, «Puede haber caducado (enviada hace 26 h)» en rojo | La historia desaparece a las 24 h. Se calcula con `requested_at` + 24 h (no sabemos cuándo se publicó la historia, pero la solicitud se envía justo después). Sin datos nuevos |
| Tres líneas de guía arriba: abrir el perfil, Verificar o Rechazar, empezar por las que caducan antes | Lo puede hacer otra persona que no sea Biel sin explicación previa |
| **Deshacer durante 5 s** tras Verificar o Rechazar («Verificando a @…» + «Deshacer» con barra que se acaba); la llamada al servidor se hace al acabar la cuenta | Hoy se actúa al primer toque; un error abre la carta a quien no toca o rechaza a quien sí la subió |
| **Rechazar con motivo** (tres opciones): «No encontramos la historia», «La historia no menciona a @{cuenta}», «Ese usuario de Instagram no existe o es privado». Se guarda en `review_note` | Hoy siempre guarda «Sense història amb la menció» y el fundador no ve nada |
| El fundador ve el motivo en su bloque: «Motivo: …» bajo el texto de rechazo, con la pista «Súbela de nuevo con la pegatina @Mención» | Le dice qué arreglar. Necesita leer `review_note`, que ya llega en `founder_members` (la política de lectura deja ver la fila propia) |
| **«Dar número al verificar»**, interruptor apagado por defecto («apagado: los números aún no han empezado»). Encendido, Verificar llama después a `admin_assign_founder_number` sin número | Cuando Biel diga que empiezan los números, verificar y numerar es un toque; mientras, no se numera nada por accidente |
| Botón **«Quitar número»** en las verificadas con número | La función `admin_clear_founder_number` existe pero no tiene botón |
| **Buscador** por @, nombre o correo | Cuando alguien escribe a soporte («ya la subí»), se le encuentra sin recorrer la lista |
| «Verificar igualmente» en las rechazadas (hoy «Verificar» a secas) | Deja claro que se corrige un rechazo |
| **Estados:** carga (tres filas en gris), «Todo al día.» cuando no queda nada por revisar, **error de carga** («No se ha podido cargar la cola. Puede ser la conexión o que la sesión haya caducado. No se ha cambiado nada.» + «Reintentar») y errores de acción en lenguaje claro («No se ha podido guardar. Revisa la conexión y vuelve a intentarlo; no ha cambiado nada.», «Ese número ya es de otra persona.») | Hoy, si `admin_list_founder_members` falla, se pinta «No hi ha sol·licituds», que parece una cola vacía; y los errores salen con el mensaje técnico |
| Textos del panel en **español con `t()`** | Hoy están en catalán y fijos («Pendent de revisar», «Verificat», «Rebutjar», «Següent número», «Assignar reservat»…). Ver duda 1 |

### Para el fundador
| Cambio | Por qué |
|---|---|
| **El momento del rayo**, una sola vez al verificarse, en lugar de abrir la carta directamente: pantalla blanca, la insignia gris, un trazo a lápiz la rodea, se enciende en azul y el rayo se dibuja (≈2 s; sin animación con `prefers-reduced-motion`). Texto: «ProTeam · Club Fundador» · «Tu insignia, verificada.» · «Hemos visto tu historia. Ya eres del Club Fundador.» · «Leer mi carta» / «Más tarde» (y «Cerrar») | Es el momento de reconocimiento que promete el Club; hoy salta un diálogo con la carta sin contexto. Se puede tocar desde el primer segundo |
| «Más tarde» deja la carta para luego: aviso «Tu carta te espera en «Ver mi carta de bienvenida».» | No obliga a leer en mal momento. `mark_founder_welcome_seen` se llama al cerrar el momento, igual que hoy al cerrar la carta |
| **Desde el 28/11, el momento sale al entrar en la app** (inicio), no solo en la pantalla de espera | Hoy `shouldShowFounderWelcome` solo se evalúa dentro de `FounderSection`, que vive en `access-gate-screen.tsx`. Con la app abierta, quien se verifique después del 28/11 no se entera ni ve la carta (estado «Actual: tras el 28/11 no se entera» del prototipo) |
| En revisión, línea bajo el texto: «La miramos a mano, una a una. Te avisamos aquí en cuanto esté.» | Explica la espera sin prometer plazos |
| **Error de carga** del bloque: «No hemos podido cargar tu insignia. Revisa tu conexión. Tu solicitud no se ha perdido.» + «Reintentar» | Hoy, si la consulta de `founder_members` falla, el bloque enseña «Consigue tu insignia…», como si no hubiera pedido nada |

## 3. Textos nuevos (todos para `t()` en los 7 idiomas)
- Admin: «Club Fundador · verificaciones» · «Abre el Instagram de cada persona, busca la historia que menciona a @{0} y decide. Nadie se verifica solo.» · «Abre su perfil y mira las historias de hoy.» · «¿Sale la imagen del Club y la mención? Verificar. ¿No? Rechazar con el motivo.» · «Las historias duran 24 horas: empieza por las que caducan antes.» · «Por revisar» · «Verificadas» · «Rechazadas» · «Todas» · «Buscar por @, nombre o correo» · «Dar número al verificar» · «apagado: los números aún no han empezado» · «el siguiente libre: {0}» · «enviada {0}» · «Caduca hacia las {0} · quedan {1} h» · «Caduca en {0} min» · «Puede haber caducado (enviada hace {0} h)» · «Verificar» · «Verificar igualmente» · «Rechazar» · «¿Por qué la rechazas? Se lo enseñamos tal cual.» · los 3 motivos · «Cancelar» · «Verificando a @{0}…» · «Rechazando a @{0}…» · «Deshacer» · «Deshecho. No se ha enviado nada.» · «Verificada. Verás la carta abrirse en su próxima visita.» · «Verificada · {0}» · «Rechazada. Le enseñamos el motivo y puede volver a enviarla.» · «Siguiente número» · «Número reservado (1–10)» · «Asignar reservado» · «{0} asignado a @{1}» · «Quitar número» · «Número quitado. Vuelve a estar libre.» · «Ese número ya es de otra persona.» · «Todo al día.» · «No queda ninguna historia por revisar. Cuando alguien envíe su usuario, aparecerá aquí, la más antigua arriba.» · «Ninguna solicitud coincide con «{0}». Prueba con el @ sin espacios.» · «No se ha podido cargar la cola.» · «Puede ser la conexión o que la sesión haya caducado. No se ha cambiado nada.» · «Reintentar» · «No se ha podido guardar. Revisa la conexión y vuelve a intentarlo; no ha cambiado nada.» · «No se ha podido asignar el número. Vuelve a intentarlo.»
- Fundador: «ProTeam · Club Fundador» · «Tu insignia, verificada.» · «Hemos visto tu historia. Ya eres del Club Fundador.» · «Leer mi carta» · «Más tarde» · «Cerrar» · «Tu carta te espera en «Ver mi carta de bienvenida».» · «La miramos a mano, una a una. Te avisamos aquí en cuanto esté.» · «Motivo: {0}» · «Súbela de nuevo con la pegatina @Mención.» · «No hemos podido cargar tu insignia.» · «Revisa tu conexión. Tu solicitud no se ha perdido.»

## 4. Lo que NO sale
Número de apuntados fuera de `/admin` (los recuentos de la cola solo los ve quien verifica); importe o mención del precio fundador; condiciones de los tickets; nombre de Biel fuera de la carta; plazos de verificación prometidos («en 24 h»); escasez o plazas.

## 5. Componentes del código afectados
- `src/components/admin/founder-admin-section.tsx`: textos con `t()`; reloj de 24 h (función pura en `lib/founder.ts`, p. ej. `founderStoryExpiry(requested_at, now)` con test); deshacer con temporizador antes de llamar a `admin_review_founder_badge`; selector de motivo para `_note`; interruptor «Dar número al verificar» (encadena `admin_assign_founder_number` con `_number` nulo); botón «Quitar número» (`admin_clear_founder_number`); buscador en cliente; `list.isError` con su estado y «Reintentar»; mensajes de error claros (ya se traduce `number_taken`).
- `src/components/founder/founder-section.tsx`: leer `review_note` y enseñarlo en el rechazo; estado de error con `member.isError`; mover la apertura automática (`shouldShowFounderWelcome`) a un componente que también se monte en el inicio de la app (p. ej. `FounderVerifiedMoment` en `_authenticated` o en `assistant-home.tsx`) para que funcione después del 28/11.
- Nuevo `src/components/founder/founder-verified-moment.tsx`: la pantalla del rayo (reutiliza la roseta y el rayo de `FounderBadge`; trazo con `pathLength` como `FounderSignature`), abre `FounderWelcomeDialog` con «Leer mi carta».
- `src/styles.css`: animación del momento junto a `founder-pop` y `founder-sign`, con su bloque `prefers-reduced-motion`.
- `src/lib/founder.ts`: constantes de los 3 motivos (clave + texto) y la función de caducidad. `FOUNDER_INSTAGRAM` sigue pendiente de la cuenta provisional.
- **Sin cambios en base de datos:** todo usa las columnas y funciones que ya existen.

## 6. Dudas para Biel
1. **Idioma del panel `/admin`:** hoy está en catalán y sin traducir. ¿Lo pasamos a español con `t()` como el resto, o lo dejas en catalán porque solo lo usas tú?
2. **¿Quién verifica?** Si no eres solo tú, la guía de tres líneas sirve para que otra persona lo haga sin explicación. ¿Hay alguien más?
3. **Números:** ¿cuándo empiezan y a quién van del 2 al 10? Mientras, el interruptor «Dar número al verificar» queda apagado.
4. **Motivos de rechazo:** ¿te valen los tres y que el fundador los vea tal cual?
5. **El momento del rayo:** ¿lo quieres antes de la carta o prefieres que se abra la carta directamente, como hoy?
6. **¿Aviso fuera de la app al verificar?** Hoy solo se entera al volver a entrar. Se podría avisar por correo (Lucía, a mano, como el soporte), pero no existe ningún envío automático y no lo damos por hecho.
7. **@ provisional** de Instagram (sigue `app.proteam`, suspendida): cambia el texto de la cola, de los motivos y de la imagen.
