# Crítica de vídeo v4-ED01 · «El trabajo que no se ve» (piloto editorial 2D)

Andrés (05) · 24/11 · criterio v4 (Biel, 24/11) · vídeo `tools/reel_v5/v4-ED01/final.mp4` (1080×1920, 25 fps, 15,2 s) · en cola para jue 26/11 (calentamiento).
Método: un fotograma por segundo y cuatro por segundo en los cambios, todo a 270–360 px de ancho (tamaño móvil); muestreo de píxeles para el violeta; sonido en ventanas de 0,1 s (RMS) con ffmpeg + numpy.

## Nota: **68/100 · SUSPENSO** (dos suspensos directos) → vuelve a montaje

| Criterio | Peso | Nota | Por qué |
|---|---|---|---|
| Idea editorial clara | 25 | 19 | «El trabajo que no se ve» es una idea limpia y de entrenador. Pero las dos frases que la cuentan («Martes» y «Nadie graba esto. Nadie lo aplaude.») no se leen en el móvil (ver legibilidad): sin ellas el arranque es «MART… ARTE / NADIE mira.» y la idea solo aparece en el segundo 9. |
| Legibilidad en móvil | 20 | 11 | MARTES nunca se ve entero; pies y créditos en mono de 22–26 px (≈7–9 px en un móvil); EL TRABAJO entra cortado por la derecha. |
| Ritmo y sonido | 15 | 10 | Estructura buena: paneo con rampa, desenfoque entre planos, silencio real antes de la frase (7,5–8,2 s, −52 dBFS) y subrayado tras él. Pero el zumbido es plano (−22 dB de 0,3 a 13,6 s), papel y obturador casi no se oyen (+1–2 dB en 4,8 / 5,6 / 6,3 s), el golpe más fuerte es el de 2,4 s (−7,5 dB) y el acorde del ultravioleta apenas sube (+4 dB, 9,4–9,8 s): la jerarquía del sonido está al revés. Final sin resolución clara: corta a −23 dB. |
| Encaje de fase | 15 | 9 | Sale el jue 26/11 (calentamiento: curiosidad, misterio, ni app ni fecha). No hay app ni fecha, bien; pero «Todo esto es lo que decide el sábado» explica, es tono de problema/contexto, no de «algo se está encendiendo». |
| Identidad | 15 | 10 | Paleta, duotono, grano, Jakarta + Instrument Serif + Plex Mono, folios y créditos: todo en su sitio, no parece plantilla. Falla la regla del ultravioleta (ver abajo). |
| Verdad | 10 | 9 | Sin cifras ni datos. Las cinco fotos están en `banco/INVENTARIO.csv` con licencia (DP, CC BY 2.0, CC BY-SA 4.0) y crédito en pantalla y en caption; sin caras ni famosos. «Vestuario, 18:55» es una foto del Estadio de Silesia: vale como ilustración, no como lugar real del entrenador. |
| **Total** | 100 | **68** | |

## Suspensos directos

