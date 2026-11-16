# SKILL · Social Content Visual Audit (04 Carousel Lab; la usa 05 con carruseles y Stories)
**Para qué:** revisar composición, legibilidad, jerarquía, consistencia y calidad gráfica de cada imagen **mirándola**.

## Herramientas
Read sobre cada JPG final (`feed/`, `stories/`); miniatura con PIL; lámina de conjunto:
```bash
python3 - <<'PY'
from PIL import Image; import glob,sys
fs=sorted(glob.glob('feed/c10-*.jpg')); ims=[Image.open(f).resize((360,450)) for f in fs]
s=Image.new('RGB',(360*len(ims),450)); [s.paste(im,(360*i,0)) for i,im in enumerate(ims)]; s.save('/tmp/c10-conjunto.jpg')
PY
```

## Lista de comprobación (por imagen; sí/no y nota)
1. **Legibilidad:** todo texto necesario se lee en la miniatura de 360 px de ancho.
2. **Jerarquía:** se sabe qué leer primero, segundo y tercero.
3. **Márgenes:** nada a menos de 90 px del borde; en Stories, texto entre y≈260 y y≈1600.
4. **Contraste:** texto sobre foto con velo suficiente; nunca texto sobre zona con detalle.
5. **Tipografía:** solo Manrope e Instrument Serif itálica azul; una palabra en serif por pantalla.
6. **Color:** tinta/negro, papel, azul. El azul marca una sola cosa.
7. **Ortografía y tipografía fina:** tildes, signos de apertura (¿ ¡), comillas « », sin líneas viudas de una palabra, sin cortes raros.
8. **Imagen:** foto nítida, sujeto no cortado por la cara, reconocible si es persona; sin marcas de agua.
9. **Producto:** captura real y legible; nada inventado.
10. **Sin adornos:** ni iconos decorativos, ni logos, ni plantillas.

## Lista de conjunto (carrusel o secuencia)
- Coherencia: misma rejilla y mismos tamaños base en todas.
- Variedad: no hay tres composiciones idénticas seguidas.
- Ritmo: alternan pantallas densas y de respiro.
- Continuidad: la portada y el cierre se reconocen como la misma pieza.
- Diferencia: la lámina de conjunto no se confunde con la del carrusel anterior.

## Resultado
Tabla por imagen con fallos y corrección concreta («c10-3: cuerpo a 30 px, subir a 36; última línea viuda»). Un «no» en 1, 3, 7 o 9 bloquea la entrega.

## Control
¿He abierto cada JPG final (no el HTML)? ¿He mirado la lámina de conjunto y la miniatura?
