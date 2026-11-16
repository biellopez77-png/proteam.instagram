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
| ENTRENADOR | 46 |
| EQUIPO | 9 |
| INSTALACION | 8 |
| JUGADOR | 18 |
| OBJETO | 6 |
| PRODUCTO | 38 |
| STAFF | 13 |

## Reserva de «primer fotograma» (16/11)
Fotos de 1080 px de ancho o más, cara reconocible en el tercio superior y aire abajo para el texto. En el inventario llevan «primer fotograma» en la columna de uso.
- **Baloncesto:** `PROTEAM_ENTRENADOR_REFERENTE_FOTO_018` (Pablo Laso, 2026) y `_019` (Šarūnas Jasikevičius, 2024). Sin usar.
- **Balonmano:** `PROTEAM_JUGADOR_REFERENTE_FOTO_002` (Nikola Karabatić, 2019), `_003` (Dika Mem, 2019) y `PROTEAM_ENTRENADOR_REFERENTE_FOTO_020` (Talant Dujshebaev, 2012). Sin usar.
- **Fútbol:** `PROTEAM_ENTRENADOR_REFERENTE_FOTO_015` (Ancelotti, usada en u04), `_016` y `_017` (Luis de la Fuente, usadas en u05) y `PROTEAM_JUGADOR_REFERENTE_FOTO_001` (Lamine Yamal, usada en u05). **Faltan dos de fútbol sin usar**: en Commons, de Flick y Simeone solo hay ruedas de prensa y alfombras rojas recientes; se buscan con los recursos de u06 y u07.
- Todas son de Wikimedia Commons con licencia leída en la fuente (CC BY o CC BY-SA: atribución al publicar). Referentes como ejemplo, nunca como aval.

## Huecos por cubrir (prioridad)
1. **Vídeos**: no hay ninguno. Hacen falta clips verticales de entrenadores dando instrucciones, rondos, circuitos con conos, calentamientos, tiempos muertos y banquillos.
2. **Planificación y organización (C)**: libretas de entrenamiento, hojas de planificación, mesa de trabajo, ordenador con hoja de cálculo, anotaciones. En Commons libres casi no hay nada; lo mejor sería grabarlo o fotografiarlo nosotros.
3. **Análisis (D)**: analista con portátil o tablet, revisión de vídeo, pizarra táctica de fútbol sin personas.
4. **Contextos (E)**: vestuario de base, gimnasio, pabellón vacío, banquillo vacío.
5. **ProTeam**: grabaciones de pantalla de la navegación (planificación, registro de un partido en directo, informe). Ahora solo hay capturas fijas.
