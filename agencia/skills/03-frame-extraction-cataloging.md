# SKILL · Frame Extraction & Cataloging (03 Resource Bank; base del sistema de vídeo)
**Para qué:** sacar fotogramas con su marca de tiempo, verlos de verdad y catalogar planos.

## Herramientas (comprobadas)
`tools/video_intel.py` (OpenCV + PIL). Los fotogramas sueltos van a `intel/.frames/<id>/` (fuera de git, regenerables con la orden guardada en `analisis.json`); las **láminas** con marca de tiempo van a `intel/videos/<id>/laminas/` (en git). Cada fotograma se llama `f<número>_t<segundos>.jpg`.

## Los cuatro modos
| modo | orden | qué extrae |
|---|---|---|
| 1 General | `analyze … --modo general` | primer segundo en detalle + inicio, mitad y final de cada plano |
| 2 Detalle | `analyze … --modo detalle [--fps 4]` | lo anterior + un fotograma cada 1/fps s + los dos fotogramas de cada corte |
| 3 Completo | `analyze … --modo completo` | **todos** los fotogramas, en láminas de 60 |
| 4 Tramo | `window ID --desde 8 --hasta 14` | todos los fotogramas del intervalo, en láminas de 40 |

## Procedimiento
1. Comprueba en `intel/INDEX.csv` si el vídeo ya está analizado (misma huella = no se repite).
2. Lanza el modo que pida la tarea. Un Reel de 25 s a 30 fps son ~760 fotogramas: modo completo = 13 láminas.
3. **Mira cada lámina con Read**, en orden. Cada casilla lleva `mm:ss.cc · f<número> · E<plano>`.
4. Apunta lo mirado: `python3 tools/video_intel.py visto ID lamina1.jpg lamina2.jpg`. `estado ID` dice el porcentaje de fotogramas realmente vistos y qué láminas faltan. **No se afirma «visto entero» con láminas sin marcar.**
5. **Registro por fotograma** cuando se pida (modo 3 o 4): tabla en `intel/videos/<id>/registro_fotogramas.md` con fotograma · marca de tiempo · lámina · plano · qué se ve · elementos · texto visible · movimiento respecto al anterior · observación. Los fotogramas idénticos consecutivos se agrupan en un rango («f24–f93, sin cambios») y se dice.
6. **Catálogo de planos** (vídeos propios): por cada plano, si contiene un recurso reutilizable (foto, captura, animación), se anota en la ficha del recurso «usada en <id> · 00:mm:ss». De vídeos ajenos se cataloga **la referencia** (qué recurso usan y para qué), nunca el material.
7. Si el volumen es grande (más de 20 láminas), se trabaja por lotes de 5 láminas, conservando el orden, y se declara dónde se paró.

## Límites reales
Una lámina de 60 casillas reduce cada fotograma a 200 px de ancho: sirve para movimiento y cortes, no para leer texto pequeño; para eso, modo tramo (250 px) o abrir el fotograma suelto de `.frames/`.

## Control
¿`estado` coincide con lo que digo haber visto? ¿Registro con marcas de tiempo? ¿Original referenciado (ruta y sha256)?
