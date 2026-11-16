# SKILL · Social Media Performance Analysis (06 Performance & Learning)
**Para qué:** leer los resultados reales de Instagram frente al objetivo de cada pieza.

## Herramientas (comprobadas en sesiones anteriores)
Windsor.ai `get_data` (connector `instagram`, cuenta `17841445998297098`; consultar `get_fields` antes). Campos por publicación: `media_id`, `timestamp`, `media_type`, `media_caption`, `media_views`, `media_reach`, `media_reel_avg_watch_time`, `media_reel_skip_rate`, `media_saved`, `media_shares`, `media_reel_total_interactions`, likes y comentarios si existen. Cuenta: seguidores, visitas al perfil, toques en enlaces. Web y altas: analítica de Lovable (**solo lectura**). **No disponible:** visitas al perfil y seguidores por Reel; curva de retención segundo a segundo.

## Procedimiento
1. **Cruza** `queue.json` (`media_id`, `id`, hora) con los datos. Cada pieza se lee a las **24 h y a las 48 h** de publicarse; nunca antes de 20 h.
2. **Tabla base por pieza:** vistas · alcance · tiempo medio · % saltos en 3 s · guardados · compartidos · comentarios · interacciones.
3. **Tasas (fórmula siempre a la vista):** retención media = tiempo medio / duración · guardados por 1.000 = guardados / vistas × 1.000 · compartidos por 1.000 · interacción = interacciones / alcance.
4. **Contra el objetivo declarado** (de la entrega de 01 o 04): identificación → compartidos y comentarios; educación → guardados; conversión → toques en enlace y altas en 48 h; alcance → vistas y saltos. Una pieza se juzga por **su** métrica, no por las vistas.
5. **Nota de visita llena** (fórmula de `APRENDIZAJES.md`): retención 25 + saltos 25 + guardados y compartidos por 1.000 30 + acción 20.
6. **Contexto:** hora, día, duración, si fue la primera pieza del día, incidencias. Con menos de 300 vistas, las tasas se dan con el aviso «muestra pequeña».
7. **Comparación justa:** con las piezas del mismo formato de los últimos 14 días (mediana), no con una sola.
8. **Stories:** respuestas, toques en sticker, salidas y respuestas por mensaje, frente a «qué buscábamos aprender» escrito por 04.
9. **Salida:** tabla, tres hechos, y lo que **no** se puede concluir por falta de dato.

## Nunca
Inventar o redondear a favor · comparar piezas de duración muy distinta por tiempo medio en segundos (se usa la proporción) · llamar «éxito» a vistas sin retención ni acción.

## Control
¿Cada cifra viene de una consulta de hoy? ¿Fórmulas escritas? ¿Declarado lo no disponible?
