#!/bin/bash
# Mezcla v2: como mezcla.sh, pero la música baja (silencio de cine) justo antes de los dos momentos clave. Uso: mezcla2.sh <id> <t1> <t2>
set -e; cd "$(dirname "$0")/$1"; A=$2; B=$3
D=$(python3 -c "s=open('times.js').read();print(round(float(s.split('VEND=')[1].split(';')[0])+.7,2))")
ffmpeg -loglevel error -y -i voz.wav -af "loudnorm=I=-15:TP=-1.5:LRA=9" -ar 48000 voz_n.wav
ffmpeg -loglevel error -y -i voz_n.wav -i sfx.wav -filter_complex "[1]volume=0.32[s];[0][s]amix=inputs=2:normalize=0:duration=longest,alimiter=limit=0.95[a]" -map "[a]" -ar 48000 vs.wav
dip(){ echo "(1-0.85*clip((t-($1-0.7))/0.5,0,1)*clip(($1+1.2-t)/0.8,0,1))"; }
ffmpeg -loglevel error -y -i m1.mp3 -af "atrim=0:$D,afade=t=in:d=0.05,afade=t=out:st=$(python3 -c "print($D-1.4)"):d=1.4,loudnorm=I=-16:TP=-2:LRA=11,volume='$(dip $A)*$(dip $B)':eval=frame" -ar 48000 mus_n.wav
ffmpeg -loglevel error -y -i vs.wav -i mus_n.wav -filter_complex "[1]volume=0.26[m];[0][m]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]" -map "[a]" -ar 48000 vsm.wav
ffmpeg -loglevel error -y -i v.mp4 -i vsm.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest final.mp4
rm -f voz_n.wav vs.wav mus_n.wav vsm.wav; echo ok $1
