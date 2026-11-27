"""Preparación de fotos v7-raqueta-wootten-1965 (enmarcadas; el recorte con rembg no queda limpio: la foto de 1967 lleva retoque de prensa alrededor de la figura)."""
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
Image.open('photos/alc.jpg').convert('RGB').crop((60,0,1200,1140)).save('photos/alc_crop.jpg',quality=92)
Image.open('photos/gym.jpg').convert('RGB').crop((0,120,1600,1067)).save('photos/gym_crop.jpg',quality=92)
Image.open('photos/cole.jpg').convert('RGB').crop((0,330,1600,1120)).save('photos/cole_crop.jpg',quality=92)  # sin los carteles de patrocinio del techo
grade('photos/alc_crop.jpg','img/alc_g.jpg',keep_blue=False)
grade('photos/gym_crop.jpg','img/gym_g.jpg',keep_blue=False)  # el azul de la pared sale a manchas con la máscara: B/N entero
grade('photos/cole_crop.jpg','img/cole_g.jpg')
