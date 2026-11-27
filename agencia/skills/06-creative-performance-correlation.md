# SKILL · Creative Performance Correlation (06 Performance & Learning)
**Para qué:** relacionar características creativas con resultados sin afirmar causas que no están probadas.

## Herramientas
`intel/INDEX.csv` y `intel/videos/<id>/analisis.json` (características medidas), fichas de `agencia/aprendizaje/`, métricas de Windsor, `python3` (csv, statistics).

## Procedimiento
1. **Tabla de características** (`intel/aprendizaje/CARACTERISTICAS.csv`, una fila por pieza publicada). Medidas del análisis: duración · planos · cortes cada 10 s · plano medio · s hasta hook completo · s de la primera palabra · palabras por segundo · n.º de tramos sin movimiento · cola tras la última palabra. Codificadas a mano mirando láminas y documentos (con definición fija): tipo de apertura (cara / escena / texto / producto) · tipo de hook · estructura · territorio · ficha guardable (sí/no y segundos) · forma de mostrar producto · CTA.
2. **Une los resultados** (48 h): saltos 3 s, retención proporcional, guardados y compartidos por 1.000, acción, nota de visita llena.
3. **Compara grupos**, no piezas: mediana de la métrica con y sin la característica, y el **n** de cada grupo.
4. **Escalera de confianza** (se escribe siempre):
   - n < 3 por grupo → **anécdota**. No se concluye nada.
   - 3–5 por grupo y misma dirección → **indicio**. Pasa a hipótesis y a experimento.
   - ≥ 6 por grupo, diferencia clara y sin otra variable que lo explique → **patrón observado**. Sigue sin ser causa.
   - Experimento con una sola variable cambiada y repetido → **evidencia**. Solo esto puede convertirse en recomendación firme.
5. **Busca la explicación rival:** hora, día, tema, duración, persona de la foto, novedad de la cuenta. Si no se puede descartar, se anota.
6. **Redacción obligatoria:** «En n = 4 Reels con ficha guardable, la mediana de guardados por 1.000 fue X frente a Y en n = 3 sin ella [indicio]. Puede deberse también a … Experimento propuesto: …».
7. **Actualiza** `APRENDIZAJES.md`: hechos, hipótesis, experimentos y recomendaciones en sus secciones; nada salta de sección sin cumplir la escalera.

## Nunca
«Funciona porque…» con una pieza · mezclar formatos · leer una media con un valor extremo sin decirlo · cambiar la definición de una característica a mitad de serie.

## Control
¿n por grupo escrito? ¿Nivel de la escalera declarado? ¿Explicación rival considerada?
