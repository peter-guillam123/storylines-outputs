"""Storylines motion: ICE immigration enforcement crackdown (15 seconds).

Every piece of on-screen text is a C(text, source, support) claim. The
animation reads its words from T[key], so the screen and the manifest match.
Two articles could not be fetched in full; see sources/NOT-FETCHED.md. This
video uses neither of them as a source.
Build:  python3 outputs/motion-kit/motion.py outputs/motion-ice-crackdown
Render: python3 outputs/motion-kit/render.py outputs/motion-ice-crackdown
"""
from build import C

DATA_FILE = "trump-administration.json"
STORYLINE_INDEX = 2
SLUG = "ice-crackdown"
PAGE_TITLE = "ICE immigration enforcement crackdown: a Storylines video"
KICKER = "Trump administration"
DURATION = 15
SOUND = ("Narration by a synthetic British voice (Kokoro’s “Emma”), generated offline, over "
         "a sparse, restrained score: a held low chord and soft piano, with a chord at each new date. A muted close as "
         "the cage appears, three low pulses for the three incidents on 20 September, and a slow swell as the "
         "arrest figures fill the screen. No stingers.")

SRC = {
    "cage": "us-news/2026/sep/14/alligator-alcatraz-immigration-jail-cages-report",
    "miller": "us-news/2026/sep/19/stephen-miller-trump-migrant-children",
    "third": "us-news/2026/sep/21/what-is-trump-third-country-deportation-policy",
    "evan": "us-news/2026/sep/24/citizen-injured-ice-mistaken-fugitive-arrest",
}

THEME = """
--paper:#f3f1ee;--ink:#1b1e22;--muted:#5c5f63;--rule:#dad6d0;--card:#e8e4de;
--accent:#c4532f;--accent-strong:#a23f1f;--accent-ink:#fff;--chip:#1b1e22;--chip-ink:#f3f1ee;--focus:#2c63d6;
--hero-bg:#161a1e;--hero-bg-solid:#171b1f;--hero-ink:#f1eee9;--accent-on-hero:#f08a64;
--hero-glow:radial-gradient(55% 70% at 90% 5%,rgba(196,83,47,.45),transparent 60%),radial-gradient(60% 70% at 0% 110%,rgba(110,140,170,.35),transparent 60%);
"""
THEME_DARK = """
--paper:#121417;--ink:#ebe8e3;--muted:#a3a5a8;--rule:#2a2d31;--card:#1c1f23;
--accent:#f08a64;--accent-strong:#f5a384;--accent-ink:#121417;--chip:#ebe8e3;--chip-ink:#121417;--focus:#86adff;
"""

DEK = [C("Thirty seconds on the Trump administration’s immigration crackdown, through the Guardian’s reporting on "
         "detention, deportation, the courts and the street.",
         note="Summary of the video. Each element is sourced in the script below.")]


def D(label, note):
    return C(label, note=note)


