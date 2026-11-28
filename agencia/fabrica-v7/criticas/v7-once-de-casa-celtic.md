# Crítica · v7-once-de-casa-celtic «Los once de casa» (historia con fotos)

**Andrés (05) · 28/11/2026 · Nota: 80/100 → NO PASA (mínimo 85). Vuelve a montaje (Marta B, 02).**

Material revisado: el vídeo de `publicar/cola.json` (`da97d7e8-…mp4`, 25,6 s, cierre outro2), descargado en el sandbox de Higgsfield; `video_mudo.mp4` del repo, un fotograma cada 0,5 s a 270 px y recortes a 405 px y a tamaño real; guion, `CREDITOS.md` y caption.

## Comprobaciones duras
- **Voz entera y cierre nuevo:** faster-whisper small oye: «Lisboa, 1967. El Celtic gana la Copa de Europa al Inter. Empieza perdiendo por un penalti y gana 2-1. Es el primer equipo británico que lo consigue, pero el dato está en el mapa. Los 11 de Joxton [Jock Stein] nacieron a menos de 50 kilómetros de su estadio. Antes de buscar lejos, mira quién juega cerca.» y «Dale like y síguenos para más vídeos como este» (21,88–24,8 s). Coincide con «## Voz». En pantalla: «ProTeam · ¿Te ha servido? · Dale like y síguenos · para más vídeos como este» (22,0–25,6 s). Ni app, ni producto, ni lista de espera, ni lanzamiento.
- **Niveles:** −16,0 LUFS integrados, true peak −0,9 dBTP, LRA 2,7 LU. Voz entre −13 y −18 dB RMS por segundo; los valles solo con música, entre −31 y −43 dB. Hueco a 21 s (−28,8 dB) entre «cerca» y el cierre: correcto.
- **Música y efectos:** reales (Epidemic: piano y cuerdas suaves; papel, chinchetas, lápiz, obturador, placas de marcador), bajos.
- **Fotos:** Tagido (DP), Anefo (CC0), Thomas Nugent (CC BY-SA 2.0), Crowsus (CC BY-SA 4.0), con crédito en cada foto, en el pie final (≈17 px, se lee) y en el caption. Stein es foto de archivo; nada sugiere apoyo a ProTeam.
- **Caption:** termina con «¿Te ha servido? Dale like y síguenos para más vídeos como este.». Sin precios, sin Biel, sin cifras de apuntados.
- **Texto:** nada cortado en plano quieto («JOCK STEI» a 9,5 s es la escritura en curso).

## Verdad y fuentes
Todo tiene fuente en el guion (UEFA 2003; The Irish Times 2019): 25/05/1967, Estádio Nacional, 2-1 al Inter tras el penalti de Mazzola (7′), goles de Gemmell y Chalmers; primer equipo británico campeón de Europa; los once nacidos a menos de 30 millas (48 km) de Celtic Park → «a menos de cincuenta kilómetros». Las chinchetas van rotuladas «ejemplo, no ubicación exacta» y el mapa «recreación». Bien.

## Nota por apartados
| apartado | nota | por qué |
|---|---|---|
| Historia real y gancho | 11/20 | La historia es muy buena para cantera y el remate se cita solo. Pero el gancho es exactamente el prohibido: **«Lisboa, 1967.»** (GUION_VIRAL §3). Y detrás, 1 s sin voz (≈2,2–3,2 s) con la pantalla casi vacía. El dato fuerte (los once, 50 km) no llega hasta 13,6 s. |
| Cada cosa que dice la voz se anima en su momento | 17/20 | Muy bien sincronizado: copa y fichas, marcador 0–1 en «perdiendo», punto de penalti en «penalti» (7,0 s), 1–1 → 2–1 en «dos a uno», ficha de Stein y subrayado, contador 0→3→7→11 con las chinchetas, compás y «50 km» ultravioleta en su palabra. Fallan los vacíos: 2,5–3,5 s y 12,0–12,7 s (mapa en blanco mientras dice «Pero el dato»). |
| Transiciones | 11/15 | Viajes suaves y sin destellos, pero el primero (≈2,3–3,3 s) pasa por un plano casi negro con un rótulo diminuto. El remate «MIRA QUIÉN JUEGA CERCA.» está entero solo ~21,0–21,8 s y entra el cierre con fundido cruzado, sin pasar por negro; la voz del cierre entra a 0,7 s de «cerca». |
| Sonido | 13/15 | Voz confiada y clara, música real suave, efectos bajos. «Jock Stein» suena algo pegado (whisper: «Joxton»). Silencio de voz de 1 s en el segundo 2, justo donde más se pierde gente. |
| Verdad y fuentes | 15/15 | Todo con dos fuentes y sin exagerar. |
| Estética | 13/15 | Paleta, tipografías, ultravioleta una sola vez (50 km), créditos legibles. Pero la foto final de Celtic Park enseña el **escudo del club** en la fachada (derecha) y el rótulo grande del estadio; y en 6–9 s el tercio inferior queda vacío. |
| **Total** | **80/100** | No pasa. |

## Correcciones (por orden de importancia)
1. **Gancho nuevo (obligatorio; hay que regrabar la voz y cambiar «## Voz» del guion).** Abrir con el dato del mapa, no con «Lisboa, 1967.». Propuesta (≈58 palabras):
   > «Los once nacieron a menos de cincuenta kilómetros de su estadio. Y ganaron la Copa de Europa. Lisboa, 1967: el Celtic de Jock Stein empieza perdiendo con el Inter por un penalti y gana dos a uno. Es el primer equipo británico que lo consigue... Antes de buscar lejos, mira quién juega cerca.»
   Primer fotograma: el mapa con Celtic Park, el contador «11» y el círculo «50 km» ya dibujado (ultravioleta en «cincuenta kilómetros», única vez). La postal de Lisboa pasa a la tercera frase. Si se prefiere mantener el texto actual, como mínimo poner «LOS 11 · A MENOS DE 50 KM» en pantalla desde el fotograma 0 (pero «Lisboa, 1967.» sigue siendo el gancho prohibido en la voz: no basta para 85).
2. **Sin huecos al principio:** nada de silencio de 1 s en los primeros 3 s; el viaje no puede pasar por un plano vacío. Lo mismo en 12,0–12,7 s: que el mapa ya esté dibujado cuando dice «el dato».
3. **Remate quieto y a negro:** «MIRA QUIÉN JUEGA CERCA.» entero y quieto ≥ 1 s con la cámara parada, fundido a NEGRO de 0,5 s y outro2 desde negro; la voz del cierre ≥ 1,2 s después de «cerca».
4. **Escudo del Celtic** en la foto de Crowsus: difuminarlo (y valorar recortar el rótulo grande) para que no parezca contenido del club.
5. «Jock Stein»: en la nueva toma, comprobar con whisper que se oye «yok stin» separado.
6. Opcional: subir 150–200 px las escenas de 6–9 s o agrandar el marcador para llenar el tercio inferior.
7. `video_mudo.mp4` nuevo en el repo, cola y panel actualizados a la vez; caption sin cambios salvo que cambie la primera frase (puede quedarse igual).
