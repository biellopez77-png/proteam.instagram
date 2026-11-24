"""Efectos sintetizados de v6-panenka-1976 «Una cerveza o una chocolatina»: papel de la entrada que se rompe, toques del marcador de la tanda,
aire en los movimientos de cámara, un acorde suave en la parábola de la pica (ultravioleta), tic de las semanas, rebote de la chapa y la tableta,
toques de las tres paradas, tic del reloj que espera y lápiz en la hoja. Sin música. Sin golpes.
python3 sfx_v6-panenka-1976.py v6-panenka-1976/sfx.wav v6-panenka-1976/times.js"""
import sys, json, numpy as np
src=open('../reel_v4/sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2]
exec(src)
DUR2=DUR+1.0; out=np.zeros(int(SR*(DUR2+1)))
def put(t,x,g):
    i=int(max(0,t)*SR); out[i:i+len(x)]+=x[:max(0,len(out)-i)]*g
def tick(f=1800,d=.05):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.exp(-tt*90)
def chord(d=2.4):
    n=int(d*SR); tt=np.arange(n)/SR; y=sum(np.sin(2*np.pi*f*tt)*a for f,a in [(220,1),(277.2,.7),(329.6,.6),(440,.35)])
    return y*np.minimum(1,tt/.25)*np.exp(-tt*1.3)/2.6
def thud(f=140,d=.18):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt*(1-tt))*np.exp(-tt*28)
put(.0,paper(.5),.25)
for k in range(20): put(.05+(at('1976')+.4)*k/20,tick(1400+k*15,.03),.05)
put(at('checoslovaquia')-.35,paper(.7),.4)
s0=at('checoslovaquia')+.15; s1=at('tres')+.1
for k in range(8): put(s0+(s1-s0)*k/7,tick(900 if k<7 else 500,.07),.15)
for t,d,g in [(at('checoslovaquia')-.3,1.0,.3),(at('enfrente')-.3,1.1,.4),(at('panenka',2)-.35,1.1,.4),(at('llevaba')-.3,1.1,.4),
              (at('al')-.35,1.1,.4),(at('piensa')-.5,1.1,.45),(at('esta')-.1,1.0,.3),(at('sabado')-.2,1.1,.35),(at('apuntalo')-.3,1.4,.4)]:
    put(t,air(d),g)
put(at('enfrente')-.2,paper(.4),.25)
put(at('pica')-.05,chord(3.0),.3)
put(at('pica')-.05,air(1.6,400,3500),.25)
for k in range(30): put(at('llevaba')+.1+(at('club')-at('llevaba'))*k/30,tick(1600,.025),.05)
put(at('cerveza')+.05,thud(180),.35); put(at('chocolatina')+.05,thud(130),.35)
for w,n in [('principio',1),('paraba',1),('muchos',1)]: put(at(w,n)+.25,thud(110,.15),.3)
for k in range(6): put(at('espera')+k*.25,tick(1100,.04),.1)
put(at('se')-.05,air(.9,300,3000),.35)
for k in range(18): put(at('dice')-.05+(at('fallo')+.4-at('dice'))*k/18,pencil(.1),.25)
put(at('quien')-.1,pencil(.6),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
