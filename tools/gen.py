import asyncio, os, json
from playwright.async_api import async_playwright
B = '/home/claude/feed'; A = '/home/claude/m2'
os.makedirs(f'{B}/out', exist_ok=True)
for f in ('fonts', 'proteam-mark.webp'):
    if not os.path.exists(f'{B}/{f}'): os.symlink(f'{A}/{f}', f'{B}/{f}')
if not os.path.exists(f'{B}/app'): os.symlink(f'{A}/out/rb2/app', f'{B}/app')
os.makedirs(f'{B}/cov', exist_ok=True)

CSS = '''
@font-face{font-family:M;font-weight:600;src:url(fonts/manrope-latin-700-normal.woff2)}
@font-face{font-family:M;font-weight:800;src:url(fonts/manrope-latin-800-normal.woff2)}
@font-face{font-family:M;font-weight:500;src:url(fonts/manrope-latin-500-normal.woff2)}
@font-face{font-family:S;font-style:italic;src:url(fonts/instrument-serif-latin-400-italic.woff2)}
@font-face{font-family:P;font-weight:500;src:url(fonts/ibm-plex-mono-latin-500-normal.woff2)}
:root{--ink:#0d0f14;--blue:#2f6bff;--mute:#8a8f9c;--soft:#e9efff}
*{box-sizing:border-box}html,body{margin:0}
.st{position:relative;overflow:hidden;background:#fff;font-family:M;color:var(--ink)}
.st.bl{background:var(--blue);color:#fff}
.dots{position:absolute;inset:0;background-image:radial-gradient(circle,#d9dde5 2.4px,transparent 2.6px);background-size:60px 60px;opacity:.6}
.bl .dots{background-image:radial-gradient(circle,rgba(255,255,255,.22) 2.4px,transparent 2.6px)}
.top{position:absolute;left:84px;right:84px;top:76px;display:flex;align-items:center;gap:18px}
.top img{width:52px;height:52px}.bl .top img{filter:brightness(0) invert(1)}
.lab{font-family:P;font-weight:500;letter-spacing:.08em;font-size:26px;text-transform:uppercase}
.lab b{color:var(--blue);font-weight:500}.bl .lab b{color:#fff;opacity:.75}
.h{position:absolute;left:84px;right:84px;font-weight:800;letter-spacing:-.04em;line-height:1.02}
.h em{font-family:S;font-style:italic;font-weight:400;color:var(--blue);letter-spacing:-.01em}
.bl .h em{color:#fff}
.p{position:absolute;left:84px;right:84px;font-weight:500;font-size:42px;line-height:1.3;color:#2a2e38}
.bl .p{color:#fff;opacity:.92}
.src{position:absolute;left:84px;right:84px;font-family:P;font-weight:500;letter-spacing:.06em;font-size:22px;color:var(--mute);text-transform:uppercase}
.bl .src{color:#fff;opacity:.7}
.foot{position:absolute;left:84px;right:84px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-family:P;font-weight:500;font-size:26px;letter-spacing:.06em;color:var(--mute)}
.bl .foot{color:#fff;opacity:.8}
.big{position:absolute;left:84px;right:84px;font-weight:800;letter-spacing:-.06em;line-height:.9;color:var(--blue)}
.bl .big{color:#fff}
.chip{display:inline-flex;align-items:center;gap:14px;padding:18px 30px;border-radius:60px;border:4px solid var(--ink);background:#fff;font-weight:800;font-size:36px}
.bl .chip{border-color:#fff;color:var(--blue)}
.li{position:absolute;left:84px;right:84px;display:flex;flex-direction:column;gap:30px}
.it{display:flex;gap:28px;align-items:flex-start;font-size:44px;font-weight:600;line-height:1.2}
.it i{font-style:normal;flex:none;width:64px;height:64px;border-radius:50%;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800;margin-top:-2px}
.ph{position:absolute;border:14px solid var(--ink);border-radius:64px;overflow:hidden;background:#fff;box-shadow:0 30px 80px rgba(13,15,20,.18)}
.ph img{display:block;width:100%}
.opt{display:flex;align-items:center;gap:26px;padding:28px 34px;border:4px solid var(--ink);border-radius:30px;background:#fff;font-size:44px;font-weight:700}
.opt b{width:70px;height:70px;border-radius:50%;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;flex:none}
'''

def page(w, h, inner, blue=False):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="st{" bl" if blue else ""}" style="width:{w}px;height:{h}px"><div class="dots"></div>{inner}</div></body></html>'

def top(label):
    return f'<div class="top"><img src="proteam-mark.webp"><span class="lab">{label}</span></div>'

