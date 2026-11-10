// «Trazo analiza» · Atlético 1–2 Barça (LaLiga, 8 nov 2026). Reel 1080x1920, 31 s.
// Dato: 19 tiros del Barça, 4 a puerta (los mismos que el Atlético); los dos goles, de Fermín López (45' y 66'),
// llegando al área desde segunda línea. Fuentes: Sofascore/365Scores y 101 Great Goals / Goal.
// Zona útil: x 0–940, y 250–1500. Centro de composición CX = 500.
(() => {
const W = 1080, H = 1920, CX = 500;
const S = T.seg, E = T.ease, O = T.out;

// Medio campo vertical (portería arriba). Metros -> px.
const PX0 = CX, PY0 = 590, K = 15, XM = 27, YM = 38;
const P = (mx, my) => [PX0 + mx * K, PY0 + my * K];
const lerp2 = (a, b, t) => [T.lerp(a[0], b[0], t), T.lerp(a[1], b[1], t)];
const quad = (a, c, b, t) => lerp2(lerp2(a, c, t), lerp2(c, b, t), t);

function pathLen(pts) { let L = 0; for (let i = 1; i < pts.length; i++) L += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); return L; }
function curve(a, c, b, n = 40) { const o = []; for (let i = 0; i <= n; i++) o.push(quad(a, c, b, i / n)); return o; }
function stroke(ctx, pts, prog, o = {}) {
  if (prog <= 0) return;
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
  if (o.head && prog > .15) { // punta de flecha
    const ang = Math.atan2(end[1] - prev[1], end[0] - prev[0]), hl = (o.lw ?? 8) * 3.2;
    ctx.beginPath(); ctx.moveTo(end[0] - Math.cos(ang - .5) * hl, end[1] - Math.sin(ang - .5) * hl);
    ctx.lineTo(...end); ctx.lineTo(end[0] - Math.cos(ang + .5) * hl, end[1] - Math.sin(ang + .5) * hl); ctx.stroke();
  }
  ctx.restore();
}
function rectPts(x0, y0, x1, y1) { return [[x0, y0], [x0, y1], [x1, y1], [x1, y0]]; }

function pitch(ctx, prog, a = 1) {
  if (prog <= 0 || a <= 0) return;
  const o = { color: '#b9c3d8', lw: 5, a };
  const [l, t] = P(-XM, 0), [r, b] = P(XM, YM);
  stroke(ctx, [[l, t], [r, t]], S(prog, 0, .4), o);                                 // línea de fondo
  stroke(ctx, [[l, t], [l, b]], S(prog, .1, .5), { ...o, dash: [2, 16] });          // recorte de la pizarra
  stroke(ctx, [[r, t], [r, b]], S(prog, .1, .5), { ...o, dash: [2, 16] });
  stroke(ctx, rectPts(...P(-20.15, 0), ...P(20.15, 16.5)), S(prog, .3, .7), o);     // área grande
  stroke(ctx, rectPts(...P(-9.16, 0), ...P(9.16, 5.5)), S(prog, .45, .8), o);        // área pequeña
  const arc = []; for (let i = 0; i <= 30; i++) { const an = Math.PI * (.2 + .6 * i / 30); arc.push([PX0 + Math.cos(an) * 9.15 * K, PY0 + 11 * K + Math.sin(an) * 9.15 * K]); }
  stroke(ctx, arc, S(prog, .6, .9), o);                                               // semicírculo
  // portería
  ctx.save(); ctx.globalAlpha = a * S(prog, .7, 1); ctx.strokeStyle = INK; ctx.lineWidth = 7; ctx.lineCap = 'round';
  const [g0] = P(-3.66, 0), [g1] = P(3.66, 0); ctx.beginPath(); ctx.moveTo(g0, t); ctx.lineTo(g0, t - 26); ctx.lineTo(g1, t - 26); ctx.lineTo(g1, t); ctx.stroke();
  ctx.fillStyle = '#b9c3d8'; const ps = P(0, 11); ctx.beginPath(); ctx.arc(ps[0], ps[1], 6, 0, 7); ctx.fill(); ctx.restore();
}

// Fichas: Barça = azul relleno con iniciales; Atlético = aro de tinta.
function chip(ctx, x, y, kind, label = '', a = 1, sc = 1) {
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a; ctx.translate(x, y); ctx.scale(sc, sc);
  ctx.shadowColor = 'rgba(13,15,20,.18)'; ctx.shadowBlur = 14; ctx.shadowOffsetY = 5;
  ctx.beginPath(); ctx.arc(0, 0, 32, 0, 7);
  if (kind === 'b') { ctx.fillStyle = BLUE; ctx.fill(); ctx.shadowColor = 'transparent'; T.font(ctx, 30, 800); ctx.fillStyle = '#fff'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(label, 0, 2); }
  else { ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent'; ctx.lineWidth = 7; ctx.strokeStyle = INK; ctx.stroke(); }
  ctx.restore();
}
function name(ctx, x, y, s, a) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; T.font(ctx, 40, 800); ctx.fillStyle = INK; ctx.textAlign = 'center'; ctx.textBaseline = 'top'; ctx.lineWidth = 10; ctx.strokeStyle = '#fff'; ctx.lineJoin = 'round'; ctx.strokeText(s, x, y + 40); ctx.fillText(s, x, y + 40); ctx.restore(); }
function ball(ctx, x, y, a = 1) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = INK; ctx.beginPath(); ctx.arc(x, y, 13, 0, 7); ctx.fill(); ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(x - 4, y - 4, 4, 0, 7); ctx.fill(); ctx.restore(); }
function goalFlash(ctx, t, t0) {
  const k = S(t, t0, t0 + .9); if (k <= 0 || k >= 1) return;
  const [x, y] = P(0, 0); ctx.save(); ctx.globalAlpha = 1 - k; ctx.strokeStyle = BLUE; ctx.lineWidth = 10;
  ctx.beginPath(); ctx.arc(x, y - 10, 40 + 160 * O(k), 0, 7); ctx.stroke(); ctx.restore();
}
function mono(ctx, s, x, y, size, color, a = 1, align = 'center') { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; T.mono(ctx, s, x, y, size, color, align); ctx.restore(); }
function fadeIO(t, a, b, f = .3) { return Math.min(O(S(t, a, a + f)), 1 - S(t, b - f, b)); }