SCRIPT = [
    {"time": "0:00", "label": "Title", "items": [
        ("kicker", D("Guardian reporting, 14–24 September 2026", "Span of publication dates of the Storyline’s articles.")),
        ("st", D("Street · Detention · Court · Removal", "Labels for the four stages of the crackdown, shown as a strip that lights up as each is covered.")),
    ]},
    {"time": "0:01", "label": "Reported 14 September · Detention", "items": [
        ("d1", D("Reported 14 Sept", "The Guardian published its report on the watchdog findings on 14 September 2026; the watchdog report's own date is not given.")),
        ("b1", C("Detainees at the since-closed Alligator Alcatraz were locked in metal cages, a watchdog finds", "cage",
                 ["Before the facility was shuttered, detainees at Florida’s “Alligator Alcatraz” federal immigration jail were frequently locked in outside metal cages no bigger than a phone booth, according to a damning government watchdog report",
                  "The notorious immigration jail closed in June"])),
        ("sq18", C("The cage: about 18 sq ft", "cage", "Each cage, the report noted, offered only about 18 sq ft of floor space")),
        ("sq37", C("ICE’s own minimum for one person: 37 sq ft", "cage",
                   "less than half the minimum 37 sq ft required for single-person spaces by ICE’s own published national detention standards")),
    ]},
    {"time": "0:04", "label": "18 September · Removal", "items": [
        ("d2", D("18 Sept", "Date: the explainer, published on Monday 21 September 2026, says the court ruled “on Friday”.")),
        ("b2", C("An appeals court rules Trump’s third-country deportation policy unlawful", "third",
                 "A US federal appeals court ruled on Friday that the Trump administration’s third-country removals policy was unlawful.")),
        ("b2b", C("“The third country deportation policy continues” – Homeland Security", "third",
                  "“The third country deportation policy continues,” James Percival, the Department of Homeland Security’s general counsel, said in a statement.")),
        ("n2", C("25,000+", "third", "has deported more than 25,000 migrants, refugees and asylum seekers to countries that are not their own")),
        ("n2l", C("people deported to countries that are not their own", "third",
                  "has deported more than 25,000 migrants, refugees and asylum seekers to countries that are not their own")),
        ("deals", C("35 deals with other countries", "third",
                    "The Trump administration has struck 35 deals allowing it to deport migrants and asylum seekers to countries that are not their own")),
    ]},
    {"time": "0:06", "label": "Reported 19 September · Court", "items": [
        ("d3", D("Reported 19 Sept", "Publication date of the Guardian’s report.")),
        ("b3", C("Almost 200,000 children ordered removed since Trump returned, an advocacy group finds", "miller",
                 ["Almost 200,000 children have been ordered removed from the US by immigration judges since Trump returned to the White House",
                  "according to analysis of data from the Department of Justice’s executive office for immigration review (EOIR) conducted by the California-based advocacy Mobile Pathways"])),
        ("mh", C("Children ordered removed each month", "miller",
                 "Removal orders rose from 7,366 a month in January 2025 to 16,200 in June, 16,750 in July")),
        ("m1", C("Jan 2025: 7,366", "miller", "Removal orders rose from 7,366 a month in January 2025")),
        ("m2", C("Jul 2026: 16,750", "miller", "16,750 in July", note="Year derived: the article, published in September 2026, describes “a rapid increase over this spring and summer”.")),
        ("m3", C("Aug 2026: 14,744", "miller", "and 14,744 in August", note="Year derived: August 2026, as for July.")),
        ("msrc", C("Source: Mobile Pathways analysis of court data", "miller",
                   "according to Mobile Pathways’ research")),
    ]},
    {"time": "0:08", "label": "Sunday 20 September · Street", "items": [
        ("d4", D("Sun 20 Sept", "Date: the Evanston article, published on Thursday 24 September 2026, says “on Sunday”.")),
        ("b4", C("Three violent incidents on one Sunday", "evan",
                 "The incident was one of three separate violent Sunday events involving federal immigration officers.")),
        ("i1", C("Evanston: a US citizen is hurt in an arrest attempt", "evan",
                 ["two federal immigration agents allegedly beat and badly injured a US citizen in a botched arrest attempt in Illinois",
                  "Evanston, a suburb of Chicago"])),
        ("i2", C("Austin: an ICE agent shoots a man at a traffic stop", "evan",
                 "In Austin, Texas, an ICE agent shot and seriously wounded a 28-year-old Venezuelan man in a traffic stop")),
        ("i3", C("Michigan: a man dies after reportedly fleeing officers", "evan",
                 "authorities are investigating the death of a 36-year-old Guatemalan national who crashed his car into a tree at high speed after reportedly attempting to flee immigration officers")),
    ]},
    {"time": "0:11", "label": "The scale", "items": [
        ("d5", D("July", "Month as given in the article.")),
        ("b5", C("A record 50,000 arrests in July alone", "evan", "resulted in a record 50,000 arrests in July alone")),
        ("b5b", C("as enforcement “surges”, especially into Democratic-run cities and states", "evan",
                  "with enforcement “surges” into Democratic-run cities and states in particular")),
        ("key", D("Each dot: 500 arrests", "Derived: 100 dots stand for 50,000 arrests.")),
    ]},
    {"time": "0:13", "label": "End card", "items": [
        ("ec", D("Drawn from Guardian journalism", "End card heading. The card lists every article in the Storyline by date and headline.")),
    ]},
]

