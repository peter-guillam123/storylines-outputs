"""Storylines motion: Pep Guardiola's departure from Manchester City (15 seconds).

Every piece of on-screen text is a C(text, source, support) claim. The
animation reads its words from T[key], so the screen and the manifest match.
Build:  python3 outputs/motion-kit/motion.py outputs/motion-city-guardiola
Render: python3 outputs/motion-kit/render.py outputs/motion-city-guardiola
Score:  python3 outputs/motion-kit/audio.py outputs/motion-city-guardiola
"""
from build import C

DATA_FILE = "manchester-city.json"
STORYLINE_INDEX = 1
SLUG = "city-guardiola"
PAGE_TITLE = "Pep Guardiola's departure from Manchester City: a Storylines video"
KICKER = "Manchester City"
DURATION = 15
SOUND = ("A warm, slow score in a major key: soft piano over held strings-like chords. A gentle bell for each "
         "group of trophies, a quiet shift to a minor chord as the news breaks, and a long, open chord under "
         "“Nothing is eternal”. No speech.")

SRC = {
    "exp": "football/2026/may/18/pep-guardiola-departure-manchester-city-end-of-premier-league-season",
    "tells": "football/2026/may/19/pep-guardiola-tells-manchester-city-players-leaving-enzo-maresca-chelsea-compensation",
    "refuses": "football/2026/may/19/pep-guardiola-exit-manchester-city-arsenal-bournemouth",
    "confirm": "football/2026/may/22/pep-guardiola-confirms-leaving-manchester-city",
    "england": "football/2026/may/23/pep-guardiola-managing-england-manchester-city",
}

THEME = """
--paper:#f6efe8;--ink:#1d1520;--muted:#62575f;--rule:#e2d6cc;--card:#efe4da;
--accent:#d9793f;--accent-strong:#a8521f;--accent-ink:#1d1520;--chip:#1d1520;--chip-ink:#f6efe8;--focus:#3a64d0;
--hero-bg:#1a1220;--hero-bg-solid:#1c1422;--hero-ink:#f6ede4;--accent-on-hero:#f4b860;
--hero-glow:radial-gradient(60% 70% at 80% 100%,rgba(242,143,107,.45),transparent 60%),radial-gradient(50% 60% at 10% 0%,rgba(150,110,200,.25),transparent 60%);
"""
THEME_DARK = """
--paper:#140f16;--ink:#efe6de;--muted:#aa9fa6;--rule:#2e2530;--card:#1f1822;
--accent:#f4b860;--accent-strong:#f6c983;--accent-ink:#140f16;--chip:#efe6de;--chip-ink:#140f16;--focus:#8fb0ff;
"""

DEK = [C("Fifteen seconds on the end of Pep Guardiola’s decade at Manchester City: the trophies, the week the news "
         "broke, and his own words on leaving.",
         note="Summary of the video. Each element is sourced in the script below.")]


def D(label, note):
    return C(label, note=note)


