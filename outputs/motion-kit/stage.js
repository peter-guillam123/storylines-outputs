/* Storylines motion: a tiny deterministic animation toolkit.
   Every frame is a pure function of time t (seconds), so the renderer can
   seek to any frame and get the same picture. Pages define setup() to build
   the DOM once and frame(t) to pose it. */
const W = 1920, H = 1080;
const STAGE = document.getElementById('stage');
const clamp = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const lerp = (a, b, t) => a + (b - a) * t;
const P = (t, a, b) => clamp((t - a) / (b - a));
const E = {
  lin: t => t,
  outCubic: t => 1 - Math.pow(1 - t, 3),
  inCubic: t => t * t * t,
  inOutCubic: t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  outQuint: t => 1 - Math.pow(1 - t, 5),
  outExpo: t => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t)),
  inExpo: t => (t <= 0 ? 0 : Math.pow(2, 10 * t - 10)),
  inOutExpo: t => (t <= 0 ? 0 : t >= 1 ? 1 : t < 0.5 ? Math.pow(2, 20 * t - 10) / 2 : (2 - Math.pow(2, -20 * t + 10)) / 2),
  outBack: t => { const c1 = 1.4, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); },
};
/* in-then-out envelope: 0 before a, eases to 1 by a+din, holds, eases to 0 over [b, b+dout] */
const env = (t, a, b, din = 0.45, dout = 0.35, ein = E.outExpo, eout = E.inCubic) =>
  ein(P(t, a, a + din)) * (1 - eout(P(t, b, b + dout)));

function mk(tag, cls, parent, text) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text != null) e.textContent = text;
  (parent || STAGE).appendChild(e);
  return e;
}
function svg(tag, attrs, parent) {
  const e = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (parent) parent.appendChild(e);
  return e;
}
function tf(e, { x = 0, y = 0, s = 1, sx, sy, r = 0, o } = {}) {
  e.style.transform = `translate(${x}px,${y}px) rotate(${r}deg) scale(${sx ?? s},${sy ?? s})`;
  if (o != null) e.style.opacity = o;
}
/* Split text into masked words for kinetic reveals. */
function words(parent, text, cls) {
  const line = mk('div', cls, parent);
  const ws = text.split(' ').map(w => {
    const m = mk('span', 'wm', line);
    return mk('span', 'wi', m, w);
  });
  return { line, ws };
}
/* Words rise into their masks, then drop out. */
function wordsIO(w, t, tin, tout, { stagger = 0.035, dur = 0.55, ease = E.outExpo, outDur = 0.3 } = {}) {
  w.ws.forEach((e, i) => {
    const pin = ease(P(t, tin + i * stagger, tin + i * stagger + dur));
    const pout = tout == null ? 0 : E.inCubic(P(t, tout + i * stagger * 0.4, tout + i * stagger * 0.4 + outDur));
    e.style.transform = `translateY(${(1 - pin) * 112 - pout * 112}%)`;
  });
  w.line.style.visibility = t < tin - 0.01 || (tout != null && t > tout + outDur + w.ws.length * stagger) ? 'hidden' : 'visible';
}
/* A number that counts between two values. */
function counter(e, t, a, b, from, to, fmt, ease = E.outExpo) {
  e.textContent = fmt(lerp(from, to, ease(P(t, a, b))));
}
const fmtInt = v => Math.round(v).toLocaleString('en-GB');

/* The date rail: evenly spaced labelled stops along the bottom; a playhead
   eases between stops at given times. keys = [[time, stopIndex], ...] */
