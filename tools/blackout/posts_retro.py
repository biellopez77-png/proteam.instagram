"""Posts de feed de la identidad retro: tele 3D sobre gris + texto azul justificado (estilo póster)."""
import os
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)); F = '/home/claude/tts/'
BLUE = (31, 60, 255)
def just(d, text, x, y, w, font, lh):
    words = text.split(); lines = []; cur = []
    for wd in words:
        if d.textlength(' '.join(cur + [wd]), font=font) > w and cur: lines.append(cur); cur = [wd]
        else: cur.append(wd)
    lines.append(cur)
    for i, ln in enumerate(lines):
        if i < len(lines) - 1 and len(ln) > 1:
            tw = sum(d.textlength(t, font=font) for t in ln); gap = (w - tw) / (len(ln) - 1); xx = x
            for t in ln: d.text((xx, y), t, font=font, fill=BLUE); xx += d.textlength(t, font=font) + gap
        else: d.text((x, y), ' '.join(ln), font=font, fill=BLUE)
        y += lh
def post(i, texto, out):
    im = Image.open(os.path.join(D, f'out/tele/tv{i}.png')).convert('RGB'); d = ImageDraw.Draw(im)
    mk = Image.open(os.path.join(D, '..', 'proteam-mark.webp')).convert('RGBA').resize((76, 76)); im.paste(mk, ((1080 - 76) // 2, 70), mk)
    just(d, texto.upper(), 150, 1000, 780, ImageFont.truetype(F + 'inter-tight-latin-800-normal.ttf', 34), 44)
    f = ImageFont.truetype(F + 'inter-tight-latin-900-normal.ttf', 44); s = '@app.proteam'
    d.text(((1080 - d.textlength(s, font=f)) / 2, 1250), s, font=f, fill=BLUE)
    im.save(out, quality=94); print(out)
if __name__ == '__main__':
    os.makedirs(os.path.join(D, 'out/retro'), exist_ok=True)
    T = {1: 'Excels que nadie abre, libretas que no vieron el partido y 47 audios para saber quién viene. Así se lleva un equipo. Hasta ahora.',
         2: 'Planifica la semana, convoca, registra el partido en directo y controla la carga. En una sola app. Seis meses gratis para tu primer equipo.',
         3: 'Para tu primer equipo. Sin tarjeta. Fútbol, baloncesto y balonmano. Solo hasta el 27 de noviembre a las 23:59.',
         4: 'Último día: seis meses gratis para tu primer equipo. A las 23:59 se corta la señal y vuelven a ser tres.'}
    for i, t in T.items(): post(i, t, os.path.join(D, f'out/retro/post-{i}.jpg'))
