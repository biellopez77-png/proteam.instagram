# Genera las láminas del carrusel y las Stories de T01-1-r3 «Trece mil para siete» (Clara, 23/11)
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

IMG = R + 'tools/reel_v2/img/'

def photo(x, y, w, h, src, rot=-2, cap=''):
    """Foto real enmarcada en blanco con sombra suave."""
    c = f'<div style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-weight:700;font-size:18px;letter-spacing:.14em;opacity:.45">{cap}</div>' if cap else ''
    pad = 26; bot = 64 if cap else pad
    return (f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">'
            f'<div style="position:absolute;left:{pad}px;top:{pad}px;right:{pad}px;bottom:{bot}px;background:url({src}) center/cover"></div>{c}</div>')

def underline(x, y, w, col=BLUE):
    return f'<svg style="left:{x}px;top:{y}px" width="{w}" height="30" viewBox="0 0 {w} 30">{PENCIL}<path filter="url(#pen)" d="M4 18 C {w*.3} 8, {w*.7} 26, {w-4} 12" stroke="{col}" stroke-width="8" fill="none" stroke-linecap="round"/></svg>'

ROWS = ['El peligroso', 'La banda', 'El balón parado']

def ficha(x, y, w=640, h=520, rot=-2, filled=True, hi=None, title='Rival · EJEMPLO'):
    """Ficha del rival: tres renglones a lápiz."""
    inner = f'<div style="position:absolute;left:54px;top:44px;font-weight:700;font-size:24px;letter-spacing:.14em;opacity:.5;text-transform:uppercase">{title}</div>'
    for i, t in enumerate(ROWS):
        ty = 130 + i * ((h - 170) // 3)
        col = BLUE if hi == i else INK
        inner += f'<div style="position:absolute;left:54px;top:{ty}px;font-weight:800;font-size:22px;letter-spacing:.12em;opacity:.45">{i+1}</div>'
        if filled:
            inner += f'<div class="hand" style="position:absolute;left:100px;top:{ty-18}px;font-size:{int(w*0.095)}px;line-height:1;color:{col};transform:rotate({(-1,1,-0.5)[i]}deg)">{t}</div>'
            if hi == i:
                inner += underline(96, ty + int(w*0.095) - 6, int(w*0.5))
        inner += f'<div style="position:absolute;left:96px;right:54px;top:{ty+int(w*0.095)+4}px;height:2px;background:rgba(18,18,18,.18)"></div>'
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{inner}</div>'

MESES = ['Sep', 'Oct', 'Nov', 'Dic', 'Ene', 'Feb', 'Mar', 'Abr']

def calendar(x, y, w=860, h=470, rot=-1, thread=True, pinned=False, full=False, title='Liga · doble vuelta · EJEMPLO'):
    """Calendario genérico: ida arriba (tachada), vuelta abajo; un hilo azul une octubre con enero."""
    cw = (w - 100 - 3*20) // 4; ch = (h - 140 - 30) // 2
    inner = f'<div style="position:absolute;left:50px;top:34px;font-weight:700;font-size:22px;letter-spacing:.14em;opacity:.5;text-transform:uppercase">{title}</div>'
    pos = {}
    for i, m in enumerate(MESES):
        c, r = i % 4, i // 4
        lx = 50 + c*(cw+20); ty = 100 + r*(ch+30); pos[m] = (lx, ty)
        hi = (m in ('Oct', 'Ene'))
        bd = f'4px solid {BLUE}' if (hi and thread) else '3px solid rgba(18,18,18,.55)'
        inner += f'<div style="position:absolute;left:{lx}px;top:{ty}px;width:{cw}px;height:{ch}px;border:{bd};border-radius:8px"><div style="position:absolute;left:16px;top:10px;font-weight:800;font-size:26px">{m}</div>'
        if r == 0 and not full:
            inner += f'<svg style="left:10px;top:{ch//2}px" width="{cw-20}" height="20">{PENCIL}<path filter="url(#pen)" d="M2 14 L{cw-24} 4" stroke="{INK}" stroke-opacity=".35" stroke-width="5" stroke-linecap="round"/></svg>'
        if full or (pinned and m == 'Ene'):
            inner += f'<div style="position:absolute;left:{cw//2-38}px;top:{ch//2-24}px;width:76px;height:58px;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.18);transform:rotate({(-4,3,-2,5)[i%4]}deg)"><div style="margin:14px 10px 0;height:3px;background:{BLUE if m=="Ene" else "rgba(18,18,18,.4)"}"></div><div style="margin:9px 10px 0;height:3px;background:rgba(18,18,18,.3)"></div><div style="margin:9px 10px 0;width:30px;height:3px;background:rgba(18,18,18,.3)"></div></div>'
        inner += '</div>'
    if thread:
        (ax, ay), (bx, by) = pos['Oct'], pos['Ene']
        x1, y1 = ax + cw//2, ay + ch - 6; x2, y2 = bx + cw//2, by + 8
        inner += f'<svg style="left:0;top:0" width="{w}" height="{h}">{PENCIL}<path filter="url(#pen)" d="M{x1} {y1} C {x1+40} {y1+60}, {x2+120} {y2-70}, {x2} {y2}" stroke="{BLUE}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>'
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{inner}</div>'

N = 6
txt = lambda h, sub='', top=1010: f'<div style="position:absolute;left:90px;top:{top}px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
S = {}

# 1 · portada (titular: 8 palabras: La primera vuelta es tu base de datos)
S['c1'] = page(f'''
<div class="k">Fútbol · liga a doble vuelta</div>
{photo(300, 250, 480, 640, IMG+'papel.jpg', -2.5, 'EL PAPEL DE LEHMANN · 2006')}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>La primera vuelta <em>es tu base de datos.</em></h1></div>
<div class="foot">DESLIZA →</div>''')

# 2 · problema
S['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
{calendar(110, 300, 860, 520, -1.5)}
{txt('Vuelves a jugar contra él <em>y no recuerdas qué te hizo.</em>', 'El resultado, sí. Por dónde te llegaron, no.')}''')

# 3 · paso 1
S['c3'] = page(f'''
<div class="k">Paso 1 · al acabar</div>{num(3)}
{ficha(200, 290, 680, 560, -2)}
{txt('Tres líneas <em>del rival.</em>', 'El peligroso, la banda y el balón parado.')}''')

# 4 · paso 2
S['c4'] = page(f'''
<div class="k">Paso 2 · guárdala</div>{num(4)}
{calendar(110, 300, 860, 520, -1.5, thread=True, pinned=True)}
{txt('Ponla en la semana <em>de la vuelta.</em>', 'Una ficha por rival.')}''')

# 5 · paso 3
S['c5'] = page(f'''
<div class="k">Paso 3 · la semana que vuelves</div>{num(5)}
{ficha(200, 290, 680, 560, 1.5, hi=1)}
{txt('Léelas antes <em>de preparar el partido.</em>', 'Las tres líneas que apuntaste en la ida.')}''')

# 6 · resumen
rows = [('1', 'Al acabar, tres líneas.'), ('2', 'El peligroso, la banda, el balón parado.'), ('3', 'En la semana de la vuelta.'), ('4', 'Léelas antes de preparar.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:38px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px;flex:none">{a}</span><span style="font-weight:700;font-size:50px;letter-spacing:-.01em;line-height:1.15">{b}</span></div>' for a, b in rows)
S['c6'] = page(f'''
<div class="k">Resumen · la vuelta</div>{num(6)}
<div style="position:absolute;left:90px;top:300px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:1040px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>''')

# Stories
S['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta · fútbol</div>
{calendar(110, 420, 860, 520, -1.5, thread=True, title='Liga · doble vuelta')}
<div style="position:absolute;left:90px;top:1060px;width:900px"><h1 style="font-size:84px">¿Contra quién vuelves a jugar <em>este mes?</em></h1></div>
<div style="position:absolute;left:140px;top:1470px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
S['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta · fútbol</div>
{ficha(250, 380, 580, 460, -2, filled=False, title='Rival de la ida')}
<div style="position:absolute;left:90px;top:960px;width:900px"><h1 style="font-size:84px">Del rival de la ida, <em>¿qué tienes?</em></h1></div>
{opt('Lo que recuerdo', 1270)}{opt('Tres líneas apuntadas', 1450)}
<div class="tag" style="left:140px;top:1640px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in S.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(S))
