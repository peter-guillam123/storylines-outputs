"""Storylines motion: The 2025-26 Premier League title race (15 seconds).

Every piece of on-screen text is a C(text, source, support) claim. The
animation reads its words from T[key], so the screen and the manifest match.
Build:  python3 outputs/motion-kit/motion.py outputs/motion-city-title-race
Render: python3 outputs/motion-kit/render.py outputs/motion-city-title-race
Score:  python3 outputs/motion-kit/audio.py outputs/motion-city-title-race
"""
from build import C

DATA_FILE = "manchester-city.json"
STORYLINE_INDEX = 2
SLUG = "city-title-race"
PAGE_TITLE = "The 2025-26 Premier League title race: a Storylines video"
KICKER = "Manchester City"
DURATION = 15
SOUND = ("Narration by a synthetic British voice (Kokoro’s “George”), generated offline, over "
         "a driving, match-night rhythm with a synthesised crowd that swells as each result lands, loudest for the "
         "final draw at Bournemouth. The beat drops away for Guardiola’s words at the end, over a settled major "
         "chord.")

SRC = {
    "arteta": "football/2026/apr/25/angry-mikel-arteta-slams-red-card-decisions-after-arsenal-beat-newcastle",
    "everton": "football/2026/may/04/everton-manchester-city-premier-league-match-report",
    "brentford": "football/2026/may/09/manchester-city-brentford-premier-league-match-report",
    "palace": "football/2026/may/13/premier-league-manchester-city-crystal-palace-match-report",
    "bmth": "football/2026/may/19/kroupi-goal-hands-title-to-arsenal-as-bournemouth-hold-off-late-city-rally",
}

THEME = """
--paper:#f1f4ef;--ink:#10201a;--muted:#55635c;--rule:#d3dcd5;--card:#e4ebe5;
--accent:#c9a227;--accent-strong:#8a6d0c;--accent-ink:#10201a;--chip:#10201a;--chip-ink:#f1f4ef;--focus:#2f62d0;
--hero-bg:#0b1d15;--hero-bg-solid:#0d2018;--hero-ink:#eef3ee;--accent-on-hero:#f4d35e;
--hero-glow:radial-gradient(60% 70% at 88% 5%,rgba(244,211,94,.3),transparent 60%),radial-gradient(60% 70% at 0% 110%,rgba(40,140,90,.35),transparent 60%);
"""
THEME_DARK = """
--paper:#0c1511;--ink:#e6eee8;--muted:#9fb0a6;--rule:#1f2e27;--card:#15221c;
--accent:#f4d35e;--accent-strong:#f6dd83;--accent-ink:#0c1511;--chip:#e6eee8;--chip-ink:#0c1511;--focus:#8fb0ff;
"""

DEK = [C("Thirty seconds on the last month of the title race: the results, the gap between Arsenal and Manchester "
         "City, and the draw that settled it.",
         note="Summary of the video. Each element is sourced in the script below.")]


def D(label, note):
    return C(label, note=note)


