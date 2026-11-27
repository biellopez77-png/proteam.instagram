// Trazo: la línea azul de la pizarra convertida en personaje. Librería de dibujo en canvas, sin IA.
// Uso: se carga en una página (render.py) junto a una escena que define window.SCENE = {w,h,dur,draw(ctx,t)}.
const BLUE = '#2f6bff', INK = '#0d0f14', RED = '#ef4444', SOFT = '#e9efff', MUTE = '#8a8f9c';
const T = {};
T.clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
T.lerp = (a, b, t) => a + (b - a) * t;
T.ease = t => (t = T.clamp(t), t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
T.out = t => (t = T.clamp(t), 1 - Math.pow(1 - t, 3));
T.back = t => { t = T.clamp(t); const c = 1.7; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); };
T.bounce = t => { t = T.clamp(t); const n = 7.5625, d = 2.75;
  if (t < 1 / d) return n * t * t; if (t < 2 / d) return n * (t -= 1.5 / d) * t + .75;
  if (t < 2.5 / d) return n * (t -= 2.25 / d) * t + .9375; return n * (t -= 2.625 / d) * t + .984375; };
T.seg = (t, a, b) => T.clamp((t - a) / (b - a));
T.rnd = (i) => { const x = Math.sin(i * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };

T.board = (ctx, W, H) => {
  ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = 'rgba(217,221,229,.75)';
  for (let y = 30; y < H; y += 60) for (let x = 30; x < W; x += 60) { ctx.beginPath(); ctx.arc(x, y, 2.6, 0, 7); ctx.fill(); }
};

// Poses en unidades de altura (1 = altura de la figura). Origen en la cadera.
T.POSES = {
  line:  { footL: [-.62, .46], kneeL: [-.45, .46], hip: [-.25, .46], kneeR: [-.05, .46], footR: [.12, .46], neck: [.28, .46], elbowL: [.36, .46], handL: [.44, .46], elbowR: [.5, .46], handR: [.58, .46], head: 0 },
  stand: { footL: [-.11, .46], kneeL: [-.07, .23], hip: [0, 0], kneeR: [.07, .23], footR: [.11, .46], neck: [0, -.4], elbowL: [-.13, -.22], handL: [-.17, -.04], elbowR: [.13, -.22], handR: [.17, -.04], head: .12 },
  slump: { footL: [-.16, .46], kneeL: [-.2, .3], hip: [-.02, .2], kneeR: [.14, .3], footR: [.16, .46], neck: [.1, -.12], elbowL: [-.06, .02], handL: [-.08, .2], elbowR: [.2, .04], handR: [.22, .22], head: .11 },
  raise: { footL: [-.13, .46], kneeL: [-.08, .23], hip: [0, 0], kneeR: [.08, .23], footR: [.13, .46], neck: [0, -.41], elbowL: [-.14, -.22], handL: [-.18, -.04], elbowR: [.12, -.6], handR: [.16, -.82], head: .12 },
  point: { footL: [-.11, .46], kneeL: [-.07, .23], hip: [0, 0], kneeR: [.07, .23], footR: [.11, .46], neck: [0, -.4], elbowL: [-.13, -.22], handL: [-.17, -.04], elbowR: [.2, -.36], handR: [.38, -.44], head: .12 },
  sit:   { footL: [-.2, .46], kneeL: [-.24, .22], hip: [0, .22], kneeR: [.18, .22], footR: [.2, .46], neck: [0, -.2], elbowL: [-.12, -.04], handL: [-.2, .14], elbowR: [.12, -.04], handR: [.2, .14], head: .12 },
};
T.mix = (a, b, t) => { const o = {}; for (const k in a) o[k] = typeof a[k] === 'number' ? T.lerp(a[k], b[k], t) : [T.lerp(a[k][0], b[k][0], t), T.lerp(a[k][1], b[k][1], t)]; return o; };

// Dibuja a Trazo con un solo trazo. x,y = cadera; s = altura en px; prog = parte del trazo dibujada (0..1).
T.trazo = (ctx, pose, x, y, s, o = {}) => {
  const prog = o.prog ?? 1, lw = o.lw ?? s * .045, color = o.color ?? BLUE;
  const P = k => [x + pose[k][0] * s, y + pose[k][1] * s];
  const order = ['footL', 'kneeL', 'hip', 'kneeR', 'footR', 'kneeR', 'hip', 'neck', 'elbowL', 'handL', 'elbowL', 'neck', 'elbowR', 'handR', 'elbowR', 'neck'];
  const pts = order.map(P);
  const r = pose.head * s;
  if (r > 1) { const n = P('neck'); const c = [n[0], n[1] - r]; for (let i = 0; i <= 28; i++) { const a = Math.PI / 2 + i / 28 * Math.PI * 2; pts.push([c[0] + Math.cos(a) * r, c[1] + Math.sin(a) * r]); } }
  let L = 0; const d = [0]; for (let i = 1; i < pts.length; i++) { L += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); d.push(L); }
  const lim = L * prog;
  ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  ctx.beginPath(); ctx.moveTo(...pts[0]);
  for (let i = 1; i < pts.length; i++) {
    if (d[i] <= lim) ctx.lineTo(...pts[i]);
    else { const f = (lim - d[i - 1]) / Math.max(1e-6, d[i] - d[i - 1]); ctx.lineTo(T.lerp(pts[i - 1][0], pts[i][0], f), T.lerp(pts[i - 1][1], pts[i][1], f)); break; }
  }
  ctx.stroke();
  if (r > 1 && prog >= .98 && (o.eyes ?? true)) { // ojos: dos puntos secos
    const n = P('neck'), c = [n[0] + (o.look ?? 0) * r * .3, n[1] - r];
    ctx.fillStyle = INK; const er = Math.max(3, lw * .32), blink = o.blink ? .25 : 1;
    for (const sx of [-.32, .32]) { ctx.beginPath(); ctx.ellipse(c[0] + sx * r, c[1] - r * .05, er, er * blink, 0, 0, 7); ctx.fill(); }
  }
  ctx.restore();
};

