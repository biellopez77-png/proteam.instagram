# SKILL · Motion Graphics Direction (02 Creative Direction)
**Para qué:** planificar tipografía cinética, máscaras, gráficos y animaciones que comuniquen, no que adornen.

## Herramientas
Producción en HTML/CSS/JS (`tools/reelNN/reel.html`, tiempos en `times.js` salidos de la voz), render con Playwright y ffmpeg. Fuentes en `tools/fonts/`. Verificación con las láminas de `tools/video_intel.py` (modo `window` para ver una animación fotograma a fotograma).

## Procedimiento
1. **Prueba de utilidad:** para cada animación, completa «Esto se mueve para que el espectador entienda/sienta ___». Si no hay respuesta, se quita.
2. **Jerarquía tipográfica:** un solo foco por pantalla. Manrope 800 para el dato o la orden; Instrument Serif itálica azul para la palabra emocional (una por pantalla). Etiquetas pequeñas solo si no hace falta leerlas para entender.
3. **Tamaño mínimo legible en móvil** (sobre 1080 px de ancho): texto principal ≥ 64 px, secundario ≥ 40 px. Nada que haya que leer por debajo de 32 px. Una captura de la app a pantalla de móvil reducida **no se lee**: se amplía la zona que importa.
4. **Entradas y salidas:** entrada en 6–10 fotogramas (0,2–0,33 s), con dirección coherente (lo nuevo entra desde donde mira el sujeto o desde abajo); salida más corta que la entrada. Sin rebotes ni giros gratuitos.
5. **Tiempo de exposición:** `max(0,8 s, 0,3 s × palabras)`. Una ficha «guardable» (lista de 3 líneas) ≥ 2 s completa en pantalla.
6. **Sincronía:** cada entrada cae en la palabra de `times.js`; subrayados y tachados coinciden con la sílaba tónica.
7. **Metáfora visual:** si la idea es abstracta (olvidar, repetir, desordenar), una sola metáfora sostenida todo el Reel (p. ej. la foto que se borra), no una por plano.
8. **Variación:** anota en el documento qué recursos se usan y contrástalos con los tres Reels anteriores (skill `02-visual-originality-audit`).

## Ejemplo medido (u04)
Lámina detalle_002, 00:06,67–00:09,60: ficha «1 Ejercicio · 2 Tiempos · 3 Parejas» visible 2,9 s (cumple). Su cabecera «APUNTA DESPUÉS DE CADA BUEN ENTRENO» es ilegible a ese tamaño: o se sube o se quita. Lámina detalle_003, 00:13,87–00:16,53: captura de la app a móvil pequeño, no se lee hasta la ampliación de 00:16,80.

## Control
¿Cada animación tiene su frase de utilidad? ¿Algún texto por debajo del mínimo? ¿Alguna exposición por debajo de la fórmula?
