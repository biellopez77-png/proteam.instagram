"""Efectos sintetizados de v6-reloj-24 «Diecinueve a dieciocho»: placas del marcador, pases suaves, aire en los movimientos de cámara, lápiz en la libreta y la hoja, un acorde suave en el 24 (ultravioleta) y los segundos del partidillo. Sin música. Sin golpes.
python3 sfx_v6-reloj-24.py v6-reloj-24/sfx.wav v6-reloj-24/times.js"""
import sys, json, numpy as np
src=open('../reel_v4/sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2]
exec(src)
DUR2=DUR+1.0; out=np.zeros(int(SR*(DUR2+1)))
def put(t,x,g):
    i=int(max(0,t)*SR); out[i:i+len(x)]+=x[:max(0,len(out)-i)]*g
def tick(f=1800,d=.05):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.exp(-tt*90)
def clack():
    n=int(.12*SR); y=bp(rng.standard_normal(n),300,2500)*np.exp(-np.arange(n)/SR*45); return y/(np.abs(y).max()+1e-9)
def chord(d=2.2):
    n=int(d*SR); tt=np.arange(n)/SR; y=sum(np.sin(2*np.pi*f*tt)*a for f,a in [(220,1),(277.2,.7),(329.6,.6),(440,.35)])
    return y*np.minimum(1,tt/.25)*np.exp(-tt*1.4)/2.6
put(0.0,clack(),.45); put(at('dieciocho')-.05,clack(),.45)
for t,d,g in [(at('nba')-.2,1.2,.3),(at('equipo')-.6,1.2,.4),(at('asi')-.1,1.3,.4),(at('cuarenta')-.4,1.0,.25),(at('buen')-.3,1.0,.25),
              (at('veinticuatro')-.3,1.0,.25),(at('1954'),1.6,.4),(at('media')-.3,1.0,.3),(at('piensa')-.5,1.1,.45),(at('cuantos')-.1,1.0,.3),
              (at('raya')-.5,.9,.25),(at('martes')-.2,1.1,.35),(at('apuntalo')-.3,1.4,.4)]:
    put(t,air(d),g)
put(at('asi')+.2,paper(.6),.3)
p0=at('equipo')+.45; p1=at('espera')+.75
for k in range(9): put(p0+(k+.85)*(p1-p0)/9,tick(900,.06),.12)
for w,d in [('cuarenta',.9),('buen',.9),('divide',.8)]: put(at(w)-.15,pencil(d),.28)
put(at('divide')+.3,pencil(.5),.3)
put(at('veinticuatro')-.05,chord(),.32)
for k in range(25): put(at('raya')-.15+(at('tiro')+.6-at('raya'))*k/25,pencil(.1),.35)
d0=at('doce'); d1=at('alta')+.2
for k in range(12): put(d0+(d1-d0)*k/12,tick(1500,.04),.1)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
