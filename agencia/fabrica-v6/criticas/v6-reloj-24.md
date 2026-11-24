# Crítica · v6-reloj-24 «Diecinueve a dieciocho» · Andrés (05) · 24/11

**Vídeo:** tools/reel_v6/v6-reloj-24/final.mp4 (commit 8c33887) · 1080×1920 · 30 fps · 42,8 s · voz hasta 41,2 s
**Método:** 43 fotogramas (1/s) a tamaño móvil + fotogramas extra en 20,5–23 s, 28,3–29,2 s, 30,8–31,3 s y 39,6–40,3 s; tiempos de voz por palabra (times.js, Scribe) contra la locución del guion; loudness con ebur128.

## Nota: 80/100 → **SUSPENDE** (condición eliminatoria: texto cortado)

| Criterio | Nota | Por qué |
|---|---|---|
| Historia y gancho real | 22/25 | «Diecinueve a dieciocho» con las placas cayendo es un gancho limpio; la cuenta de Syracuse es la historia y se entiende en 20 s. |
| Claridad para un entrenador de base | 17/20 | Libreta, división y hoja de tiros se siguen bien; el 93,1 casi no se ve (ver 28,6 s). |
| Pizarra y transiciones | 13/20 | La pista y el contador de pases funcionan; la libreta se recorta arriba en el acercamiento (21–23 s) y la hoja pisa el subtítulo a 30–31 s. |
| Verdad y fuentes | 14/15 | Todas las cifras casan con ESPN Classic, Wikipedia «Danny Biasone», NBA.com y TIME. El «Así que» simplifica la causa (el 19-18 como detonante), que es la lectura habitual. «EJEMPLO» visible en la hoja. |
| Estética v4 | 8/10 | Fondo, duotono, tipografías y cursiva bien. UV una vez (el 24, 21,7–23 s). La barra 1954-55 y el «Team» del cierre van en índigo muy cerca del UV; no cuenta como segundo UV, pero se acerca. |
| Sonido | 6/10 | Voz clara y bien sincronizada; pausa tras «Divide.» correcta. Integrado −25,5 LUFS (pico −6,7 dBFS): muy bajo para Reels, se oirá floja frente al resto del feed. |

## Comprobación de datos (voz → fuente)
- 19-18, Fort Wayne–Minneapolis, noviembre de 1950 (0–5 s; rótulo 22·11·1950) → ESPN Classic ✔
- Dueño de los Nationals y su director general (Biasone y Ferris), 48 min = 2.880 s, ~120 tiros, 2.880/120 = 24 (13–22 s) → Wikipedia ✔
- 1954 llega el reloj; media por equipo 79 → 93 (voz), barras 79,5 → 93,1 (22,8–28,8 s) → NBA.com «Season review 1954-55», TIME ✔
- Hoja 9·6·3·7 rotulada EJEMPLO; raya por tiro y partidillo de 12 s son propuesta, no dato ✔
- Fotos: Jecarp155 CC0 y U.S. DoD dominio público, pie en pantalla desde 29 s ✔

## Marcas de tiempo y correcciones
1. **20,5–23,0 s · TEXTO CORTADO (eliminatorio).** En el acercamiento a la libreta, «48 min × 60 s =» se sale por arriba del cuadro (21,3 s) y «2.880 s» queda cortado y montado encima de la cabecera «PROTEAM — HISTORIAS · BALONCESTO» (22,2–23,0 s; a 23 s solo se ve la mitad inferior del 2.880). → Limitar el acercamiento para que la libreta no suba por encima de y ≈ 140 px (debajo de la cabecera) o, mejor, al hacer zoom desplazar el encuadre para que las tres líneas (2.880 s / 120 / 2.880 ÷ 120) quepan enteras con el 24; si no caben, que «48 min × 60 s =» se desvanezca antes de salir del cuadro. Ninguna línea puede tocar la cabecera.
2. **28,6–28,9 s · el 93,1 apenas se ve (~0,3 s)** antes del corte a la foto (29,0 s). Es la cifra que demuestra que el reloj funcionó. → Que la barra termine de contar en «noventa» (≈28,1 s) y aguante 93,1 quieto al menos 0,8 s; retrasar el barrido a 29,2 s («Piensa» empieza a 29,23 s, cabe).
3. **30,0–30,8 s · solape.** Mientras sube la hoja de tiros, las filas 3C/4C pasan por debajo del subtítulo «¿Cuántos tiros saca por cuarto?». → Que la hoja entre ya por encima de y ≈ 1.250 px o que el subtítulo aparezca cuando la hoja haya llegado.
4. **29,0 s y 33–34 s · fotos que pisan la cabecera.** En el barrido y en la subida de la foto de penetración, la foto pasa por encima del rótulo «PROTEAM — HISTORIAS». → Máscara bajo la cabecera o que la cabecera esté por encima de la capa de fotos.
5. **Sonido.** Subir el integrado a −14/−15 LUFS con limitador a −1 dBTP (la voz entera, sin tocar la mezcla relativa con los efectos).
6. **40–42,8 s · cierre.** El guion pide que la hoja de tiros se convierta en tarjeta; ahora es un corte a logo estático. No es eliminatorio, pero se pierde el puente «esto se apunta». Si da tiempo, la hoja encoge a tarjeta antes del logo (39,7–40,5 s).
7. (Menor) **3–5 s:** «EL PARTIDO CON MENOS PUNTOS DE LA NBA» va en cuerpo diminuto y gris; en móvil no se lee. Subir a ≥ 30 px y más contraste: es el dato que justifica la historia.
8. (Menor) Revisar que el índigo de la barra 1954-55 y de «Team» sea el azul del sistema y no un violeta: el único violeta debe ser el 24.

Con 1–3 y 5 corregidos, la pieza pasa de 85.
