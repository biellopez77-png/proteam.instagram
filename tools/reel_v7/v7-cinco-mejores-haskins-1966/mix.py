"""Mezcla v7 · «Mis cinco mejores» (Haskins, Texas Western, 1966) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», desde los 4 s del archivo; distinta de la de los últimos v7,
que usaron «Calm Piano, Dreamy, Intro 01-03» y «Soft Piano, Strings, Calm, Intro, Logo») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-walkie-luis-enrique-2022/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.7; DUR = OUT + 4.0   # la voz acaba en 25,1 s; a 25,7 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 26,0)
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2, af=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', f] + (['-af', af] if af else []) + ['-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: una sola pieza larga, sin cortes; entra suave y baja al cierre
put(mus, ld('mus.mp3'), 0.0, 1.0, off=4.0, dur=DUR, fi=.4, fo=2.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .6 * np.clip((tt - E(35)) / .15, 0, 1) * np.clip((T(36) + .05 - tt) / .15, 0, 1)   # silencio breve antes de «Puse a mis cinco mejores»
env *= 1 + .3 * np.clip((tt - E(56)) / 1.0, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)     # sube 1 s tras «no la grada» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3'))
ST = pk(ld('stamp.mp3')); CA = pk(ld('cards.mp3')); CH = pk(ld('chips.mp3'))
CO = [0.17, 0.83, 1.13, 1.76, 1.97]                                         # golpes sueltos de carta dentro de cards.mp3
for f in [6.3, 10.0, 13.4, 17.95, 21.3]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, .05, .035)                                                     # panel de las finales
put(sfx, CH, T(13) - .02, .035, dur=.35, fo=.1)                             # se enciende 1966
put(sfx, SL, T(14) - .15, .05)                                              # recorte de 1966
put(sfx, SL, T(15) - .25, .045); put(sfx, SH, T(15) - .1, .08)              # ficha de Rupp + obturador
put(sfx, ST, T(16) + .05, .09)                                              # sello «Nº1»
for i in range(5): put(sfx, CA, T(18) + i * .17, .05, off=CO[i] - .02, dur=.28, fo=.08)   # cinco fichas de Kentucky
put(sfx, SL, T(22) - .3, .04); put(sfx, MK, T(22) - .1, .03, dur=1.0, fi=.02, fo=.25)    # ficha de Haskins y silueta a rotulador
put(sfx, SH, T(25) - .05, .08)                                              # foto de Shed
for i in range(5): put(sfx, CA, T(27) + i * .17, .05, off=CO[i] - .02, dur=.28, fo=.08)   # cinco fichas de Texas Western
put(sfx, SL, 13.85, .04)                                                    # tarjeta de la cita
for i in range(5): put(sfx, CH, T(36) + i * .06, .018, dur=.3, fo=.1)       # fichas que aparecen
put(sfx, CH, T(40) - .1, .045, dur=.5, fo=.15)                              # se juntan en «mejores»
put(sfx, SL, T(41) - .3, .045); put(sfx, SH, T(41) - .2, .07)               # foto del trofeo
put(sfx, SL, T(44) - .3, .035)                                              # marcador
put(sfx, MK, T(47) - .2, .03, off=2.0, dur=1.2, fi=.02, fo=.3)              # pista a rotulador
for i in range(5): put(sfx, CH, T(48) + i * .08, .015, dur=.25, fo=.08)     # cinco posiciones
put(vox, ld(sys.argv[1]), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a2 = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a2 * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
