"""Genera los 3 Reels del kit como proyectos HyperFrames (1080x1920).
   python3 make.py RAW_DIR OUT_DIR   -> OUT_DIR/<reel>/index.html + assets/
Cada escena es una foto o vídeo de Higgsfield, el móvil con capturas reales o la tarjeta final.
El texto entra palabra a palabra (desenfoque -> nítido) y la cámara nunca se queda quieta."""
import json, os, shutil, sys

RAW, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
FONTS = os.path.join(ROOT, 'tools', 'fonts'); APP = os.path.join(ROOT, 'tools', 'app')

REELS = {
 'r1-focos': {'dur': 12.8, 'music': 12.3, 'scenes': [
    {'kind': 'video', 'src': 'vid100.mp4', 't': 0, 'd': 7.7, 'zoom': [1.0, 1.12]},
    {'kind': 'end', 't': 7.7, 'd': 5.1},
  ], 'text': [
    {'t': 0.25, 'd': 2.2, 'y': 470, 'cls': 'kick', 'html': '27.11 · 23:59'},
    {'t': 0.45, 'd': 2.0, 'y': 540, 'cls': 'big', 'html': 'Hay algo'},
    {'t': 0.95, 'd': 1.5, 'y': 680, 'cls': 'big', 'html': '<em>a oscuras.</em>'},
    {'t': 2.6, 'd': 4.8, 'y': 540, 'cls': 'big', 'html': 'El 27'},
    {'t': 3.3, 'd': 4.1, 'y': 680, 'cls': 'big', 'html': 'se encienden'},
    {'t': 4.3, 'd': 3.1, 'y': 820, 'cls': 'big', 'html': 'los <em>focos.</em>'},
  ]},
 'r2-sal-al-campo': {'dur': 15.0, 'music': 11.9, 'scenes': [
    {'kind': 'video', 'src': 'vid101.mp4', 't': 0, 'd': 8.0, 'zoom': [1.15, 1.0]},
    {'kind': 'phone', 't': 8.0, 'd': 4.2, 'screens': [['mo-plan.jpg', 'Planifica.'], ['reg-0.jpg', 'Registra.'], ['res-0.jpg', 'Analiza.']]},
    {'kind': 'end', 't': 12.2, 'd': 2.8},
  ], 'text': [
    {'t': 0.3, 'd': 1.9, 'y': 420, 'cls': 'big s', 'html': 'Cada semana'},
    {'t': 0.75, 'd': 1.45, 'y': 530, 'cls': 'big s', 'html': 'sales al campo.'},
    {'t': 2.4, 'd': 0.95, 'y': 470, 'cls': 'big', 'html': 'Con libreta.'},
    {'t': 3.4, 'd': 0.95, 'y': 470, 'cls': 'big', 'html': 'Con memoria.'},
    {'t': 4.4, 'd': 1.2, 'y': 470, 'cls': 'big', 'html': 'Con intuición.'},
    {'t': 5.9, 'd': 2.0, 'y': 420, 'cls': 'big', 'html': 'Esta vez,'},
    {'t': 6.5, 'd': 1.4, 'y': 560, 'cls': 'big', 'html': 'con <em>datos.</em>'},
  ]},
 'r3-tres-deportes': {'dur': 12.0, 'music': 19.45, 'scenes': [
    {'kind': 'image', 'src': 'img0.png', 't': 0, 'd': 1.35, 'zoom': [1.25, 1.1], 'pos': '50% 70%'},
    {'kind': 'video', 'src': 'vid102.mp4', 't': 1.35, 'd': 1.3, 'zoom': [1.1, 1.0], 'from': 1.2},
    {'kind': 'image', 'src': 'img2.png', 't': 2.65, 'd': 1.3, 'zoom': [1.0, 1.15], 'pos': '60% 60%'},
    {'kind': 'image', 'src': 'img1.png', 't': 3.95, 'd': 2.5, 'zoom': [1.2, 1.05], 'pos': '55% 60%'},
    {'kind': 'image', 'src': 'img3-res.png', 't': 6.45, 'd': 2.6, 'zoom': [1.0, 1.12], 'pos': '60% 40%'},
    {'kind': 'end', 't': 9.05, 'd': 2.95},
  ], 'text': [
    {'t': 0.1, 'd': 1.2, 'y': 760, 'cls': 'huge', 'html': 'Fútbol.'},
    {'t': 1.4, 'd': 1.2, 'y': 760, 'cls': 'huge', 'html': 'Baloncesto.'},
    {'t': 2.7, 'd': 1.2, 'y': 760, 'cls': 'huge', 'html': 'Balonmano.'},
    {'t': 4.05, 'd': 2.3, 'y': 420, 'cls': 'big', 'html': 'Un mismo'},
    {'t': 4.45, 'd': 1.9, 'y': 560, 'cls': 'big', 'html': '<em>banquillo.</em>'},
    {'t': 6.55, 'd': 2.4, 'y': 380, 'cls': 'big s', 'html': 'En tu'},
    {'t': 6.85, 'd': 2.1, 'y': 490, 'cls': 'big s', 'html': '<em>bolsillo.</em>'},
  ]},
}

