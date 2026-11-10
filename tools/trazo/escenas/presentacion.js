// Reel de presentación de Trazo (25 s, 1080x1920). Guion: brief del 10 nov.
(() => {
const W = 1080, H = 1920;
const MSGS = ['¿Mañana a qué hora?', 'Mi hijo no puede', '¿Quién trae balones?', '¿Hay entreno?', 'Pásame la alineación', '¿Y las fichas?', 'Llego tarde, míster', '¿El sábado a las 9?'];
const IT = [];
MSGS.forEach((m, i) => IT.push({ k: 'msg', l: m, t0: .5 + i * .42 }));
['plantilla_v7_FINAL.xlsx', 'cargas_OK2.xlsx', 'convocatoria(3).xlsx'].forEach((m, i) => IT.push({ k: 'excel', l: m, t0: 4.6 + i * .6 }));
IT.push({ k: 'libreta', l: '', t0: 7.2 });
IT.push({ k: 'nota', l: 'conos\n¡petos!', t0: 7.8 });
IT.push({ k: 'nota', l: '¿llamar a\nlos padres?', t0: 8.3 });
IT.push({ k: 'alerta', l: '!', t0: 8.8 });
IT.push({ k: 'alerta', l: '12', t0: 9.2 });
IT.forEach((it, i) => {
  it.x0 = 160 + T.rnd(i + 3) * 760; it.tx = 260 + T.rnd(i + 9) * 560; it.ty = 1000 + T.rnd(i + 21) * 330 - (i > 10 ? 120 : 0);
  it.r0 = (T.rnd(i + 5) - .5) * 1.4; it.r = (T.rnd(i + 7) - .5) * .6; it.col = i % 7;
});
// Microciclo
const DAYS = ['L', 'M', 'X', 'J', 'V', 'S', 'D'];
const BL = [['Recuperación', 'soft', 220], ['Fuerza', 'blue', 340], ['Táctica', 'blue', 400], ['Velocidad', 'blue', 280], ['Activación', 'soft', 180], ['Partido', 'ink', 520], ['Descanso', 'line', 130]];
const GX = 84, GW = 120, GG = 12, GY = 690;
const CAP = [
  [.15, 4.3, [['Cuarenta mensajes.']]],
  [4.45, 6.95, [['Tres Excel.']]],
  [7.05, 10.4, [['Una libreta'], ['\n'], ['que ya '], ['no se lee.', true]]],
  [13.0, 16.95, [['El entrenador de base'], ['\n'], ['también trabaja.', true]]],
  [17.05, 20.5, [['Merece orden.'], ['\n'], ['Merece '], ['su sitio.', true]]],
];
function caption(ctx, t) {
  for (const [a, b, segs] of CAP) {
    if (t < a || t > b) continue;
    const k = Math.min(T.out(T.seg(t, a, a + .3)), 1 - T.seg(t, b - .25, b));
    T.text(ctx, segs, W / 2, 380, 92, { a: k, dy: (1 - k) * 24 });
  }
}
function blockRect(i, t) {
  const g = T.back(T.seg(t, 12.2 + i * .12, 12.9 + i * .12));
  const x = GX + i * (GW + GG), h = BL[i][2] * g;
  return [x, GY + 40, GW, h, g];
}
function grid(ctx, t, a) {
  if (t < 12.1 || a <= 0) return;
  ctx.save(); ctx.globalAlpha = a;
  DAYS.forEach((d, i) => T.mono(ctx, d, GX + i * (GW + GG) + GW / 2, GY, 30, INK));
  BL.forEach((b, i) => {
    const [x, y, w, h, g] = blockRect(i, t); if (h < 2) return;
    T.rr(ctx, x, y, w, h, 22);
    if (b[1] === 'blue') { ctx.fillStyle = BLUE; ctx.fill(); } else if (b[1] === 'ink') { ctx.fillStyle = INK; ctx.fill(); }
    else if (b[1] === 'soft') { ctx.fillStyle = SOFT; ctx.fill(); } else { ctx.lineWidth = 4; ctx.strokeStyle = BLUE; ctx.setLineDash([12, 10]); ctx.stroke(); ctx.setLineDash([]); }
    if (h > 120) {
      ctx.save(); ctx.translate(x + w / 2, y + h - 22); ctx.rotate(-Math.PI / 2); T.font(ctx, 32, 800);
      ctx.fillStyle = (b[1] === 'soft' || b[1] === 'line') ? BLUE : '#fff'; ctx.textBaseline = 'middle'; ctx.globalAlpha = a * T.seg(t, 12.9 + i * .12, 13.3 + i * .12);
      ctx.fillText(b[0], 0, 0, h - 40); ctx.restore();
    }
  });
  ctx.restore();
}
window.SCENE = { w: W, h: H, dur: 25, fps: 30, draw(ctx, t) {
  T.board(ctx, W, H);
  const fin = T.ease(T.seg(t, 20.5, 21.8));          // salida hacia el logo
  // etiqueta superior
  ctx.save(); ctx.globalAlpha = 1 - fin;
  T.mono(ctx, t < 11.5 ? 'Martes · 23:47' : 'Microciclo · semana 12', W / 2, 250, 30, t < 11.5 ? MUTE : BLUE);
  ctx.restore();
  // Trazo
  const sinkK = T.ease(T.seg(t, 3.4, 10.2)), up = T.back(T.seg(t, 10.6, 11.3)), move = T.ease(T.seg(t, 12.0, 13.4));
  let pose = T.mix(T.POSES.line, T.POSES.stand, T.ease(T.seg(t, 1.5, 2.9)));
  pose = T.mix(pose, T.POSES.slump, sinkK * (1 - up));
  if (t >= 10.6) pose = T.mix(pose, T.POSES.raise, T.ease(T.seg(t, 10.6, 11.1)) * (1 - T.ease(T.seg(t, 12.6, 13.4))));
  if (t >= 17.2) pose = T.mix(pose, T.POSES.point, T.ease(T.seg(t, 17.2, 17.7)) * (1 - T.ease(T.seg(t, 19.6, 20.2))));
  if (t >= 20.5) pose = T.mix(pose, T.POSES.line, fin);
  let s = T.lerp(520, 330, move), hx = 540, hy = T.lerp(1150, 1520, move);
  hy += 170 * sinkK * (1 - up);
  if (t >= 20.5) { s = T.lerp(330, 180, fin); hy = T.lerp(1520, 1020, fin); hx = T.lerp(540, 552, fin); }
  const lineDraw = T.out(T.seg(t, 0, 1.4));
  const nod = t > 17.2 && t < 20.4 ? Math.sin((t - 17.2) * 5) * 6 : 0;
  // caos (detrás y encima de Trazo)
  const itemsBehind = [], itemsFront = [];
  IT.forEach((it, i) => {
    if (t < it.t0) return;
    let x, y, r, sc = 1, a = 1;
    const f = T.bounce(T.seg(t, it.t0, it.t0 + .75));
    x = T.lerp(it.x0, it.tx, f); y = T.lerp(-260, it.ty + 170 * sinkK * .6, f); r = T.lerp(it.r0, it.r, f);
    if (t >= 10.6) { const k = T.out(T.seg(t, 10.6, 11.2)); y -= 220 * k * (1 - T.seg(t, 11.3, 12)); r += (T.rnd(i) - .5) * k; }
    if (t >= 11.3) {
      const k = T.ease(T.seg(t, 11.3 + it.col * .06, 12.6 + it.col * .1)); const br = blockRect(it.col, Math.max(t, 13.5));
      const bx = br[0] + br[2] / 2, by = br[1] + 40 + (i % 3) * 60;
      x = T.lerp(x, bx, k); y = T.lerp(y, by, k) - Math.sin(k * Math.PI) * 260; r = T.lerp(r, 0, k); sc = T.lerp(1, .22, k); a = 1 - T.seg(k, .75, 1);
    }
    if (a > 0) (i % 3 === 0 && t < 11.3 ? itemsFront : itemsBehind).push([it, x, y, r, sc, a]);
  });
  itemsBehind.forEach(([it, x, y, r, sc, a]) => T.card(ctx, it.k, x, y, r, sc, a, it.l));
  grid(ctx, t, 1 - fin);
  if (t < 1.5) { // la línea nace
    const y = 1150 + .46 * 520, x0 = 540 - .62 * 520, x1 = 540 + .58 * 520;
    ctx.save(); ctx.strokeStyle = BLUE; ctx.lineCap = 'round'; ctx.lineWidth = 520 * .045; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(T.lerp(x0, x1, lineDraw), y); ctx.stroke(); ctx.restore();
  } else {
    const look = t < 10 ? Math.sin(t * 1.3) * .8 : 0;
    const blink = [3.2, 6.1, 14.4, 18.8].some(b => t > b && t < b + .12);
    if (fin < .98) T.trazo(ctx, pose, hx, hy + nod, s, { eyes: t > 2.7 && fin < .3, look, blink });
  }
  itemsFront.forEach(([it, x, y, r, sc, a]) => T.card(ctx, it.k, x, y, r, sc, a, it.l));
  // badge 40 (gancho del primer segundo)
  if (t < 11.6) {
    const k = T.back(T.seg(t, .1, .5)), a = 1 - T.seg(t, 11.0, 11.6);
    T.card(ctx, 'alerta', 800, 640 + 170 * sinkK * .3, .1, k, a, '40');
  }
  caption(ctx, t);
  // cierre: logo, ProTeam, pro-team.app
  if (t >= 20.5) {
    const lk = T.back(T.seg(t, 21.4, 22.1));
    T.logo(ctx, window.LOGO, W / 2, 860, 300 * lk, T.seg(t, 21.4, 21.8));
    const wk = T.out(T.seg(t, 22.0, 22.6));
    T.text(ctx, [['ProTeam']], W / 2, 1140 + (1 - wk) * 30, 130, { a: wk });
    const uk = T.out(T.seg(t, 22.5, 23.1));
    ctx.save(); ctx.globalAlpha = uk; T.mono(ctx, 'pro-team.app', W / 2, 1250, 40, BLUE); ctx.restore();
    const fk = T.out(T.seg(t, 23.2, 23.8));
    ctx.save(); ctx.globalAlpha = fk; T.font(ctx, 46, 'i'); ctx.fillStyle = INK; ctx.textAlign = 'center'; ctx.fillText('El entrenador de base también trabaja.', W / 2, 1420); ctx.restore();
  }
} };
})();
