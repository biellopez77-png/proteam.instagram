# u72 · informe técnico (medido, no opinado)

- **Archivo:** `reels/u72-once-cinco-siete.mp4` · sha256 `b70dbf43f0d45577…` · fuente: —
- **Marca / tipo / formato / tema:** proteam / propio / reel / contexto: dato corto 11·5·7, tres deportes el mismo lunes
- **Técnica:** 17.133 s · 1080×1920 (9:16) · 30.0 fps · 514 fotogramas leídos · h264 · 1935 kbps
- **Audio:** aac 2 canales 48000 Hz
- **Analizado:** 2026-11-19 00:02 · orden: `python3 tools/video_intel.py analyze reels/u72-once-cinco-siete.mp4 --id u72 --tema contexto: dato corto 11·5·7, tres deportes el mismo lunes --modo detalle`

## Montaje (automático; confirmar en láminas)
9 planos · 8 cortes duros · 0 transiciones o movimientos fuertes · plano medio 1.9 s (más largo 2.967 s, más corto 0.233 s) · 4.67 cortes cada 10 s

Tramos sin movimiento (≥ 1,5 s): 00:02.83–00:04.37 (1.53 s); 00:06.90–00:09.57 (2.67 s); 00:10.57–00:12.50 (1.93 s)

| plano | desde | hasta | dura | movimiento | luz |
|---|---|---|---|---|---|
| E1 | 00:00.00 | 00:01.40 | 1.4 s | 0.0011 | 0.219 |
| E2 | 00:01.40 | 00:04.37 | 2.967 s | 0.0031 | 0.327 |
| E3 | 00:04.37 | 00:06.07 | 1.7 s | 0.0085 | 0.179 |
| E4 | 00:06.07 | 00:06.30 | 0.233 s | 0.0167 | 0.044 |
| E5 | 00:06.30 | 00:06.60 | 0.3 s | 0.031 | 0.111 |
| E6 | 00:06.60 | 00:09.57 | 2.967 s | 0.0055 | 0.294 |
| E7 | 00:09.57 | 00:12.50 | 2.933 s | 0.0078 | 0.176 |
| E8 | 00:12.50 | 00:15.07 | 2.567 s | 0.0055 | 0.091 |
| E9 | 00:15.07 | 00:17.13 | 2.067 s | 0.0078 | 0.19 |

## Texto en pantalla (OCR; verificar)
| desde | hasta | palabras | texto leído |
|---|---|---|---|
| 00:00.17 | 00:00.50 | 2 | EN JUEGO |
| 00:00.67 | 00:00.80 | 2 | EN JUEGO |
| 00:01.40 | 00:01.40 | 5 | Ta, wy id NW TE |
| 00:01.87 | 00:02.13 | 1 | ye |
| 00:02.87 | 00:02.87 | 7 | JUEGO wy mS SP. ST! BALONMANO yA |
| 00:02.93 | 00:02.93 | 7 | Ba Use no Tap mS SP. BALONMANO |
| 00:03.20 | 00:03.20 | 6 | VEGO Tap SP. er BALONMANO Zs |
| 00:03.47 | 00:03.47 | 7 | Ji VEGO id SP. le BALONMANO ST! |
| 00:03.73 | 00:03.73 | 5 | ye a2 Az ESTO BALONMANO |
| 00:04.00 | 00:04.00 | 6 | JUEGO a2 SP, Az ONCESTO BALONMANO |
| 00:04.27 | 00:04.27 | 5 | SP. ME BALONMANO STO pu |
| 00:04.37 | 00:04.37 | 7 | pr! De wh ad sp Az ra |
| 00:05.07 | 00:05.07 | 5 | 54 ye Ny EDO ad |
| 00:05.87 | 00:05.87 | 7 | om, Za sD la ad ES] pu |
| 00:06.07 | 00:09.53 | 8 | TRES DEPORTES ELMISMO lunes PC SEMANA CONVOCATORIA MINUTOS |
| 00:10.40 | 00:10.40 | 5 | ES ye ad Ry 45) |
| 00:10.93 | 00:11.47 | 3 | POR ESO ProTeam. |
| 00:12.00 | 00:12.47 | 2 | POR ESO |
| 00:12.53 | 00:15.03 | 12 | LISTA DE ESPERA 08 09 17 23 DÍAS HORAS MIN SEG entrenador@miclub.es| |
| 00:15.47 | 00:16.27 | 4 | HASTA EL 27 NOV |
| 00:16.53 | 00:17.07 | 2 | 27 NOV |

## Audio (medido)
Volumen integrado -14.31 LUFS · pico real -0.16 dB · rango 2.50 LU
Silencios (< −38 dB, ≥ 0,25 s): ninguno
Subidas bruscas de energía (posibles golpes o efectos): 00:01.40, 00:04.40, 00:05.40, 00:09.60, 00:11.10, 00:15.10
Transcripción: ver `transcripcion.json`

## Láminas y cobertura visual
Fotogramas mirados por un agente: **31 de 514 (6.0 %)**.

| lámina | modo | tramo | fotogramas | vista |
|---|---|---|---|---|
| `laminas/general_001.jpg` | general | 00:00.00–00:06.43 | 18 | sí |
| `laminas/general_002.jpg` | general | 00:06.57–00:17.10 | 13 | sí |
| `laminas/detalle_001.jpg` | detalle | 00:00.00–00:05.07 | 24 | NO |
| `laminas/detalle_002.jpg` | detalle | 00:05.33–00:09.57 | 24 | NO |
| `laminas/detalle_003.jpg` | detalle | 00:09.60–00:15.03 | 24 | NO |
| `laminas/detalle_004.jpg` | detalle | 00:15.07–00:17.07 | 9 | NO |

Los juicios (qué funciona, qué falla y por qué) van en `observaciones.md`, cada uno con su marca de tiempo y la lámina donde se ve.
