# S-006 · Fotos de jugador: límite de tamaño y tipo

**Qué pasa:** el almacén `player-photos` (privado) no tiene `file_size_limit` ni `allowed_mime_types`
(SQL 20/11: ambos `NULL`). Las políticas `player_photos_staff_insert/update` dejan subir cualquier archivo
a la carpeta del equipo a cualquier miembro del cuerpo técnico, llamando a la API directamente:
un PDF, un vídeo de 2 GB o un SVG. La app solo usa `.jpg`/`.png` (`src/lib/photos.server.ts`, línea 6,
`PHOTO_PATH_RE`), así que el resto ocupa espacio y nunca se ve.

**Arreglo:** `migracion.sql` (una sola sentencia sobre `storage.buckets`): 5 MB y solo JPEG/PNG.
La foto más grande guardada hoy pesa 2,1 MB, así que no rompe nada existente.

**Cómo probar:** en la ficha de un jugador, subir una foto JPG del móvil → se guarda;
subir por API un PDF o un archivo de más de 5 MB → Supabase responde 413/400.

Va como PR (base de datos). Sin aplicar: la sesión programada no tiene acceso a proteamapp.
