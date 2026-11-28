"""Recortes y gradación de las fotos de v7-salon-de-bingo-hurley (../bielsa/grade.py). Ver CREDITOS.md."""
from PIL import Image
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
# 1 · Bob hurley.jpg (Vault7424, CC BY-SA 3.0): foto pequeña (473×640) → enmarcada, recortada a Hurley
Image.open('photos/hurley.jpg').convert('RGB').crop((150, 70, 473, 520)).save('photos/hurley_crop.jpg', quality=94)
grade('photos/hurley_crop.jpg', 'img/hurley_g.jpg', keep_blue=False)
# 2 · White Eagle Hall.jpg (Macaddct1984, CC BY-SA 4.0): fachada de hoy, sin la acera ni los carteles de abajo
Image.open('photos/whiteeagle.jpg').convert('RGB').crop((90, 70, 1150, 905)).save('photos/whiteeagle_crop.jpg', quality=93)
grade('photos/whiteeagle_crop.jpg', 'img/whiteeagle_g.jpg', keep_blue=False)
# 3 · St. Anthony High School 2014 (Jaylen123456789, CC BY-SA 3.0)
Image.open('photos/stanthony.jpg').convert('RGB').crop((0, 0, 1300, 800)).save('photos/stanthony_crop.jpg', quality=93)
grade('photos/stanthony_crop.jpg', 'img/stanthony_g.jpg', keep_blue=False)
# 4 · Basketball Hall of Fame, Springfield MA (John Phelan, CC BY 3.0): la cúpula y la torre (B/N: el azul del cielo dejaba un borde)
Image.open('photos/halloffame.jpg').convert('RGB').crop((150, 0, 1400, 1050)).save('photos/halloffame_crop.jpg', quality=93)
grade("photos/halloffame_crop.jpg", "img/halloffame_g.jpg", keep_blue=False)
# 5 · Bingo card.jpg (Abbey Hendrickson, CC BY 2.0)
grade('photos/bingo.jpg', 'img/bingo_g.jpg', keep_blue=False)
