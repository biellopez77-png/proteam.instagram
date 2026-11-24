# Motor editorial 2D (v4) — cómo se fabrica un reel

> Biel, 23–24/11: **motion graphics editorial en 2D, nada en 3D.** Cada reel es una revista que se mueve. Este documento manda sobre cualquier mención a three.js, escenas 3D, `luz.html` o «sala oscura modelada».

## El lenguaje
- Retícula de revista: folio arriba («ProTeam — Nº 00 · p. 07»), pie con el crédito real de cada foto.
- Fotos reales con licencia de `banco/fotos` en **duotono azul** (#02050F → #636DFF → #F4F7FB), grano de imprenta. Capturas reales de la app (`banco/proteam/*_CAPTURA_*`) tal cual, como figura.
- Tipografía: **Plus Jakarta Sans 800** gigante y recortada (la palabra cruza la página o lleva la foto dentro de las letras); **Instrument Serif cursiva** para la frase que importa; IBM Plex Mono para pies y folios.
- Cámara 2D: paneo por la retícula con rampa de velocidad, desenfoque al cambiar de plano, empuje hacia la figura, paso de página antes del cierre.
- **Ultravioleta (#8B5CF6) una sola vez por pieza**: el subrayado de la frase clave, tras un silencio.
- Sonido sintetizado (sin licencias): zumbido grave, papel en cada corte, obturador en cada foto, silencio antes de la frase, acorde en el ultravioleta, resolución en el cierre.
- 13–16 s, 5 páginas. Cierre: «ProTeam» + una línea serif.

## Cómo se hace
1. `tools/reel_v5/piezas/<ID>/spec.json` (ver E02–E06 como ejemplo):
```json
{"titulo":"…","fase":"Problema · mié 2/12","tono":55,
 "paginas":[{"tipo":"palabra","d":2.5,"palabra":"DOMINGO","foto":"OBJETO_GENERAL_FOTO_001","fig":"Fig. 1 — …","hora":"23:40"}, …]}
```
2. Tipos de página:
   - `palabra` {palabra, foto, fig, hora, size?} — palabra gigante que cruza con foto detrás.
   - `dentro` {palabra, foto, serif, cap, size?} — la foto dentro de las letras + frase serif.
   - `reticula` {figs:[3×{foto, lab}], letras?, labSize?} — paneo con rampa por tres figuras. `labSize` (p. ej. 40) pone los pies grandes, en tinta y con saltos de línea, para cuando el dato va en el pie.
   - `frase` {foto, pre, serif, uv, size?, uvTop?, pos?} — foto a sangre + frase serif; `uv:true` en UNA página.
   - `cifra` {num, pre, serif, cap, size?} — número o fecha enorme. **Solo datos reales.**
   - `captura` {foto: PRODUCTO_…_CAPTURA_…, fig, serif} — captura real de la app como figura.
   - `portada` {l1, serif, l2, fotos:[3], cap, size?} — titular a doble página.
   - `cierre` {serif}.
3. Hoja de contacto: `python3 tools/reel_v5/motor/build.py <ID> --still` → `piezas/<ID>/hoja.png`. Mírala: ¿algo se corta, se pisa o no se lee en un móvil? Ajusta `size`, `uvTop`, textos.
4. Render: `python3 tools/reel_v5/motor/build.py <ID>` → `final.mp4` (~5 Mb/s), `cover.jpg`, `sonido.wav`. Créditos y folios salen solos del inventario.
5. Fotos con licencia «sin verificar» o de personas famosas: el motor las rechaza / no se usan. Caras: solo de fotos con licencia y nunca dando a entender que apoyan ProTeam.

## Reglas de texto
Español de España, frases cortas, nada de precio, nunca cifras de apuntados, nada inventado, sin el nombre de Biel. Calentamiento (26–28/11): ni app ni fecha.

## Láminas: carruseles y Stories (Clara, 24/11)
Las láminas son páginas de la misma revista que el reel: mismos colores, fuentes, duotono, grano, folio arriba («ProTeam — Nº 00 · p. 0X») y crédito de la foto abajo.
1. Fuentes en `agencia/fabrica-v4/carruseles/<ID>/`: `carrusel.json` (1080×1350) y `stories.json` (1080×1920), `{"numero","seccion","formato":"carrusel"|"story","laminas":[…]}`.
2. Tipos (`tools/reel_v5/motor/lamina.html`):
   - `palabra` {palabra, foto, fig, hora, serif?, size, left} — lámina 1: palabra gigante recortada sobre la foto.
   - `dentro` {palabra, foto, serif, cap, size, top} — la foto dentro de las letras.
   - `figuras` {letras, figs:[3×{foto, lab}]} — retícula de tres figuras con pie.
   - `frase` {foto, pre, serif, uv?, size, pos, uvW} — foto a sangre + frase serif. **`uv:true` en una sola lámina** (el script lo comprueba).
   - `portada` {l1, serif, l2, fotos:[3], cap, size} — titular a doble página.
   - `final` {cap, serif, big, bigLines, lista:[…], firma} — qué se lleva el entrenador.
   - `pregunta` {foto, cap, big, serif, size} — Story: pregunta escrita como titular.
   - `encuesta` {pre, big, serif, foto?, size} — Story: titular arriba y hueco limpio para pegar el sticker a mano.
3. Render: `python3 tools/reel_v5/motor/lamina.py <ID> --hoja` → `png/<ID>-c1.png…`, `-s1.png`, `-s2.png` y `hoja.png` (todas a 360 px de ancho, tamaño móvil). Mira la hoja antes de subir: palabras que no se leen, texto que se pisa, folio tapado por la foto.
4. Máximo 5–8 palabras grandes por lámina. Mismas reglas de texto y de licencias que el reel.
