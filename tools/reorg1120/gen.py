"""Stories informativas tras la suspensión de Instagram (20/11). HANDLE = cuenta provisional (pendiente de Biel)."""
import os, sys
H=os.path.dirname(os.path.abspath(__file__))
HANDLE=os.environ.get('HANDLE','@cuenta_provisional')
ROS="110.0,10.0 132.8,25.0 160.0,23.4 172.2,47.8 196.6,60.0 195.0,87.2 210.0,110.0 195.0,132.8 196.6,160.0 172.2,172.2 160.0,196.6 132.8,195.0 110.0,210.0 87.2,195.0 60.0,196.6 47.8,172.2 23.4,160.0 25.0,132.8 10.0,110.0 25.0,87.2 23.4,60.0 47.8,47.8 60.0,23.4 87.2,25.0"
def badge(s): return f'<svg width="{s}" height="{s}" viewBox="0 0 220 220" aria-hidden="true"><polygon points="{ROS}" fill="#2f6bff"/><path d="M78 112l22 22 44-48" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CSS='.handle{display:inline-block;padding:14px 26px;border-radius:999px;background:#2f6bff;color:#fff;font-weight:800;font-size:44px}'
def page(n,b): open(os.path.join(H,n+'.html'),'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>{CSS}</style></head><body>{b}</body></html>')
# 1 · Qué ha pasado (una idea: seguimos aquí)
page('r1',f'''<div class="s dark"><img src="proteam-mark.webp" style="position:absolute;left:90px;top:250px;width:120px">
<div class="in" style="justify-content:center"><h1 style="font-size:104px;letter-spacing:-.03em">Seguimos <span class="sr" style="letter-spacing:0">aquí.</span></h1>
<div class="sm" style="font-size:44px;margin-top:40px;color:#c9ccd4;line-height:1.4">Instagram ha suspendido nuestra cuenta. Ya lo estamos resolviendo.</div>
<div class="sm" style="font-size:44px;margin-top:30px;color:#c9ccd4;line-height:1.4">Mientras tanto, nos encuentras aquí.</div></div></div>''')
# 2 · La cuenta provisional
page('r2',f'''<div class="s paper"><div class="in" style="justify-content:center;align-items:flex-start">{badge(200)}
<div class="k" style="margin-top:50px">Cuenta provisional</div>
<h1 style="font-size:96px;margin-top:20px;letter-spacing:-.03em">Club Fundador <span class="sr" style="letter-spacing:0">ProTeam</span></h1>
<div class="sm" style="font-size:42px;margin-top:36px;color:#3a4150;line-height:1.4">El sitio de los primeros entrenadores de ProTeam, mientras recuperamos la cuenta.</div>
<div style="margin-top:50px"><span class="handle">{HANDLE}</span></div></div></div>''')
# 3 · Nada cambia
rows=[('Lista de espera','Abierta hasta el 27 de noviembre'),('3 meses gratis','Para quien entra en la lista'),('Lanzamiento','Sábado 28 de noviembre')]
page('r3','''<div class="s dark"><div class="in"><div class="k">Lo importante</div><h1 style="font-size:100px;margin-top:30px;letter-spacing:-.03em">Nada <span class="sr" style="letter-spacing:0">cambia.</span></h1>
<div style="margin-top:70px">'''+''.join(f'<div class="ln"><div class="n">{i+1}</div><div><div class="t">{a}</div><div class="sm" style="color:#8d93a1;font-size:34px;margin-top:6px">{b}</div></div></div>' for i,(a,b) in enumerate(rows))+'''</div>
<div style="margin-top:auto;font-weight:800;font-size:44px">pro-team.app</div></div></div>''')
# 4 · Club Fundador sin precio fundador (solo lo confirmado)
ben=[('Insignia numerada','Con tu número de fundador.'),('3 meses gratis','Para la lista de espera.'),('Soporte de tú a tú','Te acompañamos en la prueba.'),('Tu voz en ProTeam','Votaciones para fundadores.'),('Invitaciones para amigos','Muy pronto, los detalles.')]
page('r4',f'''<div class="s dark"><div class="in" style="top:230px"><div style="display:flex;align-items:center;gap:30px">{badge(170)}<h1 style="font-size:84px;letter-spacing:-.03em">Club <span class="sr" style="letter-spacing:0">Fundador</span></h1></div>
<div style="margin-top:50px">'''+''.join(f'<div class="ln"><div class="n">{i+1}</div><div><div class="t">{t}</div><div class="sm" style="color:#8d93a1;font-size:32px;margin-top:6px">{d}</div></div></div>' for i,(t,d) in enumerate(ben))+'''</div>
<div style="margin-top:auto;font-weight:800;font-size:40px">Lista de espera hasta el 27 · pro-team.app</div></div></div>''')
