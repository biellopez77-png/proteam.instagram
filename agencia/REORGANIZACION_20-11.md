# Reorganización · 20/11 · Instagram suspendido (manda sobre LANZAMIENTO.md mientras dure)

**Situación:** Instagram ha suspendido la cuenta personal de Biel y la de ProTeam. La respuesta puede tardar hasta 48 h. Se prepara una cuenta provisional, «Club Fundador ProTeam». La estrategia del lanzamiento se mantiene: fases, Club Fundador, 3 meses gratis y lista de espera hasta el 27/11 a las 23:59.

## Prioridades
1. **Continuidad:** web, lista de espera, la nueva cuenta, la experiencia de los interesados y los enlaces.
2. **Club Fundador:** sección web, ventajas, insignia, bienvenida y comunicaciones.
3. **Piezas informativas:** Stories y diseños, siempre para aprobación.
4. **Audiovisual: EN PAUSA.** Ni guiones, ni Reels, ni ideas de Reels, ni vídeos, hasta autorización expresa de Biel.

**Regla mientras dure:** no se publica nada fuera sin aprobación de Biel. Ni en Instagram, ni en producción de la web o la app, ni comunicaciones masivas.

## 1. Tareas detenidas
**Turnos programados pausados (9):**
- Producción de Reels (cada 3 h).
- Guiones (cada hora).
- Radar de actualidad.
- Publicación de Laura (cada hora).
- Lucía en Instagram (cada hora).
- Samuel diario y Samuel de los lunes: dependen de las métricas de Instagram.
- SEO semanal: publica en la web sin aprobación.

**Tareas de la oficina cerradas como «detenida»:**
- Por la pausa audiovisual: reducir texto en los Reels, «ProTeam por dentro», el contador de solución (u28/u30/u31/u33), u57/u58 (u57 está producido y no saldrá), el fotograma 0 de u39–u45, Reel de impacto por fases, recursos de impacto y contexto.
- Por la cuenta suspendida: las capturas de la cola, «medir por fase» con Instagram y el token de Instagram.
- Sustituida: «carruseles y Stories por fase» pasa a ser «piezas informativas para aprobación».

## 2. Tareas que continúan
**Turnos activos:**
- Laura (encargos).
- Clara: carruseles y Stories, ahora solo piezas informativas en borrador.
- Equipo técnico: todo como PR, sin publicar.
- Álex.
- Lucía emails.
- Activación de equipos en prueba.
- Prospección de clubes y de escuelas.
- Parte semanal.

**Tareas abiertas:**
- Club Fundador (R1).
- Registro y lista de espera (R1).
- Día 28 con tarjeta (R1).
- Emails del 27 y el 28 (Lucía).
- Preguntas frecuentes (Lucía).
- Qué contestar sobre el Club (Lucía).
- Cocreación del 25: queda preparada en borrador; si se publica y cuándo, lo decide Biel.
- Reducir texto en las Stories (Clara).
- Piezas informativas (Clara).
- Medir la web y la lista (Samuel).

## 3. Quién ha recibido las nuevas instrucciones
Todos los agentes las tienen en la oficina: 00 Laura, 01 Dani, 02 Marta, 03 Pau, 04 Clara, 05 Andrés, 06 Samuel, 07 Lucía, R1 (equipo técnico) y 08 Álex. Cada uno tiene un bloque «CAMBIO 20/11» al principio de sus instrucciones, que dice qué para, qué sigue y qué prioriza. Además hay una regla nueva («regla-pausa-audiovisual-20-11») que todos los turnos leen al empezar.

