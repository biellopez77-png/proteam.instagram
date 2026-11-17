# Apartado «Análisis» del admin (encargo de Biel 17/11, prioridad 1)

Listo para aplicar en `biellopez77-png/proteamapp`. Este turno no tuvo acceso al repositorio (sin `add_repo`; `git clone` pide credenciales), así que no está subido ni publicado.

## Aplicar (2 minutos)
```bash
cd proteamapp
python3 ../proteam.instagram/revision/pendiente-push/T-admin-analisis/aplicar.py
bun run build                                   # i18n:check + vite build
bunx vitest run src/lib/admin-analytics.test.ts # 10 pruebas
git add -A && git commit -m "Admin: apartado Análisis (cuentas, lista de espera, facturación)" && git -c push.negotiate=true push
```
Después `deploy_project` y comprobar con un usuario no admin que `/admin` → «Análisis» dice «Accés denegat».

## Qué hay
- `src/lib/admin-analytics.ts`: cálculo puro (estado de facturación, filtros, serie por día/semana). 10 pruebas en `admin-analytics.test.ts` (pasan).
- `src/lib/admin-analytics.functions.ts`: `getPlatformAnalytics`, solo lectura. Comprueba `is_platform_admin` (igual que el resto del admin) **antes** de leer nada; sin migraciones, sin abrir RLS, sin datos de jugadores. Recorre todas las páginas de usuarios (no se queda en 1.000).
- `src/components/admin/analytics-section.tsx`: filtros (facturación; fechas de alta con 7 días / 30 días / todo y desde–hasta), 8 tarjetas, gráfica de altas (recharts, por día hasta 62 días y por semana si es más largo) y tabla de las cuentas filtradas (nombre, email, alta, estado; 50 primeras).
- `admin.tsx`: pestaña «Anàlisi» la primera del menú del admin (la pestaña por defecto sigue siendo «Comptes»); el menú pasa a `flex-wrap` para que las 5 pestañas quepan a 375 px.
- 41 textos nuevos en los 7 idiomas (`i18n-claves.json`; el script solo añade los que falten).

## Qué significa cada número (de la base de datos real, 17/11)
- **Cuentas registradas**: usuarios con login propio (`auth.users`), sin la cuenta de administrador. Los jugadores sin acceso no tienen login y no cuentan.
- **Cuentas activas**: han iniciado sesión en los últimos 30 días (`last_sign_in_at`). Hoy: 17 de 44.
- **Lista de espera**: clubs creados durante la campaña (concesión con la nota «Llista d'espera Blackout Friday», hoy 7) + `leads` con origen de lista de espera (hoy 0; no existe otra tabla de lista de espera).
- **Pagando**: suscripción de Stripe activa o con pago pendiente (hoy 0 en la BD).
- **Con código promocional**: `billing_source = manual` / `manual_active` o concesión activa de origen `manual_code` (hoy 3 clubs).
- **En prueba**: `subscription_status = trialing` (hoy 11 clubs).
- **Sin plan**: sin club, prueba caducada o suscripción cancelada.
Una cuenta con varios clubs toma el mejor estado (pagando > código > prueba > sin plan). Los cupones de descuento de Stripe sobre una suscripción pagada cuentan como «pagando».

## Sin comprobar aquí
`bun run build` completo y las capturas a 375 y 1280 px (hace falta el repositorio). Sí comprobado: tipos con `tsc --strict` contra stubs, las 10 pruebas, el escáner de i18n del repo sobre los archivos nuevos (0 textos sin clave, 0 plantillas con prosa) y el aviso de idioma cruzado de es/ca.
