"""Efectos sintetizados de v6-saque-banda-liverpool «El entrenador de los saques de banda»: aire en los movimientos de cámara, filas que caen,
la carta de la ficha, lápiz en el tachado y las rayas, un acorde suave en la barra del 68,4 % (ultravioleta), toques de pase y segundos del cronómetro. Sin música. Sin golpes.
python3 sfx_v6-saque-banda-liverpool.py v6-saque-banda-liverpool/sfx.wav v6-saque-banda-liverpool/times.js"""
import sys, json, numpy as np
src=open('../reel_v4/sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2]
exec(src)
DUR2=DUR+1.0; out=np.zeros(int(SR*(DUR2+1)))
def put(t,x,g):
    i=int(max(0,t)*SR); out[i:i+len(x)]+=x[:max(0,len(out)-i)]*g
def tick(f=1800,d=.05):
    n=int(d*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.exp(-tt*90)
def chord(d=2.2):
    n=int(d*SR); tt=np.arange(n)/SR; y=sum(np.sin(2*np.pi*f*tt)*a for f,a in [(220,1),(277.2,.7),(329.6,.6),(440,.35)])
    return y*np.minimum(1,tt/.25)*np.exp(-tt*1.4)/2.6
for t,d,g in [(at('temporada')-.3,1.2,.4),(at('verano')-.2,1.2,.4),(at('klopp'),1.0,.3),(at('ano')-.5,1.2,.4),(at('casi')-.6,1.2,.4),
              (at('trabajo',2)-.1,1.2,.3),(at('piensa')-.5,1.1,.45),(at('cuantos')-.1,1.0,.3),(at('este')-.1,1.0,.25),(at('martes')-.2,1.1,.35),(at('apuntalo')-.3,1.4,.4)]:
    put(t,air(d),g)
for k in range(19): put(at('temporada')+.1+k*.05,tick(700+k*15,.04),.06)
put(at('klopp')+.1,paper(.6),.35)
put(at('sesenta')-.1,chord(),.3)
put(at('largo')-.05,pencil(.3),.35); put(at('largo')+.15,pencil(.3),.35)
for w in ['ya','reciben']: put(at(w)-.05,tick(900,.06),.15)
for k in range(16): put(at('cuente')-.2+(at('perdido')+.3-at('cuente')+.2)*k/16,pencil(.1),.35)
d0=at('diez'); 
for k in range(int(at('apuntalo')-d0)): put(d0+k+1,tick(1500,.04),.1)
put(at('desmarcan'),tick(900,.06),.15)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
