# Crítica · v7-cuatro-minutos-milan-1954 «Cuatro minutos sin tirar» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 75/100 → NO APROBADO. Vuelve a montaje.**

Material revisado: `tools/reel_v7/v7-cuatro-minutos-milan-1954/video_mudo.mp4` (60 fotogramas, uno cada 0,5 s, a 360 px de ancho, y fotogramas a tamaño completo a 9,0 / 15,5 / 17,5 / 24,0 s), `reel.html`, `mix.py`, `words.json`, `CREDITOS.md`, el guion y el vídeo de la cola (`488244e8-…mp4`, 27,9 s), descargado y analizado en el sandbox de Higgsfield (faster-whisper small y medium, espectrograma, RMS cada 50 ms, EBU R128). El vídeo de la tarea (`33cb34f4-…`) ya está en `files_old`: se audita el de la cola.

## Comprobaciones duras
- **Cierre:** el vídeo de la cola acaba con outro2 en pantalla («¿Te ha servido? / Dale like y síguenos / para más vídeos como este», 24,5–27,9 s) y en voz («Dale like y síguenos para más vídeos como este», 24,2–27,1 s). Sin «app» en voz ni en pantalla. **Pero el `video_mudo.mp4` del repo lleva todavía el cierre retirado** («ProTeam / Estamos terminando la app. / Síguenos para no perderte nada. / MUY PRONTO, NOVEDADES», 25,0–30,0 s). Hay que sustituirlo.
- **Caption de la cola:** termina la parte de texto con «¿Te ha servido? Dale like y síguenos para más vídeos como este.» (después, fuentes, créditos y hashtags, como el resto de v7 aprobados). Sin app, sin precios, sin fechas de lanzamiento. **El post del panel aún tenía el caption con «Estamos terminando la app de ProTeam…» y el vídeo viejo:** corregido por mí con el caption y el vídeo de la cola.
- **Voz entera → FALLA.** Whisper (small, vídeo entero) oye: «Indiana, 1954. Un instituto de 161 alumnos llega a la final del estado. Enfrente, una escuela 10 veces más grande. Último cuarto. Bobby Plump coge el balón y no lo suelta. Más de 4 minutos sin tirar. 15.000 personas en la grada. Últimos segundos, tira. 32 a 30. Ganar a veces es saber. Dale like y síguenos…». **Falta «esperar», la última palabra y la idea del vídeo.** Whisper medium sobre 22,0–24,15 s tampoco la oye («…es saber.»); sobre 24,25–24,9 s solo oye «Dale like». RMS cada 50 ms: 23,95 s −33 dB, 24,00 −38, 24,05 −39, 24,10 −43, 24,15 −46 dB: donde `words.json` pone «esperar» (23,94–24,26 s) apenas queda un resto de la «s» y silencio; a 24,2 s entra la voz del cierre. En pantalla ESPERAR se enciende a ~24,0 s, pero no se oye: el remate queda «Ganar, a veces… es saber.» y el cierre se come la palabra clave.
- **Niveles:** −18,6 LUFS integrados, pico −1,0 dBFS. Voz entre −14 y −22 dB RMS por medio segundo; pausas con música a −28/−30 dB (2,5 · 6,5 · 9,5 · 13,5 · 16,0 · 18,0 · 21,5 s): la voz va ~10–12 dB por encima. Efectos bajos y reales (Epidemic). Música real, una sola pista.
- **Fotos:** Chris Flook (CC BY-SA 4.0), Phillips 66 (dominio público), Steve Shook / Groganphoto (CC BY 2.0), vía Commons; créditos en el pie (23,5–24,4 s) y en el caption. Sin escudos ni logos; la calle de Milan rotulada «HOY»; Plump sin año ni uniforme. Nada sugiere que nadie apoye ProTeam. Se quitó bien la postal del pabellón (dominio público solo en EE. UU.).
- Sin nombre de Biel, cifras de apuntados, lista de espera ni lanzamiento.
- **Texto:** nada cortado ni solapado. «4 MINUTOS» (170 px) va de 56 a 983 px: margen justo a la izquierda pero dentro.

