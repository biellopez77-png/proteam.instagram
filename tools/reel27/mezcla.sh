#!/bin/bash
# Mezcla del u27 (sin voz): música nueva + sfx 0,32, nivel final -15 LUFS
set -e
V=$1; OUT=$2
ffmpeg -loglevel error -y -i musica_alineada.wav -i sfx.wav -filter_complex "[1]volume=0.32[s];[0][s]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-15:TP=-1.5:LRA=9,alimiter=limit=0.95[a]" -map "[a]" -ar 48000 mix.wav
ffmpeg -loglevel error -y -i $V -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $OUT.con.mp4
ffmpeg -loglevel error -y -i $V -i sfx.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $OUT.sin.mp4
echo ok
