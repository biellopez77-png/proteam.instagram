# Ficha · Historia compartible del Club Fundador

**Agente:** Irene (P1) · **Fecha:** 23/11/2026, rehecha en v4 el 24/11/2026 · **Tareas:** `exp-historia-compartible` y `irene-v4-paleta` (6/10)
**Prototipo navegable:** https://claude.ai/artifact/58yvi6xKTFiYJ9VfYJMaba (versión 2, v4; móvil 375 y escritorio; selector de estado, de imagen y de fechas; casilla «Marcar lo propuesto»; las tres imágenes a tamaño Instagram con lo que tapa la interfaz)
**Imágenes propuestas (1080 × 1920, v4):** `agencia/experiencia/prototipos/historia-compartible/compartir-peto.jpg` y `compartir-foco.jpg` (las de papel y tinta v3 se retiran del repo; quedan en el historial de git)
**Base:** rama `revision/club-fundador` de proteamapp (PR #1): `founder/founder-section.tsx` (ventana de 3 pasos), `lib/founder.ts` (`FOUNDER_INSTAGRAM`, `FOUNDER_SHARE_IMAGE`), `public/club-fundador/compartir.jpg`; en Instagram, `stories/cocreacion1120/share.jpg`.

## 0. Rehecho en v4 (24/11, sistema v4 de Biel del 23/11)

Mismas funciones, mismos textos y mismos estados que la versión v3; cambia la piel y la imagen.

**Confirmado (no cambia):** la ventana de `founder-section.tsx` entera (título, descripción, 3 pasos, «Compartir» solo con `navigator.share`, «Descargar imagen», campo, «Ya la he compartido» / «Actualizar solicitud», aviso de abajo), el RPC, los avisos y el mensaje de la imagen («¡Ya estoy dentro!» + «Formo parte del Club Fundador de ProTeam, la app para entrenadores.», insignia con rayo y sin número, mención, pro-team.app).

**Propuesto en v4:**
- Paleta: fondo #02050F, ventana #060C19, bloque del Club en la espera #0C1323 iluminado desde arriba (lo único con luz), Plus Jakarta Sans; azules #636DFF/#6AA8FF/#B9E0FF.
- La luz señala lo activo dentro de la ventana: el paso que toca se enciende (1 con el campo vacío, 3 al escribir el usuario); los hechos llevan una marca en hielo; el campo con foco, halo azul eléctrico. En revisión, los tres pasos hechos.
- **Ultravioleta una vez por pantalla:** en la espera, «Conseguir mi insignia» (sin solicitar o rechazada) o el rayo de la insignia verificada; en revisión, ninguno. Con la ventana abierta, solo el rayo de la insignia dentro de la imagen: la espera queda apagada bajo el velo y ningún botón de la ventana va en ultravioleta.
- **Imagen nueva v4, dos opciones** (sala a oscuras, una luz y un objeto real; todo entre y = 300 e y = 1540; la mención como línea de luz azul eléctrico discontinua, «tu mención aquí»):
  - **Peto (recomendada):** el peto azul colgado de una percha bajo un foco, con «PROTEAM · CLUB FUNDADOR», la insignia (rayo ultravioleta con filo blanco) y «¡Ya estoy dentro!» impresos en la tela; la frase de abajo como pie de foto. Encaja con IDENTIDAD.md §10 (objeto iluminado + texto escrito en el objeto).
  - **Foco:** la insignia sola bajo una lámpara de pabellón, «dentro!» en Instrument Serif cursiva como única voz. Más limpia, pero se acerca al «fondo oscuro + titular» que IDENTIDAD.md prohíbe.
- Estados: error de imagen con un **móvil boca abajo** (ilustración provisional) + «Reintentar»; error de envío dentro de la ventana en coral suave; «sin encontrar» en coral y «en revisión» en ámbar suaves, sin rojo.
- Selector de fechas en la línea de la espera: «El 11 de diciembre abrimos la app.» (supuesto de RELANZAMIENTO.md, por confirmar) frente a «El 28 de noviembre» del código. Ningún otro texto depende de la fecha.
- Las franjas que tapa Instagram se marcan en coral, no en rojo.

**Cómo se hicieron los JPG:** la imagen es un SVG de 1080 × 1920 dentro del prototipo (la misma función dibuja la vista previa, la galería y el JPG), renderizado con Chromium y Plus Jakarta Sans / Instrument Serif locales. Para cambiar la @ cuando haya cuenta provisional basta con cambiar `IG` y volver a renderizar.

**Dudas nuevas para Biel (v4):**
6. ¿Peto, foco o la actual? Recomiendo peto.
7. Objetos: el peto y el móvil boca abajo son dibujos provisionales. ¿Foto propia o con licencia (`banco/fotos`) o dibujo?
8. En la imagen, el ultravioleta va en el rayo de la insignia. ¿Correcto, o la historia (pieza pública) no debe gastar el ultravioleta?

## 1. Qué se conserva (sin tocar) — versión v3, vigente salvo lo del apartado 0
- La ventana entera y su orden: título «Tu insignia del Club Fundador», descripción, 3 pasos con sus textos, imagen, «Compartir» (solo si existe `navigator.share`) y «Descargar imagen», campo «Tu usuario de Instagram», «Ya la he compartido» / «Actualizar solicitud», aviso de abajo.
- La lógica: `normalizeInstagramHandle`, RPC `request_founder_badge`, toasts «¡Recibido! Revisamos tu historia y te avisamos.» y «No se ha podido enviar. Inténtalo de nuevo.», estados `requested` / `rejected` / `verified` con sus textos.
- Verificación a mano desde `/admin`. Pulsar «Compartir» no verifica nada.
- El mensaje de la imagen: «¡Ya estoy dentro!» + «Formo parte del Club Fundador de ProTeam, la app para entrenadores.», la insignia con **rayo** y sin número, la mención y `pro-team.app`.
- Una sola imagen para todos (archivo estático): ni nombre, ni número, ni dato del usuario.

## 2. Qué cambia (todo propuesto)
| Cambio | Por qué |
|---|---|
| **Imagen nueva** en dos versiones, «papel» (blanco) y «tinta», sin resplandor ni degradado; sistema v3: tinta, un azul, trazo a lápiz alrededor de la insignia, subrayado azul bajo «dentro!» | La actual parece una plantilla oscura con brillo; la nueva es de la casa y se distingue en la ronda de historias |
| **Hueco a lápiz «tu mención aquí · @app.proteam»** dentro de la imagen | Sin mención no hay insignia y la verificación es manual: el hueco le dice dónde pegar la pegatina @Mención y a nosotros nos facilita encontrarla |
| Todo el contenido entre y = 300 e y = 1540 | Instagram tapa los 250 px de arriba (progreso, perfil) y los 340 de abajo («Enviar mensaje») |
| Paso 2 con la ruta en Instagram: «Aa o pegatina → @Mención → app.proteam» | Muchos entrenadores no saben dónde está la pegatina de mención |
| Vista previa más grande al lado de los botones (124 px de ancho en móvil, 146 en escritorio; hoy 160 centrada, encima) y una línea de ayuda según el caso | Se ve qué se comparte sin bajar |
| Sin «Compartir» (ordenador o navegador sin `navigator.share`): «Desde el ordenador no se puede compartir directamente: descárgala, pásala al móvil y súbela a tu historia.» | Hoy, en el ordenador, solo aparece «Descargar» sin explicar el siguiente paso |
| **Error de imagen**: si `compartir.jpg` no carga (`onError` del `<img>`), hueco a lápiz con «No hemos podido cargar la imagen. Revisa tu conexión.» + «Reintentar», y los botones desactivados | Hoy se vería una imagen rota |
| **Error de envío** también dentro de la ventana, bajo el campo (además del toast) | El toast desaparece y la ventana no dice nada |
| Pasos ya hechos en azul cuando la solicitud está en revisión | Se ve en qué punto está |
| Estado vacío: con el campo vacío, el botón sigue desactivado (como hoy) y aparece la pista «El de tu cuenta, el mismo con el que subes la historia.» | Evita que escriban el nombre en vez del usuario |

## 3. Textos nuevos (todos para `t()` en los 7 idiomas)
- «Aa o pegatina» · «@Mención»
- «Al compartir, elige Instagram → Tu historia.»
- «Desde el ordenador no se puede compartir directamente: descárgala, pásala al móvil y súbela a tu historia.»
- «No hemos podido cargar la imagen.» · «Revisa tu conexión.» · «Reintentar» · «Sin la imagen no puedes compartirla todavía. Tu solicitud no se pierde.»
- «El de tu cuenta, el mismo con el que subes la historia.»
- En la imagen (no pasa por `t()`, es un JPG por idioma si se traduce): «PROTEAM · CLUB FUNDADOR», «tu mención aquí».
- Cambia el `alt` de la imagen si se adopta: «Imagen para compartir: «¡Ya estoy dentro!» con la insignia del Club Fundador y un hueco para tu mención».

## 4. Lo que NO aparece (a propósito)
Número de apuntados (misterio), número de fundador en la imagen (ver duda 3), precio fundador, tickets regalo, nombre de Biel, plazas limitadas.

## 5. Componentes y archivos afectados
- `public/club-fundador/compartir.jpg` → sustituir por la versión elegida (mismo nombre y tamaño, 1080 × 1920; sin cambios de código).
- `src/components/founder/founder-section.tsx` → paso 2 con la ruta, maquetación de la vista previa, texto según `canShare`, estado de error de imagen (`onError` + reintento con `?r=`), error de envío en línea (estado local de la mutación), pista del campo, pasos en azul si `requested`.
- `src/lib/i18n/dict/*.json` → textos nuevos y `alt`.
- Sin cambios en `lib/founder.ts`, RPC, migración ni `/admin`.
- Fuera de la app: `stories/cocreacion1120/share.jpg` del repo de Instagram, si se cambia la imagen también aquí.

## 6. Dudas para Biel
1. ~~¿Papel, tinta o la actual?~~ Sustituida por la duda 6 (v3 retirado).
2. **@ de la imagen:** la cuenta provisional sigue sin decidir y `@app.proteam` está suspendida. La imagen lleva la @ escrita en el hueco: en cuanto haya cuenta, regenero el JPG (es una plantilla) y se cambia `FOUNDER_INSTAGRAM`.
3. **Número en público:** una segunda historia «Fundador Nº 011» al verificarse sería un buen motivo para volver a compartir, pero un número bajo deja adivinar cuántos somos. ¿Lo dejamos fuera mientras dure el misterio? (no está en el prototipo).
4. ¿Traducimos la imagen a los otros 6 idiomas o se queda en español?
5. ¿La misma imagen se usa también como historia de la cuenta (`stories/cocreacion1120/share.jpg`) para que todo el mundo reconozca el formato?
