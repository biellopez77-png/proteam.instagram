"""Efectos sintetizados de v6-uno-a-cero-1891 «Uno a cero con dieciocho en pista»: tiza en el 1–0, tic del contador de años,
lápiz en la pista, caída suave de los 18 alumnos, mimbre de las cestas, aire en los cambios, el balón que entra en la cesta,
botes del balón, lápiz en las rayas de la hoja y acorde suave cuando el tímido recibe (ultravioleta). Sin música.
python3 sfx_v6-uno-a-cero-1891.py ../reel_v4/v6-uno-a-cero-1891/sfx.wav ../reel_v4/v6-uno-a-cero-1891/times.js"""
import sys, json, numpy as np
src=open('../reel_v4/sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2]
exec(src)
DUR2=DUR+1.0; out=np.zeros(int(SR*(DUR2+1)))
def put(t,x,g):
    i=int(max(0,t)*SR); out[i:i+len(x)]+=x[:max(0,len(out)-i)]*g
def tick(f=1800,d=.05):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.exp(-tt*90)
def thud(f=140,d=.18):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt*(1-tt))*np.exp(-tt*28)
def chord(d=2.2):
    n=int(d*SR); tt=np.arange(n)/SR; y=sum(np.sin(2*np.pi*f*tt)*a for f,a in [(220,1),(277.2,.7),(329.6,.6),(440,.35)])
    return y*np.minimum(1,tt/.2)*np.exp(-tt*1.4)/2.6
def chalk(d=.3):
    n=int(d*SR); y=bp(rng.standard_normal(n),900,4000)*(rng.random(n)>.45); return y*env(n,1,.2)/(np.abs(y).max()+1e-9)
put(.05,chalk(.4),.3); put(.4,chalk(.25),.3); put(.5,chalk(.2),.25); put(.62,chalk(.5),.3)
put(at('asi')-.1,air(1.2),.35)
y0=at('diciembre'); y1=at('1891')+1.2
for k in range(20): put(y0+(y1-y0)*k/20,tick(1250+k*20,.03),.05)
put(at('dieciocho')-.4,air(1.1),.4)
put(at('dieciocho')-.3,pencil(.9),.25)
d0=at('dieciocho')-.05; d1=at('alumnos')+.4
for i in range(18): put(d0+i*(d1-d0)/18+.3,thud(180+i*4,.1),.12)
put(at('dos')-.2,pencil(1.4),.22)
put(at('cestas')+.2,paper(.35),.3); put(at('melocotones')+.3,paper(.35),.3)
put(at('canasta')+.12,paper(.5),.45); put(at('canasta')+.12,thud(110,.25),.35)
seg=(at('cada')+.3-at('imagina'))/4
for k in range(1,5): put(at('imagina')+k*seg,thud(170,.12),.25)
put(at('reglas')-.1,air(1.0,300,3000),.25)
for t,d,g in [(at('y',2)-.35,1.2,.45),(at('ahora',2)-.35,1.1,.4),(at('este')-.1,1.0,.3),(at('martes')-.2,1.1,.35)]: put(t,air(d),g)
put(at('este')+.1,paper(.4),.25)
for i in range(3): put(at('segundo')+i*.55,pencil(.25),.35)
put(at('tres',2)+.02,chord(2.2),.26)
a=at('cuenta')-.05; b=at('numero')-.05
for i in range(11): put(a+i*(b-a)/11,pencil(.12),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
