from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
# Duke Chapel: el recorte con rembg (isnet-general-use + alpha matting) se come la base del edificio (piedra oscura contra árboles);
# va en marco, recortada a la torre.
Image.open('photos/chapel.jpg').convert('RGB').crop((430,0,1130,1000)).save('photos/chapel_crop.jpg',quality=92)
Image.open('photos/sign.jpg').convert('RGB').crop((200,18,655,420)).save('photos/sign_crop.jpg',quality=92)
Image.open('photos/gym.jpg').convert('RGB').crop((0,30,787,372)).save('photos/gym_crop.jpg',quality=92)
grade('photos/chapel_crop.jpg','img/chapel_g.jpg')
# r2 (Marta B, 27/11): la estación recortada al autobús y el andén (sin el cartel «COLORED WAITING ROOM», que entra por primera vez en «La ley lo prohíbe», ni caras)
Image.open('photos/bus.jpg').convert('RGB').crop((412,250,1000,690)).save('photos/bus_crop.jpg',quality=92)
grade('photos/bus_crop.jpg','img/bus_g.jpg',keep_blue=False)
grade('photos/sign_crop.jpg','img/sign_g.jpg',keep_blue=False)
grade('photos/gym_crop.jpg','img/gym_g.jpg')
