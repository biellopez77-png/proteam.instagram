# SKILL · Media Asset Management (03 Resource Bank)
**Para qué:** que cualquier recurso se encuentre en segundos y nunca haya dos iguales.

## Herramientas
`banco/` (fotos, vídeos, proteam), `banco/INVENTARIO.csv`, `banco/INDICE.md`, `sha256sum`, `python3` (csv), `ffprobe`, PIL.

## Procedimiento
1. **Entrada:** todo archivo nuevo pasa por: mirar (Read) → medir (dimensiones; vídeo con `ffprobe`) → huella `sha256sum` → comprobar que la huella no existe ya → nombrar → fila de inventario.
2. **Nombre:** `PROTEAM_CATEGORIA_TEMA_TIPO_NNN.ext`. Categorías: ENTRENADOR, STAFF, JUGADOR, EQUIPO, INSTALACION, OBJETO, PRODUCTO, PLANIFICACION, ANALISIS, ENTRENAMIENTO. Tipos: FOTO, VIDEO, CAPTURA, GRABACION.
3. **Fila** (columnas actuales, no se quitan): nombre, categoria, tema, descripcion, deporte, plano, orientacion, calidad, uso, procedencia, autor, licencia, uso_comercial, enlace, ubicacion, estado. Datos que no caben (resolución exacta, duración, acción, etiquetas, sha256) van en `descripcion` como `clave=valor;` hasta que se amplíe el CSV en una sola pasada para todo el banco.
4. **Estado:** `disponible`, `usada en <id>[, <id>…]`, `pendiente` (no descargada o licencia sin comprobar), `retirada` (motivo).
5. **Duplicados y casi duplicados:** misma huella = se borra el nuevo. Misma escena con otro encuadre = se conserva la mejor como principal y la otra solo si aporta un plano distinto (se anota «alternativa de <nombre>»).
6. **Uso:** al cerrarse una pieza, se actualiza `estado` con su id. Una foto usada en los últimos cinco Reels no se propone de nuevo.
7. **Índice:** `INDICE.md` con recuento por categoría y deporte, y la lista de **huecos** (qué no tenemos y para qué tipo de idea haría falta).
8. **Auditoría mensual:** archivos sin fila, filas sin archivo, licencias «sin comprobar», categorías con menos de 5 recursos.

## Comprobación rápida
```bash
python3 - <<'PY'
import csv,os
rows=list(csv.DictReader(open('banco/INVENTARIO.csv',encoding='utf-8')))
names={r['nombre'] for r in rows}
files={f for d,_,fs in os.walk('banco') for f in fs if f.lower().endswith(('.jpg','.jpeg','.png','.mp4','.webm'))}
print('sin fila:',sorted(files-names)[:20]); print('sin archivo:',sorted(n for n in names-files)[:20])
PY
```

## Control
¿Cada archivo tiene fila y cada fila archivo (o estado `pendiente`)? ¿Algún dato inventado? ¿Índice actualizado?
