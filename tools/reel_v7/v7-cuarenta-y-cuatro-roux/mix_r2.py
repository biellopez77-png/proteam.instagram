"""r2 Roux (se ejecuta en el sandbox de Higgsfield). Base: v7-sistema-lobanovski/mix_r3.py.
old.mp4 = mezcla de la r1 (1565e42c-….mp4, 26,43 s): de ella solo se usa la historia, 0–22,38 s (voz entera, música y efectos tal cual).
mus1.mp3 = Epidemic «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» (la misma de la r1; su tercera vuelta entró a 20,4 s con off 1,0), que sigue en su sitio en el respiro y baja bajo el cierre.
sting.mp3 = Epidemic «Musical, Loop, Logo, Calm, Piano 01» (el sting de la r1), ahora con el cierre.
outro2.mp4 = tools/reel_v6/outro/outro2.mp4, su audio a 23,40 s (remate quieto hasta 22,9 s + fundido a negro de 0,5 s)."""
import subprocess,numpy as np
SR=48000; HX=22.38; XF=0.12; OUT2=23.40; DUR=OUT2+4.0
def ld(f,ch=2):
  r=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac',str(ch),'-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
  return np.frombuffer(r,np.float32).reshape(-1,ch).copy()
S=ld('old.mp4'); M=ld('mus1.mp3'); O=ld('outro2.mp4'); ST=ld('sting.mp3')
N=int(DUR*SR); t=np.arange(N)/SR; out=np.zeros((N,2))
rms=lambda x:np.sqrt(np.mean(x**2))
# 1 · historia tal cual, fundido cruzado a la música sola
i0=int(HX*SR); i1=int((HX+XF)*SR)
out[:i1]+=S[:i1]; out[i0:i1]*=np.linspace(1,0,i1-i0)[:,None]
# 2 · la música sigue en su sitio (posición en la pista = t − 20,4 + 1,0) al nivel que tenía
pos=lambda x:int((x-20.4+1.0)*SR)
a,b=int(22.08*SR),i0; g=rms(S[a:b])/rms(M[pos(22.08):pos(22.08)+(b-a)])
bed=np.zeros((N,2)); m=M[pos(HX):]; n=min(len(m),N-i0); bed[i0:i0+n]=g*m[:n]
bed[i0:i1]*=np.linspace(0,1,i1-i0)[:,None]
k=np.interp(t,[OUT2+.1,OUT2+.45,DUR-1.4,DUR],[1,.45,.45,0])   # baja bajo la voz del cierre y se apaga al final
out+=bed*k[:,None]
# 3 · cierre común outro2 (voz) al nivel de la voz de la historia + el sting de piano bajo
act=lambda x:np.sqrt(np.mean(x[np.abs(x[:,0])>.02]**2))
og=act(S[:int(22.0*SR)])/act(O)*0.95
j=int(OUT2*SR); n=min(len(O),N-j); out[j:j+n]+=og*O[:n]
st=ST[:int(4.0*SR)].copy(); f1=int(.3*SR); st[:f1]*=np.linspace(0,1,f1)[:,None]; f2=int(1.2*SR); st[-f2:]*=np.linspace(1,0,f2)[:,None]
n=min(len(st),N-j); out[j:j+n]+=.22*og*st[:n]
f=int((DUR-.25)*SR); out[f:]*=np.linspace(1,0,N-f)[:,None]
out/=max(1,np.abs(out).max()/.89)
print('g música %.3f  og %.3f  pico %.2f'%(g,og,np.abs(out).max()))
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','mix_r2.wav'],input=out.astype(np.float32).tobytes(),check=True)
