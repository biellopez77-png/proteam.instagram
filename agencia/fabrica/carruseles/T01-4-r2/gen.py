# Genera las láminas del carrusel y las Stories de T01-4-r2 «95 contra 37» (Clara, 22/11)
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


def pitch(x, y, w=720, h=520, crosses=0, side='L', zones=False, losses=None, faded=False, shots=False):
    """Medio campo dibujado a lápiz, portería propia abajo. Centros desde una banda; zonas de pérdida."""
    op = '.35' if faded else '1'
    s = f'<svg style="left:{x}px;top:{y}px;opacity:{op}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{PENCIL}<g filter="url(#pen)" fill="none" stroke-linecap="round" stroke-linejoin="round">'
    s += f'<rect x="4" y="4" width="{w-8}" height="{h-8}" stroke="{INK}" stroke-width="7"/>'
    cx = w/2
    s += f'<rect x="{cx-170}" y="{h-150}" width="340" height="146" stroke="{INK}" stroke-width="4" opacity=".6"/>'
    s += f'<rect x="{cx-70}" y="{h-56}" width="140" height="52" stroke="{INK}" stroke-width="4" opacity=".6"/>'
    s += f'<path d="M{cx-60} {h-150} A70 70 0 0 1 {cx+60} {h-150}" stroke="{INK}" stroke-width="4" opacity=".6"/>'
    s += f'<path d="M{cx-60} 4 A70 70 0 0 0 {cx+60} 4" stroke="{INK}" stroke-width="4" opacity=".6"/>'
    s += f'<path d="M{cx-40} {h-4} L{cx+40} {h-4}" stroke="{INK}" stroke-width="10"/>'
    if zones:
        for k in (1, 2):
            s += f'<path d="M{w*k/3} 8 L{w*k/3} {h-8}" stroke="{BLUE}" stroke-width="3" stroke-dasharray="6 14" opacity=".7"/>'
        s += f'<path d="M8 {h/2} L{w-8} {h/2}" stroke="{BLUE}" stroke-width="3" stroke-dasharray="6 14" opacity=".7"/>'
    for i in range(crosses):
        x0 = 30 if side == 'L' else w-30
        y0 = 120 + i*34
        x1 = cx + (-30 + i*14)
        y1 = h - 110 - (i % 2)*20
        col = INK
        s += f'<path d="M{x0} {y0} Q {(x0+x1)/2} {y0-40} {x1} {y1}" stroke="{col}" stroke-width="5" stroke-dasharray="3 14" opacity=".75"/>'
        s += f'<circle cx="{x1}" cy="{y1}" r="7" fill="{col}" stroke="none" opacity=".75"/>'
    if losses:
        for (lx, ly) in losses:
            s += xmark(lx, ly, RED, 16)
    if shots:
        s += omark(cx+150, h-240, INK, 20)
        s += f'<path d="M{cx+135} {h-220} L{cx+20} {h-30}" stroke="{INK}" stroke-width="5"/>'
    s += '</g></svg>'
    return s

def bignum(x, y, t, col, fs=300):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;font-weight:800;font-size:{fs}px;letter-spacing:-.05em;line-height:1;color:{col}">{t}</div>'

def sheet(x, y, w=760, h=600, izq=0, dcha=0, perd=0, rot=-1.5):
    tal = lambda n: ''.join(f'<span style="display:inline-block;width:10px;height:70px;background:{BLUE};border-radius:5px;margin-right:16px;transform:rotate({(-1)**k*3}deg)"></span>' for k in range(n))
    box = lambda lab, n, top, left, bw: f'<div style="position:absolute;left:{left}px;top:{top}px;width:{bw}px;height:170px;border:4px solid rgba(18,18,18,.7);border-radius:6px"><div style="position:absolute;left:18px;top:12px;font-weight:700;font-size:24px;letter-spacing:.12em;opacity:.55">{lab}</div><div style="position:absolute;left:22px;top:62px">{tal(n)}</div></div>'
    inner = f'<div style="position:absolute;left:50px;top:40px;font-weight:800;font-size:36px">Centros en contra</div>'
    inner += box('IZQ.', izq, 100, 50, (w-130)//2) + box('DCHA.', dcha, 100, 80+(w-130)//2, (w-130)//2)
    inner += f'<div style="position:absolute;left:50px;top:{320}px;font-weight:800;font-size:36px">Pérdidas por zona</div>'
    inner += box('ZONA', perd, 380, 50, w-100)
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);padding:0;background:#fffdf8">{inner}</div>'

N = 7
txt = lambda h, sub='', top=1000: f'<div style="position:absolute;left:90px;top:{top}px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
slides = {}

# 1 · portada
slides['c1'] = page(f'''
<div class="k">Fútbol · primer tiempo</div>
{bignum(110, 300, '95', BLUE)}
<svg style="left:500px;top:330px" width="80" height="260">{PENCIL}<path filter="url(#pen)" d="M60 10 L20 250" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></svg>
{bignum(600, 300, '37', RED)}
<div class="tag" style="left:116px;top:640px">TIROS</div><div class="tag" style="left:606px;top:640px">CENTROS</div>
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>Recuerdas los tiros. <em>Los centros, no.</em></h1></div>
<div class="foot" style="bottom:110px">DESLIZA →</div>''')