| Regla | ¿Cae? | Dónde |
|---|---|---|
| Algo en 3D | No | Todo 2D. |
| **Texto cortado o que se pisa** | **Sí** | 0,0–2,4 s: MARTES (430 px) es más ancho que la página y nunca se ve entero: primero «MART», luego «ARTE»; la S no aparece nunca. En móvil se lee «ARTE». 10,9–11,5 s: EL TRABAJO entra con la O cortada por el borde derecho y en reposo (12–13 s) la O queda pegada al borde, sin margen. 7,2–7,5 s: el pie de la Fig. 3 se pisa con el de la Fig. 2 durante el paneo. |
| **Más de un momento ultravioleta** | **Sí** | 1,60–1,75 s: `textShadow` de MARTES con `rgba(139,92,246,.7)` (aberración cromática en violeta, se ve el borde violeta en el fotograma 1,64 s). El ultravioleta bueno es el subrayado de «el sábado» (9,1–9,8 s, #8E64FA medido). Son dos. La línea del cierre es #636DFF (azul), esa sí vale. |
| Datos inventados, precio o apuntados | No | |
| Caras de famosos o fotos sin licencia | No | |
| Parece plantilla genérica | No | |

## Marcas de tiempo

- **0,0–2,4 · p. 01 MARTES.** Foto del carro de balones bien en duotono. La palabra cruza la página pero no se completa nunca. «19:42 · Campo 3» en mono 26 px: ilegible en móvil. 1,60–1,75 destello violeta.
- **2,4 · corte a NADIE.** Golpe de −7,5 dB: el pico de toda la pieza, demasiado pronto.
- **2,4–4,7 · p. 07 NADIE / mira.** NADIE con la foto dentro de las letras se lee bien; «mira.» en serif bien. «Nadie graba esto. Nadie lo aplaude.» en mono 26 px: la frase que cuenta la idea, ilegible.
- **4,7–8,0 · pp. 12–13 retícula.** Paneo con rampa y desenfoque a los 5,7–6,3 s: bonito. Pies de foto (22 px) ilegibles; «LISTA CONVOCADOS» de fondo casi invisible (#1a2440 sobre #02050F) y cortado: decoración que no se lee ni aporta. Empuje hacia el balón correcto.
- **7,5–8,2 · silencio** (−52 dBFS). Bien.
- **8,4–10,8 · p. 19 frase + UV.** «Todo esto es / lo que decide el sábado.» y subrayado violeta a 9,1–9,8. Es el mejor momento. El «Todo esto es» en mono 26 px se pierde.
- **10,8–13,3 · p. 24 doble página.** EL TRABAJO / que no / SE VE. + tres fotos. Entrada cortada (ver arriba).
- **13,0–13,75 · paso de página**, 13,75–15,2 cierre «ProTeam / para el que lo prepara.» con línea azul. Correcto, pero 1,4 s de cierre y el audio no resuelve.

## Correcciones concretas (para Marta)

ED01 está hecho a mano en `tools/reel_v5/base/editorial.html` y no tiene `spec.json`. **Pasarlo al motor**: crear `tools/reel_v5/piezas/v4-ED01/spec.json` y montar con `build.py` (así las correcciones son campos del spec y el motor controla el ultravioleta único y los créditos). Mapeo y cambios:

1. **p. 01 → `palabra`** {palabra:"MARTES", foto:"PROTEAM_OBJETO_BALONES_CARRO_FOTO_001", fig:"Fig. 1 — Carro de balones", hora:"19:42 · Campo 3", **size: 300** (o lo que haga que se lea entera al menos 0,6 s)}. Comprobar en la hoja que en algún momento se ve «MARTES» completo.
2. **Quitar el destello violeta de 1,6 s** (si se queda en editorial.html: borrar la línea `s1t.style.textShadow` o cambiar `rgba(139,92,246,.7)` por `rgba(106,168,255,.6)` en los dos lados). En el spec: un solo `uv:true`, en la página de la frase.
3. **p. 07 → `dentro`** {palabra:"NADIE", foto:"PROTEAM_OBJETO_GUANTES_CONO_FOTO_001", **serif:"mira."**, **cap:"Nadie graba esto. Nadie lo aplaude."**} — y que `cap` salga a ≥ 44 px o pase a serif (es la idea, no un pie).
4. **pp. 12–13 → `reticula`** con **`labSize: 40`** (pies grandes, en tinta) y `letras:"LISTA CONVOCADOS"` solo si se lee; si no, quitarlo.
5. **p. 19 → `frase`** {foto:"PROTEAM_OBJETO_BALON_LINEA_FOTO_001", pre:"Todo esto es" (≥ 40 px), serif:"lo que decide el sábado.", **uv:true**}.
6. **p. 24 → `portada`** {l1:"EL TRABAJO", serif:"que no", l2:"SE VE.", fotos:[silbatos, vestuario, balones], cap:"Lo que pasa entre partido y partido", **size: 150**} para dejar ≥ 64 px de margen derecho también en la entrada.
7. **Sonido**: bajar el golpe de 2,4 s unos 8 dB (que no sea el pico), subir papel/obturador a +6 dB sobre el zumbido en cada corte y foto, acorde UV a +10 dB sobre el zumbido, y resolución en el cierre con caída a −40 dB al final (15,0 s) para que el bucle no corte.
8. **Fase**: para el 26/11 (calentamiento) quitar la explicación: cambiar la frase UV por algo que abra en vez de cerrar, p. ej. `serif:"Alguien lo está viendo."` (curiosidad, sin app ni fecha), y dejar «lo que decide el sábado» para la versión de problema/contexto. Si Biel prefiere la frase actual, mover ED01 a contexto (lun 30/11).
9. **Cierre**: `cierre` {serif:"para el que lo prepara."} con 2 s (13,2–15,2).

Mirar la hoja (`build.py v4-ED01 --still`) antes de renderizar: MARTES entero, ningún texto por debajo de 40 px salvo folio y crédito, nada pegado al borde, un solo violeta.
