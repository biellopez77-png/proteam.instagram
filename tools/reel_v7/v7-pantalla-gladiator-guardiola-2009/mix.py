"""Mezcla v7 · Siete minutos a oscuras (Guardiola, Roma 2009) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Orchestra, Epic, Dreamy, Suspense») + SFX reales bajos + voz (ElevenLabs, Mateo)
+ en el cierre, el audio de tools/reel_v6/outro/outro2.mp4 y el sting «Logo, Calm, Piano 01» bajo.
Base: tools/reel_v7/wooden/mix.py y v7-techo-forest-clough/mix.py.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.1; DUR = OUT + 4.0   # la voz acaba en 23,98 s; remate quieto hasta 25,1 y fundido a negro de 0,5 s al cierre (xfade fadeblack; outro2, 4,0 s, desde 25,1)
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vn', '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); outro = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
put(mus, ld('mus.mp3'), 0.0, 1.0, off=0.0, dur=OUT + 2.4, fi=.3, fo=2.2)   # la música sigue y baja durante el cierre
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(55)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube ~1 s en «no la das tú» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); TO = pk(ld('token.mp3'))
SW = pk(ld('switch.mp3')); WS = pk(ld('whistle.mp3')); HU = pk(ld('hum.mp3'))
for f in [2.92, 5.92, 19.6]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
for f in [9.2, 15.85, 18.15, 21.0]: put(sfx, WH, f - .05, .035, dur=1.0, fi=.05, fo=.4)   # desplazamientos cortos
put(sfx, SH, -.05, .09)                            # polaroid del Olímpico (obturador)
put(sfx, MK, T(1), .05, dur=.8, fi=.03, fo=.3)     # fecha a mano 27·05·2009
put(sfx, SL, T(2) - .2, .09)                       # foto de la grada y ficha de la final
put(sfx, SL, T(3) - .1, .07)
put(sfx, SH, T(6) - .45, .08)                      # Guardiola
put(sfx, WS, T(8) - .02, .06, dur=.9, fo=.3)       # silbato corto y lejano
put(sfx, SL, T(9) - .2, .06)                       # barra del calentamiento
put(sfx, TO, T(11) + .02, .08, dur=.4, fo=.15)     # el corte: un clic
put(sfx, MK, T(14) - .35, .035, dur=1.0, fi=.05, fo=.3)   # perchas y bancos
put(sfx, SW, T(16) - .12, .12, dur=.6, fo=.15)     # interruptor: a oscuras
put(sfx, SL, T(17) - .1, .05)                      # reloj −10:00
put(sfx, HU, T(24) - .1, .035, off=10.0, dur=E(37) - T(24) + 1.4, fi=.5, fo=.9)   # zumbido de proyector, muy bajo
put(sfx, TO, T(30), .07, dur=1.8, fo=.5)           # las fichas se iluminan una a una
put(sfx, SW, T(40) - .15, .12, dur=.6, fo=.15)     # vuelve la luz
put(sfx, MK, T(43) - .2, .045, dur=.6, fi=.03, fo=.2)     # bocadillo
put(sfx, MK, T(45), .04, dur=.7, fi=.03, fo=.3)    # se borra
put(sfx, SL, T(47) - .45, .09)                     # portada de la final
put(sfx, TO, T(48) + .05, .07, dur=.25, fo=.1); put(sfx, TO, T(48) + .3, .07, dur=.25, fo=.1)   # 1 y 2 en el marcador
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(outro, ld(sys.argv[2]), OUT)                   # audio del cierre común (su voz entra a los 0,3 s)
put(outro, pk(ld('sting.mp3')) * .22 * .25, OUT, dur=4.0, fo=.8)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
ro = 20 * np.log10(np.sqrt((outro[int((OUT + .3) * SR):int((OUT + 3.0) * SR), :] ** 2).mean()) + 1e-12)
outro *= 10 ** ((-20 - ro) / 20)                   # la voz del cierre, al nivel de la voz de la historia
mix = vox + mus * duck + sfx * vg + outro
mix /= max(1, np.abs(mix).max() / .89)
fo = int((DUR - .5) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  cierre %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), ro, np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
