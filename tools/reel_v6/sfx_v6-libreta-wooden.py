"""Efectos sintetizados de v6-libreta-wooden «Dos mil trescientas veintiséis»: lápiz en ráfaga en la libreta, papel en las quince hojas,
aire en los movimientos de cámara, toques en los trofeos, lápiz de los investigadores, un acorde suave en la barra del 50,3 % (ultravioleta),
tic del cronómetro, una palmada suave en cada «así sí / así no / así sí» y lápiz en la hoja del sábado. Sin música. Sin golpes.
python3 sfx_v6-libreta-wooden.py v6-libreta-wooden/sfx.wav v6-libreta-wooden/times.js"""
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
def clap(d=.12):
    n=int(d*SR); y=bp(rng.standard_normal(n),900,3500); return y*np.exp(-np.arange(n)/SR*45)/(np.abs(y).max()+1e-9)
for k in range(26): put(.05+(at('veintiseis')+.6)*k/26,pencil(.08),.22)
for t,d,g in [(at('son'),1.2,.35),(at('ucla')-.4,1.2,.4),(at('dos',2)-.4,1.1,.4),(at('esperaban')-.4,1.1,.4),(at('la')-.1,1.4,.35),
              (at('cuando')-.3,1.1,.4),(at('ahora')-.5,1.1,.45),(at('cuantas'),1.0,.3),(at('este')-.3,1.1,.4),(at('apuntalo')-.3,1.4,.4)]:
    put(t,air(d),g)
for k in range(14): put(at('quince')-.1+k*(at('entrenamientos')+.5-at('quince'))/14,paper(.18),.12)
put(at('ultima')-.05,tick(900,.06),.15)
for k in range(9): put(at('nueve')-.1+k*.14,tick(1200+k*40,.04),.08)
for k in range(22): put(at('dos',2)+.1+(at('frase')+.4-at('dos',2))*k/22,pencil(.09),.22)
put(at('elogios',2),tick(700,.06),.12); put(at('broncas',2),tick(650,.06),.12)
put(at('esto')-.1,chord(),.3)
for k in range(21): put(at('casi')+.1+(at('segundos')-at('casi'))*k/20,tick(1500,.03),.06)
for w,n in [('asi',1),('asi',2),('asi',3)]: put(at(w,n)-.03,clap(),.22)
put(at('hacer',2)-.1,tick(900,.06),.15)
for k in range(31): put(at('instruccion')-.2+(at('martes')-.3-at('instruccion')+.2)*k/31,pencil(.1),.3)
put(at('martes')+.1,pencil(.4),.35)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
