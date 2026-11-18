import { JSDOM } from "jsdom";
async function run(patched) {
  const { window } = new JSDOM(`<body><input placeholder="Cerca jugador"><button aria-label="Tancar menú"></button></body>`);
  const { document, MutationObserver, Node } = window;
  const ATTRS = ["title","placeholder","aria-label","alt","aria-placeholder"];
  const originalAttr = new WeakMap(), appliedAttr = new WeakMap();
  let calls = 0;
  const lookup = (d, s) => d[s];
  function translateAttrs(el, dict) {
    calls++;
    let store = originalAttr.get(el);
    for (const a of ATTRS) {
      if (!el.hasAttribute(a)) continue;
      if (!store) { store = {}; originalAttr.set(el, store); }
      if (store[a] === undefined) store[a] = el.getAttribute(a) ?? "";
      const source = store[a]; const trimmed = source.trim(); if (!trimmed) continue;
      const next = lookup(dict, trimmed) ?? source;
      if (patched) { let ap = appliedAttr.get(el); if (!ap) { ap = {}; appliedAttr.set(el, ap); } ap[a] = next; }
      if (el.getAttribute(a) !== next) el.setAttribute(a, next);
    }
  }
  let dict = {};
  new MutationObserver((records) => {
    for (const r of records) if (r.type === "attributes") {
      const el = r.target; const name = r.attributeName;
      if (patched && name && el.getAttribute(name) === appliedAttr.get(el)?.[name]) continue;
      const store = originalAttr.get(el); if (store && name) delete store[name];
      translateAttrs(el, dict);
    }
  }).observe(document.body, { subtree: true, attributes: true, attributeFilter: ATTRS });
  const tick = () => new Promise(r => setTimeout(r, 0));
  const all = () => document.querySelectorAll("input,button").forEach(e => translateAttrs(e, dict));
  dict = { "Cerca jugador": "Buscar jugador", "Tancar menú": "Cerrar menú" }; all(); await tick();
  const es = [document.querySelector("input").placeholder, document.querySelector("button").getAttribute("aria-label")];
  dict = { "Cerca jugador": "Search player", "Tancar menú": "Close menu" }; all(); await tick();
  const en = [document.querySelector("input").placeholder, document.querySelector("button").getAttribute("aria-label")];
  // React vuelve a escribir el original catalán: debe traducirse
  document.querySelector("input").setAttribute("placeholder", "Cerca jugador"); await tick();
  console.log(patched ? "CON parche" : "SIN parche", { es, en, react: document.querySelector("input").placeholder, llamadas: calls });
}
await run(false); await run(true);
