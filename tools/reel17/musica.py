"""Música nueva del u17 (sintetizada aquí: trap oscuro y minimalista, 143 BPM, 808, hi-hats con redobles,
pad oscuro en Re menor, silencio antes del golpe). python3 musica.py DROP END out.wav"""
import sys, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR=48000; DROP=float(sys.argv[1]); END=float(sys.argv[2]); OUT=sys.argv[3]
BPM=143; B=60/BPM; rng=np.random.default_rng(17)
N=int(SR*(END+.5)); L=np.zeros(N); R=np.zeros(N)
def bp(x,lo,hi,o=2): return sosfilt(butter(o,[lo,hi],'bandpass',fs=SR,output='sos'),x)
def lp(x,f,o=2): return sosfilt(butter(o,f,'low',fs=SR,output='sos'),x)
def hp(x,f,o=2): return sosfilt(butter(o,f,'high',fs=SR,output='sos'),x)
def put(t,x,g=1,pan=0):
    i=int(t*SR)
    if i>=N or i+len(x)<0: return
    x=x[:N-i]; L[i:i+len(x)]+=x*g*(1-pan); R[i:i+len(x)]+=x*g*(1+pan)
def kick():
    n=int(.35*SR); t=np.arange(n)/SR; f=45+110*np.exp(-t*35); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9)
def b808(freq,d):
    n=int(d*SR); t=np.arange(n)/SR; f=freq*(1+.6*np.exp(-t*30))
    y=np.tanh(1.8*np.sin(2*np.pi*np.cumsum(f)/SR))*np.minimum(1,t/.004)*np.exp(-t*1.1); y[-int(.02*SR):]*=np.linspace(1,0,int(.02*SR)); return y
def snare():
    n=int(.22*SR); t=np.arange(n)/SR; y=bp(rng.standard_normal(n),1500,7000)*np.exp(-t*22)+.5*np.sin(2*np.pi*190*t)*np.exp(-t*30); return y/np.abs(y).max()
def hat(d=.04):
    n=int(d*SR); y=hp(rng.standard_normal(n),7000)*np.exp(-np.arange(n)/SR*90); return y/np.abs(y).max()
def pad(freqs,d):
    n=int(d*SR); t=np.arange(n)/SR; y=sum(np.sin(2*np.pi*f*t+np.sin(2*np.pi*.3*t)*.4)+.3*np.sin(2*np.pi*f*2.003*t) for f in freqs)
    y=lp(y,1400); e=np.minimum(1,t/.8)*np.minimum(1,(d-t)/.6); return y*e/np.abs(y).max()
# pad (Re menor → Si bemol): todo el tema, bajo en el silencio
D=[146.83,174.61,220.0]; Bb=[116.54,146.83,174.61]
bar=4*B; t0=DROP-4*bar
k=0; t=0.0
while t<END:
    put(t,pad(D if k%2==0 else Bb,bar+.6),.16,0); t+=bar; k+=1
# antes del golpe: hats sueltos y nada de graves; 0,25 s de silencio total antes del DROP
t=DROP-8*B
while t<DROP-.25:
    if t>=0: put(t,hat(.03),.10,.3)
    t+=B/2
# silencio: se apaga el pad un instante
i0=int((DROP-.25)*SR); i1=int(DROP*SR); g=np.ones(N); g[i0:i1]=np.linspace(1,.0,i1-i0); g[i1:i1+int(.05*SR)]=np.linspace(0,1,int(.05*SR))
# a partir del DROP: patrón trap
notes=[73.42,73.42,58.27,65.41]
nb=int((END-DROP)/B)+1
for j in range(nb):
    tb=DROP+j*B
    if j%8 in (0,3,6): put(tb,kick(),.9)
    if j%4==2: put(tb,snare(),.45,-.1)
    if j%8==0: put(tb,b808(notes[(j//8)%4],B*3.2),.55)
    roll = (j%8==7)
    sub = 6 if roll else 2
    for s in range(sub): put(tb+s*B/sub,hat(.025),.12 if s%2==0 else .08,.25)
L*=g; R*=g
# golpe extra en el DROP
put(DROP,kick(),1.0); put(DROP,b808(73.42,B*4),.6)
# fundido de salida 1,2 s
fe=int(1.2*SR); e=int(END*SR); L=L[:e]; R=R[:e]; L[-fe:]*=np.linspace(1,0,fe); R[-fe:]*=np.linspace(1,0,fe)
y=np.stack([L,R],1); y=y/np.abs(y).max()*.89
wavfile.write(OUT,SR,(y*32767).astype(np.int16)); print('ok',OUT,round(len(L)/SR,2))
