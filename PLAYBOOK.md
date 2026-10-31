# ProTeam · Instagram autónomo (@app.proteam)

Este repositorio es la fuente de todo lo que se publica en @app.proteam y el manual
para las sesiones programadas que lo gestionan. El dueño (Biel) ha aprobado que la
cuenta funcione sola: publicar, analizar y ajustar sin pedirle aprobación. Solo se le
avisa de problemas o decisiones que no se pueden deshacer.

## Herramientas

- **Instagram**: conector Windsor.ai, cuenta `17841445998297098`.
  - Leer: `get_data` connector `instagram` (campos con `get_fields`).
  - Publicar: `execute_action` connector `instagram` con `create_video_post`
    (Reel; `video_url`, `caption`, `cover_url`, `share_to_feed: true`),
    `create_carousel_post` (`image_urls` 2–10 JPEG, `caption`),
    `create_image_post` (`image_url`, `caption`), `create_story`
    (`image_url` o `video_url`, sin texto). Comentarios: `reply_to_comment`.
- **URLs públicas** de los archivos: `https://cdn.jsdelivr.net/gh/OWNER/REPO@main/<ruta>`.
  Si Instagram no la acepta, probar `https://raw.githubusercontent.com/OWNER/REPO/main/<ruta>`.
- **Plantillas visuales**: `tools/gen.py` (Playwright + fuentes + capturas reales de la app en
  `tools/app/`). Formato feed 1080×1350, Stories 1080×1920.

## Cola

`queue.json`: lista de piezas con `when` (hora de Madrid), `kind` (reel, carousel, image,
story), `files`, `caption`, `cover`, `status` (`pending`, `published`, `failed`), y tras
publicar `media_id`, `published_at` o `error`.

Publicar = cada pieza `pending` con `when` <= ahora + 10 min y no más de 6 h en el pasado.
Una pieza con más de 6 h de retraso se reprograma al siguiente hueco libre del mismo tipo.
Tras cada publicación, actualizar su estado en `queue.json` y añadir una línea a `log.md`;
hacer commit y push.

Nunca publicar dos veces la misma pieza: si `status` no es `pending`, no se toca. Si una
publicación falla, un reintento como máximo; después `failed` con el error.

## Estrategia (resumen)

- Reels = alcance. Gancho de pregunta, dato o conflicto en el primer segundo; nunca empezar
  por la pantalla de la app. Objetivo: saltos en 3 s < 40 %.
- Feed (carruseles e imágenes) = seguidores y feed completo: 3 por semana, guardables,
  serie "Lo que dicen los datos #N" y piezas de balonmano.
- Stories = fidelizar: 1–3 al día (teaser del Reel, pregunta rápida, dentro de ProTeam,
  el Reel en Story). Las encuestas no se pueden poner por API: usar tarjetas de pregunta
  que invitan a responder por mensaje.
- Pilares: Lo que dicen los datos 40 %, El problema del entrenador 20 %, ProTeam en 30 s
  25 %, Prueba real 15 %.
- Una sola llamada a la acción por pieza. "3 meses gratis" solo en piezas de producto.
- Castellano revisado, sin catalanismos ni erratas, 3–5 hashtags.
- Prohibido inventar testimonios, resultados o estadísticas. Los datos llevan fuente o
  "datos de ejemplo". No usar el caso de un club sin su permiso.
- Marca: azul #2f6bff, tinta #0d0f14, Manrope 800 + Instrument Serif cursiva en azul para el
  remate, fondo blanco con puntos, logo ProTeam arriba a la izquierda.

## Rutina

- **Cada ejecución de publicación**: publicar lo que toque, leer métricas de las últimas
  piezas publicadas y anotarlas en `log.md`. Responder comentarios nuevos con respuestas
  cortas y útiles en nombre de ProTeam (nunca prometer cosas que la app no hace, nunca datos
  personales). Ocultar spam.
- **Cada lunes (planificación)**: analizar la semana anterior con datos (alcance, saltos,
  visionado medio, guardados, compartidos, seguidores, comentarios), escribir el informe
  semanal en `reports/AAAA-MM-DD.md`, decidir qué potenciar y qué dejar, generar con
  `tools/gen.py` los 3 carruseles o imágenes y las Stories de la semana siguiente, añadirlos
  a `queue.json` y reordenar los Reels del backlog según lo que funcione.
- **Cada primer lunes de mes**: auditoría mensual en `reports/`.

## Límites conocidos

- Los Reels con voz nueva se producen en sesiones con el ordenador de Biel conectado
  (descarga de voces de ElevenLabs). El backlog de Reels en `reels/` cubre hasta el 11 de
  diciembre de 2026; avisar a Biel cuando queden menos de 10.
- Instagram no da seguidores por Reel ni datos demográficos por debajo de 100 seguidores.
