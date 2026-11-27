# Crítica · v7-chocolate-wenger-1996 «Tienen hambre» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 87/100 → APROBADO. Programado el martes 8/12 a las 18:00.**

Material revisado: el vídeo que está ahora en `publicar/cola.json` (`71b165a1-…mp4`, 28,9 s, cierre outro2), descargado y analizado en el sandbox de Higgsfield; fotogramas cada 0,5 s a 270 px y recortes a 405 px donde hacía falta; el guion, `CREDITOS.md` y la cola.

**Ojo, vídeo de la tarea:** la tarea apuntaba a `e2d34f17-…mp4` (31,0 s). Ese vídeo lleva el **cierre retirado**: whisper oye «Estamos terminando la app de ProTeam. Síguenos para no perderte nada.» (25,1–29,6 s) y en pantalla sale «Estamos terminando la app · MUY PRONTO, NOVEDADES» (25,5–31,0 s). Con ese vídeo sería suspenso automático. En la cola ya está en `files_old` y `files` apunta a `71b165a1` (commit 1f3d67e, «Cola: 42 vídeos con el cierre nuevo»). La nota es para `71b165a1`. **No se puede publicar `e2d34f17` en ningún sitio.**

## Comprobaciones duras (vídeo 71b165a1)
- **Voz entera y cierre nuevo:** faster-whisper small oye: «1996. Arsène Wenger dirige su primer partido con el Arsenal. En el descanso nadie habla. Pregunta al fisio qué pasa. Tienen hambre. Les había quitado el chocolate de antes del partido. Ganan 2 a 0 y en el autobús de vuelta cantan: ¡Queremos nuestras chocolatinas! Y Wenger les pone pescado, brócoli y agua. El partido empieza en el plato.» y luego «Dale like y síguenos para más vídeos como este» (25,2–28,6 s). En pantalla, «¿Te ha servido? Dale like y síguenos · para más vídeos como este» (25,5–28,9 s). Ni «app», ni lista de espera, ni lanzamiento.
- **Niveles:** −18,3 LUFS integrados; **true peak −0,6 dBTP** (un poco por encima del −1 habitual). La voz va entre −15 y −20 dB RMS; las pausas, solo con música, entre −29 y −33 dB: la voz va 10–14 dB por encima. Efectos bajos y reales (tablillas, autocar, plato, agua). Dos huecos de ~60 ms casi en silencio en el vídeo antiguo (20,7 s y 24,5 s); en este no molestan.
- **Música:** real, de Epidemic («Musical, Loop, Piano, Sentimental, Fast 01») y sting del cierre.
- **Fotos:** Ronnie Macdonald (CC BY 2.0, dos), Gordon Flood (CC BY 2.0) y Jeffery Martin (CC0), con crédito en la foto, en el pie y en el caption. Sin escudos del Arsenal ni del Blackburn, sin vallas publicitarias, chocolatina y agua sin marca. Nada sugiere que Wenger o un club apoyen ProTeam.
- **Texto:** nada cortado en plano quieto. A 22,8 s «PESCADO, BRÓCOLI, AGUA» y el vaso salen por la derecha, pero es el viaje de cámara (en movimiento), no un plano fijo.
- Caption: termina con «¿Te ha servido? Dale like y síguenos para más vídeos como este.», con fuentes y créditos. Sin precios, sin el nombre de Biel, sin cifras de apuntados.

## Verdad y fuentes
Todo lo que dice la voz tiene fuente en el guion: primer partido, 12/10/1996, Blackburn 0-2 Arsenal (arsenal.com; Premier League); el silencio del descanso y la pregunta al fisio Gary Lewin, «They're hungry», «I hadn't given them their chocolate before the game» (arsenal.com; Daily Mirror; ESPN); el cántico en el autocar de vuelta, «We want our Mars bars!» (arsenal.com; Daily Mirror; Yorkshire Post), traducido a «chocolatinas» para no nombrar la marca; pescado, brócoli y agua («fish, pasta, mineral water», la «Evian-broccoli diet»: Yorkshire Post; ESPN). El remate va sin comillas, como idea. El guion se cuida de no decir que la dieta ganara títulos. Bien.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | Historia muy buena para entrenadores: graciosa, con giro («tienen hambre») y una idea que se queda. El gancho «1996.» es seco: el contador 1990→1996 ayuda, pero la primera frase no plantea ninguna pregunta. |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Muy bien: sello «PARTIDO 1», bocadillos vacíos que se apagan en «nadie habla», maletín que se abre con «¿Qué les pasa?», «HAMBRE», chocolatina tachada que sale de la bandeja, tablillas 0-2, autocar con notas y la frase rebotando, plato que se llena (pescado, brócoli, vaso). Flojo: el marcador aparece vacío ~0,2 s antes de «Ganan». |
| Transiciones | 12/15 | Viajes suaves en las pausas, sin destellos. Pero el remate no se queda quieto: a 24,9 s «PLATO.» aún está entrando y a 25,0 s ya empieza el fundido, con el logo encima del remate a 25,0–25,5 s. «EN EL PLATO.» entero y quieto casi no se ve. |
| Sonido | 13/15 | Voz confiada y clara, música de piano suave debajo, efectos bajos. True peak −0,6 dBTP. |
| Verdad y fuentes | 15/15 | Todo con fuente y sin exagerar. |
| Estética | 12/15 | Paleta, tipografías y ultravioleta una sola vez (EN EL PLATO), bien. Pero casi todas las escenas dejan vacío el 40–45 % de abajo (6–19 s), y los créditos del pie del remate (~9 px) no se leen en el móvil. |
| **Total** | **87/100** | Aprobado. |

## Mejoras (no bloquean; para la próxima pieza o si se remonta)
1. Remate quieto: «EN EL PLATO.» entero y parado al menos 1 s antes del fundido (como en el remontaje de Berna: alargar la historia ~0,8 s con música).
2. True peak a −1,0 dBTP o menos (limitador al final de mix.py).
3. Bajar las escenas 2–6 unos 150–250 px o agrandarlas para llenar el tercio inferior.
4. Créditos del pie a ≥ 17 px.
5. Gancho: abrir con la frase del descanso («En el descanso, nadie hablaba.») y dar el año después, o poner «PRIMER PARTIDO» ya en el primer segundo.
