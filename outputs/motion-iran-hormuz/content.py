"""Storylines motion: US-Iran war and Hormuz negotiations (15 seconds).

Every piece of on-screen text is a C(text, source, support) claim. The
animation reads its words from T[key], so the screen and the manifest match.
Build:  python3 outputs/motion-kit/motion.py outputs/motion-iran-hormuz
Render: python3 outputs/motion-kit/render.py outputs/motion-iran-hormuz
"""
from build import C

DATA_FILE = "trump-administration.json"
STORYLINE_INDEX = 1
SLUG = "iran-hormuz"
PAGE_TITLE = "US-Iran war and Hormuz negotiations: a Storylines video"
KICKER = "Trump administration"
DURATION = 15
SOUND = ("Narration by a synthetic British voice (Kokoro’s “Emma”), generated offline, over "
         "a low drone with a sea-like wash. The February strikes are marked by muted low pulses, not explosions. "
         "A slowing count runs under the cost figure, a soft chime marks each stage of Iran’s offer, and the "
         "video ends on an unresolved chord and a slow clock for the wait for Trump’s answer.")

SRC = {
    "house": "world/2026/sep/15/iran-war-cost-cbo-report",
    "un": "us-news/2026/sep/22/trump-calls-on-allies-enforce-complete-economic-isolation-iran-un-speech",
    "talks": "world/2026/sep/23/iran-denies-dropping-preconditions-very-productive-three-hour-un-talks-new-york",
    "offer": "world/2026/sep/24/ed-miliband-meets-iran-foreign-minister-us-ultimatum-strait-hormuz",
    "choices": "world/2026/sep/25/trump-tough-choices-iran-accelerated-deal-reopen-hormuz-midterm-elections",
}

THEME = """
--paper:#f1f4f2;--ink:#0f1d20;--muted:#51626a;--rule:#d0dad8;--card:#e2eae8;
--accent:#d9822b;--accent-strong:#9c520c;--accent-ink:#0f1d20;--chip:#0f1d20;--chip-ink:#f1f4f2;--focus:#1f6fd1;
--hero-bg:#06242a;--hero-bg-solid:#08262c;--hero-ink:#eef3f1;--accent-on-hero:#f2a950;
--hero-glow:radial-gradient(60% 70% at 92% 0%,rgba(242,169,80,.5),transparent 60%),radial-gradient(70% 70% at 0% 110%,rgba(30,160,170,.45),transparent 60%);
"""
THEME_DARK = """
--paper:#0c1618;--ink:#e6eeec;--muted:#9fb0b4;--rule:#1f2e31;--card:#142326;
--accent:#f2a950;--accent-strong:#f6bd74;--accent-ink:#0c1618;--chip:#e6eeec;--chip-ink:#0c1618;--focus:#7fb4ff;
"""

DEK = [C("Thirty seconds on the war, its cost, and the offer Iran has put to Donald Trump to reopen the strait of "
         "Hormuz.", note="Summary of the video. Each element is sourced in the script below.")]


def D(label, note):
    return C(label, note=note)