SCRIPT = [
    {"time": "0:00", "label": "Title", "items": [
        ("kicker", D("Guardian reporting, 25 April – 19 May 2026", "Span of publication dates of the Storyline’s key stories.")),
    ]},
    {"time": "0:01", "label": "Sunday 19 April", "items": [
        ("d1", D("Sun 19 Apr", "Date derived: the 25 April article (a Saturday) calls the match “last Sunday’s pivotal game”.")),
        ("b1", C("City beat Arsenal in a pivotal game", "arteta", "last Sunday’s pivotal game at the Eithad Stadium")),
        ("s1", C("City 2 · Arsenal 1", "arteta", "City went on to win 2-1")),
    ]},
    {"time": "0:03", "label": "Saturday 25 April", "items": [
        ("d2", D("Sat 25 Apr", "Date: the article, published on Saturday 25 April 2026, says Arsenal won “on Saturday”.")),
        ("b2", C("Arsenal go three points clear, having played a game more", "arteta",
                 "to move three points back in front of City at the top of the table, albeit having played an extra match")),
        ("b2b", C("Mikel Arteta now says City’s Khusanov should have been sent off on 19 April. At the time, it caused little controversy.", "arteta",
                  ["The Arsenal manager insisted that the City defender, Abdukodir Khusanov, should have been sent off",
                   "an incident that did not generate much controversy, the consensus being Khusanov had defended his position fairly"],
                  note="19 April is “last Sunday” in this 25 April article.")),
        ("s2", C("Arsenal 1 · Newcastle 0", "arteta", "Arsenal had beaten Newcastle 1-0 at the Emirates Stadium")),
        ("g2", C("3 points", "arteta", "to move three points back in front of City", note="“Three” written as 3.")),
        ("g2b", C("Arsenal ahead, having played an extra match", "arteta", "albeit having played an extra match")),
    ]},
    {"time": "0:04", "label": "Monday 4 May", "items": [
        ("d3", D("Mon 4 May", "Date: the report was published on Monday 4 May 2026; the Brentford report calls it “Monday’s 3-3 draw at Everton”.")),
        ("b3", C("A 97th-minute equaliser saves a point at Everton", "everton",
                 "Jérémy Doku’s superb 97th-minute equaliser for Manchester City")),
        ("b3b", C("The Guardian’s report: “It is out of City’s hands now.”", "everton", "It is out of City’s hands now.")),
        ("s3", C("Everton 3 · City 3", "brentford", "Monday’s 3-3 draw at Everton")),
        ("g3", C("3 wins", "everton", "Arsenal are three wins from winning their first league title in 22 years.", note="“Three” written as 3.")),
        ("g3b", C("Arsenal’s distance from the title", "everton", "Arsenal are three wins from winning their first league title")),
    ]},
    {"time": "0:06", "label": "Saturday 9 May", "items": [
        ("d4", D("Sat 9 May", "Date: the report was published on Saturday 9 May 2026 and refers to Arsenal’s trip to West Ham “on Sunday”.")),
        ("b4", C("City win to keep up the pressure", "brentford", ["Manchester City keep pressure on Arsenal",
                 "secure victory and three points to keep their breath on Arsenal’s neck"])),
        ("s4", C("City 3 · Brentford 0", "palace", "the 3-0 win against Brentford")),
        ("g4", C("2 points", "brentford", "the deficit is down to two points but each have played 35 matches", note="“Two” written as 2.")),
        ("g4b", C("Arsenal ahead, 35 games each", "brentford", "each have played 35 matches")),
    ]},
    {"time": "0:08", "label": "Wednesday 13 May", "items": [
        ("d5", D("Wed 13 May", "Date: the report was published on Wednesday 13 May 2026 and says Arsenal host Burnley “on Monday”.")),
        ("b5", C("If Arsenal beat Burnley and City don’t win at Bournemouth, Arsenal are champions", "palace",
                 "if Arsenal defeat Burnley on Monday, and City fail to do the same at Bournemouth the next day, then Mikel Arteta’s team will be champions")),
        ("s5", C("City 3 · Crystal Palace 0", "palace", ["as Manchester City beat Crystal Palace 3-0",
                 "Savinho scoring on 84 minutes to follow Antoine Semenyo’s and Omar Marmoush’s first-half strikes"])),
        ("g5", C("2 points", "palace", "takes Manchester City back to within two points of Arsenal after 36 games each", note="“Two” written as 2.")),
        ("g5b", C("Arsenal ahead, 36 games each", "palace", "after 36 games each")),
    ]},
    {"time": "0:09", "label": "Tuesday 19 May", "items": [
        ("d6", D("Tue 19 May", "Date: the report was published on Tuesday 19 May 2026.")),
        ("b6", C("Arsenal are champions, their first title in 22 years", "bmth",
                 ["that means Arsenal are the 2025-26 Premier League champions", "Congratulations, Arsenal, champions of England after 22 years."])),
        ("s6", C("Bournemouth 1 · City 1", "bmth", ["held Manchester City to a 1-1 draw", "Erling Haaland’s late equaliser was nowhere near enough."])),
        ("k6", C("Junior Kroupi scores for Bournemouth", "bmth", "When Kroupi scored his brilliant strike")),
        ("champ", C("Champions: Arsenal", "bmth", "Congratulations, Arsenal, champions of England after 22 years.")),
    ]},
    {"time": "0:12", "label": "The last word", "items": [
        ("q7", C("“They deserve it.”", "bmth", "“They deserve it.”")),
        ("a7", C("Pep Guardiola, City manager, congratulating Arsenal", "bmth",
                 "“On behalf of everyone at Manchester City, we congratulate Mikel and all the staff, players and fans on winning the Premier League,” he said.")),
    ]},
    {"time": "0:13", "label": "End card", "items": [
        ("ec", D("Drawn from Guardian journalism", "End card heading.")),
    ]},
]

