# a1-papel · carrusel y Stories (Clara, 22/11)

Reel: A1 «El papel de un millón» (guion en `agencia/sistema-v3/GUIONES_PRIORITARIOS.md`). Sustituye a `posts/a1-carrusel`.

- Carrusel 1080×1440, 6 láminas (`c1`…`c6`): portada «Lehmann tenía un papel. ¿Y tu portera?» → problema → paso 1 (seis zonas) → paso 2 (una raya por gol) → paso 3 (descanso: la zona con más rayas es tu ajuste; martes, esa zona) → resumen + «Guárdalo».
- Stories 1080×1920: `s1` pregunta («¿Qué apuntas tú en el descanso?»), `s2` encuesta («El marcador» / «Por dónde nos marcan»). Los stickers se pegan a mano desde Instagram.
- Rayas de la hoja: EJEMPLO (rotulado en las láminas).
- Foto: chuleta de Lehmann, Andreas Köpke, dominio público (`tools/reel_v2/img/papel.jpg`, ver `tools/reel_v2/CREDITOS.md`).
- Regenerar: `python3 gen.py` y renderizar cada HTML a PNG con Playwright (1080 de ancho).
- En el feed: `media/a1-papel-c1.png`…`-c6.png`, `-s1.png`, `-s2.png`; posts `a1-papel-carrusel`, `a1-papel-story1`, `a1-papel-story2`.
