#!/bin/bash
# Mezcla del u12: voz (loudnorm propio) + sfx 0,32 (amix normalize=0, alimiter) + música de fondo (segundo amix)
set -e
V=$1; OUT=$2   # V = vídeo mudo
ffmpeg -loglevel error -y -i voz.wav -af "loudnorm=I=-15:TP=-1.5:LRA=9" -ar 48000 voz_n.wav
ffmpeg -loglevel error -y -i voz_n.wav -i sfx.wav -filter_complex "[1]volume=0.32[s];[0][s]amix=inputs=2:normalize=0:duration=longest,alimiter=limit=0.95[a]" -map "[a]" -ar 48000 vs.wav
ffmpeg -loglevel error -y -i musica_alineada.wav -af "loudnorm=I=-16:TP=-2:LRA=11" -ar 48000 mus_n.wav
ffmpeg -loglevel error -y -i vs.wav -i mus_n.wav -filter_complex "[1]volume=0.26[m];[0][m]amix=inputs=2:normalize=0:duration=longest,alimiter=limit=0.95[a]" -map "[a]" -ar 48000 vsm.wav
ffmpeg -loglevel error -y -i $V -i vsm.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $OUT.con.mp4
ffmpeg -loglevel error -y -i $V -i vs.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $OUT.sin.mp4
echo ok