CHECKS = [
    "**Order.** The Storyline covers different stages of one system rather than one chain of events, so the video runs "
    "in date order and lights up the stage each item belongs to. Two dates are the Guardian’s publication dates "
    "(14 and 19 September) and are labelled \"Reported\"; 18 and 20 September are the days the events happened.",
    "**Unfetched articles.** The Austin shooting and the miscarriages investigation could not be fetched in full. The "
    "Austin line is sourced to the Evanston article, which reports it; the miscarriages investigation is credited on "
    "the end card but not used.",
    "**Evanston.** The article says agents \"allegedly beat and badly injured\" the man; the police say he reported head, "
    "face and neck injuries, the mayor that he was treated for minor injuries. The screen says only that he was hurt in "
    "an arrest attempt.",
    "**The ruling.** The government's response is shown with the ruling: Homeland Security's general counsel said the "
    "policy continues. The article adds that the government has 90 days to appeal and is expected to.",
    "**Children's removal orders.** The figures are an analysis by the advocacy group Mobile Pathways, and the screen "
    "says so. The article gives \"almost 200,000\" in one place and \"more than 200,000\" in another; the video uses "
    "the first. Three monthly figures are shown: January 2025, July 2026 (the highest given) and August 2026 (the "
    "latest). June 2026 (16,200) is left out for space. The article gives no figures between January 2025 and June "
    "2026, so the bars are not joined as a trend line.",
    "**Alligator Alcatraz.** The screen says the jail has since closed. Staff told inspectors the cages were \"calming "
    "areas\", and DeSantis's office said the area met federal standards; neither fits in a 2.5-second beat, and both "
    "are in the explainer.",
    "**Dot grid.** 100 dots, each standing for 500 arrests, fill to 50,000. The unit is the video's own, and is labelled.",
    "**The cage graphic.** The squares' areas are in the ratio 18:37.",
    "**Images.** None. Type, colour and drawn shapes only. **Sound:** narration by a synthetic voice (Kokoro, run offline), with music and effects synthesised in code; no samples, no licensed music.",
]

