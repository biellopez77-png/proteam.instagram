"""Genera las Stories de cocreación, encuestas, Club Fundador e imagen para compartir (20/11)."""
import os, math
H=os.path.dirname(os.path.abspath(__file__))
def badge(c1='#2f6bff',c2='#1b46c9',size=420,num=None,glow=True):
    # roseta de verificado: 12 lóbulos
    pts=[];n=12;R=100;r=88
    for i in range(n*2):
        a=math.pi*i/n-math.pi/2; rr=R if i%2==0 else r
        pts.append(f"{110+rr*math.cos(a):.1f},{110+rr*math.sin(a):.1f}")
    numtxt=f'<text x="110" y="196" text-anchor="middle" font-family="M" font-weight="800" font-size="20" fill="#fff" opacity=".9">{num}</text>' if num else ''
    g=f'filter:drop-shadow(0 0 60px {c1}88)' if glow else ''
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 220 220" style="{g}"><defs><linearGradient id="g{c1[1:]}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
<polygon points="{' '.join(pts)}" fill="url(#g{c1[1:]})"/><circle cx="110" cy="110" r="70" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/>
<image href="mark-w.png" x="70" y="66" width="80" height="80"/>{numtxt}</svg>'''
HEAD='<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>{}</style></head><body>'
CSS='''.q{position:absolute;left:90px;right:90px;top:250px}.q .k{margin-bottom:26px}.q h1{font-size:70px}
.cmp{position:absolute;left:90px;right:90px;top:640px;display:grid;grid-template-columns:1fr 1fr;gap:40px}
.cmp .o{display:flex;flex-direction:column;align-items:center;gap:22px}
.tag{font-weight:800;font-size:36px}.tag i{font-style:normal;display:inline-flex;width:58px;height:58px;border-radius:50%;background:#2f6bff;color:#fff;align-items:center;justify-content:center;margin-right:14px;font-size:30px}
.ph{width:300px;height:420px;border-radius:38px;overflow:hidden;border:6px solid #262b36;background:#fff;position:relative}
.ph img{width:100%;display:block}
.wf{width:300px;height:420px;border-radius:38px;border:6px solid #262b36;background:#f4f5f8;position:relative;overflow:hidden}
.bar{position:absolute;background:#d9dde6;border-radius:8px}
.blue{background:#2f6bff!important}
.hole{position:absolute;left:0;right:0;top:1060px;height:560px}
'''
def page(name,body,extra=''):
    open(os.path.join(H,name+'.html'),'w').write(HEAD.format(CSS+extra)+body+'</body></html>')
# 1 · intro
page('s1','''<div class="s dark"><div style="position:absolute;left:50%;top:430px;transform:translateX(-50%);width:760px;height:760px;border-radius:50%;background:radial-gradient(circle,#2f6bff55,#2f6bff00 70%)"></div>
<img src="proteam-mark.webp" style="position:absolute;left:50%;top:560px;transform:translateX(-50%);width:420px">
<div class="in" style="justify-content:flex-end"><h1 style="font-size:132px;letter-spacing:-.04em">Entrenador,<br><span class="sr" style="letter-spacing:0">te necesitamos.</span></h1></div></div>''')
page('s2','''<div class="s paper"><div class="in"><div class="k">ProTeam · la app para entrenadores</div>
<h1 style="font-size:116px;margin-top:40px;letter-spacing:-.03em">Queremos construir ProTeam <span class="sr" style="letter-spacing:0">contigo.</span></h1>
<div class="sm" style="font-size:44px;margin-top:50px;color:#3a4150">Cinco preguntas rápidas.<br>Tu opinión nos ayuda a decidir.</div>
<div style="margin-top:auto;display:flex;align-items:center;gap:26px;font-weight:800;font-size:40px">Toca para empezar <svg width="120" height="40" viewBox="0 0 120 40"><path d="M0 20h108M90 4l18 16-18 16" stroke="#2f6bff" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div></div>''')
# encuestas
def poll(name,num,q,cmp):
    page(name,f'''<div class="s dark"><div class="q"><div class="k">Pregunta {num} de 5</div><h1>{q}</h1></div><div class="cmp">{cmp}</div><div class="hole"></div></div>''')
poll('p1',1,'¿Qué combinación de colores prefieres?','''
<div class="o"><div class="ph"><img src="mo-home.jpg"></div><div class="tag"><i>A</i>La actual</div></div>
<div class="o"><div class="ph"><img src="mo-home.jpg" style="filter:hue-rotate(38deg) saturate(.9)"></div><div class="tag"><i style="background:#7a5cff">B</i>Con lila</div></div>''')
side='''<div class="wf"><div class="bar" style="left:0;top:0;bottom:0;width:96px;border-radius:0;background:#1b1f29"></div>
'''+''.join(f'<div class="bar" style="left:24px;top:{60+i*62}px;width:48px;height:22px;background:{"#2f6bff" if i==0 else "#3c4352"}"></div>' for i in range(5))+''.join(f'<div class="bar" style="left:120px;top:{60+i*70}px;width:{140-i%2*40}px;height:40px"></div>' for i in range(5))+'</div>'
bottom='<div class="wf">'+''.join(f'<div class="bar" style="left:28px;top:{50+i*70}px;width:{230-i%2*60}px;height:40px"></div>' for i in range(4))+'<div class="bar" style="left:0;right:0;bottom:0;height:78px;border-radius:0;background:#1b1f29"></div>'+''.join(f'<div class="bar" style="left:{30+i*52}px;bottom:26px;width:28px;height:28px;border-radius:50%;background:{"#2f6bff" if i==0 else "#3c4352"}"></div>' for i in range(5))+'</div>'
poll('p2',2,'¿Cómo prefieres navegar por la app?',f'<div class="o">{side}<div class="tag"><i>A</i>Menú lateral</div></div><div class="o">{bottom}<div class="tag"><i>B</i>Menú inferior</div></div>')
poll('p3',3,'¿Qué color prefieres para la insignia del Club Fundador?',
 '<div style="grid-column:1/3;display:flex;justify-content:space-between">'+''.join(f'<div class="o">{badge(a,b,260,glow=False)}<div class="tag"><i style="background:{a}">{l}</i>{n}</div></div>' for a,b,l,n in [('#2f6bff','#1b46c9','A','Azul'),('#d9a632','#a8751a','B','Oro'),('#7a5cff','#5536d6','C','Lila')])+'</div><div class="sm" style="grid-column:1/3;color:#8d93a1;font-size:28px;text-align:center">Diseño provisional</div>')
search='<div class="wf"><div class="bar" style="left:24px;right:24px;top:40px;height:58px;border-radius:30px;background:#fff;border:3px solid #2f6bff"></div><svg style="position:absolute;left:44px;top:56px" width="28" height="28" viewBox="0 0 28 28"><circle cx="12" cy="12" r="8" stroke="#2f6bff" stroke-width="4" fill="none"/><path d="M18 18l7 7" stroke="#2f6bff" stroke-width="4" stroke-linecap="round"/></svg>'+''.join(f'<div class="bar" style="left:24px;top:{130+i*62}px;width:{240-i%3*50}px;height:36px"></div>' for i in range(4))+'</div>'
filt='<div class="wf">'+''.join(f'<div class="bar" style="left:{24+i*92}px;top:40px;width:80px;height:46px;border-radius:24px;{"background:#2f6bff" if i==0 else "background:#fff;border:3px solid #c7ccd6"}"></div>' for i in range(3))+''.join(f'<div class="bar" style="left:{24+i*120}px;top:100px;width:{100}px;height:40px;border-radius:22px;background:#fff;border:3px solid #c7ccd6"></div>' for i in range(2))+''.join(f'<div class="bar" style="left:24px;top:{170+i*58}px;width:{240-i%3*50}px;height:34px"></div>' for i in range(4))+'</div>'
poll('p4',4,'¿Qué prefieres para encontrar jugadores, datos o ejercicios?',f'<div class="o">{search}<div class="tag"><i>A</i>Buscador</div></div><div class="o">{filt}<div class="tag"><i>B</i>Filtros</div></div>')
chart='<div class="wf" style="background:#fff">'+''.join(f'<div class="bar blue" style="left:{40+i*46}px;bottom:70px;width:30px;height:{h}px;opacity:{.45+i*.1}"></div>' for i,h in enumerate([90,150,120,210,170]))+'<svg style="position:absolute;left:20px;top:40px" width="250" height="120" viewBox="0 0 250 120"><path d="M0 100 C60 90 90 30 140 50 S220 10 250 20" stroke="#2f6bff" stroke-width="6" fill="none"/></svg></div>'
data='<div class="wf" style="background:#fff">'+''.join(f'<div style="position:absolute;left:26px;right:26px;top:{40+i*70}px;display:flex;justify-content:space-between;font-weight:800;font-size:26px;color:#0d0f14;border-bottom:2px solid #e4e7ee;padding-bottom:16px"><span style="color:#6b7385;font-weight:700">{k}</span><span>{v}</span></div>' for i,(k,v) in enumerate([('Minutos','412'),('Sesiones','18'),('RPE medio','6,2'),('Asistencia','94 %'),('Partidos','7')]))+'</div>'
poll('p5',5,'¿Cómo prefieres consultar la información?',f'<div class="o">{chart}<div class="tag"><i>A</i>Más visual</div></div><div class="o">{data}<div class="tag"><i>B</i>Más datos</div></div>')
# Imagen para compartir (la sube el usuario) y anuncio de ProTeam
page('share','''<div class="s dark"><div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 38%,#2f6bff40,#0d0f1400 55%)"></div>
<div style="position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center">'''+badge(size=520,num='CLUB FUNDADOR')+'''</div>
<div class="in" style="top:930px;align-items:center;text-align:center"><h1 style="font-size:104px;letter-spacing:-.03em">¡Ya estoy <span class="sr" style="letter-spacing:0">dentro!</span></h1>
<div class="sm" style="font-size:44px;margin-top:34px;color:#c9ccd4">Formo parte del Club Fundador de ProTeam,<br>la app para entrenadores.</div>
<div style="margin-top:auto;font-weight:800;font-size:46px">@app.proteam</div><div class="sm" style="color:#8d93a1;margin-top:10px">pro-team.app</div></div></div>''')
page('anuncio','''<div class="s paper"><div class="in"><div class="k">Lista de espera</div>
<h1 style="font-size:104px;margin-top:36px;letter-spacing:-.03em">¡Ya estás dentro de la lista de espera de <span class="sr" style="letter-spacing:0">ProTeam!</span></h1>
<div style="display:flex;align-items:center;gap:40px;margin-top:70px">'''+badge(size=300,glow=False)+'''<div class="sm" style="font-size:44px;font-weight:700">Ahora, consigue tu insignia del <b style="color:#2f6bff">Club Fundador.</b></div></div>
<div class="sm" style="margin-top:60px;font-size:40px;color:#3a4150">Entra desde el enlace de la bio, comparte tu imagen en una historia y menciónanos.</div>
<div style="margin-top:auto;font-weight:800;font-size:40px">Enlace en la bio →</div></div></div>''')
# Presentación del Club Fundador (sin precio ni condiciones sin aprobar)
ben=[('Insignia verificada y numerada','Con tu número de fundador.'),('3 meses gratis','Para la lista de espera.'),('Soporte de tú a tú','Te acompañamos los 3 meses.'),('Tu voz en ProTeam','Votaciones solo para fundadores.'),('3 tickets regalo','Para tus amigos. Pronto, más.'),('Precio fundador','Condiciones muy pronto.')]
page('club','''<div class="s dark"><div class="in" style="top:230px"><div style="display:flex;align-items:center;gap:30px">'''+badge(size=170,glow=False)+'''<h1 style="font-size:84px;letter-spacing:-.03em">Club <span class="sr" style="letter-spacing:0">Fundador</span></h1></div>
<div style="margin-top:50px">'''+''.join(f'<div class="ln"><div class="n">{i+1}</div><div><div class="t">{t}</div><div class="sm" style="color:#8d93a1;font-size:32px;margin-top:6px">{d}</div></div></div>' for i,(t,d) in enumerate(ben))+'''</div>
<div style="margin-top:auto;font-weight:800;font-size:40px">Lista de espera hasta el 27 · enlace en la bio</div></div></div>''')