CHECKS = [
    "**Staying inside the Storyline.** Arsenal's win over Burnley on 18 May is reported only in an article from a "
    "different Storyline (Guardiola's departure). This video uses only its own Storyline's articles, so it shows the "
    "condition set out on 13 May (\"if Arsenal defeat Burnley … and City fail to do the same at Bournemouth\") and then "
    "the draw that made Arsenal champions, without reporting the Burnley result.",
    "**The gap.** Each figure is given as the report gives it: three points with Arsenal having played an extra match "
    "(25 April); two points with 35 games each (9 May); two points with 36 games each (13 May). On 4 May the report "
    "gives no points gap, so the video shows its \"three wins from winning their first league title\" instead.",
    "**Scores.** City 2-1 Arsenal and Arsenal 1-0 Newcastle (25 April article); Everton 3-3 City (4 May); City 3-0 "
    "Brentford (the 13 May report's \"3-0 win against Brentford\"); City 3-0 Crystal Palace (13 May); Bournemouth 1-1 "
    "City (19 May). Home side first.",
    "**Arteta's complaint.** On 25 April Arteta said City's Khusanov should have been sent off in the 19 April game "
    "(not the Newcastle match, where his complaint was about Newcastle's Pope). The article says the incident \"did not "
    "generate much controversy\" at the time; the screen says so too.",
    "**Headline and standfirst sources.** Where a score is stated only in a Guardian standfirst in the Storylines data, "
    "the manifest says so, and a body passage is cited alongside it where one exists.",
    "**19 April.** The 25 April article spells the ground \"Eithad Stadium\" (a typo). The video does not name the "
    "ground, only that it was \"a pivotal game\", the article's phrase.",
    "**Team colours.** Red for Arsenal and light blue for City are a charting convention to tell the teams apart, not "
    "club branding.",
    "**Left out.** Barney Ronay's opinion piece and the 4 May explainer on Guardiola's frustration. Both are credited "
    "on the end card.",
    "**Images.** None. Type, colour and drawn shapes only. **Sound:** music and effects synthesised in code; no samples, "
    "no licensed music; narration by a synthetic voice (Kokoro, run offline), held to the same sourcing rules.",
]

ANIM_CSS = """
#stage{background:#0b1a13;color:#eef3ee}
.bg{position:absolute;inset:-10%;background:radial-gradient(45% 55% at 85% 8%,rgba(244,211,94,.18),transparent 70%),
  radial-gradient(55% 60% at 5% 100%,rgba(40,140,90,.3),transparent 70%)}
.stripes{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 160px,transparent 160px 320px)}
.pitch{position:absolute;inset:0}
.grain{position:absolute;inset:0;opacity:.14;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.title{position:absolute;left:120px;top:250px;width:1600px}
.title .kick{font:800 30px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:#f4d35e;margin-bottom:34px}
.title .tl{font:800 156px/.96 var(--sans);letter-spacing:-.04em}
.hd{position:absolute;left:120px;top:70px;font:700 26px/1 var(--sans);opacity:.8}
.date{position:absolute;left:120px;top:190px;font:800 40px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#f4d35e}
.big{position:absolute;left:120px;top:280px;width:900px;font:800 84px/1.04 var(--sans);letter-spacing:-.03em}
.sub{position:absolute;left:120px;width:880px;font:600 40px/1.2 var(--sans);opacity:.9}
.board{position:absolute;left:1120px;top:260px;width:680px}
.team{display:grid;grid-template-columns:18px 1fr 110px;gap:22px;align-items:center;height:104px;border-bottom:2px solid rgba(238,243,238,.14)}
.team i{display:block;width:18px;height:70px;border-radius:4px}
.team .nm{font:800 52px/1 var(--sans);letter-spacing:-.01em}
.team .sc{font:900 84px/1 var(--sans);text-align:right;font-variant-numeric:tabular-nums}
.gap{position:absolute;left:1120px;top:560px;width:680px}
.gap .gn{font:900 120px/1 var(--sans);letter-spacing:-.04em;color:#f4d35e}
.gap .gl{font:700 32px/1.2 var(--sans);opacity:.85;margin-top:10px}
.champ{position:absolute;left:1120px;top:560px;width:700px;font:900 64px/1 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#f4d35e}
.q{position:absolute;left:120px;top:330px;width:1600px;font:italic 500 170px/1 var(--serif)}
.qa{position:absolute;left:124px;top:560px;width:1500px;font:700 32px/1.3 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#f4d35e}
:root{--ec-bg:#eef3ee;--ec-ink:#10201a;--ec-accent:#8a6d0c;--ec-rule:#d3dcd5}
"""

