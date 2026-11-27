"""Efectos sintetizados de v6-tiro-por-abajo-1962 «Veintiocho de treinta y dos»: lápiz en la hoja y el 28/32, tic del contador hasta 100,
aire en los cambios, bote y red en el tiro por abajo, el tiro cortado de «Y lo dejó», papel del libro, barras que suben y bajan,
lápiz en la hoja de libres y acorde suave en la barra ultravioleta. Sin música.
python3 sfx_v6-tiro-por-abajo-1962.py ../reel_v4/v6-tiro-por-abajo-1962/sfx.wav ../reel_v4/v6-tiro-por-abajo-1962/times.js"""
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
def swish(d=.35):
    n=int(d*SR); y=bp(rng.standard_normal(n),2500,9000); return y*env(n,1.2,.25)/(np.abs(y).max()+1e-9)
for i in range(5): put(.02+i*.06,pencil(.3),.18)
put(.1,pencil(.6),.3); put(at('treinta'),pencil(.5),.3); put(at('dos')-.05,pencil(.45),.3)
put(at('asi')-.1,air(1.1),.35)
c0=at('cien')-.05; c1=at('puntos')+.4
for k in range(20): put(c0+(c1-c0)*k/20,tick(1250+k*25,.03),.05)
put(at('esa')-.3,air(1.1),.4); put(at('esa'),pencil(1.0),.25)
put(at('dos',2)+.1,air(.6,400,4000),.25)
r1=at('dos',2)+.15+.85; put(r1,swish(),.4); put(r1+.35,thud(150,.2),.3); put(r1+.75,thud(150,.15),.18)
put(at('sesenta'),air(1.0,300,3000),.22); put(at('ciento')+.05,chord(2.2),.24)
put(at('y',3)+.1,air(.4,500,5000),.25)
put(at('en')-.05,paper(.4),.3); put(at('conto')-.05,paper(.6),.4); put(at('ridiculo')-.1,pencil(.5),.3)
put(at('acabo')-.3,air(1.0),.3)
d0=at('cincuenta'); 
for k in range(10): put(d0+k*.07,tick(1500-k*40,.03),.06)
put(at('rick')-.3,air(1.2,300,4000),.4)
n0=at('noventa')-.05
for k in range(18): put(n0+k*.04,tick(1100+k*40,.03),.05)
for t,d,g in [(at('y',5)-.35,1.1,.45),(at('quien')-.3,1.0,.4),(at('este')-.3,1.1,.4),(at('martes')-.2,1.0,.3)]: put(t,air(d),g)
a=at('segundo'); b=at('cada')+.2
for i in range(5): put(a+i*(b-a)/5,pencil(.3),.32)
put(at('deja'),pencil(.6),.35)
put(at('cuenta'),pencil(.45),.35); put(at('entra',2)-.1,air(.9,300,3000),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
