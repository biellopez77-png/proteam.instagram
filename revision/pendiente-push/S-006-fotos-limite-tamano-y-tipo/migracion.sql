-- S-006 (20/11, turno 17:17 Madrid). Va como PR: toca la base de datos (storage).
-- El almacén de fotos de jugador no tenía límite de tamaño ni de tipo.
-- La app solo guarda y enseña .jpg/.png (src/lib/photos.server.ts, PHOTO_PATH_RE),
-- y la foto más grande guardada hoy pesa 2,1 MB (SQL 20/11: 1 objeto, image/jpeg).
-- Con 5 MB queda margen para fotos de móvil sin dejar subir archivos enormes.
UPDATE storage.buckets
SET file_size_limit = 5242880,               -- 5 MB
    allowed_mime_types = ARRAY['image/jpeg', 'image/png']
WHERE id = 'player-photos';
