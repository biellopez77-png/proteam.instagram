# Crítica de vídeo E02 · «De noche»

Andrés (05) · 24/11 · criterio v4 (Biel, 24/11) · vídeo `tools/reel_v5/piezas/E02/final.mp4` (1080×1920, 25 fps, 13,48 s) · spec `piezas/E02/spec.json` · fase del spec: Calentamiento · vie 27/11.
Método: un fotograma por segundo a 360 px de ancho (móvil) y cuatro por segundo en hoja de 180 px; muestreo a 10 fps para el violeta; sonido en ventanas de 0,1 s (RMS) con ffmpeg + numpy; licencias contra `banco/INVENTARIO.csv`.

## Nota: **69/100 · SUSPENSO** (un suspenso directo: texto cortado) → vuelve a montaje

| Criterio | Peso | Nota | Por qué |
|---|---|---|---|
| Idea editorial clara | 25 | 19 | «De noche / frío / otra vez / alguien sigue pensando en el sábado / algo se está encendiendo» es una idea limpia y de calentamiento. Pero la palabra que la abre (DE NOCHE) no se lee nunca entera, y las fotos son de día con cielo de nubes blancas: la imagen contradice el titular. |
| Legibilidad en móvil | 20 | 10 | DE NOCHE nunca completo; OTRA VEZ casi invisible y cortado; entradilla, pies, hora y «Con lluvia. Con seis.» en mono pequeño (≈7–9 px en móvil). Lo único que se lee bien: FRÍO, «y ahí sigue.», la frase serif y el cierre. |
| Ritmo y sonido | 15 | 9 | Estructura correcta (paneo con rampa, desenfoque, paso de página). Pero satura: pico de **+0,46 dBFS a 2,67 s** (corte a FRÍO). Zumbido plano a −19 dB de 0,8 a 9,6 s; el silencio antes de la frase dura 0,3 s (7,8–8,1, −51 dB) y es casi imperceptible; el acorde del ultravioleta solo sube +4 dB (−15 dB a 10,2–10,4); el pico de 11,9 s (−12 dB) está en el paso de página, no en el cierre; el audio acaba a −21 dB en 13,3 s y los últimos 0,4 s de vídeo son negro. |
| Encaje de fase | 15 | 11 | Calentamiento: sin app, sin fecha, sin explicar, bien; la línea «algo se está encendiendo» es exactamente el tono. Falla el territorio 8 (espacios a oscuras, una luz): las cinco fotos son de día. |
| Identidad | 15 | 13 | Paleta, duotono, grano, Jakarta 800 + Instrument Serif + Plex Mono, folios (p. 01 → pp. 03–04) y créditos: en su sitio, no parece plantilla. Un solo ultravioleta medido (subrayado de «el sábado», 9,9–11,4 s). La línea del cierre mide (122,108,247): azul #636DFF mezclado; comprobar en el spec que es azul. |
| Verdad | 10 | 7 | Sin cifras, precio ni apuntados. Todas las fotos con licencia (DP, CC BY-SA 2.0, CC BY 4.0, CC BY 3.0). **Pero** `ENTRENADOR_ENTRENADORA_INDICA_FOTO_001` es Cindy Parlow Cone (exinternacional y presidenta de US Soccer, según el propio enlace del inventario): dentro de FRÍO no se le ve la cara, así que no es suspenso directo, pero es una persona conocida y la foto no aporta nada (dentro de las letras solo se ve cielo). «Noviembre · 18:30 · Ya no hay luz» sobre una foto a pleno día. |
| **Total** | 100 | **69** | |

## Suspensos directos

| Regla | ¿Cae? | Dónde |
|---|---|---|
| Algo en 3D | No | Todo 2D. |
| **Texto cortado o que se pisa** | **Sí** | 0,0–2,6 s: DE NOCHE cruza más ancho que la página y nunca se ve entero: «DE NO» → «NOCH» → «OCHE». En móvil se lee «NOCHE» a medias. 6,2–7,0 s: OTRA VEZ entra cortado por la izquierda («O VE», «TRA», «RA») y durante el desenfoque se dobla («ODTRA VIEZ»). 5,0 s: el pie de la Fig. 3 queda cortado por el borde («Fig. 3 — El cro…»). |
| Más de un momento ultravioleta | No | Solo el subrayado de 9,9–11,4 s. |
| Datos inventados, precio o apuntados | No | |
| Caras de famosos o fotos sin licencia | No (rozando) | Foto de Cindy Parlow Cone en FRÍO, sin cara visible. Cambiarla igualmente. |
| Parece plantilla genérica | No | |

