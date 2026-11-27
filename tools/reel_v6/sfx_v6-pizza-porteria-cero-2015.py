"""Efectos sintetizados de v6-pizza-porteria-cero-2015 «La pizza os la hacéis vosotros»: caída de los nueve goles en contra,
cartón de la caja que se abre, tiza del 0 en la tapa, golpe del 1 y acorde suave en el 0 ultravioleta, aire en los cambios,
amasado y lápiz en la cocina, tics de las doce porterías a cero, silencio en «la Premier», lápiz en la pizarra y tic del reloj. Sin música.
python3 sfx_v6-pizza-porteria-cero-2015.py ../reel_v4/v6-pizza-porteria-cero-2015/sfx.wav ../reel_v4/v6-pizza-porteria-cero-2015/times.js"""
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
g=at('goles')
for i in range(9): put(.05+i*(g+.3-.05)/9+.25,thud(170+i*5,.12),.18)
put(at('y')-.1,air(1.1),.35)
put(at('si')-.25,air(.9),.3)
put(at('cero')-.05,paper(.55),.4)
put(at('os')-.05,chalk(.6),.3)
put(at('jornada')-.3,air(.9),.3)
put(at('diez'),tick(1500,.06),.15)
put(at('uno'),thud(120,.25),.4)
put(at('cero',2)+.2,chord(2.0),.24)
put(at('la',2)-.35,air(1.2),.45)
put(at('y',2)-.2,pencil(.8),.22)
put(at('metieron'),paper(.9),.18)
put(at('cocina')-.1,pencil(.7),.22)
put(at('despues')-.3,air(.9),.3)
a=at('llegaron'); b=at('mas')+.1
for i in range(12): put(a+i*(b-a)/12+.1,tick(1300+i*40,.04),.1)
# corte seco en «Y en mayo, la Premier»: nada entre y3-0.1 y no-0.35
put(at('no')-.3,air(1.0),.35)
put(at('este')-.3,air(1.0),.3)
put(at('elige'),paper(.3),.2)
put(at('uno',2)-.2,air(.9),.25)
put(at('contar')-.1,pencil(1.0),.25)
m=at('marquen'); n_=at('minutos')+.2
for k in range(11): put(m+(n_-m)*k/10,tick(1700,.03),.08)
put(at('llega'),pencil(.4),.2)
put(at('celebra'),air(1.0,300,3000),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
