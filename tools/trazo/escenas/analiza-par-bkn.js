// «Trazo analiza» #3 · Partizan 80–66 Baskonia (Euroliga, jornada 11, Belgrado, 11 nov 2026).
// Datos: parciales por cuartos 23-18, 19-20, 23-22, 15-6 (42–38 al descanso, 65–60 al final del tercero);
// el Baskonia anotó 6 puntos en el último cuarto; Partizan mandó por dentro (Jekiri).
// Fuentes: EFE (crónica y ficha, vía Infobae), EITB Kirolak y Gigantes del Basket.
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
function label(ctx, s, x, y, size, color, a = 1, align = 'left', weight = 800) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; T.font(ctx, size, weight); ctx.fillStyle = color; ctx.textAlign = align; ctx.textBaseline = 'middle'; ctx.fillText(s, x, y); ctx.restore(); }

// ---------- Pista de baloncesto (FIBA: 15 m de ancho, media pista 14 m). M(x, d): x lateral, d = distancia a la línea de fondo ----------
let M = null, K = 54, R = 27;
const half = (x0, y0, k) => { K = k; R = k * .5; M = (x, d) => [x0 + x * k, y0 + d * k]; };
function arc3() { const o = [], a0 = Math.asin(1.415 / 6.75); for (let i = 0; i <= 40; i++) { const a = Math.PI - a0 - (Math.PI - 2 * a0) * i / 40; o.push(M(6.75 * Math.cos(a), 1.575 + 6.75 * Math.sin(a))); } return o; }
function court(ctx, prog, a = 1, depth = 12.6, closed = false) {
  if (prog <= 0 || a <= 0) return;
  const o = { color: '#b9c3d8', lw: 5, a };
  ctx.save(); ctx.globalAlpha = a * S(prog, 0, .3) * .9; ctx.fillStyle = '#f5f8ff';
  ctx.beginPath(); [M(-7.5, 0), M(7.5, 0), M(7.5, depth), M(-7.5, depth)].forEach((p, i) => i ? ctx.lineTo(...p) : ctx.moveTo(...p)); ctx.fill();
  ctx.globalAlpha = a * S(prog, .3, .7); ctx.fillStyle = 'rgba(47,107,255,.08)';
  ctx.beginPath(); [M(-2.45, 0), M(2.45, 0), M(2.45, 5.8), M(-2.45, 5.8)].forEach((p, i) => i ? ctx.lineTo(...p) : ctx.moveTo(...p)); ctx.fill(); ctx.restore();
  stroke(ctx, [M(-7.5, depth), M(-7.5, 0), M(7.5, 0), M(7.5, depth)], S(prog, 0, .55), o);
  stroke(ctx, [M(-2.45, 0), M(-2.45, 5.8), M(2.45, 5.8), M(2.45, 0)], S(prog, .3, .7), o);
  const ft = []; for (let i = 0; i <= 24; i++) { const g = Math.PI - Math.PI * i / 24; ft.push(M(1.8 * Math.cos(g), 5.8 + 1.8 * Math.sin(g))); }
  stroke(ctx, ft, S(prog, .5, .85), o);
  stroke(ctx, [M(-6.6, 0), M(-6.6, 2.99), ...arc3(), M(6.6, 2.99), M(6.6, 0)], S(prog, .4, 1), o);
  if (closed) {
    stroke(ctx, [M(-7.5, 14), M(7.5, 14)], S(prog, .3, .6), o);
    const cc = []; for (let i = 0; i <= 24; i++) { const g = Math.PI * i / 24; cc.push(M(1.8 * Math.cos(g), 14 - 1.8 * Math.sin(g))); }
    stroke(ctx, cc, S(prog, .5, .9), o);
  }
  const ka = a * S(prog, .7, 1);
  stroke(ctx, [M(-.9, 1.2), M(.9, 1.2)], 1, { color: INK, lw: Math.max(5, K * .13), a: ka });
  const c = M(0, 1.575); ctx.save(); ctx.globalAlpha = ka; ctx.strokeStyle = '#ff8a1f'; ctx.lineWidth = Math.max(4, K * .1); ctx.beginPath(); ctx.arc(c[0], c[1], K * .3, 0, 7); ctx.stroke(); ctx.restore();
}
// Fichas: Baskonia (y «tu equipo») = azul relleno; Partizan (rival) = aro de tinta.
function chip(ctx, p, kind, lab = '', a = 1, sc = 1) {
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a; ctx.translate(p[0], p[1]); ctx.scale(sc, sc);
  ctx.shadowColor = 'rgba(13,15,20,.18)'; ctx.shadowBlur = 12; ctx.shadowOffsetY = 4;
  ctx.beginPath(); ctx.arc(0, 0, R, 0, 7);
  if (kind === 'b') { ctx.fillStyle = BLUE; ctx.fill(); ctx.shadowColor = 'transparent'; }
  else { ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.lineWidth = R * .24; ctx.strokeStyle = INK; ctx.stroke(); }
  if (lab) { T.font(ctx, R * 1.05, 800); ctx.fillStyle = kind === 'b' ? '#fff' : INK; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(lab, 0, 2); }
  ctx.restore();
}
function tag(ctx, x, y, s, a) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; T.font(ctx, 42, 800); ctx.fillStyle = INK; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic'; ctx.lineWidth = 12; ctx.strokeStyle = '#fff'; ctx.lineJoin = 'round'; ctx.strokeText(s, x, y); ctx.fillText(s, x, y); ctx.restore(); }
function ball(ctx, p, a = 1) { if (a <= 0) return; const r = R * .46; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = '#ff8a1f'; ctx.strokeStyle = INK; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(p[0], p[1], r, 0, 7); ctx.fill(); ctx.stroke(); ctx.restore(); }
function ring(ctx, p, t, t0, color = BLUE, RR = 150) {
  const k = S(t, t0, t0 + .8); if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.globalAlpha = 1 - k; ctx.strokeStyle = color; ctx.lineWidth = 10;
  ctx.beginPath(); ctx.arc(p[0], p[1], 30 + RR * O(k), 0, 7); ctx.stroke(); ctx.restore();
}
function cross(ctx, p, k, a) { if (k <= 0 || a <= 0) return; const r = 34 * T.back(k); ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = RED; ctx.lineWidth = 12; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(p[0] - r, p[1] - r); ctx.lineTo(p[0] + r, p[1] + r); ctx.moveTo(p[0] + r, p[1] - r); ctx.lineTo(p[0] - r, p[1] + r); ctx.stroke(); ctx.restore(); }
const mm = (p, dx = 0, dy = 0) => M(p[0] + dx, p[1] + dy);

