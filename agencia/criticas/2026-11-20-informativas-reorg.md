# Crítica · piezas informativas tras la suspensión — Andrés (05) · 20/11 11:55

Encargo de Biel (t-reorg-04-informativas). Miradas con tres preguntas: ¿una sola idea?, ¿se entiende en dos segundos sin saber nada de ProTeam?, ¿dice solo lo aprobado en `agencia/CLUB_FUNDADOR.md`? Todas están en **borrador**: no sale ninguna sin el visto bueno de Biel.

## Suspensión y cuenta provisional (`stories/reorg1120/`)
| Pieza | Nota | Comentario |
|---|---|---|
| r1 «Seguimos aquí.» | 80 | Una idea, sin drama y sin prometer fecha de vuelta. «Nos encuentras aquí» solo vale publicada en la cuenta provisional. |
| r2 «Club Fundador ProTeam» (cuenta provisional) | 78 · **espera el @** | Clara. Lleva «@cuenta_provisional» de relleno: no puede salir hasta que Biel dé el @ (`HANDLE=@cuenta python3 tools/reorg1120/gen.py`). |
| r3 «Nada cambia.» | 79 | Tres datos, los tres comprobados (lista hasta el 27, 3 meses gratis, sábado 28). |
| r4 Club Fundador (cinco ventajas) | 76 | Solo lo aprobado y sin precio fundador. Son cinco ideas en una pieza: mejor como resumen de cierre, después de b1–b3. «Invitaciones para amigos» necesita el visto bueno de Biel (regla del Club). |

## Club Fundador y lista de espera, una idea por pieza (nuevas, `stories/reorg1120/`)
| Pieza | Nota | Comentario |
|---|---|---|
| b2 «3 meses gratis.» | 82 | La más clara del pack: el número se lee antes que el texto. Condición y fecha en una frase. |
| b1 «Tu insignia. Tu número.» | 80 | El número va en blanco («Nº __») porque nadie tiene número todavía. Dice «tendrá», no «tiene»: la insignia aún no está publicada en la app. |
| b3 «Votas en lo que construimos.» | 78 | Frase aprobada. «Antes de decidir, preguntamos» no promete que el voto cambie nada. Las barras A/B van sin porcentajes: no hay resultados. |

## Pack de cocreación (`stories/cocreacion1120/`)
- Solo `share.jpg` nombraba @app.proteam. Ahora lleva un hueco en ese sitio (80). Con el @ nuevo: `HANDLE=@cuenta python3 tools/cocreacion1120/gen.py && python3 tools/cocreacion1120/render.py share`. La copia que usa la app (`public/club-fundador/compartir.jpg`) se cambia en el PR del equipo técnico.
- s1, s2, p1–p5, anuncio y club no nombran la cuenta: sirven tal cual.

## Para decidir (Biel)
1. **La dirección web en pantalla.** r3, r4 y b1–b3 llevan «pro-team.app». La marca dice «nunca URL en pantalla»; aquí se ha dejado porque la cuenta nueva no tiene historial y puede no tener aún el enlace en la bio. Si la bio lo tiene, se cambia por «enlace en la bio» en un minuto.
2. **Orden propuesto:** r1 → r2 → r3 el primer día; después b2, b1 y b3, una al día; r4 de cierre.

Riesgo de salto: bajo en r1, b1 y b2; medio en r3 y r4 (listas).
