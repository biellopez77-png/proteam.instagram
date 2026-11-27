# SKILL · Video Forensic Analysis (05 Critical Lab; la usan 02 y 06)
**Para qué:** auditar el vídeo real, propio o ajeno, con evidencias visuales y marcas de tiempo.

## Herramientas (comprobadas el 16/11 con `reels/u04-mejor-entreno.mp4`)
`tools/video_intel.py` (ffprobe, ffmpeg, OpenCV, tesseract `spa+eng`), Read para ver las láminas. Transcripción: en Reels propios, `voz <id> tools/reelNN/voz.tsv` (exacta, con tiempos por palabra); en vídeos ajenos **no hay transcriptor local** (ver `intel/README.md`, dependencias).

## Procedimiento
1. **¿Ya está analizado?** `python3 tools/video_intel.py buscar <id o marca>`. Si existe y la cobertura es suficiente, se lee `intel/videos/<id>/` y no se repite.
2. **Analiza:** `analyze VIDEO --id ID --marca M --tipo propio|competencia|referencia --tema "…" --fuente "…" --modo detalle`. Para Reel propio, añade `voz ID tools/reelNN/voz.tsv`.
3. **Lee `informe.md`** (lo medido): técnica, planos y duraciones, tramos sin movimiento, texto leído por OCR, volumen, silencios, subidas de energía, frases con su segundo.
4. **Mira todas las láminas del modo elegido**, en orden, y márcalas (`visto`). Para cada duda, `window ID --desde A --hasta B` y se mira el tramo fotograma a fotograma.
5. **Cruza tres líneas de tiempo:** imagen (láminas) · texto en pantalla (verificado a ojo; el OCR solo orienta) · voz (`transcripcion.json`). Busca: texto que llega tarde o se va pronto, corte sin motivo, imagen que no cambia mientras la voz avanza, voz que acaba antes que el vídeo.
6. **Primer segundo:** describe el fotograma 0 y cuándo se puede leer el hook completo.
7. **Reglas fijas:** comprueba en pantalla fecha y oferta exactas, «la app de ProTeam», captura real, personas reconocibles.
8. **Escribe `observaciones.md`** con los 17 puntos del agente. Cada observación: `mm:ss–mm:ss · lámina · qué se ve · por qué importa · corrección`. Se etiqueta como **medido**, **visto** u **opinión**.
9. **Cobertura:** copia la línea de `estado ID` (láminas vistas y % de fotogramas). Lo no visto o no oído se declara.

## Lo que no se puede afirmar
- Entonación, timbre, claridad de la voz o calidad de la mezcla: no se ha escuchado; solo hay medidas (LUFS, silencios, ritmo de palabras).
- Qué música suena, si la hay.
- Nada de un tramo cuyas láminas no se han mirado.

## Ejemplo real (u04, extracto)
`00:22.03–00:22.27 · tramo_20p8-22p5_002 · visto y medido: plano de 0,23 s (7 fotogramas) con «hasta el 28.11» sobre otra foto · un destello así no se lee y parece un error de montaje · alargar a ≥ 0,8 s o quitar el cambio de foto.`

## Control
¿Cada crítica importante tiene marca de tiempo y lámina? ¿Cobertura declarada? ¿He opinado de algo que no he visto u oído?