## Verdad y fuentes
Todo lo que dice la voz tiene fuente en el guion: 161 alumnos (WCPO, AP, Wikipedia), «diez veces más grande» (Indiana Historical Bureau; WCPO: 1.662 alumnos), el último cuarto y «más de cuatro minutos» con el balón (Wikipedia; AP), 15.000 personas (WCPO), el tiro en los últimos segundos y el 32-30 (Wikipedia, AP, IHB, WCPO). No se dice quién mandó esperar ni los segundos exactos: bien. «Ganar, a veces, es saber esperar» va como idea, sin comillas. El cronómetro «BALÓN RETENIDO» cuenta hacia arriba y está rotulado «recreación»: correcto.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 16/20 | Historia muy buena para entrenadores (paciencia, reloj, competir siendo pequeño). El arranque «Indiana, 1954.» con una puerta de museo es tranquilo: el gancho fuerte (161 contra diez veces más) llega a los 3 s y tras 0,8 s de pantalla vacía (2,3–3,0 s, viaje). Y sin «esperar», el relato no se cierra. |
| Cada cosa que dice la voz se anima en su momento | 16/20 | Muy bien: sello 1954, contador 20→152→161 con los puntos, bloque ×10 que cae, «4.º» que se enciende, «❚❚» sobre el balón en «no lo suelta», cronómetro 0:00→+4:00, grada 3.423→15.000, «TIRA.» y el balón que entra, 32 y 30 en su palabra. Flojo: el balón no va «pegado bajo la mano» de Plump, flota al lado de la foto; en «Últimos segundos» (18,5–19,5 s) el balón está quieto un segundo antes de salir; y ESPERAR se enciende sin que la voz lo diga. |
| Transiciones | 11/15 | Viajes suaves y sin destellos en las pausas. Pero el final está pisado: ESPERAR aparece a ~24,0 s y el logo ProTeam ya se cruza encima a 24,0–24,5 s; el remate no se queda ni medio segundo entero y quieto. |
| Sonido | 6/15 | Voz confiada y clara, música real suave, efectos bajos: bien hasta 23,9 s. Falla lo que más importa: la palabra final «esperar» no se oye (−38 a −46 dB) y la voz del cierre entra a 24,2 s, encima de donde debía estar. |
| Verdad y fuentes | 14/15 | Todo con fuente y con prudencia. Resta un punto: el panel tenía el caption viejo con la app (ya corregido) y el repo un mudo con el cierre retirado. |
| Estética | 12/15 | Paleta, tipografías, fichas de prensa y fotos con licencia, bien. Pero el bloque ×10 (7,0–10,0 s) y los puntos de la grada (16,5–18,0 s) van en índigo (#6E6EED aprox.), que en el móvil se lee como violeta y le quita fuerza al único ultravioleta (ESPERAR). Créditos del pie muy pequeños. |
| **Total** | **75/100** | No aprobado. |

## Correcciones (para Marta, 02)
1. **Recuperar «esperar».** Volver a mezclar con la voz entera: que «esperar» suene completo (23,94–24,26 s según `words.json`; comprobar en la toma limpia de Mateo dónde acaba de verdad) y sin fundido ni recorte de la pista de voz antes de 24,5 s. Comprobar con whisper small sobre el vídeo final que se oye «…es saber esperar.» y, en el RMS, que 23,95–24,25 s está a nivel de voz (−16/−22 dB), no a −40.
2. **Separar el remate del cierre.** ESPERAR encendido y quieto desde que se dice hasta al menos 0,8 s después de que acabe la palabra (cámara parada); el fundido a negro de 0,5 s empieza después, y la voz de outro2 entra como pronto 0,5 s tras «esperar» (si acaba a 24,26 s: fundido desde ~25,1 s, voz del cierre desde ~25,6 s). Nada del logo ProTeam sobre ESPERAR.
3. **Ultravioleta solo en ESPERAR:** pasar el bloque ×10 y los puntos de la grada a azul de la paleta (#6AA8FF o un azul grisáceo), no índigo.
4. **El balón bajo la mano de Plump** en «coge el balón y no lo suelta» (11,8–13,3 s): que el balón quede pegado al borde inferior de la ficha, junto a la mano/cuerpo, con el «❚❚» encima.
5. **Gancho:** acortar el viaje vacío de 2,3–3,0 s o dejar la ficha de Milan visible hasta que entre «Un instituto» (que no haya pantalla vacía en los primeros 3 s).
6. **Subir `video_mudo.mp4` nuevo con outro2** al repo (el actual lleva «Estamos terminando la app»).
7. Créditos del pie a 17 px como en los v7 aprobados.
8. Mismo caption de la cola (está bien). Panel ya corregido; al acabar, actualizar el vídeo del panel y de la cola.