// ---------- Recreación 1: Partizan ataca la pintura (bloqueo directo y continuación) ----------
function pnr(ctx, u, a) {
  if (a <= 0) return;
  const kScr = E(S(u, .1, .9)), kDrv = E(S(u, 1.0, 2.0)), kRoll = E(S(u, 1.3, 2.35)), kPass = S(u, 2.1, 2.5), kShot = S(u, 2.6, 2.9);
  const drv = [[0, 9.6], [2.7, 9.3], [3.1, 6.9]], rol = [[1.0, 8.8], [-.7, 6.2], [.5, 2.8]];
  stroke(ctx, curve(M(...drv[0]), M(...drv[1]), M(...drv[2])), kDrv, { color: INK, lw: 7, head: true, dash: [2, 18], a: a * .8 });
  stroke(ctx, curve(M(...rol[0]), M(...rol[1]), M(...rol[2])), kRoll, { color: INK, lw: 7, head: true, dash: [2, 18], a: a * .8 });
  const a1 = quad(drv[0], drv[1], drv[2], kDrv);
  const a5 = kRoll > 0 ? quad(rol[0], rol[1], rol[2], kRoll) : lerp2([1.7, 5.3], rol[0], kScr);
  // defensa (Baskonia)
  let d1 = lerp2([0, 8.5], [.2, 7.9], E(S(u, .9, 1.5))); d1 = lerp2(d1, [1.9, 7.3], E(S(u, 1.6, 2.5)));
  let d5 = lerp2([1.4, 4.3], [2.8, 5.9], E(S(u, .9, 1.8))); d5 = lerp2(d5, [1.7, 4.3], E(S(u, 2.55, 3.2)));
  const d4 = lerp2([-5.7, 1.8], [-3.7, 2.5], E(S(u, 1.9, 2.7)));
  [[-5.3, 5.9], [5.6, 4.6], d4, d1, d5].forEach(p => chip(ctx, M(...p), 'b', '', a));
  // ataque (Partizan)
  [[-6.3, 6.7], [6.5, 5.0], [-6.8, 1.1]].forEach(p => chip(ctx, M(...p), 'a', '', a));
  chip(ctx, M(...a1), 'a', '', a);
  chip(ctx, M(...a5), 'a', '5', a, 1 + .16 * Math.sin(S(u, 2.5, 3.0) * Math.PI));
  // pase
  if (kPass > 0) stroke(ctx, [mm(a1, -.5, -.3), mm(a5, .5, .4)], 1, { color: '#ff8a1f', lw: 5, a: a * (1 - S(u, 2.5, 2.9)) * .9 });
  let bp = mm(a1, .6, .35);
  if (kPass > 0) bp = lerp2(bp, mm(a5, .5, .35), E(kPass));
  if (kShot > 0) bp = lerp2(mm(a5, .5, .35), M(0, 1.575), O(kShot));
  ball(ctx, bp, a * (1 - S(u, 2.9, 3.2)));
}

