# Genera las láminas del carrusel y las Stories de T01-1-r2 «El vestuario te mira» (Clara, 23/11)
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


PAPEL = f'{R}tools/reel_v2/img/papel.jpg'

def photo(x, y, w, rot=-2, cap=''):
    h = int(w*1395/1080)
    c = f'<div class="tag" style="left:0;top:{h+44}px;opacity:.5">{cap}</div>' if cap else ''
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w+36}px;height:{h+36}px;transform:rotate({rot}deg);background:#fff"><img src="{PAPEL}" style="position:absolute;left:18px;top:18px;width:{w}px;height:{h}px;display:block"/>{c}</div>'

def sheet(x, y, w, rows, rot=-1, title='', hi=None, filled=None, under=False, dim=False, lh=96, mark=''):
    """Hoja del entrenador: renglones a lápiz; el último, libre (o rellenado)."""
    n = len(rows)
    h = 130 + n*lh + 40
    inner = f'<div style="position:absolute;left:50px;top:40px;font-weight:700;font-size:22px;letter-spacing:.14em;opacity:.5;text-transform:uppercase">{title}</div>'
    for i, t in enumerate(rows):
        ty = 120 + i*lh
        last = (i == n-1)
        col = f'rgba(47,107,255,.85)' if (last and hi) else 'rgba(18,18,18,.18)'
        wd = 5 if (last and hi) else 2
        dash = 'dashed' if (last and hi and not filled) else 'solid'
        op = '.3' if (dim and not last) else '.85'
        if not (last and under):
            inner += f'<div style="position:absolute;left:50px;right:50px;top:{ty+lh-14}px;border-top:{wd}px {dash} {col}"></div>'
        if last and mark and not filled:
            inner += f'<div class="hand" style="position:absolute;left:62px;top:{ty+8}px;font-size:60px;line-height:1;color:{BLUE}">{mark}</div>'
        if t and not last:
            inner += f'<div class="hand" style="position:absolute;left:62px;top:{ty+8}px;font-size:56px;line-height:1;opacity:{op};transform:rotate({(-1,1,-.5,.6)[i%4]}deg)">{t}</div>'
        if last and filled:
            inner += f'<div class="hand" style="position:absolute;left:62px;top:{ty+2}px;font-size:64px;line-height:1;color:{BLUE};transform:rotate(-1deg)">{filled}</div>'
        if last and under:
            inner += f'<svg style="left:48px;top:{ty+lh-10}px" width="{w-100}" height="34">{PENCIL}<path filter="url(#pen)" d="M4 14 C {(w-100)*.3} 4, {(w-100)*.7} 28, {w-104} 10" stroke="{BLUE}" stroke-width="10" fill="none" stroke-linecap="round"/></svg>'
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{inner}</div>'

def dot(cx, cy, n, col=INK, ring=None, op=1):
    r = f'<div style="position:absolute;left:-22px;top:-22px;width:130px;height:130px;border:6px solid {ring};border-radius:50%"></div>' if ring else ''
    return f'<div style="position:absolute;left:{cx-43}px;top:{cy-43}px;width:86px;height:86px;opacity:{op}">{r}<div style="width:86px;height:86px;border-radius:50%;background:{col};color:#fbfaf7;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">{n}</div></div>'

def board(x, y, w=860, h=600, rot=-1):
    lines = (f'<div style="position:absolute;left:40px;right:40px;top:40px;bottom:40px;border:3px solid rgba(47,107,255,.22);border-radius:4px"></div>'
             f'<div style="position:absolute;left:{w//2-120}px;top:40px;width:240px;height:120px;border:3px solid rgba(47,107,255,.22);border-top:none"></div>')
    d = dot(300, 330, 9, INK, ring='rgba(18,18,18,.5)', op=.55) + dot(520, 290, 10, INK, ring='rgba(18,18,18,.5)', op=.55) + dot(700, 420, 7, RED, ring=RED)
    xs = ''  # sin aspas: el 9 y el 10 marcados con círculo
    _xs = ''.join(f'<svg style="left:{cx-40}px;top:{cy-40}px" width="80" height="80">{PENCIL}<path filter="url(#pen)" d="M10 10 L70 70 M70 10 L10 70" stroke="{INK}" stroke-width="6" stroke-linecap="round" opacity=".55"/></svg>' for cx, cy in [(300, 330), (520, 290)])
    tag = f'<div class="tag" style="left:44px;top:{h-34}px;opacity:.4;font-size:20px">EJEMPLO</div>'
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{lines}{d}{xs}{tag}</div>'


def room(x, y, w=860, h=560, rot=-1, sheet_in=False, cold=True):
    """Vestuario visto desde arriba: once puntos en el banco y sus miradas hacia el centro (el entrenador)."""
    import math
    cx, cy = w//2, h-110
    inner = f'<div style="position:absolute;left:30px;right:30px;top:30px;height:16px;border-bottom:3px solid rgba(18,18,18,.12)"></div>'
    lines = ''
    for i in range(11):
        a = math.pi*(0.08 + 0.84*i/10)
        px = cx - math.cos(a)*(w/2-90); py = cy - math.sin(a)*(h-230)
        lines += f'<path filter="url(#pen)" d="M{px:.0f} {py:.0f} L{cx:.0f} {cy-30:.0f}" stroke="{INK}" stroke-width="2" opacity=".18"/>'
        inner += f'<div style="position:absolute;left:{px-22:.0f}px;top:{py-22:.0f}px;width:44px;height:44px;border-radius:50%;background:{INK};opacity:.82"></div>'
    svg = f'<svg style="left:0;top:0" width="{w}" height="{h}">{PENCIL}{lines}</svg>'
    centre = (f'<div class="frame" style="left:{cx-80}px;top:{cy-70}px;width:160px;height:110px;transform:rotate(-4deg)">'
              + ''.join(f'<div style="position:absolute;left:20px;right:20px;top:{28+i*26}px;border-top:3px solid {BLUE}"></div>' for i in range(3)) + '</div>') if sheet_in else \
             f'<div style="position:absolute;left:{cx-70}px;top:{cy-50}px;width:140px;height:80px;border:3px dashed rgba(18,18,18,.3);border-radius:10px"></div>'
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{svg}{inner}{centre}</div>'

