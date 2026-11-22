# Genera las láminas del carrusel y las Stories de T01-3-r3 «Primera posesión» (Clara, 22/11)
import os
D = os.path.dirname(os.path.abspath(__file__))
R = '../../../../'  # raíz del repo
CSS = f"""
@font-face{{font-family:M;font-weight:500;src:url({R}tools/fonts/manrope-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({R}tools/fonts/manrope-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:800;src:url({R}tools/fonts/manrope-latin-800-normal.woff2)}}
@font-face{{font-family:S;font-style:italic;src:url({R}tools/fonts/instrument-serif-latin-400-italic.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:#fbfaf7}}
.pg{{position:relative;width:1080px;height:1440px;background:#fbfaf7;color:#121212;font-family:M;overflow:hidden}}
.st{{height:1920px}}
.k{{position:absolute;left:90px;top:150px;font-weight:700;font-size:26px;letter-spacing:.18em;color:#121212;opacity:.55;text-transform:uppercase}}
.n{{position:absolute;right:90px;top:150px;font-weight:700;font-size:26px;letter-spacing:.12em;opacity:.35}}
h1{{font-weight:800;font-size:84px;line-height:1.04;letter-spacing:-.025em}}
h2{{font-weight:800;font-size:70px;line-height:1.08;letter-spacing:-.02em}}
em{{font-family:S;font-style:italic;font-weight:400;color:#2f6bff;letter-spacing:0;font-size:1.12em}}
.sub{{font-weight:500;font-size:36px;line-height:1.35;color:#121212;opacity:.6;margin-top:28px}}
.frame{{position:absolute;background:#fff;padding:18px;box-shadow:0 2px 4px rgba(0,0,0,.06),0 30px 70px rgba(30,25,15,.16)}}
.frame img{{display:block;width:100%;height:100%;object-fit:cover}}
.tag{{position:absolute;font-weight:700;font-size:22px;letter-spacing:.16em;color:#121212;opacity:.45}}
.foot{{position:absolute;left:90px;bottom:150px;font-weight:700;font-size:24px;letter-spacing:.16em;opacity:.4}}
svg{{position:absolute;overflow:visible}}
"""
PENCIL = """<defs><filter id="pen" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4" result="t"/>
<feDisplacementMap in="SourceGraphic" in2="t" scale="3.2"/></filter></defs>"""

def page(body, story=False):
    cls = 'pg st' if story else 'pg'
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="{cls}">{body}</div></body></html>'

INK = '#121212'; BLUE = '#2f6bff'; RED = '#d23a2a'

def xmark(x, y, col=RED, s=22):
    return f'<path d="M{x-s} {y-s} L{x+s} {y+s} M{x+s} {y-s} L{x-s} {y+s}" stroke="{col}" stroke-width="8" stroke-linecap="round"/>'

def omark(x, y, col=INK, r=22, num=None):
    t = f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{col}" stroke-width="7"/>'
    if num:
        t += f'<text x="{x}" y="{y+r+44}" font-family="M" font-weight="800" font-size="34" fill="{col}" text-anchor="middle">{num}</text>'
    return t