T.rr = (ctx, x, y, w, h, r) => { ctx.beginPath(); ctx.roundRect(x, y, w, h, r); };
T.font = (ctx, size, weight = 800, fam = 'M') => { ctx.font = `${weight === 'i' ? 'italic 400' : weight} ${size}px ${weight === 'i' ? 'S' : fam}`; };

// Tarjetas del caos. kind: msg, excel, libreta, nota, alerta. Se dibujan centradas en (x,y) con rotación rot.
T.card = (ctx, kind, x, y, rot = 0, sc = 1, a = 1, label = '') => {
  ctx.save(); ctx.globalAlpha = a; ctx.translate(x, y); ctx.rotate(rot); ctx.scale(sc, sc);
  ctx.shadowColor = 'rgba(13,15,20,.16)'; ctx.shadowBlur = 30; ctx.shadowOffsetY = 12;
  if (kind === 'msg') {
    T.rr(ctx, -170, -52, 340, 104, 34); ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent';
    ctx.lineWidth = 4; ctx.strokeStyle = INK; ctx.stroke();
    ctx.fillStyle = '#22c55e'; ctx.beginPath(); ctx.arc(-118, 0, 26, 0, 7); ctx.fill();
    T.font(ctx, 30, 700); ctx.fillStyle = INK; ctx.textBaseline = 'middle'; ctx.fillText(label || '¿Mañana a qué hora?', -80, 0, 236);
  } else if (kind === 'excel') {
    T.rr(ctx, -150, -110, 300, 220, 18); ctx.fillStyle = '#fff'; ctx.fill(); ctx.shadowColor = 'transparent';
    ctx.lineWidth = 4; ctx.strokeStyle = INK; ctx.stroke();
    ctx.fillStyle = '#1d6f42'; T.rr(ctx, -150, -110, 300, 46, [18, 18, 0, 0]); ctx.fill();
    T.font(ctx, 24, 700, 'P'); ctx.fillStyle = '#fff'; ctx.textBaseline = 'middle'; ctx.fillText(label || 'plantilla_v7_FINAL.xlsx', -134, -87, 270);
    ctx.strokeStyle = '#c9ced8'; ctx.lineWidth = 2;
    for (let i = 1; i < 5; i++) { ctx.beginPath(); ctx.moveTo(-150, -64 + i * 34); ctx.lineTo(150, -64 + i * 34); ctx.stroke(); }
    for (let i = 1; i < 4; i++) { ctx.beginPath(); ctx.moveTo(-150 + i * 75, -64); ctx.lineTo(-150 + i * 75, 110); ctx.stroke(); }
    ctx.fillStyle = RED; ctx.fillRect(-70, -26, 66, 26);
  } else if (kind === 'libreta') {
    T.rr(ctx, -130, -160, 260, 320, 14); ctx.fillStyle = '#fbf7ec'; ctx.fill(); ctx.shadowColor = 'transparent';
    ctx.lineWidth = 4; ctx.strokeStyle = INK; ctx.stroke();
    ctx.strokeStyle = '#cfd8f0'; ctx.lineWidth = 2; for (let i = 0; i < 8; i++) { ctx.beginPath(); ctx.moveTo(-110, -110 + i * 34); ctx.lineTo(110, -110 + i * 34); ctx.stroke(); }
    ctx.strokeStyle = '#6b7280'; ctx.lineWidth = 3;
    for (let i = 0; i < 7; i++) { ctx.beginPath(); let px = -100; ctx.moveTo(px, -120 + i * 34); while (px < 90 - (i % 3) * 30) { px += 14; ctx.lineTo(px, -120 + i * 34 + (T.rnd(i * 50 + px) - .5) * 14); } ctx.stroke(); }
    ctx.fillStyle = INK; for (let i = 0; i < 6; i++) { ctx.beginPath(); ctx.arc(-130, -130 + i * 52, 9, 0, 7); ctx.fill(); }
  } else if (kind === 'nota') {
    ctx.fillStyle = '#ffe680'; ctx.fillRect(-100, -100, 200, 200); ctx.shadowColor = 'transparent';
    T.font(ctx, 30, 700); ctx.fillStyle = INK; ctx.textBaseline = 'middle'; ctx.textAlign = 'center';
    (label || 'conos\n¡petos!').split('\n').forEach((l, i, A) => ctx.fillText(l, 0, (i - (A.length - 1) / 2) * 40, 180));
  } else if (kind === 'alerta') {
    ctx.fillStyle = RED; ctx.beginPath(); ctx.arc(0, 0, 58, 0, 7); ctx.fill(); ctx.shadowColor = 'transparent';
    T.font(ctx, label.length > 2 ? 40 : 56, 800); ctx.fillStyle = '#fff'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(label || '!', 0, 3);
  }
  ctx.restore();
};

