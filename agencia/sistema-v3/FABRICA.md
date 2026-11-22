# Fábrica de contenido v3 (Biel, 22/11)

Objetivo: el máximo de contenido con el sistema v3, todo como **propuesta para revisión** (no se publica nada en Instagram ni se toca la web o la app). Se ve en el **feed simulado**: https://claude.ai/artifact/LgY44TbsUR1wkS79NrXksv (slug `9f62c74c-524c-4f00-8f55-c4c92432f775`, base de datos colección `posts`).

Antes de trabajar, lee: SISTEMA_GUIONES.md, SISTEMA_VISUAL.md (con la «Receta de cine adaptada»), BANCO_TEMAS.md y la dirección creativa del 22/11 (agencia/direccion-creativa/2026-11-22/00-CONSOLIDADO.md: tonos de color y criterios).

## La cadena

| Paso | Quién (turno) | Entrada | Salida |
|---|---|---|---|
| 1. Ideas y propuestas | Dani A y Dani B (01) | la primera idea libre de BANCO_TEMAS.md según la rotación | `agencia/fabrica/propuestas/<id>.md`: 3 propuestas completas del reel (shock, contexto, problema, subproblemas, solución al final y final circular, con variaciones) + post `<id>` en el feed con estado «idea» |
| 2. Crítica | Andrés (05) | propuestas sin nota | `agencia/fabrica/criticas/<id>.md` con la tabla de notas; la ganadora (≥ 80) se copia como guion final en `agencia/fabrica/guiones/<id>.md`; post a «en guion» con la nota; tarea para Marta en la oficina |
| 3. Recursos | Pau (03), dentro del turno de Marta | guion final | 3-5 imágenes reales con licencia (Commons) o dibujadas; créditos en el guion |
| 4. Montaje | Marta A y Marta B (02) | tareas «Montar <id>» pendientes | vídeo en `tools/reel_v4/<id>/final.mp4`, subido al feed (`media/<id>.mp4` y portada `media/<id>.jpg`), post a «listo» |
| 5. Contenido normal | Clara (04) | cada reel «listo» | 1 carrusel (1080×1440, 5-7 láminas PNG) y 2 Stories por reel, subidos al feed (`media/<id>-c1.png`…), posts tipo «carrusel» y «story» |

**Reparto entre turnos duplicados:** antes de coger algo, márcalo en la oficina (`tasks/<id>` con `state: "trabajando"` y `by: "Marta A"` o `"Marta B"`). Si ya está «trabajando» y tiene menos de 90 minutos, coge otra cosa.

**Rotación de temas (Dani):** T01 → T03 → T02 → T04 → T05 → T09 → T06 → T07 → T08 → T10 → T11 → T12 → T14, y vuelta a empezar. Dani A coge las ideas impares y Dani B las pares de cada tema. Marca la idea en BANCO_TEMAS.md con `[en curso <fecha>]` y luego `[hecha → <id>]`.

## Montaje (Marta): reglas fijas

- Plantilla: `tools/reel_v4/a3.html`. Cópiala a `tools/reel_v4/<id>.html` y cambia solo el contenido. Mantén la mecánica de cámara: **planos fijos, la cámara solo se mueve al cambiar de zona** (0,6 s, entrada y salida suaves). Nada de derivas, temblores, golpes ni flashes.
- **Poco ruido:** fondo `#fbfaf7`, tinta `#121212`, un acento azul `#2f6bff`, rojo `#d23a2a` solo para la amenaza. Sin grano, sin viñetas, sin brillos en los textos, sin etiquetas que no hagan falta. Las fotos reales van enmarcadas en blanco con una sombra suave.
- **Gancho:** un plano nuevo cada 1-2 s, y se ve lo que se nombra.
- Fundidos a negro solo en los giros (como mucho 2 por vídeo). Subtítulos de 58 px en la zona segura (y ≈ 1330).
- **Final:** «Apúntalo en la app de ProTeam» → la cámara se desliza a una pantalla en blanco con ProTeam en grande → frase puente que enlaza con la primera frase («Porque…», «Como…») → la cámara vuelve al primer encuadre. El último fotograma tiene que ser igual que el primero.
- **Voz:** Mateo `gpMzl7dbkfC9dIxAqQZT`, eleven_v4, 1 toma (`generations_count: 1`). Tiempos con Scribe (`creative_transcribe_audio`, `connect_from` del nodo de voz). Ritmo `SP=1.1 python3 tools/reel_v4/tiempos.py <id>`.
- **Música:** reutiliza `tools/reel_v4/a3/m1.mp3` (o otra de la biblioteca `tools/reel_v4/musica/`). Solo se genera música nueva una vez por semana (cuesta 900 créditos).
- **Créditos de ElevenLabs:** cada reel gasta unos 800 en voz. Si quedan menos de 10.000 (consúltalo con `account_get_usage`), no generes voz: deja el reel en «en guion» y apúntalo en el log.
- **Efectos:** `sfx_a3.py` adaptado (aire, lápiz, papel). **Mezcla:** `./mezcla2.sh <id> <t_giro1> <t_giro2>`.
- **Revisión obligatoria:** contacto de fotogramas cada 1,5 s y el test de saltos (diferencia entre fotogramas: ningún pico de un solo fotograma). Si falla, se corrige antes de subir.
- **Subir al feed:** `list_files` del feed, después `publish_files` en modo patch con `media/<id>.mp4` y `media/<id>.jpg`, y `db_write` de `posts/<id>` con `status: "listo"`.

## Feed simulado: formato de `posts/<id>`

`{order (número; más alto = más arriba), type: "reel" | "carrusel" | "story", title, tema, status: "idea" | "en guion" | "en montaje" | "listo", score, agent, hook, caption, video, cover, slides: [...], short (en Stories), updatedAt}`

Orden: cada pieza nueva usa `order` = el mayor que haya + 1.

## Límites

- No se publica nada en Instagram, no se contacta a nadie, no se toca la web ni la app.
- No se inventan datos ni testimonios; los hechos de referentes llevan fuente. Sin el nombre de Biel y sin el precio.
- Caras reales solo de fotos reales con licencia, nunca generadas.