SCRIPT = [
    {"time": "0:00", "label": "Title", "items": [
        ("kicker", D("Guardian reporting, 14–25 September 2026", "Span of publication dates of the Storyline’s articles.")),
    ]},
    {"time": "0:01", "label": "February", "items": [
        ("d1", D("February", "The UN speech article dates the joint strikes to “February” without a year.")),
        ("b1", C("The US and Israel strike Iran", "un", "since the US and Israel launched joint strikes in February")),
        ("iran", C("Iran", "offer", "Issues such as whether tolls or navigational fees could be imposed by the littoral states Oman and Iran",
                   note="Map label. The diagram puts Oman on the south side of the strait, as the 25 September article says, and Iran on the north.")),
        ("oman", C("Oman", "choices", "Oman, located on the south side of the strait")),
        ("strait", C("Strait of Hormuz", "talks", "the strait of Hormuz – a key waterway for transporting oil")),
        ("nts", D("Diagram, not to scale", "Label: the coastlines are drawn shapes, not a map.")),
    ]},
    {"time": "0:03", "label": "Since early in the war", "items": [
        ("d2", D("Since early in the war", "Phrase from the UN speech article.")),
        ("b2", C("Iran grips the strait of Hormuz", "un",
                 "Iran has maintained a stranglehold over energy shipping through the strait of Hormuz since early in the war")),
        ("b2b", C("a key waterway for transporting oil", "talks", "a key waterway for transporting oil")),
    ]},
    {"time": "0:04", "label": "15 September", "items": [
        ("d3", D("15 Sept", "Date: the CBO article was published on Tuesday 15 September 2026; the vote was “late on Tuesday”.")),
        ("b3", C("The war has cost at least", "house",
                 "a Congressional Budget Office (CBO) report showed the conflict had cost at least $38bn")),
        ("cost", C("$38bn", "house", "had cost at least $38bn")),
        ("costLab", C("so far, says Congress’s budget office, and $3bn more each month", "house",
                      ["a Congressional Budget Office (CBO) report showed the conflict had cost at least $38bn",
                       "It estimated that the costs of the war will grow $3bn for every month the conflict continues"])),
        ("b4", C("The House votes to end the war, for the third time", "house",
                 "The US House of Representatives has voted for a third time to end the war in Iran")),
        ("vFor", C("For 220", "house", "The final tally of 220-204",
                   note="220 is the vote approving the war powers resolution; 204 against.")),
        ("vAg", C("Against 204", "house", "The final tally of 220-204")),
        ("desk", C("None of the votes has reached Trump’s desk", "house",
                   "None of the resolutions have made it to the president’s desk, where Trump would almost certainly veto them.")),
    ]},
    {"time": "0:07", "label": "22 September", "items": [
        ("d5", D("22 Sept", "Date: the article, published on 22 September 2026, says the speech was “on Tuesday”.")),
        ("b5", C("At the UN, Trump calls for the “complete economic isolation of Iran”", "un",
                 "“I call on all nations to help to enforce the complete economic isolation of Iran,” Trump said in a speech to the UN general assembly on Tuesday.")),
        ("b5b", C("He also calls talks with Iran “very productive”", "talks",
                  ["Iran denies dropping preconditions amid ‘very productive’ three-hour UN talks in New York",
                   "Trump said the three-hour talks held in a room at the UN headquarters had gone very well and been very productive."],
                  note="The talks were reported on 23 September; the article does not give their date.")),
    ]},
    {"time": "0:09", "label": "24 September", "items": [
        ("d6", D("24 Sept", "Date: the article was published on Thursday 24 September 2026.")),
        ("b6", C("Iran says it has offered to reopen the strait in six days", "offer",
                 "Iran said it has told Donald Trump it is willing to open the strait of Hormuz in six days")),
        ("day15", D("Days 1–5", "Label for the first stage of the timetable (“In the first four to five days under this timetable”).")),
        ("t15", C("The US would lift its blockade and end the war on all fronts, including Lebanon", "choices",
                  "In the first four to five days under this timetable, the US would have to lift the naval blockade on Iran’s oil ports, restore the waiver that lifted sanctions on Iran’s oil exports, end the war on all fronts and permit the release of some of Iran’s frozen assets.",
                  note="Two of the four conditions, shortened for the screen; “including Lebanon” is from the same article: “order Benjamin Netanyahu to end Israel’s attacks on Hezbollah in Lebanon, thus achieving the “ceasefire on all fronts””. The explainer lists all four.")),
        ("day6", D("Day 6", "Label.")),
        ("t6", C("The strait would reopen", "choices", "On the sixth day, the strait of Hormuz would be reopened by Iran")),
        ("day7", D("Day 7", "Label.")),
        ("t7", C("Nuclear talks would start", "choices", "And on the next day, negotiations would start on the future of Iran’s civil nuclear programme")),
        ("route", C("Proposed route: Oman and Iran", "choices", "with ships using a new route designated by Oman and Iran")),
    ]},
    {"time": "0:12", "label": "What happens next", "items": [
        ("b8", C("Iran is waiting for Trump’s answer", "offer",
                 "Abbas Araghchi, the Iranian foreign minister, said he was waiting to hear a response from the Americans to the proposal.")),
        ("b8b", C("Iran’s foreign minister wants a deal before the US midterm elections", "offer",
                  "Araghchi added he would like the deal to go through before the midterm elections")),
    ]},
    {"time": "0:13", "label": "End card", "items": [
        ("ec", D("Drawn from Guardian journalism", "End card heading. The card lists every article in the Storyline by date and headline.")),
    ]},
]

