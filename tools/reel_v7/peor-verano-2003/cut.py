from rembg import remove, new_session
from PIL import Image
s=new_session('isnet-general-use')
im=Image.open('../../../banco/fotos/PROTEAM_EQUIPO_ENTRENAMIENTO_SELECCION_BALONCESTO_FOTO_001.jpg').convert('RGB')
# entrenador y dos jugadores en primer plano (centro)
c=im.crop((250,190,760,665)); c.save('photos/coach.jpg')
o=remove(c,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
o.save('photos/coach_cut.png')
