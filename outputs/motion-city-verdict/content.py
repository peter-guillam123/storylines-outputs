"""Storylines motion: Manchester City found guilty of financial fair play breaches (15 seconds).

Every piece of on-screen text is a C(text, source, support) claim. The
animation reads its words from T[key], so the screen and the manifest match.
Build:  python3 outputs/motion-kit/motion.py outputs/motion-city-verdict
Render: python3 outputs/motion-kit/render.py outputs/motion-city-verdict
Score:  python3 outputs/motion-kit/audio.py outputs/motion-city-verdict
"""
from build import C

DATA_FILE = "manchester-city.json"
STORYLINE_INDEX = 0
SLUG = "city-verdict"
PAGE_TITLE = "Manchester City found guilty of financial fair play breaches: a Storylines video"
KICKER = "Manchester City"
DURATION = 15
SOUND = ("A low, serious score in a minor key. Soft typewriter-like ticks mark the years of the investigation, a "
         "single heavy note lands with the verdict, muted plucks count the trophies, and the reactions sit over "
         "sparse piano. No speech.")

SRC = {
    "main": "football/2026/sep/25/manchester-city-found-guilty-of-breaking-premier-leagues-financial-fair-play-rules",
    "explain": "football/2024/sep/15/everything-you-need-to-know-about-manchester-citys-hearing-and-charges",
    "chair": "football/2026/sep/26/enzo-maresca-noel-gallagher-manchester-city-guilty-verdict",
    "pulis": "football/2026/sep/27/tony-pulis-says-he-and-stoke-were-cheated-in-2011-fa-cup-final-after-manchester-city-verdict",
    "mancini": "football/2026/sep/28/roberto-mancini-double-contract-manchester-city",
}

THEME = """
--paper:#f4f1ea;--ink:#141821;--muted:#5d6068;--rule:#dcd7cc;--card:#ebe6db;
--accent:#b8871f;--accent-strong:#8a620f;--accent-ink:#141821;--chip:#141821;--chip-ink:#f4f1ea;--focus:#2f62d0;
--hero-bg:#0d1017;--hero-bg-solid:#0f121a;--hero-ink:#f3efe6;--accent-on-hero:#e3b04b;
--hero-glow:radial-gradient(55% 70% at 88% 5%,rgba(227,176,75,.35),transparent 60%),radial-gradient(55% 70% at 0% 110%,rgba(90,120,160,.3),transparent 60%);
"""
THEME_DARK = """
--paper:#10131a;--ink:#ece8df;--muted:#a3a6ad;--rule:#272b34;--card:#1a1e27;
--accent:#e3b04b;--accent-strong:#ecc36f;--accent-ink:#10131a;--chip:#ece8df;--chip-ink:#10131a;--focus:#8fb0ff;
"""

DEK = [C("Fifteen seconds on how a process a decade in the making reached a guilty verdict, and what the club, "
         "its former manager and a beaten FA Cup finalist said next.",
         note="Summary of the video. Each element is sourced in the script below.")]


def D(label, note):
    return C(label, note=note)


