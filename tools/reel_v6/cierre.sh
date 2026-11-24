#!/bin/bash
# Sustituye el final de un explicativo por el cierre común (outro/outro.mp4).
# Uso: tools/reel_v6/cierre.sh <id> <inicio de la palabra que se quita (s)>
set -e; cd "$(dirname "$0")"; id=$1; ws=$2; x=0.35
vs=$(python3 -c "print(round($ws-0.25,3))"); c=$(python3 -c "print(round($ws+0.25,3))"); o=$(python3 -c "print(round($c-$x,3))"); fo=$(python3 -c "print(round($ws-0.06,3))")
ffmpeg -v error -y -i $id/final.mp4 -i outro/outro.mp4 -filter_complex \
"[0:v]trim=0:$vs,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=0.5[v0];[1:v]setpts=PTS-STARTPTS[v1];[v0][v1]xfade=transition=fade:duration=$x:offset=$o[v];\
[0:a]atrim=0:$ws,asetpts=PTS-STARTPTS,afade=t=out:st=$fo:d=0.06,apad=whole_dur=$o[a0];[1:a]asetpts=PTS-STARTPTS[a1];[a0][a1]concat=n=2:v=0:a=1[a]" \
-map "[v]" -map "[a]" -c:v libx264 -preset veryfast -b:v 4500k -maxrate 6M -bufsize 10M -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart $id/publicar.mp4
echo "ok $id $(ffprobe -v error -show_entries format=duration -of csv=p=0 $id/publicar.mp4)"