def foot(n, tot, right='DESLIZA →'):
    return f'<div class="foot"><span>@APP.PROTEAM</span><span>{n}/{tot} · {right}</span></div>' if tot else '<div class="foot"><span>@APP.PROTEAM</span><span>PRO-TEAM.APP</span></div>'

S = {}
# ---------- carousel 1: corners (#1)
L1 = 'Lo que dicen los datos · <b>#1</b>'
S['c1-1'] = page(1080, 1350, top(L1) + '<div class="h" style="top:330px;font-size:132px">¿Cuántos córners hacen falta para <em>un gol?</em></div>' + foot(1, 4))
S['c1-2'] = page(1080, 1350, top(L1) + '<div class="big" style="top:300px;font-size:330px">3<span style="font-size:150px;letter-spacing:-.03em"> de 100</span></div><div class="h" style="top:700px;font-size:88px">córners acaban <em>en gol.</em></div><div class="p" style="top:950px">Parece una ocasión clarísima, pero casi nunca entra.</div><div class="src" style="bottom:150px">Fuente: Opta · Championship 24/25 · 2,9 %</div>' + foot(2, 4))
S['c1-3'] = page(1080, 1350, top(L1) + '<div class="h" style="top:260px;font-size:96px">Entonces, ¿por qué algunos equipos <em>marcan tantos?</em></div><div class="li" style="top:780px"><div class="it"><i>1</i>Los entrenan como una jugada más.</div><div class="it"><i>2</i>Apuntan qué saque funciona y cuál no.</div><div class="it"><i>3</i>Lo revisan partido a partido.</div></div>' + foot(3, 4))
S['c1-4'] = page(1080, 1350, top('ProTeam') + '<div class="h" style="top:300px;font-size:112px">Apunta cada córner <em>en directo,</em> desde la banda.</div><div class="p" style="top:760px">Y al acabar, el informe del partido en una sola página.</div><div style="position:absolute;left:84px;top:1000px"><span class="chip">Síguenos para el #2 →</span></div>' + foot(0, 0), True)
# ---------- carousel 2: balonmano
L2 = 'Balonmano · <b>estadística</b>'
S['c2-1'] = page(1080, 1350, top(L2) + '<div class="h" style="top:320px;font-size:120px">3 cosas que tu estadística <em>se pierde</em> en directo.</div><div class="p" style="top:900px">Y cómo las registra ProTeam.</div>' + foot(1, 5))
def hb(n, tit, em, txt, img):
    return page(1080, 1350, top(L2) + f'<div class="big" style="top:210px;font-size:150px">0{n}</div><div class="h" style="top:380px;font-size:84px">{tit} <em>{em}</em></div><div class="p" style="top:590px;width:470px;font-size:38px">{txt}</div><div class="ph" style="left:600px;top:540px;width:400px;height:640px"><img src="app/{img}.jpg"></div>' + foot(n + 1, 5))
S['c2-2'] = hb(1, 'Los tiros que', 'nadie ve.', 'Pulsas «No lo he visto» y marcas solo si fue gol. Cuenta para el portero sin ensuciar los mapas.', 'nlv-3')
S['c2-3'] = hb(2, 'Los golpes', 'francos.', 'Un toque: si defiendes suma uno vuestro, si atacas, uno del rival.', 'gf-2')
S['c2-4'] = hb(3, 'Las posesiones', 'reales.', 'Cada cambio de posesión queda registrado: ataques y defensas, los de verdad.', 'res-1')
S['c2-5'] = page(1080, 1350, top('ProTeam') + '<div class="h" style="top:300px;font-size:116px">Estadística de balonmano <em>que cuadra.</em></div><div class="p" style="top:740px">Pruébalo 3 meses gratis, sin tarjeta.</div><div style="position:absolute;left:84px;top:960px"><span class="chip">Enlace en la bio →</span></div>' + foot(0, 0), True)
# ---------- image post: pregunta
S['q1'] = page(1080, 1350, top('Pregunta de la <b>semana</b>') + '<div class="h" style="top:250px;font-size:92px">¿Qué te quita más tiempo <em>fuera del campo?</em></div><div class="li" style="top:690px;gap:26px"><div class="opt"><b>A</b>Convocatorias y asistencia</div><div class="opt"><b>B</b>Pasar a limpio la estadística</div><div class="opt"><b>C</b>Planificar la semana</div></div><div class="src" style="top:1170px;color:var(--ink)">Responde con la letra en comentarios ↓</div>' + foot(0, 0))
# ---------- carousel 3: penaltis (#2)
L3 = 'Lo que dicen los datos · <b>#2</b>'
S['c3-1'] = page(1080, 1350, top(L3) + '<div class="h" style="top:360px;font-size:140px">¿Un penalti es <em>gol seguro?</em></div>' + foot(1, 4))
S['c3-2'] = page(1080, 1350, top(L3) + '<div class="big" style="top:300px;font-size:330px">78<span style="font-size:170px"> %</span></div><div class="h" style="top:680px;font-size:88px">de los penaltis <em>acaban dentro.</em></div><div class="p" style="top:930px">O sea: más o menos, 1 de cada 5 no entra.</div><div class="src" style="bottom:150px">Media histórica aproximada</div>' + foot(2, 4))
S['c3-3'] = page(1080, 1350, top(L3) + '<div class="h" style="top:300px;font-size:104px">¿Quién debería <em>tirarlos?</em></div><div class="p" style="top:600px;font-size:54px;font-weight:700;color:var(--ink)">El que más mete.<br>No el que más ganas tiene.</div><div class="p" style="top:860px">Y eso solo se sabe si apuntas los marcados… y los fallados.</div>' + foot(3, 4))
S['c3-4'] = page(1080, 1350, top('ProTeam') + '<div class="h" style="top:300px;font-size:112px">Cada penalti, <em>jugador a jugador.</em></div><div class="p" style="top:720px">Marcados y fallados, apuntados en directo.</div><div style="position:absolute;left:84px;top:960px"><span class="chip">Síguenos para el #3 →</span></div>' + foot(0, 0), True)