SCRIPT = [
    {"time": "0:00", "label": "Title", "items": [
        ("kicker", D("Guardian reporting, 18–23 May 2026", "Span of publication dates of the Storyline’s key stories.")),
    ]},
    {"time": "0:01", "label": "1 July 2016", "items": [
        ("d1", C("1 July 2016", "exp", "Guardiola started at City on 1 July 2016")),
        ("b1", C("Guardiola starts at City, joining from Bayern Munich", "exp",
                 "Guardiola started at City on 1 July 2016, joining from Bayern Munich.")),
    ]},
    {"time": "0:03", "label": "The decade", "items": [
        ("d2", D("The decade", "Label.")),
        ("b2", C("17 major trophies in 10 years", "confirm",
                 "following a decade of glittering success in which he won 17 major trophies",
                 note="“A decade” shown as 10 years; the 18 May article also says “10 trophy-filled years”.")),
        ("t1", C("6 Premier League titles", "exp", "As manager Guardiola has won six Premier Leagues and a Champions League with City.", note="“Six” written as 6.")),
        ("t2", C("5 League Cups", "exp", "his fifth League Cup in March", note="“Fifth” League Cup: 5 in total.")),
        ("t3", C("3 FA Cups", "exp", "Guardiola won his third FA Cup with City on Saturday", note="“Third” FA Cup: 3 in total.")),
        ("t4", C("1 Champions League", "exp", "six Premier Leagues and a Champions League with City", note="“A Champions League” written as 1.")),
        ("t5", C("1 Club World Cup", "exp", "He has also won the Fifa Club World Cup, Uefa Super Cup and three Community Shields.", note="Written as 1.")),
        ("t6", C("1 Uefa Super Cup", "exp", "He has also won the Fifa Club World Cup, Uefa Super Cup and three Community Shields.", note="Written as 1.")),
        ("b2b", C("His first title, in 2017-18, came with a record 100 points", "confirm",
                  "The first of City’s six league titles under him, in 2017-18, came with a 100-point tally, another record")),
    ]},
    {"time": "0:05", "label": "Monday 18 May", "items": [
        ("d3", D("Mon 18 May", "Date: the article, published on 18 May 2026, refers to “reports on Monday night”.")),
        ("b3", C("News breaks that he is expected to leave", "exp",
                 ["Pep Guardiola is expected to leave Manchester City after 10 trophy-filled years as manager.",
                  "The club did not confirm reports on Monday night"])),
        ("b3b", C("The club does not confirm it", "exp", "The club did not confirm reports on Monday night")),
    ]},
    {"time": "0:07", "label": "Tuesday 19 May", "items": [
        ("d4", D("Tue 19 May", "Date: the article reporting that he told the players was published on the morning of 19 May 2026; the Bournemouth draw was that evening (the match report is dated 19 May).")),
        ("b4", C("Reports say he has told his players he is leaving", "refuses",
                 "despite reports that he has already informed his players")),
        ("b4c", C("In public, he refuses to confirm it", "refuses",
                  "Pep Guardiola refused to publicly comment on the expectation that his 10-year reign at Manchester City will come to an end")),
        ("b4b", C("That night, a draw at Bournemouth means Arsenal are champions", "refuses",
                  "A 1-1 draw at Bournemouth meant City could not prevent Arsenal becoming Premier League champions.")),
    ]},
    {"time": "0:08", "label": "Friday 22 May", "items": [
        ("d5", D("Fri 22 May", "Date: the article, published on Friday 22 May 2026, says the departure “was confirmed on Friday”.")),
        ("b5", C("City confirm he is leaving", "confirm", "his departure from Manchester City was confirmed on Friday")),
        ("stand", C("The Pep Guardiola Stand", "confirm", "The Pep Guardiola Stand will open on Sunday for Aston Villa’s visit in the season’s final game.")),
        ("b5b", C("Enzo Maresca is expected to replace him", "confirm",
                  "With the former Chelsea head coach Enzo Maresca expected to replace him")),
    ]},
    {"time": "0:10", "label": "Friday 22 May, in the club video", "items": [
        ("q7", C("“Nothing is eternal.”", "confirm", "Nothing is eternal.”")),
        ("a7", C("Pep Guardiola, in the club video confirming his departure, 22 May", "confirm",
                 "In a club video confirming his departure earlier in the day, he said",
                 note="Date: the 22 May article says the club video was released “earlier in the day”.")),
    ]},
    {"time": "0:11", "label": "Reported 23 May", "items": [
        ("d6", D("Reported 23 May", "Publication date of the article; it does not date the remarks.")),
        ("b6", C("He won’t rule out managing England", "england",
                 "Pep Guardiola has left open the possibility of managing England in the future")),
        ("q6", C("“I don’t have any absolute plan about my future”", "england",
                 "“I don’t have any absolute plan about my future,” he said.")),
    ]},
    {"time": "0:12", "label": "Sunday 24 May", "items": [
        ("d7", D("Sun 24 May", "Date derived: the 23 May article (a Saturday) says his final match is “Sunday’s visit of Aston Villa”.")),
        ("last", C("His last game: at home to Aston Villa", "england",
                   "Guardiola’s final match of a supremely successful decade leading City is Sunday’s visit of Aston Villa on the last day of the season.")),
    ]},
    {"time": "0:13", "label": "End card", "items": [
        ("ec", D("Drawn from Guardian journalism", "End card heading.")),
    ]},
]