// ---------- Recreación 2: el Baskonia mueve el balón por fuera, tira y falla ----------
const BK = [[0, 9.5], [-6.2, 6.4], [6.2, 6.4], [-6.8, 1.2], [2.4, 5.7]];
function stuck(ctx, v, a) {
  if (a <= 0) return;
  const k1 = S(v, .4, .8), k2 = S(v, 1.3, 1.7), k3 = S(v, 2.1, 2.5), kShot = S(v, 2.9, 3.3), kReb = S(v, 3.3, 3.75);
  // de qué lado está el balón (-1 izquierda, 1 derecha): la defensa bascula
  let side = E(k1) - E(k2) - E(k3);
  const att = BK.map((p, i) => [p[0] + .1 * Math.sin(v * 1.7 + i * 2), p[1] + .08 * Math.cos(v * 1.3 + i)]);
  const def = BK.map((p, i) => [p[0] * .74 + side * .5, 1.575 + (p[1] - 1.575) * .76]);
  def[4] = lerp2(def[4], [1.9, 3.2], E(S(v, 3.1, 3.7)));
  // pases (línea naranja que se apaga)
  const passes = [[0, 2, .4, .8], [2, 0, 1.3, 1.7], [0, 1, 2.1, 2.5]];
  passes.forEach(([i, j, t0, t1]) => { const k = S(v, t0, t1); if (k > 0) stroke(ctx, [mm(att[i]), mm(att[j])], k, { color: '#ff8a1f', lw: 5, a: a * (1 - S(v, t1, t1 + .5)) * .9 }); });
  def.forEach(p => chip(ctx, M(...p), 'a', '', a));
  att.forEach((p, i) => chip(ctx, M(...p), 'b', '', a, i === 1 ? 1 + .14 * Math.sin(S(v, 2.8, 3.2) * Math.PI) : 1));
  let bp = mm(att[0], .55, -.45);
  if (k1 > 0) bp = lerp2(mm(att[0], .55, -.45), mm(att[2], -.55, -.45), E(k1));
  if (k2 > 0) bp = lerp2(mm(att[2], -.55, -.45), mm(att[0], -.55, -.45), E(k2));
  if (k3 > 0) bp = lerp2(mm(att[0], -.55, -.45), mm(att[1], .55, -.45), E(k3));
  if (kShot > 0) { const q = quad(mm(att[1], .55, -.45), M(-3.6, 1.0), M(.25, 1.5), kShot); bp = q; }
  if (kReb > 0) bp = lerp2(M(.25, 1.5), mm(def[4], -.5, -.4), O(kReb));
  if (kShot > 0) stroke(ctx, curve(mm(att[1], .55, -.45), M(-3.6, 1.0), M(.25, 1.5)), kShot, { color: BLUE, lw: 6, dash: [2, 16], a: a * (1 - S(v, 3.3, 3.9)) });
  ball(ctx, bp, a);
  cross(ctx, M(0, 1.575), S(v, 3.3, 3.6), a * (1 - S(v, 4.1, 4.4)));
}

// Marcador del último cuarto (abajo a la izquierda)
function board4(ctx, a, nP, nB, popP, popB) {
  if (a <= 0) return;
  const x = 70, y = 1262, w = 540, h = 226;
  ctx.save(); ctx.globalAlpha = a; ctx.shadowColor = 'rgba(13,15,20,.12)'; ctx.shadowBlur = 24; ctx.shadowOffsetY = 8;
  T.rr(ctx, x, y, w, h, 30); ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.lineWidth = 4; ctx.strokeStyle = '#d7e0f5'; ctx.stroke(); ctx.restore();
  mono(ctx, '4.º cuarto', x + w / 2, y + 40, 40, BLUE, a);
  T.text(ctx, [[String(nP)]], x + w * .26, y + 146, 96 * (1 + .12 * popP), { a });
  T.text(ctx, [[String(nB), true]], x + w * .74, y + 146, 96 * (1 + .12 * popB), { a });
  mono(ctx, 'Partizan', x + w * .26, y + 190, 40, INK, a); mono(ctx, 'Baskonia', x + w * .74, y + 190, 40, BLUE, a);
}