SCRIPT = [
    {"time": "0:00", "label": "Title", "items": [
        ("kicker", D("Guardian reporting, 25–28 September 2026", "Span of publication dates of the Storyline’s key stories.")),
    ]},
    {"time": "0:01", "label": "How it got here", "items": [
        ("hh", D("How it got here", "Heading for the background beat.")),
        ("hb", C("A process a decade in the making", "main",
                 "The extent of the charge sheet reflected a process that had been a decade in the making.")),
        ("y1", C("2015", "main", "hacked and made public in 2015")),
        ("h1", C("Football Leaks: millions of private documents made public", "main",
                 "The Football Leaks affair, in which millions of private documents relating to football clubs and players were hacked and made public in 2015, led to reporting on City’s affairs")),
        ("y2", C("Dec 2018", "main", "In December 2018 the Premier League began its own investigation into City.")),
        ("h2", C("The Premier League opens its investigation", "main",
                 "In December 2018 the Premier League began its own investigation into City.")),
        ("y3", C("Feb 2023", "explain", "In February 2023 the Premier League charged the club with more than 100 rule breaches")),
        ("h3", C("City are charged with more than 100 rule breaches", "explain",
                 "In February 2023 the Premier League charged the club with more than 100 rule breaches")),
        ("y4", C("Sept 2024", "explain", "with the process starting in September 2024")),
        ("h4", C("Hearings begin before an independent commission", "explain",
                 "The counts have been heard by a three-person independent commission, with the process starting in September 2024.",
                 note="This explainer was first published on 15 September 2024 and updated on 25 September 2026.")),
    ]},
    {"time": "0:03", "label": "Friday 25 September", "items": [
        ("d1", D("Fri 25 Sept", "Date: the article was published on Friday 25 September 2026 and says neither party would confirm the outcome “on Friday”.")),
        ("b1", C("News breaks: City are found guilty of the vast majority of more than 100 charges", "main",
                 "Manchester City have been found guilty of the vast majority of more than a hundred charges related to breaches of the Premier League’s financial rules",
                 note="“More than a hundred” is shown as “more than 100”.")),
        ("b1b", C("They face possible relegation, or expulsion from the Premier League", "main",
                  "The serial champions now face the possibility of being relegated from the Premier League, or expelled from the competition altogether")),
        ("b1c", C("City deny wrongdoing and are expected to appeal", "pulis", "City are expected to appeal and they deny any wrongdoing.")),
        ("boxes", C("More than 100 charges", "explain", "charged the club with more than 100 rule breaches",
                    note="Drawn as a grid of 100 boxes with a plus sign: the articles give different exact totals (see Checks).")),
    ]},
    {"time": "0:05", "label": "What City won in those seasons", "items": [
        ("b2", C("In the seasons the charges cover, City won", "main",
                 "From season 2009-10 to 2022-23 inclusive City won seven Premier League titles, a Champions League, three FA Cups and six League Cups.")),
        ("seasons", C("2009-10 to 2022-23", "main", "From season 2009-10 to 2022-23 inclusive")),
        ("t1", C("7 Premier League titles", "main", "City won seven Premier League titles", note="“Seven” written as 7.")),
        ("t2", C("6 League Cups", "main", "six League Cups", note="“Six” written as 6.")),
        ("t3", C("3 FA Cups", "main", "three FA Cups", note="“Three” written as 3.")),
        ("t4", C("1 Champions League", "main", "a Champions League", note="“A Champions League” written as “1”.")),
    ]},
    {"time": "0:07", "label": "City’s response", "items": [
        ("q2", C("“The Premier League process remains ongoing”", "main",
                 "A City spokesperson said: “The Premier League process remains ongoing, with significant elements to be completed, and subject to strict confidentiality.")),
        ("a2", C("A Manchester City spokesperson", "main", "A City spokesperson said")),
        ("b3", C("City deny wrongdoing and are expected to appeal", "pulis", "City are expected to appeal and they deny any wrongdoing.")),
    ]},
    {"time": "0:08", "label": "Saturday 26 September", "items": [
        ("d2", D("Sat 26 Sept", "Date: the article says al-Mubarak spoke “on Saturday afternoon”; published Saturday 26 September 2026.")),
        ("q3", C("“Nothing has changed”", "chair", "“While some people have been quick to reach their own conclusions, and there is so much noise swirling around us, nothing has changed.",
                 note="Capital N at the start of a quote used alone.")),
        ("a3", C("Khaldoon al-Mubarak, City chair", "chair", "Khaldoon al-Mubarak, the Manchester City chair")),
    ]},
    {"time": "0:10", "label": "Reported 27 September", "items": [
        ("d3", D("Reported 27 Sept", "Publication date of the article. It quotes Pulis’s BBC Sport column without dating it.")),
        ("b4", C("Tony Pulis says his Stoke side were “cheated” in the 2011 FA Cup final", "pulis",
                 ["Tony Pulis says he and Stoke were ‘cheated’ in 2011 FA Cup final",
                  "Tony Pulis has said his Stoke City team were “cheated” out of the 2011 FA Cup"])),
        ("b4b", C("City won that final 1–0", "pulis", "Pulis’s Stoke lost the 2011 Cup final 1-0 after Yaya Touré’s goal.")),
    ]},
    {"time": "0:11", "label": "Reported 28 September", "items": [
        ("d4", D("Reported 28 Sept", "Publication date of the article. It does not date Mancini’s news conference.")),
        ("ctx", C("The charges include alleged failures to give accurate details of player and manager payments", "mancini",
                  "Among the raft of charges that City faced is an alleged failure to provide accurate details for player and manager payments")),
        ("q5", C("“Manchester City is not guilty and the fact of having a double contract isn’t my problem but theirs, probably”", "mancini",
                 "Manchester City is not guilty and the fact of having a double contract isn’t my problem but theirs, probably.”")),
        ("a5", C("Roberto Mancini, former City manager", "mancini", "when he managed Manchester City")),
    ]},
    {"time": "0:13", "label": "End card", "items": [
        ("ec", D("Drawn from Guardian journalism", "End card heading.")),
    ]},
]

