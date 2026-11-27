# Crítica de vídeo E03 · «El silbato»

Andrés (05) · 24/11 · criterio v4 (Biel, 24/11) · vídeo `tools/reel_v5/piezas/E03/final.mp4` (1080×1920, 25 fps, 13,48 s, commit 280b1eb) · spec `piezas/E03/spec.json` · fase del spec: Calentamiento · sáb 28/11.
Método: un fotograma por segundo a 360 px de ancho (móvil) y cuatro por segundo en hoja de 180 px; sonido en ventanas de 0,1 s (RMS y pico) con ffmpeg + numpy y `volumedetect` a 48 kHz; licencias contra `banco/INVENTARIO.csv`.

## Nota: **66/100 · SUSPENSO** (dos suspensos directos: texto cortado y cara de persona conocida) → vuelve a montaje

| Criterio | Peso | Nota | Por qué |
|---|---|---|---|
| Idea editorial clara | 25 | 20 | La mejor idea de las de calentamiento: «90' — lo que se ve dura noventa minutos / lo que no se ve dura toda la semana / hoy se juega lo que se preparó entre semana». Se entiende sin la app. Pero la palabra que abre (SÁBADO) no se lee entera y la mitad de la idea («lo que no se ve dura toda la semana») va en mono diminuto. |
| Legibilidad en móvil | 20 | 10 | SÁBADO nunca completo (0,0–2,5 s: «SÁBA» → «ÁBAD» → «BADO»). Pie de la Fig. 1 montado encima de la foto. «Lo que no se ve dura toda la semana», «Faltan diez minutos», pies de las figuras y la entradilla «Hoy se juega»: mono ≈7–9 px en móvil. LUNES/MARTES/JUEVES gris sobre negro, cortado por la izquierda y pisado por la Fig. 4. Se leen bien: 90', la serif de la p. 2, la frase de la p. 5 y el cierre. |
| Ritmo y sonido | 15 | 9 | Estructura buena (cruce, cifra, paneo con rampa, empuje a la Fig. 4, foto a sangre, cierre). Sonido: pico a **−0,9 dBFS en 2,58 s** (corte a 90'), casi saturando y en el sitio equivocado; zumbido plano a −19 dB de 0,8 a 7,7 s; silencio antes de la frase solo 0,2 s (8,0–8,1, −50 dB); acorde UV +4 dB (−15 dB a 10,3–10,4); el golpe más alto del final (−11,8 dB a 11,9 s) cae en el paso de página, no en el cierre; 13,0–13,48 s negro y el audio corta a −22 dB. |
| Encaje de fase | 15 | 11 | Calentamiento: sin app, sin fecha, sin explicar, bien; «para el que lo prepara» deja el misterio. SÁBADO es un día, no una fecha: vale. Pero no hay nada de territorio 8 (oscuridad, una luz): silbatos sobre fondo blanco y fotos de pabellón iluminado. |
| Identidad | 15 | 12 | Paleta, duotono, grano, Jakarta 800 + Instrument Serif + Plex Mono, folios (p. 01, p. 02, pp. 03–04, p. 05) y créditos abajo: correcto y no parece plantilla. Un solo ultravioleta (subrayado 9,9–12,0 s). Resta: la foto de silbatos sobre blanco rompe el duotono (queda casi blanca, parece recorte de catálogo) y el texto de fondo de la retícula se monta con la figura. |
| Verdad | 10 | 4 | Sin cifras inventadas (90' es la duración de un partido), sin precio ni apuntados; todas las fotos con licencia (CC BY-SA 4.0, CC BY-SA 3.0, CC BY 2.0). **Pero** la Fig. 4 `STAFF_PIZARRA_JUGADA_FOTO_001` es **Mike Montgomery** (el propio enlace del inventario: `Mike_Montgomery_diagramming_play.jpg`), entrenador conocido, con la cara visible y grande de 6,8 a 9,8 s (empuje incluido). Además la Fig. 3 es un staff profesional (Thüringer HC, EHF) con caras reconocibles. |
| **Total** | 100 | **66** | |

## Suspensos directos

| Regla | ¿Cae? | Dónde |
|---|---|---|
| Algo en 3D | No | Todo 2D. |
| **Texto cortado o que se pisa** | **Sí** | 0,0–2,5 s: SÁBADO nunca entero («SÁBA», «ÁBAD», «BADO»). 0,0–0,7 s: pie «Fig. 1 — Dos silbatos. Uno de reserva.» encima de la foto. 5,8–7,3 s: LUNES/MARTES/JUEVES cortado por la izquierda («ES / RTES / VES») y JUEVES pisado por la Fig. 4. 5,3–6,0 s: Fig. 3 cortada por el borde derecho y su pie («Fig. 3 — Notas…») truncado. 7,0 s: pie de la Fig. 4 empieza fuera de cuadro («4 — La jugada, otra vez»). |
| Más de un momento ultravioleta | No | Solo el subrayado de 9,9–12,0 s. |
| Datos inventados, precio o apuntados | No | |
| **Caras de famosos o fotos sin licencia verificada** | **Sí** | Fig. 4 = Mike Montgomery, cara visible 6,8–9,8 s. |
| Parece plantilla genérica | No | |

## Marcas de tiempo

- **0,0–2,5 · p. 01 SÁBADO.** Silbatos sobre blanco (duotono casi blanco). La palabra cruza y no se completa; «Faltan diez minutos» y el pie en mono ilegible; el pie arranca pisando la foto.
- **2,5–2,6 · corte a 90'.** Golpe a −0,9 dBFS, el pico de toda la pieza; demasiado pronto y demasiado alto.
- **2,6–5,0 · p. 02 cifra.** 90' y «dura noventa minutos.» se leen muy bien. «Lo que no se ve / dura toda la semana.» (la mitad de la idea) en mono pequeño: se pierde.
- **5,0–7,9 · pp. 03–04 retícula.** Paneo con rampa Fig. 2 → Fig. 3 → Fig. 4 y empuje: buen movimiento. LUNES/MARTES/JUEVES de fondo, cortado y pisado. Fig. 4 con la cara de Montgomery a toda página 7,5–8,0 s.
- **8,0–8,1 · silencio** (−50 dB una sola ventana). No se nota.
- **8,1–12,0 · p. 05 frase + UV.** Balón en la línea, duotono bonito. «Hoy se juega» en mono ilegible; «lo que se preparó / entre semana.» serif, bien. Subrayado violeta 9,9–12,0: único y con tiempo quieto.
- **12,0–13,0 · paso de página y cierre** «ProTeam / para el que lo prepara.» Bien, pero corto (≈1 s legible). **13,0–13,48 negro**, el audio corta a −22 dB.

## Correcciones concretas (para Marta, campos de `piezas/E03/spec.json`)

1. **p. 1 `palabra`**: añadir `"size": 190, "left": 40, "cruce": 30` (como DOMINGO) y comprobar en la hoja (`build.py E03 --still`) que «SÁBADO» se ve completo ≥ 0,6 s.
2. **p. 1 `foto`**: cambiar `OBJETO_GENERAL_FOTO_002` (silbatos sobre blanco) por un objeto sobre fondo oscuro o con una luz (territorio 8). Si no hay, pedir a Pau un silbato en penumbra; de momento vale `OBJETO_BALON_LINEA_FOTO_001` recortado distinto o una de banquillo vacío. Mover el pie para que no pise la foto (o acortar `fig` a «Fig. 1 — Dos silbatos.»).
3. **p. 2 `cap`**: es la mitad de la idea; pasarla a serif o añadir `"capSize": 44` (si el tipo `cifra` no lo admite, mover «Lo que no se ve dura toda la semana.» a `serif` de una página propia `frase` sin UV o meterla en la `pre` de la p. 5).
4. **pp. 3–4 `figs[2].foto`**: **quitar `STAFF_PIZARRA_JUGADA_FOTO_001` (Mike Montgomery)**. Sustituir por `ENTRENADOR_TIEMPO_MUERTO_PIZARRA_FOTO_001` solo si Pau confirma que no es una persona conocida, o por una pizarra/libreta sin cara. Revisar también `STAFF_TRABAJO_FOTO_003` (staff profesional del Thüringer HC con caras): mejor una mesa de notas sin caras.
5. **pp. 3–4 `reticula`**: añadir `"labSize": 40`; quitar `"letras"` (LUNES/MARTES/JUEVES no se lee y se pisa con la Fig. 4) o pasarlo a la `pre` de la p. 5 («Lunes. Martes. Jueves.»). Comprobar que la Fig. 3 y su pie entran enteros en cuadro.
6. **p. 5 `frase`**: añadir `"preSize": 44` y subir `"d"` de 3,1 a **3,6**.
7. **p. 6 `cierre`**: subir `"d"` de 1,9 a **2,2** y que el vídeo no acabe en negro (duración del render = suma de `d`).
8. **Sonido** (motor, igual que E02): golpe del corte p. 1→p. 2 a −6 dBFS como máximo; papel/obturador +6 dB sobre el zumbido en cada corte y foto; silencio antes de la frase ≥ 0,6 s; acorde UV +10 dB sobre el zumbido; resolución en el cierre con caída a −40 dB al final.

Con 1, 4 y 5 se quitan los dos suspensos directos; con 3, 6 y el sonido debería pasar de 80 (legibilidad ~16, verdad 9, ritmo 12).