// Jugadas (recreación, metros desde la línea de gol; x negativa = izquierda del ataque)
const G1 = { t0: 5.0, t1: 11.2,
  def: [[[-14, 7], [-13, 9.5]], [[-5, 6], [-7, 5.5]], [[5, 6], [0, 6.5]], [[14, 7], [9, 7]], [[-2, 22], [-1, 25]]],
  pedri: [[-12, 32], [-14, 22], [-9, 15]], ferm: [[9, 34], [12, 24], [4, 14]], shot: [3.2, 0] };
const G2 = { t0: 11.2, t1: 16.3,
  def: [[[-13, 7], [-10, 7]], [[-4, 6], [-1, 5.5]], [[5, 6], [8, 7]], [[14, 8], [20, 8]], [[3, 20], [10, 19]]],
  lamine: [[24, 26], [22, 16], [17, 12]], ferm: [[-6, 33], [-8, 20], [2, 9.5]], shot: [-2.5, 0] };

function play(ctx, t, G, A, B, ferm, kA, kB, kF, kPass, kShot, kOut) {
  const a = Math.min(O(S(t, G.t0, G.t0 + .5)), 1 - kOut);
  G.def.forEach(([p0, p1], i) => { const m = E(S(t, G.t0 + .9, G.t0 + 2.6)); const p = P(...lerp2(p0, p1, m)); chip(ctx, ...p, 'a', '', a); });
  const pa = curve(P(...A[0]), P(...A[1]), P(...A[2])), pf = curve(P(...ferm[0]), P(...ferm[1]), P(...ferm[2]));
  stroke(ctx, pa, kA, { color: INK, lw: 7, head: true, a: a * .8 });
  stroke(ctx, pf, kF, { color: BLUE, lw: 9, head: true, dash: [2, 22], a: Math.max(a, 0) });
  const posA = quad(P(...A[0]), P(...A[1]), P(...A[2]), E(kA)), posF = quad(P(...ferm[0]), P(...ferm[1]), P(...ferm[2]), E(kF));
  chip(ctx, ...posA, 'b', B[0], a); name(ctx, ...posA, B[1], a);
  chip(ctx, ...posF, 'b', 'FL', a, 1 + .08 * Math.sin(kF * Math.PI)); name(ctx, ...posF, 'Fermín', a);
  // balón: con A, pase a Fermín, disparo
  let bp = [posA[0] + 26, posA[1] - 26];
  if (kPass > 0) bp = lerp2(bp, [posF[0], posF[1] - 30], E(kPass));
  if (kShot > 0) { const g = P(...G.shot); bp = lerp2([posF[0], posF[1] - 30], [g[0], g[1] - 8], O(kShot)); }
  ball(ctx, ...bp, a);
}