CHECKS = [
    "**How many charges.** The articles differ: 134 (the verdict article), 115 (the chair article), and \"more than 100\" "
    "(the explainer and several others). The video uses \"more than 100\", which all of them support. The grid of 100 "
    "boxes with a plus sign illustrates that figure; it is not a count.",
    "**How the verdict became known.** The verdict article says neither party would publicly confirm the outcome on "
    "Friday and that City were expected to appeal; the prime minister, Andy Burnham, said \"these are reports at this "
    "stage\". The Guardian nonetheless reports the verdict as fact in its own voice, and the video follows it, alongside "
    "City's denial and expected appeal.",
    "**Trophies.** The seven titles, six League Cups, three FA Cups and one Champions League are from the verdict "
    "article, for seasons 2009-10 to 2022-23 inclusive. The video does not suggest any trophy will be taken away.",
    "**Mancini.** The charge context line is from the Mancini article (\"an alleged failure to provide accurate details "
    "for player and manager payments\"). His quote is given in full, including \"Manchester City is not guilty\".",
    "**Friday 25 September.** The verdict article says club executives learned the outcome after a shareholders' "
    "meeting on the Thursday; the news broke on the Friday. The screen says \"News breaks\" under that date. City's "
    "denial and expected appeal are shown with the verdict and again in their own beat.",
    "**The explainer's date.** \"Everything you need to know…\" was first published on 15 September 2024 and updated "
    "on 25 September 2026, the date the end card gives.",
    "**Dates.** \"Reported\" marks publication dates where the article does not date the remark.",
    "**Left out.** Rui Pinto's reaction, the opinion pieces (Barney Ronay, Simon Hattenstone), the Uefa history and "
    "Noel Gallagher's and others' reactions. All are credited on the end card.",
    "**Images.** None. Type, colour and drawn shapes only. **Sound:** music and effects synthesised in code; no samples, "
    "no licensed music, no speech.",
]

