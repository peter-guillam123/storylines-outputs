"""Storylines motion: White House bans CNN, MS Now and Politico (15 seconds).

Every piece of on-screen text is a C(text, source, support) claim. The
animation reads its words from T[key], so the screen and the manifest match.
Build:  python3 outputs/motion-kit/motion.py outputs/motion-press-ban
Render: python3 outputs/motion-kit/render.py outputs/motion-press-ban
"""
from build import C

DATA_FILE = "trump-administration.json"
STORYLINE_INDEX = 0
SLUG = "press-ban"
PAGE_TITLE = "White House bans CNN, MS Now and Politico: a Storylines video"
KICKER = "Trump administration"
DURATION = 15

SRC = {
    "ban": "us-news/2026/sep/18/trump-bans-cnn-msnow-politico-white-house",
    "sue": "us-news/2026/sep/21/white-house-news-organization-ban-lawsuit",
    "dinner": "us-news/2026/sep/24/judge-orders-trump-restore-white-house-access-cnn-ms-now-politico-media-ban",
    "pool": "media/2026/sep/25/trump-media-ban-white-house-pool",
    "af1": "us-news/2026/sep/25/white-house-cnn-air-force-one",
}

THEME = """
--paper:#f6f2ea;--ink:#16171c;--muted:#5f5c56;--rule:#ddd5c7;--card:#ede6d9;
--accent:#e5482c;--accent-strong:#bf3219;--accent-ink:#fff;--chip:#16171c;--chip-ink:#f6f2ea;--focus:#2d5bd8;
--hero-bg:#121318;--hero-bg-solid:#15161b;--hero-ink:#f6f2ea;--accent-on-hero:#ff7a5c;
--hero-glow:radial-gradient(55% 75% at 88% 8%,rgba(255,91,58,.55),transparent 62%),radial-gradient(45% 60% at 5% 105%,rgba(122,96,255,.28),transparent 60%);
"""
THEME_DARK = """
--paper:#131419;--ink:#ece8e0;--muted:#a7a39c;--rule:#2e2f36;--card:#1d1e25;
--accent:#ff6a4d;--accent-strong:#ff8c73;--accent-ink:#16171c;--chip:#ece8e0;--chip-ink:#131419;--focus:#8fb0ff;
"""

DEK = [C("Fifteen seconds on how a ban on three news organisations became a lawsuit, a halt to the TV networks’ pool "
         "coverage, a court order and a fresh exclusion, in nine days.",
         note="Summary of the video. Each development is sourced in the script below.")]


def D(label, note):
    return C(label, note=note)


