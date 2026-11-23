# Ficha · Historia compartible del Club Fundador

**Agente:** Irene (P1) · **Fecha:** 23/11/2026 · **Tarea:** `exp-historia-compartible` (abierta por Irene: es un entregable suyo en `agencia/experiencia/PLAN.md` sin tarea propia)
**Prototipo navegable:** https://claude.ai/artifact/58yvi6xKTFiYJ9VfYJMaba (móvil 375 y escritorio; selector de estado y de imagen; casilla «Marcar lo propuesto»; vista de las tres imágenes a tamaño Instagram con las zonas que tapa la interfaz)
**Imágenes propuestas (1080 × 1920):** `agencia/experiencia/prototipos/historia-compartible/compartir-papel.jpg` y `compartir-tinta.jpg`
**Base:** rama `revision/club-fundador` de proteamapp (PR #1): `founder/founder-section.tsx` (ventana de 3 pasos), `lib/founder.ts` (`FOUNDER_INSTAGRAM`, `FOUNDER_SHARE_IMAGE`), `public/club-fundador/compartir.jpg`; en Instagram, `stories/cocreacion1120/share.jpg`.

## 1. Qué se conserva (sin tocar)
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
1. **¿Papel, tinta o la actual?** Recomiendo papel: es la que más se distingue y la que mejor encaja con v3.
2. **@ de la imagen:** la cuenta provisional sigue sin decidir y `@app.proteam` está suspendida. La imagen lleva la @ escrita en el hueco: en cuanto haya cuenta, regenero el JPG (es una plantilla) y se cambia `FOUNDER_INSTAGRAM`.
3. **Número en público:** una segunda historia «Fundador Nº 011» al verificarse sería un buen motivo para volver a compartir, pero un número bajo deja adivinar cuántos somos. ¿Lo dejamos fuera mientras dure el misterio? (no está en el prototipo).
4. ¿Traducimos la imagen a los otros 6 idiomas o se queda en español?
5. ¿La misma imagen se usa también como historia de la cuenta (`stories/cocreacion1120/share.jpg`) para que todo el mundo reconozca el formato?