ANIM_CSS = """
#stage{background:#111316;color:#ebe8e3}
.bg{position:absolute;inset:-10%;background:radial-gradient(45% 55% at 85% 10%,rgba(196,83,47,.30),transparent 70%),
  radial-gradient(55% 60% at 5% 100%,rgba(110,140,170,.25),transparent 70%)}
.grain{position:absolute;inset:0;opacity:.16;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.title{position:absolute;left:120px;top:250px;width:1600px}
.title .kick{font:800 30px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:#f08a64;margin-bottom:34px}
.title .tl{font:800 156px/.96 var(--sans);letter-spacing:-.04em}
.hd{position:absolute;left:120px;top:70px;font:700 26px/1 var(--sans);opacity:.8}
.strip{position:absolute;left:1060px;top:62px;width:740px;display:grid;grid-template-columns:repeat(4,1fr)}
.strip .sg{position:relative;padding-top:26px;font:800 20px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase}
.strip .sg::before{content:"";position:absolute;left:0;right:10px;top:0;height:8px;border-radius:4px;background:currentColor}
.date{position:absolute;left:120px;top:190px;font:800 40px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase}
.big{position:absolute;left:120px;top:280px;width:900px;font:800 84px/1.04 var(--sans);letter-spacing:-.03em}
.sub{position:absolute;left:120px;width:880px;font:600 40px/1.2 var(--sans);opacity:.9}
.inc{position:absolute;left:1120px;width:700px;font:600 44px/1.2 var(--sans)}
.inc b{color:#f08a64;font-weight:800}
.sq{position:absolute;border:5px solid #ebe8e3;border-radius:4px}
.sq.small{background:repeating-linear-gradient(90deg,#c39be0 0 5px,transparent 5px 16px);border-color:#c39be0}
.sql{position:absolute;font:700 34px/1.2 var(--sans);width:520px}
.sql.l18{color:#c39be0}
.n2{position:absolute;left:1120px;top:330px;font:900 150px/.85 var(--sans);letter-spacing:-.05em;color:#a6cc85}
.n2l{position:absolute;left:1128px;top:480px;width:680px;font:600 38px/1.2 var(--sans)}
.dealdots{position:absolute;left:1128px;top:620px;width:680px;display:flex;flex-wrap:wrap;gap:12px}
.dealdots i{width:26px;height:26px;border-radius:50%;background:#a6cc85}
.deals{position:absolute;left:1128px;top:750px;font:800 26px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:#a6cc85}
.mh{position:absolute;left:1120px;top:330px;font:800 26px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:#79bde0}
.mbar{position:absolute;left:1120px;height:120px;background:#79bde0;border-radius:8px;transform-origin:left}
.mlab{position:absolute;left:1120px;font:800 40px/1 var(--sans)}
.place{position:absolute;left:1180px;width:30px;height:30px;border-radius:50%;background:#f08a64}
.grid{position:absolute;left:1120px;top:250px;width:700px;display:grid;grid-template-columns:repeat(10,1fr);gap:18px}
.grid i{width:46px;height:46px;border-radius:50%;background:#f08a64}
.key{position:absolute;left:1120px;top:900px;font:700 24px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;opacity:.7}
:root{--ec-bg:#f3f1ee;--ec-ink:#1b1e22;--ec-accent:#a23f1f;--ec-rule:#dad6d0}
.ec-list{gap:14px!important}.ec-list li{padding-top:14px!important}.ec-h{font-size:33px!important}
"""

