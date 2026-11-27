# Crítica · v7-libros-phil-jackson «Un libro para cada jugador» (historia con fotos)

**Andrés (05) · 27/11/2026 · Nota: 87/100 → APROBADO** (pub_v3 approve → vie 4/12 18:00; el primer hueco libre de las 18:00 desde mañana: del 28/11 al 3/12 ya están ocupados).

Material revisado: `tools/reel_v7/v7-libros-phil-jackson/video_mudo.mp4` (52 fotogramas, uno cada 0,5 s, a 360 px de ancho) y el vídeo final de cloudfront (`93cd7a3f-…mp4`, 26,1 s, 1080×1920, H.264 + AAC 256k) descargado y analizado en el sandbox de Higgsfield.

## Comprobaciones duras
- **Voz entera:** faster-whisper small oye 53 de 54 palabras (se come la «A» de «A Shaquille», 6,6 s); medium, sobre ese tramo, oye «A Shaquille O'Neal le tocó Nietzsche»: están las 54. Nombres claros: «Phil Jackson», «Shaquille O'Neal», «Nietzsche», «Siddhartha», «Shaq». El cierre común también se oye entero.
- **Niveles:** −16,8 LUFS integrados, true peak −0,9 dBFS, LRA 3,6 LU. Voz (RMS por 100 ms) entre −11 y −16; huecos solo con música entre −28 y −37: la voz va unos 14–15 dB por encima. Sin picos de efectos en los huecos (máximo −22 en los silencios entre frases).
- **Destellos:** salto máximo de luminancia media entre fotogramas 13,7/255 a 17,1 s (es el viaje largo de la hoja a la balda, no un destello). La hoja blanca entra en 0,3 s (13,0–13,2 s: luminancia 30 → 72): rápido pero en fundido.
- **Texto:** nada cortado ni solapado. El rótulo «A SHAQUILLE O'NEAL» ocupa de x=27 a x=1031 (margen de 27 px) y empieza en y=44.
- **Fotos:** Phil Jackson (Keith Allison, CC BY-SA 2.0), Shaq en la final de 2000 (Bigmoe797, CC BY-SA 4.0; comprobado que es O'Neal con el 34 de los Lakers, foto original en `photos/raw2.jpg`), portadas de 1908 y 1922 (dominio público). Ninguna sugiere apoyo a ProTeam. Sin logotipos de los Lakers ni de la NBA.
- **Música:** real (Epidemic, «Musical, Loop, Piano, Sentimental, Fast 01»), no sintetizada.
- Sin precios, fechas de lanzamiento, cifras de apuntados ni el nombre de Biel.

## Verdad y fuentes (comprobado hoy en The Players' Tribune y en NPR)
- Ecce Homo el primer año con Shaq; Siddhartha «the next year»; libros repartidos «on a flight at the start of a long road trip»; expulsión en Chicago contra los Bulls y Shaq leyendo Siddhartha en el autobús; el resumen en el vuelo de vuelta («a young prince, who has money, fame, and women, just like me»); «still the only one I ever received». Todo, en The Players' Tribune (Jackson, 2016).
- «Uno distinto para cada jugador»: Jeanie Buss en SI (2020), en el guion.
- Matiz para el caption, no bloqueante: «Jackson dice que fue el único que recibió (The Players' Tribune; NPR)». NPR cuenta el resumen, pero no dice que fuera el único, y con otras palabras («a young man who's rich, famous, good-looking…»). Mejor citar solo The Players' Tribune en esa frase.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | Historia muy buena y con remate. El gancho tarda: «Al empezar un viaje largo» es contexto; lo que sorprende (Nietzsche para Shaq) llega a los 7,8 s. El caption sí abre con ello. |
| Cada cosa que dice la voz se anima en su momento | 18/20 | Ventanilla y tarjeta en «viaje largo»; ficha en «Phil Jackson»; libros que caen en «libros»; balda y dorsales en «uno distinto»; portada en «Nietzsche»; calendario 1999-00 → 2000-01 en «al año siguiente»; autobús, EXPULSADO y silbato; la hoja se escribe sola; sello «N.º 1 · EL ÚNICO»; libros que se apagan y fichas que se encienden en «cada jugador». Falla poco: el sello cae a 15,1 s, con «el» y antes de «único». |
| Transiciones | 12/15 | Viajes suaves en general, pero dos son muy largos y rápidos: 10,6–11,0 s (cruza media pared hasta el autobús) y 17,0–17,3 s (de la hoja a la balda; empieza sobre «Porque», no en la pausa de 16,72–17,04). La hoja blanca entra en 0,3 s y sube mucho el brillo. |
| Sonido | 13/15 | Voz confiada y clara, música suave bajo la voz y efectos bajos. La pausa «libros... elegía» dura solo 0,26 s (18,34–18,60): el remate no respira; whisper la transcribe con coma. |
| Verdad y fuentes | 14/15 | Todo comprobado. Solo el matiz de NPR en el caption. |
| Estética | 13/15 | Paleta, tipografías y ultravioleta una sola vez (CADA JUGADOR), todo correcto. Pero «A SHAQUILLE O'NEAL» va casi de borde a borde (27 px) y muy arriba (y=44, debajo de la barra de Instagram). El recorte del dorsal hace que el 34 se lea «31». El pie de créditos (20,0–20,8 s) no se puede leer en el móvil. |
| **Total** | **87/100** | |

## Mejoras (no bloquean; para la próxima pieza o si se remonta)
1. **6,8–10,6 s:** bajar «A SHAQUILLE O'NEAL» a la zona segura (y ≥ 200) y reducirlo a 64–72 px para dejar ≥ 80 px a cada lado. O dejar solo «A SHAQUILLE» en la palabra fuerte y el nombre completo en la ficha.
2. **17,0 s:** empezar el viaje a la balda en la pausa (16,75 s) y hacerlo en 0,9 s con el desenfoque limitado a 4 px. Mejor aún: poner la balda cerca de la hoja en la pared para que el viaje sea corto.
3. **18,34–18,60 s:** alargar la pausa «libros... elegía» a 0,6–0,7 s en la mezcla, como se hizo en michels y lobanovski.
4. **13,0 s:** que la hoja entre en 0,5 s y con fondo menos blanco (#DDE3F0) para que el brillo no suba de golpe.
5. **15,1 s:** retrasar el sello a 15,2 s (con «único»).
6. **7,0 s:** encuadrar la foto de Shaq un poco más a la izquierda para que se vea el 34 entero.
7. **Caption:** HECHO por Andrés en publicar/cola.json. En la frase del único resumen, «(The Players' Tribune; NPR)» pasa a ser «(The Players' Tribune)».
8. **Gancho:** la próxima vez, abrir con el dato que sorprende (por ejemplo, «Phil Jackson le dio Nietzsche a Shaquille O'Neal») y contar el contexto después.
