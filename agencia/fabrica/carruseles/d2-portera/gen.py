# Genera las láminas del carrusel y las Stories de d2-portera «Paró doce y fue su mejor partido» (Clara, 23/11)
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

def tally(x, y, n, col=INK, h=70, gap=17):
    """Palotes a lápiz, en grupos de cinco (cuatro rayas y una cruzada)."""
    out = ''; cx = x
    full, rest = divmod(n, 5)
    groups = [5]*full + ([rest] if rest else [])
    for g in groups:
        w = 4*gap + 20
        paths = ''
        for i in range(min(g, 4)):
            px = 10 + i*gap
            paths += f'<path d="M{px} 6 L{px+2} {h-4}" />'
        if g == 5:
            paths += f'<path d="M0 {h-14} L{w} 14" />'
        out += f'<svg style="left:{cx}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{PENCIL}<g filter="url(#pen)" stroke="{col}" stroke-width="6" fill="none" stroke-linecap="round">{paths}</g></svg>'
        cx += w + 24
    return out

N = 6
txt = lambda h, sub='', top=1010: f'<div style="position:absolute;left:90px;top:{top}px;width:900px"><h2>{h}</h2>' + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>'
num = lambda i: f'<div class="n">{i}/{N}</div>'
lab = lambda t, x=50, y=34: f'<div style="position:absolute;left:{x}px;top:{y}px;font-weight:700;font-size:22px;letter-spacing:.16em;opacity:.45">{t}</div>'
S = {}

# 1 · portada (titular: 7 palabras)
S['c1'] = page(f'''
<div class="k">Balonmano · la portera</div>
{photo('portera.jpg', 150, 280, 740, 494, -2, pos='60% 30%')}
<div style="position:absolute;left:90px;top:1000px;width:900px"><h1>Le marcaron veinte. <em>Fue su mejor partido.</em></h1></div>
<div class="foot">DESLIZA →</div>''')

# 2 · problema: marcador (EJEMPLO)
S['c2'] = page(f'''
<div class="k">El problema</div>{num(2)}
<div class="frame" style="left:150px;top:300px;width:780px;height:420px;transform:rotate(-1.5deg)">
{lab('SÁBADO · FINAL · EJEMPLO')}
<div style="position:absolute;left:0;top:110px;width:780px;text-align:center;font-weight:800;font-size:190px;letter-spacing:-.04em;line-height:1">14<span style="opacity:.3"> – </span><span style="color:{RED}">20</span></div>
{underline(470, 320, 210, RED)}
</div>
{txt('Perdéis de seis y en el vestuario <em>nadie la mira.</em>', 'Tú ves el 20. Ella también.')}''')

# 3 · paso 1: cuenta tiros
S['c3'] = page(f'''
<div class="k">Paso 1 · durante el partido</div>{num(3)}
<div class="frame" style="left:100px;top:290px;width:880px;height:480px;transform:rotate(-1deg)">
{lab('HOJA DE LA PORTERA · EJEMPLO')}
<div class="hand" style="position:absolute;left:50px;top:105px;font-size:50px;opacity:.8">Paradas</div>
{tally(260, 100, 12, BLUE)}
<div style="position:absolute;right:50px;top:105px;font-weight:800;font-size:52px;color:{BLUE}">12</div>
<div class="hand" style="position:absolute;left:50px;top:235px;font-size:50px;opacity:.8">Goles</div>
{tally(260, 230, 20)}
<div style="position:absolute;right:50px;top:235px;font-weight:800;font-size:52px">20</div>
<div style="position:absolute;left:50px;top:350px;width:780px;border-top:3px solid rgba(18,18,18,.15)"></div>
<div class="hand" style="position:absolute;left:50px;top:375px;font-size:50px">Tiros a portería</div>
<div style="position:absolute;right:50px;top:375px;font-weight:800;font-size:52px">32</div>
</div>
{txt('Cuenta tiros, <em>no goles.</em>', 'Una raya por parada y otra por gol.')}''')

# 4 · paso 2: la cuenta
S['c4'] = page(f'''
<div class="k">Paso 2 · la cuenta</div>{num(4)}
<div class="frame" style="left:140px;top:300px;width:800px;height:440px;transform:rotate(1.2deg)">
{lab('PARADAS ÷ TIROS · EJEMPLO', 56, 40)}
<div style="position:absolute;left:56px;top:110px;font-weight:800;font-size:120px;letter-spacing:-.03em;line-height:1"><span style="color:{BLUE}">12</span> ÷ 32</div>
<div style="position:absolute;left:56px;top:270px;font-weight:800;font-size:110px;letter-spacing:-.03em;line-height:1">= 37,5 %</div>
{underline(60, 385, 460)}
</div>
{txt('Paradas entre tiros. <em>Cada partido, igual.</em>', 'Siempre el mismo cálculo, para poder compararlo.')}''')

