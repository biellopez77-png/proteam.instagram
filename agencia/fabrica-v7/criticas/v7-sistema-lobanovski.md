# Crítica · v7-sistema-lobanovski «Veintidós piezas» · r2

**Andrés (05) · 27/11/2026 · Nota: 74/100 → NO APROBADO. Vuelve a montaje.**

Material revisado: el vídeo de la cola (`publicar/cola.json` → `ba0ddccd-625e-4931-877f-5d7365248851.mp4`, **26,0 s**), descargado en el sandbox de Higgsfield. Lo he mirado en fotogramas cada 0,5 s y he hecho capturas más finas entre 18,6 y 25,5 s. También lo he transcrito con faster-whisper small y he medido niveles cada 0,1 s.
Ojo: el vídeo de la tarea (`284685c0-…`, en `files_old`) no es el de la cola. Además, el `video_mudo.mp4` del repo (28,07 s) es antiguo: todavía acaba con el cierre retirado («Estamos terminando la app. Síguenos para no perderte nada. Muy pronto, novedades»).

## Lo que se ha corregido desde la r1 (80/100)
- **EQUIPO > SUMA:** ahora sí. La red y «EQUIPO» van a la izquierda, el «>» ultravioleta en medio y los unos y «SUMA» a la derecha (21,3–22,0 s). Corrección bloqueante resuelta.
- **Contador:** mientras cuenta solo salen las cifras («7», «21»), y «22 PIEZAS:» aparece al llegar a 22. Bien.
- **Rótulo de los trofeos:** entra con los trofeos (18,6 s). Bien.
- **Márgenes y créditos del pie:** bien.
- **Cierre outro2:** el audio dice «Dale like y síguenos para más vídeos como este» (22,32–25,14 s) y en pantalla se lee «¿Te ha servido? · Dale like y síguenos · para más vídeos como este». No se menciona la app ni en la voz ni en la pantalla.
- **Caption de la cola:** termina con el cierre nuevo, sin app ni enlace. Bien.

## Lo que suspende (bloqueante)
1. **Falta la última palabra de la historia.** Whisper oye «…vale más que la suma de sus…» (último tramo, 22,06–22,32 s), y el nivel se hunde hasta −46 dB a 22,2 s. Justo después entra «Dale like…», a 22,32 s. **El «once» del remate no suena.** Al recortar de 28,1 a 26,0 s, el cierre se ha comido la última palabra, y es la palabra que cierra la idea («la suma de sus once»).
2. **La frase de la pizarra no llega a leerse entera.** A 22,0 s, «de» apenas empieza a aparecer, y a 22,3 s «de sus *once*.» ya sale apagado dentro del fundido. El remate no se queda nunca quieto y completo. En la r1 pedí lo contrario: que la frase se viera entera y quieta antes de irse.
3. **El logo se solapa con la pizarra.** A 22,3 s, «ProTeam» aparece en grande encima de la red de EQUIPO y del «>» (fundido cruzado, no fundido a negro). Es texto solapado, y por eso suspende aunque sea medio segundo. En Rangnick, Reep, Villas-Boas y Dean Smith ya se monta así: fundido a negro de 0,5 s y luego outro2.

## Otros puntos
- **Pizarra vacía (19,7–20,2 s):** la cámara llega a un marco vacío mientras suena «Porque un». Es medio segundo muerto: que la red de EQUIPO empiece a dibujarse con «Porque», o que la cámara llegue unos 0,3 s más tarde.
- **Niveles:** −18,8 LUFS y pico de −1,3 dBFS. La voz va entre −17 y −20 dB y las pausas de solo música, entre −30 y −35 dB. Bien.
- **Repo desfasado:** `video_mudo.mp4` y `CREDITOS.md` no recogen la r2 ni el cierre outro2. Hay que subir el mudo nuevo y apuntar la versión de la cola.
- **Panel:** el caption del post todavía terminaba con «Estamos terminando la app de ProTeam…» y el vídeo era el `284685c0`. Lo he puesto igual que la cola (caption con el cierre nuevo y vídeo `ba0ddccd`) para que nadie publique la versión vieja.

## Verdad y fuentes
Las mismas que en la r1, y todas se sostienen: ingeniería térmica, la fiesta con Zelentsov, los tiros, pases y errores, los 22 elementos en dos sistemas de 11 y las Recopas de 1975 y 1986, las dos por 3-0. Las fotos son CC0 (Anefo, Nationaal Archief). No hay precios, fechas, cifras de apuntados ni el nombre de Biel. La música es real, de Epidemic.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Igual que en la r1. El gancho arranca con el nombre. |
| Cada cosa que dice la voz se anima en su momento | 15/20 | Contador y trofeos arreglados, pero la pizarra está vacía en «Porque un» y el remate no llega a mostrarse entero. |
| Transiciones | 10/15 | La pizarra pasa a outro2 con un fundido cruzado y el logo queda encima de la red. |
| Sonido | 8/15 | El «once» final está cortado, y el cierre entra sin respiro (0 s entre «sus» y «Dale»). |
| Verdad y fuentes | 13/15 | El signo ya está bien, pero la frase final queda incompleta («la suma de sus…»). |
| Estética | 12/15 | Paleta, fotos y márgenes bien. Pierde puntos por el logo solapado. |
| **Total** | **74/100** | Suspende por texto solapado y por el remate cortado. |

## Correcciones (para Marta, 02)
1. **(Bloqueante) Que vuelva el «once».** Deja entera la voz de la historia, de 0 a ~22,9 s (en la r1, «once» acababa hacia 22,8–22,9 s con la apertura de 0,5 s). Después, 0,3–0,6 s de silencio solo con música y, a continuación, outro2. La duración total quedará en unos 27,5–28 s.
2. **(Bloqueante) Remate entero y quieto.** «Porque un equipo / vale más que la *suma* de sus *once*.» entero, con la pizarra EQUIPO > SUMA completa, quieto al menos 0,8 s después de que suene «once». Luego, apagado.
3. **(Bloqueante) Fundido a negro de 0,5 s antes de outro2,** como en Rangnick r2: que el logo de ProTeam no aparezca nunca encima de la pizarra.
4. Que la red de EQUIPO empiece a dibujarse con «Porque» (20,16 s), o que la cámara llegue a la pizarra unos 0,3 s más tarde, para que no se vea un marco vacío.
5. Sube el `video_mudo.mp4` nuevo, con outro2, y anota en `CREDITOS.md` la r3 y la URL de la cola. El caption de la cola ya está bien: no lo toques.
6. Comprueba con whisper que se oigan las 58 palabras, «once» incluido, y luego «Dale like y síguenos para más vídeos como este».

Todo lo demás está aprobado: voz, música, efectos, fotos, contador, trofeos y pizarra EQUIPO > SUMA. En la r3 solo miraré el tramo de 19,5 s al final y haré un repaso rápido completo.

---
*Crítica anterior (r1, 80/100): en el historial de git de este archivo.*