CHECKS = [
    "**The strait diagram.** The coastlines are drawn shapes labelled \"Diagram, not to scale\", not a map. The only "
    "geography they assert is sourced: Oman lies on the south side of the strait (25 September article) and the "
    "strait's littoral states are Oman and Iran (24 September article). The moving dots stand for shipping, thinning "
    "as Iran grips the strait; they are not a count. The dashed line is the proposed route, not an existing one.",
    "**Oil prices.** An earlier cut showed $64 rising to $107 a barrel. It was dropped: the $107 figure (24 September) "
    "sat out of date order, the pair implied a steady rise (the price fell below $100 on 23 September), and next to "
    "\"Iran grips the strait\" it implied a single cause, while the article says the war in Ukraine has also pushed "
    "prices up.",
    "**When Iran made its offer.** The offer was laid out to US envoys earlier in the week (23 and 25 September "
    "articles) and described publicly by Araghchi on 24 September. The screen says \"Iran says it has offered\", "
    "dated 24 September, so it does not read as a reply to Trump's speech of 22 September.",
    "**Trump's side.** Alongside his call for Iran's isolation, the video gives his description of the talks as "
    "\"very productive\" (reported 23 September).",
    "**The vote.** The screen adds that none of the resolutions has reached Trump's desk, so the vote is not read as "
    "ending the war.",
    "**The vote tally.** The article gives the tally as 220-204 on a resolution to end the war. The bars are labelled \"For\" "
    "and \"Against\" on that basis.",
    "**Iran's offer.** The headline says \"six days\"; the timetable has the strait reopening on day six and nuclear talks "
    "on day seven. The screen shows two of the four US conditions for days one to five (lifting the blockade and ending "
    "the war on all fronts); the other two (restoring an oil sanctions waiver, releasing some frozen assets) are on the "
    "web page's script and in the explainer.",
    "**\"Iran grips the strait\".** Paraphrases the UN speech article's \"stranglehold over energy shipping\".",
    "**Left out.** The Minab school strike (conflicting figures between two articles), the talks in New York, and "
    "reactions from other countries. The opinion piece (Arwa Mahdawi) is credited on the end card but not quoted.",
    "**Images.** None. Type, colour and drawn shapes only. **Sound:** narration by a synthetic voice (Kokoro, run offline), with music and effects synthesised in code; no samples, no licensed music.",
]

