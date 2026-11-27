"""Preparación de fotos (v7-esquinas-tuchel-mainz). python3 cut.py
- Thomas Tuchel coach Mainz05 at away match in Leverkusen 2014.jpg (Schnederpelz, CC BY-SA 3.0): se reutiliza img/tuchel_g.png
  de tools/reel_v7/v7-pantalla-nagelsmann-2017 (cut.py de esa pieza: escudo y patrocinador tapados, rembg, B/N con el azul).
- BruchwegPlatz2.jpg (AVespucci, CC BY-SA 3.0), bajada en el sandbox de Higgsfield y traída a 1600 px → photos/bruchweg.jpg:
  recorte apaisado con el banderín de córner y graduado (B/N con el azul)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
b = Image.open('photos/bruchweg.jpg').convert('RGB').crop((0, 380, 1600, 1200)).resize((1100, 564), Image.LANCZOS)
b.save('photos/bruchweg_crop.jpg', quality=92); grade('photos/bruchweg_crop.jpg', 'img/bruchweg_g.jpg', keep_blue=True)