CHECKS = [
    "**Trophies.** The six groups come from the 18 May article (six Premier Leagues, a Champions League, his third FA "
    "Cup, his fifth League Cup, the Club World Cup and the Uefa Super Cup) and add up to 17, the figure the 22 May "
    "article gives for major trophies. The 22 May article also gives 20 in total, counting three Community Shields; "
    "the video uses the 17 major trophies.",
    "**19 May.** A morning article reported that he had told the players; that evening's report says he \"refused to "
    "publicly comment\" \"despite reports that he has already informed his players\". The video says \"Reports say\" "
    "and shows his public refusal. City confirmed his departure on 22 May.",
    "**Order of the quotes.** \"Nothing is eternal\" is from the club video of 22 May and is shown in that beat, before "
    "the 23 May England remarks.",
    "**His last game.** The Storyline's articles were all published before the match, so the video gives the fixture "
    "but no result.",
    "**The sun.** The setting sun behind the video is decoration, not a claim.",
    "**Left out.** The Chelsea compensation dispute over Maresca, Barney Ronay's opinion piece, and the explainers "
    "by Jonathan Wilson and Jamie Jackson. All are credited on the end card.",
    "**Images.** None. Type, colour and drawn shapes only. **Sound:** music and effects synthesised in code; no samples, "
    "no licensed music, no speech.",
]

ANIM_CSS = """
#stage{background:linear-gradient(180deg,#140e1b 0%,#1f1424 55%,#3a1f2e 100%);color:#f6ede4}
.sun{position:absolute;left:1380px;width:420px;height:420px;border-radius:50%;
  background:radial-gradient(circle at 50% 45%,#ffd9a0 0%,#f4b860 40%,#e0784e 75%,rgba(224,120,78,0) 76%);
  box-shadow:0 0 160px 60px rgba(242,143,107,.28)}
.haze{position:absolute;left:0;right:0;bottom:0;height:420px;background:linear-gradient(180deg,rgba(58,31,46,0),rgba(40,20,32,.95) 70%)}
.grain{position:absolute;inset:0;opacity:.14;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.title{position:absolute;left:120px;top:230px;width:1500px}
.title .kick{font:800 30px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:#f4b860;margin-bottom:34px}
.title .tl{font:800 150px/.97 var(--sans);letter-spacing:-.04em}
.hd{position:absolute;left:120px;top:70px;font:700 26px/1 var(--sans);opacity:.8}
.date{position:absolute;left:120px;top:190px;font:800 40px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#f4b860}
.big{position:absolute;left:120px;top:280px;width:920px;font:800 88px/1.03 var(--sans);letter-spacing:-.03em}
.sub{position:absolute;left:120px;width:900px;font:600 42px/1.2 var(--sans);opacity:.92}
.troph{position:absolute;left:1060px;top:270px;width:800px}
.troph .row{display:grid;grid-template-columns:380px 1fr;align-items:center;gap:18px;margin-bottom:22px}
.troph .lab{font:700 32px/1.15 var(--sans)}
.troph .dots{display:flex;gap:14px}
.troph .dots i{width:40px;height:40px;border-radius:50%;background:#f4b860;box-shadow:0 0 18px rgba(244,184,96,.5)}
.standwrap{position:absolute;left:1000px;top:330px;width:820px;height:420px}
.tier{position:absolute;left:0;right:0;height:26px;border-radius:4px;background:rgba(246,237,228,.12)}
.standname{position:absolute;left:0;right:0;top:-10px;text-align:center;font:900 56px/1 var(--sans);letter-spacing:.04em;
  text-transform:uppercase;color:#f4b860}
.q{position:absolute;left:120px;top:330px;width:1500px;font:italic 500 170px/1 var(--serif)}
.qs{position:absolute;left:120px;top:560px;width:1400px;font:italic 500 56px/1.15 var(--serif)}
.qa{position:absolute;left:124px;font:700 30px/1.3 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#f4b860}
.last{position:absolute;left:120px;top:800px;font:700 34px/1.2 var(--sans);opacity:.85}
:root{--ec-bg:#f6efe8;--ec-ink:#1d1520;--ec-accent:#a8521f;--ec-rule:#e2d6cc}
"""