CSS = """
@font-face{font-family:M;font-weight:800;src:url(assets/manrope-latin-800-normal.woff2)}
@font-face{font-family:M;font-weight:500;src:url(assets/manrope-latin-500-normal.woff2)}
@font-face{font-family:S;font-style:italic;font-weight:400;src:url(assets/instrument-serif-latin-400-italic.woff2)}
@font-face{font-family:P;font-weight:500;src:url(assets/ibm-plex-mono-latin-500-normal.woff2)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0d0f14}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0d0f14;color:#f5f7fb;font-family:M}
.sc{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden}
.cam{position:absolute;left:0;top:0;width:1080px;height:1920px}
.cam video,.cam img.bgi{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover}
.shade{position:absolute;left:0;top:0;width:1080px;height:1920px;background:linear-gradient(180deg,rgba(13,15,20,.85) 0%,rgba(13,15,20,.35) 34%,rgba(13,15,20,0) 52%,rgba(13,15,20,.2) 78%,rgba(13,15,20,.8) 100%)}
.tx{position:absolute;left:84px;width:912px;white-space:nowrap}
.tx .w{display:inline-block;white-space:pre}
.big{font-weight:800;font-size:128px;letter-spacing:-.04em;line-height:1}
.big.s{font-size:112px}
.huge{font-weight:800;font-size:172px;letter-spacing:-.05em;line-height:1;text-align:center;left:0;width:1080px}
.kick{font-family:P;font-weight:500;font-size:34px;letter-spacing:.12em;color:#9db8ff}
em{font-family:S;font-style:italic;font-weight:400;color:#2f6bff;font-size:1.1em;letter-spacing:-.01em;text-shadow:0 0 50px rgba(47,107,255,.45)}
#logo{position:absolute;left:84px;top:170px;display:flex;align-items:center;gap:16px;font-weight:800;font-size:40px;letter-spacing:-.02em}
#logo img{width:62px;height:62px}
.phone{position:absolute;left:290px;top:430px;width:500px;height:1085px;border-radius:72px;background:#0a0b0f;box-shadow:0 0 0 4px #2a2f3a,0 60px 160px rgba(0,0,0,.7),0 0 140px rgba(47,107,255,.35);overflow:hidden}
.phone img{position:absolute;left:16px;top:16px;width:468px;height:1053px;object-fit:cover;object-position:top;border-radius:58px}
.plab{position:absolute;left:0;width:1080px;top:1580px;text-align:center;font-weight:800;font-size:96px;letter-spacing:-.04em}
.end-bg{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(120% 60% at 50% 40%,#13204a 0%,#0d0f14 60%)}
.end-mark{position:absolute;left:390px;top:470px;width:300px;height:300px}
.end-name{position:absolute;left:0;width:1080px;top:800px;text-align:center;font-weight:800;font-size:110px;letter-spacing:-.04em}
.end-chip{position:absolute;left:0;width:1080px;top:960px;text-align:center}
.end-chip span{display:inline-block;font-family:P;font-weight:500;font-size:32px;letter-spacing:.1em;padding:16px 28px 14px;border-radius:999px;background:#2f6bff;color:#fff}
.end-line{position:absolute;left:0;width:1080px;top:1070px;text-align:center;font-weight:500;font-size:44px;color:rgba(245,247,251,.86)}
.end-line em{font-size:1.15em}
.end-cta{position:absolute;left:0;width:1080px;top:1190px;text-align:center}
.end-cta span{display:inline-block;font-weight:800;font-size:54px;background:#f5f7fb;color:#0d0f14;padding:24px 44px 22px;border-radius:18px}
.end-url{position:absolute;left:0;width:1080px;top:1330px;text-align:center;font-family:P;font-weight:500;font-size:34px;letter-spacing:.08em;color:rgba(245,247,251,.75)}
#grain{position:absolute;left:-100px;top:-100px;width:1280px;height:2120px;background:url(assets/grain.png);mix-blend-mode:overlay;opacity:.13}
#flash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:#fff}
"""