| Agente | Qué detiene | Qué sigue | Qué necesita |
|---|---|---|---|
| 01 Dani, 02 Marta, 03 Pau | Todo lo audiovisual | 01: textos cortos para Clara si se los pide. 03: imágenes para piezas informativas | La autorización de Biel para retomar |
| 04 Clara | Programar y publicar | Piezas informativas en borrador | El @ provisional y el visto bueno de Biel |
| 05 Andrés | Críticas de guiones y Reels | Revisar las piezas informativas, la web y el Club | — |
| 06 Samuel | Métricas de Instagram | Web y lista de espera | — |
| 07 Lucía | Instagram | Emails: mensaje sobre la suspensión, sin dar el @ nuevo hasta que Biel lo confirme | El @ provisional |
| R1 | Publicar sin aprobación | PRs de continuidad y del Club Fundador | La aprobación de cada PR |

## 4. Web y app

| Trabajo | Estado |
|---|---|
| Enlaces a Instagram en la web | **Comprobado:** la web publicada no enlaza a @app.proteam en ningún sitio, así que no hay enlaces rotos |
| Suscripción: fecha de fin de la prueba, renovación y cancelación desde «Facturación» | **Implementado y publicado** (20/11, 02:40) |
| Insignia del Club Fundador (lista de espera, verificación manual, numeración, carta) | **Implementado y probado en local, PR #1 sin publicar** |
| Sección Club Fundador en la portada (solo ventajas confirmadas, sin precio fundador) | **Implementado y probado (compila), en el PR #1 sin publicar** |
| Traducciones de /adviento (página añadida por Lovable hoy; rompía `bun run build`) | **Implementado y probado (compila), en el PR #1** |
| La insignia exige mencionar a @app.proteam, que está suspendida | **Pendiente de Biel:** el @ provisional. Se cambia en un solo sitio (`FOUNDER_INSTAGRAM`) y se regenera la imagen para compartir |
| Perfil general y onboarding | **Diseñados** (lienzo «Club Fundador · propuesta»); se implementarán como PR |
| Aviso de la suspensión en la web | **No hecho.** Propuesta: no ponerlo en la web (solo en Stories y emails), salvo que Biel quiera un aviso |

## 5. Piezas informativas que conviene preparar
**Diseñadas** en `stories/reorg1120/` (en borrador, para aprobación):
1. `r1`: «Seguimos aquí.» Qué ha pasado, en una frase.
2. `r2`: «Club Fundador ProTeam», la cuenta provisional, con el @ pendiente.
3. `r3`: «Nada cambia.» Lista de espera hasta el 27, 3 meses gratis y lanzamiento el sábado 28.
4. `r4`: el Club Fundador **sin** el precio fundador (sustituye a `club.jpg`).

**Cuando llegue el @:** se regeneran `r2`, la imagen para compartir de la insignia y las encuestas del pack de cocreación. Basta con `HANDLE=@cuenta python3 tools/reorg1120/gen.py`.

## 6. Materiales que se aprovechan
- **Pack de cocreación** (`stories/cocreacion1120/`): sirve tal cual en la cuenta nueva y encaja con «Club Fundador».
- **Lienzo «Club Fundador · propuesta»:** base de la sección web, el perfil y el onboarding.
- **`agencia/CLUB_FUNDADOR.md`:** ventajas y su estado, numeración y verificación.
- **Guiones POV y gráficos** (`agencia/guiones/2026-11-20-pov-serie-camara-en-mano.md`, `agencia/recursos/pov/`): guardados para cuando se retome.
- **Reels ya producidos que no han salido** (u51, u68, u72, u57 y otros): guardados y sin publicar; se decide al volver.

## 7. Decisiones de Biel
1. **El @ de la cuenta provisional** y si se conecta a Windsor para publicar desde la oficina. Hasta entonces se publica a mano.
2. **Aprobar las Stories `r1`–`r4`.**
3. **Aprobar el PR #1** (insignia, sección web, Adviento) y aplicar su migración.
4. **¿Aviso de la suspensión en la web?** Recomiendo que no.
5. **La insignia mientras no haya cuenta:** recomiendo que la mención sea a la cuenta provisional.
6. **La cocreación del miércoles 25:** si se hace en la cuenta provisional.
7. **El límite de uso:** sigue abierta la decisión de los créditos o el horario ligero. Con 9 turnos pausados, el gasto ya baja mucho.
