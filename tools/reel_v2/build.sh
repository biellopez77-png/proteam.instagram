#!/bin/bash
# Monta <id>/reel.html: cabecera común + tiempos + ayudantes + cuerpo + cierre de la lista de espera
cd "$(dirname "$0")"; k=$1
{ cat common/_head.html; echo "<script src=\"/tools/reel_v2/$k/times.js\"></script>"; echo '<script>'; cat common/_helpers.js $k/_body.js | sed '/^window.frame/,$d'; cat common/_web.js; sed -n '/^window.frame/,$p' $k/_body.js; echo '</script></body></html>'; } > $k/reel.html
