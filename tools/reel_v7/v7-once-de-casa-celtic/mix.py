"""Mezcla v7 · Los once de casa (Celtic de Jock Stein, Lisboa 1967) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» encadenada con «… Logo 03», fundido de 1,4 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/wooden/mix.py y v7-ubuntu-rivers-2008/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json con los tiempos ya desplazados; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)
La voz lleva 0,35 s de silencio añadido en 17,80 s (pausa antes del remate «Antes de buscar lejos…»)."""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 21.61; DUR = OUT + 4.0   # la voz acaba en 21,01 s; a 21,61 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s, sin app)
PAUSE_AT, PAUSE = 17.80, 0.35
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
M1 = ld('mus1.mp3'); M2 = ld('mus2.mp3')
put(mus, M1, 0.0, 1.0, dur=13.0, fi=.3, fo=1.4)
put(mus, M2, 11.6, 1.0, dur=DUR - 11.6, fi=1.4, fo=1.6)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(52)) / .6, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube 1 s en «mira quién juega cerca» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); ST = pk(ld('stamp.mp3')); CA = pk(ld('card.mp3')); CK = pk(ld('click.mp3'))
SH = pk(ld('shutter.mp3')); MP = pk(ld('map.mp3')); PI = pk(ld('pin.mp3')); PE = pk(ld('pencil.mp3'))
for f in [2.12, 8.74, 11.5, 17.66]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .07)                                   # la postal desliza
put(sfx, ST, T(1) - .02, .12)                            # matasellos
put(sfx, PE, T(6) - .1, .05, dur=1.2, fi=.03, fo=.3)     # la copa se dibuja
put(sfx, CA, T(3) - .05, .09)                            # ficha CELTIC
put(sfx, CA, T(10) - .05, .09)                           # ficha INTER
put(sfx, SL, T(11) - .3, .05)                            # marcador
put(sfx, CK, T(12) - .05, .06, dur=.5, fo=.2)            # placas 0-1
put(sfx, CK, T(18) - .1, .07, dur=.5, fo=.2)             # 1-1
put(sfx, CK, T(19) - .1, .08, dur=.5, fo=.2)             # 2-1
put(sfx, CA, T(19) + .05, .05)                           # CELTIC sube un escalón
put(sfx, SH, T(20) - .4, .09)                            # foto de Jock Stein (obturador)
put(sfx, SL, T(21) - .05, .06)                           # ficha de prensa
put(sfx, PE, T(24) + .05, .05, dur=.7, fi=.03, fo=.2)    # subrayado
put(sfx, MP, T(30) - .2, .08, dur=1.8, fi=.05, fo=.5)    # el mapa se despliega
pinT = lambda i: T(36) + i * ((E(39) - T(36)) / 11)
for i in range(11): put(sfx, PI, pinT(i), .035 + .004 * (i % 3))   # 11 chinchetas, muy suaves
put(sfx, PE, T(43) - .05, .06, dur=E(44) - T(43) + .2, fi=.03, fo=.25)   # compás: el círculo de 50 km
put(sfx, SL, T(47) - .1, .05)                            # foto pequeña de Celtic Park
put(sfx, SH, T(48) - .5, .06)                            # foto final
V = np.repeat(ld(sys.argv[1], 1), 2, 1); cut = int(PAUSE_AT * SR)
put(vox, V[:cut], 0.0); put(vox, V[cut:], PAUSE_AT + PAUSE)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