JS = r"""
const POSTER_T = 11.2;
const COL = { City: '#7cc4ee', Arsenal: '#ef5350' };
let S = {};
function board(key) {
  const b = mk('div', 'board');
  const rows = T[key].split(' · ').map(x => {
    const m = x.match(/^(.*) (\d+)$/); const r = mk('div', 'team', b);
    const chip = mk('i', '', r); chip.style.background = COL[m[1]] || '#8f9c95';
    mk('div', 'nm', r, m[1]); mk('div', 'sc', r, m[2]); return r; });
  return { b, rows };
}
function gap(n, l) { const g = mk('div', 'gap'); mk('div', 'gn', g, T[n]); mk('div', 'gl', g, T[l]); return g; }
function setup() {
  S.bg = mk('div', 'bg'); mk('div', 'stripes');
  const p = svg('svg', { class: 'pitch', viewBox: '0 0 1920 1080' }, STAGE);
  S.lines = [
    svg('circle', { cx: 1460, cy: 540, r: 330, fill: 'none', stroke: 'rgba(238,243,238,.07)', 'stroke-width': 4 }, p),
    svg('line', { x1: 1460, y1: 0, x2: 1460, y2: 1080, stroke: 'rgba(238,243,238,.07)', 'stroke-width': 4 }, p),
  ];
  mk('div', 'grain');
  S.title = mk('div', 'title');
  S.kick = words(S.title, T.kicker, 'kick');
  S.tl = [words(S.title, 'The 2025-26', 'tl'), words(S.title, 'Premier League', 'tl'), words(S.title, 'title race', 'tl')];
  S.hd = mk('div', 'hd', null, T.title);
  S.rail = rail(['19 Apr', '25 Apr', '4 May', '9 May', '13 May', '19 May'], { color: '#eef3ee', accent: '#f4d35e' });
  S.dates = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6'].map(k => words(STAGE, T[k], 'date'));
  S.b = {};
  ['b1', 'b2', 'b3', 'b4', 'b5', 'b6'].forEach(k => S.b[k] = words(STAGE, T[k], 'big'));
  S.b2b = words(STAGE, T.b2b, 'sub'); S.b2b.line.style.top = '600px'; S.b2b.line.style.fontSize = '34px';
  S.b3b = words(STAGE, T.b3b, 'sub'); S.b3b.line.style.top = '620px';
  S.k6 = words(STAGE, T.k6, 'sub'); S.k6.line.style.top = '620px';
  S.b.b5.line.style.fontSize = '64px';
  S.champ = mk('div', 'champ', null, T.champ);
  S.boards = ['s1', 's2', 's3', 's4', 's5', 's6'].map(board);
  S.gaps = [null, gap('g2', 'g2b'), gap('g3', 'g3b'), gap('g4', 'g4b'), gap('g5', 'g5b'), null];
  S.q7 = words(STAGE, T.q7, 'q'); S.a7 = words(STAGE, T.a7, 'qa');
}

const BEATS = [[1.5, 3.05], [3.1, 4.85], [4.9, 6.85], [6.9, 8.35], [8.4, 9.85], [9.9, 11.95]];
function frame(t) {
  tf(S.bg, { x: Math.sin(t * 0.4) * 30, y: Math.cos(t * 0.3) * 24 });
  S.lines.forEach((l, i) => l.style.opacity = E.outCubic(P(t, 0.2 + i * 0.2, 1.0 + i * 0.2)));
  wordsIO(S.kick, t, 0.1, 1.05, { stagger: 0.02 });
  S.tl.forEach((w, i) => wordsIO(w, t, 0.15 + i * 0.1, 1.1 + i * 0.03, { stagger: 0.05, dur: 0.55 }));
  S.title.style.visibility = t < 1.55 ? 'visible' : 'hidden';
  S.hd.style.opacity = E.outCubic(P(t, 1.4, 1.8)) * (1 - P(t, 13.3, 13.6));
  S.rail.pose(t, [[0, 0], [1.5, 0], [3.1, 1], [4.9, 2], [6.9, 3], [8.4, 4], [9.9, 5]],
    E.outCubic(P(t, 1.4, 1.8)) * (1 - E.inCubic(P(t, 11.8, 12.2))));
  const o = { stagger: 0.03, dur: 0.5 };
  S.dates.forEach((w, i) => wordsIO(w, t, BEATS[i][0], BEATS[i][1], o));
  ['b1', 'b2', 'b3', 'b4', 'b5', 'b6'].forEach((k, i) => wordsIO(S.b[k], t, BEATS[i][0] + 0.05, BEATS[i][1], { ...o, stagger: 0.025 }));
  wordsIO(S.b2b, t, 3.6, 4.85, { ...o, stagger: 0.02 });
  wordsIO(S.b3b, t, 5.5, 6.85, { ...o, stagger: 0.02 });
  wordsIO(S.k6, t, 10.5, 11.95, { ...o, stagger: 0.02 });
  // scoreboards: rows slide in, the score flips up
  S.boards.forEach((bd, i) => {
    const [a, b] = BEATS[i];
    const v = env(t, a + 0.05, b, 0.35, 0.25);
    bd.b.style.opacity = v;
    bd.rows.forEach((r, j) => {
      tf(r, { x: (1 - E.outExpo(P(t, a + 0.05 + j * 0.08, a + 0.5 + j * 0.08))) * 120 });
      const sc = r.lastChild; sc.style.transform = `translateY(${(1 - E.outBack(P(t, a + 0.3 + j * 0.1, a + 0.65 + j * 0.1))) * 60}px)`;
      sc.style.opacity = E.outCubic(P(t, a + 0.3 + j * 0.1, a + 0.5 + j * 0.1));
    });
  });
  S.gaps.forEach((g, i) => {
    if (!g) return;
    const [a, b] = BEATS[i];
    tf(g, { y: (1 - E.outExpo(P(t, a + 0.5, a + 0.9))) * 40, o: env(t, a + 0.5, b, 0.3, 0.25) });
  });
  tf(S.champ, { y: (1 - E.outExpo(P(t, 10.4, 10.9))) * 40, o: env(t, 10.4, 11.95, 0.3, 0.25) });
  wordsIO(S.q7, t, 12.0, 13.3, { ...o, stagger: 0.1, dur: 0.6 });
  wordsIO(S.a7, t, 12.35, 13.3, { ...o, stagger: 0.02 });
  endCard(t, 13.4);
}
"""

