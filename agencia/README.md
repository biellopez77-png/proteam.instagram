# Agencia creativa ProTeam

> **Desde el 16/11:** las instrucciones completas de cada agente están en `agentes/` (primero `agentes/00_COMUN.md`), sus procedimientos en `skills/` y el sistema de vídeo y la biblioteca en `../intel/README.md`. Los `PROMPT_AGENTE*.md` son los encargos originales de Biel y quedan como referencia. No se espera el OK de Biel para nada: donde este archivo diga «Biel aprueba», vale el protocolo de la oficina.

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

## Dónde se gestiona
Todo se manda y se ve desde la oficina (https://claude.ai/artifact/CEbj9fsPQPUvVtRsp1S18o). Los agentes son las personas de la oficina (01 Dani, 02 Marta, 03 Pau, 04 Clara, 05 Andrés, 06 Samuel, 00 Laura) y las tareas programadas son sus turnos. Protocolo obligatorio: `../oficina/PROTOCOLO.md`.

## Flujo (sin esperar el OK de Biel; detalle en `agentes/00_COMUN.md` §10)
1. **Idea:** Content Lab parte de un insight con escena y entrega concepto, hooks puntuados y guion.
2. **Puerta 1:** Critical Lab audita el guion (escala del 16/11; por debajo de 75 o con bloqueante, vuelve).
3. **Dirección:** Creative Direction compara con los cinco últimos Reels y escribe el documento de producción (15 puntos).
4. **Recursos:** Resource Bank localiza, clasifica o pide el material, con origen y licencia.
5. **Producción:** voz, música, montaje y render con `REEL_ESTILO.md` y `tools/reelNN/`.
6. **Análisis y puerta 2:** el vídeo real se analiza con `tools/video_intel.py`; Critical Lab lo audita con marcas de tiempo. Solo entonces se programa.
7. **Aprendizaje:** Performance & Learning lee resultados a 24 y 48 h y actualiza `APRENDIZAJES.md`.
Carruseles y Stories: Carousel Lab hace la pieza, con las mismas dos puertas. Lo que falte y solo pueda dar Biel queda como tarea «FALTA (Biel): …» en la oficina.

## Cómo se activan
En cualquier conversación con Claude: «ACTIVAR AGENTE 1: PROTEAM CONTENT LAB» , «ACTIVAR AGENTE 2: PROTEAM CREATIVE DIRECTION» , «ACTIVAR AGENTE 3: PROTEAM RESOURCE BANK» , «ACTIVAR AGENTE 4: PROTEAM CAROUSEL LAB», «ACTIVAR AGENTE 5: PROTEAM CRITICAL LAB» o «ACTIVAR AGENTE 6: PROTEAM PERFORMANCE & LEARNING LAB» (son seis skills guardadas en la cuenta de Biel, que cargan las instrucciones de `agentes/`). Trabajan solos en sus turnos programados y también ejecutan los encargos que Biel deja en la oficina (turno de Laura, cada 2 h).

## Base de conocimiento compartida (leer siempre)
- `MARCA.md` — público, tono, identidad visual, oferta y prohibiciones.
- `HOOKS_REFERENCIA.md` — los 12 patrones de hooks de referencia.
- `REELS_REFERENCIA.md` — guiones de referencia y por qué funcionan.
- `APRENDIZAJES.md` — lo aprendido de resultados y críticas; reglas vigentes para el próximo contenido (leer siempre).
- `REFERENCIAS.md` — referencias (@unrespiro…) y competencia: patrones que aprendemos fuera.
- `HISTORIAL.md` — todo lo ya hecho (hooks, temas, enfoques, CTA, conceptos visuales). Se actualiza al entregar.
- `../DIRECCION_CREATIVA.md` y `../REEL_ESTILO.md` — dirección visual y sistema de producción.
- `../banco/INDICE.md` y `../banco/INVENTARIO.csv` — banco de recursos (fotos, vídeos, capturas reales).
- `agentes/` y `skills/` — instrucciones completas y procedimientos de cada agente.
- `../intel/` — sistema de vídeo, vídeos analizados, competencia, insights y características (`../intel/README.md`).