SCRIPT = [
    {"time": "0:00", "label": "Title", "items": [
        ("kicker", D("18–26 September 2026", "Span of the events shown: the ban was announced on Friday 18 September "
                     "(ban article, published that day) and CNN was blocked from Air Force One for Saturday 26 September.")),
    ]},
    {"time": "0:01", "label": "Friday 18 September", "items": [
        ("d1", D("Fri 18 Sept", "Date: the ban article, published on 18 September 2026, says the post was made “on Friday”.")),
        ("b1", C("Trump bans three news outlets from the White House", "ban",
                 "Donald Trump abruptly announced that he is banning outlets CNN, MS Now and Politico from the White House over their coverage.")),
        ("outlets", C("CNN · MS Now · Politico", "ban", "banning outlets CNN, MS Now and Politico")),
        ("press", D("Press", "Label on the drawn press passes.")),
        ("q1", C("“constant ‘reporting’ FAKE NEWS!”", "ban",
                 "over what he called their “constant ‘reporting’ FAKE NEWS!”")),
        ("a1", C("Donald Trump on Truth Social", "ban", "In a post on his Truth Social platform on Friday")),
    ]},
    {"time": "0:03", "label": "Saturday 19 September", "items": [
        ("d2", D("Sat 19 Sept", "Date: the lawsuit article, published on Monday 21 September 2026, says “on Saturday”.")),
        ("b2", C("Their badges are switched off", "sue",
                 "were told that their badges had been disabled and were taken")),
        ("stamp", C("Disabled", "sue", "had their badges disabled on Saturday")),
    ]},
    {"time": "0:04", "label": "Monday 21 September", "items": [
        ("d3", D("Mon 21 Sept", "Date: the lawsuit article, published on Monday 21 September 2026, says the suit was filed “on Monday morning”.")),
        ("b3", C("They sue.", "sue", "have sued to regain their ability to enter the building")),
        ("b3b", C("The TV networks stop filming the president, in solidarity", "pool",
                  "ceased recording and transmitting White House footage on Monday, in solidarity with CNN, MS Now and Politico")),
        ("nets", C("Fox · ABC · CBS · CNN · NBC", "sue",
                   "the five television networks that make up the primary video pool covering the White House – Fox News, ABC News, CBS News, CNN and NBC News")),
        ("poolLab", C("The TV pool", "pool", "The primary White House television pool")),
    ]},
    {"time": "0:06", "label": "In court", "items": [
        ("d4", D("In court", "Label. The justice department’s filing is dated only “earlier this week” in the 24 September "
                 "article; the hearing was “on Wednesday” (23 September). The date rail sits at 23 September for this beat.")),
        ("b4", C("Government lawyers argue the ban protects national security", "dinner",
                 "Department of Justice lawyers argued that the ban was necessary for national security reasons")),
    ]},
    {"time": "0:07", "label": "Thursday 24 September", "items": [
        ("d5", D("Thu 24 Sept", "Date: the article, published late on Thursday 24 September 2026 (US time), describes the order as issued early that morning and the dinner as “on Thursday evening”.")),
        ("b5", C("A judge orders their access restored for 14 days", "dinner",
                 "issued an early morning order forcing the administration to return access for a 14-day period")),
        ("n14", C("14", "dinner", "for a 14-day period")),
        ("days", D("days", "Label for the figure 14.")),
        ("b5b", C("That night, CNN and MS Now reporters are kept out of a state dinner", "dinner",
                  "Journalists for CNN and MS Now were denied access to the White House state dinner in honor of Xi Jinping, China’s president, on Thursday evening")),
    ]},
    {"time": "0:09", "label": "Friday 25 September", "items": [
        ("d6", D("Fri 25 Sept", "Date: the pool article, published on Friday 25 September 2026, quotes CNN’s anchor “on Friday morning”.")),
        ("b6", C("The TV pool starts filming again", "pool",
                 "The primary White House television pool has resumed filming administration events")),
    ]},
    {"time": "0:10", "label": "Saturday 26 September", "items": [
        ("d7", D("Sat 26 Sept", "Date: the article (published Friday evening, US time) refers to the flight as “on Saturday”.")),
        ("b7", C("CNN is left off Air Force One", "af1",
                 "The White House has blocked CNN from traveling aboard Air Force One on Saturday")),
        ("af1", C("Air Force One · Tennessee", "af1",
                  "CNN had been scheduled to fly with Donald Trump to Tennessee for a college football game")),
    ]},
    {"time": "0:11", "label": "Why it matters", "items": [
        ("q8", C("“This is about more than the rights of journalists”", "ban",
                 "“This is about more than the rights of journalists,” Henrich wrote in a statement.")),
        ("a8", C("Jacqui Heinrich, president of the White House Correspondents’ Association, 18 Sept", "ban",
                 "Jacqui Heinrich, president of the White House Correspondents’ Association (WHCA)",
                 note="Date: her statement is reported in the ban article of 18 September 2026.")),
    ]},
    {"time": "0:13", "label": "End card", "items": [
        ("ec", D("Drawn from Guardian journalism", "End card heading. The card lists every article in the Storyline by date and headline.")),
    ]},
]