MIX = {"music_gain": 0.55, "fx_gain": 1.0, "rt": 1.6}


def score(A):
    """Match-night drive at 124 bpm, with a synthesised crowd that swells on each result."""
    import numpy as np
    m, N = A.mix, A.note
    beat = 60 / 124
    cues = []
    roots = [(0.0, "A1"), (1.5, "F1"), (3.1, "C2"), (4.9, "G1"), (6.9, "A1"), (8.4, "F1"), (9.9, "D2"), (12.0, "A1")]
    def root(t):
        return N(max((r for r in roots if r[0] <= t + 1e-6), key=lambda r: r[0])[1])
    # the rhythm runs in finished-video time so the tempo stays steady through the holds
    r0, r1 = A.T(1.5), A.T(11.9)
    for t, x in A.bass_pulse(lambda r: root(A.Tinv(r)), r0, r1, step=beat / 2, length=0.18, cutoff=500):
        m.add(x, t, "music", gain=0.85, real=True)
    t = r0
    while t < r1:
        m.add(A.thud(120, 48, 0.3, 14, 0.5), t, "music", gain=0.8, real=True)          # kick on the beat
        m.add(A.tick(8000, 0.02, 0.22), t + beat / 2, "music", pan=0.3, real=True)      # off-beat hat
        t += beat
    for i, (t0, ns) in enumerate([(0.0, ["A2", "E3", "C4"]), (1.5, ["F2", "C3", "A3"]), (3.1, ["C3", "G3", "E4"]),
                                  (4.9, ["G2", "D3", "B3"]), (6.9, ["A2", "E3", "C4"]), (8.4, ["F2", "C3", "A3"]),
                                  (9.9, ["D3", "A3", "F#4"]), (12.0, ["A2", "E3", "C#4"])]):
        t1 = [1.5, 3.1, 4.9, 6.9, 8.4, 9.9, 12.0, 15.0][i]
        m.add(A.pad([N(n) for n in ns], A.D(t0, t1) + 0.8, cutoff=1300, a=0.2, r=0.8), t0, "music", gain=0.45, verb=0.3)

    def crowd(dur, level):
        n = A.noise(dur)
        x = A.filt(A.filt(n, "highpass", 250), "lowpass", 2800)
        tt = A.tt(dur)
        am = 0.75 + 0.25 * np.sin(2 * np.pi * (3.3 * tt + 0.7 * np.sin(2 * np.pi * 0.9 * tt)))
        envl = np.minimum(1, tt / 0.18) * np.exp(-np.maximum(0, tt - 0.25) * 2.2)
        return x * am * envl * level

    m.add(A.thud(70, 34, 1.2, 4, 0.3), 0.18, gain=0.8, verb=0.3); cues.append(0.18)
    for i, (a, _) in enumerate([[1.5, 0], [3.1, 0], [4.9, 0], [6.9, 0], [8.4, 0], [9.9, 0]]):
        m.add(crowd(1.8, 0.16 if i < 5 else 0.26), a + 0.3, pan=0.1, verb=0.4)
        m.add(A.blip(N("E5"), 0.14), a + 0.3, gain=0.2, verb=0.3); cues.append(a + 0.3)
    # the title settled: a bright chord, then the beat drops for Guardiola's words
    m.add(A.chime(N("C#6")), 10.0, gain=0.35, verb=0.5)
    m.add(A.chime(N("A5")), 10.05, gain=0.35, verb=0.5)
    for t0, n in [(12.0, "E4"), (12.5, "C#4"), (13.45, "A3")]:
        m.add(A.piano(N(n), 2.0, 0.7), t0, "music", gain=1.0, verb=0.5); cues.append(t0)
    m.add(A.sweep_noise(0.5, 6000, 800), 13.35, gain=0.1, verb=0.3)
    return cues

