"""Efectos suaves de A1 (fluido): soplos largos en los movimientos de cámara, lápiz en las rayas y la portería, un roce de papel. Sin golpes.
python3 sfx_a1.py a1/sfx.wav a1/times.js"""
import sys, json, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR=48000; rng=np.random.default_rng(7)
js=open(sys.argv[2]).read(); W=json.loads(js.split('WORDS=')[1].split(';')[0]); DUR=float(js.split('VEND=')[1].split(';')[0])+.7
out=np.zeros(int(SR*(DUR+1)))
def at(w,n=1):
    c=0
    for x in W:
        if x[0]==w:
            c+=1
            if c==n: return x[1]
def bp(x,lo,hi,o=2): return sosfilt(butter(o,[lo,hi],'bandpass',fs=SR,output='sos'),x)
def put(t,x,g):
    i=int(max(0,t)*SR); out[i:i+len(x)]+=x[:len(out)-i]*g
def env(n,a,peak):
    t=np.linspace(0,1,n); return np.where(t<peak,(t/peak)**a,((1-t)/(1-peak))**1.8)
def air(d,lo=180,hi=2200):
    n=int(d*SR); x=rng.standard_normal(n); y=np.zeros(n); k=8
    for j in range(k):
        f=lo*(hi/lo)**(j/(k-1)); y+=bp(x,f*.7,min(f*1.4,SR/2-100))*np.exp(-((np.arange(n)/n-j/(k-1))**2)/(2*.14**2))
    return y*env(n,1.5,.5)/(np.abs(y).max()+1e-9)
def pencil(d=.16):
    n=int(d*SR); y=bp(rng.standard_normal(n),1800,6500)*(1+.6*np.sin(np.arange(n)/SR*2*np.pi*38)); return y*env(n,1,.2)/(np.abs(y).max()+1e-9)
def paper(d=.5):
    n=int(d*SR); y=bp(rng.standard_normal(n),900,5000)*(rng.random(n)>.6); y=bp(y,800,6000); return y*env(n,1.2,.3)/(np.abs(y).max()+1e-9)
for t,d,g in [(at('lo')-.1,1.3,.5),(at('en')-.1,1.0,.4),(at('mundial')+.3,1.4,.4),(at('jens')-.1,1.4,.5),(at('alemania')-.2,1.2,.35),
              (at('ahora')-.2,1.4,.4),(at('veinte')+.1,1.2,.35),(at('desde')-.2,1.3,.45),(at('mismo')-.1,2.2,.35),(at('ella')-.2,1.6,.4),
              (at('dale')-.3,1.5,.4),(at('rayas')-.4,1.2,.35),(at('tu',3)-.2,1.6,.5),(at('apuntalo')-.3,1.4,.4)]:
    put(t,air(d),g)
put(at('tu',3),paper(),.35)
s=at('seis'); put(s-.35,pencil(.8),.35); put(s+.2,pencil(.7),.25)
a0=at('una',2)+.1; a1=at('gol')+.35
for k in range(9): put(a0+(a1-a0)*k/9,pencil(),.4)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
