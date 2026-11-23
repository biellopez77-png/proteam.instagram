# Fábrica v4 (Biel, 23/11; sustituye a sistema-v3/FABRICA.md)

> **PARADO (Biel, 23/11 16:27): «No quiero nada en 3D».** Nada de escenas 3D ni motion graphics. No se produce nada hasta que Biel decida de dónde sale la imagen real (grabación propia, vídeo de stock con licencia o vídeo generado).


Lee antes: IDENTIDAD.md, IDEACION.md, RELANZAMIENTO.md y agencia/fabrica-v4/PROPUESTAS.md. Todo es **propuesta**: no se publica nada hasta el OK de Biel. Se ve en el panel/feed: https://claude.ai/artifact/LgY44TbsUR1wkS79NrXksv (slug `9f62c74c-524c-4f00-8f55-c4c92432f775`, colección `posts`).

## Cadena

| Paso | Quién | Salida |
|---|---|---|
| 1. Conceptos | Dani A / Dani B (01) | `agencia/fabrica-v4/conceptos/<id>.md` (ficha de IDEACION.md), 3 conceptos por tema en 3 territorios; post `<id>` en el feed con `status:"idea"`, `tema:"v4 · <fase>"`, `territorio` |
| 2. Crítica | Andrés (05) | `agencia/fabrica-v4/criticas/<id>.md` con la tabla v4; el mejor (≥ 80) pasa a `agencia/fabrica-v4/guiones/<id>.md` y tarea «Montar v4 <id>» en la oficina |
| 3. Recursos | Pau (03) | espacios 3D, objetos, texturas y sonidos en `tools/reel_v5/lib/` (licencias en CREDITOS.md) |
| 4. Montaje | Marta A / Marta B (02) | `tools/reel_v5/<id>/final.mp4` + portada, al feed como `status:"listo"` |
| 5. Carruseles y Stories | Clara (04) | mismo espacio y objetos que su reel, fondo #02050F, texto dentro de la escena |

Prioridad ahora: **las propuestas P01–P12** (PROPUESTAS.md), en el orden del calendario del relanzamiento. Ids: `v4-P01`…

## Montaje v4 (Marta): técnica

- Base técnica: `tools/reel_v5/base/luz.html` (piloto del territorio 8). Three.js 0.170 + postproceso (UnrealBloomPass para halos, ShaderPass de grano y viñeta, OutputPass), sombras suaves, niebla, polvo en suspensión, todo **determinista** en `window.frame(t)` y `window.ready=true`.
- Instalar: `cd tools/reel_v5 && npm i three@0.170 @fontsource/plus-jakarta-sans` (node_modules no se sube).
- Render: `FPS=30 python3 tools/blackout/htmlreel.py video tools/reel_v5/<id>/escena.html tools/reel_v5/<id>/v.mp4 <dur> <audio.wav>` (WebGL por SwiftShader ya configurado en `photo.py`; unos 3 s por fotograma).
- **Una plantilla por territorio** en `tools/reel_v5/base/` (luz, despiece, ruido, retransmision, expediente, columnas, escala). Si no existe la del territorio, la creas a partir de `luz.html` y la dejas ahí para los demás.
- Cámara: un movimiento por idea que **descubre** (dolly, órbita, grúa, atravesar); nada de derivas sin motivo.
- Luz motivada: cada información entra con una fuente de luz y su sonido.
- Texto solo dentro de la escena (pizarra, peto, marcador, pared, pantalla). Plus Jakarta Sans.
- Sonido: biblioteca de `tools/reel_v5/lib/sonidos/` + música por familia (IDENTIDAD.md §8). El piloto usa sonido sintetizado con numpy (sin problemas de licencia). **No usar música de ElevenLabs en nada que vaya a publicarse hasta que Biel confirme la licencia.** Voz de Mateo solo si el concepto la pide, en su registro.
- Silencio de 0,6–1 s antes del momento ultravioleta (una sola vez).
- Revisión: hoja de contacto cada 1 s y test de saltos; mirar que el texto se lee en un móvil y que nada parece plantilla.
- Subida al feed: `list_files`, `publish_files` (patch) con `media/<id>.mp4` y `.jpg`, `db_write posts/<id>` (`status:"listo"`, `tema:"v4 · <fase>"`, `territorio`, `video`, `cover`, `caption`).

## Límites

No se publica nada, no se contacta a nadie, no se toca la web ni la app. Nada inventado, sin precio, sin cifra de apuntados, sin el nombre de Biel. Caras reales solo de fotos/vídeo con licencia y nunca como si apoyaran a ProTeam. Los reels v3 del feed se quedan como archivo; no se rehacen salvo que Biel lo pida.