## Marcas de tiempo

- **0,0–2,6 · p. 01 DE NOCHE.** Foto del campo en duotono, bonita pero diurna. La palabra cruza y no se completa. «Noviembre · 18:30 · Ya no hay luz» y el pie, en mono ilegible.
- **2,6–2,7 · corte a FRÍO.** Golpe que satura (+0,46 dBFS), el pico de toda la pieza, demasiado pronto.
- **2,7–5,0 · p. 02 FRÍO / y ahí sigue.** Se lee muy bien. La foto dentro de las letras no se distingue (cielo). «Con lluvia. Con seis. Con los que vengan.» en mono pequeño: es la mejor línea de entrenador y se pierde.
- **5,0–7,9 · pp. 03–04 retícula.** Paneo con rampa por conos → cronómetro → pizarra; empuje hacia la pizarra correcto. OTRA VEZ de fondo, gris sobre negro, cortado y doblado: no se lee ni aporta. Pies ilegibles.
- **7,8–8,1 · silencio** (−51 dB una sola ventana). Demasiado corto para que se note.
- **8,1–11,5 · p. 05 frase + UV.** «Y cuando se apagan los focos,» en mono 26 px (ilegible) / «alguien sigue / pensando en el sábado.» en serif, bien. Subrayado violeta 9,9–11,4: correcto y único. 1,5 s quieto antes del paso de página: vale.
- **11,5–11,8 · paso de página**, 11,8–13,0 cierre «ProTeam / algo se está encendiendo.» 13,0–13,48 negro, el audio corta a −21 dB.

## Correcciones concretas (para Marta, campos de `piezas/E02/spec.json`)

1. **p. 1 `palabra`**: añadir `"size": 190, "left": 40, "cruce": 30` (como DOMINGO) y comprobar en la hoja (`build.py E02 --still`) que «DE NOCHE» se ve completo ≥ 0,6 s. Si no cabe, `"palabra": "NOCHE"`.
2. **p. 1 `foto`**: cambiar por una foto de noche o con focos encendidos (buscar en `banco/fotos` con estado disponible; si no hay, pedir a Pau una de territorio 8). Si no la hay, cambiar `hora` a algo que no contradiga la foto (p. ej. «Noviembre · 17:50 · Se va la luz»).
3. **p. 2 `dentro`**: cambiar `"foto"` de `ENTRENADOR_ENTRENADORA_INDICA_FOTO_001` (persona conocida) por una textura u objeto con contraste dentro de las letras (p. ej. `OBJETO_BALON_LINEA_FOTO_001` o una de lluvia/hierba). Añadir `"capSize": 40` para que «Con lluvia. Con seis. Con los que vengan.» se lea.
4. **pp. 3–4 `reticula`**: añadir `"labSize": 40`. Quitar `"letras": "OTRA\nVEZ"` o pasarlo a la `cap` de la p. 2 («Otra vez.»); de fondo no se lee.
5. **p. 5 `frase`**: añadir `"preSize": 44` para la entradilla y subir `"d"` de 3,2 a **3,6** (dejar ≥ 1 s de violeta quieto y aire antes del paso).
6. **p. 6 `cierre`**: subir `"d"` de 1,9 a **2,2** y que el vídeo no acabe en negro (comprobar que la duración del render = suma de `d`).
7. **Sonido** (motor): limitar el golpe del corte p. 1→p. 2 a −6 dBFS como máximo (ahora satura); papel/obturador +6 dB sobre el zumbido en cada corte y foto; silencio antes de la frase ≥ 0,6 s; acorde UV a +10 dB sobre el zumbido; resolución en el cierre (no en el paso de página) con caída a −40 dB al final.
8. **Comprobar** que la línea del cierre es #636DFF (azul) y no violeta.

Con 1, 3, 4 y 5 resueltos sube a legibilidad ~16 y verdad 9; con el sonido y la foto nocturna debería pasar de 80.