# ---- 30-second cut with narration (see motion-kit/timing.py)
LENGTH = 30
VOICE = "bm_george"
SEGMENTS = [(0, 1.5, 1.2), (1.5, 3.1, 1.2, 2.0), (3.1, 4.9, 1.2, 3.0), (4.9, 6.9, 1.2, 3.2), (6.9, 8.4, 1.1, 2.2),
            (8.4, 9.9, 1.1, 3.5), (9.9, 12.0, 1.1, 3.0), (12.0, 13.4, 0.9, 2.0), (13.4, 15, 1.2)]
SCRIPT_SEG = [0, 1, 2, 3, 4, 5, 6, 7, 8]
NARRATION = [
    (1, "n1", C("City beat Arsenal in April.", "arteta", ["last Sunday’s pivotal game", "City went on to win 2-1"],
                note="April: the game was on Sunday 19 April, “last Sunday” in this 25 April article.")),
    (2, "n2", C("Then Arsenal went three points clear, having played a game more.", "arteta",
                "to move three points back in front of City at the top of the table, albeit having played an extra match")),
    (4, "n4", C("City drew at Everton, then beat Brentford", "brentford",
                ["Monday’s 3-3 draw at Everton", "Manchester City keep pressure on Arsenal as Jérémy Doku sparks defeat of Brentford"])),
    (5, "n4b", C("and Crystal Palace, to get within two points.", "palace",
                 ["as Manchester City beat Crystal Palace 3-0 to close to within two points of Arsenal",
                  "takes Manchester City back to within two points of Arsenal after 36 games each"])),
    (6, "n5", C("Then a draw at Bournemouth meant Arsenal were champions.", "bmth",
                ["held Manchester City to a 1-1 draw that means Arsenal are the 2025-26 Premier League champions",
                 "Congratulations, Arsenal, champions of England after 22 years."])),
]
