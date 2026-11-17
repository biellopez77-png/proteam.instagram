# Banco de recursos audiovisuales ProTeam

Lo mantiene el **Agente 03 · ProTeam Resource Bank** (skill `proteam-resource-bank`). El inventario completo, con todas las columnas, está en `INVENTARIO.csv`: nombre, categoría, tema, descripción, deporte, plano, orientación, calidad, uso, procedencia, autor, licencia, uso comercial, enlace, ubicación y estado.

## Estructura
- `fotos/`: fotografías reales (entrenadores, staff, jugadores, equipos, instalaciones, objetos).
- `videos/`: clips y footage. **Está vacía de momento.**
- `proteam/`: capturas reales de la app, sin modificar.
- `INVENTARIO.csv`: una fila por recurso.

Nombres: `PROTEAM_CATEGORIA_TEMA_TIPO_NNN` (TIPO = FOTO, VIDEO, CAPTURA o GRABACION).
Estado: `disponible`, `usada en uNN` o `pendiente`.

> **Licencias:** las fotos de Commons con CC BY o CC BY-SA exigen atribución si se publican (decisión actual de Biel: son imágenes públicas y se usan como ejemplo, sin dar a entender respaldo). Las fotos de referentes aportadas por Biel no tienen la licencia comprobada.

## Recuento actual
| Categoría | Recursos |
|---|---|
| ENTRENADOR | 51 |
| EQUIPO | 22 |
| INSTALACION | 12 |
| JUGADOR | 26 |
| OBJETO | 6 |
| PARTIDO | 5 |
| PRODUCTO | 38 |
| STAFF | 15 |

