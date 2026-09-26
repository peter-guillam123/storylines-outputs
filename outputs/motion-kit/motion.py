"""Build a Storylines motion piece: the animation source, its web page and its manifest.

Usage: python3 outputs/motion-kit/motion.py outputs/<motion-folder>
Then render the video with outputs/motion-kit/render.py.

Each motion folder holds content.py, which lists every piece of on-screen text
as a claim tied to a passage in a fetched Guardian article (the same checks as
the explainers), plus the page's animation code (JS) and styles (ANIM_CSS).
"""
import datetime as dt
import json
import pathlib
import re
import sys

KIT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(KIT.parent / "explainer-kit"))
import build as B  # noqa: E402
from build import C, Page, esc, long_date  # noqa: E402,F401

BASE_CSS = """
:root{--sans:"Avenir Next","Avenir","Helvetica Neue",Arial,sans-serif;--serif:"Charter","Iowan Old Style",Georgia,serif}
html,body{margin:0;height:100%;background:#000;overflow:hidden}
#stage{position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden;transform-origin:0 0;
  font-family:var(--sans);-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}
#stage *{box-sizing:border-box}
.wm{display:inline-block;overflow:hidden;vertical-align:top;padding:0 .02em .1em;margin-right:.22em}
.wm:last-child{margin-right:0}
.wi{display:inline-block;will-change:transform}
.endcard{position:absolute;inset:0;padding:110px 120px;background:var(--ec-bg);color:var(--ec-ink);z-index:50}
.ec-k{font:800 30px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--ec-accent);margin-bottom:46px}
.ec-list{list-style:none;margin:0;padding:0;display:grid;gap:22px}
.ec-list li{display:grid;grid-template-columns:150px 1fr auto;gap:28px;align-items:baseline;
  border-top:2px solid var(--ec-rule);padding-top:20px}
.ec-d{font:800 24px/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--ec-accent)}
.ec-h{font:600 36px/1.22 var(--serif)}
.ec-kind{font:700 20px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;opacity:.6}
.ec-f{position:absolute;left:120px;bottom:90px;font:600 26px/1 var(--sans);letter-spacing:.04em;opacity:.7}
"""

PAGE_CSS = """
.video-wrap{max-width:var(--wide);margin:clamp(-4rem,-6vw,-2rem) auto 0;padding:0 0 .5rem;position:relative;z-index:2}
.video-wrap video{display:block;width:100%;aspect-ratio:16/9;border-radius:14px;background:#000;
  box-shadow:0 30px 80px -30px rgba(0,0,0,.55)}
.video-meta{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;font:500 .85rem/1.4 var(--sans);color:var(--muted);margin:.8rem .2rem 0}
.video-meta a{font-weight:700}
.hero-in{padding-bottom:clamp(4rem,8vw,6.5rem)}
.snd{font:700 .85rem/1 var(--sans);background:var(--ink);color:var(--paper);border:0;border-radius:99px;padding:.7rem 1rem;cursor:pointer;min-height:40px}
.snd:hover,.snd:focus-visible{background:var(--accent);color:var(--accent-ink)}
.video-meta{align-items:center}
.sound-note{font-size:1rem;background:var(--card);border-radius:10px;padding:.8rem 1rem}
.script{list-style:none;margin:0;padding:0}
.script>li{display:grid;grid-template-columns:4.2rem 1fr;gap:1rem;padding:.9rem 0;border-top:1px solid var(--rule)}
.script .ts{font:800 .85rem/1.6 var(--sans);color:var(--accent-strong);font-variant-numeric:tabular-nums}
.script h3{margin:0 0 .3rem;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.script p{margin:0 0 .35rem}
.script p:last-child{margin-bottom:0}
.script .lab{font:600 .78rem/1.4 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
@media (max-width:600px){.script>li{grid-template-columns:1fr;gap:.1rem}}
"""


class MotionPage(Page):
    kind = "video"

    def manifest_intro(self):
        m = self.mod
        return [
            f"Output: `video.mp4` in this folder, rendered from `animation.html` (web page: `index.html`; web version of "
            f"this manifest: `manifest.html`). Storyline {m.STORYLINE_INDEX + 1} of `storylines-data/{m.DATA_FILE}`.",
            "Built by `outputs/motion-kit/motion.py`, which checks every quote and figure below against the fetched "
            "article text before the animation is written. The animation reads its words only from this list, so what "
            "is on screen is exactly what is listed here.",
            "",
            "Entries are grouped by the beat of the video in which they appear, in order. Labels (dates, stage names) "
            "are marked as such.",
            "",
            "Three things are generated from the Storylines data and not listed entry by entry: the Storyline title "
            "(used exactly as given), the end card crediting each article by headline and date, and the Read more "
            "list on the web page. The soundtrack is music and sound effects synthesised in code by "
            "`outputs/motion-kit/audio.py` (no samples, no licensed music, no speech), so it adds no words or facts. The "
            "end card closes with the line \"Every fact on screen comes from these articles "
            "· theguardian.com\". The date rail's stop labels are the dates of the beats listed below.",
            "",
        ]

    def build(self):
        m = self.mod
        T, script = {}, []
        for beat in m.SCRIPT:
            self.section = f"{beat['time']} · {beat['label']}"
            paras = []
            for key, c in beat["items"]:
                T[key] = re.sub(r"<[^>]+>", "", c.text)
                html_ = self.claims(c)
                if c.src is None:   # an on-screen label rather than a sentence
                    if re.fullmatch(r"d\d", key) or key == "ec":
                        continue    # the date or heading is already the beat's heading
                    html_ = f'<span class="lab">{html_}</span>'
                paras.append(html_)
            script.append((beat, paras))
        T["title"] = self.title
        credits = []
        for a in self.articles.values():
            d = dt.datetime.fromisoformat(a["publicationTime"].replace("Z", "+00:00"))
            kind = "Video" if "/video/" in a["path"] else "Audio" if "/audio/" in a["path"] else \
                "Opinion" if a["category"] == "Contrasting opinions" else ""
            credits.append({"date": f"{d.day} {d:%b}", "headline": a["headline"].strip(), "kind": kind})
        self.write_animation(T, credits)
        self.write_page(script)
        self.write_manifest()

    def write_animation(self, T, credits):
        m = self.mod
        js = (KIT / "stage.js").read_text()
        page = f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(self.title)}: animation source</title>
