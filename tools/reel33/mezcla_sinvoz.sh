#!/bin/bash
# Mezcla del u33 (Reel de datos sin voz): música (loudnorm) + efectos 0,32 (amix normalize=0, alimiter). Copia sin música = solo efectos.
set -e
V=$1; OUT=$2
ffmpeg -loglevel error -y -i musica_alineada.wav -af "loudnorm=I=-15:TP=-1.5:LRA=9" -ar 48000 mus_n.wav
ffmpeg -loglevel error -y -i mus_n.wav -i sfx.wav -filter_complex "[1]volume=0.32[s];[0][s]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]" -map "[a]" -ar 48000 ms.wav
ffmpeg -loglevel error -y -i $V -i ms.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $OUT.con.mp4
ffmpeg -loglevel error -y -i $V -i sfx.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $OUT.sin.mp4
echo ok
