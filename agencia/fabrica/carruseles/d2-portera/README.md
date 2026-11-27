# d2-portera · carrusel y Stories (Clara, 23/11)

Reel: d2-portera «Paró doce y fue su mejor partido» (balonmano). Sin guion en `agencia/fabrica/guiones/`: el texto sale de la voz del reel (`tools/reel_v4/d2-portera/times.js`), de `tools/reel_v4/d2-portera/CREDITOS.md` y del post del feed.

- Carrusel 1080×1440, 6 láminas (`c1`…`c6`): portada «Le marcaron veinte. Fue su mejor partido.» (7 palabras, foto enmarcada) → problema (14–20 EJEMPLO; «Perdéis de seis y en el vestuario nadie la mira») → paso 1 cuenta tiros, no goles (hoja de palotes 12 + 20 = 32, EJEMPLO) → paso 2 paradas ÷ tiros (12 ÷ 32 = 37,5 %) → paso 3 el lunes, a ella antes que a nadie (barras por jornada EJEMPLO) → resumen + «Guárdalo y pásaselo a tu segundo».
- Stories 1080×1920: `s1` pregunta («¿Cuántos tiros paró tu portera el sábado?»), `s2` encuesta («¿Qué cuentas de tu portera?»: «Los goles que encaja» / «Los tiros que para»). Los stickers se pegan a mano desde Instagram.
- Fotos: `portera.jpg` y `lanzadora.jpg` (Steffen Prößdorf, CC BY-SA 4.0), las mismas del reel.
- Cálculo: porcentaje de paradas = paradas ÷ tiros a portería (paradas + goles). Escena de ejemplo, no un partido real.
- Regenerar: `python3 gen.py` y `python3 render.py <carpeta_salida>` (Playwright; también exporta JPEG 1080×1350).
- En el feed: `media/d2-portera-c1.png`…`-c6.png`, `-s1.png`, `-s2.png`; posts `d2-portera-carrusel`, `-story1`, `-story2`. En la cola de publicación: `d2-portera-carrusel`, `-story1`, `-story2` (revisión).
