"""Pack de gráficos para los vídeos POV (fondo transparente, 1080x1920). Cada gráfico entra animado (0,5 s) y se queda."""
import os
H=os.path.dirname(os.path.abspath(__file__))
ROS="110.0,10.0 132.8,25.0 160.0,23.4 172.2,47.8 196.6,60.0 195.0,87.2 210.0,110.0 195.0,132.8 196.6,160.0 172.2,172.2 160.0,196.6 132.8,195.0 110.0,210.0 87.2,195.0 60.0,196.6 47.8,172.2 23.4,160.0 25.0,132.8 10.0,110.0 25.0,87.2 23.4,60.0 47.8,47.8 60.0,23.4 87.2,25.0"
CSS='''html,body{background:transparent}.s{background:transparent}
.card{position:absolute;background:rgba(13,15,20,.86);backdrop-filter:blur(18px);border-radius:34px;color:#f5f5f3;padding:36px 40px;box-shadow:0 30px 80px rgba(0,0,0,.35)}
.lt{background:#fff;color:#0d0f14}
.ap{animation:ap .5s cubic-bezier(.2,1.2,.4,1) both}.d1{animation-delay:.12s}.d2{animation-delay:.24s}.d3{animation-delay:.36s}.d4{animation-delay:.48s}.d5{animation-delay:.6s}
@keyframes ap{from{opacity:0;transform:translateY(40px) scale(.94)}to{opacity:1;transform:none}}
.chip{display:inline-flex;align-items:center;gap:18px;padding:18px 28px;border-radius:999px;background:rgba(13,15,20,.86);color:#fff;font-weight:800;font-size:40px}
.chip b{width:58px;height:58px;border-radius:50%;background:#2f6bff;display:flex;align-items:center;justify-content:center;font-size:30px}
.cell{border:2px solid #2a303c;padding:10px 14px;font-size:24px;font-weight:700;color:#c9ccd4}
'''
def page(name,body):
    open(os.path.join(H,name+'.html'),'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>{CSS}</style></head><body><div class="s">{body}</div></body></html>')
# G01 Excel caótico
rows=''.join('<tr>'+''.join(f'<td class="cell" style="{"background:#3a1d1d;color:#ff8a8a" if (r*3+c)%7==0 else ""}">{t}</td>' for c,t in enumerate(v))+'</tr>' for r,v in enumerate([['Jugador','Min','RPE','Asist.'],['Marc','62','?','✓'],['Pau','—','7','✗'],['Nil','45','6','?'],['Arnau','??','—','✓'],['Joel','30','8','✓']]))
page('g01-excel',f'<div class="card ap" style="left:90px;right:90px;top:380px"><div class="k" style="margin-bottom:20px">ENTRENO_v7_FINAL(2).xlsx</div><table style="border-collapse:collapse;width:100%">{rows}</table></div>')
# G02 calendario semana con huecos
days=['L','M','X','J','V','S','D']
cal=''.join(f'<div class="ap d{min(i,5)}" style="border-radius:22px;padding:20px 0;text-align:center;background:{"#2f6bff" if i in (1,3,5) else "rgba(255,255,255,.08)"};font-weight:800;font-size:40px">{d}<div style="font-size:22px;font-weight:700;margin-top:10px;color:#dfe6ff">{"Entreno" if i in (1,3) else ("Partido" if i==5 else "·")}</div></div>' for i,d in enumerate(days))
page('g02-semana',f'<div class="card ap" style="left:70px;right:70px;top:420px"><div class="k" style="margin-bottom:24px">TU SEMANA</div><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:12px">{cal}</div></div>')
# G03 WhatsApp
bub=''.join(f'<div class="ap d{i+1}" style="align-self:{a};max-width:78%;padding:20px 26px;border-radius:28px;background:{bg};color:{fg};font-size:34px;font-weight:600">{t}</div>' for i,(t,a,bg,fg) in enumerate([('¿Mañana a qué hora es?','flex-start','#fff','#0d0f14'),('¿Quién juega el sábado?','flex-start','#fff','#0d0f14'),('No me llegó la convocatoria 🙃','flex-start','#fff','#0d0f14'),('Ahora lo paso 🙏','flex-end','#d9fdd3','#0d0f14')]))
page('g03-whatsapp',f'<div class="ap" style="position:absolute;left:90px;right:90px;top:520px;display:flex;flex-direction:column;gap:16px">{bub}</div>')
# G04 cuatro sitios → uno
items=['Libreta','Excel','WhatsApp','Pizarra']
g04=''.join(f'<span class="chip ap d{i+1}"><b>{i+1}</b>{t}</span>' for i,t in enumerate(items))
page('g04-cuatro-sitios',f'<div style="position:absolute;left:90px;right:90px;top:520px;display:flex;flex-direction:column;gap:22px;align-items:flex-start">{g04}<div class="ap d5" style="margin-top:30px;font-weight:800;font-size:64px;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.6)">4 sitios. <span class="sr">1 equipo.</span></div></div>')
# G05 esquema de planificación
lv=[('Temporada','Objetivos y fases'),('Mesociclo','4 semanas con un foco'),('Semana','Sesiones, partido y carga'),('Sesión','Tareas con minutos')]
g05=''.join(f'<div class="ap d{i+1}" style="margin-left:{i*50}px;padding:22px 30px;border-radius:24px;background:{"#2f6bff" if i==2 else "rgba(13,15,20,.86)"};color:#fff"><div style="font-weight:800;font-size:40px">{a}</div><div style="font-size:26px;color:#dfe6ff;margin-top:6px">{b}</div></div>' for i,(a,b) in enumerate(lv))
page('g05-planificacion',f'<div style="position:absolute;left:80px;right:80px;top:440px;display:flex;flex-direction:column;gap:18px">{g05}</div>')
# G06 contador de dedos (ventajas) — se colocan junto a la mano
for n,(t) in enumerate(['Insignia numerada','3 meses gratis','Soporte de tú a tú','Tu voz en ProTeam','3 tickets regalo'],1):
    page(f'g06-dedo{n}',f'<div style="position:absolute;right:80px;top:{560+n*0}px"><span class="chip ap"><b>{n}</b>{t}</span></div>')