JS = r"""
const POSTER_T = 4.9;
let S = {};
function setup() {
  S.sun = mk('div', 'sun'); mk('div', 'haze'); mk('div', 'grain');
  S.title = mk('div', 'title');
  S.kick = words(S.title, T.kicker, 'kick');
  S.tl = [words(S.title, 'Pep Guardiola\'s', 'tl'), words(S.title, 'departure from', 'tl'), words(S.title, 'Manchester City', 'tl')];
  S.hd = mk('div', 'hd', null, T.title);
  S.rail = rail(['2016', '18 May', '19', '22', '23', '24'], { color: '#f6ede4', accent: '#f4b860' });
  S.dates = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7'].map(k => words(STAGE, T[k], 'date'));
  S.b = {};
  ['b1', 'b2', 'b3', 'b4', 'b5', 'b6'].forEach(k => S.b[k] = words(STAGE, T[k], 'big'));
  S.b2b = words(STAGE, T.b2b, 'sub'); S.b2b.line.style.top = '510px';
  S.b3b = words(STAGE, T.b3b, 'sub'); S.b3b.line.style.top = '510px';
  S.b4b = words(STAGE, T.b4b, 'sub'); S.b4b.line.style.top = '620px';
  S.b.b4.line.style.width = '1250px';
  S.b4c = words(STAGE, T.b4c, 'sub'); S.b4c.line.style.top = '510px'; S.b4c.line.style.color = '#f4b860';
  S.b5b = words(STAGE, T.b5b, 'sub'); S.b5b.line.style.top = '510px';
  S.q6 = words(STAGE, T.q6, 'qs');
  const tr = mk('div', 'troph'); S.troph = tr;
  S.tr = [['t1', 6], ['t2', 5], ['t3', 3], ['t4', 1], ['t5', 1], ['t6', 1]].map(([k, n]) => {
    const r = mk('div', 'row', tr); mk('div', 'lab', r, T[k]); const d = mk('div', 'dots', r);
    return Array.from({ length: n }, () => mk('i', '', d)); });
  const sw = mk('div', 'standwrap'); S.stand = sw;
  S.tiers = Array.from({ length: 9 }, (_, i) => { const e = mk('div', 'tier', sw); e.style.top = (110 + i * 34) + 'px';
    e.style.left = (i * 14) + 'px'; e.style.right = (i * 14) + 'px'; return e; });
  S.standname = mk('div', 'standname', sw, T.stand);
  S.q7 = words(STAGE, T.q7, 'q');
  S.a7 = words(STAGE, T.a7, 'qa'); S.a7.line.style.top = '560px';
  S.last = words(STAGE, T.last, 'big');
}

function frame(t) {
  // the sun sets slowly across the whole piece
  const sy = lerp(120, 860, E.inOutCubic(P(t, 0, 14)));
  const busy = Math.max(env(t, 3.2, 5.5, 0.3, 0.3), env(t, 8.8, 10.05, 0.3, 0.3));
  tf(S.sun, { y: sy, s: lerp(1, 1.12, P(t, 0, 14)), o: (0.9 - 0.4 * P(t, 10, 14)) * (1 - 0.75 * busy) });
  wordsIO(S.kick, t, 0.1, 1.15, { stagger: 0.02, ease: E.outCubic });
  S.tl.forEach((w, i) => wordsIO(w, t, 0.2 + i * 0.14, 1.2 + i * 0.03, { stagger: 0.06, dur: 0.7, ease: E.outCubic }));
  S.title.style.visibility = t < 1.65 ? 'visible' : 'hidden';
  S.hd.style.opacity = E.outCubic(P(t, 1.5, 1.9)) * (1 - P(t, 13.3, 13.6));
  S.rail.pose(t, [[0, 0], [1.6, 0], [3.2, 0.5], [5.6, 1], [7.1, 2], [8.8, 3], [11.3, 4], [12.3, 5]],
    E.outCubic(P(t, 1.5, 1.9)) * (1 - E.inCubic(P(t, 13.0, 13.35))));
  const o = { stagger: 0.035, ease: E.outCubic, dur: 0.55 };
  const bt = [[1.65, 3.1], [3.2, 5.5], [5.6, 7.0], [7.1, 8.7], [8.8, 11.15], [11.3, 12.2], [12.3, 13.3]];
  S.dates.forEach((w, i) => wordsIO(w, t, bt[i][0], bt[i][1], o));
  wordsIO(S.b.b1, t, 1.7, 3.1, o);
  wordsIO(S.b.b2, t, 3.25, 5.5, o);
  wordsIO(S.b2b, t, 3.8, 5.5, { ...o, stagger: 0.02 });
  wordsIO(S.b.b3, t, 5.65, 7.0, o);
  wordsIO(S.b3b, t, 6.1, 7.0, { ...o, stagger: 0.02 });
  wordsIO(S.b.b4, t, 7.15, 8.7, o);
  wordsIO(S.b4c, t, 7.5, 8.7, { ...o, stagger: 0.02 });
  wordsIO(S.b4b, t, 7.85, 8.7, { ...o, stagger: 0.02 });
  wordsIO(S.b.b5, t, 8.85, 10.05, o);
  wordsIO(S.b5b, t, 9.4, 10.05, { ...o, stagger: 0.02 });
  wordsIO(S.q7, t, 10.15, 11.15, { ...o, stagger: 0.1, dur: 0.6 });
  wordsIO(S.a7, t, 10.4, 11.15, { ...o, stagger: 0.02 });
  wordsIO(S.b.b6, t, 11.35, 12.2, { ...o, stagger: 0.025 });
  wordsIO(S.q6, t, 11.6, 12.2, { ...o, stagger: 0.02 });
  wordsIO(S.last, t, 12.35, 13.3, { ...o, stagger: 0.03 });

  // trophies, group by group
  const vT = env(t, 3.3, 5.5, 0.3, 0.3, E.outCubic);
  S.troph.style.opacity = vT;
  let k = 0;
  S.tr.forEach((row, ri) => row.forEach((d, j) => {
    const a = 3.4 + ri * 0.3 + j * 0.05;
    d.style.transform = `scale(${E.outBack(P(t, a, a + 0.35))})`;
  }));
  // the stand that will carry his name
  const vS = env(t, 8.9, 10.05, 0.4, 0.3, E.outCubic);
  S.stand.style.opacity = vS;
  S.tiers.forEach((e, i) => { const q = E.outCubic(P(t, 8.95 + i * 0.05, 9.4 + i * 0.05)); e.style.transform = `scaleX(${q})`; });
  tf(S.standname, { y: (1 - E.outCubic(P(t, 9.3, 9.8))) * 30, o: E.outCubic(P(t, 9.3, 9.7)) });
  endCard(t, 13.4);
}
"""

