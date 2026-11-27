"""Mezcla v7 · El golpe ciento uno (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» y «… 02», encadenadas con 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y peor-verano-2003/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 17.9; DUR = OUT + 5.61   # la voz acaba en 17,62 s; a 17,9 entra el cierre (xfade 0,6 s)
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(at * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: dos loops de la misma serie, fundido de 1,4 s, sin cortes; se apaga con 1,4 s mientras entra el cierre
M1, M2 = ld('mus1.mp3'), ld('mus2.mp3')
put(mus, M1, 0.0, 1.0, dur=13.8, fi=.3, fo=1.4)
put(mus, M2, 12.4, 1.0, dur=OUT + 1.6 - 12.4, fi=1.4, fo=1.4)
env = np.ones(N)                               # baja en el golpe ciento uno, sube 1 s al final
tt = np.arange(N) / SR
env *= 1 - .3 * np.clip((tt - 11.0) / .4, 0, 1) * np.clip((13.9 - tt) / .5, 0, 1)
env *= 1 + .25 * np.clip((tt - 15.9) / .6, 0, 1) * np.clip((OUT + .4 - tt) / .8, 0, 1)
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); FR = pk(ld('frame.mp3')); SH = pk(ld('shutter.mp3'))
LK = pk(ld('locker.mp3')); MK = pk(ld('marker.mp3')); HM = pk(ld('hammer.mp3')); CR = pk(ld('crack.mp3'))
for f in [4.95, 6.75, 13.45]: put(sfx, WH, f - .1, .09, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, LK, 0.85, .06, off=.2, dur=.9, fo=.4)       # la taquilla se ilumina
put(sfx, PA, 0.86, .12)                               # ficha de Duncan
put(sfx, SH, T(7) - .1, .11)                          # Popovich: obturador
put(sfx, PA, T(8) + .05, .07)                         # ficha «Entrenador»
for i in range(5): put(sfx, FR, T(11) + i * .2 + .25 - .4, .08, fo=.3)   # cinco cartelas que se cuelgan
put(sfx, PA, T(16) - .2, .13)                         # foto del cantero
put(sfx, PA, T(19) + .1, .08)                         # Jacob Riis
hit = HM[int(14.22 * SR):int(14.6 * SR)].copy(); hit[-int(.08 * SR):] *= np.linspace(1, 0, int(.08 * SR))[:, None]
for i in range(12):                                   # golpes de maza en el instante en que cae el mazo
    kp = (i / 12) ** (1 / 1.4); put(sfx, hit, T(20) + kp * (E(25) - T(20)) - .02, .11 * (1 - .3 * i / 12))
put(sfx, hit, T(33) + .1, .16)                        # el golpe ciento uno
put(sfx, CR, T(33) + .14, .2, off=.1, dur=1.6, fo=.6) # la piedra se raja (real)
put(sfx, MK, T(36) - .35, .06, fo=.3)                 # las 100 rayitas
put(sfx, MK, T(43), .07, dur=1.6, fo=.6)              # se encienden
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT + 0.3)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