ANIM_CSS = """
#stage{background:#0c0f16;color:#f3efe6}
.bg{position:absolute;inset:-10%;background:radial-gradient(45% 55% at 85% 8%,rgba(227,176,75,.26),transparent 70%),
  radial-gradient(55% 60% at 5% 100%,rgba(90,120,160,.25),transparent 70%)}
.ledger{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(243,239,230,.045) 0 2px,transparent 2px 54px)}
.margin{position:absolute;left:92px;top:0;bottom:0;width:2px;background:rgba(227,176,75,.35);transform-origin:top}
.grain{position:absolute;inset:0;opacity:.14;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.title{position:absolute;left:120px;top:230px;width:1700px}
.title .kick{font:800 30px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:#e3b04b;margin-bottom:34px}
.title .tl{font:800 138px/.98 var(--sans);letter-spacing:-.04em}
.hd{position:absolute;left:120px;top:70px;font:700 26px/1 var(--sans);opacity:.8}
.date{position:absolute;left:120px;top:190px;font:800 40px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#e3b04b}
.big{position:absolute;left:120px;top:280px;width:900px;font:800 86px/1.03 var(--sans);letter-spacing:-.03em}
.sub{position:absolute;left:120px;width:880px;font:600 40px/1.2 var(--sans);opacity:.9}
.hist{position:absolute;left:1060px;width:760px;display:grid;grid-template-columns:190px 1fr;gap:24px;align-items:baseline;
  border-top:2px solid rgba(227,176,75,.5);padding-top:18px}
.hist .y{font:900 44px/1 var(--sans);color:#e3b04b;letter-spacing:-.02em}
.hist .tx{font:600 36px/1.2 var(--sans)}
.boxes{position:absolute;left:1100px;top:280px;width:500px;display:grid;grid-template-columns:repeat(10,1fr);gap:10px}
.boxes i{display:block;aspect-ratio:1;border:3px solid rgba(243,239,230,.7);border-radius:4px}
.plus{position:absolute;left:1630px;top:470px;font:900 120px/1 var(--sans);color:#e3b04b}
.boxlab{position:absolute;left:1100px;top:830px;font:800 24px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;opacity:.8}
.troph{position:absolute;left:1060px;top:300px;width:780px}
.troph .row{display:grid;grid-template-columns:360px 1fr;align-items:center;gap:20px;margin-bottom:34px}
.troph .lab{font:700 34px/1.15 var(--sans)}
.troph .dots{display:flex;gap:14px}
.troph .dots i{width:44px;height:44px;border-radius:50%;background:#e3b04b;box-shadow:inset 0 -6px 0 rgba(0,0,0,.18)}
.troph .row:nth-child(2) .dots i{background:#c9ced6}
.troph .row:nth-child(3) .dots i{background:transparent;border:5px solid #e3b04b}
.troph .row:nth-child(4) .dots i{background:#f3efe6}
.seasons{position:absolute;left:120px;top:610px;font:800 44px/1 var(--sans);color:#e3b04b;letter-spacing:.02em}
.q{position:absolute;left:120px;top:300px;width:1600px;font:italic 500 92px/1.1 var(--serif)}
.q.long{font-size:66px;line-height:1.16;top:400px;width:1640px}
.qa{position:absolute;left:124px;font:700 30px/1.3 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#e3b04b}
.ctx{position:absolute;left:120px;top:280px;width:1500px;font:600 42px/1.2 var(--sans);opacity:.85}
:root{--ec-bg:#f3efe6;--ec-ink:#141821;--ec-accent:#8a620f;--ec-rule:#dcd7cc}
"""

