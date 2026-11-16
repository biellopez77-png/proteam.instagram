# intel/ · sistema central de análisis de vídeo y biblioteca de conocimiento (16/11)

Compartido por los seis agentes. Un vídeo se analiza **una vez**; todos leen el mismo análisis.
Regla de fondo: **lo medido lo mide la herramienta; lo visto lo ve un agente en las láminas; lo opinado se firma como opinión.** Nadie dice que ha visto lo que no ha mirado.

## 1. Auditoría de capacidades (comprobada el 16/11 en el entorno de trabajo de Claude)
| capacidad | estado | comprobación |
|---|---|---|
| Tipo de agentes | Seis skills de la cuenta de Biel que se ejecutan en sesiones de Claude (a mano o en tareas programadas), con este repositorio como memoria | skills `proteam-*` + `agencia/agentes/` |
| Ejecutar código | Sí (Python 3, shell, 2 CPU, 7 GB) | usado para todo lo de abajo |
| Leer archivos de vídeo (MP4, MOV, WebM…) | Sí | `reels/u04-mejor-entreno.mp4` |
| FFmpeg / FFprobe | Sí (6.1) | metadatos y audio de u04 |
| OpenCV | Sí (5.0) | lectura de los 759 fotogramas y detección de cortes |
| Ver imágenes (visión real) | Sí, con la herramienta Read sobre JPG/PNG | 6 láminas de u04 miradas |
| Secuencias de fotogramas | Sí, como láminas con marca de tiempo (hasta 60 fotogramas por lámina) | modos 1–4 probados |
| OCR | Sí (tesseract, español e inglés); ruidoso con texto animado o sobre foto | tabla de texto de u04; hay que verificar a ojo |
| Procesar audio (medir) | Sí: volumen, silencios, picos de energía | u04: −14,69 LUFS |
| **Escuchar** audio | **No.** El agente no oye: no puede valorar entonación, mezcla ni identificar música | — |
| Transcribir voz | **Reels propios: sí, exacta** (tiempos por palabra de `tools/reelNN/voz.tsv`). **Vídeos ajenos: no** (no hay transcriptor local: la descarga del modelo está bloqueada por la red) | `voz u04` probado; whisper → 403 |
| Leer Instagram / YouTube | **No** desde aquí (sin acceso de red) y no se saltan controles | prueba de conexión fallida |
| Herramientas externas | Sí: Windsor (métricas), ElevenLabs (voz, música, transcripción por enlace), Higgsfield (sandbox con red para Commons), Playwright | en uso por los turnos |
| Compartir skills entre agentes | Sí, por el repositorio (`agencia/skills/`) | 31 archivos |
| Conocimiento compartido | Sí: repositorio + documentos del proyecto + base de datos de la oficina | — |
| Límites | Vídeos ≤ ~400 MB por subida; un Reel de 25 s tarda ~1,5 min en modo detalle; modo completo = 13 láminas por cada 25 s; cada lámina mirada consume contexto: vídeos de más de 3 min, por tramos | medido |

## 2. Arquitectura
```
vídeo (reels/, intel/entrada/, subida a una conversación)
   └─ tools/video_intel.py analyze ─┬─ ffprobe ........ meta (técnica, sha256)
                                    ├─ OpenCV ......... recorrido de TODOS los fotogramas → cortes, planos, movimiento, luz
                                    ├─ OpenCV + PIL ... fotogramas con marca de tiempo → láminas
                                    ├─ tesseract ...... texto en pantalla (orientativo)
                                    └─ ffmpeg ......... audio medido (LUFS, silencios, picos)
   └─ voz ID voz.tsv ................ locución exacta con tiempos (Reels propios)
   └─ agente con Read ............... MIRA las láminas → visto → observaciones.md con marcas de tiempo
   └─ rasgos ID ..................... características medidas → intel/aprendizaje/CARACTERISTICAS.csv
```