def court(x, y, w=720, h=540, trap=True, help_=False, pas=False, ring=True):
    """Media pista dibujada a lápiz, aro abajo. Trampa en la esquina inferior derecha."""
    bx, by = w/2, h-62  # aro
    s = f'<svg style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{PENCIL}<g filter="url(#pen)" fill="none" stroke-linecap="round" stroke-linejoin="round">'
    s += f'<rect x="4" y="4" width="{w-8}" height="{h-8}" stroke="{INK}" stroke-width="7"/>'
    s += f'<rect x="{bx-120}" y="{h-300}" width="240" height="296" stroke="{INK}" stroke-width="4" opacity=".6"/>'
    s += f'<path d="M{bx-90} {h-300} A90 90 0 0 1 {bx+90} {h-300}" stroke="{INK}" stroke-width="4" opacity=".6"/>'
    s += f'<path d="M60 {h-4} L60 {h-150} A {bx-60} {bx-60} 0 0 1 {w-60} {h-150} L{w-60} {h-4}" stroke="{INK}" stroke-width="4" opacity=".6"/>'
    s += f'<circle cx="{bx}" cy="{by}" r="16" stroke="{INK}" stroke-width="4" opacity=".7"/><path d="M{bx-40} {by+22} L{bx+40} {by+22}" stroke="{INK}" stroke-width="5" opacity=".7"/>'
    cx, cy = w-48, h-56  # balón en la esquina
    if trap:
        s += omark(cx, cy)
        s += xmark(cx-82, cy-8) + xmark(cx-14, cy-96)
        if ring:
            s += f'<circle cx="{cx-40}" cy="{cy-44}" r="104" stroke="{RED}" stroke-width="5" opacity=".85"/>'
    hx0, hy0 = bx-150, h-330   # compañero que ayuda
    hx1, hy1 = w-170, h-250   # adónde llega
    if help_:
        s += omark(hx0, hy0, BLUE if not pas else INK)
        s += f'<path d="M{hx0+22} {hy0+18} Q {(hx0+hx1)/2} {hy0-60} {hx1-18} {hy1-22}" stroke="{BLUE}" stroke-width="6" stroke-dasharray="4 18"/>'
        s += f'<path d="M{hx1-40} {hy1-28} L{hx1-16} {hy1-20} L{hx1-30} {hy1-44}" stroke="{BLUE}" stroke-width="6"/>'
    if pas:
        s += omark(hx1, hy1, BLUE)
        s += f'<path d="M{cx-18} {cy-24} L{hx1+20} {hy1+26}" stroke="{BLUE}" stroke-width="9"/>'
        s += f'<path d="M{hx1+18} {hy1+62} L{hx1+20} {hy1+26} L{hx1+56} {hy1+30}" stroke="{BLUE}" stroke-width="9"/>'
    s += '</g></svg>'
    return s

def clock(x, y, txt='24', w=300, h=200, fs=140, bg=INK, fg='#fbfaf7'):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border-radius:28px;color:{fg};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:{fs}px;letter-spacing:-.02em;box-shadow:0 24px 60px rgba(30,25,15,.16)">{txt}</div>'

def underline(x, y, w):
    return f'<svg style="left:{x}px;top:{y}px" width="{w}" height="30" viewBox="0 0 {w} 30">{PENCIL}<path filter="url(#pen)" d="M4 18 C {w*.3} 8, {w*.7} 26, {w-4} 12" stroke="{BLUE}" stroke-width="8" fill="none" stroke-linecap="round"/></svg>'

N = 7
txt = lambda h, sub='': f'<div style="position:absolute;left:90px;top:1000px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
slides = {}

# 1 · portada
slides['c1'] = page(f'''
<div class="k">Baloncesto · descanso</div>
{clock(90, 280, '24', w=220, h=160, fs=110)}
{court(330, 420, w=600, h=450)}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>El tercer cuarto empieza <em>en el vestuario.</em></h1></div>
<div class="foot" style="bottom:110px">DESLIZA →</div>''')