// Ejercicio: 3 contra 2 + el que llega (mini pizarra)
const EX = { x0: 120, y0: 610, w: 760, h: 500 };
function drill(ctx, t, a) {
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a;
  const { x0, y0, w, h } = EX, cx = x0 + w / 2;
  T.rr(ctx, x0, y0, w, h, 36); ctx.fillStyle = '#f5f8ff'; ctx.fill(); ctx.lineWidth = 4; ctx.strokeStyle = '#d7e0f5'; ctx.stroke();
  ctx.strokeStyle = '#b9c3d8'; ctx.lineWidth = 5; ctx.strokeRect(cx - 220, y0 + 40, 440, 170);   // área
  ctx.strokeStyle = INK; ctx.lineWidth = 7; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(cx - 70, y0 + 40); ctx.lineTo(cx - 70, y0 + 16); ctx.lineTo(cx + 70, y0 + 16); ctx.lineTo(cx + 70, y0 + 40); ctx.stroke();
  // línea de salida a 20 m (conos)
  const ly = y0 + 420; ctx.setLineDash([4, 18]); ctx.strokeStyle = '#b9c3d8'; ctx.lineWidth = 5; ctx.beginPath(); ctx.moveTo(x0 + 60, ly); ctx.lineTo(x0 + w - 60, ly); ctx.stroke(); ctx.setLineDash([]);
  for (const cxn of [x0 + 60, x0 + w - 60]) { ctx.fillStyle = '#ff8a1f'; ctx.beginPath(); ctx.moveTo(cxn, ly - 22); ctx.lineTo(cxn - 16, ly + 12); ctx.lineTo(cxn + 16, ly + 12); ctx.closePath(); ctx.fill(); }
  T.mono(ctx, '20 m', x0 + w - 60, ly + 50, 40, MUTE, 'right');
  ctx.restore();
  const k1 = S(t, 21.0, 22.2), k2 = S(t, 23.0, 24.6), k3 = S(t, 24.4, 25.0), k4 = S(t, 25.0, 25.4);
  const att = [[cx - 150, y0 + 250], [cx + 150, y0 + 250]], df = [[cx - 120, y0 + 180], [cx + 120, y0 + 180]];
  // los dos que fijan arrastran a los centrales hacia fuera
  const fx = O(k1) * 50;
  chip(ctx, df[0][0] - fx, df[0][1], 'a', '', a); chip(ctx, df[1][0] + fx, df[1][1], 'a', '', a);
  chip(ctx, att[0][0] - fx, att[0][1] + 10, 'b', '1', a); chip(ctx, att[1][0] + fx, att[1][1] + 10, 'b', '2', a);
  const run = curve([cx + 40, ly], [cx + 70, y0 + 330], [cx, y0 + 150]);
  stroke(ctx, run, k2, { color: BLUE, lw: 9, head: true, dash: [2, 22], a });
  const pr = quad([cx + 40, ly], [cx + 70, y0 + 330], [cx, y0 + 150], E(k2));
  chip(ctx, ...pr, 'b', '3', a, 1 + .1 * Math.sin(k2 * Math.PI));
  let bp = [att[1][0] + fx - 20, att[1][1] - 20];
  if (k3 > 0) bp = lerp2(bp, [pr[0], pr[1] - 30], E(k3));
  if (k4 > 0) bp = lerp2([pr[0], pr[1] - 30], [cx - 30, y0 + 26], O(k4));
  ball(ctx, ...bp, a);
}

const RULES = [
  [21.0, 23.0, [['Dos fijan a '], ['los centrales.', true]]],
  [23.0, 25.0, [['El tercero sale '], ['desde 20 m.', true]]],
  [25.0, 27.4, [['Solo vale el gol '], ['del que llega.', true]]],
];