# 5 · paso 3: el lunes, a ella (barras EJEMPLO)
J = [('J1', 28), ('J2', 31), ('J3', 30), ('J4', 37.5)]
bars = ''
for i, (j, v) in enumerate(J):
    hpx = int(v * 7.5); x0 = 80 + i*185; best = (i == 3)
    bars += f'<div style="position:absolute;left:{x0}px;bottom:90px;width:110px;height:{hpx}px;background:{BLUE};opacity:{1 if best else .35};border-radius:10px 10px 0 0"></div>'
    vs = (f'{v:.1f}'.replace('.', ',') if v % 1 else f'{int(v)}') + ' %'
    bars += f'<div style="position:absolute;left:{x0-20}px;bottom:{100+hpx}px;width:150px;text-align:center;font-weight:800;font-size:32px;opacity:{1 if best else .55}">{vs}</div>'
    bars += f'<div style="position:absolute;left:{x0}px;bottom:40px;width:110px;text-align:center;font-weight:700;font-size:24px;letter-spacing:.12em;opacity:.5">{j}</div>'
S['c5'] = page(f'''
<div class="k">Paso 3 · el lunes</div>{num(5)}
<div class="frame" style="left:150px;top:280px;width:780px;height:500px;transform:rotate(-1deg)">
{lab('PARADAS ÷ TIROS POR JORNADA · EJEMPLO')}
{bars}
</div>
{txt('El lunes, se lo enseñas <em>a ella antes que a nadie.</em>', 'El 20 era mentira: fue su mejor porcentaje.')}''')

# 6 · resumen
rows = [('1', 'Una raya por parada y por gol.'), ('2', 'Paradas ÷ tiros.'), ('3', 'Cada partido, igual.'), ('4', 'El lunes, a ella primero.')]
lis = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin-bottom:38px"><span style="font-weight:800;font-size:34px;color:{BLUE};width:40px">{a}</span><span style="font-weight:700;font-size:50px;letter-spacing:-.01em">{b}</span></div>' for a, b in rows)
S['c6'] = page(f'''
<div class="k">Resumen · la portera</div>{num(6)}
<div style="position:absolute;left:90px;top:330px;width:900px">{lis}</div>
<div style="position:absolute;left:90px;top:960px;width:900px"><h2 style="font-size:76px"><em>Guárdalo</em> y pásaselo a tu segundo.</h2></div>
<div class="foot" style="text-transform:none;letter-spacing:.04em;font-weight:500;font-size:24px">Cifras de ejemplo. Fotos: Steffen Prößdorf (CC BY-SA 4.0)</div>''')

# Stories
S['s1'] = page(f'''
<div class="k" style="top:260px">Pregunta · balonmano</div>
{photo('lanzadora.jpg', 160, 400, 712, 475, -2)}
<div style="position:absolute;left:90px;top:1040px;width:900px"><h1 style="font-size:84px">¿Cuántos tiros paró tu portera <em>el sábado?</em></h1></div>
<div style="position:absolute;left:140px;top:1470px;width:800px;height:200px;border:3px dashed rgba(18,18,18,.22);border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;letter-spacing:.16em;color:rgba(18,18,18,.35)">HUECO PARA EL STICKER DE PREGUNTA</div>''', story=True)
opt = lambda t, top: f'<div style="position:absolute;left:140px;top:{top}px;width:800px;height:150px;background:#fff;border-radius:30px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 20px 50px rgba(30,25,15,.10);display:flex;align-items:center;padding-left:56px;font-weight:800;font-size:44px">{t}</div>'
S['s2'] = page(f'''
<div class="k" style="top:260px">Encuesta · balonmano</div>
<div class="frame" style="left:110px;top:420px;width:860px;height:340px;transform:rotate(-1.5deg)">
{lab('EJEMPLO')}
<div style="position:absolute;left:0;top:90px;width:860px;text-align:center;font-weight:800;font-size:150px;letter-spacing:-.04em;line-height:1"><span style="color:{BLUE}">12</span><span style="opacity:.3"> / </span>20</div>
<div class="hand" style="position:absolute;left:0;top:250px;width:860px;text-align:center;font-size:44px;opacity:.7">paradas <span style="opacity:.4">y</span> goles</div>
</div>
<div style="position:absolute;left:90px;top:930px;width:900px"><h1 style="font-size:80px">¿Qué cuentas de <em>tu portera?</em></h1></div>
{opt('Los goles que encaja', 1300)}{opt('Los tiros que para', 1480)}
<div class="tag" style="left:140px;top:1670px">HUECO PARA EL STICKER DE ENCUESTA</div>''', story=True)

for k, v in S.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print('ok', list(S))