JS = r"""
const POSTER_T = 12.7;
const SC = ['#f08a64', '#c39be0', '#79bde0', '#a6cc85'];   // street, detention, court, removal
let S = {};
function setup() {
  S.bg = mk('div', 'bg'); mk('div', 'grain');
  S.title = mk('div', 'title');
  S.kick = words(S.title, T.kicker, 'kick');
  S.tl = [words(S.title, 'ICE immigration', 'tl'), words(S.title, 'enforcement', 'tl'), words(S.title, 'crackdown', 'tl')];
  S.hd = mk('div', 'hd', null, T.title);
  const st = mk('div', 'strip'); S.strip = st;
  S.sg = T.st.split(' · ').map((n, i) => { const e = mk('div', 'sg', st, n); return e; });
  S.rail = rail(['14 Sept', '18 Sept', '19 Sept', '20 Sept'], { color: '#ebe8e3', accent: '#f08a64' });
  S.dates = ['d1', 'd2', 'd3', 'd4', 'd5'].map((k, i) => { const w = words(STAGE, T[k], 'date'); w.line.style.color = [SC[1], SC[3], SC[2], SC[0], SC[0]][i]; return w; });
  S.b = {};
  ['b1', 'b2', 'b3', 'b4', 'b5'].forEach(k => S.b[k] = words(STAGE, T[k], 'big'));
  S.b2b = words(STAGE, T.b2b, 'sub'); S.b2b.line.style.top = '690px';
  S.b5b = words(STAGE, T.b5b, 'sub'); S.b5b.line.style.top = '480px';
  S.inc = ['i1', 'i2', 'i3'].map((k, i) => { const w = words(STAGE, T[k], 'inc'); w.line.style.top = (300 + i * 170) + 'px'; return w; });
  // cage
  S.sq37 = mk('div', 'sq'); S.sq18 = mk('div', 'sq small');
  const big = 420, small = Math.round(big * Math.sqrt(18 / 37));
  Object.assign(S.sq37.style, { left: '1120px', top: '300px', width: big + 'px', height: big + 'px' });
  Object.assign(S.sq18.style, { left: '1120px', top: (300 + big - small) + 'px', width: small + 'px', height: small + 'px' });
  S.l18 = mk('div', 'sql l18', null, T.sq18); Object.assign(S.l18.style, { left: '1120px', top: '750px' });
  S.l37 = mk('div', 'sql', null, T.sq37); Object.assign(S.l37.style, { left: '1120px', top: '800px' });
  // removal
  S.n2 = mk('div', 'n2', null, T.n2); S.n2l = mk('div', 'n2l', null, T.n2l);
  const dd = mk('div', 'dealdots'); S.dd = Array.from({ length: 35 }, () => mk('i', '', dd));
  S.deals = mk('div', 'deals', null, T.deals);
  // court
  S.mh = mk('div', 'mh', null, T.mh);
  S.mb = [[7366, 'm1'], [16750, 'm2'], [14744, 'm3']].map(([v, k], i) => {
    const b = mk('div', 'mbar'); Object.assign(b.style, { top: (390 + i * 160) + 'px', height: '80px', width: Math.round(680 * v / 16750) + 'px' });
    const l = mk('div', 'mlab', null, T[k]); l.style.top = (480 + i * 160) + 'px'; l.style.fontSize = '34px';
    return { b, l }; });
  S.msrc = mk('div', 'key', null, T.msrc); S.msrc.style.top = '870px';
  // street
  S.places = [0, 1, 2].map(i => { const e = mk('div', 'place'); e.style.top = (312 + i * 170) + 'px'; e.style.left = '1060px'; return e; });
  // scale
  const g = mk('div', 'grid'); S.dots = Array.from({ length: 100 }, () => mk('i', '', g));
  S.key = mk('div', 'key', null, T.key);
}

function frame(t) {
  tf(S.bg, { x: Math.sin(t * 0.3) * 30, y: Math.cos(t * 0.22) * 24 });
  wordsIO(S.kick, t, 0.1, 1.05, { stagger: 0.02 });
  S.tl.forEach((w, i) => wordsIO(w, t, 0.15 + i * 0.12, 1.15 + i * 0.03, { stagger: 0.05, dur: 0.6, ease: E.outCubic }));
  S.title.style.visibility = t < 1.6 ? 'visible' : 'hidden';
  S.hd.style.opacity = E.outCubic(P(t, 1.45, 1.9)) * (1 - P(t, 13.2, 13.5));

  // stage strip: lights up the stage each beat belongs to
  const beats = [[1.5, 4.0, 1], [4.0, 6.4, 3], [6.4, 8.6, 2], [8.6, 11.0, 0]];
  const stripVis = E.outCubic(P(t, 1.5, 2.0)) * (1 - P(t, 13.2, 13.5));
  S.strip.style.opacity = stripVis;
  S.sg.forEach((e, i) => {
    let on = 0, seen = 0;
    beats.forEach(([a, b, s]) => { if (s === i) { on = Math.max(on, env(t, a, b - 0.1, 0.3, 0.3, E.outCubic, E.inCubic)); if (t > a) seen = 1; } });
    if (t > 11.0) on = 0.6;
    e.style.color = SC[i];
    e.style.opacity = 0.25 + 0.75 * Math.max(on, seen * 0.35);
  });

  S.rail.pose(t, [[0, 0], [1.5, 0], [4.0, 1], [6.4, 2], [8.6, 3]],
    E.outCubic(P(t, 1.4, 1.9)) * (1 - E.inCubic(P(t, 10.8, 11.2))));
  const bt = [[1.5, 3.9], [4.0, 6.3], [6.4, 8.5], [8.6, 10.9], [11.0, 13.3]];
  S.dates.forEach((w, i) => wordsIO(w, t, bt[i][0], bt[i][1], { stagger: 0.03, ease: E.outCubic }));
  const o = { stagger: 0.03, ease: E.outCubic, dur: 0.5 };
  wordsIO(S.b.b1, t, 1.6, 3.9, o);
  wordsIO(S.b.b2, t, 4.1, 6.3, o);
  wordsIO(S.b2b, t, 4.8, 6.3, { ...o, stagger: 0.02 });
  wordsIO(S.b.b3, t, 6.5, 8.5, o);
  wordsIO(S.b.b4, t, 8.7, 10.9, o);
  S.inc.forEach((w, i) => wordsIO(w, t, 9.25 + i * 0.35, 10.9, { ...o, stagger: 0.02 }));
  wordsIO(S.b.b5, t, 11.1, 13.3, o);
  wordsIO(S.b5b, t, 11.5, 13.3, { ...o, stagger: 0.02 });

  // cage: the ICE minimum draws, then the cage appears inside it
  const vC = env(t, 1.8, 3.85, 0.5, 0.3, E.outCubic);
  const d37 = E.outCubic(P(t, 1.8, 2.5));
  S.sq37.style.clipPath = `inset(0 ${(1 - d37) * 100}% 0 0)`;
  S.sq37.style.opacity = vC;
  const d18 = E.outCubic(P(t, 2.4, 2.9));
  tf(S.sq18, { y: (1 - d18) * 30, o: d18 * vC });
  tf(S.l18, { o: E.outCubic(P(t, 2.6, 2.9)) * vC });
  tf(S.l37, { o: E.outCubic(P(t, 2.1, 2.4)) * vC });

  // removal
  const vR = env(t, 4.2, 6.3, 0.45, 0.3, E.outCubic);
  counter(S.n2, t, 4.2, 5.0, 0, 25000, v => fmtInt(v) + (v > 24999 ? '+' : ''), E.outCubic);
  tf(S.n2, { y: (1 - E.outCubic(P(t, 4.2, 4.6))) * 40, o: vR });
  tf(S.n2l, { o: E.outCubic(P(t, 4.4, 4.7)) * vR });
  S.dd.forEach((d, i) => { const q = E.outCubic(P(t, 4.9 + i * 0.018, 5.15 + i * 0.018)); d.style.transform = `scale(${q})`; d.style.opacity = vR; });
  tf(S.deals, { o: E.outCubic(P(t, 5.3, 5.6)) * vR });

  // court
  const vM = env(t, 6.6, 8.5, 0.45, 0.3, E.outCubic);
  S.mh.style.opacity = vM;
  S.mb.forEach(({ b, l }, i) => {
    const a = 6.8 + i * 0.22;
    b.style.transform = `scaleX(${E.outCubic(P(t, a, a + 0.6))})`; b.style.opacity = (i === 0 ? 0.55 : 1) * vM;
    l.style.opacity = E.outCubic(P(t, a + 0.3, a + 0.6)) * vM; });
  S.msrc.style.opacity = E.outCubic(P(t, 7.4, 7.7)) * vM;

  // street: a marker beside each incident
  S.places.forEach((p, i) => {
    const a = 9.25 + i * 0.35;
    const q = E.outCubic(P(t, a, a + 0.3)) * (1 - E.inCubic(P(t, 10.9, 11.2)));
    const pulse = 1 + 0.25 * Math.max(0, Math.sin((t - a) * 5));
    p.style.transform = `scale(${q * pulse})`; p.style.opacity = q;
    p.style.boxShadow = `0 0 ${20 * q}px #f08a64`;
  });

  // scale: 100 dots fill in, each 500 arrests
  const vG = env(t, 11.1, 13.2, 0.4, 0.3, E.outCubic);
  S.dots.forEach((d, i) => {
    const r = Math.floor(i / 10), c = i % 10;
    const q = E.outCubic(P(t, 11.2 + (r + c) * 0.045, 11.5 + (r + c) * 0.045));
    d.style.transform = `scale(${q})`; d.style.opacity = vG;
  });
  S.key.style.opacity = E.outCubic(P(t, 11.9, 12.2)) * vG;
  endCard(t, 13.4);
}
"""

