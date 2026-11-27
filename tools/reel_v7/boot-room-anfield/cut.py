from rembg import remove, new_session
from PIL import Image
s=new_session('isnet-general-use')
for n,box in [('shankly',(60,40,1013,1530)),('paisley',(290,300,720,1530))]:
    im=Image.open(f'photos/{n}.jpg').convert('RGB').crop(box)
    o=remove(im,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
    o=o.crop(o.getbbox()); o.save(f'photos/{n}_cut.png'); print(n,o.size)
