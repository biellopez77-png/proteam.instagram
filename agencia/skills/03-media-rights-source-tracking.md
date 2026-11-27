# SKILL · Media Rights & Source Tracking (03 Resource Bank)
**Para qué:** saber de dónde sale cada recurso y bajo qué condiciones conocidas se usa. No es asesoría legal: es un registro honesto.

## Herramientas
`banco/INVENTARIO.csv` (columnas procedencia, autor, licencia, uso_comercial, enlace), API de Commons (`extmetadata`: `LicenseShortName`, `Artist`, `Credit`, `UsageTerms`, `AttributionRequired`), `intel/INDEX.csv` (campo `fuente`).

## Procedimiento
1. **En el momento de la descarga**, copia de la fuente: URL de la página del archivo (no la del JPG), autor tal como aparece, nombre corto de la licencia y fecha de consulta.
2. **Clasifica el origen:**
   - `propio` (capturas y grabaciones de ProTeam; material que pasa Biel).
   - `commons` / otra fuente con licencia leída.
   - `tercero-referencia` (vídeos de otras marcas guardados para analizar; **no se reutilizan** en piezas).
   - `desconocido` (no se usa en nada publicado).
3. **Estado de la licencia:** `comprobada <fecha>` solo si se ha leído en la fuente; si no, `sin comprobar` y el recurso queda `pendiente`.
4. **Obligaciones conocidas:** si la licencia pide atribución (CC BY, CC BY-SA), se anota el texto de crédito y dónde se pone (descripción del post). Si es «compartir igual», se anota. Si hay dudas sobre uso comercial o sobre la imagen de una persona, se escribe la duda tal cual: no se resuelve suponiendo.
5. **Personas reconocibles:** se usan como ejemplo editorial, nunca como aval (regla de MARCA.md). Nada que sugiera que esa persona usa o recomienda la app.
6. **Vídeos ajenos:** se analizan solo los que Biel facilite como archivo o los de acceso público descargables sin saltarse controles. No se evita ningún inicio de sesión, restricción de privacidad ni protección de plataforma. En `fuente` se anota la URL pública y quién aportó el archivo.
7. **Revisión:** en cada auditoría mensual, lista de recursos `sin comprobar` y de créditos pendientes.

## Qué nunca se escribe
Una licencia deducida («parece libre»), un autor inventado, «uso comercial: sí» sin haberlo leído.

## Control
¿Enlace a la página de origen? ¿Licencia leída y fechada? ¿Crédito necesario anotado? ¿Algún `desconocido` en una pieza publicada? (No puede haberlo.)