## Reserva de «primer fotograma» (16/11)
Fotos de 1080 px de ancho o más, cara reconocible en el tercio superior y aire abajo para el texto. En el inventario llevan «primer fotograma» en la columna de uso.
- **Baloncesto:** `PROTEAM_ENTRENADOR_REFERENTE_FOTO_018` (Pablo Laso, 2026) y `_019` (Šarūnas Jasikevičius, 2024). Sin usar.
- **Balonmano:** `PROTEAM_JUGADOR_REFERENTE_FOTO_002` (Nikola Karabatić, 2019), `_003` (Dika Mem, 2019) y `PROTEAM_ENTRENADOR_REFERENTE_FOTO_020` (Talant Dujshebaev, 2012). Sin usar.
- **Fútbol:** `PROTEAM_ENTRENADOR_REFERENTE_FOTO_015` (Ancelotti, usada en u04), `_016` y `_017` (Luis de la Fuente, usadas en u05) y `PROTEAM_JUGADOR_REFERENTE_FOTO_001` (Lamine Yamal, usada en u05). **Faltan dos de fútbol sin usar**: en Commons, de Flick y Simeone solo hay ruedas de prensa y alfombras rojas recientes; se buscan con los recursos de u06 y u07. **16/11, tarde:** esa búsqueda no se ha podido hacer (sin acceso a Commons en la sesión); siguen faltando. Para u06 faltan además jugadores de un grande en carrera con chaleco GPS y un campo de base con petos; para u07, un entrenador de fútbol al final de un partido. Detalle y consultas preparadas en `agencia/recursos/2026-11-16-u06-…` y `…-u07-…`.
- **Nuevas del 16/11, 19:10 (Commons, licencia leída, miradas):** balonmano `PROTEAM_PARTIDO_EXCLUSION_ARBITRO_FOTO_001` (árbitro con los dos dedos, u25; con ella el banco de balonmano llega a 20 de 20). Baloncesto: `PROTEAM_PARTIDO_TIRO_LIBRE_NBA_FOTO_001` (u16), `PROTEAM_EQUIPO_TIEMPO_MUERTO_SELECCION_FOTO_001` y `PROTEAM_EQUIPO_TIEMPO_MUERTO_ACB_FOTO_001` (u20), `PROTEAM_JUGADOR_PIVOT_EUROLIGA_FOTO_001` (u26), `PROTEAM_EQUIPO_ENTRENAMIENTO_SELECCION_BALONCESTO_FOTO_001` (u13) y `PROTEAM_STAFF_BANQUILLO_NBA_FOTO_001` (u12). Ficha: `agencia/recursos/2026-11-16-fotograma0-fotos-nuevas.md`.
- **Nuevas del 16/11, 20:00 (Commons, licencia leída, miradas):** baloncesto `PROTEAM_EQUIPO_ENTRENAMIENTO_NBA_FOTO_001` (entrenamiento del All-Star de la NBA 2022, vertical; u13, segunda opción). Fútbol: `PROTEAM_INSTALACION_CANTERA_BARCA_FOTO_001` (campos de la cantera del Barça con porterías pequeñas, vertical 1080×1920; u14), `_002` (la misma entera en horizontal) y `PROTEAM_INSTALACION_LA_MASIA_FOTO_001` (letrero «LA MASIA»; u14). Sin menores reconocibles en ninguna.
- **Nuevas del 16/11, 21:00 (Commons, licencia leída, miradas):** fútbol `PROTEAM_JUGADOR_CORNER_BANDERIN_FOTO_001` (córner junto al banderín, Barça 2009; u24) y `PROTEAM_JUGADOR_CORNER_CHAMPIONS_FOTO_001` (córner en el Bernabéu, Champions 2010; u24). Balonmano: `PROTEAM_JUGADOR_PORTERO_SOLO_FOTO_001` (portero del Barça) y `_002` (portero del Kiel), los dos solos y en vertical (u23). Baloncesto: `PROTEAM_EQUIPO_BANQUILLO_NBA_HIELO_FOTO_001` (banquillo de la NBA con hielo en las rodillas; u22). Ficha: `agencia/recursos/2026-11-16-fotograma0-u22-u23-u24.md`.
- **Nuevas del 16/11, 23:55 (Commons, licencia leída, miradas):** baloncesto `PROTEAM_JUGADOR_REBOTE_NBA_FOTO_001` (pívot de los Lakers cerrando el rebote, vertical), `_002` (balón en el aire junto al aro) y `_003` (rebote cogido y rival que llega tarde, vertical), las tres para u26; `PROTEAM_EQUIPO_CALENTAMIENTO_SELECCION_USA_FOTO_001` (selección de EE. UU. tirando en media pista, u13); `PROTEAM_EQUIPO_BANQUILLO_SELECCION_USA_FOTO_001` y `PROTEAM_EQUIPO_TIEMPO_MUERTO_NBA_FOTO_001` (arranque del «ProTeam por dentro» de baloncesto). Fútbol: `PROTEAM_EQUIPO_ENTRENAMIENTO_REAL_MADRID_FOTO_001` (calentamiento en el Bernabéu, vertical; arranque de u30). Balonmano: `PROTEAM_PARTIDO_ARBITRO_EHF_FOTO_001` (árbitras de la EHF ante el vídeo; u25, opción 2).
- **Nuevas del 17/11, 10:55 (Commons, licencia leída a las 9:25, miradas):** baloncesto `PROTEAM_JUGADOR_BASE_REAL_MADRID_FOTO_001`, `_002` y `_003` (Théo Maledon con el Real Madrid, Euroliga 29/9/2026, verticales; u35). Sin usar.
- Todas son de Wikimedia Commons con licencia leída en la fuente (CC BY o CC BY-SA: atribución al publicar). Referentes como ejemplo, nunca como aval.

## Huecos por cubrir (prioridad)
1. **Vídeos**: no hay ninguno. Hacen falta clips verticales de entrenadores dando instrucciones, rondos, circuitos con conos, calentamientos, tiempos muertos y banquillos.
2. **Planificación y organización (C)**: libretas de entrenamiento, hojas de planificación, mesa de trabajo, ordenador con hoja de cálculo, anotaciones. En Commons libres casi no hay nada; lo mejor sería grabarlo o fotografiarlo nosotros.
3. **Análisis (D)**: analista con portátil o tablet, revisión de vídeo, pizarra táctica de fútbol sin personas.
4. **Contextos (E)**: vestuario de base, gimnasio, pabellón vacío, banquillo vacío.
5. **ProTeam**: grabaciones de pantalla de la navegación (planificación, registro de un partido en directo, informe). Ahora solo hay capturas fijas.