// ---------- Gráfico: puntos por cuarto (ficha del partido) ----------
const QP = [23, 19, 23, 15], QB = [18, 20, 22, 6], ACC = ['0–0', '23–18', '42–38', '65–60', '80–66'];
const QT = [4.4, 5.15, 5.9, 8.0];
function chart(ctx, t, a) {
  if (a <= 0) return;
  const base = 1130, u = 19, gx = i => 175 + i * 190;
  stroke(ctx, [[70, base], [880, base]], S(t, 4.0, 4.6), { color: '#b9c3d8', lw: 5, a });
  const la = a * O(S(t, 4.1, 4.6));
  ctx.save(); ctx.globalAlpha = la; T.rr(ctx, 93, 545, 34, 34, 8); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = INK; ctx.stroke();
  T.rr(ctx, 348, 542, 40, 40, 8); ctx.fillStyle = BLUE; ctx.fill(); ctx.restore();
  label(ctx, 'Partizan', 142, 564, 40, INK, la); label(ctx, 'Baskonia', 402, 564, 40, INK, la);
  // resalte del último cuarto
  const hk = O(S(t, 7.4, 7.9)), pulse = 1 + .012 * Math.sin(t * 6);
  if (hk > 0) { ctx.save(); ctx.globalAlpha = a * hk; ctx.translate(gx(3), 900); ctx.scale(pulse, 1);
    T.rr(ctx, -92, -290, 184, 520, 26); ctx.fillStyle = 'rgba(47,107,255,.10)'; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = BLUE; ctx.setLineDash([12, 12]); ctx.stroke(); ctx.restore(); }
  for (let i = 0; i < 4; i++) {
    const k = O(S(t, QT[i], QT[i] + .65)); if (k <= 0) continue;
    const hp = QP[i] * u * k, hb = QB[i] * u * k * (i === 3 ? 1 + .04 * Math.sin(t * 9) * S(t, 8.8, 9.2) : 1);
    ctx.save(); ctx.globalAlpha = a;
    T.rr(ctx, gx(i) - 68, base - hp, 58, hp, [10, 10, 0, 0]); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = INK; ctx.stroke();
    T.rr(ctx, gx(i) + 6, base - hb, 64, hb, [10, 10, 0, 0]); ctx.fillStyle = i === 3 && t > 8.8 ? RED : BLUE; ctx.fill();
    ctx.restore();
    label(ctx, String(Math.round(QP[i] * k)), gx(i) - 39, base - hp - 32, 44, INK, a * k, 'center');
    label(ctx, String(Math.round(QB[i] * k)), gx(i) + 38, base - hb - 32, 44, i === 3 && t > 8.8 ? RED : BLUE, a * k, 'center');
    mono(ctx, `${i + 1}.º`, gx(i), base + 46, 40, i === 3 && hk > 0 ? BLUE : MUTE, a * k);
  }
  const bk = T.back(S(t, 8.6, 9.0));
  if (bk > 0) T.text(ctx, [['15–6', true]], gx(3), 594, 96 * bk, { a: a * Math.min(1, bk) });
  // marcador acumulado
  let n = 0; QT.forEach((q, i) => { if (t >= q + .5) n = i + 1; });
  const pop = Math.max(...QT.map(q => Math.sin(S(t, q + .5, q + .85) * Math.PI)));
  const sa = a * O(S(t, 4.3, 4.8));
  mono(ctx, 'Marcador', 350, 1232, 40, MUTE, sa);
  T.text(ctx, [[ACC[n]]], 350, 1378, 124 * (1 + .08 * pop), { a: sa });
  mono(ctx, 'Partizan – Baskonia', 350, 1436, 40, INK, sa);
}

