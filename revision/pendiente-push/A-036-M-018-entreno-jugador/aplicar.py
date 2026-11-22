#!/usr/bin/env python3
"""A-036 y M-018 (mejora continua, sesiones y rutinas: entrenamiento del jugador, 20/11 10:17 Madrid).

Archivo: `src/routes/_authenticated/app.workout.$routineId.tsx` (pantalla a pantalla
completa donde el jugador hace la rutina; commit 32ecd1f leído con `read_file`).

A-036 (error): la pantalla guarda en el móvil un «entrenamiento en curso» nada más
abrirse (el `useEffect(() => persist(), [persist])` escribe en `localStorage` en el
primer render, antes de que el jugador toque nada). Si el jugador entra solo a mirar
la rutina, o toca «COMENÇAR» sin querer, y sale con la X, al volver a Inicio
(`app.index.tsx`) le sale encima de todo «Tens un entrenament en curs» con el
cronómetro contando desde entonces. Además, si la rutina ya no le llega
(`listRoutinesForMe` no la devuelve: borrada, pasada a borrador o fuera del equipo)
la pantalla se queda para siempre en «Carregant rutina…» y el aviso de Inicio le
manda una y otra vez ahí.
Arreglo: (1) no se guarda nada hasta la primera acción del jugador (serie, peso,
RPE, cronómetro, «Següent»); una sesión ya guardada sigue guardándose como hasta
ahora; (2) si la lista de rutinas ha cargado y esta no está, se borra la sesión
guardada y se vuelve a Inicio.

M-018 (accesibilidad/móvil): la X de salir mide 20 px (solo el icono) y las casillas
«Pes (kg)», «RPE…» no tienen la etiqueta enlazada al campo (el lector de pantalla
dice solo «campo de texto»). Arreglo: X de 44 px; `htmlFor`/`id` con `useId`;
`inputMode="decimal"` para que salga el teclado numérico en el móvil.

Sin textos nuevos, sin BD, sin servidor. 1 archivo.

Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
src = root / "src/routes/_authenticated/app.workout.$routineId.tsx"
code = src.read_text(encoding="utf-8")

subs = [
    # useId para enlazar etiquetas
    ('import { useCallback, useEffect, useRef, useState } from "react";',
     'import { useCallback, useEffect, useId, useRef, useState } from "react";'),
    # saber cuándo ha cargado la lista de rutinas
    ('  const { data: routines } = useQuery({ queryKey: ["routines"], queryFn: () => routinesFn() });',
     '  const { data: routines, isSuccess: routinesLoaded } = useQuery({ queryKey: ["routines"], queryFn: () => routinesFn() });'),
    # solo se guarda si ya había sesión o el jugador ha hecho algo
    ('  const savingRef = useRef(false);\n',
     '  const savingRef = useRef(false);\n'
     '  // A-036: no se guarda un «entrenamiento en curso» solo por abrir la pantalla.\n'
     '  const touchedRef = useRef(Boolean(persisted));\n'),
    ('  const persistSnapshot = useCallback((nextExIdx: number, nextStates: Record<number, ExState>) => {\n'
     '    writeWorkoutSession({',
     '  const persistSnapshot = useCallback((nextExIdx: number, nextStates: Record<number, ExState>) => {\n'
     '    if (!touchedRef.current) return;\n'
     '    writeWorkoutSession({'),
    # rutina que ya no llega: limpiar y volver a Inicio (hooks antes del return)
    ('  if (!routine) return <div className="p-8 text-center text-muted-foreground">Carregant rutina…</div>;',
     '  useEffect(() => {\n'
     '    if (!routinesLoaded || routine) return;\n'
     '    clearWorkoutSession(routineId);\n'
     '    navigate({ to: "/app", replace: true });\n'
     '  }, [navigate, routine, routineId, routinesLoaded]);\n'
     '\n'
     '  if (!routine) return <div className="p-8 text-center text-muted-foreground">Carregant rutina…</div>;'),
    # la primera acción marca la sesión como empezada
    ('  const patch = (p: Partial<ExState>) => setStates((s) => {\n',
     '  const patch = (p: Partial<ExState>) => setStates((s) => {\n'
     '    touchedRef.current = true;\n'),
    ('  function nextExercise(finalPatch?: Partial<ExState>) {\n',
     '  function nextExercise(finalPatch?: Partial<ExState>) {\n'
     '    touchedRef.current = true;\n'),
    # X de 44 px
    ('<button aria-label="Tornar a l\'inici" onClick={() => navigate({ to: "/app" })}><X className="h-5 w-5" /></button>',
     '<button aria-label="Tornar a l\'inici" onClick={() => navigate({ to: "/app" })} className="-ml-2 flex h-11 w-11 shrink-0 items-center justify-center"><X className="h-5 w-5" aria-hidden="true" /></button>'),
    # etiqueta enlazada y teclado numérico
    ('''  return (
    <div>
      <label className="text-sm font-medium">{label}</label>
      <input type="number" step={step} min={min} max={max}''',
     '''  const id = useId();
  return (
    <div>
      <label htmlFor={id} className="text-sm font-medium">{label}</label>
      <input id={id} type="number" inputMode="decimal" step={step} min={min} max={max}'''),
]

for old, new in subs:
    n = code.count(old)
    if n != 1:
        sys.exit(f"No encontrado una sola vez ({n}): {old[:70]!r}")
    code = code.replace(old, new)

src.write_text(code, encoding="utf-8")
print("A-036 y M-018 aplicados en", src)