# 2 · problema
ficha = f'''<div class="frame" style="left:150px;top:270px;width:780px;height:520px;transform:rotate(1.2deg);padding:0;background:#fffdf8">
<div style="position:absolute;left:50px;top:40px;font-weight:700;font-size:24px;letter-spacing:.14em;opacity:.5">LAIRD Y WATERS · 2008 · IJPAS</div>
<div style="position:absolute;left:50px;top:84px;font-weight:500;font-size:28px;opacity:.6">8 entrenadores titulados · lo que recuerdan de un primer tiempo</div>
<div style="position:absolute;left:50px;top:170px;width:680px">
<div style="display:flex;justify-content:space-between;font-weight:800;font-size:58px;margin-bottom:34px"><span>Tiros</span><span style="color:{BLUE}">95 %</span></div>
<div style="display:flex;justify-content:space-between;font-weight:800;font-size:58px;margin-bottom:34px"><span>Centros</span><span style="color:{RED}">37,5 %</span></div>
<div style="display:flex;justify-content:space-between;font-weight:800;font-size:58px;opacity:.45"><span>Posesión</span><span>32,5 %</span></div></div></div>'''
slides['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
{ficha}
{txt('En el descanso corriges lo que recuerdas, <em>no lo que pasó.</em>', 'Y lo que te hace daño casi nunca es un tiro.')}''')

# 3 · paso 1
slides['c3'] = page(f'''
<div class="k">Paso 1</div>{num(3)}
{sheet(160, 280)}
{txt('Una hoja, <em>dos casillas.</em>', 'Centros en contra por banda. Pérdidas por zona.')}''')

# 4 · paso 2
slides['c4'] = page(f'''
<div class="k">Paso 2</div>{num(4)}
{pitch(180, 250, w=720, h=520, crosses=5, side='L')}
<div class="tag" style="left:180px;top:800px">EJEMPLO · CINCO CENTROS POR LA IZQUIERDA</div>
{txt('Centros en contra, <em>por banda.</em>', 'Izquierda o derecha. Una raya cada vez.')}''')

# 5 · paso 3
slides['c5'] = page(f'''
<div class="k">Paso 3</div>{num(5)}
{pitch(180, 250, w=720, h=520, zones=True, losses=[(330, 170), (360, 205), (318, 222), (380, 160), (345, 240)])}
<div class="tag" style="left:180px;top:800px">EJEMPLO · CINCO PÉRDIDAS EN LA MISMA ZONA</div>
{txt('Pérdidas, <em>por zona.</em>', 'Dónde pierdes el balón, no cuántas veces.')}''')

# 6 · paso 4
slides['c6'] = page(f'''
<div class="k">Paso 4</div>{num(6)}
{sheet(110, 300, w=620, h=560, izq=5, dcha=1, perd=5, rot=-1)}
<svg style="left:800px;top:420px" width="160" height="160">{PENCIL}<g filter="url(#pen)" fill="none" stroke-linecap="round">{omark(80, 80, INK, 46)}<path d="M20 140 L140 20" stroke="{INK}" stroke-width="6" opacity=".55"/></g></svg>
<div class="tag" style="left:804px;top:600px">SIN CASILLA</div>
{txt('Los tiros, no. <em>Ya los recuerdas.</em>', 'La hoja guarda lo que a ti se te escapa.')}''')

# 7 · resumen
rows = [('1', 'Una hoja, dos casillas.'), ('2', 'Centros en contra, por banda.'), ('3', 'Pérdidas, por zona.'), ('4', 'Una raya cada vez. Tiros, no.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:34px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px">{a}</span><span style="font-weight:700;font-size:46px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
slides['c7'] = page(f'''
<div class="k">Resumen · primer tiempo</div>{num(7)}
{bignum(300, 250, '95', BLUE, 200)}{bignum(580, 250, '37', RED, 200)}
<div style="position:absolute;left:90px;top:560px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:1060px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>''')

# Stories
slides['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta · fútbol</div>
{pitch(240, 400, w=600, h=440, crosses=5, side='L')}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1 style="font-size:84px">¿Por qué banda te centraron más <em>el último partido?</em></h1></div>
<div style="position:absolute;left:140px;top:1470px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
slides['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta · fútbol</div>
{bignum(250, 400, '95', BLUE, 240)}{bignum(570, 400, '37', RED, 240)}
<div style="position:absolute;left:90px;top:860px;width:900px"><h1 style="font-size:84px">En el descanso, <em>¿de qué hablas?</em></h1></div>
{opt('Del tiro al palo', 1270)}{opt('De la banda que nos centran', 1450)}
<div class="tag" style="left:140px;top:1640px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in slides.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(slides))
