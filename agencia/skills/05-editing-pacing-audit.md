# SKILL · Editing & Pacing Audit (05 Critical Lab)
**Para qué:** juzgar el ritmo y el montaje con números y con ojos, y decir dónde falla.

## Herramientas
`intel/videos/<id>/informe.md` y `analisis.json` (planos, cortes, tramos sin movimiento, energía de audio), `fotogramas.csv` (movimiento por fotograma), `transcripcion.json`, láminas.

## Procedimiento
1. **Tabla de planos** (del informe): duración de cada uno. Marca: > 4 s (largo), < 0,4 s (destello), y la secuencia de duraciones.
2. **Curva de ritmo:** ¿las duraciones se acortan hacia el giro y se alargan en la idea clave y la ficha guardable? Un ritmo plano o al revés se señala.
3. **Tramos sin movimiento ≥ 1,5 s:** para cada uno, mira la lámina: ¿está justificado (lectura de una ficha, pausa dramática) o es una imagen parada mientras la voz sigue?
4. **Cortes con motivo:** cada corte duro frente a `transcripcion.json` y a las subidas de energía (±0,15 s). Lista los que no coinciden con inicio de frase, palabra de impacto ni golpe.
5. **Densidad:** palabras por segundo de la locución (objetivo ~3) y cambios visuales por cada 5 s. Tramo con más de 5 s de voz y un solo estado visual = se cae la atención.
6. **Exposición de textos:** con las láminas de detalle (resolución 0,25 s) o tramo, mide cuánto está cada texto completo en pantalla frente a `max(0,8 s, 0,3 s × palabras)`.
7. **Arranque y final:** tiempo hasta la primera palabra (≤ 0,3 s), hook completo legible (≤ 1 s), y cola tras la última palabra (≤ 0,8 s).
8. **Repetición visual:** misma composición en dos planos seguidos sin intención.
9. **Veredicto de ritmo** con las tres correcciones de mayor impacto, cada una con segundo, causa y arreglo.

## Ejemplo real (u04)
Planos: 3,17 · 1,13 · 2,10 · 7,47 · 5,03 · 2,03 · 1,10 · 0,23 · 3,03 s. El plano de 7,47 s (00:06,40–00:13,87) contiene cuatro estados (ficha, borrado, «sensación», «no se repiten»): bien resuelto por dentro. Problemas: destello de 0,23 s en 00:22,03; cola de 1,6 s tras la última palabra (voz acaba 00:23,70, vídeo 00:25,30); arranque fijo 1,67 s (00:00,73–00:02,40).

## Control
¿Números sacados del informe, no estimados a ojo? ¿Cada problema con segundo y arreglo? ¿He mirado las láminas de los tramos señalados?
