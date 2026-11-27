"""Efectos suaves del u17 (sin voz): golpe en la zona tachada, papel del documento, clics de la sanción, barrido del reto."""
import sys, json, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR=48000; rng=np.random.default_rng(5)
T=json.loads(open('times.js').read().split('=',1)[1].split(';')[0]); out=np.zeros(int(SR*T['END']))
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],'bandpass',fs=SR,output='sos'),x)
def put(t,x,g): i=int(t*SR); x=x[:len(out)-i]; out[i:i+len(x)]+=x*g
def env(n,a,pk): t=np.linspace(0,1,n); return np.where(t<pk,(t/pk)**a,((1-t)/(1-pk))**1.6)
def paper(d=.3): n=int(d*SR); x=bp(rng.standard_normal(n),1200,6000); return x*env(n,1,.2)/np.abs(x).max()
def tick(f=2200): n=int(.03*SR); y=bp(rng.standard_normal(n),f*.5,f*1.6)*np.exp(-np.arange(n)/SR*260); return y/np.abs(y).max()
def whoosh(d=.45,lo=300,hi=3000):
    n=int(d*SR); x=rng.standard_normal(n); y=sum(bp(x,lo*(hi/lo)**(j/9)*.6,min(lo*(hi/lo)**(j/9)*1.6,SR/2-100))*np.exp(-((np.arange(n)/n-j/9)**2)/(2*.09**2)) for j in range(10)); return y*env(n,1.6,.55)/np.abs(y).max()
for i in range(5): put(T['no']+i*.06,tick(2600+150*i),.25)
put(T['no']+.7,whoosh(.35,3000,600),.3); put(T['no']+.85,whoosh(.35,3000,600),.3)
put(T['doc']-.05,whoosh(.4,2500,400),.25); put(T['doc']+.1,paper(),.4)
put(T['pen'],tick(1800),.3); put(T['pen']+.55,tick(1800),.3)
put(T['reto']-.08,whoosh(.45),.25); put(T['cta']-.08,whoosh(.45),.25)
out=out/np.abs(out).max()*.85; wavfile.write(sys.argv[1],SR,(out*32767).astype(np.int16)); print('ok')
