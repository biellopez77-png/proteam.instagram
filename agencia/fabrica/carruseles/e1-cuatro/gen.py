# Genera las láminas del carrusel y las Stories de e1-cuatro «El martes que no puedes ir» (Clara, 23/11)
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
IMG = R + 'tools/reel_v4/e1-cuatro/img/'

def photo(x, y, w, h, src, rot=0, pos='center'):
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)"><img src="{IMG}{src}" style="object-position:{pos}"></div>'

def agenda(x, y, w=620, crossed=True, ok=False, s=1.0):
    """Hoja de agenda dibujada: Martes 24 · 19:00 ENTRENO."""
    h = int(300*s)
    t = f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;padding:0;background:#fffdf8;transform:rotate(-1.2deg)">'
    t += f'<div style="position:absolute;left:{int(44*s)}px;top:{int(36*s)}px;font-weight:700;font-size:{int(26*s)}px;letter-spacing:.16em;opacity:.45">MARTES 24</div>'
    t += f'<div style="position:absolute;left:0;right:0;top:{int(92*s)}px;border-top:2px solid rgba(47,107,255,.14)"></div>'
    t += f'<div style="position:absolute;left:{int(44*s)}px;top:{int(130*s)}px;font-weight:800;font-size:{int(64*s)}px;letter-spacing:-.01em">19:00 <span style="font-weight:700;opacity:.8">ENTRENO</span></div>'
    t += f'<div style="position:absolute;left:0;right:0;top:{int(240*s)}px;border-top:2px solid rgba(47,107,255,.14)"></div>'
    if crossed:
        t += f'<svg style="left:{int(30*s)}px;top:{int(150*s)}px" width="{w-60}" height="{int(60*s)}">{PENCIL}<path filter="url(#pen)" d="M0 {int(40*s)} C {w*.3} {int(20*s)}, {w*.6} {int(44*s)}, {w-70} {int(14*s)}" stroke="{RED}" stroke-width="9" fill="none" stroke-linecap="round"/></svg>'
    if ok:
        t += f'<svg style="left:{w-110}px;top:{int(22*s)}px" width="90" height="90">{PENCIL}<path filter="url(#pen)" d="M10 46 L36 72 L82 14" stroke="{BLUE}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return t + '</div>'

def head(x, y, notes=(), fade=False):
    """Perfil de cabeza a lápiz con notas dentro."""
    s = f'<svg style="left:{x}px;top:{y}px" width="520" height="560" viewBox="0 0 520 560">{PENCIL}<g filter="url(#pen)" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
    s += '<path d="M150 540 L150 430 C 70 390, 40 300, 50 220 C 64 100, 170 20, 290 24 C 410 28, 490 120, 480 230 C 476 280, 500 300, 510 330 L470 344 C 474 380, 470 410, 440 420 L400 424 C 396 470, 380 500, 330 500 L330 540"/>'
    s += '</g></svg>'
    for i, (t, dx, dy, rot) in enumerate(notes):
        op = .28 if fade else 1
        s += f'<div style="position:absolute;left:{x+dx}px;top:{y+dy}px;background:#fff;padding:14px 22px;font-weight:700;font-size:30px;box-shadow:0 10px 30px rgba(30,25,15,.12);transform:rotate({rot}deg);opacity:{op};white-space:nowrap">{t}</div>'
    return s

def underline(x, y, w):
    return f'<svg style="left:{x}px;top:{y}px" width="{w}" height="30" viewBox="0 0 {w} 30">{PENCIL}<path filter="url(#pen)" d="M4 18 C {w*.3} 8, {w*.7} 26, {w-4} 12" stroke="{BLUE}" stroke-width="8" fill="none" stroke-linecap="round"/></svg>'

def sheet(x, y, rows, w=640, title='HOY TOCA', rot=1.2, checks=0):
    t = f'<div class="frame" style="left:{x}px;top:{y}px;width:{w}px;height:{140+len(rows)*104}px;padding:0;background:#fffdf8;transform:rotate({rot}deg)">'
    t += f'<div style="position:absolute;left:48px;top:40px;font-weight:800;font-size:30px;letter-spacing:.14em;color:{BLUE}">{title}</div>'
    for i, r in enumerate(rows):
        yy = 110 + i*104
        t += f'<div style="position:absolute;left:0;right:0;top:{yy}px;border-top:2px solid rgba(47,107,255,.14)"></div>'
        t += f'<div style="position:absolute;left:48px;top:{yy+28}px;font-weight:700;font-size:38px">{r}</div>'
        if i < checks:
            t += f'<svg style="left:{w-110}px;top:{yy+18}px" width="70" height="70">{PENCIL}<path filter="url(#pen)" d="M8 36 L28 56 L62 12" stroke="{BLUE}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return t + '</div>'