MIX = {"music_gain": 0.75, "fx_gain": 0.8, "rt": 2.6}


def score(A):
    """Warm and slow, in D major, turning briefly minor as the news breaks."""
    m, N = A.mix, A.note
    cues = []
    chords = [(0.0, ["D3", "A3", "F#4"]), (1.6, ["G2", "D3", "B3"]), (3.2, ["D3", "A3", "F#4"]),
              (5.6, ["B2", "F#3", "D4"]), (7.1, ["G2", "B2", "E3"]), (8.8, ["A2", "E3", "C#4"]),
              (10.15, ["D3", "A3", "E4"]), (11.3, ["G2", "D3", "B3"]), (12.3, ["D3", "A3", "F#4"])]
    for i, (t0, ns) in enumerate(chords):
        t1 = chords[i + 1][0] if i + 1 < len(chords) else 15.0
        m.add(A.pad([N(n) for n in ns], t1 - t0 + 1.2, cutoff=1000, a=0.7, r=1.2), t0, "music", gain=0.55, verb=0.45)
    # a slow piano line, one note per beat
    for t0, n in [(0.2, "F#4"), (1.65, "D4"), (3.2, "A4"), (5.6, "F#4"), (7.1, "E4"), (8.8, "C#5"), (10.15, "A4"), (11.3, "B4"), (12.35, "F#4")]:
        m.add(A.piano(N(n), 2.5, 0.75), t0, "music", gain=1.0, verb=0.55); cues.append(t0)
    m.add(A.piano(N("D2"), 3.0, 0.7), 0.2, "music", gain=0.8, verb=0.5)
    # a gentle bell for each group of trophies
    for ri, n in enumerate(["D6", "F#6", "A6", "B6", "C#7", "D7"]):
        m.add(A.chime(A.note(n) / 2), 3.4 + ri * 0.3, gain=0.22, pan=0.4, verb=0.6); cues.append(3.4 + ri * 0.3)
    # the stand: a soft rising wash
    m.add(A.sweep_noise(1.0, 300, 3000), 8.9, gain=0.06, verb=0.5)
    # Nothing is eternal: a long open chord
    m.add(A.piano(N("D2"), 3.2, 0.8), 10.15, "music", gain=0.9, verb=0.6)
    m.add(A.piano(N("A2"), 3.2, 0.6), 10.2, "music", gain=0.8, verb=0.6)
    m.add(A.piano(N("D2"), 2.8, 0.7), 12.35, "music", gain=0.8, verb=0.6)
    m.add(A.sweep_noise(0.5, 5000, 800), 13.35, gain=0.06, verb=0.3); cues.append(13.4)
    return cues
