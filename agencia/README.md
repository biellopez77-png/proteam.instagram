# Agencia creativa ProTeam

Seis agentes que trabajan como dos departamentos de la misma productora:

| Agente | Qué hace | Entrega |
|---|---|---|
| **01 · ProTeam Content Lab** | Estrategia, ideas, hooks, guiones de Reels | `guiones/AAAA-MM-DD-<slug>.md` |
| **02 · ProTeam Creative Direction** | Convierte un guion aprobado en documento de producción frame a frame | `produccion/AAAA-MM-DD-<slug>.md` |
| **04 · ProTeam Carousel Lab** | Carruseles de valor, comunidad y fidelización (ficha, hooks, diapositivas, dirección visual, copy) | `carruseles/AAAA-MM-DD-<slug>.md` + imágenes en `../feed/` |
| **05 · ProTeam Critical Lab** | Filtro de calidad: critica y puntúa (sobre 100) guiones, montajes y carruseles antes de publicar | `criticas/AAAA-MM-DD-<id>.md` |
| **06 · ProTeam Performance & Learning Lab** | Analiza métricas, críticas y comentarios; convierte resultados en cambios para los agentes | `APRENDIZAJES.md` + `aprendizaje/` |
| **03 · ProTeam Resource Bank** | Busca, clasifica y mantiene fotos, vídeos y capturas; prepara los recursos de cada Reel | `../banco/` + `recursos/AAAA-MM-DD-<slug>.md` |

Después, la producción (voz, montaje, render, música, panel y cola) se hace con el sistema de `REEL_ESTILO.md` y `tools/reelN/`.

## Flujo
1. Biel da un tema, objetivo o idea (o pide «MODO IDEAS / HOOKS / GUIONES / MEJORA / SERIES / ESTRATEGIA»).
2. Content Lab propone hooks, conceptos y guiones → Biel elige o aprueba.
3. Creative Direction recibe el guion aprobado y escribe el documento técnico (A–F).
4. Resource Bank cruza el documento con el banco, busca lo que falta y deja la lista de pendientes (lo que tiene que grabar o pasar Biel).
5. Critical Lab puntúa el guion (antes de producir) y el montaje final (antes de programar): por debajo de 75/100 no se publica; se corrige y se vuelve a puntuar.
6. Producción monta el Reel, lo sube al panel y lo programa.
7. Performance & Learning analiza resultados y críticas y actualiza `APRENDIZAJES.md`, que todos los agentes leen antes de crear.

## Cómo se activan
En cualquier conversación con Claude: «ACTIVAR AGENTE 1: PROTEAM CONTENT LAB» , «ACTIVAR AGENTE 2: PROTEAM CREATIVE DIRECTION» , «ACTIVAR AGENTE 3: PROTEAM RESOURCE BANK» , «ACTIVAR AGENTE 4: PROTEAM CAROUSEL LAB», «ACTIVAR AGENTE 5: PROTEAM CRITICAL LAB» o «ACTIVAR AGENTE 6: PROTEAM PERFORMANCE & LEARNING LAB» (son dos skills guardadas en la cuenta de Biel). No son agentes autónomos que trabajen solos: se activan en una conversación o desde una tarea programada.

## Base de conocimiento compartida (leer siempre)
- `MARCA.md` — público, tono, identidad visual, oferta y prohibiciones.
- `HOOKS_REFERENCIA.md` — los 12 patrones de hooks de referencia.
- `REELS_REFERENCIA.md` — guiones de referencia y por qué funcionan.
- `APRENDIZAJES.md` — lo aprendido de resultados y críticas; reglas vigentes para el próximo contenido (leer siempre).
- `HISTORIAL.md` — todo lo ya hecho (hooks, temas, enfoques, CTA, conceptos visuales). Se actualiza al entregar.
- `../DIRECCION_CREATIVA.md` y `../REEL_ESTILO.md` — dirección visual y sistema de producción.
- `../banco/INDICE.md` y `../banco/INVENTARIO.csv` — banco de recursos (fotos, vídeos, capturas reales).