function rail(stops, { y = 980, x0 = 120, x1 = 1800, color = '#fff', accent = '#f60' } = {}) {
  const g = mk('div', 'rail');
  g.style.cssText = `position:absolute;left:0;top:0;width:${W}px;height:${H}px;pointer-events:none`;
  const line = mk('div', 'rail-line', g);
  line.style.cssText = `position:absolute;left:${x0}px;top:${y}px;height:2px;width:${x1 - x0}px;background:${color};opacity:.25;transform-origin:left`;
  const prog = mk('div', 'rail-prog', g);
  prog.style.cssText = `position:absolute;left:${x0}px;top:${y - 1}px;height:4px;width:${x1 - x0}px;background:${accent};transform-origin:left`;
  const xs = stops.map((_, i) => (stops.length === 1 ? x0 : x0 + ((x1 - x0) * i) / (stops.length - 1)));
  const dots = stops.map((s, i) => {
    const d = mk('div', 'rail-dot', g);
    d.style.cssText = `position:absolute;left:${xs[i] - 9}px;top:${y - 8}px;width:18px;height:18px;border-radius:50%;border:3px solid ${color};background:transparent;box-sizing:border-box`;
    const l = mk('div', 'rail-lab', g, s);
    l.style.cssText = `position:absolute;left:${xs[i]}px;top:${y + 22}px;transform:translateX(-50%);font:700 22px/1 var(--sans);letter-spacing:.12em;color:${color};white-space:nowrap`;
    return { d, l };
  });
  const head = mk('div', 'rail-head', g);
  head.style.cssText = `position:absolute;left:0;top:${y - 15}px;width:32px;height:32px;border-radius:50%;background:${accent};box-shadow:0 0 0 10px ${accent}33,0 0 40px ${accent}`;
  return {
    g,
    pose(t, keys, vis) {
      g.style.opacity = vis;
      let pos = keys[0][1];
      for (let i = 1; i < keys.length; i++) {
        const [tk, sk] = keys[i], [tp, sp] = keys[i - 1];
        if (t >= tk) pos = sk; else if (t > tk - 0.3) { pos = lerp(sp, sk, E.inOutCubic(P(t, tk - 0.3, tk))); break; } else break;
      }
      const fi = Math.floor(pos), fr = pos - fi;
      const x = fi >= xs.length - 1 ? xs[xs.length - 1] : lerp(xs[fi], xs[fi + 1], fr);
      head.style.transform = `translateX(${x - 16}px)`;
      prog.style.transform = `scaleX(${(x - x0) / (x1 - x0)})`;
      line.style.transform = `scaleX(${E.outExpo(clamp(vis * 1.2))})`;
      dots.forEach((d, i) => {
        const on = pos >= i - 0.02;
        d.d.style.background = on ? accent : 'transparent';
        d.d.style.borderColor = on ? accent : color;
        d.l.style.opacity = Math.abs(pos - i) < 0.35 ? 1 : on ? 0.55 : 0.3;
        d.l.style.color = Math.abs(pos - i) < 0.35 ? accent : color;
      });
    },
  };
}

/* The end card: credits every Guardian article the video draws on. */
function endCard(t, t0, opts) {
  if (!endCard.el) {
    const c = mk('div', 'endcard');
    const k = mk('div', 'ec-k', c, 'Drawn from Guardian journalism');
    const list = mk('ol', 'ec-list' + (CREDITS.length > 8 ? ' ec-many' : ''), c);
    const items = CREDITS.map(cr => {
      const li = mk('li', '', list);
      mk('span', 'ec-d', li, cr.date);
      mk('span', 'ec-h', li, cr.headline);
      if (cr.kind) mk('span', 'ec-kind', li, cr.kind);
      return li;
    });
    const f = mk('div', 'ec-f', c, 'Every fact on screen comes from these articles · theguardian.com');
    endCard.el = { c, k, items, f };
  }
  const e = endCard.el;
  const p = E.outExpo(P(t, t0, t0 + 0.6));
  e.c.style.visibility = t < t0 ? 'hidden' : 'visible';
  e.c.style.clipPath = `inset(${(1 - p) * 100}% 0 0 0)`;
  tf(e.k, { y: (1 - E.outExpo(P(t, t0 + 0.15, t0 + 0.7))) * 40, o: P(t, t0 + 0.15, t0 + 0.5) });
  e.items.forEach((li, i) => {
    const q = E.outExpo(P(t, t0 + 0.25 + i * 0.06, t0 + 0.85 + i * 0.06));
    tf(li, { y: (1 - q) * 30, o: q });
  });
  tf(e.f, { o: P(t, t0 + 0.7, t0 + 1.0) });
}

let READY = false;
/* The piece is authored on a short design timeline; WARP (from timing.json) maps
   finished-video time to design time, holding each finished frame for longer. */
function warp(t) {
  if (typeof WARP === 'undefined' || !WARP.length) return t;
  if (t <= WARP[0][0]) return WARP[0][1];
  for (let i = 1; i < WARP.length; i++) {
    const [x1, y1] = WARP[i], [x0, y0] = WARP[i - 1];
    if (t <= x1) return y0 + (y1 - y0) * (t - x0) / (x1 - x0);
  }
  return WARP[WARP.length - 1][1];
}
function renderAt(t) { frame(warp(Math.min(t, DURATION - 1e-4))); }
function fit() {
  const s = Math.min(innerWidth / W, innerHeight / H);
  STAGE.style.transform = `translate(${(innerWidth - W * s) / 2}px,${(innerHeight - H * s) / 2}px) scale(${s})`;
}
document.fonts.ready.then(() => {
  setup();
  renderAt(0);
  READY = true;
  if (!location.search.includes('render')) {
    fit();
    addEventListener('resize', fit);
    const t0 = performance.now();
    const loop = now => { renderAt(((now - t0) / 1000) % (DURATION + 1.5)); requestAnimationFrame(loop); };
    requestAnimationFrame(loop);
  }
});