def scene_html(i, s):
    sid = f's{i}'
    a = f'id="{sid}" class="clip sc" data-start="{s["t"]}" data-duration="{s["d"]}" data-track-index="{i + 1}" style="z-index:{i + 2}" data-layout-allow-overflow'
    if s['kind'] == 'video':
        ms = s.get('from', 0)
        return (f'<div {a}><div id="{sid}-cam" class="cam"></div><div class="shade"></div></div>\n'
                f'<video id="{sid}-v" class="clip" src="assets/{s["src"]}" muted playsinline data-start="{s["t"]}" data-duration="{s["d"]}" data-media-start="{ms}" data-track-index="{40 + i}" '
                f'style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;z-index:{i + 2}"></video>')
    if s['kind'] == 'image':
        return f'<div {a}><div id="{sid}-cam" class="cam"><img class="bgi" src="assets/{s["src"]}" style="object-position:{s.get("pos", "50% 50%")}"></div><div class="shade"></div></div>'
    if s['kind'] == 'phone':
        ims = ''.join(f'<img id="{sid}-i{k}" src="assets/{sc}">' for k, (sc, _) in enumerate(s['screens']))
        labs = ''.join(f'<div id="{sid}-l{k}" class="plab">{lab}</div>' for k, (_, lab) in enumerate(s['screens']))
        return (f'<div {a}><div class="end-bg"></div><div id="{sid}-cam" class="cam"><div id="{sid}-ph" class="phone">{ims}</div>{labs}</div></div>')
    if s['kind'] == 'end':
        return (f'<div {a}><div class="end-bg"></div><div id="{sid}-cam" class="cam">'
                f'<img id="{sid}-mark" class="end-mark" src="assets/mark.png">'
                f'<div id="{sid}-name" class="end-name">ProTeam</div>'
                f'<div id="{sid}-chip" class="end-chip"><span>LISTA DE ESPERA ABIERTA</span></div>'
                f'<div id="{sid}-line" class="end-line">6 meses gratis para la <em>lista.</em></div>'
                f'<div id="{sid}-cta" class="end-cta"><span>Crea tu cuenta</span></div>'
                f'<div id="{sid}-url" class="end-url">pro-team.app · 27.11 · 23:59</div></div></div>')

