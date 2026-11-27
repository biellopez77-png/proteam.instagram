"""Mezcla r3 · v7-sexto-hombre-auerbach (sandbox de Higgsfield).
Misma mezcla de r1/r2 (voz de Mateo, música «Musical, Loop, Piano, Sentimental, Fast 02» y efectos de Epidemic) hasta 21,4 s
(mix.m4a, sacada del vídeo r1). Desde ahí la música sigue sola: la misma pista, en la misma posición (entra a 0,55 s; desfase
comprobado por correlación, r = 0,95) y con la ganancia ajustada (0,814), con fundido cruzado de 21,4 a 21,6 s, mientras el remate
se queda quieto en pantalla. A 22,5 s entra el audio del cierre (outro2 + sting «Logo, Calm, Piano 01» a 0,22: outro_full.mp4)
y la música baja hasta 24,7 s. Después: loudnorm −16,5 LUFS, +0,5 dB y limitador → −16,9 LUFS, −1,1 dBTP.
python3 mix_r3.py → mix_raw.wav"""
import subprocess, numpy as np
SR=48000; OUT=22.5; DUR=OUT+4.0
def ld(f):
    r=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout;return np.frombuffer(r,np.float32).reshape(-1,2).copy()
m=ld('mix.m4a'); u=ld('mus.mp3'); o=ld('outro_full.mp4')
N=int(DUR*SR)
a,b=int(21.2*SR),int(21.6*SR); i0=int((21.2-.55)*SR); x=u[i0:i0+(b-a),0]; y=m[a:b,0]; g=float((x@y)/(x@x))
mc=np.zeros((N,2)); st=int(.55*SR); n=min(N-st,len(u)); mc[st:st+n]=g*u[:n]
t=np.arange(N)/SR
w=np.clip((t-21.40)/.2,0,1)[:,None]
old=np.zeros((N,2)); k=min(N,len(m)); old[:k]=m[:k]
mus_env=np.clip((OUT+2.2-t)/2.2,0,1)[:,None]**1.5
mix=old*(1-w)+mc*w*mus_env
mix[int(OUT*SR):int(OUT*SR)+len(o)]+=o[:N-int(OUT*SR)]
fo=int((DUR-.5)*SR); mix[fo:]*=np.linspace(1,0,N-fo)[:,None]
mix=np.clip(mix,-1,1)
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','mix_raw.wav'],input=mix.astype(np.float32).tobytes(),check=True)
# ffmpeg -i mix_raw.wav -af loudnorm=I=-16.5:TP=-1.5:LRA=11 mix.wav; ffmpeg -i mix.wav -af "volume=0.5dB,alimiter=limit=0.88:attack=2:release=40:level=false" mix2.wav
# ffmpeg -i mudo.mp4 -i mix2.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest -movflags +faststart final.mp4