function trazoAt(ctx, pose, x, y, s, o = {}) {
  if (o.flip) { ctx.save(); ctx.translate(x, 0); ctx.scale(-1, 1); T.trazo(ctx, pose, 0, y, s, o); ctx.restore(); }
  else T.trazo(ctx, pose, x, y, s, o);
}

window.SCENE = { w: W, h: H, dur: 31, fps: 30, draw(ctx, t) {
  T.board(ctx, W, H);
  const P_ = T.POSES;

  // ---------- 0–4 s · gancho ----------
  const hookA = 1 - S(t, 3.6, 4.1);
  if (hookA > 0) {
    mono(ctx, 'LaLiga · Atlético 1–2 Barça', CX, 330, 40, MUTE, hookA);
    const k1 = T.back(S(t, 0, .35)), k2 = T.back(S(t, .25, .6)), k3 = O(S(t, .7, 1.2));
    T.text(ctx, [['19', true], [' tiros.']], CX, 600 + (1 - k1) * 30, 150, { a: hookA * Math.min(1, k1 * 1.2) });
    T.text(ctx, [['4', true], [' a puerta.']], CX, 780 + (1 - k2) * 30, 150, { a: hookA * Math.min(1, k2 * 1.2) });
    T.text(ctx, [['Decidió '], ['el que llegaba.', true]], CX, 960 + (1 - k3) * 20, 84, { a: hookA * k3 });
  }

  // ---------- Trazo (hilo conductor) ----------
  // posiciones: gancho (centro abajo) -> pizarra (abajo izquierda) -> lección (abajo derecha) -> cierre (línea)
  const toBoard = E(S(t, 3.6, 4.8)), toDrill = E(S(t, 19.4, 20.6)), fin = E(S(t, 27.4, 28.4));
  let hx = T.lerp(CX, 210, toBoard), hy = T.lerp(1310, 1350, toBoard), s = T.lerp(300, 270, toBoard);
  hx = T.lerp(hx, 800, toDrill); hy = T.lerp(hy, 1392, toDrill); s = T.lerp(s, 190, toDrill);
  const RAISE = { ...P_.raise, elbowR: [.22, -.56], handR: [.3, -.8] };
  let pose = T.mix(P_.stand, RAISE, E(S(t, .5, .9)) * (1 - E(S(t, 2.8, 3.3))));
  // en la pizarra señala (gol 1, gol 2, patrón)
  const pt = Math.max(fadeIO(t, 8.3, 10.6, .4), fadeIO(t, 13.8, 16.0, .4), fadeIO(t, 17.0, 19.3, .4));
  pose = T.mix(pose, P_.point, E(pt));
  pose = T.mix(pose, P_.point, E(fadeIO(t, 21.0, 27.3, .4)));
  const flip = t > 20.0;
  if (t > 27.4) { pose = T.mix(pose, P_.line, fin); hx = T.lerp(800, CX + 10, fin); hy = T.lerp(1392, 950, fin); s = T.lerp(190, 170, fin); }
  const nod = Math.sin(t * 2.2) * 4 * (t < 27 ? 1 : 0);
  const blink = [1.9, 6.4, 12.7, 18.1, 23.6].some(b => t > b && t < b + .12);
  const look = t < 3.5 ? -.6 : (t < 19.5 ? .7 : -.7);
  trazoAt(ctx, pose, hx, hy + nod, s, { flip, blink, look: flip ? -look : look, eyes: fin < .3 });

  // ---------- 4–19.5 s · pizarra ----------
  const boardA = Math.min(O(S(t, 3.9, 4.4)), 1 - S(t, 19.2, 19.8));
  if (boardA > 0) {
    pitch(ctx, S(t, 4.0, 5.3), boardA);
    // gol 1 · 45'
    if (t > G1.t0 && t < G1.t1) {
      const out = S(t, 10.6, 11.2);
      play(ctx, t, G1, G1.pedri, ['PE', 'Pedri'], G1.ferm, S(t, 5.8, 7.6), 0, S(t, 6.6, 8.6), S(t, 8.6, 9.0), S(t, 9.0, 9.35), out);
      goalFlash(ctx, t, 9.35);
    }
    // gol 2 · 66'
    if (t > G2.t0 && t < G2.t1) {
      const out = S(t, 15.6, 16.2);
      play(ctx, t, G2, G2.lamine, ['LY', 'Lamine'], G2.ferm, S(t, 11.8, 13.4), 0, S(t, 12.2, 14.2), S(t, 14.0, 14.5), S(t, 14.5, 14.85), out);
      goalFlash(ctx, t, 14.85);
    }
    // patrón: las dos llegadas juntas y la zona de llegada
    const pk = S(t, 16.2, 17.2);
    if (pk > 0) {
      const ga = boardA;
      stroke(ctx, curve(P(...G1.ferm[0]), P(...G1.ferm[1]), P(...G1.ferm[2])), pk, { color: BLUE, lw: 9, head: true, dash: [2, 22], a: ga });
      stroke(ctx, curve(P(...G2.ferm[0]), P(...G2.ferm[1]), P(...G2.ferm[2])), pk, { color: BLUE, lw: 9, head: true, dash: [2, 22], a: ga });
      const zk = O(S(t, 17.0, 17.8)), z = P(3, 11);
      ctx.save(); ctx.globalAlpha = ga * .9; ctx.fillStyle = 'rgba(47,107,255,.12)'; ctx.strokeStyle = BLUE; ctx.lineWidth = 6;
      ctx.beginPath(); ctx.ellipse(z[0], z[1], 150 * zk, 85 * zk, 0, 0, 7); ctx.fill(); ctx.stroke(); ctx.restore();
      chip(ctx, ...P(...G1.ferm[0]), 'b', '', ga * .45, .7); chip(ctx, ...P(...G2.ferm[0]), 'b', '', ga * .45, .7);
    }
    // textos de la pizarra
    const c1 = fadeIO(t, 5.0, 11.0), c2 = fadeIO(t, 11.3, 16.2), c3 = fadeIO(t, 16.4, 19.5);
    mono(ctx, 'Gol 1 · minuto 45', CX, 290, 40, BLUE, c1 * boardA);
    T.text(ctx, [['Pedri arrastra.'], ['\n'], ['Fermín llega.', true]], CX, 400, 80, { a: c1 * boardA });
    mono(ctx, 'Gol 2 · minuto 66', CX, 290, 40, BLUE, c2 * boardA);
    T.text(ctx, [['Lamine filtra.'], ['\n'], ['Fermín llega.', true]], CX, 400, 80, { a: c2 * boardA });
    mono(ctx, 'Los dos goles', CX, 290, 40, BLUE, c3 * boardA);
    T.text(ctx, [['Llegar tarde,'], ['\n'], ['pero a tiempo.', true]], CX, 400, 80, { a: c3 * boardA });
    // pie: etiqueta de recreación
    mono(ctx, 'Recreación', 560, 1300, 40, INK, boardA * O(S(t, 4.6, 5.2)), 'left');
    mono(ctx, 'de la jugada', 560, 1355, 40, MUTE, boardA * O(S(t, 4.6, 5.2)), 'left');
  }

  // ---------- 19.8–27.4 s · lección ----------
  const lessA = Math.min(O(S(t, 19.8, 20.4)), 1 - S(t, 27.2, 27.6));
  if (lessA > 0) {
    mono(ctx, 'Para el martes', CX, 290, 40, BLUE, lessA);
    T.text(ctx, [['3 contra 2'], ['\n'], ['+ '], ['el que llega.', true]], CX, 410, 90, { a: lessA });
    drill(ctx, t, lessA * O(S(t, 20.2, 20.8)));
    for (const [a, b, segs] of RULES) { const k = fadeIO(t, a, b, .25); if (k > 0) T.text(ctx, segs, CX, 1200 + (1 - k) * 16, 60, { a: k * lessA }); }
  }

  // ---------- 27.6–31 s · cierre ----------
  if (t > 27.6) {
    const lk = T.back(S(t, 28.2, 28.9));
    T.logo(ctx, window.LOGO, CX, 690, 260 * lk, S(t, 28.2, 28.6));
    const wk = O(S(t, 28.7, 29.3));
    T.text(ctx, [['ProTeam']], CX, 960 + (1 - wk) * 30, 120, { a: wk });
    const ck = O(S(t, 29.3, 29.9));
    T.text(ctx, [['Guárdalo para '], ['el próximo entreno.', true]], CX, 1130 + (1 - ck) * 20, 58, { a: ck });
    mono(ctx, '@app.proteam', CX, 1250, 40, MUTE, O(S(t, 29.8, 30.3)));
  }
} };
})();
