# Montaje base de la serie POV (P1–P4)

Encargo de Biel (20/11, t-mis20-02-pov). Guiones: `agencia/guiones/2026-11-20-pov-serie-camara-en-mano.md`. Gráficos: `agencia/recursos/pov/` (fuentes en `tools/pov/`).

## Cuando llegue la grabación
1. Guarda las tomas en orden (una por frase) y monta:
   `python3 tools/reelPOV/montar.py P1 --clips toma1.mp4 toma2.mp4 … --margen 1 --musica musica.mp3 --salida reels/p1-domingo-a-las-once.mp4`
   - `--margen 1` quita el segundo de margen que Biel deja al principio y al final de cada toma.
   - La voz es la del clip. Si Biel no habla, `--voz voz.wav` con Mateo (regla de siempre: ningún Reel sin voz, y dentro del tope diario).
   - La música baja al 60 % cuando hay voz.
2. Ajusta en `planes.json` los segundos `de` y `a` de cada gráfico a la voz real (los que hay son los del guion).
3. Mira el vídeo: si un gráfico tapa las manos o la pantalla, muévelo con `dy` (píxeles, negativo sube) o hazlo más pequeño con `escala`. Los gráficos acompañan y nunca tapan al protagonista.
4. Después, lo de todos los Reels: análisis del vídeo, auditoría de Andrés con encaje de fase y a la cola. P3 no se monta hasta que R4 confirme que las pantallas grabadas son la versión publicada. P4 necesita el visto bueno de Biel.

## Qué hace
- El vídeo de Biel se ve siempre entero (1080×1920, 30 fps, recorte al centro); no se oscurece.
- Cada gráfico entra con su WebM con alfa (0,5 s), se queda fijo y sale en seco en su corte. Si dos gráficos se pisan en `planes.json`, no monta.
- Palabra clave: `{"g": "g10-palabra", "texto": "23:04", …}` genera la g10 con ese texto. `"tachado": true` tacha el gráfico en rojo (los mensajes de P3).
- Cierre: g09 en los últimos 3 s de cada plan.

## Probar sin grabación
`python3 tools/reelPOV/montar.py P1 --prueba` monta el plan sobre un fondo de prueba con reloj (queda en `tools/reelPOV/_cache/`, que no se sube). Probado el 20/11 con P1, P2 y P3, y con dos tomas de tamaños y fps distintos más música.
