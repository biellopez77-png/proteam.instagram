# Genera las láminas del carrusel y las Stories de b2-rpe «Una pregunta del 1 al 10» (Clara, 23/11)
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

def underline(x, y, w, col=BLUE):
    return f'<svg style="left:{x}px;top:{y}px" width="{w}" height="30" viewBox="0 0 {w} 30">{PENCIL}<path filter="url(#pen)" d="M4 18 C {w*.3} 8, {w*.7} 26, {w-4} 12" stroke="{col}" stroke-width="8" fill="none" stroke-linecap="round"/></svg>'

def photo(src, x, y, w, h, rot=-2, pad=22, pos='center'):
    return f'<div class="frame" style="left:{x}px;top:{y}px;width:{w+2*pad}px;height:{h+2*pad}px;padding:{pad}px;transform:rotate({rot}deg)"><div style="width:{w}px;height:{h}px;background:url({src}) {pos}/cover"></div></div>'

def circle(x, y, w, h, col=BLUE):
    return f'<svg style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{PENCIL}<path filter="url(#pen)" d="M{w*.55} {h*.06} C {w*.98} {h*.04}, {w*1.0} {h*.9}, {w*.5} {h*.95} C {w*.04} {h*.97}, {w*.0} {h*.12}, {w*.62} {h*.12}" stroke="{col}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>'

def scale(x, y, pick=7):
    out = ''
    for i in range(1, 11):
        cx = x + (i-1)*76
        op = '1' if i == pick else '.38'
        out += f'<div style="position:absolute;left:{cx}px;top:{y}px;width:70px;text-align:center;font-weight:800;font-size:64px;opacity:{op};color:{BLUE if i==pick else INK}">{i}</div>'
    out += circle(x + (pick-1)*76 - 22, y - 26, 116, 130)
    return out

N = 6
txt = lambda h, sub='', top=1010: f'<div style="position:absolute;left:90px;top:{top}px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
S = {}

# 1 · portada (titular: 6 palabras)
S['c1'] = page(f'''
<div class="k">Baloncesto · la carga</div>
{photo('tension.jpg', 150, 280, 740, 494, -2)}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>Lo podías saber <em>desde el jueves.</em></h1></div>
<div class="foot">DESLIZA →</div>''')