CHECKS = [
    "**Dates.** Calendar dates are worked out from each article's publication date and the day of the week it gives "
    "(18 September 2026 was a Friday). Each is noted above.",
    "**The 'In court' beat.** The national security argument was made in a justice department filing dated only "
    "\"earlier this week\"; the hearing was on Wednesday 23 September. The beat is labelled \"In court\" rather than "
    "given a date, and the rail sits on 23 September.",
    "**Air Force One.** The exclusion was reported on Friday evening (US time) for Saturday's flight. The video places it "
    "on Saturday 26 September, the date of the flight.",
    "**Drawn elements.** The press passes, the five pool dots and the flight arc are diagrams, not pictures of real "
    "objects. The five networks and their order come from the lawsuit article. The arc shows no route.",
    "**The TV pool.** CNN's dot goes dark first, because the White House removed CNN from pool duty; the other "
    "four networks then stop filming in solidarity, as the pool article describes.",
    "**Why it matters.** The closing quote is from Jacqui Heinrich's statement on the day of the ban. Her full sentence "
    "continues: \"It is about the right of the American people to receive a full and independent account of the "
    "activities, policies and decisions of whoever occupies the nation's highest office.\" It is cut at the first "
    "sentence for length; the cut does not change its meaning.",
    "**Left out.** The opinion piece (Margaret Sullivan) is credited on the end card but not quoted: a 15-second video "
    "could not label it clearly as opinion.",
    "**Images.** None. Type, colour and drawn shapes only. No sound.",
]

ANIM_CSS = """
#stage{background:#111217;color:#f6f2ea}
.bg{position:absolute;inset:-10%;background:radial-gradient(45% 55% at 80% 20%,rgba(255,91,58,.42),transparent 70%),
  radial-gradient(40% 50% at 10% 100%,rgba(122,96,255,.22),transparent 70%)}
.grain{position:absolute;inset:0;opacity:.18;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.title{position:absolute;left:120px;top:250px;transform-origin:0 0;width:1500px}
.title .kick{font:800 30px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:#ff7a5c;margin-bottom:34px}
.title .tl{font:800 156px/.96 var(--sans);letter-spacing:-.04em}
.sweep{position:absolute;left:120px;top:222px;height:6px;width:1680px;background:#ff5b3a;transform-origin:left}
.date{position:absolute;left:120px;top:190px;font:800 40px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#ff7a5c}
.big{position:absolute;left:120px;top:280px;width:1040px;font:800 94px/1.02 var(--sans);letter-spacing:-.03em}
.big.b2{top:540px;font-size:60px;font-weight:700;color:#f6f2ea;opacity:.92;width:1000px}
.quote{position:absolute;left:120px;top:560px;width:1000px;font:italic 500 58px/1.15 var(--serif);color:#ffd3c7}
.attr{position:absolute;left:124px;top:650px;font:700 26px/1.3 var(--sans);letter-spacing:.08em;text-transform:uppercase;opacity:.75}
.card{position:absolute;left:0;top:0;width:250px;height:340px;border-radius:22px;background:#f6f2ea;color:#16171c;
  overflow:hidden;box-shadow:0 40px 80px -30px rgba(0,0,0,.7);transform-origin:50% 60%}
.card .strip{height:62px;background:#ff5b3a}
.card .pr{font:800 20px/1 var(--sans);letter-spacing:.3em;text-transform:uppercase;margin:28px 26px 0;color:#8a857c}
.card .nm{font:800 46px/1 var(--sans);letter-spacing:-.02em;margin:18px 26px 0;text-transform:uppercase}
.card .bar{position:absolute;left:26px;right:26px;bottom:30px;height:48px;border-radius:8px;
  background:repeating-linear-gradient(90deg,#16171c 0 4px,transparent 4px 9px);opacity:.8}
.card .stamp{position:absolute;left:50%;top:52%;padding:12px 22px;border:6px solid #e5482c;color:#e5482c;border-radius:10px;
  font:900 38px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;background:rgba(246,242,234,.85)}
.card .glow{position:absolute;inset:0;border-radius:22px;box-shadow:inset 0 0 0 6px #4fd1a0}
.card .flag{position:absolute;inset:0;border-radius:22px;box-shadow:inset 0 0 0 8px #ff5b3a}
.nets{position:absolute;left:1180px;top:820px;width:640px;display:flex;justify-content:space-between}
.net{width:104px;text-align:center}
.net .dot{width:64px;height:64px;margin:0 auto 14px;border-radius:50%;border:4px solid #f6f2ea}
.net .nl{font:800 22px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase}
.poolLab{position:absolute;left:1180px;top:772px;font:800 22px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:#ff7a5c}
.n14{position:absolute;left:1290px;top:690px;font:900 120px/.8 var(--sans);letter-spacing:-.06em;color:#4fd1a0}
.days{position:absolute;left:1470px;top:714px;font:800 44px/1 var(--sans);letter-spacing:.3em;text-transform:uppercase;color:#4fd1a0}
.arc{position:absolute;left:0;top:0;width:1920px;height:1080px}
.afl{position:absolute;left:1190px;top:860px;font:800 24px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:#ff7a5c}
.wq{position:absolute;left:120px;top:300px;width:1560px;font:italic 500 104px/1.08 var(--serif);color:#f6f2ea}
.wa{position:absolute;left:124px;top:640px;width:1400px;font:700 30px/1.3 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#ff7a5c}
.hd{position:absolute;left:120px;top:70px;font:700 26px/1 var(--sans);letter-spacing:.02em;opacity:.8}
.ec-list{gap:14px!important}.ec-list li{padding-top:14px!important}.ec-h{font-size:33px!important}
:root{--ec-bg:#f6f2ea;--ec-ink:#16171c;--ec-accent:#d63d20;--ec-rule:#ddd5c7}
"""