ANIM_CSS = """
#stage{background:#05191d;color:#eef3f1}
.bg{position:absolute;inset:-10%;background:radial-gradient(45% 55% at 85% 10%,rgba(242,169,80,.34),transparent 70%),
  radial-gradient(55% 60% at 5% 100%,rgba(30,160,170,.35),transparent 70%)}
.grain{position:absolute;inset:0;opacity:.16;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.title{position:absolute;left:120px;top:250px;transform-origin:0 0;width:1500px;z-index:5}
.title .kick{font:800 30px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:#f2a950;margin-bottom:34px}
.title .tl{font:800 156px/.96 var(--sans);letter-spacing:-.04em}
.hd{position:absolute;left:120px;top:70px;font:700 26px/1 var(--sans);opacity:.8}
.date{position:absolute;left:120px;top:190px;font:800 40px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#f2a950}
.big{position:absolute;left:120px;top:280px;width:880px;font:800 88px/1.03 var(--sans);letter-spacing:-.03em}
.sub{position:absolute;left:120px;top:640px;width:860px;font:600 44px/1.2 var(--sans);opacity:.85}
.map{position:absolute;left:0;top:0;width:1920px;height:1080px}
.maplab{position:absolute;font:800 26px/1 var(--sans);letter-spacing:.3em;text-transform:uppercase;color:#9fd8de}
.nts{position:absolute;left:1560px;top:900px;font:600 18px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;opacity:.5}
.fig{position:absolute;left:112px;top:490px;font:900 200px/.85 var(--sans);letter-spacing:-.05em;color:#f2a950}
.figlab{position:absolute;left:120px;top:690px;width:840px;font:600 38px/1.2 var(--sans);opacity:.9}
.vbar{position:absolute;left:120px;height:90px;border-radius:10px;transform-origin:left}
.vlab{position:absolute;left:140px;font:800 40px/90px var(--sans);letter-spacing:.02em;color:#05191d}
.tt{position:absolute;left:120px;top:600px;width:900px;display:grid;grid-template-columns:2fr 1fr 1fr;gap:10px}
.tile{border-radius:14px;padding:18px 18px 20px;background:rgba(238,243,241,.08);box-shadow:inset 0 0 0 2px rgba(238,243,241,.25);min-height:200px}
.tile .tl2{font:800 20px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:#f2a950}
.tile .tx{font:700 28px/1.15 var(--sans);margin-top:12px}
.tile.hot{background:#f2a950;color:#05191d;box-shadow:none}
.tile.hot .tl2{color:#05191d}
.routeLab{position:absolute;left:1070px;top:432px;font:800 22px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#f2a950}
:root{--ec-bg:#eef3f1;--ec-ink:#0f1d20;--ec-accent:#9c520c;--ec-rule:#d0dad8}
.ec-list{gap:16px!important}.ec-list li{padding-top:16px!important}
"""