# 2 · problema: marcador por cuartos (EJEMPLO)
Q = [('1º', '18', '16'), ('2º', '17', '15'), ('3º', '9', '22'), ('4º', '14', '19')]
cells = ''
for i, (q, a, b) in enumerate(Q):
    hot = (i == 2)
    col = RED if hot else INK
    cells += f'''<div style="position:absolute;left:{50+i*185}px;top:90px;width:160px;text-align:center">
<div style="font-weight:700;font-size:26px;letter-spacing:.12em;opacity:.5">{q}</div>
<div style="font-weight:800;font-size:84px;line-height:1.15;color:{col};opacity:{1 if hot else .5}">{a}</div>
<div style="font-weight:700;font-size:40px;opacity:.35">{b}</div></div>'''
S['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
<div class="frame" style="left:120px;top:300px;width:840px;height:420px;transform:rotate(-1.5deg)">
<div style="position:absolute;left:50px;top:34px;font-weight:700;font-size:22px;letter-spacing:.16em;opacity:.45">SÁBADO · POR CUARTOS · EJEMPLO</div>
{cells}
{underline(410, 330, 150, RED)}
</div>
{txt('El sábado, en el tercer cuarto, <em>se apagan.</em>', 'Cambias la charla. Cambias las rotaciones. Nada.')}''')

# 3 · paso 1: la pregunta
S['c3'] = page(f'''
<div class="k">Paso 1 · al acabar el entreno</div>{num(3)}
<div class="frame" style="left:90px;top:330px;width:900px;height:380px;transform:rotate(-1deg)">
<div class="hand" style="position:absolute;left:60px;top:40px;font-size:60px;opacity:.75">¿Cuánto te ha costado?</div>
{scale(60, 200)}
</div>
{txt('Una pregunta: <em>del 1 al 10.</em>', 'Al acabar cada entreno, a cada jugador.')}''')

# 4 · paso 2: la cuenta (EJEMPLO)
S['c4'] = page(f'''
<div class="k">Paso 2 · la cuenta</div>{num(4)}
<div class="frame" style="left:140px;top:300px;width:800px;height:440px;transform:rotate(1.2deg)">
<div style="position:absolute;left:56px;top:40px;font-weight:700;font-size:22px;letter-spacing:.16em;opacity:.45">JUEVES · EJEMPLO</div>
<div style="position:absolute;left:56px;top:110px;font-weight:800;font-size:120px;letter-spacing:-.03em;line-height:1"><span style="color:{BLUE}">7</span> × 90′</div>
<div style="position:absolute;left:56px;top:270px;font-weight:800;font-size:110px;letter-spacing:-.03em;line-height:1">= 630</div>
{underline(60, 385, 330)}
</div>
{txt('Multiplícalo <em>por los minutos.</em>', 'Esfuerzo × minutos: la carga del día.')}''')

# 5 · paso 3: tres semanas (EJEMPLO)
W = [(520, 'S1'), (610, 'S2'), (700, 'S3')]
bars = ''
for i, (v, lab) in enumerate(W):
    hpx = int(v * 0.42)
    x0 = 90 + i*240
    bars += f'<div style="position:absolute;left:{x0}px;bottom:90px;width:120px;height:{hpx}px;background:{BLUE};opacity:{.45 + i*.25};border-radius:10px 10px 0 0"></div>'
    bars += f'<div style="position:absolute;left:{x0}px;bottom:{100+hpx}px;width:120px;text-align:center;font-weight:800;font-size:34px">{v}</div>'
    bars += f'<div style="position:absolute;left:{x0}px;bottom:40px;width:120px;text-align:center;font-weight:700;font-size:24px;letter-spacing:.12em;opacity:.5">JUE {lab}</div>'
S['c5'] = page(f'''
<div class="k">Paso 3 · tres semanas</div>{num(5)}
<div class="frame" style="left:120px;top:280px;width:840px;height:500px;transform:rotate(-1deg)">
<div style="position:absolute;left:50px;top:34px;font-weight:700;font-size:22px;letter-spacing:.16em;opacity:.45">CARGA DEL JUEVES · EJEMPLO</div>
{bars}
</div>
{txt('Compara <em>jueves y sábados.</em>', 'En tres semanas sabrás quién llega roto.')}''')

# 6 · resumen
rows = [('1', 'Al acabar, del 1 al 10.'), ('2', 'Por los minutos.'), ('3', 'Jueves contra sábado.'), ('4', 'Tres semanas.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:38px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px">{a}</span><span style="font-weight:700;font-size:50px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
S['c6'] = page(f'''
<div class="k">Resumen · la carga</div>{num(6)}
<div style="position:absolute;left:90px;top:330px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:960px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>
<div class="foot" style="text-transform:none;letter-spacing:.04em;font-weight:500;font-size:24px">Método: RPE de sesión (Foster et al., 2001)</div>''')

# Stories
S['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta · baloncesto</div>
{photo('balones.jpg', 160, 400, 712, 475, -2)}
<div style="position:absolute;left:90px;top:1040px;width:900px"><h1 style="font-size:84px">¿Qué día entrenas <em>más fuerte?</em></h1></div>
<div style="position:absolute;left:140px;top:1470px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
S['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta · baloncesto</div>
<div class="frame" style="left:110px;top:420px;width:860px;height:340px;transform:rotate(-1.5deg)">
<div class="hand" style="position:absolute;left:50px;top:30px;font-size:52px;opacity:.75">¿Cuánto te ha costado?</div>
{scale(50, 180)}
</div>
<div style="position:absolute;left:90px;top:930px;width:900px"><h1 style="font-size:80px">¿Les preguntas cuánto <em>les ha costado?</em></h1></div>
{opt('Lo pregunto', 1300)}{opt('Lo intuyo', 1480)}
<div class="tag" style="left:140px;top:1670px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in S.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(S))
