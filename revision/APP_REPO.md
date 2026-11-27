# Código de la app (GitHub) — desde el 17/11

La app de Lovable está sincronizada con **biellopez77-png/proteamapp** (privado, rama `main`). Lo que se sube a `main` aparece en Lovable. Publicar en pro-team.app sigue siendo «Publicar» en Lovable (o `deploy_project` del conector, que no gasta créditos de IA).

Esto sustituye a `send_message` para los arreglos: el equipo técnico ya no espera créditos de Lovable, arregla en el código.

## Preparar el entorno en un turno

```bash
git clone --depth 1 https://github.com/biellopez77-png/proteamapp /home/claude/proteamapp
cd /home/claude/proteamapp
# bun.lock apunta a una caché privada de Lovable que el proxy no deja pasar:
# se cambia SOLO en local por el registro público y se restaura antes de subir.
sed -i -E 's#https://europe-west[0-9]+-npm.pkg.dev/lovable-core-prod/sandbox-npm-cache/#https://registry.npmjs.org/#g' bun.lock
bun install --frozen-lockfile
bun run build          # i18n:check + vite build: tiene que acabar sin errores
git checkout -- bun.lock
```

No usar `npm install`: trae versiones nuevas del plugin de Lovable y reescribe `src/routes/mcp.ts` y `src/routes/[.well-known]/…`.

## Reglas para tocar el código

1. Leer `AGENTS.md` del repositorio de la app y respetarlo. Nunca reescribir historia: nada de force push, rebase ni amend de lo ya subido.
2. **Arreglos pequeños y claros** (textos, traducciones, aria-labels, un fallo concreto con archivo y línea, estilos): directamente en `main`, solo si `bun run build` pasa y `git diff` toca únicamente lo necesario. Commit en castellano que diga qué se arregla.
3. **Cambios grandes** (base de datos, pagos/Stripe, autenticación, permisos/RLS, `supabase/`, más de ~5 archivos o funciones nuevas): rama `revision/<tema>` y pull request (`gh pr create`) para que Biel lo revise. Nunca en `main`.
4. Nunca tocar secretos, claves ni `.env`; nunca ejecutar migraciones contra la base de datos real; nunca `deploy_project` de un cambio grande sin que Biel haya fusionado el PR.
5. Antes de subir: `git checkout -- bun.lock` y `git status` limpio salvo los archivos del arreglo. Subir con `git -c push.negotiate=true push`.
6. Cada arreglo: fila en `REGISTRO.md` (fecha, ID, commit o PR, «0 créditos», resultado).
