
const T = window.TIMES; window.DUR = T.END;
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const E = { out: p => 1 - Math.pow(1 - p, 3), out5: p => 1 - Math.pow(1 - p, 5), io: p => p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2 };
const $ = id => document.getElementById(id);
const show = (el, v) => { el.style.display = v ? (el._d || 'block') : 'none'; };
const IMG = n => `/tools/reel31/img/${n}.jpg`;
const mk = (tag, css, html, parent) => { const d = document.createElement(tag); if (css) d.style.cssText = css; if (html != null) d.innerHTML = html; (parent || $('txt')).appendChild(d); return d; };
function ph(src, pos = '50% 30%') {
  const d = document.createElement('div'); d.className = 'ph';
  const i = document.createElement('img'); i.src = IMG(src); i.style.objectPosition = pos; d.appendChild(i);
  const s = document.createElement('div'); s.className = 'sh'; d.appendChild(s); d._img = i; d._sh = s;
  $('phs').appendChild(d); return d;
}
function place(el, o = {}) {
  el.style.left = '0px'; el.style.top = '0px'; el.style.width = '1080px'; el.style.height = '1920px';
  el.style.opacity = o.op == null ? 1 : o.op; el.style.zIndex = o.z || 1;
  el._img.style.transformOrigin = o.org || '50% 50%';
  el._img.style.transform = `scale(${o.is || 1.06}) translate(${o.ix || 0}px,${o.iy || 0}px)`;
  el._sh.style.background = o.grad || `rgba(0,0,0,${o.dark || 0})`;
}
function tx(html, y, cls, size) { const d = document.createElement('div'); d.className = 'tx ' + cls; d.style.top = y + 'px'; d.style.fontSize = size + 'px'; d.innerHTML = html; $('txt').appendChild(d); return d; }
function reveal(el, p) { el.querySelectorAll('.mask>span').forEach((s, i, a) => { const q = E.out5(clamp(p * (1 + .25 * (a.length - 1)) - .25 * i)); s.style.transform = `translateY(${(1 - q) * 110}%)`; }); }
const M = s => `<span class="mask"><span>${s}</span></span>`;