JS = r"""
const POSTER_T = 2.7;
let S = {};
function setup() {
  S.bg = mk('div', 'bg'); mk('div', 'grain');
  S.sweep = mk('div', 'sweep');
  S.title = mk('div', 'title');
  S.kick = words(S.title, T.kicker, 'kick');
  const tl = T.title.split(' ');   // White House bans / CNN, MS Now / and Politico
  S.tl = [words(S.title, tl.slice(0, 3).join(' '), 'tl'), words(S.title, tl.slice(3, 6).join(' '), 'tl'), words(S.title, tl.slice(6).join(' '), 'tl')];
  S.hd = mk('div', 'hd', null, T.title);

  S.rail = rail(['18', '19', '20', '21', '22', '23', '24', '25', '26'], { color: '#f6f2ea', accent: '#ff5b3a' });

  const dates = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7'];
  S.dates = dates.map(k => words(STAGE, T[k], 'date'));
  S.b1 = words(STAGE, T.b1, 'big');
  S.q1 = words(STAGE, T.q1, 'quote'); S.q1.line.style.top = '640px';
  S.a1 = words(STAGE, T.a1, 'attr'); S.a1.line.style.top = '730px';
  S.b2 = words(STAGE, T.b2, 'big');
  S.b3 = words(STAGE, T.b3, 'big');
  S.b3b = words(STAGE, T.b3b, 'big b2'); S.b3b.line.style.top = '420px';
  S.b4 = words(STAGE, T.b4, 'big');
  S.b5 = words(STAGE, T.b5, 'big');
  S.b5b = words(STAGE, T.b5b, 'big');
  S.b6 = words(STAGE, T.b6, 'big');
  S.b7 = words(STAGE, T.b7, 'big');
  S.wq = words(STAGE, T.q8, 'wq');
  S.wa = words(STAGE, T.a8, 'wa');

  // press passes
  S.cards = T.outlets.split(' · ').map(n => {
    const c = mk('div', 'card');
    mk('div', 'strip', c); mk('div', 'pr', c, T.press); mk('div', 'nm', c, n); mk('div', 'bar', c);
    const g = mk('div', 'glow', c), f = mk('div', 'flag', c), st = mk('div', 'stamp', c, T.stamp);
    return { c, g, f, st };
  });
  // the TV pool
  S.poolLab = mk('div', 'poolLab', null, T.poolLab);
  const nets = mk('div', 'nets');
  S.nets = T.nets.split(' · ').map(n => { const w = mk('div', 'net', nets); const d = mk('div', 'dot', w); mk('div', 'nl', w, n); return { w, d }; });
  S.netsBox = nets;
  // 14 days
  S.n14 = mk('div', 'n14', null, T.n14); S.days = mk('div', 'days', null, T.days);
  // flight arc
  const s = svg('svg', { class: 'arc', viewBox: '0 0 1920 1080' }, STAGE);
  S.arcPath = svg('path', { d: 'M1160 800 C 1380 560, 1620 470, 1900 480', fill: 'none', stroke: '#ff5b3a', 'stroke-width': 5, 'stroke-dasharray': '14 14' }, s);
  S.arcDot = svg('circle', { r: 14, fill: '#ff5b3a' }, s);
  S.arcLen = S.arcPath.getTotalLength();
  S.afl = mk('div', 'afl', null, T.af1);
}

const CARD_POS = [[1260, 300, -8], [1440, 280, 0], [1620, 300, 8]];
const CARD_SMALL = [[1330, 150, -6], [1470, 140, 0], [1610, 150, 6]];

function frame(t) {
  // background drift
  tf(S.bg, { x: Math.sin(t * 0.4) * 40, y: Math.cos(t * 0.3) * 30 });

  // TITLE (0–1.5), then shrinks into the running header
  const tIn = E.outExpo(P(t, 0, 0.7));
  S.sweep.style.transform = `scaleX(${tIn * (1 - E.inExpo(P(t, 1.1, 1.45)))})`;
  S.sweep.style.transformOrigin = t < 1.1 ? 'left' : 'right';
  wordsIO(S.kick, t, 0.1, 1.05, { stagger: 0.02 });
  S.tl.forEach((w, i) => wordsIO(w, t, 0.15 + i * 0.12, 1.15 + i * 0.03, { stagger: 0.05, dur: 0.6 }));
  S.title.style.visibility = t < 1.6 ? 'visible' : 'hidden';
  S.hd.style.opacity = E.outCubic(P(t, 1.45, 1.9)) * (1 - P(t, 13.2, 13.5));

  // DATE RAIL
  S.rail.pose(t, [[0, 0], [1.5, 0], [3.1, 1], [4.3, 3], [6.0, 5], [7.2, 6], [9.0, 7], [10.1, 8]],
    E.outCubic(P(t, 1.4, 1.9)) * (1 - E.inCubic(P(t, 11.3, 11.7))));

  // beat dates
  const bt = [[1.5, 3.0], [3.1, 4.2], [4.3, 5.9], [6.0, 7.1], [7.2, 8.9], [9.0, 10.0], [10.1, 11.3]];
  S.dates.forEach((w, i) => wordsIO(w, t, bt[i][0], bt[i][1], { stagger: 0.03 }));

  // beat text
  wordsIO(S.b1, t, 1.6, 2.95);
  wordsIO(S.q1, t, 2.0, 2.95, { stagger: 0.05 });
  wordsIO(S.a1, t, 2.15, 2.95, { stagger: 0.03 });
  wordsIO(S.b2, t, 3.2, 4.15);
  wordsIO(S.b3, t, 4.35, 5.85, { dur: 0.4 });
  wordsIO(S.b3b, t, 4.7, 5.85, { stagger: 0.03 });
  wordsIO(S.b4, t, 6.05, 7.05, { stagger: 0.03 });
  wordsIO(S.b5, t, 7.25, 7.85, { stagger: 0.03 });
  wordsIO(S.b5b, t, 7.98, 8.85, { stagger: 0.018, dur: 0.45 });
  wordsIO(S.b6, t, 9.05, 9.95, { stagger: 0.03 });
  wordsIO(S.b7, t, 10.15, 11.3, { stagger: 0.04 });
  wordsIO(S.wq, t, 11.5, 13.2, { stagger: 0.06, dur: 0.7 });
  wordsIO(S.wa, t, 11.95, 13.2, { stagger: 0.02 });

  // PRESS PASSES
  const small = E.inOutCubic(P(t, 4.3, 4.9)) * (1 - E.inOutCubic(P(t, 7.2, 7.7))) + E.inOutCubic(P(t, 8.9, 9.4));
  S.cards.forEach((k, i) => {
    const inn = E.outExpo(P(t, 1.55 + i * 0.1, 2.35 + i * 0.1));
    const [bx, by, br] = CARD_POS[i], [sx2, sy2, sr] = CARD_SMALL[i];
    let x = lerp(bx, sx2, small), y = lerp(by, sy2, small), r = lerp(br, sr, small), s = lerp(1, 0.5, small);
    x += (1 - inn) * 700; r += (1 - inn) * 25;
    // badges disabled (Sat 19) until the order (Thu 24)
    const dis = E.outExpo(P(t, 3.25 + i * 0.07, 3.6 + i * 0.07)) * (1 - E.outCubic(P(t, 7.3, 7.7)));
    y += dis * 26 * (1 - small); r += dis * (i - 1) * 5;
    tf(k.st, { x: -125 + 0, y: -30, s: lerp(2.2, 1, E.outBack(P(t, 3.25 + i * 0.07, 3.6 + i * 0.07))), r: -12, o: dis });
    k.st.style.transform = `translate(-50%,-50%) rotate(-12deg) scale(${lerp(2.2, 1, E.outBack(P(t, 3.25 + i * 0.07, 3.6 + i * 0.07)))})`;
    k.c.style.filter = `saturate(${1 - dis * 0.9}) brightness(${1 - dis * 0.25})`;
    k.g.style.opacity = env(t, 7.35, 8.6, 0.3, 0.4);
    // CNN and MS Now kept out of the dinner
    k.f.style.opacity = i < 2 ? env(t, 8.15, 8.85, 0.2, 0.3) : 0;
    // CNN falls off the plane (Sat 26)
    let fall = 0;
    if (i === 0) fall = E.inCubic(P(t, 10.45, 11.1));
    y += fall * 700; r += fall * -40;
    const fade = 1 - E.inCubic(P(t, 11.25, 11.6));
    tf(k.c, { x, y, r, s, o: inn * fade });
  });

  // THE TV POOL
  const poolVis = E.outCubic(P(t, 4.55, 4.9)) * (1 - E.inCubic(P(t, 10.0, 10.3))) * (1 - env(t, 7.2, 8.85, 0.3, 0.2));
  S.netsBox.style.opacity = poolVis; S.poolLab.style.opacity = poolVis;
  S.nets.forEach((n, i) => {
    // CNN (index 3) is taken off pool duty by the White House; the other four then stop in solidarity
    const off = i === 3 ? E.outCubic(P(t, 4.6, 4.8)) : E.outCubic(P(t, 5.0 + [0, 1, 2, 0, 3][i] * 0.12, 5.25 + [0, 1, 2, 0, 3][i] * 0.12));
    const on2 = E.outCubic(P(t, 9.1 + i * 0.1, 9.35 + i * 0.1));
    const live = Math.max(1 - off, on2);
    n.d.style.background = `rgba(255,91,58,${live})`;
    n.d.style.borderColor = live > 0.5 ? '#ff5b3a' : 'rgba(246,242,234,.5)';
    n.d.style.boxShadow = `0 0 ${40 * live}px rgba(255,91,58,${0.8 * live})`;
    tf(n.w, { y: (1 - E.outExpo(P(t, 4.55 + i * 0.05, 5.0 + i * 0.05))) * 40, o: 0.45 + 0.55 * live });
  });

  // 14 DAYS
  const v14 = env(t, 7.45, 7.9, 0.5, 0.2);
  tf(S.n14, { y: (1 - E.outExpo(P(t, 7.3, 7.9))) * 80, o: v14 });
  tf(S.days, { y: (1 - E.outExpo(P(t, 7.4, 8.0))) * 40, o: v14 });

  // FLIGHT ARC
  const draw = E.inOutCubic(P(t, 10.15, 10.9));
  const av = 1 - E.inCubic(P(t, 11.2, 11.5));
  S.arcPath.setAttribute('stroke-dashoffset', 0);
  S.arcPath.style.clipPath = `inset(0 ${(1 - draw) * 100}% 0 0)`;
  S.arcPath.style.opacity = t < 10.1 ? 0 : av;
  const pt = S.arcPath.getPointAtLength(S.arcLen * draw);
  S.arcDot.setAttribute('cx', pt.x); S.arcDot.setAttribute('cy', pt.y);
  S.arcDot.style.opacity = t < 10.1 ? 0 : av;
  tf(S.afl, { o: env(t, 10.3, 11.2, 0.3, 0.3) });

  // END CARD
  endCard(t, 13.35);
}
"""
