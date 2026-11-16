# SKILL · Video Metadata Extraction (03 Resource Bank)
**Para qué:** conocer los datos técnicos reales de cualquier vídeo antes de catalogarlo o usarlo.

## Herramientas (comprobadas en este entorno)
`ffprobe` y `ffmpeg` 6.1, OpenCV 5. Formatos probados: MP4/H.264 + AAC. MOV, WebM y otros que ffmpeg lea funcionan igual.

## Procedimiento
1. **Ficha rápida:**
```bash
ffprobe -v error -print_format json -show_format -show_streams VIDEO
```
   Se leen: contenedor, duración, tamaño, bitrate; vídeo (códec, ancho×alto, `avg_frame_rate`, `pix_fmt`, rotación en `side_data_list`); audio (códec, canales, Hz, bitrate) o su ausencia; etiquetas (fecha de creación, codificador).
2. **Ficha completa y registrada** (recomendado): `python3 tools/video_intel.py analyze VIDEO --id ID --tipo propio|competencia|referencia --modo general`. Deja `intel/videos/ID/analisis.json` con `meta` (incluye sha256, relación de aspecto calculada y fotogramas realmente leídos) y lo apunta en `intel/INDEX.csv`.
3. **Comprobaciones para publicar un Reel propio:** 1080×1920, 9:16, 30 fps, H.264, `yuv420p`, AAC 44,1 o 48 kHz, volumen integrado entre −16 y −13 LUFS y pico real ≤ −1 dB (los da el informe), duración ≤ lo que marque `APRENDIZAJES.md`.
4. **Discrepancias:** si los fotogramas declarados y los leídos no coinciden, o la duración del contenedor y la del vídeo difieren más de 0,1 s, se anota (suele indicar un final cortado o fotogramas duplicados).
5. **Catalogación:** duración, resolución, fps, orientación y si tiene audio pasan a la fila del inventario.

## Lo que los metadatos no dicen
Autor, licencia, fecha real de grabación o lugar, salvo que estén en las etiquetas; y aun así no prueban nada. No se deduce la procedencia de un vídeo por sus metadatos.

## Ejemplo real
`reels/u04-mejor-entreno.mp4`: 25,3 s · 1080×1920 (9:16) · 30 fps · 759 fotogramas · H.264 · 1.835 kbps · AAC estéreo 48 kHz · −14,69 LUFS · pico −1,83 dB.

## Control
¿He medido o he copiado lo que decía el nombre del archivo? ¿Está en el índice?
