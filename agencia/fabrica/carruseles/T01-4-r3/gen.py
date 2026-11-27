# Genera las láminas del carrusel y las Stories de T01-4-r3 «Gol, palo, árbitro» (Clara, 23/11)
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
.frame{{position:absolute;background:#fffdf8;box-shadow:0 2px 4px rgba(0,0,0,.06),0 30px 70px rgba(30,25,15,.16)}}
.tag{{position:absolute;font-weight:700;font-size:22px;letter-spacing:.16em;color:#121212;opacity:.45}}
.foot{{position:absolute;left:90px;bottom:110px;font-weight:700;font-size:24px;letter-spacing:.16em;opacity:.4}}
.hand{{font-family:S;font-style:italic;font-weight:400;color:#121212}}
svg{{position:absolute;overflow:visible}}
"""
PENCIL = """<defs><filter id="pen" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4" result="t"/>
<feDisplacementMap in="SourceGraphic" in2="t" scale="3.2"/></filter></defs>"""
INK = '#121212'; BLUE = '#2f6bff'; RED = '#d23a2a'

def page(body, story=False):
    cls = 'pg st' if story else 'pg'
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="{cls}">{body}</div></body></html>'

def notebook(x, y, w=700, h=560, rot=-2, words=('Gol.', 'Palo.', 'Árbitro.'), fs=104):
    """Libreta de banquillo: espiral arriba, renglones, tres palabras a lápiz, torcidas."""
    lines = ''.join(f'<div style="position:absolute;left:0;right:0;top:{120+i*96}px;height:2px;background:rgba(47,107,255,.16)"></div>' for i in range(5) if 120+i*96 < h-30)
    rings = ''.join(f'<div style="position:absolute;top:-22px;left:{60+i*((w-120)//9)}px;width:22px;height:46px;border:5px solid rgba(18,18,18,.55);border-radius:12px;background:transparent"></div>' for i in range(10))
    ws = ''.join(f'<div class="hand" style="position:absolute;left:{70+i*34}px;top:{70+i*120}px;font-size:{fs}px;line-height:1;transform:rotate({(-3,2,-1)[i%3]}deg);opacity:.88">{t}</div>' for i, t in enumerate(words))
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{lines}{rings}{ws}</div>'

def tally(n, col=BLUE, hgt=62):
    out = ''
    for k in range(n):
        out += f'<span style="display:inline-block;width:9px;height:{hgt}px;background:{col};border-radius:5px;margin-right:13px;transform:rotate({(-1)**k*4}deg)"></span>'
    return out

LAB = ['Pérdidas', 'Centros', 'Tiros', 'Balón parado', 'Portero', 'Banda']

def grid(x, y, w=820, h=640, counts=None, hi=None, rot=-1, title='Primer tiempo · EJEMPLO', dim=False, struck=False):
    """Hoja preparada en casa: seis casillas (2 columnas × 3 filas)."""
    bw = (w-50*2-30)//2; bh = (h-130-2*24-(70 if struck else 0))//3
    inner = f'<div style="position:absolute;left:50px;top:36px;font-weight:700;font-size:24px;letter-spacing:.14em;opacity:.5;text-transform:uppercase">{title}</div>'
    for i, lab in enumerate(LAB):
        c, r = i % 2, i // 2
        lx = 50 + c*(bw+30); ty = 100 + r*(bh+24)
        isHi = (hi == i)
        bd = f'5px solid {BLUE}' if isHi else '4px solid rgba(18,18,18,.65)'
        bg = 'rgba(47,107,255,.07)' if isHi else 'transparent'
        op = '1' if (not dim or isHi) else '.35'
        n = counts[i] if counts else 0
        inner += f'<div style="position:absolute;left:{lx}px;top:{ty}px;width:{bw}px;height:{bh}px;border:{bd};border-radius:8px;background:{bg};opacity:{op}"><div style="position:absolute;left:20px;top:14px;font-weight:800;font-size:30px">{lab}</div><div style="position:absolute;left:22px;bottom:18px">{tally(n, INK if not isHi else BLUE, 52)}</div></div>'
    if struck:
        inner += f'<div class="hand" style="position:absolute;left:{w-430}px;top:{h-78}px;font-size:40px;opacity:.6">el 7 no baja a ayu…</div>'
        inner += f'<svg style="left:{w-440}px;top:{h-56}px" width="420" height="20">{PENCIL}<path filter="url(#pen)" d="M4 10 L410 8" stroke="{RED}" stroke-width="7" stroke-linecap="round"/></svg>'
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{inner}</div>'

def underline(x, y, w, col=BLUE):
    return f'<svg style="left:{x}px;top:{y}px" width="{w}" height="30" viewBox="0 0 {w} 30">{PENCIL}<path filter="url(#pen)" d="M4 18 C {w*.3} 8, {w*.7} 26, {w-4} 12" stroke="{col}" stroke-width="8" fill="none" stroke-linecap="round"/></svg>'

N = 7
txt = lambda h, sub='', top=1010: f'<div style="position:absolute;left:90px;top:{top}px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
S = {}
CNT = [4, 5, 2, 1, 0, 3]  # EJEMPLO: rayas de un primer tiempo inventado para la hoja (rotulado EJEMPLO)

# 1 · portada (titular: 6 palabras)
S['c1'] = page(f'''
<div class="k">Fútbol · el descanso</div>
{notebook(190, 290, 700, 520, -2.5)}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>«Gol, palo, árbitro» <em>no es un plan.</em></h1></div>
<div class="foot">DESLIZA →</div>''')

# 2 · problema
ficha = f'''<div class="frame" style="left:560px;top:250px;width:420px;height:330px;transform:rotate(2deg)">
<div style="position:absolute;left:36px;top:30px;font-weight:700;font-size:20px;letter-spacing:.14em;opacity:.5">LAIRD Y WATERS · 2008</div>
<div style="position:absolute;left:36px;top:66px;font-weight:500;font-size:24px;line-height:1.3;opacity:.62;width:350px">8 entrenadores titulados. Podían apuntar.</div>
<div style="position:absolute;left:30px;top:150px;font-weight:800;font-size:130px;letter-spacing:-.05em;line-height:1;color:{RED}">59 %</div>
<div style="position:absolute;left:36px;top:288px;font-weight:700;font-size:20px;letter-spacing:.12em;opacity:.45">DE LO IMPORTANTE</div></div>'''
S['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
{notebook(110, 330, 520, 440, -3, fs=80)}
{ficha}
{txt('Apuntas lo que te sorprende, <em>no lo que se repite.</em>')}''')

# 3 · paso 1
S['c3'] = page(f'''
<div class="k">Paso 1 · en casa</div>{num(3)}
{grid(130, 270, 820, 640, counts=None, title='Primer tiempo')}
{txt('Prepara <em>seis casillas.</em>', 'Antes del partido. En casa.')}''')

# 4 · paso 2
S['c4'] = page(f'''
<div class="k">Paso 2 · en el campo</div>{num(4)}
{grid(130, 250, 820, 700, counts=CNT, struck=True)}
{txt('En el campo, <em>solo rayas.</em>', 'Ni frases ni notas largas.')}''')

# 5 · paso 3
S['c5'] = page(f'''
<div class="k">Paso 3 · al descanso</div>{num(5)}
{grid(130, 270, 820, 640, counts=CNT, hi=1, dim=True)}
{txt('Lee la casilla <em>más llena.</em>', 'Antes de hablar.')}''')

# 6 · paso 4
S['c6'] = page(f'''
<div class="k">Paso 4 · en el vestuario</div>{num(6)}
<div class="frame" style="left:150px;top:300px;width:780px;height:560px;transform:rotate(-1deg);background:#fff">
<div style="position:absolute;left:60px;top:70px;font-weight:800;font-size:96px;color:{BLUE};letter-spacing:-.02em">Centros</div>
<div style="position:absolute;left:64px;top:200px">{tally(5, BLUE, 90)}</div>
<div style="position:absolute;left:60px;top:370px;font-weight:800;font-size:56px;opacity:.28;text-decoration:line-through;text-decoration-color:{RED};text-decoration-thickness:6px">El árbitro</div>
</div>
{txt('Habla de eso. <em>No del árbitro.</em>', 'Que la segunda parte no empiece igual.')}''')

# 7 · resumen
rows = [('1', 'En casa, seis casillas.'), ('2', 'En el campo, solo rayas.'), ('3', 'Al descanso, la más llena.'), ('4', 'Después, hablas.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:38px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px">{a}</span><span style="font-weight:700;font-size:50px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
S['c7'] = page(f'''
<div class="k">Resumen · el descanso</div>{num(7)}
<div style="position:absolute;left:90px;top:330px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:1010px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>''')

# Stories
S['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta · fútbol</div>
{notebook(220, 400, 640, 480, -2.5, words=('', '', ''), fs=90)}
<div class="hand" style="position:absolute;left:330px;top:560px;font-size:120px;color:rgba(18,18,18,.25)">¿…?</div>
<div style="position:absolute;left:90px;top:1010px;width:900px"><h1 style="font-size:84px">¿Qué pone tu libreta <em>del último partido?</em></h1></div>
<div style="position:absolute;left:140px;top:1470px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
S['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta · fútbol</div>
{notebook(250, 380, 580, 440, -2, fs=82)}
<div style="position:absolute;left:90px;top:960px;width:900px"><h1 style="font-size:84px">En el descanso, <em>¿qué miras primero?</em></h1></div>
{opt('Lo que recuerdo', 1270)}{opt('Lo que apunté', 1450)}
<div class="tag" style="left:140px;top:1640px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in S.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(S))
