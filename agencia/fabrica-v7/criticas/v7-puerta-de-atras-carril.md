# Crítica · v7-puerta-de-atras-carril «Los listos, a los fuertes» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 81/100 → NO SALE (a remontaje con Marta, tarea «Montar v7 v7-puerta-de-atras-carril»).** Buena historia y buena pizarra; falla el final: el remate no se queda quieto, el logo de ProTeam entra encima de «LOS LISTOS» (texto solapado = suspenso automático) y la voz del cierre pisa la última palabra.

Material revisado: el vídeo de la cola (`publicar/cola.json` → `ee4b91eb-…mp4`, 28,6 s, 1080×1920), descargado en el sandbox de Higgsfield: fotogramas cada 0,5 s a tamaño móvil y el tramo 23,6–26,0 s a 5 fps. Ojo: `tools/reel_v7/v7-puerta-de-atras-carril/video_mudo.mp4` del repo es el antiguo (30,7 s) y **acaba con el cierre de la app** («Estamos terminando la app. Síguenos para no perderte nada · Muy pronto, novedades», 25,8–30,7 s). La tarea apuntaba además al vídeo `9844c4a7`, que ya está en `files_old`. Lo auditado es el de la cola, que sí lleva outro2.

## Comprobaciones duras
- **Cola (ee4b91eb):** sin app, producto, lista de espera ni lanzamiento en voz, pantalla ni caption. Cierre outro2 en pantalla («ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este») y en voz («Dale like y síguenos para más vídeos como este», 24,96–27,78 s). Caption de la cola termina con el cierre nuevo.
- **Repo:** `video_mudo.mp4` = cierre de la app. Hay que subir el nuevo.
- **Panel:** tenía el caption viejo («Estamos terminando la app de ProTeam…») y el vídeo viejo (`9844c4a7`). Corregido por Andrés: caption y vídeo = los de la cola. **No debe salir nada desde el panel con el caption viejo.**
- **Texto solapado (suspenso):** a 24,8 s el logo «ProTeam» aparece encima de «los fuertes le quitan a los débiles» y de «LOS LISTOS,» (fundido cruzado, no a negro); a 25,0 s aún se leen los dos.
- **Voz entera (faster-whisper small):** «1996. Princeton contra UCLA, el vigente campeón. El ataque de Pete Carril tenía una seña: el corte por la puerta de atrás. Quedan 7 segundos. Un pase picado. Una bandeja por la puerta de atrás, 43 a 41. Se lo enseñó su padre, obrero del acero. Los fuertes le quitan a los débiles. Los listos, a los fuertes.» Están las 58 palabras. Whisper oye «Uc Lea» (3,04–3,98 s) y «Carroll» (6,72–7,04 s): la pronunciación de UCLA y de Carril no queda clara para un oído español.
- **Niveles:** −17,5 LUFS integrados, true peak −0,7 dBFS (por encima del −1,0 habitual), LRA 6,1 LU. Voz entre −18 y −21 dB RMS por segundo; huecos con música/efectos −29/−30 dB salvo el viaje de 1,2–2,0 s (−22,9 dB: el whoosh y el papel van altos para un hueco). Música real (Epidemic, piano y cuerdas), no sintetizada.
- **Fotos:** Jadwin Gymnasium (David Keddie, CC BY-SA 4.0), pancarta de Carril (Jonathan Schilling, CC BY-SA 4.0), partido de 1988 (Joe Shlabotnik, CC BY 2.0): licencias del guion; ninguna sugiere apoyo a ProTeam, sin escudos. Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel. Ultravioleta solo en la flecha de la bandeja (14,2–17,0 s).

## Verdad y fuentes
Todo lo que dice la voz está en las fuentes del guion: 1996, Princeton 43-41 UCLA, vigente campeón (AP/Spokesman-Review; PAW; SI); el corte por la puerta de atrás como seña del ataque de Carril (Wikipedia, SI); siete segundos, pase picado de Goodrich y bandeja de Lewullis (PAW; AP «backdoor layup»); la frase del padre, obrero de una acería (ficha del libro; Hoop Thoughts). Ficha «NCAA · PRIMERA RONDA · INDIANÁPOLIS · MARZO 1996» y «UCLA · CAMPEÓN 1995» correctas. El reloj que baja 0:07 → 0:04 va rotulado «recreación» y no afirma cuándo entró la bandeja: aceptable. Caption bien.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | Historia redonda (pequeño contra campeón, siete segundos, frase del padre). Pero abre con «1996.» en seco: un año no es gancho; la tensión llega a los 10 s. |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Ficha que se rellena, trofeo en «campeón», CARRIL en su nombre, flecha del corte en «puerta de atrás», reloj en «siete segundos», pase con bote en «picado», bandeja en ultravioleta, marcador 43-41, casco y viga en «obrero del acero», remate palabra a palabra. Falla: el marcador sube por separado y deja leer «20 – 0» y «43 – 0» / «43 – 12» (15,6–16,8 s). |
| Transiciones | 9/15 | Viajes suaves por la pared, pero el final no respira: «fuertes» acaba a 24,80 s, la flecha final aún se dibuja a 24,6 s y a 24,8 s ya entra el logo en fundido cruzado sobre el remate. El remate no está quieto ni 0,2 s. |
| Sonido | 11/15 | Voz confiada y clara, música suave. La voz del cierre entra a 24,96 s, 0,16 s después de «fuertes»: pisa el remate. UCLA y Carril suenan raros. True peak −0,7 dBFS. Viaje de 1,2–2,0 s alto. |
| Verdad y fuentes | 15/15 | Todo comprobado. |
| Estética | 11/15 | Paleta, tipografías y ultravioleta una vez, correctos. Texto solapado en el fundido (logo sobre LOS LISTOS). Pie de créditos (23,2–25,0 s) y pies de foto ilegibles en el móvil. |
| **Total** | **81/100** | Suspende además por texto solapado. |

## Correcciones para el remontaje (Marta)
1. **Final (23,0–25,8 s):** «LOS LISTOS, a los fuertes.» y la flecha ya terminados y quietos al menos 1,0 s después de «fuertes» (24,80 s) → quietos de ~24,6 a ~25,6 s, cámara parada; después **fundido a NEGRO** de 0,5 s (no cruzado) y outro2 desde negro; la voz del cierre entra ~0,3 s después del inicio del fundido (≈25,9 s). Mueve outro2 y su sting a la vez en `mix.py`. Que el logo no se vea nunca encima del remate.
2. **Marcador (15,6–16,8 s):** que los dos números suban a la vez y en proporción (0–0 → 21–20 → 43–41), para que no se lea «20 – 0», «43 – 0» ni «43 – 12».
3. **Pronunciación (opcional):** no se regenera la voz solo por esto; si se rehace por otro motivo, «U-ce-ele-a» y «Pit Carríl» en el prompt.
4. **Mezcla:** baja el whoosh/papel del viaje de 1,2–2,0 s unos 6 dB y deja el true peak ≤ −1,0 dBTP.
5. **Pie de créditos y pies de foto:** a 17 px como mínimo y el pie final ≥ 1,5 s quieto (o fuera de pantalla, quedan en el caption).
6. **Gancho (opcional):** abrir con la tensión («Quedan siete segundos contra el campeón…» o «Princeton contra el vigente campeón») y dar el año después.
7. Sube el `video_mudo.mp4` nuevo al repo (el del repo tiene el cierre de la app) y pon el vídeo nuevo en la cola y en el panel a la vez.