# G07 insignia + número
page('g07-insignia',f'''<div class="ap" style="position:absolute;left:0;right:0;top:520px;display:flex;flex-direction:column;align-items:center;gap:24px"><svg width="420" height="420" viewBox="0 0 220 220" style="filter:drop-shadow(0 0 60px #2f6bffaa)"><polygon points="{ROS}" fill="#2f6bff"/><circle cx="110" cy="110" r="70" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/><path d="M78 112l22 22 44-48" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="chip">Club Fundador</span></div>''')
# G08 tarjeta comparativa antes/después
page('g08-antes-despues','''<div style="position:absolute;left:70px;right:70px;top:460px;display:grid;grid-template-columns:1fr 1fr;gap:20px"><div class="card ap" style="position:relative;padding:30px"><div class="k" style="color:#ff8a8a">ANTES</div><div style="font-size:30px;font-weight:700;line-height:1.5;margin-top:14px">Libreta<br>Excel<br>WhatsApp<br>Pizarra<br>Domingo noche</div></div><div class="card ap d2" style="position:relative;padding:30px;background:rgba(47,107,255,.92)"><div class="k" style="color:#fff">AHORA</div><div style="font-size:30px;font-weight:700;line-height:1.5;margin-top:14px">Semana<br>Convocatoria<br>Partido<br>Carga<br>En un sitio</div></div></div>''')
# G09 cierre CTA
page('g09-cta','''<div class="card lt ap" style="left:90px;right:90px;bottom:360px;text-align:center"><div style="font-weight:800;font-size:54px;line-height:1.1">Lista de espera <span class="sr">hasta el 27</span></div><div class="sm" style="margin-top:14px;color:#3a4150">3 meses gratis · enlace en la bio</div></div>''')
# G10 subtítulo palabra clave (plantilla)
page('g10-palabra','''<div class="ap" style="position:absolute;left:0;right:0;top:1180px;text-align:center"><span style="display:inline-block;padding:14px 30px;border-radius:18px;background:#2f6bff;color:#fff;font-weight:800;font-size:64px">PALABRA</span></div>''')
