"""Imagen de la pantalla azul (4:3) para la tele 3D de los posts.  python3 pantalla.py "LÍNEA 1|LÍNEA 2" CH out.png"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from crt import crt
F = '/home/claude/tts/'
def screen(lines, ch, out, W=1200, H=900):
    im = Image.new('RGB', (W, H), '#1f3cff'); d = ImageDraw.Draw(im)
    for r in range(0, 700, 6):  # degradado radial suave
        d.ellipse([W * .42 - r * 1.2, H * .4 - r, W * .42 + r * 1.2, H * .4 + r], outline=None)
    g = Image.new('L', (W, H), 0); gd = ImageDraw.Draw(g); gd.ellipse([-200, -250, W * .95, H * 1.05], fill=90); g = g.filter(ImageFilter.GaussianBlur(160))
    im = Image.composite(Image.new('RGB', (W, H), '#3a58ff'), im, g); d = ImageDraw.Draw(im)
    vt = ImageFont.truetype(F + 'vt323-latin-400-normal.ttf', 78); big = ImageFont.truetype(F + 'inter-tight-latin-900-normal.ttf', 10)
    d.text((70, 50), ch, font=vt, fill='#3dffa8')
    ls = lines.split('|'); size = 150
    while True:
        big = ImageFont.truetype(F + 'inter-tight-latin-900-normal.ttf', size)
        if max(d.textlength(l, font=big) for l in ls) < W - 180 and len(ls) * size * .92 < H - 300: break
        size -= 4
    glow = Image.new('RGB', (W, H), 'black'); gd = ImageDraw.Draw(glow)
    y = (H - len(ls) * size * .92) / 2 + 30
    for l in ls:
        gd.text((90, y), l, font=big, fill='#ffffff'); y += size * .92
    im = Image.fromarray(__import__('numpy').clip(__import__('numpy').asarray(im).astype(int) + __import__('numpy').asarray(glow.filter(ImageFilter.GaussianBlur(14))).astype(int) * .5, 0, 255).astype('uint8'))
    d = ImageDraw.Draw(im); y = (H - len(ls) * size * .92) / 2 + 30
    for l in ls: d.text((90, y), l, font=big, fill='#f4f6ff'); y += size * .92
    crt(im, .7, 1.3, 3, curve=.0).save(out)
if __name__ == '__main__': screen(sys.argv[1], sys.argv[2], sys.argv[3])