JS = r"""
const POSTER_T = 11.4;
let S = {};
// channel centreline, right (the Gulf) to left (open sea), in stage coordinates
const CH = 'M1880 470 C 1700 470, 1560 520, 1440 560 S 1180 600, 1040 640';
function setup() {
  S.bg = mk('div', 'bg'); mk('div', 'grain');
  // --- the strait diagram
  const m = svg('svg', { class: 'map', viewBox: '0 0 1920 1080' }, STAGE);
  const defs = svg('defs', {}, m);
  const lg = svg('linearGradient', { id: 'landfade', x1: '1000', x2: '1420', y1: 0, y2: 0, gradientUnits: 'userSpaceOnUse' }, defs);
  svg('stop', { offset: 0, 'stop-color': '#0d3940', 'stop-opacity': 0 }, lg); svg('stop', { offset: 1, 'stop-color': '#0d3940', 'stop-opacity': 1 }, lg);
  const cg = svg('linearGradient', { id: 'coastfade', x1: '1000', x2: '1300', y1: 0, y2: 0, gradientUnits: 'userSpaceOnUse' }, defs);
  svg('stop', { offset: 0, 'stop-color': '#4fc3cf', 'stop-opacity': 0 }, cg); svg('stop', { offset: 1, 'stop-color': '#4fc3cf', 'stop-opacity': 1 }, cg);
  S.mapG = svg('g', {}, m);
  S.north = svg('path', { d: 'M1000 0 H1920 V400 C 1800 410, 1700 420, 1590 470 C 1520 500, 1470 520, 1420 512 C 1330 500, 1230 520, 1130 560 C 1080 578, 1030 580, 1000 578 Z', fill: 'url(#landfade)' }, S.mapG);
  S.south = svg('path', { d: 'M1920 560 C 1800 555, 1700 580, 1620 610 C 1560 632, 1520 640, 1500 700 C 1480 760, 1400 800, 1300 820 C 1200 840, 1100 860, 1000 900 V1080 H1920 Z', fill: 'url(#landfade)' }, S.mapG);
  S.coastN = svg('path', { d: 'M1000 578 C 1030 580, 1080 578, 1130 560 C 1230 520, 1330 500, 1420 512 C 1470 520, 1520 500, 1590 470 C 1700 420, 1800 410, 1920 400', fill: 'none', stroke: 'url(#coastfade)', 'stroke-width': 3 }, S.mapG);
  S.coastS = svg('path', { d: 'M1920 560 C 1800 555, 1700 580, 1620 610 C 1560 632, 1520 640, 1500 700 C 1480 760, 1400 800, 1300 820 C 1200 840, 1100 860, 1000 900', fill: 'none', stroke: 'url(#coastfade)', 'stroke-width': 3 }, S.mapG);
  S.ch = svg('path', { d: CH, fill: 'none', stroke: 'none' }, S.mapG);
  S.chLen = S.ch.getTotalLength();
  S.route = svg('path', { d: 'M1880 455 C 1700 450, 1560 495, 1440 535 S 1180 575, 1040 615', fill: 'none', stroke: '#f2a950', 'stroke-width': 6, 'stroke-dasharray': '18 14' }, S.mapG);
  S.routeLen = S.route.getTotalLength();
  S.ships = Array.from({ length: 22 }, () => svg('rect', { width: 34, height: 12, rx: 6, fill: '#eef3f1' }, S.mapG));
  S.rings = [0, 1, 2].map(() => svg('circle', { r: 10, fill: 'none', stroke: '#f2a950', 'stroke-width': 4 }, S.mapG));
  S.labs = [['iran', 1640, 300], ['oman', 1640, 760], ['strait', 1130, 640]].map(([k, x, y]) => {
    const e = mk('div', 'maplab', null, T[k]); e.style.left = x + 'px'; e.style.top = y + 'px'; return e; });
  S.labs[2].style.fontSize = '20px'; S.labs[2].style.color = '#eef3f1';
  S.nts = mk('div', 'nts', null, T.nts);
  S.routeLab = mk('div', 'routeLab', null, T.route);

  // --- figures
  S.cost = mk('div', 'fig'); S.costLab = mk('div', 'figlab', null, T.costLab);
  S.vFor = mk('div', 'vbar'); S.vAg = mk('div', 'vbar');
  S.vFor.style.cssText += ';top:600px;background:#f2a950'; S.vAg.style.cssText += ';top:710px;background:#9fd8de';
  S.vForL = mk('div', 'vlab', null, T.vFor); S.vForL.style.top = '600px';
  S.vAgL = mk('div', 'vlab', null, T.vAg); S.vAgL.style.top = '710px';

  // --- timetable tiles
  const tt = mk('div', 'tt'); S.tt = tt;
  S.tiles = [['day15', 't15'], ['day6', 't6'], ['day7', 't7']].map(([a, b]) => {
    const e = mk('div', 'tile', tt); mk('div', 'tl2', e, T[a]); mk('div', 'tx', e, T[b]); return e; });

  // --- title
  S.title = mk('div', 'title');
  S.kick = words(S.title, T.kicker, 'kick');
  S.tl = [words(S.title, 'US-Iran war', 'tl'), words(S.title, 'and Hormuz', 'tl'), words(S.title, 'negotiations', 'tl')];
  S.hd = mk('div', 'hd', null, T.title);
  S.rail = rail(['Feb', '15 Sept', '22 Sept', '24 Sept'], { color: '#eef3f1', accent: '#f2a950' });
  S.dates = ['d1', 'd2', 'd3', 'd5', 'd6'].map(k => words(STAGE, T[k], 'date'));
  S.b = {};
  ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b8'].forEach(k => S.b[k] = words(STAGE, T[k], 'big'));
  S.b8b = words(STAGE, T.b8b, 'sub');
  S.b2b = words(STAGE, T.b2b, 'sub'); S.b2b.line.style.top = '500px';
  S.b5b = words(STAGE, T.b5b, 'sub'); S.b5b.line.style.top = '780px';
  S.desk = words(STAGE, T.desk, 'sub'); S.desk.line.style.top = '830px'; S.desk.line.style.fontSize = '36px';
}

function frame(t) {
  tf(S.bg, { x: Math.sin(t * 0.35) * 40, y: Math.cos(t * 0.25) * 30 });
  // title
  wordsIO(S.kick, t, 0.1, 1.05, { stagger: 0.02 });
  S.tl.forEach((w, i) => wordsIO(w, t, 0.15 + i * 0.12, 1.15 + i * 0.03, { stagger: 0.05, dur: 0.6 }));
  S.title.style.visibility = t < 1.6 ? 'visible' : 'hidden';
  S.hd.style.opacity = E.outCubic(P(t, 1.45, 1.9)) * (1 - P(t, 13.2, 13.5));
  S.rail.pose(t, [[0, 0], [1.5, 0], [3.0, 0.35], [4.8, 1], [7.8, 2], [9.2, 3]],
    E.outCubic(P(t, 1.4, 1.9)) * (1 - E.inCubic(P(t, 11.9, 12.3))));
  const bt = [[1.5, 2.9], [3.0, 4.7], [4.8, 7.7], [7.8, 9.1], [9.2, 11.9]];
  S.dates.forEach((w, i) => wordsIO(w, t, bt[i][0], bt[i][1], { stagger: 0.03 }));
  wordsIO(S.b.b1, t, 1.6, 2.9);
  wordsIO(S.b.b2, t, 3.05, 4.7, { stagger: 0.03 });
  wordsIO(S.b.b3, t, 4.85, 6.3, { stagger: 0.03 });
  wordsIO(S.b.b4, t, 6.4, 7.7, { stagger: 0.03 });
  wordsIO(S.b.b5, t, 7.85, 9.1, { stagger: 0.03 });
  wordsIO(S.b.b6, t, 9.25, 11.85, { stagger: 0.04 });
  wordsIO(S.b.b8, t, 12.0, 13.3, { stagger: 0.04, dur: 0.6 });
  wordsIO(S.b8b, t, 12.35, 13.3, { stagger: 0.03 });

  // map: appears with the war, dims behind the figures, returns for the offer
  const mapIn = E.outCubic(P(t, 1.3, 2.0));
  const dim = 0.5 * env(t, 4.75, 9.15, 0.35, 0.35, E.inOutCubic, E.inOutCubic);
  const mapOut = 1 - E.inCubic(P(t, 13.0, 13.4));
  S.mapG.style.opacity = mapIn * (1 - 0.8 * dim) * mapOut;
  const drawC = E.inOutCubic(P(t, 1.3, 2.3));
  [S.coastN, S.coastS].forEach(c => { c.style.strokeDasharray = 2400; c.style.strokeDashoffset = 2400 * (1 - drawC); });
  S.north.style.opacity = S.south.style.opacity = E.outCubic(P(t, 1.6, 2.4));
  S.labs.forEach((l, i) => l.style.opacity = E.outCubic(P(t, 2.0 + i * 0.1, 2.4 + i * 0.1)) * (1 - 0.8 * dim) * mapOut);
  S.nts.style.opacity = 0.5 * E.outCubic(P(t, 2.2, 2.6)) * (1 - dim) * mapOut;
  tf(S.mapG, { x: 0, y: (1 - mapIn) * 40 });

  // strikes (February): rings pulse on the north side
  S.rings.forEach((r, i) => {
    const q = P(t, 1.7 + i * 0.25, 2.6 + i * 0.25);
    r.setAttribute('cx', [1520, 1700, 1280][i]); r.setAttribute('cy', [330, 250, 420][i]);
    r.setAttribute('r', 10 + 90 * E.outCubic(q)); r.style.opacity = q > 0 && q < 1 ? 1 - q : 0;
  });

  // shipping: dense, then thinning to a trickle as Iran grips the strait
  const grip = E.inOutCubic(P(t, 3.1, 4.3));
  S.ships.forEach((sh, i) => {
    const u = ((t * 0.09 + i / S.ships.length) % 1);
    const p = S.ch.getPointAtLength(S.chLen * u);
    const keep = i % 7 === 0 ? 1 : 1 - grip;
    sh.setAttribute('x', p.x - 17); sh.setAttribute('y', p.y - 6 + ((i * 37) % 3 - 1) * 14);
    sh.style.opacity = Math.min(1, Math.sin(u * Math.PI) * 3) * keep * E.outCubic(P(t, 1.5, 2.2));
  });

  wordsIO(S.b2b, t, 3.4, 4.7, { stagger: 0.03 });
  wordsIO(S.b5b, t, 8.3, 9.1, { stagger: 0.025 });
  wordsIO(S.desk, t, 7.0, 7.7, { stagger: 0.02 });

  // cost
  const vCost = env(t, 4.9, 6.3, 0.5, 0.25);
  counter(S.cost, t, 4.9, 5.8, 0, 38, v => '$' + Math.round(v) + 'bn');
  tf(S.cost, { y: (1 - E.outExpo(P(t, 4.9, 5.4))) * 60, o: vCost });
  tf(S.costLab, { y: (1 - E.outExpo(P(t, 5.1, 5.6))) * 30, o: vCost });

  // vote
  const vV = env(t, 6.45, 7.7, 0.4, 0.25);
  const g1 = E.outExpo(P(t, 6.5, 7.2)), g2 = E.outExpo(P(t, 6.6, 7.3));
  S.vFor.style.width = (820 * 220 / 220) + 'px'; S.vAg.style.width = (820 * 204 / 220) + 'px';
  S.vFor.style.transform = `scaleX(${g1})`; S.vAg.style.transform = `scaleX(${g2})`;
  S.vFor.style.opacity = S.vAg.style.opacity = vV;
  S.vForL.style.opacity = vV * P(t, 6.8, 7.0); S.vAgL.style.opacity = vV * P(t, 6.9, 7.1);

  // Iran's offer: timetable tiles and the proposed route
  const vT = env(t, 9.4, 11.9, 0.4, 0.3);
  S.tiles.forEach((e, i) => {
    const a = 9.5 + i * 0.55;
    tf(e, { y: (1 - E.outExpo(P(t, a, a + 0.5))) * 50, o: E.outCubic(P(t, a, a + 0.3)) * vT });
    e.classList.toggle('hot', t > a + 0.15 && t < a + 0.8);
  });
  const rd = E.inOutCubic(P(t, 10.1, 10.9));
  S.route.style.strokeDashoffset = 0;
  S.route.style.clipPath = `inset(0 0 0 ${(1 - rd) * 100}%)`;
  S.route.style.opacity = t > 10.05 ? env(t, 10.05, 12.9, 0.2, 0.3) : 0;
  S.routeLab.style.opacity = env(t, 10.4, 11.9, 0.3, 0.3);
  endCard(t, 13.4);
}
"""