def build(name, R):
    d = os.path.join(OUT, name); a = os.path.join(d, 'assets'); os.makedirs(a, exist_ok=True)
    for f in ['manrope-latin-800-normal.woff2', 'manrope-latin-500-normal.woff2', 'instrument-serif-latin-400-italic.woff2', 'ibm-plex-mono-latin-500-normal.woff2']:
        shutil.copy(os.path.join(FONTS, f), a)
    shutil.copy(os.path.join(HERE, '..', 'mark.png'), a); shutil.copy(os.path.join(HERE, '..', 'grain.png'), a)
    shutil.copy(os.path.join(HERE, 'music.mp3'), a)
    for s in R['scenes']:
        if 'src' in s: shutil.copy(os.path.join(RAW, s['src']), a)
        for sc, _ in s.get('screens', []): shutil.copy(os.path.join(APP, sc), a)
    D = R['dur']
    body = [scene_html(i, s) for i, s in enumerate(R['scenes'])]
    for k, t in enumerate(R['text']):
        body.append(f'<div id="t{k}" class="clip tx {t["cls"]}" data-start="{t["t"]}" data-duration="{t["d"]}" data-track-index="{20 + k}" style="top:{t["y"]}px;z-index:30" data-layout-allow-overflow>{t["html"]}</div>')
    body.append(f'<div id="logo" class="clip" data-start="0" data-duration="{D}" data-track-index="60" style="z-index:31"><img src="assets/mark.png">ProTeam</div>')
    body.append(f'<div id="gr" class="clip" data-start="0" data-duration="{D}" data-track-index="61" style="position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:40" data-layout-ignore><div id="grain"></div></div>')
    body.append(f'<div id="fl" class="clip" data-start="0" data-duration="{D}" data-track-index="62" style="position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:41" data-layout-ignore><div id="flash"></div></div>')
    body.append(f'<audio id="music" class="clip" src="assets/music.mp3" data-start="0" data-duration="{D}" data-media-start="{R["music"]}" data-volume="0.95" data-fade-out="0.8" data-track-index="70"></audio>')
    spec = json.dumps({'scenes': R['scenes'], 'text': R['text'], 'dur': D})
    html = f"""<!doctype html><html lang="es" data-resolution="portrait"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080, height=1920">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1080" data-height="1920">
{chr(10).join(body)}
</div>
<script>
const SPEC = {spec};
document.fonts.load('800 100px M').then(() => document.fonts.load('italic 400 100px S')).then(() => document.fonts.load('500 30px P')).then(() => {{
  const tl = gsap.timeline({{ paused: true }});
  let seed = 27; const rnd = () => {{ seed = (seed * 16807) % 2147483647; return seed / 2147483647; }};
  // cámara: deriva continua en cada escena
  SPEC.scenes.forEach((s, i) => {{
    const z = s.zoom || [1.04, 1.0];
    const cam = '#s' + i + '-cam';
    tl.fromTo(cam, {{ scale: z[0], rotation: i % 2 ? .6 : -.6 }}, {{ scale: z[1], rotation: i % 2 ? -.4 : .4, duration: s.d, ease: 'none' }}, s.t);
    if (s.kind === 'video') tl.fromTo('#s' + i + '-v', {{ scale: z[0] }}, {{ scale: z[1], duration: s.d, ease: 'none' }}, s.t);
    // entrada con golpe: empieza grande y desenfocada
    if (i > 0) {{
      tl.fromTo('#s' + i, {{ filter: 'blur(18px)' }}, {{ filter: 'blur(0px)', duration: .3, ease: 'expo.out' }}, s.t);
      tl.set('#flash', {{ opacity: s.kind === 'end' ? .9 : .45 }}, s.t - .001);
      tl.to('#flash', {{ opacity: 0, duration: s.kind === 'end' ? .5 : .22, ease: 'power2.out' }}, s.t);
    }}
    if (s.kind === 'phone') {{
      const n = s.screens.length, each = s.d / n;
      tl.fromTo('#s' + i + '-ph', {{ y: 900, rotation: 8, scale: .9 }}, {{ y: 0, rotation: 0, scale: 1, duration: .6, ease: 'expo.out' }}, s.t);
      s.screens.forEach((_, k) => {{
        const t0 = s.t + k * each;
        if (k > 0) tl.fromTo('#s' + i + '-i' + k, {{ yPercent: 100 }}, {{ yPercent: 0, duration: .45, ease: 'expo.inOut' }}, t0 - .15);
        else tl.set('#s' + i + '-i0', {{ yPercent: 0 }}, t0);
        tl.fromTo('#s' + i + '-l' + k, {{ opacity: 0, y: 60, filter: 'blur(12px)' }}, {{ opacity: 1, y: 0, filter: 'blur(0px)', duration: .35, ease: 'expo.out' }}, t0 + .1);
        tl.to('#s' + i + '-l' + k, {{ opacity: 0, filter: 'blur(10px)', duration: .18, ease: 'power2.in' }}, t0 + each - .2);
      }});
      tl.to('#s' + i + '-ph', {{ rotation: -2, scale: 1.04, duration: s.d, ease: 'none' }}, s.t + .6);
    }}
    if (s.kind === 'end') {{
      const e = '#s' + i;
      tl.fromTo(e + '-mark', {{ scale: 2.4, opacity: 0, filter: 'blur(20px)' }}, {{ scale: 1, opacity: 1, filter: 'blur(0px)', duration: .55, ease: 'expo.out' }}, s.t + .05);
      tl.fromTo(e + '-name', {{ y: 80, opacity: 0, filter: 'blur(12px)' }}, {{ y: 0, opacity: 1, filter: 'blur(0px)', duration: .45, ease: 'expo.out' }}, s.t + .3);
      tl.fromTo(e + '-chip', {{ scale: .6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: .4, ease: 'back.out(2)' }}, s.t + .55);
      tl.fromTo(e + '-line', {{ opacity: 0, filter: 'blur(10px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: .3, ease: 'power2.out' }}, s.t + .75);
      tl.fromTo(e + '-cta', {{ y: 60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: .45, ease: 'expo.out' }}, s.t + .95);
      tl.fromTo(e + '-url', {{ opacity: 0 }}, {{ opacity: 1, duration: .3 }}, s.t + 1.15);
      tl.to(e + '-cam', {{ scale: 1.05, duration: s.d, ease: 'none' }}, s.t);
      tl.fromTo('#logo', {{ opacity: 1 }}, {{ opacity: 0, duration: .2 }}, s.t);
    }}
  }});
  // texto palabra a palabra
  SPEC.text.forEach((t, k) => {{
    const el = document.getElementById('t' + k);
    const parts = [];
    el.childNodes.forEach((n) => {{
      if (n.nodeType === 3) n.textContent.split(/( )/).forEach((w) => {{ if (w) parts.push(w === ' ' ? document.createTextNode(' ') : Object.assign(document.createElement('span'), {{ className: 'w', textContent: w }})); }});
      else {{ n.classList.add('w'); parts.push(n); }}
    }});
    el.textContent = ''; parts.forEach((p) => el.appendChild(p));
    const ws = el.querySelectorAll('.w');
    tl.fromTo(ws, {{ opacity: 0, scale: 1.35, filter: 'blur(14px)', transformOrigin: '0% 70%' }}, {{ opacity: 1, scale: 1, filter: 'blur(0px)', duration: .34, ease: 'expo.out', stagger: .08 }}, t.t);
    tl.to(ws, {{ opacity: 0, filter: 'blur(12px)', duration: .16, ease: 'power2.in', stagger: .03 }}, t.t + t.d - .22);
  }});
  tl.set('#flash', {{ opacity: 0 }}, 0);
  for (let t = 0; t < SPEC.dur; t += 1 / 12) tl.set('#grain', {{ x: Math.round(rnd() * 160 - 80), y: Math.round(rnd() * 160 - 80) }}, t);
  window.__timelines['main'] = tl; tl.seek(0);
}});
</script></body></html>"""
    open(os.path.join(d, 'index.html'), 'w').write(html)
    print('ok', name)

for n, R in REELS.items():
    if len(sys.argv) > 3 and n not in sys.argv[3:]: continue
    build(n, R)
