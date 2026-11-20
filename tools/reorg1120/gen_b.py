"""Club Fundador y lista de espera, una idea por Story (20/11, Clara). Borradores para aprobación de Biel.
python3 tools/reorg1120/gen_b.py && python3 tools/reorg1120/render.py b1 b2 b3"""
import os
H=os.path.dirname(os.path.abspath(__file__))
ROS="110.0,10.0 132.8,25.0 160.0,23.4 172.2,47.8 196.6,60.0 195.0,87.2 210.0,110.0 195.0,132.8 196.6,160.0 172.2,172.2 160.0,196.6 132.8,195.0 110.0,210.0 87.2,195.0 60.0,196.6 47.8,172.2 23.4,160.0 25.0,132.8 10.0,110.0 25.0,87.2 23.4,60.0 47.8,47.8 60.0,23.4 87.2,25.0"
def page(n,b,css=''): open(os.path.join(H,n+'.html'),'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>{css}</style></head><body>{b}</body></html>')
FOOT='<div style="margin-top:auto;font-weight:800;font-size:40px">Club Fundador · pro-team.app</div>'
# b1 · Insignia con tu número (el número va en blanco: nadie tiene número todavía)
page('b1',f'''<div class="s dark"><div style="position:absolute;inset:0;background:radial-gradient(circle at 30% 30%,#2f6bff38,#0d0f1400 55%)"></div>
<div class="in"><svg width="520" height="520" viewBox="0 0 220 220" aria-hidden="true" style="margin-left:-24px"><polygon points="{ROS}" fill="#2f6bff"/>
<text x="110" y="100" text-anchor="middle" font-family="M" font-weight="800" font-size="22" fill="#fff" opacity=".8" letter-spacing="3">FUNDADOR</text>
<text x="110" y="150" text-anchor="middle" font-family="M" font-weight="800" font-size="50" fill="#fff">Nº __</text></svg>
<div class="k" style="margin-top:60px">Club Fundador</div>
<h1 style="font-size:104px;margin-top:24px;letter-spacing:-.03em">Tu insignia.<br><span class="sr" style="letter-spacing:0">Tu número.</span></h1>
<div class="sm" style="font-size:44px;margin-top:40px;color:#c9ccd4">Cada entrenador fundador de ProTeam, la app para entrenadores, tendrá la suya.</div>{FOOT}</div></div>''')
# b2 · Lista de espera: 3 meses gratis hasta el 27
page('b2',f'''<div class="s paper"><div class="in"><div class="k">Lista de espera</div>
<div style="font-weight:800;font-size:620px;line-height:.86;letter-spacing:-.06em;color:#2f6bff;margin:30px 0 0 -30px">3</div>
<h1 style="font-size:112px;letter-spacing:-.03em;margin-top:10px">meses <span class="sr" style="letter-spacing:0">gratis.</span></h1>
<div class="sm" style="font-size:44px;margin-top:40px;color:#3a4150">Si entras en la lista de espera de ProTeam hasta el 27 de noviembre.</div>
<div style="margin-top:auto;font-weight:800;font-size:40px">Abrimos el sábado 28 · pro-team.app</div></div></div>''')
# b3 · Votaciones: una pregunta, dos barras (dibujo, sin porcentajes: no hay resultados todavía)
CSS='.bar{height:120px;border-radius:26px;display:flex;align-items:center;padding:0 40px;font-weight:800;font-size:46px;margin-top:26px}'
page('b3',f'''<div class="s dark"><div class="in"><div class="k">Club Fundador</div>
<h1 style="font-size:104px;margin-top:24px;letter-spacing:-.03em">Votas en lo que <span class="sr" style="letter-spacing:0">construimos.</span></h1>
<div style="margin-top:90px"><div class="bar" style="background:#2f6bff;width:100%">A</div><div class="bar" style="background:#1b2030;border:2px solid #262b36;width:72%">B</div></div>
<div class="sm" style="font-size:44px;margin-top:70px;color:#c9ccd4">Antes de decidir, preguntamos a los entrenadores fundadores.</div>{FOOT}</div></div>''',CSS)
