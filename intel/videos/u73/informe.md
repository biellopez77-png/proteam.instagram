# u73 · informe técnico (medido, no opinado)

- **Archivo:** `reels/u73-seis-minutos.mp4` · sha256 `9b69494188d2e121…` · fuente: —
- **Marca / tipo / formato / tema:** proteam / propio / reel / Tres exclusiones, seis minutos con uno menos (balonmano, datos corto)
- **Técnica:** 15.367 s · 1080×1920 (9:16) · 30.0 fps · 461 fotogramas leídos · h264 · 1396 kbps
- **Audio:** aac 2 canales 48000 Hz
- **Analizado:** 2026-11-20 02:55 · orden: `python3 tools/video_intel.py analyze reels/u73-seis-minutos.mp4 --id u73 --tema Tres exclusiones, seis minutos con uno menos (balonmano, datos corto) --modo detalle`

## Montaje (automático; confirmar en láminas)
6 planos · 5 cortes duros · 0 transiciones o movimientos fuertes · plano medio 2.56 s (más largo 3.967 s, más corto 1.833 s) · 3.25 cortes cada 10 s

Tramos sin movimiento (≥ 1,5 s): 00:10.67–00:13.00 (2.33 s); 00:13.43–00:15.33 (1.9 s)

| plano | desde | hasta | dura | movimiento | luz |
|---|---|---|---|---|---|
| E1 | 00:00.00 | 00:02.07 | 2.067 s | 0.0028 | 0.207 |
| E2 | 00:02.07 | 00:04.27 | 2.2 s | 0.0069 | 0.105 |
| E3 | 00:04.27 | 00:07.30 | 3.033 s | 0.0102 | 0.926 |
| E4 | 00:07.30 | 00:09.13 | 1.833 s | 0.0192 | 0.152 |
| E5 | 00:09.13 | 00:13.10 | 3.967 s | 0.0036 | 0.089 |
| E6 | 00:13.10 | 00:15.37 | 2.267 s | 0.0163 | 0.9 |

## Texto en pantalla (OCR; verificar)
| desde | hasta | palabras | texto leído |
|---|---|---|---|
| 00:00.00 | 00:00.00 | 5 | 19 EL Bx ROCAS EF |
| 00:00.17 | 00:00.17 | 8 | NACY EL SABADO ROCAS 19 UET 26 EXCLUSIONES |
| 00:00.27 | 00:00.27 | 5 | 10 BORGES EL Bx ROCAS |
| 00:01.60 | 00:02.03 | 1 | EJE |
| 00:02.40 | 00:02.40 | 5 | RC EL SÁBADO ROCAS Nos |
| 00:03.13 | 00:03.13 | 7 | ya EL SÁBADO ROCAS con UNO enos. |
| 00:03.20 | 00:03.20 | 9 | Rey RC EL SABADO ROCAS afl con UNO enos. |
| 00:03.47 | 00:03.47 | 7 | AY Ik “61 con UNO enos. we |
| 00:03.73 | 00:03.73 | 5 | SÁBADO ROCAS con UNO enos. |
| 00:04.53 | 00:05.60 | 1 | 0:00 |
| 00:05.87 | 00:06.40 | 2 | 0:00 Scontra |
| 00:06.67 | 00:07.27 | 5 | EL MARTES 0:00 Scontra MINUTO. |
| 00:07.30 | 00:07.30 | 8 | YE BOR NAGY Lo STAF OCAS 19 26. |
| 00:07.47 | 00:07.73 | 4 | PREGÚN ASELO STAFF ¿CUÁNTAS |
| 00:08.00 | 00:09.10 | 8 | PREGUNTASELO TU STAFF ¿CUÁNTAS este LLE IVA 1S |
| 00:09.33 | 00:13.07 | 13 | LISTA DE ESPERA 04 11 31 02 DÍAS HORAS MIN SEG entrenador@miclub.es CE |
| 00:13.33 | 00:15.33 | 8 | LISTA: SE CIERRA EL 27 NOV Meses gratis. |

## Audio (medido)
Volumen integrado -14.40 LUFS · pico real -0.23 dB · rango 2.60 LU
Silencios (< −38 dB, ≥ 0,25 s): ninguno
Subidas bruscas de energía (posibles golpes o efectos): 00:02.20, 00:02.70, 00:04.10, 00:05.00, 00:13.20
Transcripción: ver `transcripcion.json`

## Láminas y cobertura visual
Fotogramas mirados por un agente: **80 de 461 (17.4 %)**.

| lámina | modo | tramo | fotogramas | vista |
|---|---|---|---|---|
| `laminas/general_001.jpg` | general | 00:00.00–00:09.13 | 18 | sí |
| `laminas/general_002.jpg` | general | 00:10.63–00:15.33 | 7 | sí |
| `laminas/detalle_001.jpg` | detalle | 00:00.00–00:05.33 | 24 | sí |
| `laminas/detalle_002.jpg` | detalle | 00:05.60–00:10.67 | 24 | sí |
| `laminas/detalle_003.jpg` | detalle | 00:10.93–00:15.20 | 18 | sí |

Los juicios (qué funciona, qué falla y por qué) van en `observaciones.md`, cada uno con su marca de tiempo y la lámina donde se ve.