// Texto con remate en cursiva azul: segmentos [['texto normal'], ['remate', true]]
T.text = (ctx, segs, x, y, size, o = {}) => {
  const lines = [[]]; segs.forEach(s => { if (s[0] === '\n') lines.push([]); else lines[lines.length - 1].push(s); });
  ctx.save(); ctx.globalAlpha = o.a ?? 1; ctx.textBaseline = 'alphabetic';
  lines.forEach((ln, li) => {
    let w = 0; ln.forEach(s => { T.font(ctx, size * (s[1] ? 1.08 : 1), s[1] ? 'i' : 800); w += ctx.measureText(s[0]).width; });
    let cx = o.align === 'left' ? x : x - w / 2; const cy = y + li * size * 1.08 + (o.dy ?? 0);
    ln.forEach(s => { T.font(ctx, size * (s[1] ? 1.08 : 1), s[1] ? 'i' : 800); ctx.fillStyle = s[1] ? BLUE : (o.color ?? INK); ctx.fillText(s[0], cx, cy); cx += ctx.measureText(s[0]).width; });
  });
  ctx.restore();
};
T.mono = (ctx, s, x, y, size, color = MUTE, align = 'center') => { ctx.save(); T.font(ctx, size, 500, 'P'); ctx.fillStyle = color; ctx.textAlign = align; ctx.textBaseline = 'middle'; ctx.fillText(s.toUpperCase(), x, y); ctx.restore(); };
T.logo = (ctx, img, x, y, size, a = 1) => { if (!img || !img.complete) return; ctx.save(); ctx.globalAlpha = a; ctx.drawImage(img, x - size / 2, y - size / 2, size, size); ctx.restore(); };
window.T = T; Object.assign(window, { BLUE, INK, RED, SOFT, MUTE });
