"""Efectos sintetizados de v6-nueve-hidegkuti-1953 «El nueve que no jugaba de nueve»: lápiz en la camiseta y el 9, papel del programa,
tic del contador de años, lápiz en el mapa, golpe suave de las placas del marcador, aire en los cambios de cámara, acorde suave en el hueco
(ultravioleta), rebobinado, tic del cronómetro, rebote de los tres balones y lápiz en la regla final. Sin música.
python3 sfx_v6-nueve-hidegkuti-1953.py v6-nueve-hidegkuti-1953/sfx.wav v6-nueve-hidegkuti-1953/times.js"""
import sys, json, numpy as np
src=open('../reel_v4/sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2]
exec(src)
DUR2=DUR+1.0; out=np.zeros(int(SR*(DUR2+1)))
def put(t,x,g):
    i=int(max(0,t)*SR); out[i:i+len(x)]+=x[:max(0,len(out)-i)]*g
def tick(f=1800,d=.05):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.exp(-tt*90)
def chord(d=2.4):
    n=int(d*SR); tt=np.arange(n)/SR; y=sum(np.sin(2*np.pi*f*tt)*a for f,a in [(196,1),(246.9,.7),(293.7,.6),(392,.35)])
    return y*np.minimum(1,tt/.25)*np.exp(-tt*1.3)/2.6
def thud(f=140,d=.18):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt*(1-tt))*np.exp(-tt*28)
for k in range(8): put(.0+k*.14,pencil(.14),.25)
put(.2,pencil(.9),.3)
put(at('noviembre')-.2,paper(.6),.35)
y0=at('noviembre'); y1=at('1953')+.6
for k in range(18): put(y0+(y1-y0)*k/18,tick(1300+k*20,.03),.05)
for t,d,g in [(at('inglaterra',2)-.35,1.1,.4),(at('hungria')-.35,1.1,.4),(at('su')-.3,1.1,.4),(at('hidegkuti',2)-.35,1.1,.4),
              (at('ahora')-.5,1.1,.45),(at('su',2)-.2,1.0,.3),(at('este')-.1,1.0,.3)]:
    put(t,air(d),g)
for k in range(10): put(at('inglaterra',2)+k*.3,pencil(.2),.18)
put(at('seis')+.12,thud(120,.22),.45); put(at('tres')+.12,thud(100,.22),.45)
put(at('bajaba')-.1,pencil(.7),.3)
put(at('sigo')-.05,chord(2.4),.28)
put(at('me')-.2,air(.6,600,4000),.3)
for k in range(12): put(at('marco')+(at('minuto')+.3-at('marco'))*k/12,tick(1500,.03),.07)
for w,n in [('acabo',1),('tres',2),('goles',1)]: put(at(w,n)+.35,thud(160,.15),.35)
put(at('sigue')-.15,pencil(.6),.3); put(at('otro')-.15,pencil(.6),.3); put(at('antes')-.2,paper(.4),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
