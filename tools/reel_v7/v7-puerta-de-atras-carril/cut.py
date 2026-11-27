from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
# 1 · Jadwin Gymnasium (exterior): fuera el cielo y el suelo, recorte del edificio
# (rembg con isnet probado: se queda con la farola, no con el edificio; la foto va en marco, sin recortar el fondo)
Image.open('photos/jadwin.jpg').convert('RGB').crop((0,180,1600,1020)).save('photos/jadwin_crop.jpg',quality=92)
# 2 · pancarta de Pete Carril bajo el techo del Jadwin (con la bandera al lado)
Image.open('photos/banner.jpg').convert('RGB').crop((150,250,730,780)).save('photos/banner_crop.jpg',quality=92)
# 3 · Princeton en el Jadwin, 1988
Image.open('photos/game1988.jpg').convert('RGB').crop((180,300,1600,1056)).save('photos/game_crop.jpg',quality=92)
grade('photos/jadwin_crop.jpg','img/jadwin_g.jpg',keep_blue=False)  # el azul aquí eran manchas del cristal
grade('photos/banner_crop.jpg','img/banner_g.jpg')
grade('photos/game_crop.jpg','img/game_g.jpg')