# 2 · problema
circ = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:110px;height:110px;border:6px solid rgba(18,18,18,.55);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:46px;color:rgba(18,18,18,.6)">{n}</div>' for n, (x, y) in enumerate([(640, 300), (800, 380), (660, 470), (840, 560), (690, 650)], 1))
slides['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
{clock(120, 360, '15:00', w=440, h=220, fs=120, bg='#2b2620', fg='#f3e7d3')}
<div class="tag" style="left:124px;top:610px">FIBA · ART. 8.4 · 15′ DE DESCANSO</div>
{circ}
{txt('Quince minutos no dan para <em>cinco jugadas nuevas.</em>', 'Y la trampa de la esquina se queda sin respuesta.')}''')

# 3 · paso 1: elegir
items = [('Jugadas nuevas', True), ('Hoja de estadística', True), ('La trampa de la esquina', False)]
nb = ''
for i, (t, cross) in enumerate(items):
    y = 120 + i*130
    op = '.35' if cross else '1'
    nb += f'<div style="position:absolute;left:90px;top:{y}px;font-weight:700;font-size:44px;opacity:{op}">{t}</div>'
    if cross:
        nb += f'<svg style="left:80px;top:{y+18}px" width="{len(t)*25}" height="30">{PENCIL}<path filter="url(#pen)" d="M0 14 L{len(t)*24} 10" stroke="{INK}" stroke-width="5" opacity=".5" stroke-linecap="round"/></svg>'
nb += f'<svg style="left:50px;top:350px" width="640" height="140">{PENCIL}<ellipse filter="url(#pen)" cx="320" cy="62" rx="300" ry="56" fill="none" stroke="{BLUE}" stroke-width="7"/></svg>'
lines = ''.join(f'<div style="position:absolute;left:0;right:0;top:{90+k*130+80}px;border-top:2px solid rgba(47,107,255,.12)"></div>' for k in range(4))
slides['c3'] = page(f'''
<div class="k">Paso 1</div>{num(3)}
<div class="frame" style="left:190px;top:280px;width:700px;height:600px;transform:rotate(-1.5deg);padding:0;background:#fffdf8">{lines}{nb}</div>
{txt('No inventes. <em>Elige una cosa.</em>', 'La que os ha costado el balón.')}''')

# 4 · paso 2: quién ayuda
slides['c4'] = page(f'''
<div class="k">Paso 2</div>{num(4)}
{court(180, 300, help_=True)}
<div class="tag" style="left:180px;top:860px">EJEMPLO</div>
{txt('Decide <em>quién ayuda.</em>', 'Un compañero que se acerca al balón encerrado.')}''')

# 5 · paso 3: adónde va el balón
slides['c5'] = page(f'''
<div class="k">Paso 3</div>{num(5)}
{court(180, 300, help_=True, pas=True, ring=False)}
<div class="tag" style="left:180px;top:860px">EJEMPLO</div>
{txt('Decide <em>adónde va el balón.</em>', 'Fuera de la esquina. Es la respuesta a la trampa.')}''')

# 6 · paso 4: primera posesión
slides['c6'] = page(f'''
<div class="k">Paso 4</div>{num(6)}
{clock(120, 330, '24', w=240, h=170, fs=118)}
{court(390, 420, w=540, h=405, help_=True, pas=True, ring=False)}
{txt('Primera posesión, <em>decidida.</em>', 'Sales del vestuario con una sola consigna.')}''')

# 7 · resumen
rows = [('1', 'Elige una cosa, no cinco.'), ('2', 'Quién ayuda.'), ('3', 'Adónde va el balón.'), ('4', 'Primera posesión, decidida.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:34px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px">{a}</span><span style="font-weight:700;font-size:46px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
slides['c7'] = page(f'''
<div class="k">Resumen · descanso</div>{num(7)}
{clock(420, 270, '24', w=240, h=160, fs=110)}
<div style="position:absolute;left:90px;top:560px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:1060px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>''')

# Stories
slides['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta</div>
{clock(390, 380, '15:00', w=300, h=150, fs=82, bg='#2b2620', fg='#f3e7d3')}
{court(240, 600, w=600, h=450)}
<div style="position:absolute;left:90px;top:1110px;width:900px"><h1 style="font-size:84px">¿Qué es lo primero que dices <em>en el descanso?</em></h1></div>
<div style="position:absolute;left:140px;top:1470px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
slides['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta · baloncesto</div>
{court(240, 380, w=600, h=450, help_=True, pas=True, ring=False)}
<div style="position:absolute;left:90px;top:920px;width:900px"><h1 style="font-size:84px">En el descanso, ¿qué <em>preparas?</em></h1></div>
{opt('Jugadas nuevas', 1270)}{opt('Una respuesta a lo que pasa', 1450)}
<div class="tag" style="left:140px;top:1640px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in slides.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(slides))
