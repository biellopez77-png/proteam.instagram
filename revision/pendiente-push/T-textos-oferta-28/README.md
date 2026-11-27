# Textos públicos de la oferta: 3 meses solo con la lista, 1 mes desde el 28

Encargo de Biel (18/11, tarea `t-dir-copy-prueba`). Arreglo publicado (va a `main`).

## Qué cambia

Hasta el 27/11 a las 23:59 (Madrid) se lee **«3 meses gratis si te apuntas antes del 28 de noviembre»**; desde el 28/11 a las 00:00, **«1 mes de prueba»**. El cambio del 28 ya queda hecho: va por la fecha de `BLACKOUT_FRIDAY_END` (`src/lib/blackout-friday.ts`), la misma que usa la cuenta atrás de la portada. En ningún texto nuevo aparece el precio.

| Dónde | Antes | Hasta el 27/11 | Desde el 28/11 |
|---|---|---|---|
| Fútbol, baloncesto y balonmano: botón principal | «Empieza gratis 3 meses» | «Apúntate a la lista de espera» + debajo «3 meses gratis si te apuntas antes del 28 de noviembre» | «Empieza con 1 mes de prueba» |
| Ídem, preguntas frecuentes | «¿Cuánto cuesta?» con el precio y «3 meses gratis» | «¿Hay prueba gratis?» → «3 meses gratis si te apuntas antes del 28 de noviembre» | → «1 mes de prueba» |
| Ídem, descripción para Google | «… 3 meses gratis.» | sin oferta (Google la guarda semanas y quedaría vieja el 28) | igual |
| Blog: botón final (`PublicCta`) | «Probar ProTeam: primer equipo 3 meses gratis» | «Apúntate a la lista de espera» + la línea de la oferta | «Empieza con 1 mes de prueba» |
| Blog: frase final de los 3 artículos | «tu primer equipo, 3 meses gratis» | «… 3 meses gratis si te apuntas antes del 28 de noviembre» | «… 1 mes de prueba» |
| Excel de la plantilla (hoja «Leyenda») | «tu primer equipo, 3 meses gratis en pro-team.app» | «Prueba ProTeam App en pro-team.app: 3 meses gratis si te apuntas antes del 28 de noviembre.» | «…: 1 mes de prueba.» (el texto sale con la fecha de descarga) |

4 textos nuevos y 3 descripciones en los 7 idiomas (ca, es, en, fr, pt, de, it). Prueba nueva: `src/lib/public-offer.test.ts`.

## Aplicar

```bash
cd proteamapp
python3 /ruta/a/aplicar.py        # se niega si ya está aplicado o si algún fragmento no cuadra
bun run build                     # i18n:check + vite build
bunx vitest run src/lib/public-offer.test.ts
git add -A && git commit -m "Textos públicos: 3 meses solo con la lista antes del 28/11; 1 mes de prueba desde el 28"
git -c push.negotiate=true push && deploy_project
```

Comprobado (18/11, turno de las 8:17): el script sobre copias de los archivos leídos con `read_file` de Lovable (commit `1edfa1de`): 15 archivos, +84/−20 (`diff-de-prueba-sobre-fragmentos.txt`; en blog, Excel y rutas son fragmentos); sintaxis TS/TSX sin errores; los 5 textos de pantalla están en los 7 diccionarios. Falta `bun run build` en el repositorio real.

## El 28 por la mañana

Abrir /futbol y /blog/control-carga-baloncesto-rpe y comprobar que ya dicen «1 mes de prueba». Si alguna sigue con «3 meses» (caché), volver a publicar.