JS = r"""
const POSTER_T = 6.9;
let S = {};
function setup() {
  S.bg = mk('div', 'bg'); mk('div', 'ledger'); S.margin = mk('div', 'margin'); mk('div', 'grain');
  S.title = mk('div', 'title');
  S.kick = words(S.title, T.kicker, 'kick');
  S.tl = [words(S.title, 'Manchester City found', 'tl'), words(S.title, 'guilty of financial', 'tl'), words(S.title, 'fair play breaches', 'tl')];
  S.hd = mk('div', 'hd', null, T.title);
  S.rail = rail(['2015', '2018', '2023', '2024', '25 Sept', '26', '27', '28'], { color: '#f3efe6', accent: '#e3b04b' });
  S.hh = words(STAGE, T.hh, 'date');
  S.hb = words(STAGE, T.hb, 'big'); S.hb.line.style.width = '860px';
  S.hist = [1, 2, 3, 4].map(i => {
    const r = mk('div', 'hist'); r.style.top = (250 + (i - 1) * 170) + 'px';
    mk('div', 'y', r, T['y' + i]); mk('div', 'tx', r, T['h' + i]); return r; });
  S.dates = ['d1', 'd2', 'd3', 'd4'].map(k => words(STAGE, T[k], 'date'));
  S.b1 = words(STAGE, T.b1, 'big'); S.b1.line.style.fontSize = '76px';
  S.b1b = words(STAGE, T.b1b, 'sub'); S.b1b.line.style.top = '690px';
  S.b1c = words(STAGE, T.b1c, 'sub'); S.b1c.line.style.top = '850px'; S.b1c.line.style.width = '1000px'; S.b1c.line.style.color = '#e3b04b';
  const bx = mk('div', 'boxes'); S.boxes = Array.from({ length: 100 }, () => mk('i', '', bx));
  S.plus = mk('div', 'plus', null, '+'); S.boxlab = mk('div', 'boxlab', null, T.boxes);
  S.b2 = words(STAGE, T.b2, 'big');
  S.seasons = mk('div', 'seasons', null, T.seasons);
  const tr = mk('div', 'troph'); S.troph = tr;
  S.tr = [['t1', 7], ['t2', 6], ['t3', 3], ['t4', 1]].map(([k, n]) => {
    const r = mk('div', 'row', tr); mk('div', 'lab', r, T[k]); const d = mk('div', 'dots', r);
    return Array.from({ length: n }, () => mk('i', '', d)); });
  S.q2 = words(STAGE, T.q2, 'q'); S.a2 = words(STAGE, T.a2, 'qa'); S.a2.line.style.top = '560px';
  S.b3 = words(STAGE, T.b3, 'sub'); S.b3.line.style.top = '650px';
  S.q3 = words(STAGE, T.q3, 'q'); S.q3.line.style.fontSize = '150px'; S.a3 = words(STAGE, T.a3, 'qa'); S.a3.line.style.top = '520px';
  S.b4 = words(STAGE, T.b4, 'big'); S.b4.line.style.width = '1500px';
  S.b4b = words(STAGE, T.b4b, 'sub'); S.b4b.line.style.top = '620px';
  S.ctx = words(STAGE, T.ctx, 'ctx');
  S.q5 = words(STAGE, T.q5, 'q long'); S.a5 = words(STAGE, T.a5, 'qa'); S.a5.line.style.top = '800px';
}

function frame(t) {
  tf(S.bg, { x: Math.sin(t * 0.3) * 30, y: Math.cos(t * 0.22) * 24 });
  S.margin.style.transform = `scaleY(${E.outCubic(P(t, 0, 1.2))})`;
  wordsIO(S.kick, t, 0.1, 1.05, { stagger: 0.02 });
  S.tl.forEach((w, i) => wordsIO(w, t, 0.15 + i * 0.12, 1.1 + i * 0.03, { stagger: 0.05, dur: 0.6, ease: E.outCubic }));
  S.title.style.visibility = t < 1.55 ? 'visible' : 'hidden';
  S.hd.style.opacity = E.outCubic(P(t, 1.4, 1.8)) * (1 - P(t, 13.3, 13.6));
  S.rail.pose(t, [[0, 0], [1.5, 0], [2.15, 1], [2.75, 2], [3.35, 3], [3.95, 4], [8.9, 5], [10.0, 6], [11.2, 7]],
    E.outCubic(P(t, 1.4, 1.8)) * (1 - E.inCubic(P(t, 12.9, 13.3))));
  const o = { stagger: 0.03, ease: E.outCubic, dur: 0.5 };

  // how it got here: four entries stack up
  wordsIO(S.hh, t, 1.5, 3.85, o);
  wordsIO(S.hb, t, 1.6, 3.85, o);
  S.hist.forEach((r, i) => {
    const a = 1.55 + i * 0.6;
    const q = E.outCubic(P(t, a, a + 0.35));
    tf(r, { x: (1 - q) * 60, o: q * (1 - E.inCubic(P(t, 3.8, 4.05))) });
  });

  // the verdict
  const bt = [[3.95, 8.85], [8.9, 9.95], [10.0, 11.15], [11.2, 12.9]];
  S.dates.forEach((w, i) => wordsIO(w, t, bt[i][0], bt[i][1], o));
  wordsIO(S.b1, t, 4.0, 5.85, o);
  wordsIO(S.b1b, t, 4.5, 5.85, { ...o, stagger: 0.02 });
  wordsIO(S.b1c, t, 4.85, 5.85, { ...o, stagger: 0.02 });
  const vB = env(t, 4.1, 5.85, 0.3, 0.3, E.outCubic);
  S.boxes.forEach((b, i) => {
    const r = Math.floor(i / 10), c = i % 10;
    const q = E.outCubic(P(t, 4.1 + (r + c) * 0.03, 4.35 + (r + c) * 0.03));
    b.style.transform = `scale(${q})`; b.style.opacity = vB;
  });
  S.plus.style.opacity = E.outCubic(P(t, 4.8, 5.0)) * vB; S.boxlab.style.opacity = E.outCubic(P(t, 4.8, 5.0)) * vB;

  // the trophies of those seasons
  wordsIO(S.b2, t, 5.95, 7.4, o);
  tf(S.seasons, { o: env(t, 6.2, 7.4, 0.3, 0.3, E.outCubic) });
  const vT = env(t, 6.0, 7.4, 0.3, 0.3, E.outCubic);
  S.troph.style.opacity = vT;
  let k = 0;
  S.tr.forEach(row => row.forEach(d => {
    const a = 6.1 + k++ * 0.045;
    d.style.transform = `scale(${E.outBack(P(t, a, a + 0.3))})`;
  }));

  // City's response, then the reactions
  wordsIO(S.q2, t, 7.5, 8.85, { ...o, stagger: 0.04 });
  wordsIO(S.a2, t, 7.8, 8.85, { ...o, stagger: 0.02 });
  wordsIO(S.b3, t, 7.7, 8.85, { ...o, stagger: 0.02 });
  wordsIO(S.q3, t, 9.0, 9.95, { ...o, dur: 0.45 });
  wordsIO(S.a3, t, 9.2, 9.95, { ...o, stagger: 0.02 });
  wordsIO(S.b4, t, 10.05, 11.15, { ...o, stagger: 0.025 });
  wordsIO(S.b4b, t, 10.45, 11.15, { ...o, stagger: 0.02 });
  wordsIO(S.ctx, t, 11.25, 12.9, { ...o, stagger: 0.02 });
  wordsIO(S.q5, t, 11.45, 12.9, { ...o, stagger: 0.022, dur: 0.4 });
  wordsIO(S.a5, t, 11.9, 12.9, { ...o, stagger: 0.02 });
  endCard(t, 13.4);
}
"""

