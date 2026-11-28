"""Gradación de las fotos de v7-cintas-pele-coerver (../bielsa/grade.py). Las tres son B/N de archivo y van enmarcadas
(el recorte con rembg no queda limpio: Coerver va a hombros entre jugadores; Pelé, con el defensa pegado)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
grade('photos/coerver.jpg', 'img/coerver_g.jpg', keep_blue=False)   # 1 · Coerver con la Copa de la UEFA (Rob Mieremet / Anefo, 29/5/1974), encuadre en Coerver y la copa
grade('photos/pele.jpg', 'img/pele_g.jpg', keep_blue=False)         # 2 · Pelé regatea (Malmö, 8/5/1960; AFP/Scanpix)
grade('photos/libro.jpg', 'img/libro_g.jpg', keep_blue=False)       # 3 · presentación del libro (Rob Bogaerts / Anefo, 8/8/1983)
