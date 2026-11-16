# SKILL · Video Editing Analysis (02 Creative Direction)
**Para qué:** analizar montaje, ritmo, cortes, continuidad y sincronía con datos del vídeo real, propio o de referencia.

## Herramientas
`python3 tools/video_intel.py analyze <vídeo> --id <id> --modo detalle` → `intel/videos/<id>/informe.md` (planos, cortes, tramos sin movimiento), `fotogramas.csv` (movimiento por fotograma), láminas y `transcripcion.json` (con `voz <id> tools/reelNN/voz.tsv` en Reels propios).

## Procedimiento
1. Lanza el análisis (si ya existe en `intel/INDEX.csv`, no lo repitas) y **mira todas las láminas de detalle**; márcalas con `visto`.
2. **Ritmo:** anota planos, duración media, el más largo y el más corto, y cortes cada 10 s. Dibuja la curva: ¿acelera hacia el giro y respira en la idea clave, o es plana?
3. **Planos largos:** todo plano de más de 4 s necesita cambio interno (texto que entra, animación) cada 1,5 s como mucho. Compruébalo en las láminas.
4. **Planos relámpago:** todo plano de menos de 0,4 s es un destello; solo vale si es intencionado y no lleva texto que haya que leer.
5. **Cortes y transiciones:** cada corte coincide con inicio de frase, palabra de impacto o golpe de música (tolerancia ±0,15 s contra `transcripcion.json` y las «subidas bruscas» del audio). Corte que no coincide con nada, se justifica o se mueve.
6. **Sincronía voz–texto:** el texto aparece con la palabra que subraya (±0,2 s) y permanece lo suficiente: mínimo 0,3 s por palabra y nunca menos de 0,8 s.
7. **Continuidad:** dirección de mirada y de movimiento coherentes entre planos; mismo tratamiento de color en fotos consecutivas.
8. **Final:** el vídeo termina como mucho 0,8 s después de la última palabra.
9. Escribe cada hallazgo con marca de tiempo, lámina y corrección.

## Ejemplo medido (u04)
9 planos, media 2,81 s, 3,2 cortes cada 10 s. Plano de 0,23 s en 00:22,03–00:22,27 (destello con texto «28.11»). La voz acaba en 00:23,70 y el vídeo en 00:25,30: 1,6 s de cartela fija sin voz.

## Control
¿He mirado todas las láminas del modo usado? ¿Cada hallazgo tiene segundo y lámina? ¿He separado lo medido de lo que opino?