// ---------- ProTeam (datos de ejemplo) ----------
function panel(ctx, a) {
  if (a <= 0) return;
  const x = 70, y = 530, w = 840, h = 660;
  ctx.save(); ctx.globalAlpha = a; ctx.shadowColor = 'rgba(13,15,20,.14)'; ctx.shadowBlur = 30; ctx.shadowOffsetY = 10;
  T.rr(ctx, x, y, w, h, 36); ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.lineWidth = 4; ctx.strokeStyle = '#d7e0f5'; ctx.stroke();
  T.rr(ctx, x + 2, y + 2, w - 4, 92, [34, 34, 0, 0]); ctx.fillStyle = SOFT; ctx.fill(); ctx.restore();
  T.logo(ctx, window.LOGO, x + 62, y + 48, 58, a);
  label(ctx, 'ProTeam', x + 104, y + 50, 42, INK, a);
  mono(ctx, 'datos de ejemplo', x + w - 34, y + 50, 40, BLUE, a, 'right');
}
const MY = [18, 16, 19, 7], RV = [15, 17, 16, 18];
function quarters(ctx, t, a, t0) {
  if (a <= 0) return;
  panel(ctx, a);
  label(ctx, 'Puntos por cuarto', 110, 678, 50, INK, a);
  ctx.save(); ctx.globalAlpha = a; T.rr(ctx, 112, 728, 38, 38, 8); ctx.fillStyle = BLUE; ctx.fill();
  T.rr(ctx, 400, 731, 32, 32, 8); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = INK; ctx.stroke(); ctx.restore();
  label(ctx, 'Tu equipo', 164, 748, 40, INK, a, 'left', 700); label(ctx, 'Rival', 446, 748, 40, INK, a, 'left', 700);
  const base = 1112, u = 14, gx = i => 200 + i * 185;
  stroke(ctx, [[104, base], [876, base]], 1, { color: '#b9c3d8', lw: 4, a });
  const hk = O(S(t, t0 + 1.9, t0 + 2.3));
  if (hk > 0) { ctx.save(); ctx.globalAlpha = a * hk; T.rr(ctx, gx(3) - 84, 800, 168, 378, 22); ctx.fillStyle = 'rgba(239,68,68,.10)'; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = RED; ctx.setLineDash([12, 12]); ctx.stroke(); ctx.restore(); }
  for (let i = 0; i < 4; i++) {
    const k = O(S(t, t0 + .4 + i * .35, t0 + .95 + i * .35)); if (k <= 0) continue;
    const hm = MY[i] * u * k, hr = RV[i] * u * k, bad = i === 3 && hk > 0;
    ctx.save(); ctx.globalAlpha = a;
    T.rr(ctx, gx(i) - 66, base - hm, 60, hm, [10, 10, 0, 0]); ctx.fillStyle = bad ? RED : BLUE; ctx.fill();
    T.rr(ctx, gx(i) + 8, base - hr, 54, hr, [10, 10, 0, 0]); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = INK; ctx.stroke(); ctx.restore();
    label(ctx, String(Math.round(MY[i] * k)), gx(i) - 36, base - hm - 28, 40, bad ? RED : BLUE, a * k, 'center');
    label(ctx, String(Math.round(RV[i] * k)), gx(i) + 35, base - hr - 28, 40, INK, a * k, 'center');
    mono(ctx, `${i + 1}.º`, gx(i), base + 42, 40, bad ? RED : MUTE, a * k);
  }
  const pk = T.back(S(t, t0 + 2.2, t0 + 2.6));
  if (pk > 0) { ctx.save(); ctx.globalAlpha = a * Math.min(1, pk); ctx.translate(gx(3), 748); ctx.scale(pk, pk); T.rr(ctx, -74, -32, 148, 64, 32); ctx.fillStyle = RED; ctx.fill(); ctx.restore();
    label(ctx, '−11', gx(3), 750, 44, '#fff', a * Math.min(1, pk), 'center'); }
  // cursor de registro en directo
  const ph = S(t, t0 + .3, t0 + 1.9);
  if (ph > 0 && ph < 1) { const x = T.lerp(120, 860, ph), al = a * Math.min(1, ph * 8, (1 - ph) * 8); stroke(ctx, [[x, 800], [x, base]], 1, { color: RED, lw: 4, a: al }); }
}
const ROWS = [['Base', 36, 9], ['Escolta', 24, 6], ['Alero', 31, 8], ['Ala-pívot', 18, 5], ['Pívot', 34, 9]];
function load(ctx, t, a, t0) {
  if (a <= 0) return;
  panel(ctx, a);
  label(ctx, 'Control de carga', 110, 678, 50, INK, a);
  mono(ctx, 'Minutos', 510, 756, 40, MUTE, a); mono(ctx, 'RPE', 830, 756, 40, MUTE, a);
  ROWS.forEach(([name, min, rpe], i) => {
    const k = O(S(t, t0 + .35 + i * .28, t0 + .9 + i * .28)); if (k <= 0) return;
    const y = 836 + i * 72, hot = rpe >= 9, hk = hot ? O(S(t, t0 + 2.3, t0 + 2.7)) : 0;
    if (hk > 0) { ctx.save(); ctx.globalAlpha = a * hk * (.75 + .25 * Math.sin(t * 7) ** 2); T.rr(ctx, 90, y - 34, 800, 68, 18); ctx.fillStyle = 'rgba(239,68,68,.12)'; ctx.fill(); ctx.restore(); }
    label(ctx, name, 110, y + 2, 40, INK, a * k, 'left', 700);
    ctx.save(); ctx.globalAlpha = a * k; T.rr(ctx, 340, y - 15, 340, 30, 15); ctx.fillStyle = SOFT; ctx.fill();
    T.rr(ctx, 340, y - 15, 340 * (min / 40) * k, 30, 15); ctx.fillStyle = hk > 0 ? RED : BLUE; ctx.fill();
    const col = rpe >= 9 ? RED : rpe >= 8 ? '#f59e0b' : BLUE, ps = 1 + .12 * hk * Math.sin(t * 7) ** 2;
    ctx.translate(830, y); ctx.scale(ps, ps); T.rr(ctx, -42, -28, 84, 56, 28); ctx.fillStyle = col; ctx.fill(); ctx.restore();
    label(ctx, `${Math.round(min * k)}'`, 694, y + 2, 40, INK, a * k);
    label(ctx, String(rpe), 830, y + 3, 40, '#fff', a * k, 'center');
  });
}