MIX = {"music_gain": 0.6, "fx_gain": 1.0, "rt": 2.4}


def score(A):
    """A low drone with a sea-like wash, in A minor. Strikes are muted pulses, not explosions."""
    import numpy as np
    m, N = A.mix, A.note
    m.add(np.vstack([A.sea(A.LEN), A.sea(A.LEN)]), 0.0, "music", gain=0.45)
    m.add(A.pad([N("A1"), N("E2")], A.LEN, cutoff=320, a=1.2, r=1.0), 0.0, "music", gain=0.7, verb=0.2)
    cues = []
    m.add(A.thud(62, 30, 1.6, 3, 0.2), 0.18, gain=0.8, verb=0.4)
    m.add(A.pad([N("A2"), N("E3"), N("C4")], A.D(0.18, 1.8), cutoff=900, a=0.05, r=1.0), 0.18, "music", gain=0.5, verb=0.4); cues.append(0.18)
    # February: muted pulses as the rings spread
    for i, t0 in enumerate([1.7, 1.95, 2.2]):
        m.add(A.filt(A.thud(55, 30, 1.2, 4, 0.05), "lowpass", 220), t0, gain=0.65, pan=0.3 + i * 0.15, verb=0.4); cues.append(t0)
    # the grip: a slow low pulse and a darker cluster
    m.add(A.pad([N("A1"), N("Bb1")], A.D(3.1, 5.0), cutoff=260, a=0.6, r=0.8), 3.1, "music", gain=0.35)
    for t0 in np.arange(3.2, 4.8, 0.7):
        m.add(A.thud(70, 40, 0.35, 10, 0.0), t0, gain=0.4); cues.append(float(t0))
    # the cost: a tick each time the counter passes a billion
    # a slowing count, like a mechanical counter settling (not one tick per billion: the counter races at first)
    for i in range(18):
        m.add(A.tick(4200, 0.01, 0.28 - i * 0.008), 4.9 + 0.9 * (i / 17) ** 1.8, pan=-0.4)
    m.add(A.blip(N("A3"), 0.6, 1.0), 5.8, gain=0.3, verb=0.4); cues += [4.9, 5.8]
    # the vote
    m.add(A.piano(N("E3"), 1.5), 6.5, "music", gain=0.9, verb=0.4)
    m.add(A.piano(N("D3"), 1.5), 6.6, "music", gain=0.8, verb=0.4); cues += [6.5, 6.6]
    # Trump at the UN
    m.add(A.pad([N("A2"), N("C3"), N("E3")], A.D(7.85, 9.25), cutoff=700, a=0.04, r=0.9), 7.85, "music", gain=0.6, verb=0.4)
    m.add(A.thud(80, 42, 0.9, 5, 0.1), 7.85, gain=0.5); cues.append(7.85)
    # Iran's offer: a chime for each stage, and the route drawn in
    m.add(A.pad([N("F2"), N("C3"), N("A3")], A.D(9.2, 12.2), cutoff=1000, a=0.4, r=1.0), 9.2, "music", gain=0.45, verb=0.4)
    for t0, n in [(9.5, "E5"), (10.05, "G5"), (10.6, "A5")]:
        m.add(A.chime(N(n)), t0, gain=0.5, pan=-0.3, verb=0.5); cues.append(t0)
    m.add(A.sweep_noise(0.8, 1200, 7000), 10.1, gain=0.14, pan=0.5, verb=0.3)
    # waiting: an unresolved chord and a slow clock
    m.add(A.pad([N("D3"), N("E3"), N("A3")], A.D(12.0, 15.0) + 0.3, cutoff=900, a=0.5, r=1.2), 12.0, "music", gain=0.5, verb=0.4)
    for t0 in [12.0, 12.6, 13.2]:
        m.add(A.tick(2600, 0.03, 0.28), t0, pan=0.2, verb=0.2); cues.append(t0)
    m.add(A.piano(N("A4"), 2.4, 0.6), 12.0, "music", gain=0.8, verb=0.5)
    # end card
    m.add(A.sweep_noise(0.5, 6000, 800), 13.35, gain=0.12, verb=0.3)
    m.add(A.piano(N("A2"), 2.0, 0.8), 13.45, "music", gain=0.9, verb=0.5)
    m.add(A.piano(N("E3"), 2.0, 0.6), 13.47, "music", gain=0.7, verb=0.5); cues.append(13.4)
    return cues