MIX = {"music_gain": 0.6, "fx_gain": 1.0, "rt": 2.2}


def score(A):
    """Low, serious and measured, in C minor."""
    m, N = A.mix, A.note
    cues = []
    chords = [(0.0, ["C3", "G3", "Eb4"]), (1.5, ["Ab2", "Eb3", "C4"]), (3.95, ["C2", "G2", "Eb3"]),
              (5.95, ["Ab2", "C3", "Eb3"]), (7.5, ["F2", "C3", "Ab3"]), (8.9, ["G2", "D3", "Bb3"]),
              (10.0, ["Eb2", "Bb2", "G3"]), (11.2, ["F2", "Ab2", "C3"]), (13.4, ["C3", "G3", "D4"])]
    for i, (t0, ns) in enumerate(chords):
        t1 = chords[i + 1][0] if i + 1 < len(chords) else 15.0
        m.add(A.pad([N(n) for n in ns], t1 - t0 + 1.0, cutoff=700, a=0.5, r=1.0), t0, "music", gain=0.6, verb=0.35)
    m.add(A.thud(64, 32, 1.4, 4, 0.2), 0.18, gain=0.8, verb=0.4); cues.append(0.18)
    # the years of the investigation: a dry tick and low note for each entry
    for i, t0 in enumerate([1.55, 2.15, 2.75, 3.35]):
        m.add(A.tick(3500, 0.018, 0.5), t0, pan=0.4, verb=0.15)
        m.add(A.piano(N(["C3", "Eb3", "G3", "Bb3"][i]), 1.2, 0.6), t0, "music", gain=0.8, verb=0.4); cues.append(t0)
    # the verdict: one heavy note, then the grid of charges ticks in
    m.add(A.thud(55, 28, 2.0, 2.5, 0.35), 4.0, gain=1.0, verb=0.5)
    m.add(A.piano(N("C2"), 3.0, 1.0), 4.0, "music", gain=1.0, verb=0.5); cues.append(4.0)
    for j in range(19):
        m.add(A.tick(5000, 0.008, 0.12), 4.1 + j * 0.03, pan=0.5)
    # the trophies: muted plucks, not a fanfare
    for j in range(17):
        m.add(A.blip(N(["C5", "Eb5", "G5", "Bb4"][j % 4]), 0.18, 1.0), 6.1 + j * 0.045, gain=0.13, pan=0.45, verb=0.3)
    cues.append(6.1)
    # the responses and reactions over sparse piano
    for t0, n in [(7.5, "Ab3"), (8.9, "G3"), (10.0, "Eb3"), (11.2, "F3"), (11.9, "Ab3")]:
        m.add(A.piano(N(n), 2.0, 0.7), t0, "music", gain=0.9, verb=0.5); cues.append(t0)
    m.add(A.sweep_noise(0.5, 6000, 800), 13.35, gain=0.1, verb=0.3)
    m.add(A.piano(N("C3"), 2.0, 0.8), 13.45, "music", gain=0.9, verb=0.5); cues.append(13.4)
    return cues
