"""Efectos sintetizados de v6-kempa-1954 «El segundo intento»: entrada que cae, tics del año, sello de Karlsruhe,
aire en los cambios, lápiz de la pista, bloqueo del 1.er intento, arco del 2.º, bote, salto, red y golpe en «Gol»
(medio segundo de silencio antes), firma «el Kempa», cronómetro del martes y tiza de la pizarra. Sin música.
python3 sfx_v6-kempa-1954.py ../reel_v4/v6-kempa-1954/sfx.wav ../reel_v4/v6-kempa-1954/times.js"""
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
def whoosh(d=.6): return air(d,400,4000)
put(0,paper(.6),.35); put(.45,thud(110,.2),.25)
a=at('mil'); b=at('cuatro')+.2
for i in range(10): put(a+i*(b-a)/10,tick(1500+i*30,.035),.07)
put(at('karlsruhe')+.15,thud(90,.22),.45)
put(at('alemania')-.2,air(.8),.3)
put(at('suecia')-.1,air(.5,300,2600),.2)
put(at('campeona'),tick(1200,.08),.12)
put(at('bernhard')-.4,air(1.1),.45)
put(at('bernhard')-.1,pencil(.9),.22)
put(at('levanta'),pencil(.6),.18)
put(at('el',3),whoosh(.7),.22)
put(at('mal'),thud(160,.16),.4)
put(at('calcula'),paper(.4),.15)
put(at('segundo')-.1,whoosh(1.3),.3)
put(at('no'),tick(1600,.06),.12)
put(at('horst')-.2,air(.9),.35)
d=at('diecinueve')
for k in range(10): put(d+.5*k/9,tick(1700,.03),.07)
put(at('salta'),whoosh(.6),.25)
put(at('coge'),thud(220,.1),.3)
put(at('lanza'),whoosh(.4),.3)
# medio segundo sin nada antes de «Gol»
put(at('gol'),thud(80,.35),.6); put(at('gol')+.02,bp(rng.standard_normal(int(.5*SR)),300,3000)*env(int(.5*SR),1,.1),.12)
put(at('hoy')+.1,pencil(1.6),.2)
put(at('el',7)-.05,pencil(.8),.25)
put(at('kempa',2)+.5,chord(2.0),.22)
put(at('salio')-.4,air(1.1),.45)
put(at('lo'),paper(.4),.15)
put(at('este')-.15,air(.9),.3)
a=at('diez')-.1; b=at('minutos')+.5
for k in range(11): put(a+(b-a)*k/10,tick(1700,.03),.08)
put(at('una'),pencil(1.2),.22)
put(at('falla'),thud(150,.14),.3)
put(at('otra'),paper(.35),.18)
put(at('otra')+.35,pencil(.5),.22)
put(at('vez')+.15,tick(2000,.07),.15)
put(at('la',5)-.35,air(1.0),.4)
put(at('funcione')-.1,chalk(.6),.25)
put(at('nombre',2)-.2,chalk(.6),.25)
put(at('invento')-.2,chalk(.6),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