def clock(x, y, t, d=220, rot=4, blue=False):
    col = BLUE if blue else INK
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;transform:rotate({rot}deg)"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:{int(d*.3)}px;letter-spacing:-.02em;color:{col}">{t}</div></div>'

def whistle(x, y, on=True, s=1.0):
    col = RED if on else 'rgba(18,18,18,.25)'
    return (f'<svg style="left:{x}px;top:{y}px" width="{int(200*s)}" height="{int(130*s)}" viewBox="0 0 200 130">{PENCIL}'
            f'<g filter="url(#pen)" fill="none" stroke="{col}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
            f'<circle cx="70" cy="75" r="45"/><path d="M95 38 L190 38 L190 70 L112 70"/><circle cx="70" cy="75" r="12"/></g></svg>')

N = 7
txt = lambda h, sub='', top=1010: f'<div style="position:absolute;left:90px;top:{top}px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
S = {}
TRES = ['Funciona · la presión arriba', 'Falla · la espalda del 3', 'Cambio · el 8, más cerca']  # EJEMPLO
EMPTY = ['', '', '']

# 1 · portada (titular: 6 palabras)
S['c1'] = page(f'''
<div class="k">Fútbol · el descanso</div>
{room(110, 280, rot=-1.5, sheet_in=True)}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>Entra al descanso <em>con algo escrito.</em></h1></div>
<div class="foot">DESLIZA →</div>''')

# 2 · problema
S['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
{room(110, 300, rot=-1)}
{clock(770, 210, '45′')}
{txt('Te miran las manos <em>y no llevas nada.</em>', 'Cuarenta y cinco minutos en la banda y ni una línea. Acabas empezando por el árbitro.')}''')

# 3 · el caso real
S['c3'] = page(f'''
<div class="k">Mundial 2006 · penaltis</div>{num(3)}
{photo(300, 230, 420, -2)}
<div class="hand" style="position:absolute;left:640px;top:760px;font-size:70px;color:{BLUE};transform:rotate(-6deg)">¿Cambiasso?</div>
{txt('Lehmann tenía un papel. <em>Cambiasso no estaba.</em>', 'Según quien lo vio, lo miró igual y se tomó su tiempo. Lo paró.', top=990)}
<div class="tag" style="left:90px;top:1350px;font-size:19px">PAPEL DE LEHMANN · FOTO: ANDREAS KÖPKE (DP) · FUENTE: FIFA, 6/7/2016</div>''')

# 4 · paso 1
S['c4'] = page(f'''
<div class="k">Paso 1 · desde el 35′</div>{num(4)}
{sheet(150, 300, 720, EMPTY, title='Descanso · tres líneas', hi=True, lh=120)}
{clock(780, 200, '35′', blue=True)}
{txt('Tu segundo <em>te escribe.</em>', 'Desde el minuto 35. Tú sigues mirando el partido.')}''')

# 5 · paso 2
S['c5'] = page(f'''
<div class="k">Paso 2 · tres líneas</div>{num(5)}
{sheet(150, 300, 780, TRES[:2] + [''], title='Descanso · EJEMPLO', hi=True, filled=TRES[2], under=True, lh=110)}
{txt('Qué funciona, qué falla, <em>un cambio.</em>', 'Una línea cada cosa. El cambio, subrayado.')}''')

# 6 · paso 3
S['c6'] = page(f'''
<div class="k">Paso 3 · al entrar</div>{num(6)}
{room(110, 300, rot=-1, sheet_in=True)}

{txt('Léelo. <em>Luego habla.</em>', 'Papel primero, voz después. Lo del árbitro no está en las tres líneas.')}''')

# 7 · resumen
rows = [('1', 'Desde el 35′, tu segundo escribe.'), ('2', 'Qué funciona.'), ('3', 'Qué falla.'), ('4', 'Un cambio.'), ('5', 'Lo lees. Luego hablas.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:36px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px">{a}</span><span style="font-weight:700;font-size:48px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
S['c7'] = page(f'''
<div class="k">Resumen · el descanso</div>{num(7)}
<div style="position:absolute;left:90px;top:310px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:1030px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>''')

# Stories
S['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta · fútbol</div>
{room(140, 400, 800, 520, rot=-2)}
<div style="position:absolute;left:90px;top:1010px;width:900px"><h1 style="font-size:80px">¿Qué es lo primero que dices <em>al entrar al vestuario?</em></h1></div>
<div style="position:absolute;left:140px;top:1490px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
S['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta · fútbol</div>
{sheet(240, 380, 600, ['', '', '', ''], rot=-2, title='Descanso', hi=True, lh=100)}
{clock(760, 330, '45′', d=180)}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1 style="font-size:80px">En el descanso, <em>¿con qué entras?</em></h1></div>
{opt('Con algo escrito', 1290)}{opt('Con lo que me sale', 1470)}
<div class="tag" style="left:140px;top:1660px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in S.items():
    open(os.path.join(D, k + '.html'), 'w').write(v)
print('ok', list(S))