N = 7
txt = lambda h, sub='', top=1000: f'<div style="position:absolute;left:90px;top:{top}px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
slides = {}

# 1 · portada
slides['c1'] = page(f'''
<div class="k">Entrenadores · el día que faltas</div>
{agenda(140, 330, w=640)}
{photo(640, 560, 300, 225, 'silbato.jpg', rot=3)}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>El martes que<br><em>no puedes ir.</em></h1></div>
<div class="foot" style="bottom:110px">DESLIZA →</div>''')

# 2 · problema
slides['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
{head(280, 300, notes=[('Quién vuelve', 150, 150, -3), ('El jueves', 210, 240, 2), ('3 semanas sin jugar', 110, 330, -1)], fade=True)}
{txt('Todo lo de tu equipo <em>está en tu cabeza.</em>', 'Y lo que no está apuntado, el martes no existe.')}''')

# 3 · paso 1: quién está
slides['c3'] = page(f'''
<div class="k">Paso 1</div>{num(3)}
{sheet(220, 330, ['Vuelve de lesión: _____', 'Tres semanas sin jugar: ___', 'Tocado, con cuidado: ___'], w=660, title='QUIÉN ESTÁ', rot=-1.2)}
<div class="tag" style="left:220px;top:830px">PLANTILLA</div>
{txt('Apunta <em>quién está.</em>', 'Quién vuelve de lesión y quién lleva semanas sin jugar.')}''')

# 4 · paso 2: de dónde venís
days = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
dd = ''
for i, d in enumerate(days):
    x = 130 + i*120
    dd += f'<div style="position:absolute;left:{x}px;top:470px;width:100px;height:120px;background:#fff;box-shadow:0 8px 24px rgba(30,25,15,.10);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:48px;opacity:{1 if d=="J" else .45}">{d}</div>'
dd += f'<svg style="left:{130+3*120-30}px;top:440px" width="160" height="180">{PENCIL}<ellipse filter="url(#pen)" cx="80" cy="90" rx="72" ry="84" fill="none" stroke="{BLUE}" stroke-width="7"/></svg>'
dd += f'<div style="position:absolute;left:{130+3*120-60}px;top:660px;width:220px;text-align:center;font-family:S;font-style:italic;font-size:44px;color:{BLUE}">lo que trabajasteis</div>'
slides['c4'] = page(f'''
<div class="k">Paso 2</div>{num(4)}
{dd}
{txt('Apunta <em>de dónde venís.</em>', 'Qué trabajasteis en la última sesión.')}''')

# 5 · paso 3: hoy toca
slides['c5'] = page(f'''
<div class="k">Paso 3</div>{num(5)}
{sheet(220, 300, ['Calentamiento', 'Tarea principal', 'Final'], w=640, checks=3)}
<div class="tag" style="left:220px;top:800px">PLANTILLA</div>
{txt('Deja escrito <em>qué toca hoy.</em>', 'La sesión entera, en una hoja.')}''')

# 6 · paso 4: pásaselo
slides['c6'] = page(f'''
<div class="k">Paso 4</div>{num(6)}
{photo(150, 290, 560, 420, 'pabellon.jpg', rot=-1.5)}
{agenda(520, 600, w=460, crossed=False, ok=True, s=.75)}
{txt('Pásaselo <em>en un minuto.</em>', 'Y el entreno sale igual, aunque tú no estés.')}''')

# 7 · resumen
rows = [('1', 'Quién está.'), ('2', 'De dónde venís.'), ('3', 'Qué toca hoy.'), ('4', 'Pásaselo en un minuto.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:34px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px">{a}</span><span style="font-weight:700;font-size:46px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
slides['c7'] = page(f'''
<div class="k">Resumen · el día que faltas</div>{num(7)}
{agenda(330, 260, w=420, crossed=False, ok=True, s=.7)}
<div style="position:absolute;left:90px;top:560px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:1060px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>''')

# Stories
slides['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta</div>
{agenda(230, 400, w=620)}
<div style="position:absolute;left:90px;top:900px;width:900px"><h1 style="font-size:84px">Si faltas el martes, ¿qué <em>no sabe tu segundo?</em></h1></div>
<div style="position:absolute;left:140px;top:1370px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
slides['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta</div>
{photo(280, 400, 520, 390, 'silbato.jpg', rot=2)}
<div style="position:absolute;left:90px;top:900px;width:900px"><h1 style="font-size:84px">Si mañana faltas, <em>tu segundo…</em></h1></div>
{opt('Sabe qué toca', 1270)}{opt('Te escribe «¿Qué toca hoy?»', 1450)}
<div class="tag" style="left:140px;top:1640px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in slides.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(slides))
