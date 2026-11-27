# Re-monta vídeos: quita el cierre antiguo (últimos 5,6 s) y pega el nuevo cierre sin app.
import json, subprocess, sys, os
L = json.load(open('list.json'))
os.makedirs('out', exist_ok=True)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
# audio del cierre: voz + sting de piano (Epidemic) bajo
subprocess.run(['ffmpeg','-v','error','-y','-i','outro2.mp4','-i','sting.mp3','-filter_complex',
 '[1:a]aresample=48000,atrim=0:4.6,afade=t=in:d=0.3,afade=t=out:st=3.4:d=1.2,volume=0.22[s];[0:a]aresample=48000[v];[v][s]amix=inputs=2:normalize=0:duration=longest,apad=whole_dur=4.6[a]',
 '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-t','4.0','outro_full.mp4'],check=True)
for vid, url in L:
    src = f'src_{vid}.mp4'
    if not os.path.exists(src): subprocess.run(['curl','-sf','-o',src,url],check=True)
    D = dur(src); cut = round(D - 5.6, 3); x = 0.5
    f = (f"[0:v]fps=30,trim=0:{cut},setpts=PTS-STARTPTS,format=yuv420p[v0];[1:v]fps=30,setpts=PTS-STARTPTS,format=yuv420p[v1];"
         f"[v0][v1]xfade=transition=fade:duration={x}:offset={cut-x}[v];"
         f"[0:a]aresample=48000,atrim=0:{cut},asetpts=PTS-STARTPTS,afade=t=out:st={cut-0.7}:d=0.7[a0];[1:a]aresample=48000,asetpts=PTS-STARTPTS[a1];"
         f"[a0][a1]acrossfade=d={x}[a]")
    out = f'out/{vid}.mp4'
    r = subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-i','outro_full.mp4','-filter_complex',f,'-map','[v]','-map','[a]',
        '-c:v','libx264','-preset','veryfast','-b:v','4500k','-maxrate','6M','-bufsize','10M','-c:a','aac','-b:a','192k','-movflags','+faststart',out])
    print(vid, D, '->', round(dur(out),2) if r.returncode==0 else 'FAIL', flush=True)
