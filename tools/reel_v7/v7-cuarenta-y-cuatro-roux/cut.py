# v7-cuarenta-y-cuatro-roux · fotos: todas enmarcadas (sin rembg: dos son pequeñas y el estadio es un plano general)
from PIL import Image
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
Image.open('photos/stadium.jpg').convert('RGB').crop((0, 250, 1400, 1050)).save('photos/stadium_crop.jpg', quality=92)   # sin el cielo
Image.open('photos/roux2008.jpg').convert('RGB').crop((0, 0, 927, 1100)).save('photos/roux2008_crop.jpg', quality=92)  # cabeza y hombros
grade('photos/stadium_crop.jpg', 'img/stadium_g.jpg')
grade('photos/roux2003.jpg', 'img/roux2003_g.jpg')
grade('photos/cantona.jpg', 'img/cantona_g.jpg', keep_blue=False)
grade('photos/roux2008_crop.jpg', 'img/roux2008_g.jpg')