MIX = {"music_gain": 0.7, "fx_gain": 0.8, "rt": 2.6}


def score(A):
    """Sparse and restrained, in E minor: low piano and a held pad. No stingers."""
    m, N = A.mix, A.note
    m.add(A.pad([N("E2"), N("B2")], A.LEN, cutoff=480, a=1.0, r=1.0), 0.0, "music", gain=0.55, verb=0.3)
    cues = []
    def chord(t0, ns, vel=0.7):
        for j, n in enumerate(ns):
            m.add(A.piano(N(n), 3.0, vel), t0 + j * 0.02, "music", gain=0.9, verb=0.55)
        cues.append(t0)
    chord(0.15, ["E2", "B2"], 0.8)
    chord(1.5, ["E3", "G3", "B3"])
    chord(4.0, ["C3", "E3", "G3", "B3"])
    chord(6.4, ["A2", "E3", "C4"])
    chord(8.6, ["B2", "E3", "F#3"], 0.6)
    chord(11.0, ["E3", "G3", "B3"])
    # the cage: the outline draws, then the cage closes inside it
    m.add(A.sweep_noise(0.7, 300, 1500), 1.8, gain=0.1, verb=0.3)
    m.add(A.thud(72, 40, 0.6, 9, 0.05), 2.45, gain=0.35, verb=0.3); cues.append(2.45)
    # removal: a quiet shimmer as the 35 deals appear
    m.add(A.sweep_noise(0.9, 2200, 6500), 4.9, gain=0.07, pan=0.4, verb=0.5); cues.append(4.9)
    # court: three low notes with the three bars
    for t0, n in [(6.8, "A3"), (7.02, "E4"), (7.24, "D4")]:
        m.add(A.piano(N(n), 2.0, 0.5), t0, "music", gain=0.8, verb=0.5); cues.append(t0)
    # street: three low pulses, one per incident
    for t0 in [9.25, 9.6, 9.95]:
        m.add(A.thud(60, 35, 0.5, 6, 0.0), t0, gain=0.35, verb=0.3); cues.append(t0)
    # scale: the dots fill as the sound thickens
    m.add(A.pad([N("E3"), N("B3"), N("E4")], A.D(11.1, 13.7), cutoff=400, a=1.0, r=0.8, bright_end=2600), 11.1, "music", gain=0.45, verb=0.4)
    m.add(A.sweep_noise(1.4, 300, 3000), 11.2, gain=0.1, verb=0.3); cues.append(11.2)
    # end card
    m.add(A.sweep_noise(0.5, 5000, 800), 13.35, gain=0.08, verb=0.3)
    chord(13.45, ["E2", "B2", "G3"], 0.6)
    return cues

