# Crítica · v7-uno-por-ciento-riley «Un uno por ciento» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 89/100 → APROBADO.** Programado para el lunes 7/12/2026 a las 18:00 (primer hueco libre de las 18:00 desde mañana).

Material revisado: el vídeo que está en `publicar/cola.json` (`files`: `c4017261-…mp4`, 27,4 s: 23,5 s de historia + cierre outro2), descargado en el sandbox de Higgsfield: 55 fotogramas (uno cada 0,5 s) a tamaño móvil, recortes a 1080 px del remate, los créditos y el cierre, transcripción con faster-whisper small y niveles. También `tools/reel_v7/v7-uno-por-ciento-riley/video_mudo.mp4` del repo (ver punto 1 de correcciones: está desfasado).

## Comprobaciones duras (ninguna falla)
- **App / producto / lista / lanzamiento:** nada en voz, pantalla ni caption. El cierre es el nuevo: en pantalla «ProTeam · ¿Te ha servido? · Dale like y síguenos · PARA MÁS VÍDEOS COMO ESTE» (23,9–27,4 s); en voz, «Dale like y síguenos para más vídeos como este» (23,82–26,58 s).
- **Caption:** cierra con «¿Te ha servido? Dale like y síguenos para más vídeos como este.», sin «app» ni enlace; después solo fuentes, créditos y hashtags.
- **Voz entera:** whisper oye las 57 palabras: «Verano de 1986. Los Lakers caen en la final del oeste. Pat Riley no pide ganar más, pide a cada jugador un 1% más. Y lo mide, cada uno tiene su número, los mejores de 800 para arriba. Tirarse a por un balón suelto también cuenta. Ocho meses después, campeones. Lo pequeño, si lo mides, crece.» «Riley» y «Lakers» salen bien escritos.
- **Niveles:** −17,6 LUFS integrados, LRA 3,8 LU, pico −1,1 dBFS. Voz entre −16 y −23 dB RMS por segundo; el final baja limpio (−30 a −46 dB en el último segundo). Música real de Epidemic (piano «Calm Piano, Dreamy, Intro 02»), efectos de Epidemic.
- **Fotos:** las cuatro de Commons con licencia (Lipofsky CC BY 3.0 / CC BY-SA 3.0; Atkins y Kennedy / LA Times CC BY 4.0), crédito en pantalla (22,9–23,5 s) y en el caption. Riley va en portada genérica «EL ENTRENADOR» sin fecha y nada sugiere que nadie apoye ProTeam. Sin logos dibujados.
- **Texto cortado o solapado:** no en las escenas. Solo se cruzan elementos durante los viajes de cámara (ELIMINADOS a 5,5 s y el borde de la libreta a 8,5 s), que es lo normal en el formato.

## Datos contra las fuentes
- «Verano de 1986. Los Lakers caen en la final del Oeste» → Clear: «stumbled in the 1986 playoffs… Western Conference Finals»; Wikipedia: ante Houston (el marcador dibujado pone LAKERS tachado y ROCKETS, sin resultado). ✔
- «un uno por ciento más» → Clear y Basketball Network: «improve their output by at least 1 percent». ✔
- «los mejores, de 800 para arriba» → MacMullan vía Clear: «elite players scored at least 800». ✔ (En pantalla «800+», sin cifra de Magic.)
- «Tirarse a por un balón suelto, también cuenta» → Riley vía Clear: «diving for loose balls». ✔
- «Ocho meses después, campeones» → Clear: «rolled out CBE in October 1986. Eight months later, they were NBA champions»; contador «OCT 1986 → JUN 1987», desfile del 17/06/1987. ✔
- Remate sin comillas: es la idea, no una cita. ✔

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 18/20 | Historia limpia y útil para cualquier entrenador; gancho correcto («Verano de 1986» con la hoja que pasa de PRIMAVERA a VERANO), pero no golpea tanto como «caen» lo haría en el primer segundo. |
| Cada cosa que dice la voz se anima | 17/20 | Muy bien: hoja de calendario, «ELIMINADOS» en «caen», «GANAR MÁS» tachado, «+1 %» línea a línea, la barra que cruza 800 en «ochocientos», la silueta que se tira y el «+1» que salta a la libreta, el contador de meses 6→8. Resta: el contador «SU NÚMERO» pasa por cifras al azar (942, 389, 736, 183) antes de fijarse en 800+; el 942 aparece antes de que la voz diga 800 y parece un dato. Y «crece.» solo se ve ~0,4 s antes de que entre el fundido. |
| Transiciones | 13/15 | Viajes suaves y en las pausas. El paso al cierre pisa el remate: «crece» acaba a ~23,6 s y la voz del cierre empieza a 23,82 s; a 23,5 s ya se ve el logo encima de «MIDES». |
| Sonido | 13/15 | Voz confiada y clara, música suave por debajo, efectos bajos. Resta lo mismo: no hay respiro entre el remate y «Dale like» (0,1–0,2 s). |
| Verdad y fuentes | 14/15 | Todo comprobado. Solo el contador aleatorio (cifras que no son de nadie). |
| Estética | 14/15 | Paleta y tipografías del sistema, ultravioleta solo en «MIDES», fotos bien graduadas. Créditos pequeños pero legibles a 1080 px. La flecha del final sale a trozos en algún fotograma (23,4 s). |
| **Total** | **89/100** | |

## Correcciones (no bloquean la publicación; para la próxima pieza y para el repo)
1. **Repo desfasado:** `tools/reel_v7/v7-uno-por-ciento-riley/video_mudo.mp4` (29,5 s) y `CREDITOS.md` siguen con el cierre antiguo («Estamos terminando la app… Muy pronto, novedades») y con la URL `7b8b4296-…`, que también queda en `files_old` de la cola. Lo que se publica es `c4017261-…` (bien). Marta: sube el mudo nuevo y actualiza CREDITOS.md para que nadie recupere la versión con app.
2. **Remate con aire:** deja 0,6–0,8 s de «crece.» quieto en pantalla antes del fundido de 0,5 s al cierre, para que la idea se asiente y la voz del cierre no empalme con el remate.
3. **Contadores:** cuando un contador representa una puntuación, que suba de 000 hacia la marca (como pedía el guion) y no gire por cifras al azar por encima de la marca.
