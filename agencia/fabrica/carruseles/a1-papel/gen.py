# Genera las láminas del carrusel y las Stories de a1-papel (Clara, 22/11)
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

def goal(x, y, w=720, h=440, grid=True, tallies=None, hl=None, ink='#121212'):
    """Portería dibujada a lápiz dividida en 6 zonas (2 filas × 3)."""
    cw, ch = w/3, h/2
    s = f'<svg style="left:{x}px;top:{y}px" width="{w}" height="{h+40}" viewBox="0 0 {w} {h+40}">{PENCIL}<g filter="url(#pen)">'
    if hl is not None:
        c, r = hl
        s += f'<rect x="{c*cw+6}" y="{r*ch+6}" width="{cw-12}" height="{ch-12}" fill="#2f6bff" opacity=".14"/>'
    s += f'<path d="M0 {h} L0 0 L{w} 0 L{w} {h}" fill="none" stroke="{ink}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    s += f'<path d="M-40 {h} L{w+40} {h}" stroke="{ink}" stroke-width="3" opacity=".35" stroke-linecap="round"/>'
    if grid:
        s += f'<path d="M{cw} 6 L{cw} {h} M{2*cw} 6 L{2*cw} {h} M6 {ch} L{w-6} {ch}" stroke="{ink}" stroke-width="3.5" opacity=".55" stroke-linecap="round" fill="none"/>'
    if tallies:
        for i, n in enumerate(tallies):
            c, r = i % 3, i // 3
            ox, oy = c*cw + 46, r*ch + 52
            col = '#2f6bff' if hl == (c, r) else '#2b2a27'
            for j in range(min(n, 4)):
                xx = ox + j*30
                s += f'<path d="M{xx} {oy} L{xx+4} {oy+ch-104}" stroke="{col}" stroke-width="7" stroke-linecap="round"/>'
            if n >= 5:
                s += f'<path d="M{ox-14} {oy+ch-120} L{ox+110} {oy+16}" stroke="{col}" stroke-width="7" stroke-linecap="round"/>'
            for j in range(5, n):
                xx = ox + 140 + (j-5)*30
                s += f'<path d="M{xx} {oy} L{xx+4} {oy+ch-104}" stroke="{col}" stroke-width="7" stroke-linecap="round"/>'
    s += '</g></svg>'
    return s

T = [0, 0, 2, 1, 6, 1]  # rayas de EJEMPLO: arriba izq, centro, der · abajo izq, centro, der
HL = (1, 1)  # abajo centro… se recalcula abajo
HL = (T.index(max(T)) % 3, T.index(max(T)) // 3)

def underline(x, y, w):
    return f'<svg style="left:{x}px;top:{y}px" width="{w}" height="30" viewBox="0 0 {w} 30">{PENCIL}<path filter="url(#pen)" d="M4 18 C {w*.3} 8, {w*.7} 26, {w-4} 12" stroke="#2f6bff" stroke-width="8" fill="none" stroke-linecap="round"/></svg>'

slides = {}
# 1 · portada
slides['c1'] = page(f'''
<div class="k">Mundial 2006 · penaltis</div>
<div class="frame" style="left:290px;top:240px;width:500px;height:640px;transform:rotate(-3deg)"><img src="{R}tools/reel_v2/img/papel.jpg" style="object-position:50% 40%"></div>
<div style="position:absolute;left:90px;top:970px;width:900px"><h1>Lehmann tenía<br>un papel.<br><em>¿Y tu portera?</em></h1></div>
<div class="foot" style="bottom:110px">DESLIZA →</div>''')
# 2 · problema
slides['c2'] = page(f'''
<div class="k">El problema</div><div class="n">2/6</div>
{goal(180, 330, grid=False)}
<div style="position:absolute;left:0;top:380px;width:1080px;text-align:center;font-family:S;font-style:italic;font-size:300px;color:#2f6bff;line-height:1">?</div>
<div style="position:absolute;left:90px;top:960px;width:900px"><h2>Le marcan veinte goles y nadie sabe <em>por dónde.</em></h2></div>''')
# 3 · paso 1
slides['c3'] = page(f'''
<div class="k">Paso 1</div><div class="n">3/6</div>
{goal(180, 330)}
<div style="position:absolute;left:90px;top:960px;width:900px"><h2>Divide la portería en <em>seis zonas.</em></h2><p class="sub">Dos filas, tres columnas. En cualquier papel.</p></div>''')
# 4 · paso 2
slides['c4'] = page(f'''
<div class="k">Paso 2</div><div class="n">4/6</div>
{goal(180, 330, tallies=T)}
<div class="tag" style="left:180px;top:820px">EJEMPLO</div>
<div style="position:absolute;left:90px;top:960px;width:900px"><h2>Tu segundo hace una raya <em>por cada gol.</em></h2><p class="sub">En la zona por donde entra. Nada más.</p></div>''')
# 5 · paso 3
slides['c5'] = page(f'''
<div class="k">Paso 3 · Descanso</div><div class="n">5/6</div>
{goal(180, 330, tallies=T, hl=HL)}
<div style="position:absolute;left:{180+HL[0]*240}px;top:{330+(HL[1]+1)*220+50}px;width:240px;text-align:center;font-weight:800;font-size:26px;letter-spacing:.12em;color:#2f6bff">↑ TU AJUSTE</div>
<div class="tag" style="left:180px;top:820px">EJEMPLO</div>
<div style="position:absolute;left:90px;top:960px;width:900px"><h2>La zona con más rayas es <em>tu ajuste.</em></h2><p class="sub">Esa es la charla del descanso. Y la tarea del martes.</p></div>''')
# 6 · resumen
rows = [('1', 'Seis zonas en la portería.'), ('2', 'Una raya por cada gol.'), ('3', 'Descanso: la zona con más rayas.'), ('4', 'Martes: entrena esa zona.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:34px"><span style="font-weight:800;font-size:34px;color:#2f6bff;width:40px">{a}</span><span style="font-weight:700;font-size:44px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
slides['c6'] = page(f'''
<div class="k">Resumen</div><div class="n">6/6</div>
{goal(330, 290, w=420, h=256, tallies=None)}
<div style="position:absolute;left:90px;top:700px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:1110px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>''')

# Stories
slides['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta</div>
<div class="frame" style="left:360px;top:360px;width:360px;height:465px;transform:rotate(2.5deg)"><img src="{R}tools/reel_v2/img/papel.jpg" style="object-position:50% 40%"></div>
<div style="position:absolute;left:90px;top:930px;width:900px"><h1 style="font-size:88px">¿Qué apuntas tú <em>en el descanso?</em></h1></div>
<div style="position:absolute;left:140px;top:1300px;width:800px;height:240px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
slides['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta</div>
{goal(240, 400, w=600, h=366, tallies=T, hl=HL)}
<div style="position:absolute;left:90px;top:940px;width:900px"><h1 style="font-size:84px">En el descanso, ¿qué miras <em>primero?</em></h1></div>
{opt('El marcador', 1280)}{opt('Por dónde nos marcan', 1460)}
<div class="tag" style="left:140px;top:1650px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in slides.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(slides))