// ---------- Ejercicio: «El último cuarto» (pista entera en horizontal) ----------
const X0 = 80, YC = 790, KE = 30;
const ML = (x, d) => [X0 + d * KE, YC + x * KE], MR = (x, d) => [X0 + (28 - d) * KE, YC - x * KE];
const LANES = [-5.6, -3.6, 3.6, 5.6], SPOTS = [[-6.2, 4.6], [-3.2, 8.6], [3.2, 8.6], [6.2, 4.6]];
function drill(ctx, t, a, t0) {
  if (a <= 0) return;
  K = KE; R = 20;
  const cp = S(t, t0, t0 + .8);
  M = ML; court(ctx, cp, a, 14, true); M = MR; court(ctx, cp, a, 14, true); M = ML;
  const tr = t0 + 2.8, leg = .5;                      // carreras: 4 tramos (2 idas y vueltas)
  const ph = T.clamp((t - tr) / leg, 0, 4), n = Math.min(3, Math.floor(ph)), f = E(ph - n), run = ph > 0 && ph < 4;
  const dRun = ph >= 4 ? .8 : (n % 2 === 0 ? T.lerp(.8, 27.2, f) : T.lerp(27.2, .8, f));
  const kSet = E(S(t, tr + 2.0, tr + 2.6)), ca = a * O(S(t, t0 + .5, t0 + .9));
  // estelas
  if (run) LANES.forEach(x => { const p = ML(x, dRun), dir = n % 2 === 0 ? -1 : 1; stroke(ctx, [[p[0] + dir * 120, p[1]], [p[0] + dir * 26, p[1]]], 1, { color: BLUE, lw: 6, a: ca * .35 * Math.sin((ph - n) * Math.PI), dash: [2, 14] }); });
  // defensa esperando en la zona izquierda
  const DEF0 = [[-1.6, 2.2], [-1.6, 4.6], [1.6, 4.6], [1.6, 2.2]];
  DEF0.forEach((p, i) => { const q = lerp2(p, [SPOTS[i][0] * .72, 1.575 + (SPOTS[i][1] - 1.575) * .72], kSet); chip(ctx, ML(...q), 'a', '', ca); });
  const pos = LANES.map((x, i) => lerp2([x, dRun], SPOTS[i], kSet));
  const bob = run ? 0 : Math.sin(t * 9) * 3 * (1 - kSet) * (t < tr ? 1 : 0);
  pos.forEach((p, i) => { const q = ML(...p); chip(ctx, [q[0], q[1] + bob * (i % 2 ? 1 : -1)], 'b', '', ca, run ? 1.08 : 1); });
  // 4 contra 4: dos pases y tiro
  const tb = tr + 2.6, k1 = S(t, tb + .1, tb + .4), k2 = S(t, tb + .6, tb + .9), ks = S(t, tb + 1.1, tb + 1.4);
  if (t > tb - .1) {
    let bp = ML(pos[1][0] + .6, pos[1][1] - .5);
    if (k1 > 0) bp = lerp2(bp, ML(pos[2][0] - .6, pos[2][1] - .5), E(k1));
    if (k2 > 0) bp = lerp2(ML(pos[2][0] - .6, pos[2][1] - .5), ML(pos[3][0] - .6, pos[3][1] + .5), E(k2));
    if (ks > 0) bp = quad(ML(pos[3][0] - .6, pos[3][1] + .5), ML(5.6, 1.2), ML(0, 1.575), O(ks));
    ball(ctx, bp, ca * O(S(t, tb - .1, tb + .1)) * (1 - S(t, tb + 1.4, tb + 1.7)));
    ring(ctx, ML(0, 1.575), t, tb + 1.4, BLUE, 110);
  }
  // tarjeta: vueltas -> posesiones
  const x = 70, y = 1262, w = 540, h = 226, laps = Math.min(2, Math.floor(ph / 2)), posMode = S(t, tr + 2.0, tr + 2.3);
  ctx.save(); ctx.globalAlpha = a; ctx.shadowColor = 'rgba(13,15,20,.12)'; ctx.shadowBlur = 24; ctx.shadowOffsetY = 8;
  T.rr(ctx, x, y, w, h, 30); ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.lineWidth = 4; ctx.strokeStyle = '#d7e0f5'; ctx.stroke(); ctx.restore();
  mono(ctx, 'Idas y vueltas', x + w / 2, y + 44, 40, BLUE, a * (1 - posMode));
  const lp = Math.max(Math.sin(S(t, tr + 1.0, tr + 1.35) * Math.PI), Math.sin(S(t, tr + 2.0, tr + 2.35) * Math.PI));
  T.text(ctx, [[String(laps), true], [' / 2']], x + w / 2, y + 168, 104 * (1 + .1 * lp), { a: a * (1 - posMode) });
  mono(ctx, 'Posesiones', x + w / 2, y + 44, 40, BLUE, a * posMode);
  for (let i = 0; i < 3; i++) { const cx = x + w / 2 + (i - 1) * 130, cy = y + 134, on = i === 0 ? T.back(S(t, tb + 1.4, tb + 1.7)) : 0;
    ctx.save(); ctx.globalAlpha = a * posMode; ctx.beginPath(); ctx.arc(cx, cy, 38, 0, 7); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 7; ctx.strokeStyle = on > 0 ? BLUE : '#b9c3d8'; ctx.stroke();
    if (on > 0) { ctx.beginPath(); ctx.arc(cx, cy, 38 * Math.min(1.1, on), 0, 7); ctx.fillStyle = BLUE; ctx.fill(); }
    ctx.restore(); label(ctx, String(i + 1), cx, cy + 3, 40, on > .5 ? '#fff' : MUTE, a * posMode, 'center'); }
}