# ---- 30-second cut with narration (see motion-kit/timing.py)
LENGTH = 30
VOICE = "bf_emma"
SEGMENTS = [(0, 1.5, 1.2), (1.5, 4.0, 1.5, 3.4), (4.0, 6.4, 1.7, 3.6), (6.4, 8.6, 1.5, 3.4), (8.6, 11.0, 1.9, 3.8), (11.0, 13.4, 1.5, 2.6), (13.4, 15, 1.2)]
SCRIPT_SEG = [0, 1, 2, 3, 4, 5, 6]
NARRATION = [
    (1, "n1", C("A watchdog found detainees were locked in cages the size of phone booths.", "cage",
                ["Alligator Alcatraz held detainees in cages the size of phone booths, DHS watchdog says",
                 "detainees at Florida’s “Alligator Alcatraz” federal immigration jail were frequently locked in outside metal cages no bigger than a phone booth"])),
    (2, "n2", C("An appeals court ruled the third-country deportation policy unlawful.", "third",
                "A US federal appeals court ruled on Friday that the Trump administration’s third-country removals policy was unlawful.")),
    (3, "n4", C("An advocacy group found almost two hundred thousand children ordered removed since Trump’s return.", "miller",
                ["Almost 200,000 children have been ordered removed from the US by immigration judges since Trump returned to the White House",
                 "conducted by the California-based advocacy Mobile Pathways"])),
    (4, "n5", C("And on one Sunday, three violent incidents involving immigration officers.", "evan",
                "The incident was one of three separate violent Sunday events involving federal immigration officers.")),
]
