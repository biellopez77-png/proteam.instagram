"""Efectos sintetizados de v6-senala-al-pasador «Una cena, cortesía del entrenador»: papel del cheque y del sobre, sobres que se posan, lápiz en la nota y en la hoja, aire en los movimientos de cámara, pases y botes suaves, un acorde suave en la flecha ultravioleta y los +3 / +1 del partidillo. Sin música. Sin golpes.
python3 sfx_v6-senala-al-pasador.py v6-senala-al-pasador/sfx.wav v6-senala-al-pasador/times.js"""
import sys, json, numpy as np
src=open('../reel_v4/sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2]
exec(src)
out=np.zeros(int(SR*(DUR+2.6)))
def put(t,x,g):
    i=int(max(0,t)*SR); out[i:i+len(x)]+=x[:max(0,len(out)-i)]*g
def tick(f=1800,d=.05):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.exp(-tt*90)
def thud(f=110,d=.18):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt*(1-.3*tt))*np.exp(-tt*28)
def chord(fs,d=2.0):
    n=int(d*SR); tt=np.arange(n)/SR; y=sum(np.sin(2*np.pi*f*tt)*a for f,a in fs)
    return y*np.minimum(1,tt/.2)*np.exp(-tt*1.6)/2.6
put(0.0,paper(.6),.35)
for k in range(8): put(.15+k*.13,tick(1400+k*60,.04),.08)
for t,d,g in [(at('en')-.1,1.3,.35),(at('dentro')-.3,1.2,.4),(at('treinta')-.4,1.1,.35),(at('regla')-.4,1.2,.4),(at('siempre')-.3,.9,.3),
              (at('piensa')-.5,1.1,.45),(at('quien')-.2,1.0,.3),(at('este')-.3,1.1,.35),(at('martes')-.2,1.0,.35),(at('apuntalo')-.3,1.4,.4)]:
    put(t,air(d),g)
u0=at('unos'); u1=at('carta')+.2
for k in range(36): put(u0+(u1-u0)*k/36,paper(.08),.08)
put(at('dentro'),paper(.7),.35); put(at('nota')-.2,paper(.5),.3)
for w,d in [('disfruta',.9),('cortesia',.7),('entrenador',.9)]: put(at(w)-.05,pencil(d),.22)
for k in range(12): put(at('treinta')+k*.09,tick(1500,.035),.07)
for k in range(16): put(at('ochocientas')+k*.09,tick(1500,.035),.07)
put(at('el')-.05,thud(),.25); put(at('anota')+.05,thud(),.22); put(at('senala')+.1,thud(90),.2)
put(at('senala')+.1,chord([(261.6,1),(329.6,.7),(392,.6),(523.3,.35)]),.3)
for k in range(3): put(at('siempre')-.25+k*.25,pencil(.18),.25)
s0=at('cuantas')-.1; s1=at('pase',2)-.15
for k in range(20): put(s0+(s1-s0)*k/20,pencil(.1),.32)
put(at('canasta')-.05,thud(),.22); put(at('tres')-.05,chord([(392,1),(493.9,.6),(587.3,.5)],1.2),.25)
put(at('una',5)-.05,tick(900,.08),.18); put(at('senala',2)-.1,pencil(.6),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
