// «Trazo analiza» #2 · Barça 34–18 Caserío Ciudad Real (Liga Asobal, partido aplazado de la 3.ª jornada, 10 nov 2026).
// Datos: 18–8 al descanso; Sergey Hernández, 8 paradas (50 %) en la primera parte y 3 siete metros parados;
// marcador cada 5': 3-2, 9-3, 10-4, 12-5, 15-7, 18-8 (parcial 6–1 entre el 5 y el 10; 6–0 hasta el 7–2 del min 8).
// Fuentes: fcbarcelona.es (crónica y ficha), EFE (Infobae) y Lanza Digital.
// Zona útil: x 0–940, y 250–1500. Centro de composición CX = 500.
(() => {
const W = 1080, H = 1920, CX = 500;
const S = T.seg, E = T.ease, O = T.out;
const lerp2 = (a, b, t) => [T.lerp(a[0], b[0], t), T.lerp(a[1], b[1], t)];
const quad = (a, c, b, t) => lerp2(lerp2(a, c, t), lerp2(c, b, t), t);
function curve(a, c, b, n = 40) { const o = []; for (let i = 0; i <= n; i++) o.push(quad(a, c, b, i / n)); return o; }
function pathLen(pts) { let L = 0; for (let i = 1; i < pts.length; i++) L += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); return L; }
function stroke(ctx, pts, prog, o = {}) {
  if (prog <= 0 || pts.length < 2) return;
  const L = pathLen(pts), lim = L * T.clamp(prog);
  ctx.save(); ctx.strokeStyle = o.color ?? BLUE; ctx.lineWidth = o.lw ?? 8; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  ctx.globalAlpha = o.a ?? 1; if (o.dash) ctx.setLineDash(o.dash);
  ctx.beginPath(); ctx.moveTo(...pts[0]); let d = 0, end = pts[0], prev = pts[0];
  for (let i = 1; i < pts.length; i++) {
    const s = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
    if (d + s >= lim) { const f = (lim - d) / Math.max(s, 1e-6); end = lerp2(pts[i - 1], pts[i], f); prev = pts[i - 1]; ctx.lineTo(...end); break; }
    d += s; ctx.lineTo(...pts[i]); prev = pts[i - 1]; end = pts[i];
  }
  ctx.stroke(); ctx.setLineDash([]);
  if (o.head && prog > .15) {
    const ang = Math.atan2(end[1] - prev[1], end[0] - prev[0]), hl = (o.lw ?? 8) * 3.2;
    ctx.beginPath(); ctx.moveTo(end[0] - Math.cos(ang - .5) * hl, end[1] - Math.sin(ang - .5) * hl);
    ctx.lineTo(...end); ctx.lineTo(end[0] - Math.cos(ang + .5) * hl, end[1] - Math.sin(ang + .5) * hl); ctx.stroke();
  }
  ctx.restore();
}
function mono(ctx, s, x, y, size, color, a = 1, align = 'center') { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; T.mono(ctx, s, x, y, size, color, align); ctx.restore(); }
function fadeIO(t, a, b, f = .3) { return Math.min(O(S(t, a, a + f)), 1 - S(t, b - f, b)); }

// ---------- Pista de balonmano (40×20 m, vertical). El Barça defiende la portería de abajo y ataca la de arriba. ----------
let V = { x0: 320, y0: 460, k: 25, r: 26 };
const P = (mx, my) => [V.x0 + mx * V.k, V.y0 + my * V.k];
function areaPts(gy, dir, r) {
  const o = [];
  for (let i = 0; i <= 24; i++) { const a = Math.PI - (Math.PI / 2) * i / 24; o.push([-1.5 + r * Math.cos(a), gy + dir * r * Math.sin(a)]); }
  for (let i = 0; i <= 24; i++) { const a = Math.PI / 2 - (Math.PI / 2) * i / 24; o.push([1.5 + r * Math.cos(a), gy + dir * r * Math.sin(a)]); }
  return o.filter(p => Math.abs(p[0]) <= 10).map(p => P(...p));
}
function court(ctx, prog, a = 1) {
  if (prog <= 0 || a <= 0) return;
  const o = { color: '#b9c3d8', lw: 5, a };
  const [l, t] = P(-10, 0), [r, b] = P(10, 40);
  ctx.save(); ctx.globalAlpha = a * S(prog, 0, .3) * .9; ctx.fillStyle = '#f5f8ff'; ctx.fillRect(l, t, r - l, b - t); ctx.restore();
  stroke(ctx, [[l, t], [r, t], [r, b], [l, b], [l, t]], S(prog, 0, .55), o);
  stroke(ctx, [P(-10, 20), P(10, 20)], S(prog, .3, .6), o);
  for (const [gy, dir] of [[0, 1], [40, -1]]) {
    stroke(ctx, areaPts(gy, dir, 6), S(prog, .4, .8), o);
    stroke(ctx, areaPts(gy, dir, 9), S(prog, .5, .9), { ...o, dash: [10, 14] });
    stroke(ctx, [P(-.5, gy + dir * 7), P(.5, gy + dir * 7)], S(prog, .7, 1), o);
    ctx.save(); ctx.globalAlpha = a * S(prog, .7, 1); ctx.strokeStyle = INK; ctx.lineWidth = 7; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    const [g0, gyy] = P(-1.5, gy), [g1] = P(1.5, gy), d = -dir * V.k * .8;
    ctx.beginPath(); ctx.moveTo(g0, gyy); ctx.lineTo(g0, gyy + d); ctx.lineTo(g1, gyy + d); ctx.lineTo(g1, gyy); ctx.stroke(); ctx.restore();
  }
}
// Fichas: Barça = azul relleno; rival = aro de tinta.
function chip(ctx, x, y, kind, label = '', a = 1, sc = 1) {
  if (a <= 0) return;
  const r = V.r;
  ctx.save(); ctx.globalAlpha = a; ctx.translate(x, y); ctx.scale(sc, sc);
  ctx.shadowColor = 'rgba(13,15,20,.18)'; ctx.shadowBlur = 12; ctx.shadowOffsetY = 4;
  ctx.beginPath(); ctx.arc(0, 0, r, 0, 7);
  if (kind === 'b') { ctx.fillStyle = BLUE; ctx.fill(); ctx.shadowColor = 'transparent';
    if (label) { T.font(ctx, r * 1.05, 800); ctx.fillStyle = '#fff'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(label, 0, 2); } }
  else { ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.lineWidth = r * .24; ctx.strokeStyle = INK; ctx.stroke(); }
  ctx.restore();
}
function tag(ctx, x, y, s, a) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; T.font(ctx, 40, 800); ctx.fillStyle = INK; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic'; ctx.lineWidth = 10; ctx.strokeStyle = '#fff'; ctx.lineJoin = 'round'; ctx.strokeText(s, x, y); ctx.fillText(s, x, y); ctx.restore(); }
function ball(ctx, x, y, a = 1) { if (a <= 0) return; const r = V.r * .42; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = '#ff8a1f'; ctx.strokeStyle = INK; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.fill(); ctx.stroke(); ctx.restore(); }
function ring(ctx, p, t, t0, color = BLUE, R = 150) {
  const k = S(t, t0, t0 + .8); if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.globalAlpha = 1 - k; ctx.strokeStyle = color; ctx.lineWidth = 10;
  ctx.beginPath(); ctx.arc(p[0], p[1], 30 + R * O(k), 0, 7); ctx.stroke(); ctx.restore();
}

// Patrón (recreación): ataque rival contra 6:0 -> parada -> pase largo -> los dos extremos corren -> gol.
const DEF = [[-7.9, 35.9], [-5.3, 34.3], [-2, 33.3], [2, 33.3], [5.3, 34.3], [7.9, 35.9]];
const ATT = [[-9.2, 38.5], [-6.2, 29.8], [0, 28.6], [6.2, 29.8], [9.2, 38.5], [0, 31.8]];
const RET = [[-8.5, 26], [-5.5, 21], [0, 19.5], [4.5, 25], [8.5, 27], [1, 25]];
const RUN_R = [[7.9, 35.9], [9.6, 24], [6.8, 11]], RUN_L = [[-7.9, 35.9], [-9.6, 23], [-3.4, 8.6]];
function transition(ctx, u, a, labels = false) {
  if (a <= 0) return;
  const kp1 = S(u, .4, .9), kp2 = S(u, 1.1, 1.6), kShot = S(u, 1.9, 2.2), saved = u >= 2.2;
  const kRunR = E(S(u, 2.2, 4.5)), kRunL = E(S(u, 2.35, 4.95));
  const kLong = S(u, 2.7, 3.7), kP3 = S(u, 4.4, 4.9), kS2 = S(u, 5.0, 5.3), kRet = E(S(u, 2.6, 5.6));
  const side = T.lerp(-.5, .5, E(S(u, .4, 1.6)));               // la defensa bascula con el balón
  // carreras de los extremos (flechas discontinuas)
  const cr = curve(P(...RUN_R[0]), P(...RUN_R[1]), P(...RUN_R[2])), cl = curve(P(...RUN_L[0]), P(...RUN_L[1]), P(...RUN_L[2]));
  stroke(ctx, cr, kRunR, { color: BLUE, lw: 8, head: true, dash: [2, 20], a });
  stroke(ctx, cl, kRunL, { color: BLUE, lw: 8, head: true, dash: [2, 20], a });
  // rival
  const rb = lerp2(ATT[3], [5, 30.6], E(S(u, 1.1, 1.9)));
  ATT.forEach((p, i) => { const q = lerp2(i === 3 ? rb : p, RET[i], kRet); chip(ctx, ...P(...q), 'a', '', a); });
  chip(ctx, ...P(0, 1), 'a', '', a);                            // portero rival
  // Barça
  const posR = quad(P(...RUN_R[0]), P(...RUN_R[1]), P(...RUN_R[2]), kRunR), posL = quad(P(...RUN_L[0]), P(...RUN_L[1]), P(...RUN_L[2]), kRunL);
  DEF.forEach((p, i) => {
    if (i === 0) { chip(ctx, ...posL, 'b', labels ? '2' : '', a, 1 + .1 * Math.sin(kRunL * Math.PI)); return; }
    if (i === 5) { chip(ctx, ...posR, 'b', labels ? '1' : '', a, 1 + .1 * Math.sin(kRunR * Math.PI)); return; }
    const out = E(S(u, 2.6, 5.2)) * 3.5;
    chip(ctx, ...P(p[0] + side, p[1] - out), 'b', '', a);
  });
  const gk = P(T.lerp(0, .7, E(kShot)), 39.1);
  chip(ctx, ...gk, 'b', 'P', a, 1 + .18 * Math.sin(S(u, 2.1, 2.5) * Math.PI));
  // balón
  let bp = P(ATT[1][0] + .8, ATT[1][1] + .6);
  if (kp1 > 0) bp = lerp2(bp, P(ATT[2][0] + .8, ATT[2][1] + .6), E(kp1));
  if (kp2 > 0) bp = lerp2(P(ATT[2][0] + .8, ATT[2][1] + .6), P(rb[0] - .8, rb[1] + .6), E(kp2));
  if (kShot > 0) bp = lerp2(P(rb[0] - .8, rb[1] + .6), [gk[0], gk[1] - V.r * .9], O(kShot));
  if (saved) bp = [gk[0] + V.r * .7, gk[1] - V.r * .7];
  if (kLong > 0) bp = lerp2(bp, [posR[0] - V.r * .7, posR[1] - V.r * .7], E(kLong));
  if (kP3 > 0) bp = lerp2([posR[0] - V.r * .7, posR[1] - V.r * .7], [posL[0] + V.r * .7, posL[1] - V.r * .7], E(kP3));
  if (kS2 > 0) bp = lerp2([posL[0] + V.r * .7, posL[1] - V.r * .7], P(-.7, .1), O(kS2));
  ball(ctx, ...bp, kS2 >= 1 ? a * (1 - S(u, 5.3, 5.6)) : a);
}

// Tarjeta contador de la columna derecha
function counter(ctx, x, y, w, h, title, value, a, extra = null, sub = null, pop = 0) {
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a;
  ctx.shadowColor = 'rgba(13,15,20,.12)'; ctx.shadowBlur = 24; ctx.shadowOffsetY = 8;
  T.rr(ctx, x, y, w, h, 30); ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.lineWidth = 4; ctx.strokeStyle = '#d7e0f5'; ctx.stroke();
  ctx.restore();
  mono(ctx, title, x + w / 2, y + 48, 40, MUTE, a);
  const big = 132 * (1 + .1 * pop);
  T.text(ctx, [[String(value), true]], extra ? x + w * .3 : x + w / 2, y + 208, big, { a });
  if (extra) T.text(ctx, [[extra[0]]], x + w * .7, y + 192, 58, { a: a * extra[1] });
  if (sub) mono(ctx, sub, x + w / 2, y + h - 42, 40, INK, a);
}

// ---------- Gráfico: goles cada 5 minutos de la primera parte (ficha del partido) ----------
const PB = [3, 6, 1, 2, 3, 3], PC = [2, 1, 1, 1, 2, 1];
function chart(ctx, t, a, dx = 0) {
  if (a <= 0) return;
  const base = 1120, u = 75, gx = i => 165 + i * 115 + dx;
  stroke(ctx, [[100 + dx, base], [805 + dx, base]], S(t, 14.5, 15.1), { color: '#b9c3d8', lw: 5, a });
  // leyenda
  const la = a * O(S(t, 14.8, 15.3));
  ctx.save(); ctx.globalAlpha = la; T.rr(ctx, 112 + dx, 540, 40, 40, 8); ctx.fillStyle = BLUE; ctx.fill();
  T.font(ctx, 40, 800); ctx.fillStyle = INK; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText('Barça', 166 + dx, 562);
  T.rr(ctx, 325 + dx, 543, 34, 34, 8); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = INK; ctx.stroke();
  ctx.fillStyle = INK; ctx.fillText('Caserío', 376 + dx, 562); ctx.restore();
  // resalte del tramo 5'–10'
  const hk = O(S(t, 17.6, 18.1)), pulse = 1 + .015 * Math.sin(t * 5);
  if (hk > 0) { ctx.save(); ctx.globalAlpha = a * hk; ctx.translate(gx(1), 890); ctx.scale(pulse, 1);
    T.rr(ctx, -60, -290, 118, 520, 26); ctx.fillStyle = 'rgba(47,107,255,.12)'; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = BLUE; ctx.setLineDash([12, 12]); ctx.stroke(); ctx.restore(); }
  for (let i = 0; i < 6; i++) {
    const k = O(S(t, 15.0 + i * .4, 15.55 + i * .4)); if (k <= 0) continue;
    const hb = PB[i] * u * k, hc = PC[i] * u * k;
    ctx.save(); ctx.globalAlpha = a;
    T.rr(ctx, gx(i) - 54, base - hb, 50, hb, [10, 10, 0, 0]); ctx.fillStyle = BLUE; ctx.fill();
    T.rr(ctx, gx(i) + 7, base - hc, 44, hc, [10, 10, 0, 0]); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = INK; ctx.stroke();
    ctx.globalAlpha = a * k; T.font(ctx, 40, 800); ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = BLUE; ctx.fillText(String(Math.round(PB[i] * k)), gx(i) - 29, base - hb - 14);
    ctx.fillStyle = INK; ctx.fillText(String(Math.round(PC[i] * k)), gx(i) + 29, base - hc - 14);
    ctx.restore();
    mono(ctx, `${(i + 1) * 5}'`, gx(i), base + 48, 40, i === 1 && hk > 0 ? BLUE : MUTE, a * k);
  }
  if (hk > 0) {
    T.text(ctx, [['6–1', true]], 590 + dx, 740 + (1 - hk) * 20, 150, { a: a * hk });
    mono(ctx, 'del minuto 5 al 10', 590 + dx, 800, 40, INK, a * hk);
  }
}

// ---------- Mapa de portería (datos de ejemplo) ----------
const DOTS = [[.12, .2, 'p'], [.86, .78, 'g'], [.5, .5, 'p'], [.2, .82, 'p'], [.9, .15, 'g'], [.62, .3, 'p'], [.1, .55, 'g'], [.78, .52, 'p'], [.4, .86, 'g'], [.3, .28, 'p'], [.66, .64, 'g'], [.55, .12, 'p'], [.7, .84, 'p'], [.14, .9, 'g']];
function goalMap(ctx, t, a) {
  if (a <= 0) return;
  const x0 = 130, x1 = 730, y0 = 700, y1 = 1100, k = S(t, 23.4, 24.3);
  stroke(ctx, [[x0 - 70, y1], [x1 + 70, y1]], S(k, 0, .4), { color: '#b9c3d8', lw: 5, a });
  stroke(ctx, [[x0, y1], [x0, y0], [x1, y0], [x1, y1]], S(k, .1, 1), { color: INK, lw: 18, a });
  const gk = S(t, 23.9, 24.4);
  for (const f of [1 / 3, 2 / 3]) {
    stroke(ctx, [[T.lerp(x0, x1, f), y0 + 14], [T.lerp(x0, x1, f), y1]], gk, { color: '#b9c3d8', lw: 4, dash: [8, 12], a });
    stroke(ctx, [[x0 + 14, T.lerp(y0, y1, f)], [x1 - 14, T.lerp(y0, y1, f)]], gk, { color: '#b9c3d8', lw: 4, dash: [8, 12], a });
  }
  DOTS.forEach(([fx, fy, kind], i) => {
    const pk = T.back(S(t, 24.2 + i * .13, 24.5 + i * .13)); if (pk <= 0) return;
    const x = T.lerp(x0 + 30, x1 - 30, fx), y = T.lerp(y0 + 30, y1 - 22, fy);
    ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.arc(x, y, 20 * pk, 0, 7);
    if (kind === 'p') { ctx.fillStyle = BLUE; ctx.fill(); } else { ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 7; ctx.strokeStyle = INK; ctx.stroke(); }
    ctx.restore();
  });
  mono(ctx, 'Ejemplo', 430, 650, 40, MUTE, a * O(S(t, 23.6, 24.0)));
  const la = a * O(S(t, 24.4, 24.9));
  ctx.save(); ctx.globalAlpha = la; ctx.beginPath(); ctx.arc(190, 1168, 18, 0, 7); ctx.fillStyle = BLUE; ctx.fill();
  T.font(ctx, 40, 800); ctx.fillStyle = INK; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText('parada', 222, 1170);
  ctx.beginPath(); ctx.arc(440, 1168, 16, 0, 7); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 7; ctx.strokeStyle = INK; ctx.stroke();
  ctx.fillStyle = INK; ctx.fillText('gol', 472, 1170); ctx.restore();
}

const RULES = [
  [26.6, 28.5, [['6 contra 6 '], ['en 9 metros.', true]]],
  [28.5, 30.2, [['Si hay parada, '], ['salen dos.', true]]],
  [30.2, 31.5, [['Gol en '], ['3 pases o menos.', true]]],
];
const SEVEN = [[11.3, -1.1], [12.2, 1.1], [13.1, -.6]];           // tres 7 metros parados (recreación)

function trazoAt(ctx, pose, x, y, s, o = {}) {
  if (o.flip) { ctx.save(); ctx.translate(x, 0); ctx.scale(-1, 1); T.trazo(ctx, pose, 0, y, s, o); ctx.restore(); }
  else T.trazo(ctx, pose, x, y, s, o);
}

window.SCENE = { w: W, h: H, dur: 34.6, fps: 30, draw(ctx, t) {
  T.board(ctx, W, H);
  const P_ = T.POSES;

  // ---------- 0–3.5 s · gancho ----------
  const hookA = 1 - S(t, 3.3, 3.7);
  if (hookA > 0) {
    mono(ctx, 'Asobal · Barça 34–18 Caserío C. Real', CX, 330, 40, MUTE, hookA);
    const k1 = T.back(S(t, 0, .35)), k2 = T.back(S(t, .25, .6)), k3 = O(S(t, .8, 1.3));
    T.text(ctx, [['8', true], [' goles']], CX, 600 + (1 - k1) * 30, 150, { a: hookA * Math.min(1, k1 * 1.2) });
    T.text(ctx, [['en '], ['30', true], [' minutos.']], CX, 780 + (1 - k2) * 30, 118, { a: hookA * Math.min(1, k2 * 1.2) });
    T.text(ctx, [['Lo que encajó '], ['el Barça.', true]], CX, 950 + (1 - k3) * 20, 84, { a: hookA * k3 });
  }

  // ---------- Trazo (hilo conductor) ----------
  const toB = E(S(t, 3.5, 4.6)), toC = E(S(t, 14.1, 15.1)), toE = E(S(t, 26.2, 27.2)), fin = E(S(t, 31.5, 32.5));
  let hx = T.lerp(CX, 770, toB), hy = 1310, s = T.lerp(300, 260, toB);
  hx = T.lerp(hx, 850, toC); hy = T.lerp(hy, 1335, toC);
  hx = T.lerp(hx, 770, toE); hy = T.lerp(hy, 1040, toE); s = T.lerp(s, 420, toE);
  const RAISE = { ...P_.raise, elbowR: [.22, -.56], handR: [.3, -.8] };
  let pose = T.mix(P_.stand, RAISE, E(S(t, .5, .9)) * (1 - E(S(t, 2.6, 3.1))));
  const pt = Math.max(fadeIO(t, 6.7, 10.3, .4), fadeIO(t, 11.1, 13.9, .4), fadeIO(t, 15.2, 19.9, .4), fadeIO(t, 20.6, 22.9, .4), fadeIO(t, 23.6, 26.0, .4), fadeIO(t, 27.3, 31.3, .4));
  pose = T.mix(pose, P_.point, E(pt));
  const flip = t > 3.4;
  if (t > 31.5) { pose = T.mix(pose, P_.line, fin); hx = T.lerp(770, CX - 10, fin); hy = T.lerp(1040, 950, fin); s = T.lerp(420, 170, fin); }
  const nod = Math.sin(t * 2.2) * 4 * (t < 31.3 ? 1 : 0);
  const blink = [1.9, 5.6, 9.3, 12.7, 16.4, 21.8, 25.2, 29.4].some(b => t > b && t < b + .12);
  trazoAt(ctx, pose, hx, hy + nod, s, { flip, blink, look: t < 3.4 ? 0 : .7, eyes: fin < .3 });

  // ---------- 3.6–14.3 s · pizarra: el patrón ----------
  const boardA = Math.min(O(S(t, 3.6, 4.1)), 1 - S(t, 14.0, 14.4));
  if (boardA > 0) {
    V = { x0: 320, y0: 460, k: 25, r: 26 };
    court(ctx, S(t, 3.6, 4.7), boardA);
    mono(ctx, 'Recreación', CX, 290, 40, BLUE, boardA);
    const c1 = fadeIO(t, 4.5, 6.9), c2 = fadeIO(t, 6.9, 8.5), c3 = fadeIO(t, 8.5, 10.7), c4 = fadeIO(t, 10.9, 14.2);
    T.text(ctx, [['El rival '], ['lanza.', true]], CX, 400, 84, { a: c1 * boardA });
    T.text(ctx, [['Sergey '], ['para.', true]], CX, 400, 84, { a: c2 * boardA });
    T.text(ctx, [['Y el Barça '], ['corre.', true]], CX, 400, 84, { a: c3 * boardA });
    T.text(ctx, [['Y paró '], ['tres 7 metros.', true]], CX, 400, 84, { a: c4 * boardA });
    // jugada 1: parada y contraataque
    const pa = Math.min(O(S(t, 4.4, 4.9)), 1 - S(t, 10.4, 10.8)) * boardA;
    if (pa > 0) {
      transition(ctx, t - 4.7, pa);
      ring(ctx, P(.7, 39.1), t, 6.9, BLUE, 120); ring(ctx, P(0, 0), t, 10.0, BLUE, 150);
      const gk = P(.7, 39.1); tag(ctx, gk[0] - 118, gk[1] + 6, 'Sergey', pa * fadeIO(t, 6.9, 8.4, .25));
    }
    // jugada 2: tres 7 metros parados
    const sa = Math.min(O(S(t, 10.8, 11.2)), 1 - S(t, 13.9, 14.3)) * boardA;
    if (sa > 0) {
      [[-7.5, 'b'], [-5, 'a'], [-2.6, 'b'], [2.6, 'b'], [5, 'a'], [7.5, 'b']].forEach(([x, k]) => chip(ctx, ...P(x, 30 + Math.abs(x) * .12), k, '', sa));
      let gx = 0, bp = P(.5, 32.4), n = 0;
      SEVEN.forEach(([t0, dx]) => {
        const k = S(t, t0, t0 + .25), back = S(t, t0 + .45, t0 + .8);
        if (t >= t0) { gx = dx * E(k) * (1 - E(back)); if (k >= 1) n++; }
        if (t >= t0 && t < t0 + .8) bp = k < 1 ? lerp2(P(.5, 32.4), P(dx, 37.6), O(k)) : lerp2(P(dx, 37.6), P(dx * 2.4, 35.2), O(S(t, t0 + .25, t0 + .8)));
        ring(ctx, P(dx, 38), t, t0 + .25, BLUE, 90);
        const nk = S(t, t0 + .25, t0 + .9);
        if (nk > 0 && nk < 1) T.text(ctx, [[String(SEVEN.findIndex(x => x[0] === t0) + 1), true]], V.x0, 900 - O(nk) * 40, 380, { a: sa * (1 - nk) * .9 });
      });
      chip(ctx, ...P(0, 33), 'a', '', sa);                         // lanzador en los 7 m
      chip(ctx, ...P(gx, 38), 'b', 'P', sa, 1 + .15 * Math.abs(gx));
      ball(ctx, ...bp, sa);
      const pop = Math.max(...SEVEN.map(([t0]) => Math.sin(S(t, t0 + .25, t0 + .6) * Math.PI)));
      counter(ctx, 612, 795, 316, 250, '7 m parados', n, sa * O(S(t, 10.9, 11.3)), null, null, pop);
    }
    // contador de paradas
    const n8 = Math.max(0, Math.min(8, Math.ceil(S(t, 6.88, 8.3) * 8)));
    const pop8 = n8 > 0 && n8 < 8 ? .5 + .5 * Math.sin(t * 30) : Math.sin(S(t, 8.3, 8.7) * Math.PI);
    counter(ctx, 612, 480, 316, 290, 'Paradas', n8, boardA * O(S(t, 4.6, 5.1)), ['50 %', S(t, 8.3, 8.7)], '1.ª parte', pop8 * .6);
  }

  // ---------- 14.4–23.4 s · el dato: goles cada 5 minutos · y cómo lo ve ProTeam ----------
  const chartA = Math.min(O(S(t, 14.4, 14.9)), 1 - S(t, 23.0, 23.4));
  if (chartA > 0) {
    const dA = 1 - S(t, 20.0, 20.3), pA = O(S(t, 20.3, 20.7));
    mono(ctx, '1.ª parte · Barça–Caserío', CX, 290, 40, BLUE, chartA * dA);
    T.text(ctx, [['Goles cada'], ['\n'], ['5 minutos.', true]], CX, 380, 80, { a: fadeIO(t, 14.5, 17.6) * chartA });
    T.text(ctx, [['Se rompió'], ['\n'], ['en cinco minutos.', true]], CX, 380, 80, { a: fadeIO(t, 17.6, 20.2) * chartA });
    mono(ctx, 'Si te pasa en tu equipo', CX, 290, 40, BLUE, chartA * pA);
    T.text(ctx, [['ProTeam te enseña'], ['\n'], ['el parcial y la racha.', true]], CX, 380, 80, { a: fadeIO(t, 20.3, 23.3) * chartA });
    chart(ctx, t, chartA, -E(S(t, 23.0, 23.4)) * 120);
    // cursor de «en directo» que recorre el gráfico
    const ph = S(t, 20.7, 23.0);
    if (ph > 0 && ph < 1) { const x = T.lerp(110, 795, E(ph)); stroke(ctx, [[x, 610], [x, 1120]], 1, { color: RED, lw: 5, a: chartA * Math.min(1, ph * 8, (1 - ph) * 8) });
      ctx.save(); ctx.globalAlpha = chartA * Math.min(1, ph * 8, (1 - ph) * 8); ctx.fillStyle = RED; ctx.beginPath(); ctx.arc(x, 610, 12, 0, 7); ctx.fill(); ctx.restore(); }
    T.text(ctx, [['18–8 '], ['al descanso.', true]], 400, 1320, 80, { a: fadeIO(t, 18.6, 20.3) * chartA });
    const ra = fadeIO(t, 20.5, 23.2) * chartA;
    if (ra > 0) { ctx.save(); ctx.globalAlpha = ra * (.55 + .45 * Math.sin(t * 7) ** 2); ctx.fillStyle = RED; ctx.beginPath(); ctx.arc(150, 1262, 16, 0, 7); ctx.fill(); ctx.restore();
      T.text(ctx, [['Registro'], ['\n'], ['en directo.', true]], 190, 1280, 64, { a: ra, align: 'left' }); }
  }

  // ---------- 23.4–26.4 s · mapa de portería ----------
  const mapA = Math.min(O(S(t, 23.3, 23.7)), 1 - S(t, 26.1, 26.4));
  if (mapA > 0) {
    mono(ctx, 'Si te pasa en tu equipo', CX, 290, 40, BLUE, mapA);
    T.text(ctx, [['Y el mapa'], ['\n'], ['de portería.', true]], CX, 380, 80, { a: mapA });
    goalMap(ctx, t, mapA);
    const k = O(S(t, 24.8, 25.3));
    T.text(ctx, [['Dónde para.'], ['\n'], ['Dónde te marcan.', true]], 150, 1290 + (1 - k) * 16, 64, { a: mapA * k, align: 'left' });
  }

  // ---------- 26.4–31.6 s · el ejercicio del martes ----------
  const exA = Math.min(O(S(t, 26.4, 26.9)), 1 - S(t, 31.3, 31.6));
  if (exA > 0) {
    V = { x0: 330, y0: 480, k: 20, r: 21 };
    mono(ctx, 'Para el martes', CX, 290, 40, BLUE, exA);
    T.text(ctx, [['Parada '], ['y salida.', true]], CX, 405, 90, { a: exA });
    court(ctx, S(t, 26.4, 27.0), exA);
    transition(ctx, (t - 26.9) * 1.25, exA * O(S(t, 26.7, 27.0)));
    ring(ctx, P(.7, 39.1), t, 28.66, BLUE, 90); ring(ctx, P(0, 0), t, 31.14, BLUE, 110);
    for (const [a, b, segs] of RULES) { const k = fadeIO(t, a, b, .25); if (k > 0) T.text(ctx, segs, CX, 1400 + (1 - k) * 16, 60, { a: k * exA }); }
  }

  // ---------- 31.6–34.6 s · cierre ----------
  if (t > 31.6) {
    const lk = T.back(S(t, 32.1, 32.8));
    T.logo(ctx, window.LOGO, CX, 690, 260 * lk, S(t, 32.1, 32.5));
    const wk = O(S(t, 32.6, 33.2));
    T.text(ctx, [['ProTeam']], CX, 960 + (1 - wk) * 30, 120, { a: wk });
    const ck = O(S(t, 33.1, 33.7));
    T.text(ctx, [['Guárdalo para '], ['el martes.', true]], CX, 1130 + (1 - ck) * 20, 64, { a: ck });
    mono(ctx, '@app.proteam', CX, 1250, 40, MUTE, O(S(t, 33.6, 34.1)));
  }
} };
})();
