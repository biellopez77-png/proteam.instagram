#!/bin/bash
# Monta reel.html a partir de las piezas (cabecera con la web de la lista, ayudantes, cuerpo del u72 y cierre de campaña)
cd "$(dirname "$0")"
{ cat _head.html; echo '<script src="/tools/reel72/times.js"></script>'; echo '<script>'; cat _helpers.js _body.js | sed '/^window.frame/,$d'; cat _web.js; sed -n '/^window.frame/,$p' _body.js; echo '</script></body></html>'; } > reel.html
