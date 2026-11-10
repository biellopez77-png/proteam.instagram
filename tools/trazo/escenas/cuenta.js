// Cuenta atrás «Algo se está ordenando». Imagen fija: --t = días que faltan (6..1). Feed 1080x1350 o Story 1080x1920.
(() => {
const LINES = {
  6: [['Una línea.'], ['\n'], ['De momento, '], ['solo eso.', true]],
  5: [['Lleva años en '], ['\n'], ['tu pizarra.', true]],
  4: [['Ha visto muchos entrenos'], ['\n'], ['planificados a las '], ['23:47.', true]],
  3: [['Ya tiene piernas.'], ['\n'], ['Y '], ['paciencia.', true]],
  2: [['Se está levantando.'], ['\n'], ['El caos, '], ['no tanto.', true]],
  1: [['Mañana '], ['se presenta.', true]],
};
const STEP = { 6: ['line', .32], 5: ['line', 1], 4: ['stand', .2], 3: ['stand', .42], 2: ['stand', .7], 1: ['stand', .93] };
window.SCENE = { w: 1080, h: 1350, dur: 0, draw(ctx, n, a) {
  n = Math.round(n); const W = a.w, H = a.h, story = H > 1500;
  T.board(ctx, W, H);
  if (story) { // Story 1080x1920: composición centrada en la zona útil (x 0–940, y 250–1580)
    const CX = 500;
    ctx.save(); T.font(ctx, 40, 500, 'P'); const lw = ctx.measureText('ALGO SE ESTÁ ORDENANDO').width; ctx.restore();
    T.logo(ctx, window.LOGO, CX - (lw + 86) / 2 + 30, 320, 64);
    T.mono(ctx, 'Algo se está ordenando', CX - (lw + 86) / 2 + 86, 320, 40, INK, 'left');
    ctx.save(); T.font(ctx, 400, 800); const nw = ctx.measureText(String(n)).width;
    T.font(ctx, 120, 'i'); const dw = ctx.measureText(n === 1 ? 'día' : 'días').width;
    const x0 = CX - (nw + 28 + dw) / 2, ny = 760;
    T.font(ctx, 400, 800); ctx.fillStyle = BLUE; ctx.textBaseline = 'alphabetic'; ctx.fillText(String(n), x0, ny);
    T.font(ctx, 120, 'i'); ctx.fillStyle = INK; ctx.fillText(n === 1 ? 'día' : 'días', x0 + nw + 28, ny); ctx.restore();
    T.text(ctx, LINES[n], CX, 900, 62);
    const [p, prog] = STEP[n]; const sz = 430, hy = 1265;
    T.trazo(ctx, T.POSES[p], CX + (p === 'line' ? .02 * sz : 0), hy, sz, { prog, eyes: false });
    T.mono(ctx, '@app.proteam  ·  ' + (n === 1 ? 'Mañana, 20:30' : `Faltan ${n}`), CX, 1530, 40, MUTE);
    return;
  }
  const top = story ? 230 : 90;
  T.logo(ctx, window.LOGO, 110, top, 64);
  T.mono(ctx, 'Algo se está ordenando', 162, top, 28, INK, 'left');
  // número
  ctx.save(); T.font(ctx, story ? 380 : 330, 800); ctx.fillStyle = BLUE; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
  const ny = story ? 640 : 470; ctx.fillText(String(n), 84, ny);
  const nw = ctx.measureText(String(n)).width; T.font(ctx, story ? 110 : 96, 'i'); ctx.fillStyle = INK;
  ctx.fillText(n === 1 ? 'día' : 'días', 84 + nw + 24, ny); ctx.restore();
  T.text(ctx, LINES[n], 84, story ? 800 : 600, story ? 66 : 66, { align: 'left' });
  // Trazo a medio dibujar
  const [p, prog] = STEP[n]; const s = story ? 560 : 440, hx = W * .56, hy = story ? 1240 : 970;
  T.trazo(ctx, T.POSES[p], hx, hy, s, { prog, eyes: false });
  // pie
  T.mono(ctx, '@app.proteam', 84, H - (story ? 260 : 70), 26, MUTE, 'left');
  T.mono(ctx, n === 1 ? 'Mañana, 20:30' : `Faltan ${n}`, W - 84, H - (story ? 260 : 70), 26, BLUE, 'right');
} };
})();
