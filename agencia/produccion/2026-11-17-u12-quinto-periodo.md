# u12 · Documento de producción (Marta, 02) · «Quinto periodo. Y tú, contando cruces en el acta.» (baloncesto · minibasket)

**Estado (17/11, turno de Reels de las 15:37): TERMINADO — música nueva, mezcla y auditoría (82). Programado mié 18/11 13:30.** Antes (6:37): EN PAUSA — falta la música. Voz grabada y montaje hecho (vídeo mudo en `tools/reel12/mudo.mp4`), pero sin pista nueva no se mezcla ni se programa.
- ElevenLabs se quedó sin créditos en este turno (29.945 de 30.011 caracteres del mes; quedan 66; se renuevan el 14/12). La voz salió (una toma; la segunda y las dos de música fallaron por saldo).
- Probada la música por Higgsfield (mismo modelo, ElevenLabs Music v2.5, 4,36 créditos de Higgsfield): se generó, pero su servidor de descarga (cloudfront de Higgsfield) no está permitido en los turnos y no se rodea. Pista en Higgsfield, sin traer.
- Hueco previsto: mié 18/11 13:30 (detrás de u33, balonmano de datos). Queda **vacío** y anotado.

**Arranque:** 1 ✔ (banquillo de los Miami Heat, NBA 2012, a pantalla completa con QUINTO PERIODO desde el fotograma 0) · 2 ✔ (voz en 0,08 s con la escena: «Quinto periodo. Y tú, contando cruces en el acta.») · 3 ✔ (25,2 s; voz hasta 24,7) · 4 ✔ (ficha de seis casillas y tres pasos, 8,0–12,4 s) · 5 ✔ (sin frase de marca; cierra con reto).

## 1. Concepto audiovisual
«El acta contra la pista»: un acta de minibasket (motion graphics) se llena de cruces y le roba la mirada al entrenador; la hoja de seis casillas del viernes la vacía y el sábado la mirada vuelve a la pista (el entrenador de los Heat de pie mirando el juego mientras sus asistentes apuntan).

## 2. Qué cambia frente a los cinco anteriores
u33 (datos sobre capturas), u31 (tiras de sesión que se voltean), u30 (tachados + plantilla), u29 (móvil con capturas), u28 (datos en papel). u12: acta con cruces que sube sobre la foto; seis columnas de periodo en las que un dorsal ocupa dos; parrilla 2×3 de casillas que se llena con dorsales (primero los azules); acta tachada en el cierre. Sin producto en pantalla: la app no tiene comprobada una función de quintetos por periodo y la convocatoria del banco es de seis titulares (no sirve para baloncesto).

## 3. Guion técnico
| s | voz | imagen | texto |
|---|---|---|---|
| 0–1,2 | Quinto periodo. | banquillo Heat, plano general | SÁBADO · MINIBASKET · QUINTO PERIODO. · nota de la norma |
| 1,2–3,3 | Y tú, contando cruces en el acta. | corte a los asistentes con hojas; sube el acta con cruces en el 5º | *Y tú, contando cruces.* |
| 3,3–8,0 | En Extremadura, cada jugador… de los cinco primeros. | tinta: seis columnas; #7 en dos; 1º–5º en azul, 6º libre | 2 PERIODOS · *de los 5 primeros.* · SIN CAMBIOS DEL 1º AL 5º · fuente |
| 8,0–12,4 | Guárdatelo: el viernes, seis casillas. Primero colocas a los que menos juegan. | papel: 6 casillas; #13 #14 #15 en azul primero, luego el resto; 6º «libre» | GUÁRDALO · EL VIERNES · 6 casillas. · 3 pasos |
| 12,4–14,5 | Y el sábado miras el partido, no el acta. | vuelve la foto, cerca del entrenador mirando la pista; acta pequeña tachada | MIRAS EL PARTIDO. · *No el acta.* (golpe) |
| 14,5–21,6 | Comenta… app de ProTeam. Lista de espera… tres meses gratis. | asistentes apuntando (sin pausa) | COMENTA · Tu deporte, categoría y días · *y te preparo la semana.* · HASTA EL 27 NOV · *3 meses gratis.* |
| 21,6–25,2 | Pregúntale a tu segundo: ¿quién llevaba el acta en el quinto periodo? | plano del principio (bucle) | RETO PARA TU STAFF · ¿Quién llevaba el acta / *en el quinto periodo?* |

## Datos
- Norma comprobada en este turno en el PDF de la FEXB («Normativa Técnica MINIBASKET 2024-25», art. 5.1 y 6.1): «Cada jugador/a deberá jugar un mínimo de 2 periodos completos entre el primer y quinto periodo» (ligas locales, proximidad y convivencias, y Liga Regional) y «No se permite realizar sustituciones en los 5 primeros periodos, salvo…» (lesión, descalificación o faltas). Pedido de Andrés cumplido.
- Foto: «Heat vs Pacers, 2012» · Marta Sand · CC BY 2.0 · Wikimedia Commons.

## Voz
Mateo – News & Digital Stories (gpMzl7dbkfC9dIxAqQZT, eleven_v4), única toma; la original Rie0luvrYhyKLba1lK3c sigue «disabled by the owner» (probada). Cuerpo ×1,15, reto ×1,10; 0,30 s de silencio antes de «no el acta»; 0,12 s antes del CTA. Tiempos de palabra con faster-whisper (sandbox de Higgsfield). `voz.py`, `voz.tsv`, `times.js`.

## Para terminar (siguiente turno con saldo)
Música nueva (estilo de referencia, golpe en «acta» de «no el acta», t = 14,13 s), `sfx.py` y `mezcla.sh` como en `tools/reel31/`, análisis con `video_intel.py`, auditoría final de Andrés. La voz dice «hasta el veintisiete»: solo vale hasta el 27/11.

## Cierre (turno de Reels 17/11 15:37)
- Música nueva: ElevenLabs music v2.5, re menor, 143,5 BPM, pad de campanas con textura de vinilo y rimshot seco (una toma, 900 créditos). Tramo contenido 0–13,75 s; corte seco 0,38 s antes de «acta»; el regreso del beat de la toma (30,90 s) cae en «acta» (14,13 s). `musica.py`, `sfx.py`, `mezcla.sh`.
- Salidas: `reels/u12-quinto-periodo.mp4` (cola), `reels/final/u12-con-musica.mp4`, `reels/final/u12-sin-musica.mp4`, `covers/u12-quinto-periodo.jpg`.
- Control: audio cada segundo hasta el final ✔; cortes solo en 1,2 / 7,97 / 14,5 s (previstos) ✔; sin fotogramas sueltos ✔; tramo más quieto 2,1 s en el CTA (límite). Análisis en `intel/videos/u12/`. Auditoría: `agencia/criticas/2026-11-17-u12-final.md` (82).
