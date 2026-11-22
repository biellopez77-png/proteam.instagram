// ── 5 · CIERRE (v3, 17/11, encargo de Andrés): la entrada en la lista de espera con el contador (misma animación de u28 v3, u30 y u09) ──
// el contador sale de lo que falta de verdad cuando se publica (jue 19/11 11:30 → vie 27/11 23:59:59 = 8 d 12 h 29 min 59 s)
let rs = 11; const rnd = () => (rs = (rs * 16807) % 2147483647) / 2147483647;
const W = { web: T.camp - .05 }; W.tap = W.web + 1.15; W.ok = W.tap + .22; W.gal = T.gra - .1;
const PT = Array.from({ length: 22 }, () => { const o = document.createElement('div'); const a = rnd() * Math.PI * 2, r = 160 + rnd() * 260;
  o.style.cssText = `position:absolute;left:0;top:0;width:${10 + rnd() * 10}px;height:${10 + rnd() * 10}px;border-radius:50%;background:${rnd() < .7 ? '#2f6bff' : '#f2f1ec'};display:none;margin-left:${470 + 70}px;margin-top:0px`;
  o._dx = Math.cos(a) * r; o._dy = Math.sin(a) * r * .7; $('web').appendChild(o); return o; });
const GA = ph(window.GAIMG, '50% 30%');
const tHE = tx('<span class="mask"><span>HASTA EL</span></span>', 1130, 'M8 shadow', 70);
const t28 = tx('<span class="mask"><span>27 NOV</span></span>', 1220, 'M8 shadow', 230);
const t3M = tx('<span class="mask"><span class="S blue">3 meses gratis.</span></span>', 800, 'shadow', 180);
function webcta(t) {
  const wv = t >= W.web && t < W.gal; show($('web'), wv);
  if (wv) {
    const p = E.out5(seg(t, W.web, W.web + .4));
    $('wp').style.top = (470 + (1 - p) * 120) + 'px'; $('wp').style.opacity = p;
    [...$('wp').children].forEach((c, i) => { const q = E.out(seg(t, W.web + i * .04, W.web + .28 + i * .04)); c.style.opacity = q; c.style.transform = `translateY(${(1 - q) * 40}px)`; });
    const pg = (t * 1.4) % 1; $('ping').style.transform = `scale(${1 + pg * 1.6})`; $('ping').style.opacity = 1 - pg;
    const total0 = ((4 * 24 + 10) * 60 + 29) * 60 + 59 - Math.floor(t - W.web);
    const acc = E.in(seg(t, W.web + .3, W.gal - .08)); const rem = Math.max(0, Math.round(total0 * (1 - acc)));
    const dd = Math.floor(rem / 86400), hh = Math.floor(rem % 86400 / 3600), mm = Math.floor(rem % 3600 / 60), ss = rem % 60;
    [['cd1', dd], ['cd2', hh], ['cd3', mm], ['cd4', ss]].forEach(([id, v]) => { const el = $(id); const nv = String(v).padStart(2, '0'); if (el.textContent !== nv) { el._ch = t; el.textContent = nv; } el.style.color = rem === 0 ? '#4f86ff' : '#f2f1ec';
      const q = E.out(seg(t, el._ch || -9, (el._ch || -9) + .18)); el.style.transform = `translateY(${(1 - q) * -22}px)`; el.style.opacity = .35 + .65 * q; });
    PT.forEach((o, i) => { const q = seg(t, W.ok + .15, W.ok + .85); o.style.display = q > 0 && q < 1 ? 'block' : 'none'; if (q > 0 && q < 1) { const e = E.out(q); o.style.transform = `translate(${o._dx * e}px,${o._dy * e + 120 * q * q}px) scale(${1 - q})`; o.style.opacity = 1 - q; } });
    const z = seg(t, W.gal - .12, W.gal); $('wp').querySelector('.cd').style.transform = `scale(${1 + .05 * Math.sin(z * Math.PI)})`;
    const fl = $('fld'), bt = $('btn'), wp = $('wp'); const top = parseFloat(wp.style.top);
    const fy = top + fl.offsetTop + 75, by = top + bt.offsetTop + 80;
    const P = [[W.web + .08, 980, 1800], [W.web + .22, 760, fy + 10], [W.web + .5, 740, fy + 14], [W.tap - .12, 560, by + 12], [W.tap - .02, 562, by + 14], [W.gal, 562, by + 14]];
    let x = P[0][1], y = P[0][2];
    for (let i = 0; i < P.length - 1; i++) if (t >= P[i][0]) { const k = E.io(seg(t, P[i][0], P[i + 1][0])); x = P[i][1] + (P[i + 1][1] - P[i][1]) * k; y = P[i][2] + (P[i + 1][2] - P[i][2]) * k; }
    const cu = $('cur'); show(cu, t > W.web + .08 && t < W.ok + .2); cu.style.left = x + 'px'; cu.style.top = y + 'px';
    const click = Math.max(Math.exp(-Math.pow((t - (W.web + .24)) / .06, 2)), Math.exp(-Math.pow((t - W.tap) / .06, 2)));
    cu.style.transform = `scale(${1 - .2 * click})`; cu.style.opacity = 1 - seg(t, W.ok, W.ok + .2);
    const focus = t > W.web + .24;
    fl.style.borderColor = focus ? '#2f6bff' : '#262b36'; fl.style.boxShadow = focus ? `0 0 0 ${(8 + 3 * Math.sin(t * 6)) * E.out(seg(t, W.web + .24, W.web + .37))}px rgba(47,107,255,.22)` : 'none';
    const em = 'entrenador@miclub.es'; const tp = seg(t, W.web + .26, W.web + .5); const ne = Math.floor(em.length * clamp(tp + .06 * Math.sin(tp * 19)));
    $('fldt').innerHTML = ne ? em.slice(0, ne) : (focus ? '' : '<span class="ph2">Tu email</span>');
    $('fc').style.opacity = focus && t < W.tap ? (Math.floor(t * 4) % 2 ? 1 : .15) : 0;
    if (t > W.tap) { fl.style.borderColor = '#262b36'; fl.style.boxShadow = 'none'; }
    const press = Math.exp(-Math.pow((t - W.tap) / .08, 2)); const hov = E.out(seg(t, W.tap - .35, W.tap - .1));
    const doneP = E.out5(seg(t, W.ok, W.ok + .45));
    bt.style.transform = `scale(${1 - .05 * press + .025 * hov * (t < W.tap ? 1 : 0)})`; bt.style.boxShadow = `0 0 ${60 * hov * (t < W.ok ? 1 : 0) + 50 * Math.exp(-Math.pow((t - W.ok - .3) / .25, 2))}px rgba(47,107,255,.6)`;
    bt.style.width = (940 - (940 - 560) * doneP) + 'px'; bt.style.borderRadius = (28 + 52 * doneP) + 'px';
    PT.forEach(o => { o.style.left = '0px'; o.style.top = (top + bt.offsetTop + 70) + 'px'; });
    const rip = $('rip'); const rp = seg(t, W.tap, W.tap + .5); show(rip, rp > 0 && rp < 1);
    rip.style.left = (560 - 70 - 20) + 'px'; rip.style.top = '60px'; rip.style.transform = `scale(${1 + rp * 40})`; rip.style.opacity = .9 * (1 - rp);
    const busy = t >= W.tap + .1 && t < W.ok;
    $('btt').style.display = t < W.tap + .1 ? 'inline' : 'none'; $('spin').style.display = busy ? 'block' : 'none'; $('spin').style.transform = `rotate(${t * 900}deg)`;
    $('ok').style.display = t >= W.ok ? 'flex' : 'none';
    $('okr').setAttribute('stroke-dashoffset', 239 * (1 - E.out(seg(t, W.ok + .05, W.ok + .4))));
    $('okp').setAttribute('stroke-dashoffset', 60 * (1 - E.out(seg(t, W.ok + .25, W.ok + .55))));
    bt.style.background = '#2f6bff';
  }
  const g0 = W.gal, v = t >= g0; show(GA, v); if (v) place(GA, { is: 1.12 - .06 * seg(t, g0, T.END), org: '50% 30%', dark: .66, z: 5 });
  show(tHE, v); show(t28, t >= g0 + .1); show(t3M, v); reveal(tHE, seg(t, g0, g0 + .3)); reveal(t28, seg(t, g0 + .1, g0 + .45));
  reveal(t3M, seg(t, T.gra - .05, T.gra + .3)); t3M.style.transform = `scale(${1 + .05 * seg(t, T.gra, T.END)})`;
  if (v) show($('web'), false);
}

