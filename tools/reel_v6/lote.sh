#!/bin/bash
# Convierte explicativos v3 a v6 con el cierre nuevo. Uso: reel_v6/lote.sh ID:CORTE [ID:CORTE ...]
cd "$(dirname "$0")/.."
for p in "$@"; do id=${p%%:*}; ws=${p##*:}; reel_v6/build.sh $id >/dev/null && reel_v6/cierre.sh $id $ws; done
