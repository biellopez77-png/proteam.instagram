# b2-rpe · carrusel y Stories (Clara, 23/11)

Reel: b2-rpe «Una pregunta del 1 al 10» (baloncesto). Sin guion en `agencia/fabrica/guiones/`: el texto sale de la voz del reel (`tools/reel_v4/b2-rpe/times.js`) y del post del feed.

- Carrusel 1080×1440, 6 láminas (`c1`…`c6`): portada «Lo podías saber desde el jueves.» (foto enmarcada) → problema (el sábado, en el tercer cuarto, se apagan; marcador por cuartos EJEMPLO) → paso 1 al acabar, del 1 al 10 → paso 2 × minutos (7 × 90′ = 630, EJEMPLO) → paso 3 tres semanas, jueves contra sábado (barras EJEMPLO) → resumen + «Guárdalo y pásaselo a tu segundo».
- Stories 1080×1920: `s1` pregunta («¿Qué día entrenas más fuerte?»), `s2` encuesta («¿Les preguntas cuánto les ha costado?»: «Lo pregunto» / «Lo intuyo»). Los stickers se pegan a mano desde Instagram.
- Fotos: `tension.jpg` (Steffen Prößdorf, CC BY-SA 4.0) y `balones.jpg` (DoD, DP), las mismas del reel (`tools/reel_v4/b2-rpe/CREDITOS.md`).
- Método: RPE de sesión (Foster et al., 2001).
- Regenerar: `python3 gen.py` y `python3 render.py <carpeta_salida>` (Playwright; también exporta JPEG 1080×1350).
- En el feed: `media/b2-rpe-c1.png`…`-c6.png`, `-s1.png`, `-s2.png`; posts `b2-rpe-carrusel`, `-story1`, `-story2`.
