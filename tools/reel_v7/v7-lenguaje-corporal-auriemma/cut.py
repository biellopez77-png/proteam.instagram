"""Preparación de fotos (v7-lenguaje-corporal-auriemma). python3 cut.py
Las fotos se bajan en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor) y llegan por image_paths:
- Geno-Auriemma-UConn-vs-Texas-3-23-08.jpg → photos/geno.jpg (782×988, original)
- Breanna_Stewart_2015.jpg → photos/stewart.jpg (335×562, original)
- Harry_A._Gampel_Pavilion_…DSC09954.JPG → photos/gampel.jpg (1200 px)
- UConn_Huskies_at_Minnesota_…070_(53345964171).jpg → photos/bench.jpg (1400 px)
Se probó rembg (u2net_human_seg): el recorte arrastraba caras del público detrás de Auriemma y abría un hueco en el trofeo
de Stewart. No queda limpio → las cuatro fotos van enmarcadas (recortadas y graduadas, B/N con el azul)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
Image.open('photos/geno.jpg').crop((0, 0, 782, 860)).save('photos/geno_crop.jpg', quality=94)
grade('photos/geno_crop.jpg', 'img/geno_g.jpg', keep_blue=True)
grade('photos/stewart.jpg', 'img/stewart_g.jpg', keep_blue=True)
grade('photos/gampel.jpg', 'img/gampel_g.jpg', keep_blue=True)
Image.open('photos/bench.jpg').crop((0, 220, 1400, 760)).save('photos/bench_crop.jpg', quality=94)
grade('photos/bench_crop.jpg', 'img/bench_g.jpg', keep_blue=True)
