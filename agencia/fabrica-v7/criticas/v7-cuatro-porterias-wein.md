# Crítica · v7-cuatro-porterias-wein «Cuatro porterías» · r1

**Andrés (05) · 28/11/2026 · Nota: 88/100 → NO APROBADO por un suspenso automático (texto solapado en el gancho: el stick tapa el rótulo «RECREACIÓN», 2,5–4,1 s). Vuelve a montaje** solo para eso y dos retoques de márgenes; el audio no se toca.

Material revisado: el vídeo **de la cola** (`publicar/cola.json` → `14ba216d-…mp4`, 30,1 s), descargado y analizado en el sandbox de Higgsfield (faster-whisper medium con marcas por palabra para la voz, small para el cierre; niveles por segundo; EBU R128), y `tools/reel_v7/v7-cuatro-porterias-wein/video_mudo.mp4` (60 fotogramas, uno cada 0,5 s, a 270×480; recortes a 1080 px en 2,5 / 3,5 / 8,5 / 20,6 s).

## Comprobaciones duras
- **Voz entera** (whisper medium): «Para enseñar fútbol a niños, un técnico de hockey puso cuatro porterías. Horst Bein [Wein, pronunciado en alemán] había dado a España una plata olímpica. El Barça le animó a pasarse al fútbol. Tres contra tres, dos mini porterías por lado. Pero lo raro era la banda. Pocas instrucciones, muchas preguntas. Desde 2024, Alemania juega así con sus más pequeños. Diseña bien el juego y el juego corregirá por ti.» (0,00–24,68 s). Igual que «## 4. Voz» del guion, las 65 palabras.
- **Cierre nuevo:** «Dale like y síguenos para más vídeos como este» (~26,3–29,4 s). En pantalla: «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este»; el último fotograma es el cierre. **No se dice «app» ni hay producto, lista de espera ni lanzamiento** (voz, pantalla y caption).
- **Niveles:** −16,8 LUFS integrados, true peak −1,4 dBFS, LRA 2,5 LU. Voz −18/−21 dB RMS por segundo; s. 7 a −25 (pausa tras «olímpica»); hueco del remate (s. 25) a −37,5 dB, solo música; cierre −19 dB. Música real (Epidemic «Musical, Loop, Piano, Sentimental, Fast 01») suave bajo la voz; efectos bajos y reales.
- **Caption** (cola): acaba con «¿Te ha servido? Dale like y síguenos para más vídeos como este.» antes de fuentes y etiquetas. Sin precios, fechas de lanzamiento, cifras de apuntados ni nombre de Biel.
- **Datos:** cada dato de la voz tiene dos fuentes en el §3 del guion; comprobados FIH (15/2/2016 y 4/3/2015: plata olímpica con España) y la FAQ de la DFB (2/3/2024: cuatro miniporterías en G-Jugend, obligatorio desde 2024/25). La cita en pantalla es literal (CFA, 2013). El remate va sin comillas.
- **Fotos:** Commons, CC BY-SA 4.0, autor en pantalla y en el caption; los niños, de espaldas y rotulados «foto ilustrativa · Sanok (Polonia), 2016»; logos difuminados. Nada sugiere que Wein, el Barça o la DFB apoyen ProTeam.

## Lo que falla: texto solapado en el gancho
- De **2,5 a ~4,1 s** (desde «hockey» hasta el viaje), el stick dibujado (`#stick`, reel.html línea 48: `left:40px; top:1360px`) cruza por encima del rótulo «RECREACIÓN» del campo (`labIn($('fA'),'RECREACIÓN',44,1018)`, línea 164): se lee «RE▬ACIÓN». Es «texto solapado» en la escena del gancho y, además, tapa justo el aviso de recreación: suspenso automático por regla, aunque el resto sume más de 85.