# ---------- stories 1080x1920
def story_reel(cov, tit, em, sub):
    return page(1080, 1920, top('Nuevo <b>reel</b>') + f'<div class="h" style="top:230px;font-size:96px">{tit} <em>{em}</em></div><div class="ph" style="left:250px;top:620px;width:580px;height:1030px"><img src="cov/{cov}"></div><div class="src" style="top:1720px;text-align:center;color:var(--ink);font-size:30px">{sub}</div>')
def story_q(tit, em, ans):
    return page(1080, 1920, top('Pregunta <b>rápida</b>') + f'<div class="h" style="top:560px;font-size:120px">{tit} <em>{em}</em></div><div class="p" style="top:1180px;font-size:48px">{ans}</div>', True)
def story_app(tit, em, img, sub):
    return page(1080, 1920, top('Dentro de <b>ProTeam</b>') + f'<div class="h" style="top:220px;font-size:92px">{tit} <em>{em}</em></div><div class="ph" style="left:220px;top:600px;width:640px;height:1150px"><img src="app/{img}.jpg"></div><div class="src" style="top:1800px;text-align:center;color:var(--ink);font-size:28px">{sub}</div>')
S['s1-a'] = story_reel('corners.jpg', '¿Cuántos córners hacen falta', 'para un gol?', 'Ya en el perfil · @app.proteam')
S['s1-b'] = story_q('¿Cuántos córners crees que hacen falta', 'para un gol?', 'La respuesta te sorprenderá. Está en nuestro último Reel.')
S['s2-a'] = story_app('Tiros que nadie ve:', '«No lo he visto».', 'nlv-3', 'Estadística de balonmano · pro-team.app')
S['s3-a'] = story_reel('penaltis.jpg', '¿Un penalti es', 'gol seguro?', 'Ya en el perfil · @app.proteam')
S['s3-b'] = story_q('En tu equipo, ¿quién tira', 'los penaltis?', 'Respóndenos por mensaje: el que más mete o el que más quiere.')
S['s4-a'] = story_app('Golpes francos', 'con un toque.', 'gf-2', 'Estadística de balonmano · pro-team.app')
S['s5-a'] = story_reel('primergol.jpg', '¿Quién marca primero,', 'gana?', 'Ya en el perfil · @app.proteam')
S['s6-a'] = story_reel('pases.jpg', '¿Cuántos pases hacen falta', 'para un gol?', 'Ya en el perfil · @app.proteam')
S['s7-a'] = story_app('Tu temporada,', 'planificada.', 'mo-plan', 'Planifica, controla la carga y analiza · pro-team.app')
S['s7-b'] = story_q('¿De qué tema quieres', 'el próximo Reel?', 'Escríbenos por mensaje. Leemos todo.')

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for k, html in S.items():
            w, h = (1080, 1920) if k.startswith('s') else (1080, 1350)
            open(f'{B}/_t.html', 'w').write(html)
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(f'file://{B}/_t.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(250)
            await pg.screenshot(path=f'{B}/out/{k}.jpg', type='jpeg', quality=92); await pg.close()
        await b.close()
asyncio.run(main())
print(len(S))
