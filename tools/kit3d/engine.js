// Motor común de los Reels 3D de ProTeam: una cámara continua que vuela por un mundo de texto, objetos y fotos.
import * as THREE from 'three';
export { THREE };
export const W = 1080, H = 1920;
let seed = 27; export const rnd = () => { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
export const ease = { out: (x) => 1 - Math.pow(1 - x, 3), inOut: (x) => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2, back: (x) => { const c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); }, expo: (x) => x === 1 ? 1 : 1 - Math.pow(2, -10 * x) };
export const clamp = (x) => Math.max(0, Math.min(1, x));
export const seg = (t, a, b) => clamp((t - a) / (b - a));
export const win = (t, a, b, fi = .3, fo = .3) => seg(t, a, a + fi) * (1 - seg(t, b - fo, b));   // ventana de visibilidad
export const F = (s, w = 800) => `${w} ${s}px M`, FS = (s) => `italic ${s}px S`, FP = (s) => `500 ${s}px P`;

export async function setup({ fog = .012, bg = '#05070c', fov = 48 } = {}) {
  await document.fonts.load('800 100px M'); await document.fonts.load('500 40px M'); await document.fonts.load('italic 100px S'); await document.fonts.load('500 30px P');
  const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('gl'), antialias: true, preserveDrawingBuffer: true });
  renderer.setSize(W, H, false); renderer.setPixelRatio(1); renderer.outputEncoding = THREE.sRGBEncoding;
  const scene = new THREE.Scene(); scene.background = new THREE.Color(bg); scene.fog = new THREE.FogExp2(bg, fog);
  const cam = new THREE.PerspectiveCamera(fov, W / H, 0.1, 800);
  scene.add(new THREE.AmbientLight('#ffffff', .7)); const dl = new THREE.DirectionalLight('#9fc0ff', 1.4); dl.position.set(10, 20, 10); scene.add(dl);
  return { renderer, scene, cam };
}
// texto en una textura: lines = [{t, font, y, color, glow}]
export function textTex(lines, w, h, opt = {}) {
  const c = document.createElement('canvas'); c.width = w; c.height = h; const g = c.getContext('2d');
  if (opt.bg) { g.fillStyle = opt.bg; g.beginPath(); g.roundRect(0, 0, w, h, opt.radius || 0); g.fill(); }
  if (opt.blur) g.filter = `blur(${opt.blur}px)`;
  g.textAlign = opt.align || 'center'; g.textBaseline = 'middle';
  const x = opt.align === 'left' ? (opt.pad || 40) : w / 2;
  lines.forEach((l) => { g.font = l.font; g.fillStyle = l.color || '#eef2fa'; g.shadowColor = l.glow || 'rgba(0,0,0,0)'; g.shadowBlur = l.glow ? 44 : 0; g.fillText(l.t, x, l.y); if (l.glow) { g.shadowBlur = 12; g.fillText(l.t, x, l.y); } });
  const t = new THREE.CanvasTexture(c); t.encoding = THREE.sRGBEncoding; t.anisotropy = 8; return t;
}
export function plane(tex, w, h, fog = true) {
  return new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: tex, transparent: true, depthWrite: false, side: THREE.DoubleSide, fog }));
}
// texto listo: ancho en unidades de mundo calculado por proporción del lienzo
export function label(scene, lines, cw, ch, worldW, pos, opt = {}) { const m = plane(textTex(lines, cw, ch, opt), worldW, worldW * ch / cw); m.position.set(...pos); m.material.opacity = 0; scene.add(m); return m; }
export const loadTex = (u) => new Promise((r) => new THREE.TextureLoader().load(u, (t) => { t.encoding = THREE.sRGBEncoding; t.anisotropy = 8; r(t); }));
export async function photo(scene, url, w, pos) { const t = await loadTex(url); const h = w * t.image.height / t.image.width; const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: t, transparent: true, fog: false, depthWrite: false })); m.position.set(...pos); m.material.opacity = 0; scene.add(m); return m; }
export function glowTex(color = '47,107,255') { const c = document.createElement('canvas'); c.width = c.height = 256; const g = c.getContext('2d'); const r = g.createRadialGradient(128, 128, 0, 128, 128, 128); r.addColorStop(0, `rgba(${color},.9)`); r.addColorStop(.4, `rgba(${color},.25)`); r.addColorStop(1, `rgba(${color},0)`); g.fillStyle = r; g.fillRect(0, 0, 256, 256); return new THREE.CanvasTexture(c); }
export function dust(scene, n = 1400, zFrom = 60, zTo = -400, spread = 120) {
  const pos = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) { pos[i * 3] = (rnd() - .5) * spread; pos[i * 3 + 1] = (rnd() - .5) * spread * 1.2; pos[i * 3 + 2] = zFrom - rnd() * (zFrom - zTo); }
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const p = new THREE.Points(g, new THREE.PointsMaterial({ color: '#8fb0ff', size: .16, transparent: true, opacity: .55, depthWrite: false })); scene.add(p); return p;
}
// línea gruesa que se dibuja: tubo con drawRange
export function tube(scene, pts, r, color, opacity = 1, segs = 400) {
  const curve = new THREE.CatmullRomCurve3(pts.map((p) => new THREE.Vector3(...p)));
  const geo = new THREE.TubeGeometry(curve, segs, r, 10, false);
  const m = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color, transparent: opacity < 1, opacity, depthWrite: opacity >= 1, fog: true }));
  m.userData.total = geo.index.count; m.userData.curve = curve; geo.setDrawRange(0, 0); scene.add(m); return m;
}
export const drawTo = (m, k) => { const n = Math.floor(m.userData.total * clamp(k) / 60) * 60; m.geometry.setDrawRange(0, n); };
// Catmull-Rom en tiempo: la cámara nunca se para en un punto clave
export function cr(keys, t) {
  let i = 0; while (i < keys.length - 2 && t > keys[i + 1][0]) i++;
  const k0 = keys[Math.max(0, i - 1)], k1 = keys[i], k2 = keys[i + 1], k3 = keys[Math.min(keys.length - 1, i + 2)];
  const s = clamp((t - k1[0]) / (k2[0] - k1[0])), s2 = s * s, s3 = s2 * s;
  return [1, 2, 3].map((j) => 0.5 * ((2 * k1[j]) + (-k0[j] + k2[j]) * s + (2 * k0[j] - 5 * k1[j] + 4 * k2[j] - k3[j]) * s2 + (-k0[j] + 3 * k1[j] - 3 * k2[j] + k3[j]) * s3));
}
export function camera(cam, POS, LOOK, t, sway = .012) { cam.position.set(...cr(POS, t)); cam.lookAt(...cr(LOOK, t)); cam.rotation.z += Math.sin(t * 1.7) * sway; }
// capa DOM: aparición con desenfoque
export function domIn(id, t, a, b = 99, d = .4) { const el = document.getElementById(id); if (!el) return; const v = seg(t, a, a + d) * (1 - seg(t, b - .25, b)); el.style.opacity = v; el.style.filter = `blur(${(1 - seg(t, a, a + d)) * 14}px)`; el.style.transform = `translateY(${(1 - ease.out(seg(t, a, a + d))) * 50}px) scale(${1 + (1 - ease.out(seg(t, a, a + d))) * .15})`; }
export function grain(t) { const gc = document.getElementById('grain').getContext('2d'); const id = gc.createImageData(540, 960); let s = Math.floor(t * 24) * 7919 + 1; for (let i = 0; i < id.data.length; i += 4) { s = (s * 16807) % 2147483647; const v = s & 255; id.data[i] = id.data[i + 1] = id.data[i + 2] = v; id.data[i + 3] = 255; } gc.putImageData(id, 0, 0); }
export const flash = (t, at, k = .5, d = .3) => { const el = document.getElementById('flash'); if (el) el.style.opacity = Math.max(0, k * (1 - seg(t, at, at + d)) * (t >= at ? 1 : 0)); };
