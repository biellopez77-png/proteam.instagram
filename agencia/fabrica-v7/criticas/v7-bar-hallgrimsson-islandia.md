# Crítica · v7-bar-hallgrimsson-islandia «Quien conoce el plan» · r1

**Andrés (05) · 28/11/2026 · Nota: 78/100 → NO APROBADO. Vuelve a montaje.**

Material revisado: el vídeo **de la cola** (`publicar/cola.json` → `531cf4b5-…mp4`, 28,1 s), descargado y analizado en el sandbox de Higgsfield (faster-whisper small con marcas por palabra, niveles por segundo y EBU R128), y `tools/reel_v7/v7-bar-hallgrimsson-islandia/video_mudo.mp4` (fotogramas cada 0,5 s a tamaño móvil y fotogramas sueltos a 0,0 / 14,0 / 17,5 / 23,6 / 24,0 / 24,3 s).

## Comprobaciones duras
- **Voz entera** (whisper): «Dos horas antes de cada partido en casa, el entrenador de Islandia se iba a un bar. Era Heimir Hallgrímsson (lo escribe «Haimier Halgrimson»; se oye el nombre completo), dentista. Allí contaba a los aficionados el once, el sistema y el plan. Puertas cerradas, ni una foto. Nunca se filtró nada. Islandia, con unos 350.000 habitantes, eliminó a Inglaterra en la Eurocopa de 2016. Quien conoce el plan, lo defiende.» Igual que «## Voz». «defiende» acaba a 23,92 s.
- **Cierre nuevo:** «Dale like y síguenos para más vídeos como este» (24,40–27,28 s). En pantalla, «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este». **No se dice «app» en ningún momento.**
- **Caption de la cola:** termina con «¿Te ha servido? Dale like y síguenos para más vídeos como este.» Sin app, producto, lista, lanzamiento, precios, fechas, cifras de apuntados ni nombre de Biel.
- **Niveles:** −16,3 LUFS integrados, pico −1,5 dBFS. Voz estable entre −17 y −21 dB RMS por segundo; música suave debajo; cierre a −20 dB y cola limpia a 28 s. Música y efectos de Epidemic (reales).
- **Datos:** todos con fuente en el guion: dos horas antes de cada partido en casa, once/sistema/plan, puertas cerradas sin fotos y «nada se filtró» (Sports Illustrated 2018; Reuters 2016; FIFA 2017); dentista (Reuters; FourFourTwo 2021); ~350.000 habitantes (SI; FourFourTwo); Inglaterra 1–2 Islandia, Niza, 27/6/2016 (UEFA; The FA). En pantalla «al principio, unos pocos → después, cientos», sin cifra inventada. Correcto.
- **Fotos:** Laugardalsvöllur (Hlynz, CC BY 3.0) y Hallgrímsson (Svetlana Beketova, CC BY-SA 3.0), ambas «modificada» en el caption; sin logotipos de la FIFA, la UEFA ni la KSÍ; nada sugiere que nadie apoye ProTeam.

## Lo que falla
1. **Texto solapado en el paso al cierre (suspenso automático).** A 24,3 s el logo «ProTeam» del cierre aparece encima de la pizarra y de «LO DEFIENDE.»: el fundido es cruzado, no a negro. Es el mismo fallo que se ha corregido en Tacos de Berna, Rangnick y Auerbach.
2. **El remate no respira.** «LO DEFIENDE.» se completa a ~23,5 s y el fundido empieza a 24,10 s: menos de 0,7 s entero y quieto (hace falta ≥ 1 s con la cámara parada). La voz del cierre entra a 24,40 s, **0,48 s** después de «defiende».
3. **Primer fotograma vacío.** A 0,0 s solo se ve «Dos», atenuado, sobre fondo azul: ni foto ni palabra fuerte. La polaroid del estadio y «−2:00» llegan a 0,5 s. Además, lo raro de la historia (el seleccionador se va a un bar a contar el once) no aparece hasta 4,3 s.
4. **Texto cortado en viajes.** A 17,5–17,7 s el contador sale como «≈350.00» cortado por el borde derecho mientras la cámara se va al marcador; a ~11,5 s «…nados / el plan.» cortado por la izquierda. Son viajes, pero se nota a tamaño móvil.
5. **Mapa de Islandia poco reconocible.** El contorno dibujado (15,5–18,3 s) parece una mancha; con el rótulo «REIKIAVIK» se entiende, pero no se reconoce la isla.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 14/20 | Historia muy buena y remate citable, pero el fotograma 0 está vacío y la decisión rara (el bar) llega a 4,3 s. |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Todo entra con su palabra: reloj, puerta, «DENTISTA.», once → 4-4-2 → flechas, cerrojo, móvil tachado, sello, contador, «2». |
| Transiciones | 10/15 | Viajes suaves, pero arrastran texto cortado y el fundido final es cruzado y pisa el remate. |
| Sonido | 13/15 | Voz clara y confiada, música suave debajo, efectos bajos; el cierre entra pegado a «defiende» (0,48 s). |
| Verdad y fuentes | 15/15 | Cada dato con fuente; cifras dudosas fuera de la voz. |
| Estética | 8/15 | Paleta y tipografías bien, fotos con licencia; pero logo sobre el remate (solapado), textos cortados en viajes y mapa poco reconocible. |
| **Total** | **78/100** | Suspende además por texto solapado. |

## Correcciones (para Marta, 02)
1. **Remate entero y quieto ≥ 1 s:** «Quien conoce el plan... / LO DEFIENDE.» completo, con la cámara parada desde que acaba «defiende» (23,92 s) hasta ~25,0 s.
2. **Fundido a NEGRO de 0,5 s** (xfade fadeblack o apagar el remate a fondo) desde ~25,0 s, y outro2 desde negro: el logo «ProTeam» no puede aparecer mientras el remate siga en pantalla.
3. **Audio:** la misma voz, música y efectos; retrasa outro2 y su sting para que «Dale» entre ~0,3 s después del inicio del cierre (≈ 1,3–1,5 s después de «defiende»). Mantén −16/−17 LUFS y pico ≤ −1,0 dBTP.
4. **Fotograma 0 con el gancho:** que a 0,0 s ya estén la polaroid del estadio y el reloj «−2:00» (o la palabra «BAR» / «−2:00» grande), no solo «Dos» atenuado. Opcional: adelantar el letrero «BAR» para que lo raro se vea antes.
5. **Nada cortado en los viajes:** que el contador «≈350.000» y el texto de «el plan.» se apaguen antes de salir por el borde (o que el viaje empiece cuando ya no están).
6. **Mapa:** un contorno de Islandia reconocible (fiordos del noroeste, península de Reikiavik), sigue rotulado «recreación».
7. Sube el `video_mudo.mp4` nuevo con outro2, el vídeo nuevo a cloudfront, `files` de `publicar/cola.json` (sigue en «revisión») y el panel. Después, tarea «Auditar v7 v7-bar-hallgrimsson-islandia».
