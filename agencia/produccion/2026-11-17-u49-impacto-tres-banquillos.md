# u49 · Producción (Marta, 02) · «Minuto 70. ¿Cuántos minutos lleva tu nueve?» · IMPACTO, mié 18/11 9:30

Guion: `agencia/guiones/2026-11-17-u49-impacto-tres-banquillos-una-fecha.md` (Dani · Andrés 82). Recursos: `agencia/recursos/2026-11-17-u49-u50-impacto.md` (Pau). Montaje: `tools/reel49/` (build.sh → reel.html).

## A · Concepto visual (nuevo)
**«Rótulos de retransmisión con la casilla en blanco».** Cada banquillo de primer nivel lleva el rótulo de TV que le falta al entrenador de base: dorsal o puesto en azul, la etiqueta y la cifra en blanco («— —» con el cursor parpadeando). Lo que sí se cuenta (14 goles) aparece; lo que nadie apunta (minutos del 9, paradas) se queda vacío. Los tres banquillos se apilan en tres franjas («el mismo sábado») y el calendario de noviembre en papel rodea el 28 a mano en azul justo en «veintiocho», con el golpe de la música. Nada de esto está en «Recursos visuales ya usados» (el marcador que rebobina de u03 y el calendario-mapa del carrusel c15 son otras cosas).

## B · Plano a plano (tiempos de `times.js`, voz entera)
| s | plano | pantalla |
|---|---|---|
| 0–4,6 | Zidane en la banda a sangre | DÍA 1 DE 10 · SÁB 28 NOV (fijo arriba) · **MIN 70** desde el fotograma 0 · *¿minutos del 9?* · rótulo [9 · MINUTOS JUGADOS · — —] · NO LO SABES. |
| 4,6–9,8 | corte seco · Pat Riley de pie, banquillo sentado detrás | **ÚLTIMO CUARTO** · rótulo [BASE · DESCANSOS · 0] · *Te das cuenta ahora.* |
| 9,8–15,5 | corte seco · tiempo muerto del THW Kiel (tarjeta nítida sobre la misma foto desenfocada) | **DESCANSO** · [POR · GOLES ENCAJADOS · 14] (cuenta hasta 14 en «catorce») · [POR · PARADAS · — —] · *Nadie las ha contado.* |
| 15,5–17,9 | tres franjas entran alternadas | TRES BANQUILLOS. · *El mismo sábado.* |
| 17,9–18,2 | negro 0,3 s (el único) | — |
| 18,2–22,6 | papel · calendario de noviembre (18 marcado, 19–27 se apagan) | APUNTA OTRO · círculo azul a mano en el 28 en «veintiocho» · **SÁB 28 NOV** · *abre ProTeam.* |
| 22,6–25,5 | tinta | HOY NO TE CONTAMOS MÁS. → QUEDAN **10** *días.* |
| 25,5–28,3 | las tres franjas otra vez (bucle con el principio) | RETO PARA TU STAFF · Mándaselo a tu segundo: · ¿Cuál de los *tres sois?* |
| 28,3–33,1 | lista de espera en motion graphics (contador real a la hora de publicar: 9 d 14 h 29 min 59 s) → Zidane oscurecido | HASTA EL 27 NOV · *3 meses gratis.* |

## C · Voz
Mateo – News & Digital Stories (`gpMzl7dbkfC9dIxAqQZT`): la original `Rie0luvrYhyKLba1lK3c` vuelve a dar «disabled by the owner» (la llamada falló sin gastar). **Una sola toma, entera y seguida, a su velocidad natural**: sin trocear, sin acelerar y sin silencios añadidos (corrección de Biel en u12). 482 caracteres. Transcripción de ElevenLabs Scribe idéntica al guion (83 palabras); los tiempos de palabra salen de ahí. Dura 32,3 s: el Reel queda en 33,1 s, más que los 27,5 del guion y que el tope provisional de 24–25 s del arranque; se prefiere la toma seguida (decisión apuntada en el log).

## D · Música
Pista nueva (ElevenLabs music v2.5, una toma, si bemol menor, ~144 BPM, 808 con slides, hi-hats en tresillo, pad granular frío, percusión de reloj en la intro, ambiente de pabellón). Intro de la pista bajo el hook; desde la entrada del beat (6,68 s de la pista) suena filtrada (paso bajo 420 Hz) bajo los tres banquillos y el «Apunta otro»; corte seco 0,38 s antes de «veintiocho» y el beat entra sin filtro exactamente en «veintiocho» (19,42 s). Fundido de salida de 1,2 s. Comprobado con Scribe que la pista no tiene voces.

## E · Efectos
Golpe de entrada, barridos en los cortes, tic de rótulo, seis tics mientras cuenta hasta 14, golpe en «catorce» y en «diez», tics suaves al apagarse los días del calendario, cierre de la lista de espera (igual que u10/u28). Al 0,32 con `amix normalize=0` y `alimiter`.

## F · Cierre de campaña
Web de la lista de espera en motion graphics con el contador real y «HASTA EL 27 NOV» + «3 meses gratis.» en serif azul. Sin precio, sin pantallas de la app, sin nombres del equipo.

**Arranque:** 1 ✔ (Zidane a sangre con MIN 70 grande desde el fotograma 0) · 2 ✔ (la voz entra a los 0,08 s con el minuto y la pregunta que no sabe contestar) · 3 ✘ (33,1 s: toma seguida por la queja de Biel en u12; se acepta y se apunta) · 4 — (Reel de impacto sin ficha: lo dice el guion y la crítica) · 5 ✔ (abre con escena y número, no con marca).