## 3. Dónde vive cada cosa
| ruta | qué es | en git |
|---|---|---|
| `intel/INDEX.csv` | índice de vídeos analizados: id, marca, tipo, formato, tema, fecha, fuente, archivo, sha256, duración, cortes, modo, cobertura, ruta | sí |
| `intel/videos/<id>/analisis.json` | todo lo medido + láminas + qué se ha mirado + la orden usada | sí |
| `intel/videos/<id>/informe.md` | informe técnico legible (se regenera solo) | sí |
| `intel/videos/<id>/fotogramas.csv` | una fila por fotograma: tiempo, plano, cambio, movimiento, luz | sí |
| `intel/videos/<id>/laminas/` | láminas con `mm:ss.cc · f<n> · E<plano>` | sí |
| `intel/videos/<id>/transcripcion.json` | locución con tiempos | sí |
| `intel/videos/<id>/observaciones.md` | auditoría con evidencias (05) | sí |
| `intel/videos/<id>/recursos.md` | planos y recursos catalogados (03) | sí |
| `intel/.frames/<id>/` | fotogramas sueltos (`f000123_t0004.100.jpg`), regenerables | no |
| `intel/competencia/` | fichas por cuenta, mapa e informes | sí |
| `intel/insights/INSIGHTS.md` | insights del público con procedencia | sí |
| `intel/aprendizaje/CARACTERISTICAS.csv` | características creativas + resultados (06) | sí |
| `intel/entrada/` | vídeos aportados pendientes de analizar | no (solo su análisis) |
| `agencia/skills/`, `agencia/agentes/` | procedimientos e instrucciones | sí |
| `agencia/criticas/`, `agencia/aprendizaje/`, `agencia/HISTORIAL.md`, `banco/` | auditorías, fichas, publicaciones propias, recursos | sí |

Identificadores: Reels propios, el id de la cola (`u04`); competencia y referencias, `<cuenta>-<nn>` (`ref-unrespiro-01`). Búsqueda: `python3 tools/video_intel.py buscar <marca | tema | formato | fecha>`. Un archivo con la misma huella no se analiza dos veces: la herramienta lo impide.

## 4. Cómo se usa
```bash
# Modo 1 · visión general (rápido): primer segundo + inicio, mitad y final de cada plano
python3 tools/video_intel.py analyze reels/u05-tres-a-cero.mp4 --id u05 --tema "…" --modo general
# Modo 2 · detalle (el normal para auditar): además, 4 fotogramas por segundo y los dos de cada corte
python3 tools/video_intel.py analyze VIDEO --id ID --marca CUENTA --tipo competencia --fuente "URL" --modo detalle
# Modo 3 · fotograma a fotograma: TODOS, 60 por lámina
python3 tools/video_intel.py analyze VIDEO --id ID --modo completo
# Modo 4 · un tramo, todos sus fotogramas
python3 tools/video_intel.py window ID --desde 8 --hasta 14
# Locución exacta de un Reel propio
python3 tools/video_intel.py voz ID tools/reelNN/voz.tsv
# Después de mirar cada lámina con Read
python3 tools/video_intel.py visto ID detalle_001.jpg detalle_002.jpg
python3 tools/video_intel.py estado ID      # cobertura real
python3 tools/video_intel.py rasgos ID      # a la tabla de 06
```
Después: `observaciones.md` (05), `recursos.md` (03), ficha de aprendizaje (06). Procedimientos: `agencia/skills/05-video-forensic-analysis.md`, `03-frame-extraction-cataloging.md`, `02-video-editing-analysis.md`.

