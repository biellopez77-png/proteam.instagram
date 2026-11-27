"""r3 Lobanovski (se ejecuta en el sandbox de Higgsfield).
src.mp4 = mezcla aprobada de la r1/r2 con el cierre antiguo (24f62949-….mp4, 28,07 s): de ella solo se usa la historia, 0–22,66 s (voz entera, «once» incluido).
mus2.mp3 = Epidemic «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02» (la misma de la mezcla, alineada en su posición: entró a 14,2 s), que sigue bajando en el respiro y bajo el cierre.
outro2.mp4 = tools/reel_v6/outro/outro2.mp4, su audio a 23,733 s (después del fundido a negro de 0,5 s)."""
import subprocess,numpy as np
SR=48000; HX=22.60; XF=0.12; OUT2=23.733; DUR=OUT2+4.0
def ld(f,ch=2):
  r=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac',str(ch),'-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
  return np.frombuffer(r,np.float32).reshape(-1,ch).copy()
S=ld('src.mp4'); M=ld('mus2.mp3'); O=ld('outro2.mp4')
N=int(DUR*SR); t=np.arange(N)/SR; out=np.zeros((N,2))
# 1 · historia tal cual (voz entera, «once» incluido), fundido cruzado a la música sola
i0=int(HX*SR); i1=int((HX+XF)*SR)
out[:i1]+=S[:i1]; out[i0:i1]*=np.linspace(1,0,i1-i0)[:,None]
# 2 · la música continúa en su sitio (entró a 14,2 s) y va bajando
o=int(14.2*SR); bed=np.zeros((N,2)); m=M[i0-o:]; n=min(len(m),N-i0); bed[i0:i0+n]=0.60*m[:n]
bed[i0:i1]*=np.linspace(0,1,i1-i0)[:,None]
k=np.ones(N); k*=np.interp(t,[22.60,22.75],[1,2.4])   # la cola del piano se sostiene en el respiro
k*=np.interp(t,[OUT2+.15,OUT2+.45,DUR-1.4,DUR],[1,.45,.45,0])   # baja bajo la voz del cierre y se apaga al final
out+=bed*k[:,None]
# 3 · cierre común outro2 (voz), al nivel de la voz de la historia
act=lambda x:np.sqrt(np.mean(x[np.abs(x[:,0])>.02]**2))
og=act(S[:int(22.4*SR)])/act(O)*0.95
j=int(OUT2*SR); n=min(len(O),N-j); out[j:j+n]+=og*O[:n]
f=int((DUR-.25)*SR); out[f:]*=np.linspace(1,0,N-f)[:,None]
out/=max(1,np.abs(out).max()/.89)
print('og',og,'pico',np.abs(out).max())
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','mix_r3.wav'],input=out.astype(np.float32).tobytes(),check=True)
