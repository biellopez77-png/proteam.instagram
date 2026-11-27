# u51 · Producción · «Sábado, una y diez. El partido acabó hace diez minutos.» (Marta, 02 · 19/11 0:50)

Guion: `agencia/guiones/2026-11-17-u51-lanz-contexto-sabado-una-y-diez.md` (Dani · Andrés 78). Montaje: `tools/reel51/` (build.sh → reel.html).
Fase: **CONTEXTO** · sale el **jue 19/11 a las 9:30** (primer Reel del jueves; el día no tenía ninguno). Vale del 19 al 21 por el texto, pero el contador del cierre está calculado para el jue 19 9:30: si se mueve, hay que rehacer el contador.

Decidido (Marta, 0:45): el jueves no tenía ningún Reel y u51 es el guion de contexto más antiguo y criticado de la reserva; la corrección de u50 (sale el mié 25) va en el siguiente turno con voz.

## A · Concepto visual (nuevo)
**«El reloj que no se para».** El banquillo vacío del Camp Nou a sangre con un marcador LED en vidrio oscuro que ya marca **13:10** en el fotograma 0. En «acabó» el marcador pasa a FINAL **13:00** (borde azul) y en «diez minutos» corre hasta 13:10 (FINAL + 10 MIN). En «el entrenador sigue con él» el reloj baja, pequeño, y sigue corriendo (13:10 → 13:14) mientras saltan tres avisos sobre el banquillo: **¿MINUTOS?**, **¿QUÉ FALLÓ?**, **¿MARTES?**. Corte a papel: «NO LO VIMOS DESDE UNA» · **OFICINA**, que se tacha en azul; corte seco en «banquillo» al banquillo vacío del Bernabéu con *en el banquillo.* Golpe de música en «nació»: **ProTeam.** a pantalla completa con destello azul y los tres deportes. Ancla: **HECHA EN EL BANQUILLO** · *no en una oficina* (tachado). Vuelve el reloj sobre el Camp Nou (bucle) para el reto **¿Quién sigue** *con el partido?*; **ABRE EL SÁBADO 28 NOV**; cierre de campaña con contador real.
Distinto de lo usado: u59 (tira de días), u49 (rótulos de TV), u50 (pantalla de bloqueo), u12 (acta). Nunca se había usado un marcador que sigue corriendo después del final, ni el tachado de «oficina».

## B · Bloques (tiempos de `times.js`)
| s | bloque | pantalla |
|---|---|---|
| 0–4,3 | A | Camp Nou a sangre · SÁBADO · reloj **13:10** desde el fotograma 0 · FINAL 13:00 (1,9 s) · corre a 13:10 · *acabó hace 10 minutos.* |
| 4,3–9,6 | B | EL ENTRENADOR *sigue con él.* · ¿MINUTOS? (6,1) · ¿QUÉ FALLÓ? (7,4) · ¿MARTES? (8,4) · reloj pequeño que sigue |
| 9,6–14,0 | C | papel: ESE PROBLEMA · NO LO VIMOS DESDE UNA · **OFICINA** tachada (12,3) · corte al Bernabéu (13,1): LO VIVIMOS *en el banquillo.* |
| 14,0–21,3 | D | *Buscábamos cómo resolverlo.* · golpe en «nació» (16,36): Y ASÍ NACIÓ **ProTeam.** · FÚTBOL · BALONCESTO · BALONMANO |
| 21,3–24,3 | E | Bernabéu oscurecido · HECHA EN EL **BANQUILLO** · *no en una oficina* (tachado) |
| 24,3–29,0 | F | Camp Nou + reloj (bucle) · RETO PARA TU STAFF · **¿Quién sigue** *con el partido?* |
| 29,0–30,9 | G | ABRE EL SÁBADO · **28 NOV** |
| 30,9–35,7 | H | cierre de campaña como u59: web de la lista con contador real (jue 19 9:30 → vie 27 23:59:59 = 8 d 14 h 29 min 59 s), «Estás dentro», **HASTA EL 27 NOV** · *3 meses gratis.* sobre el Camp Nou |

Menos texto (encargo de Biel): un titular por plano, nada de bloques de texto; las tres preguntas son de dos palabras.

## C · Voz
Mateo – News & Digital Stories (`gpMzl7dbkfC9dIxAqQZT`; la original `Rie0luvrYhyKLba1lK3c` devolvió «disabled by the owner» a las 0:45 y esa llamada falló sin generar ni gastar). Una toma entera y seguida a su velocidad, 570 caracteres, 36,4 s. Un único corte sobre silencio real (4,12 → 5,62 s de la toma) para quitar «Los jugadores ya se van» (recomendación de Andrés: la toma pasaba de 32 s). Queda en 35,0 s de voz. Transcripción con Scribe idéntica al guion (coste 0). Sin pausa antes del CTA. En la voz: «la app de ProTeam».
Cambios de texto respecto al guion (sin cambiar la idea): «Y así nació la app de ProTeam, para entrenadores de…» (regla «la app de ProTeam» en voz) y «Abre el sábado veintiocho» en vez de «Abre el 28»; fuera «Enlace en la bio» de la voz (va en la descripción).

## D · Música
Pista nueva (ElevenLabs music v2.5, una toma): re menor, ~143 BPM, intro de piano apagado con ambiente de estadio vacío y pad cálido (sin batería), luego 808 con deslizamientos cortos y hi-hats en tresillos. La entrada del beat (13,40 s de la toma) cae en «nació» (16,36 s) con 0,3 s de silencio antes. Los 2,96 s iniciales llevan una frase de piano de la propia intro; el beat se alarga repitiendo 4 compases cortados en golpe (30 ms de fundido). Fundido de salida de 1,2 s.

## E · Efectos
Golpe de entrada, tic del FINAL, tics del reloj que corre, vibración + tic por aviso, roce del papel, golpe de OFICINA y del tachado, golpe del corte al Bernabéu, golpe de «nació», tic por deporte, golpe de BANQUILLO, golpe de «¿Quién sigue», golpe del 28 y los del cierre (como u59). Al 0,32.

## F · Arranque
Arranque: 1 ✔ (banquillo del Camp Nou a sangre con **13:10** y SÁBADO puestos) 2 ✔ (voz en 0,06 s: «Sábado, una y diez») 3 ✘ 35,7 s (la voz pide 35 s; se acepta: es la pieza de contexto y u08 retuvo con 29,5 s) 4 ✔ (las tres preguntas del después del partido, 6–9,6 s) 5 ✔ (abre con escena y hora, no con marca).
Recursos: `banco/fotos/PROTEAM_INSTALACION_BANQUILLO_CAMP_NOU_FOTO_001_V.jpg` (Dnklr, CC BY 3.0, Wikimedia Commons) y `…BANQUILLO_BERNABEU_FOTO_001_V.jpg` (Daniel R. Walker, CC BY-SA 3.0, Wikimedia Commons). Sin personas: nadie del equipo ni de Biel. Como ejemplo de banquillo, nunca como aval. El rótulo del patrocinador del Camp Nou queda arriba, oscurecido por el degradado.