## 5. Quién usa qué
| agente | lee | para |
|---|---|---|
| 01 Content Lab | `transcripcion.json`, `observaciones.md` §4–5, fichas de competencia | ideas, estructuras y aperturas |
| 02 Creative Direction | láminas, `informe.md` (planos, tramos parados), matriz de originalidad | composición, montaje, no repetirse |
| 03 Resource Bank | `meta`, láminas, `recursos.md` | catalogar planos y usos |
| 04 Carousel Lab | láminas (uso de texto y jerarquía), fichas de competencia | comunicación visual y estructuras |
| 05 Critical Lab | todo | auditar con evidencias |
| 06 Performance & Learning | `CARACTERISTICAS.csv`, `analisis.json`, `observaciones.md` | relacionar creatividad y resultados |

## 6. Pruebas realizadas (16/11, con `reels/u04-mejor-entreno.mp4`)
| n.º | prueba | resultado |
|---|---|---|
| 1 | Cargar un vídeo | ✔ leído (5,8 MB) |
| 2 | Metadatos | ✔ 25,3 s · 1080×1920 · 30 fps · H.264 · AAC 48 kHz |
| 3 | Extraer fotogramas | ✔ 759 leídos; 116 extraídos en detalle; 52 en el tramo 20,8–22,5 s |
| 4 | Secuencia visual organizada | ✔ 10 láminas (3 general, 5 detalle, 2 tramo) |
| 5 | Un agente ve los fotogramas | ✔ 6 láminas miradas con Read (15,3 % de los fotogramas) |
| 6 | Relacionarlos con sus marcas de tiempo | ✔ p. ej. 00:22.03–00:22.27: plano de 7 fotogramas |
| 7 | Transcribir el audio | ◐ locución exacta importada de `voz.tsv` (70 palabras con tiempos). Reconocimiento de voz por oído: **no disponible** |
| 8 | Cambios de escena | ✔ 8 cortes, 9 planos; contrastados a ojo en las láminas |
| 9 | Informe audiovisual | ✔ `informe.md` + `observaciones.md` (17 puntos, 77/100) |
| 10 | Critical Lab usa el análisis | ✔ auditoría con marcas de tiempo y 5 correcciones |
| 11 | Resource Bank registra recursos | ✔ `recursos.md` (7 recursos con segundo de uso; 1 fila de inventario pendiente) |
| 12 | Performance & Learning usa el resultado | ✔ fila de u04 en `CARACTERISTICAS.csv`; métricas vacías hasta que se publique |
No probado: modo completo sobre un vídeo entero (sí la extracción de todos los fotogramas de un tramo), vídeos MOV, vídeos de otras marcas (no hay ninguno).

## 7. Limitaciones
1. El agente **no oye**. Del audio solo hay medidas y, en Reels propios, el texto exacto.
2. Sin transcripción automática para vídeos ajenos.
3. Sin acceso a Instagram ni YouTube: la competencia entra como archivo.
4. OCR orientativo: falla con texto animado, fino o sobre foto. El texto se verifica en las láminas.
5. La detección de cortes es automática: un motion graphic continuo cuenta como un plano; un fundido lento puede no contarse.
6. Mirar todos los fotogramas de un vídeo largo es caro: se hace por tramos y se declara la cobertura.
7. Las láminas ocupan ~3,5 MB por Reel en el repositorio.

## 8. Dependencias pendientes (qué necesita intervención)
| qué | para qué | quién |
|---|---|---|
| Vídeos de otras marcas como archivo (o capturas) en `intel/entrada/` o en una conversación, con su URL | análisis de competencia (hoy: 0 piezas) | Biel |
| Permitir el dominio `huggingface.co` en Ajustes → Capacidades de claude.ai (red del entorno) | instalar un transcriptor local (faster-whisper se instala con pip; lo que falla es la descarga del modelo) | Biel |
| Alternativa a lo anterior: transcripción de ElevenLabs con un enlace público al audio | transcribir vídeos ajenos | por probar |
| Capturas de la curva de retención de Instagram | análisis de abandono segundo a segundo | Biel |
| Decidir el rótulo de fecha: «HASTA EL 28 NOV» (MARCA.md) o «hasta el 28.11» (como sale desde u01) | unificar documentos y auditoría | Biel |
