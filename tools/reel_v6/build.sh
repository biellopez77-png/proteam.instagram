#!/bin/bash
# Uso: tools/reel_v6/build.sh <id>   (desde la raíz del repo o tools)
set -e; cd "$(dirname "$0")/.."; id=$1; mkdir -p reel_v6/$id
[ "$id" = a1 ] || python3 reel_v6/reskin.py reel_v4/$id.html reel_v6/$id.html >/dev/null
ffmpeg -v error -y -i reel_v4/$id/voz.wav -i reel_v4/$id/sfx.wav -filter_complex "[0:a]volume=1.0[v];[1:a]volume=0.8[s];[v][s]amix=inputs=2:duration=longest:normalize=0[a]" -map "[a]" -ar 48000 reel_v6/$id/audio.wav
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 reel_v4/$id/final.mp4)
(cd blackout && python3 htmlreel.py video tools/reel_v6/$id.html /tmp/${id}raw.mp4 $D ../reel_v6/$id/audio.wav >/dev/null 2>&1)
ffmpeg -v error -y -i /tmp/${id}raw.mp4 -c:v libx264 -preset veryfast -b:v 4500k -maxrate 6M -bufsize 10M -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart reel_v6/$id/final.mp4
ffmpeg -v error -y -ss 1.0 -i reel_v6/$id/final.mp4 -frames:v 1 -q:v 3 reel_v6/$id/cover.jpg
rm -f /tmp/${id}raw.mp4; echo "ok $id $D"