# ---- 30-second cut with narration (see motion-kit/timing.py)
LENGTH = 30
VOICE = "bf_emma"
SEGMENTS = [(0, 1.5, 1.2), (1.5, 3.0, 1.2, 1.8), (3.0, 4.8, 1.3, 2.5), (4.8, 6.4, 1.0, 2.2), (6.4, 7.8, 1.1, 2.6),
            (7.8, 9.2, 1.1, 3.0), (9.2, 12.0, 1.9, 5.0), (12.0, 13.4, 0.9, 2.6), (13.4, 15, 1.2)]
SCRIPT_SEG = [0, 1, 2, 3, 5, 6, 7, 8]
NARRATION = [
    (2, "n1", C("Iran has kept a stranglehold on energy shipping through the strait of Hormuz.", "un",
                "Iran has maintained a stranglehold over energy shipping through the strait of Hormuz since early in the war")),
    (5, "n3", C("Trump called for Iran’s complete economic isolation.", "un",
                "“I call on all nations to help to enforce the complete economic isolation of Iran,”")),
    (6, "n5", C("Iran says it has offered to reopen the strait, if the US meets its conditions.", "offer",
                ["Iran said it has told Donald Trump it is willing to open the strait of Hormuz in six days",
                 "so long as the US lifts sanctions on Iran’s oil exports in return, ends the war on all fronts – including in Lebanon – and releases some of Iran’s frozen assets"])),
]