function trazoAt(ctx, pose, x, y, s, o = {}) {
  if (o.flip) { ctx.save(); ctx.translate(x, 0); ctx.scale(-1, 1); T.trazo(ctx, pose, 0, y, s, o); ctx.restore(); }
  else T.trazo(ctx, pose, x, y, s, o);
}

// Tiempos de los tramos
const tB = 4.0, tC = 10.4, tC2 = 14.6, tD = 19.4, tD2 = 23.2, tE = 27.6, tF = 34.9;
window.SCENE = { w: W, h: H, dur: 38.1, fps: 30, draw(ctx, t, args = {}) {
  T.board(ctx, W, H);
  const P_ = T.POSES;

  // ---------- 0–4 s · gancho ----------
  const hookA = 1 - S(t, tB - .3, tB + .1);
  if (hookA > 0) {
    mono(ctx, 'Euroliga · Partizan 80–66 Baskonia', CX, 330, 40, MUTE, hookA);
    const k1 = T.back(S(t, 0, .35)), k2 = T.back(S(t, .25, .6)), k3 = O(S(t, 2.0, 2.5));
    T.text(ctx, [['6', true], [' puntos']], CX, 610 + (1 - k1) * 30, 170, { a: hookA * Math.min(1, k1 * 1.2) });
    T.text(ctx, [['en el '], ['último cuarto.', true]], CX, 790 + (1 - k2) * 30, 88, { a: hookA * Math.min(1, k2 * 1.2) });
    T.text(ctx, [['Así cayó '], ['el Baskonia.', true]], CX, 950 + (1 - k3) * 20, 80, { a: hookA * k3 });
  }

  // ---------- Trazo (hilo conductor) ----------
  const toB = E(S(t, tB - .4, tB + .6)), fin = E(S(t, tF, tF + 1.0));
  let hx = T.lerp(CX, 812, toB), hy = T.lerp(1310, 1362, toB), s = T.lerp(300, 240, toB);
  const RAISE = { ...P_.raise, elbowR: [.3, -.46], handR: [.37, -.76] };
  let pose = T.mix(P_.stand, RAISE, E(S(t, .5, .9)) * (1 - E(S(t, 3.0, 3.5))));
  const pt = Math.max(fadeIO(t, 4.5, 7.2, .4), fadeIO(t, 7.8, 9.2, .4), fadeIO(t, 10.9, 14.2, .4), fadeIO(t, 15.0, 17.6, .4), fadeIO(t, 19.8, 22.8, .4), fadeIO(t, 23.5, 27.3, .4), fadeIO(t, 28.0, 34.2, .4));
  pose = T.mix(pose, P_.point, E(pt));
  const sl = Math.max(fadeIO(t, 9.2, 10.4, .35), fadeIO(t, 17.9, 19.3, .35));
  pose = T.mix(pose, P_.slump, E(sl));
  const flip = t > tB - .1;
  if (t > tF) { pose = T.mix(pose, P_.line, fin); hx = T.lerp(812, CX - 10, fin); hy = T.lerp(1362, 950, fin); s = T.lerp(240, 170, fin); }
  const nod = Math.sin(t * 2.2) * 4 * (t < tF - .2 ? 1 : 0);
  const blink = [1.9, 5.6, 8.4, 12.7, 16.4, 21.8, 25.2, 29.4, 32.6].some(b => t > b && t < b + .12);
  trazoAt(ctx, pose, hx, hy + nod, s, { flip, blink, look: t < tB ? 0 : .7, eyes: fin < .3 });

  // ---------- 4–10.4 s · el dato: puntos por cuarto ----------
  const chartA = Math.min(O(S(t, tB, tB + .5)), 1 - S(t, tC - .4, tC));
  if (chartA > 0) {
    mono(ctx, 'Puntos por cuarto', CX, 290, 40, BLUE, chartA);
    T.text(ctx, [['Tres cuartos'], ['\n'], ['igualados.', true]], CX, 380, 80, { a: fadeIO(t, tB + .1, 7.5) * chartA });
    T.text(ctx, [['Y en el último,'], ['\n'], ['sin gasolina.', true]], CX, 380, 80, { a: fadeIO(t, 7.5, tC) * chartA });
    chart(ctx, t, chartA);
  }

  // ---------- 10.4–19.4 s · pizarra: por qué ----------
  const boardA = Math.min(O(S(t, tC, tC + .5)), 1 - S(t, tD - .4, tD));
  if (boardA > 0) {
    half(500, 500, 54);
    court(ctx, S(t, tC, tC + 1.0), boardA);
    mono(ctx, 'Recreación', CX, 290, 40, BLUE, boardA);
    T.text(ctx, [['Partizan castiga'], ['\n'], ['por dentro.', true]], CX, 380, 80, { a: fadeIO(t, tC + .1, tC2) * boardA });
    T.text(ctx, [['Y el Baskonia'], ['\n'], ['se atasca.', true]], CX, 380, 80, { a: fadeIO(t, tC2, tD) * boardA });
    const a1 = Math.min(O(S(t, tC + .4, tC + .8)), 1 - S(t, tC2 - .3, tC2 + .1)) * boardA;
    if (a1 > 0) { pnr(ctx, t - 11.0, a1); ring(ctx, M(0, 1.575), t, 13.9, INK, 130);
      tag(ctx, M(.5, 2.8)[0] + 150, M(.5, 2.8)[1] + 14, 'Jekiri', a1 * fadeIO(t, 13.2, 14.4, .25)); }
    const a2 = Math.min(O(S(t, tC2 - .1, tC2 + .3)), 1) * boardA;
    if (a2 > 0) stuck(ctx, t - 14.9, a2);
    const nP = Math.round(15 * S(t, 11.6, 14.0)), nB = Math.round(6 * S(t, 15.4, 18.4));
    const popP = nP < 15 && nP > 0 ? .5 + .5 * Math.sin(t * 26) : Math.sin(S(t, 14.0, 14.4) * Math.PI);
    const popB = Math.sin(S(t, 18.4, 18.9) * Math.PI);
    board4(ctx, boardA * O(S(t, tC + .5, tC + 1.0)), nP, nB, popP * .6, popB);
  }

  // ---------- 19.4–27.6 s · en tu equipo: ProTeam ----------
  const d1 = Math.min(O(S(t, tD, tD + .4)), 1 - S(t, tD2 - .3, tD2));
  if (d1 > 0) {
    mono(ctx, 'En tu equipo', CX, 290, 40, BLUE, d1);
    T.text(ctx, [['ProTeam te enseña'], ['\n'], ['los puntos por cuarto.', true]], CX, 380, 78, { a: d1 });
    quarters(ctx, t, d1, tD);
    const k = O(S(t, tD + 2.3, tD + 2.8));
    T.text(ctx, [['El cuarto'], ['\n'], ['que se te cae.', true]], 84, 1320 + (1 - k) * 16, 66, { a: d1 * k, align: 'left' });
  }
  const d2 = Math.min(O(S(t, tD2, tD2 + .4)), 1 - S(t, tE - .3, tE));
  if (d2 > 0) {
    mono(ctx, 'En tu equipo', CX, 290, 40, BLUE, d2);
    T.text(ctx, [['Control de carga:'], ['\n'], ['minutos y RPE.', true]], CX, 380, 78, { a: d2 });
    load(ctx, t, d2, tD2);
    const k = O(S(t, tD2 + 2.5, tD2 + 3.0));
    T.text(ctx, [['Quién llega'], ['\n'], ['fundido al final.', true]], 84, 1320 + (1 - k) * 16, 66, { a: d2 * k, align: 'left' });
  }

  // ---------- 27.6–34.9 s · el ejercicio del martes ----------
  const exA = Math.min(O(S(t, tE, tE + .5)), 1 - S(t, tF - .3, tF));
  if (exA > 0) {
    mono(ctx, 'Para el martes', CX, 290, 40, BLUE, exA);
    T.text(ctx, [['El último '], ['cuarto.', true]], CX, 420, 96, { a: exA });
    drill(ctx, t, exA, tE);
    const tr = tE + 2.8;
    const rules = [[tE + .4, tr, [['Se entrena a '], ['decidir cansado.', true]]], [tr, tr + 2.0, [['2 idas y vueltas '], ['a tope.', true]]], [tr + 2.0, tF, [['Y sin parar: '], ['4 contra 4.', true]]]];
    for (const [a, b, segs] of rules) { const k = fadeIO(t, a, b, .25); if (k > 0) T.text(ctx, segs, CX, 1150 + (1 - k) * 14, 58, { a: k * exA }); }
  }

  // ---------- 34.9–38.1 s · cierre ----------
  if (t > tF) {
    const lk = T.back(S(t, tF + .5, tF + 1.2));
    T.logo(ctx, window.LOGO, CX, 690, 260 * lk, S(t, tF + .5, tF + .9));
    const wk = O(S(t, tF + 1.0, tF + 1.6));
    T.text(ctx, [['ProTeam']], CX, 960 + (1 - wk) * 30, 120, { a: wk });
    const ck = O(S(t, tF + 1.5, tF + 2.1));
    T.text(ctx, [['Guárdalo para '], ['el martes.', true]], CX, 1130 + (1 - ck) * 20, 64, { a: ck });
    mono(ctx, '@app.proteam', CX, 1250, 40, MUTE, O(S(t, tF + 2.0, tF + 2.5)));
  }
} };
})();