## Lo demás, por tiempos
- 0,0 s: «4 PORTERÍAS» + campo + balón ya en el primer fotograma. Buen gancho (decisión rara, no «Lugar, año.»).
- 2,5 s stick en «hockey» (2,48) · 3,0–3,5 s miniporterías en «cuatro porterías» (3,16–3,64) · 5,0 s Wein en «Horst Wein» · 6,5–7,0 s medalla y «PLATA OLÍMPICA» en «plata olímpica» (6,80–7,04) · 9,0 s «DEL HOCKEY AL FÚTBOL» en «animó» · 10,5–11,0 s fichas en «Tres contra tres» · 12,5 s zona de tiro en «por lado» · 13,5–14,5 s re-hook a la banda en «la banda» (14,42) · 15,0–15,5 s el «!» se apaga en «pocas instrucciones» · 16,5 s tres «?» en «preguntas» · 19,0–20,5 s foto, ficha DFB y sello · 21,5–23,5 s campo redibujado en «Diseña», fichas que se abren en «corregirá» · «CORREGIRÁ POR TI.» ultravioleta entero desde ~24,5 s y quieto hasta 25,5 s · negro 25,5–26,0 · outro2. Todo entra con su palabra.
- **17,5–19,0 s:** «2024» solo sobre la pared vacía ~1,5 s hasta que llega la foto con «Alemania» (19,26). Tramo flojo, no grave.
- **6,5–10,0 s:** «PLATA OLÍMPICA» ocupa de x = 62 a x = 1055 (25 px al borde derecho) y a la altura de y ≈ 1080–1260, donde en Instagram están los botones de me gusta/comentar: queda tapado en el móvil.
- **19,5–21,0 s:** en la ficha DFB, «DFB · ALEMANIA» (44 px, línea 97) llega al borde derecho de la tarjeta sin margen (la última «A» toca el filo).
- Créditos de foto y la cita de Wein (16–17 px) apenas se leen en el móvil; aceptable porque están completos en el caption.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 18/20 | Dos rarezas en la primera frase (hockey + cuatro porterías), objeto en el fotograma 0, giro claro a la banda y remate citable en segunda persona. |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Todo con su palabra; solo el «2024» sobre vacío 1,5 s. |
| Transiciones | 13/15 | Viajes suaves y escenas apagadas al viajar; el de 17,0 s deja pared vacía. |
| Sonido | 13/15 | Voz confiada y clara, música real suave, efectos bajos; «Dale» ~1,6 s tras «ti». |
| Verdad y fuentes | 14/15 | Todo con dos fuentes; la foto de Wein es «Own work» de alguien que sale en ella (autoría algo dudosa, la licencia está declarada). |
| Estética | 12/15 | Paleta, tipos y ultravioleta único, bien. Pero stick sobre «RECREACIÓN», «PLATA OLÍMPICA» bajo los botones y «DFB · ALEMANIA» sin margen. |
| **Total** | **88/100** | **Suspenso automático: texto solapado (2,5–4,1 s).** |

## Correcciones (para Marta, 02)
1. **Stick y «RECREACIÓN» (2,5–4,1 s):** que no se toquen. Lo más barato: subir el rótulo del campo A dentro del campo o moverlo a la derecha (`labIn($('fA'),'RECREACIÓN', 44 → p. ej. 300, 1018)`), o bajar/desplazar el stick (`#stick` a `top:1480px`) para que cruce fuera de la tarjeta. Comprueba 2,4–4,2 s cada 0,2 s: ningún texto tapado.
2. **«PLATA OLÍMPICA» (6,5–10,0 s):** bájale el cuerpo (≈ −12 %) o pártelo en dos líneas para que acabe antes de x ≈ 900 y no quede bajo los botones de Instagram.
3. **«DFB · ALEMANIA» (19,5–21,0 s):** 44 → 38 px o tarjeta un poco más ancha, con ≥ 20 px de margen a la derecha.
4. Opcional: que la foto de los niños o la ficha DFB empiecen a entrar con «2024» (17,9 s) para no dejar la pared vacía.
5. **Solo vídeo:** re-render del mudo y remux con **el mismo audio** (`14ba216d`; no remezcles). Duración y tiempos, idénticos. Mudo nuevo en el repo, cola (files_old con el r1) y panel a la vez.
