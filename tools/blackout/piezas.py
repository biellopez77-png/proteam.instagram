"""Posts y Stories de Blackout Friday a partir de las fotos 3D. Tipografía sobria, sin brillos de neón.
  python3 piezas.py post-silbato | story-cuenta 15 | post-pizarra"""
import sys, os
from PIL import Image, ImageDraw, ImageFont
F = '/home/claude/tts/'; D = os.path.dirname(os.path.abspath(__file__))
def font(n, s): return ImageFont.truetype(F + n + '.ttf', s)
B, S, M, I = 'manrope-latin-800-normal', 'manrope-latin-500-normal', 'ibm-plex-mono-latin-500-normal', 'instrument-serif-latin-400-italic'
MARK = Image.open(os.path.join(D, '..', 'proteam-mark.webp')).convert('RGBA')
def mark(im, x, y, size=52, txt=True, col=(244, 246, 250)):
    m = MARK.resize((size, size)); im.paste(m, (x, y), m)
    if txt: ImageDraw.Draw(im).text((x + size + 14, y + size * .08), 'ProTeam', font=font(B, int(size * .7)), fill=col)
def shade(im, top=0, bottom=0):  # degradado suave para que lea el texto, como en una foto editada
    import numpy as np
    a = np.asarray(im).astype(float); h = a.shape[0]; y = np.arange(h)[:, None, None] / h
    k = 1 - top * np.clip(1 - y / .35, 0, 1) ** 1.5 - bottom * np.clip((y - .55) / .45, 0, 1) ** 1.5
    return Image.fromarray((a * k).clip(0, 255).astype('uint8'))
def save(im, name): p = os.path.join(D, 'out', 'piezas', name); os.makedirs(os.path.dirname(p), exist_ok=True); im.convert('RGB').save(p, quality=94); print(p)

def post_silbato():
    im = shade(Image.open(os.path.join(D, 'out/foto/silbato.png')).convert('RGB'), top=.55, bottom=.5); d = ImageDraw.Draw(im)
    d.text((80, 84), 'Blackout Friday', font=font(M, 28), fill=(170, 176, 188))
    d.text((80, 130), 'El 27 se apaga la luz.', font=font(B, 76), fill=(244, 246, 250))
    d.text((80, 218), 'Que no se apague tu equipo.', font=font(I, 66), fill=(200, 206, 216))
    d.text((80, 1218), '6 meses gratis para tu primer equipo · hasta el 27 nov', font=font(S, 30), fill=(214, 218, 226))
    mark(im, 868, 1196, 40)
    save(im, 'post-silbato.jpg')

def post_pizarra():
    im = shade(Image.open(os.path.join(D, 'out/foto/pizarra.png')).convert('RGB'), top=.6, bottom=.45); d = ImageDraw.Draw(im)
    d.text((80, 84), 'Blackout Friday', font=font(M, 28), fill=(170, 176, 188))
    d.text((80, 130), 'La jugada, en la pizarra.', font=font(B, 72), fill=(244, 246, 250))
    d.text((80, 214), 'Todo lo demás, en ProTeam.', font=font(I, 64), fill=(200, 206, 216))
    d.text((80, 1218), '6 meses gratis para tu primer equipo · hasta el 27 nov', font=font(S, 30), fill=(214, 218, 226))
    mark(im, 868, 1196, 40)
    save(im, 'post-pizarra.jpg')

def story_cuenta(n):
    im = shade(Image.open(os.path.join(D, f'out/foto/marcador-story-{n}.png')).convert('RGB'), top=.3, bottom=.65); d = ImageDraw.Draw(im)
    txt = {'15': 'Cuenta atrás.', '14': 'La jugada, en la pizarra.', '13': 'Apaga los Excels.', '12': 'Un silbato no lleva un equipo.',
           '11': '¿Quién viene el sábado?', '10': 'Todo en un sitio.', '9': 'El partido, en directo.', '8': '¿Cuándo se rompió?',
           '7': 'La semana, planificada.', '6': 'Minutos × esfuerzo.', '5': 'Recupera tu domingo.', '4': 'Casi una temporada.',
           '3': 'Tres días.', '2': 'Sin tarjeta.', '1': 'Mañana se va la luz.', '0': 'Hoy se va la luz.'}.get(n, 'Cuenta atrás.')
    d.text((80, 1440), txt, font=font(B, 76), fill=(244, 246, 250))
    d.text((80, 1534), '6 meses gratis para tu primer equipo', font=font(I, 58), fill=(205, 210, 220))
    d.text((80, 1616), 'hasta el viernes 27 · 23:59', font=font(M, 30), fill=(150, 156, 168))
    mark(im, 80, 1760, 48)
    save(im, f'story-cuenta-{n}.jpg')

def post_meses():
    im = shade(Image.open(os.path.join(D, 'out/foto/marcador-post-6.png')).convert('RGB'), top=.5, bottom=.6); d = ImageDraw.Draw(im)
    d.text((80, 84), 'Blackout Friday', font=font(M, 28), fill=(170, 176, 188))
    d.text((80, 1000), 'Seis meses.', font=font(B, 84), fill=(244, 246, 250))
    d.text((80, 1094), 'Casi una temporada entera.', font=font(I, 62), fill=(200, 206, 216))
    d.text((80, 1218), 'Gratis para tu primer equipo · hasta el 27 nov', font=font(S, 30), fill=(214, 218, 226))
    mark(im, 868, 1196, 40); save(im, 'post-meses.jpg')

def post_ultimo():
    im = shade(Image.open(os.path.join(D, 'out/foto/marcador-post-hoy.png')).convert('RGB'), top=.5, bottom=.6); d = ImageDraw.Draw(im)
    d.text((80, 84), 'Último día · Blackout Friday', font=font(M, 28), fill=(255, 150, 160))
    d.text((80, 1000), 'Hoy se va la luz.', font=font(B, 84), fill=(244, 246, 250))
    d.text((80, 1094), '6 meses gratis, hasta las 23:59.', font=font(I, 62), fill=(255, 196, 202))
    d.text((80, 1218), 'Crea tu primer equipo en pro-team.app', font=font(S, 30), fill=(214, 218, 226))
    mark(im, 868, 1196, 40); save(im, 'post-ultimo-dia.jpg')

if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'post-silbato': post_silbato()
    elif c == 'post-pizarra': post_pizarra()
    elif c == 'story-cuenta': story_cuenta(sys.argv[2])
    elif c == 'post-meses': post_meses()
    elif c == 'post-ultimo': post_ultimo()
