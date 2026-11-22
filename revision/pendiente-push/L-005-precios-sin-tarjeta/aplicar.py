#!/usr/bin/env python3
"""L-005 (1 archivo: src/routes/pricing.tsx). Uso: python3 aplicar.py <ruta proteamapp>
Arreglo de texto → main.

La descripción de /pricing (la que sale en Google y al compartir el enlace) dice
«Empieza con 3 meses gratis, sin tarjeta.», y el título «…con 3 meses gratis». Desde el
17/11 la prueba pide tarjeta (`card_required`, pantalla «Añade tu tarjeta para empezar la
prueba») y desde el 28 la prueba es de 1 mes. Se quita la promesa: el título y la
descripción quedan solo con el precio, que es lo que es esta página.
"""
import sys, pathlib
f = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "src/routes/pricing.tsx"
s = f.read_text()
for old, new in [
    ('title: "Precios de ProTeam: 9,90 €/mes por equipo con 3 meses gratis | ProTeam",',
     'title: "Precios de ProTeam: 9,90 €/mes por equipo | ProTeam",'),
    (' y equipos adicionales a 7,50 € al mes. Empieza con 3 meses gratis, sin tarjeta.",',
     ' y equipos adicionales a 7,50 € al mes.",'),
]:
    assert s.count(old) == 1, f"no encontrado: {old[:60]}"
    s = s.replace(old, new)
f.write_text(s)
print("L-005 aplicado en", f)
