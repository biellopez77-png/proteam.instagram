# SKILL · Visual Asset Discovery (03 Resource Bank)
**Para qué:** encontrar la imagen o el clip que cuenta lo que la pieza necesita, con licencia comprobada.

## Herramientas (comprobadas)
- **Sandbox de Higgsfield** (`mcp__Higgsfield__sandbox_exec`): tiene red. API de Wikimedia Commons: `action=query&list=search&srnamespace=6&srsearch=…` y `prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=1600`, con User-Agent descriptivo.
- El contenedor local **no** llega a Commons, Instagram ni YouTube.
- Traer archivos: `image_paths` (hasta 4 por llamada, 512 KB en total); vídeo corto empaquetado como describe la skill del agente (PNG contenedor) o `pendiente` con su enlace.

## Procedimiento
1. **Parte de la necesidad narrativa**, escrita por 01 o 02: «qué tiene que transmitir» y «en qué segundo». Tradúcela a una **imagen concreta**: sujeto + acción + escala de plano + emoción. («Entrenador reconocible, solo, mirando al suelo, plano medio, vertical» en vez de «entrenador».)
2. **Mira primero el banco** (`INVENTARIO.csv`, estado `disponible`, no usada en los últimos cinco Reels).
3. **Consulta por nombre propio** y contexto: «Hansi Flick training 2024», «Sarunas Jasikevicius sideline», «handball coach timeout EHF». Tres consultas distintas por necesidad, en inglés y en el idioma del país del club.
4. **Filtra por licencia** en `extmetadata.LicenseShortName`: CC0, dominio público, CC BY, CC BY-SA. Lo demás se descarta.
5. **Filtra por calidad:** lado largo ≥ 1600 px, nítida, sujeto recortable a 9:16 (o 4:5 para carrusel) sin perder la cara, sin marca de agua ni cartelería dominante de terceros.
6. **Mira cada candidata con Read** y puntúa 0–2: cuenta lo pedido · reconocible · recortable · luz y contraste · no repetida. Se propone a partir de 7 sobre 10, con **una línea de justificación narrativa**.
7. **Entrega tres opciones** por necesidad cuando existan (principal y dos alternativas) y registra las elegidas (skills `03-media-asset-management` y `03-media-rights-source-tracking`).
8. Si no hay nada válido, se dice, y se propone: otra imagen que cuente lo mismo, un elemento de edición, o un material que debe grabar Biel (pantalla, acción, duración).

## Qué no vale
Stock genérico, posados, imágenes con estética de IA, entrenadores anónimos como protagonistas, fotos políticas o polémicas, cualquier cosa cuya licencia no se haya leído en la fuente.

## Control
¿Cada recurso tiene su línea de «qué cuenta»? ¿Licencia leída, no supuesta? ¿He mirado la imagen?
