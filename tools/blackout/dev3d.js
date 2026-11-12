// Móvil 3D de ProTeam (módulo). buildPhone(THREE, RoundedBoxGeometry, opts) -> {group, screen, P}
export function buildPhone(THREE, RoundedBoxGeometry, Q = new URLSearchParams()) {
  const S = new THREE.Group();
// ---------- utilidades
function rrShape(w, h, r, cx = 0, cy = 0) {
  const s = new THREE.Shape(), x = cx - w / 2, y = cy - h / 2;
  s.moveTo(x + r, y); s.lineTo(x + w - r, y); s.absarc(x + w - r, y + r, r, -Math.PI / 2, 0, false);
  s.lineTo(x + w, y + h - r); s.absarc(x + w - r, y + h - r, r, 0, Math.PI / 2, false);
  s.lineTo(x + r, y + h); s.absarc(x + r, y + h - r, r, Math.PI / 2, Math.PI, false);
  s.lineTo(x, y + r); s.absarc(x + r, y + r, r, Math.PI, Math.PI * 1.5, false); return s;
}
// rectángulo con radio solo arriba (pantalla del portátil)
function rrTop(w, h, r) {
  const s = new THREE.Shape(), x = -w / 2, y = -h / 2;
  s.moveTo(x, y); s.lineTo(x + w, y); s.lineTo(x + w, y + h - r); s.absarc(x + w - r, y + h - r, r, 0, Math.PI / 2, false);
  s.lineTo(x + r, y + h); s.absarc(x + r, y + h - r, r, Math.PI / 2, Math.PI, false); s.lineTo(x, y); return s;
}
function slab(shape, depth, bevel, segs = 6) {
  const g = new THREE.ExtrudeGeometry(shape, { depth, bevelEnabled: bevel > 0, bevelThickness: bevel, bevelSize: bevel, bevelSegments: segs, curveSegments: 48 });
  g.translate(0, 0, -depth / 2); return g;
}
function flatUV(g, w, h) {  // UV 0..1 a partir de la posición (para ShapeGeometry)
  const p = g.attributes.position, uv = g.attributes.uv;
  for (let i = 0; i < p.count; i++) uv.setXY(i, p.getX(i) / w + .5, p.getY(i) / h + .5);
  uv.needsUpdate = true; return g;
}
const texLoader = new THREE.TextureLoader();
function screenMat() { const m = new THREE.MeshBasicMaterial({ color: '#000', toneMapped: false }); return m; }

// ---------- materiales
const TI = { natural: '#8f8d88', black: '#2d2e31', blue: '#3b4656', white: '#d8d6d0' }[Q.get('ti') || 'black'];
const titanium = new THREE.MeshPhysicalMaterial({ color: TI, metalness: 1, roughness: .32, envMapIntensity: 1.25, clearcoat: .3, clearcoatRoughness: .4 });
const glassBlack = new THREE.MeshPhysicalMaterial({ color: '#020203', metalness: 0, roughness: .08, clearcoat: 1, clearcoatRoughness: .05, envMapIntensity: .35 });
const backGlass = new THREE.MeshPhysicalMaterial({ color: TI, metalness: .25, roughness: .55, envMapIntensity: .8 });
const lensGlass = new THREE.MeshPhysicalMaterial({ color: '#0b0d12', metalness: .2, roughness: .05, clearcoat: 1, envMapIntensity: 1.4 });
const alu = new THREE.MeshPhysicalMaterial({ color: '#1a1b1e', metalness: .55, roughness: .55, envMapIntensity: .3, clearcoat: .15 });
const keyMat = new THREE.MeshStandardMaterial({ color: '#050506', metalness: 0, roughness: .85, envMapIntensity: .2 });

// ---------- MÓVIL (≈ 71,5 × 146,6 × 8,25 mm; radio de esquina 11,6 mm; marco 1,5 mm)
const P = { w: .0715, h: .1466, d: .0072, r: .0116, bezel: .0016 };
const phone = new THREE.Group(); S.add(phone);
{
  const bev = .00062;
  const body = new THREE.Mesh(slab(rrShape(P.w - 2 * bev, P.h - 2 * bev, P.r - bev), P.d - 2 * bev, bev, 8), titanium); phone.add(body);
  // cristal frontal: casi todo el frente, enrasado con el marco
  const fg = new THREE.Mesh(slab(rrShape(P.w - .0011, P.h - .0011, P.r - .0006), .0006, .00025, 4), glassBlack); fg.position.z = P.d / 2 + .00005; phone.add(fg);
  // pantalla (mismo radio que la curva del aparato, menos el marco)
  const sw = P.w - 2 * P.bezel - .0011, sh = P.h - 2 * P.bezel - .0011, sr = P.r - P.bezel - .0004;
  P.sw = sw; P.sh = sh;
  const sg = flatUV(new THREE.ShapeGeometry(rrShape(sw, sh, sr), 48), sw, sh);
  P.screen = new THREE.Mesh(sg, screenMat()); P.screen.position.z = P.d / 2 + .00085; phone.add(P.screen);
  // isla
  const isl = new THREE.Mesh(new THREE.ShapeGeometry(rrShape(.0126, .0037, .00185), 24), new THREE.MeshBasicMaterial({ color: '#000' }));
  isl.position.set(0, sh / 2 - .0035, P.d / 2 + .0009); phone.add(isl);
  // cristal trasero
  const bg = new THREE.Mesh(slab(rrShape(P.w - .0011, P.h - .0011, P.r - .0006), .0005, .0002, 4), backGlass); bg.position.z = -P.d / 2 - .00005; phone.add(bg);
  // módulo de cámaras
  const cam = new THREE.Group(); cam.position.set(P.w / 2 - .0215, P.h / 2 - .0215, -P.d / 2 - .0004); phone.add(cam);
  const plate = new THREE.Mesh(slab(rrShape(.035, .035, .0085), .0013, .0005, 6), backGlass); plate.position.z = -.0006; cam.add(plate);
  [[-.0082, .0082], [-.0082, -.0082], [.0085, 0]].forEach(([x, y]) => {
    const ring = new THREE.Mesh(new THREE.CylinderGeometry(.0068, .0068, .0022, 48), titanium); ring.rotation.x = Math.PI / 2; ring.position.set(x, y, -.0018); cam.add(ring);
    const lens = new THREE.Mesh(new THREE.CylinderGeometry(.0056, .0056, .0006, 48), lensGlass); lens.rotation.x = Math.PI / 2; lens.position.set(x, y, -.0030); cam.add(lens);
  });
  const fl = new THREE.Mesh(new THREE.CylinderGeometry(.0022, .0022, .0005, 24), new THREE.MeshStandardMaterial({ color: '#e8e2d0', roughness: .3 })); fl.rotation.x = Math.PI / 2; fl.position.set(.0085, .0115, -.0016); cam.add(fl);
  // botones laterales (redondeados)
  const btn = (x, y, l) => { const b = new THREE.Mesh(new RoundedBoxGeometry(.0013, l, .0028, 4, .0006), titanium); b.position.set(x, y, 0); phone.add(b); };
  btn(P.w / 2 + .0003, .03, .016); btn(-P.w / 2 - .0003, .036, .0058); btn(-P.w / 2 - .0003, .02, .01); btn(-P.w / 2 - .0003, .006, .01);
  btn(P.w / 2 + .0003, -.022, .0085);
}


  return { group: phone, P };
}