<style>{BASE_CSS}
{m.ANIM_CSS}</style></head>
<body><div id="stage"></div>
<script>
const DURATION = {m.DURATION};
const T = {json.dumps(T, ensure_ascii=False, indent=1)};
const CREDITS = {json.dumps(credits, ensure_ascii=False, indent=1)};
</script>
<script>
{js}
{m.JS}
</script>
</body></html>
"""
        (self.folder / "animation.html").write_text(page)

    def write_page(self, script):
        m = self.mod
        css = (KIT.parent / "explainer-kit" / "explainer.css").read_text()
        self.section = "Page header"
        dek = self.claims(*m.DEK, cite=False)
        n_text = sum(1 for a in self.articles.values() if not a["media"])
        rows = "".join(
            f'<li><span class="ts">{b["time"]}</span><div><h3>{esc(b["label"])}</h3>{"".join(f"<p>{p}</p>" for p in ps)}</div></li>'
            for b, ps in script)
        page = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(m.PAGE_TITLE)}</title>
<meta name="description" content="{esc(re.sub(r'<[^>]+>', '', dek))}">
<style>
{css}
{PAGE_CSS}
:root{{{m.THEME}}}
@media (prefers-color-scheme: dark){{:root{{{m.THEME_DARK}}}}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to the video</a>
<header class="hero">
  <div class="hero-in">
    <p class="kicker"><span>Storylines motion</span> <span class="kicker-tag">{esc(m.KICKER)}</span></p>
    <h1>{esc(self.title)}</h1>
    <p class="dek">{dek}</p>
    <p class="meta">A {m.DURATION}-second video with music and sound effects, no speech · Drawn from {n_text} Guardian articles</p>
  </div>
</header>
<main id="main">
<div class="video-wrap">
  <video controls muted loop playsinline preload="metadata" poster="poster.jpg" aria-describedby="s-script">
    <source src="video.mp4" type="video/mp4">
    Your browser can’t play this video. <a href="video.mp4">Download it</a> or read what’s on screen below.
  </video>
  <p class="video-meta"><button type="button" class="snd" id="snd">Play with sound</button><span>1080p · 16:9 · {m.DURATION} seconds</span><a href="video.mp4" download>Download the MP4</a><a href="../explainer-{m.SLUG}/index.html">Read the explainer</a></p>
</div>
<section aria-labelledby="s-script">
  <h2 id="s-script">What’s on screen</h2>
  <p class="rm-intro">Every word in the video, in order, with the Guardian article it comes from. On-screen labels are in small capitals.</p>
  <p class="sound-note"><strong>Sound.</strong> {esc(m.SOUND)}</p>
  <ol class="script">{rows}</ol>
</section>
<section class="readmore" id="read-more" aria-labelledby="rm-h">
  <h2 id="rm-h">Read more</h2>
  <p class="rm-intro">The video is drawn from these Guardian articles. The numbers match the source links above.</p>
  {self.readmore()}
</section>
</main>
<footer class="foot">
  <div class="foot-in">
    <h2>How this was made</h2>
    <p>The Guardian’s Storylines module chose this thread, and the articles in it, as one of the three strongest on the Trump administration topic page. An AI model (Claude) read the articles and designed this animation in code, using no words, dates or figures but theirs. The animation is written as a web page (<a href="animation.html">see it play live</a>) and rendered frame by frame to video; the music and sound effects are synthesised in code, with no samples or speech. Every piece of on-screen text is tied to a passage in the journalism: the full list is in the <a href="manifest.html">provenance manifest</a>. This is an experiment and has not yet been checked by a Guardian editor. <a href="../about/index.html">About this project</a>.</p>
  </div>
</footer>
<script>
(function(){{
  var v=document.querySelector('video');
  var b=document.getElementById('snd');
  if(v&&b) b.addEventListener('click',function(){{v.muted=false;v.currentTime=0;var p=v.play();if(p&&p.catch)p.catch(function(){{}});b.textContent='Playing with sound';}});
  if(!v||matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if(!('IntersectionObserver' in window)) return;
  new IntersectionObserver(function(es){{es.forEach(function(e){{
    if(e.isIntersecting&&e.intersectionRatio>.6){{var p=v.play();if(p&&p.catch)p.catch(function(){{}});}}
    else v.pause();}});}},{{threshold:[0,.6]}}).observe(v);
}})();
</script>
</body>
</html>
"""
        (self.folder / "index.html").write_text(page)


if __name__ == "__main__":
    pg = MotionPage(sys.argv[1])
    pg.build()
    if pg.errors:
        print("\n".join("ERROR " + e for e in pg.errors))
        sys.exit(1)
    print(f"Built {pg.folder.name}: {len(pg.manifest)} manifest entries, no errors")
