"""Build a Storylines explainer page and its provenance manifest.

Usage: python3 outputs/explainer-kit/build.py outputs/<explainer-folder>

Each explainer folder holds content.py (the words, each tied to a source
passage), sources/ (the fetched Guardian articles) and gets index.html and
manifest.md written into it. The build fails if any quote, figure or support
passage can't be found in the article it is credited to.
"""
import datetime as dt
import html
import importlib.util
import json
import pathlib
import re
import sys
sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
ROOT = KIT.parents[1]
GU = "https://www.theguardian.com/"

CATEGORY_ORDER = ["Key Stories", "Explainers", "Contrasting opinions", "Deep Reads",
                  "Profiles and Interviews", "Find multimedia"]
CATEGORY_LABEL = {"Key Stories": "Key stories", "Explainers": "Explainer",
                  "Contrasting opinions": "Opinion", "Deep Reads": "Deep read",
                  "Profiles and Interviews": "Profile", "Find multimedia": "Watch and listen"}


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = s.replace("⁠", "").replace("‌", "").replace("​", "").replace(" ", " ")
    s = re.sub("[‘’“”\"]", "'", s)
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def esc(s):
    return html.escape(s, quote=True)


def long_date(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return f"{d.day} {d:%B %Y}"


class C:
    """One claim: text as shown, the source key, and the passage that supports it."""

    def __init__(self, text, src=None, support=None, note=None):
        self.text, self.src, self.note = text, src, note
        self.support = [support] if isinstance(support, str) else (support or [])


class Page:
    def __init__(self, folder):
        self.folder = pathlib.Path(folder).resolve()
        sys.path.insert(0, str(KIT))
        spec = importlib.util.spec_from_file_location("content", self.folder / "content.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        data = json.loads((ROOT / "storylines-data" / self.mod.DATA_FILE).read_text())
        self.storyline = data["storylines"][self.mod.STORYLINE_INDEX]
        self.title = self.storyline["title"]
        self.manifest, self.errors, self.warnings = [], [], []
        self.section = "Header"
        self._load_articles()

    # ---- sources -------------------------------------------------------
    def _load_articles(self):
        items = []
        for cat in CATEGORY_ORDER:
            for c in self.storyline["content"]:
                if c["category"] != cat:
                    continue
                arts = c["articles"]
                if cat == "Key Stories":
                    arts = sorted(arts, key=lambda a: a["publicationTime"])
                for a in arts:
                    items.append(dict(a, category=cat))
        self.articles = {}
        for n, a in enumerate(items, 1):
            path = a["url"].replace(GU, "")
            f = self.folder / "sources" / (path.split("/")[-1] + ".json")
            media = "/video/" in path or "/audio/" in path
            rec = json.loads(f.read_text()) if f.exists() else None
            text = (a["headline"] + " " + (a["standfirst"] or ""))
            if rec:
                text += " " + (rec["headline"] or "") + " " + (rec["standfirst"] or "") + " " + rec["bodyText"]
            a.update(n=n, path=path, media=media, fetched=bool(rec),
                     byline=(rec or {}).get("byline") or a.get("byline"), normtext=norm(text), normbody=norm(rec["bodyText"]) if rec else "")
            self.articles[path] = a
        self.keys = {}
        for key, path in self.mod.SRC.items():
            if path not in self.articles:
                sys.exit(f"SRC {key}: {path} is not in this Storyline")
            self.keys[key] = self.articles[path]

    # ---- claims --------------------------------------------------------
    def check(self, c):
        if c.src is None:
            if re.search(r"\d", re.sub(r"<[^>]+>", "", c.text)) and not c.note:
                self.errors.append(f"Unsourced text with a figure: {c.text}")
            return
        a = self.keys[c.src]
        body = a["normtext"]
        for s in c.support:
            if norm(s) not in body:
                self.errors.append(f"[{c.src}] support passage not found: {s[:90]}")
        plain = re.sub(r"<[^>]+>", "", c.text)
        for q in re.findall(r"“(.+?)”", plain):
            for part in re.split(r"\s*…\s*", q):
                part = norm(part).strip(" .,;:'")
                if part and part not in body:
                    self.errors.append(f"[{c.src}] quote not found verbatim: {part[:90]}")
        sup = " ".join(norm(s) for s in c.support) + " " + norm(c.note or "")
        for num in re.findall(r"\d[\d,.]*\d|\d", plain):
            if num.replace(",", "") not in sup.replace(",", ""):
                self.errors.append(f"[{c.src}] figure '{num}' not in support passage or note: {plain[:80]}")
        outside = re.sub(r"“.+?”", "", plain)
        if "—" in outside:
            self.errors.append(f"Em dash outside a quote: {plain[:80]}")

    def record(self, c):
        self.check(c)
        self.manifest.append((self.section, c))

    def cite(self, key):
        a = self.keys[key]
        label = f"Source {a['n']}: {a['headline'].strip()} (Guardian, {long_date(a['publicationTime'])})"
        return (f'<a class="cite" href="{esc(a["url"])}" target="_blank" rel="noopener" '
                f'aria-label="{esc(label)}" data-h="{esc(a["headline"].strip())}">{a["n"]}</a>')

    def claims(self, *cs, cite=True):
        """Render claims as running text, with a source chip after each run from one article."""
        out = []
        for i, c in enumerate(cs):
            self.record(c)
            out.append(c.text)
            nxt = cs[i + 1].src if i + 1 < len(cs) else None
            if cite and c.src and c.src != nxt:
                out[-1] += self.cite(c.src)
        return " ".join(out)

    def p(self, *cs, cls=""):
        return f'<p class="{cls}">{self.claims(*cs)}</p>' if cls else f"<p>{self.claims(*cs)}</p>"

    def note(self, text):
        """Framing text with no factual content (headings, labels, instructions)."""
        self.manifest.append((self.section, C(text, None, None, "Heading or label: makes no claim beyond facts sourced elsewhere on the page")))
        return text

    # ---- page parts ----------------------------------------------------
    def thread(self):
        """The five Key Stories as a chain across the header."""
        keys = [a for a in self.articles.values() if a["category"] == "Key Stories"]
        pts = []
        for i, a in enumerate(keys):
            d = dt.datetime.fromisoformat(a["publicationTime"].replace("Z", "+00:00"))
            pts.append(f'<li style="--i:{i}"><a href="{esc(a["url"])}" target="_blank" rel="noopener">'
                       f'<span class="t-date">{d.day} {d:%b}</span>'
                       f'<span class="t-head">{esc(a["headline"].strip())}</span></a></li>')
        return ('<nav class="thread" aria-label="The five key stories in this Storyline, oldest first">'
                f'<ol>{"".join(pts)}</ol></nav>')

    def readmore(self):
        groups = []
        for cat in CATEGORY_ORDER:
            arts = [a for a in self.articles.values() if a["category"] == cat]
            if not arts:
                continue
            lis = []
            for a in arts:
                kind = "Video" if "/video/" in a["path"] else "Audio" if "/audio/" in a["path"] else ""
                by = a["byline"] if cat != "Find multimedia" else ""
                meta = " · ".join(x for x in [kind, esc(by or ""), long_date(a["publicationTime"])] if x)
                lis.append(f'<li><span class="rm-n" aria-hidden="true">{a["n"]}</span>'
                           f'<a href="{esc(a["url"])}" target="_blank" rel="noopener">{esc(a["headline"].strip())}</a>'
                           f'<span class="rm-meta">{meta}</span></li>')
            groups.append(f'<section class="rm-group"><h3>{CATEGORY_LABEL[cat]}</h3><ol>{"".join(lis)}</ol></section>')
        return "".join(groups)

    def build(self):
        m = self.mod
        self.section = "Header"
        dek = self.claims(*m.DEK, cite=False)
        body = m.body(self)
        css = (KIT / "explainer.css").read_text()
        js = (KIT / "explainer.js").read_text()
        n_text = sum(1 for a in self.articles.values() if not a["media"])
        motion = self.folder.parent / self.folder.name.replace("explainer-", "motion-")
        vlen = json.loads((motion / "timing.json").read_text())["length"] if (motion / "timing.json").exists() else 15
        video_link = (f' · <a href="../{motion.name}/index.html">Watch the {vlen}-second video</a>'
                      if self.folder.name.startswith("explainer-") and (motion / "video.mp4").exists() else "")
        n_fetched = sum(1 for a in self.articles.values() if not a["media"] and a["fetched"])
        read_line = ("read the full text of each text article" if n_fetched == n_text else
                     f"read the full text of {n_fetched} of the {n_text} text articles (the other {n_text - n_fetched} "
                     f"could not be retrieved, so only their headline and standfirst were used)")
        dates = sorted(a["publicationTime"] for a in self.articles.values())
        d0 = dt.datetime.fromisoformat(dates[0].replace("Z", "+00:00"))
        d1 = dt.datetime.fromisoformat(dates[-1].replace("Z", "+00:00"))
        span = f"{d0.day}–{d1.day} {d1:%B %Y}" if d0.month == d1.month else f"{d0.day} {d0:%B} – {d1.day} {d1:%B %Y}"
        page = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(m.PAGE_TITLE)}</title>
<meta name="description" content="{esc(re.sub(r'<[^>]+>', '', dek))}">
<style>
{css}
:root{{{m.THEME}}}
@media (prefers-color-scheme: dark){{:root{{{m.THEME_DARK}}}}}
{getattr(m, 'CSS', '')}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to the explainer</a>
<header class="hero">
  <div class="hero-in">
    <p class="kicker"><span>Storylines explainer</span> <span class="kicker-tag">{esc(m.KICKER)}</span></p>
    <h1>{esc(self.title)}</h1>
    <p class="dek">{dek}</p>
    <p class="meta">Drawn from {n_text} Guardian articles published {span} · About a five-minute read{video_link}</p>
    {self.thread()}
  </div>
</header>
<main id="main">
{body}
<section class="readmore" id="read-more" aria-labelledby="rm-h">
  <h2 id="rm-h">Read more</h2>
  <p class="rm-intro">Every fact on this page comes from these Guardian articles. The numbers match the source links in the text.</p>
  {self.readmore()}
</section>
</main>
<footer class="foot">
  <div class="foot-in">
    <h2>How this was made</h2>
    <p>The Guardian’s Storylines module chose this thread, and the articles in it, as one of the three strongest on the Trump administration topic page. An AI model (Claude) then {read_line} and wrote this summary, using nothing but those articles. Every sentence is tied to a passage in the journalism: the full list is in the <a href="manifest.html">provenance manifest</a>. This is an experiment and has not yet been checked by a Guardian editor. <a href="../about/index.html">About this project</a>.</p>
  </div>
</footer>
<script>
{js}
{getattr(m, 'JS', '')}
</script>
</body>
</html>
"""
        (self.folder / "index.html").write_text(page)
        self.write_manifest()
        return page

    def write_manifest(self):
        m = self.mod
        out = [f"# Provenance manifest: {self.title}", ""] + (self.manifest_intro() if hasattr(self, "manifest_intro") else [
               f"Output: `index.html` in this folder (web version of this manifest: `manifest.html`). Storyline {m.STORYLINE_INDEX + 1} of `storylines-data/{m.DATA_FILE}`.",
               "Built by `outputs/explainer-kit/build.py`, which checks every quote and figure below against the fetched article text.",
               "", "Every piece of text on the page is listed in the order it appears. Headings, labels and instructions "
               "are marked as such: they make no claim beyond facts sourced elsewhere on the page.",
               "",
               "Two parts of the page are generated straight from the Storylines data and are not listed entry by entry: "
               "the chain of five key stories in the header and the Read more list. Both reproduce each article's headline, "
               "byline and publication date exactly as the Guardian published them. The line under the title counts the text "
               "articles in the Storyline and gives the span of their publication dates.", ""])
        sec, i = None, 0
        for s, c in self.manifest:
            if s != sec:
                out += [f"## {s}", ""]
                sec = s
            i += 1
            txt = re.sub(r"<[^>]+>", "", c.text).strip()
            out.append(f"**{i}.** {txt}")
            if c.src:
                a = self.keys[c.src]
                out.append(f"- Source: [{a['headline'].strip()}]({a['url']}) ({long_date(a['publicationTime'])})")
                for sp in c.support:
                    where = "" if norm(sp) in a["normbody"] else " *(from the headline or standfirst, not the body text)*"
                    out.append(f"- Supports: {sp}{where}")
            if c.note:
                out.append(f"- Note: {c.note}")
            out.append("")
        out += ["## Checks", ""] + [f"- {x}" for x in m.CHECKS] + [""]
        (self.folder / "manifest.md").write_text("\n".join(out))
        self.write_manifest_html(out)

    def write_manifest_html(self, md_lines):
        """A readable web version of manifest.md, so the page's footer link works when hosted."""
        def inline(t):
            t = esc(t)
            t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
            t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
            return re.sub(r"\[(.+?)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
        body, in_ul = [], False
        for line in md_lines:
            if line.startswith("- ") and not in_ul:
                body.append("<ul>")
                in_ul = True
            if not line.startswith("- ") and in_ul:
                body.append("</ul>")
                in_ul = False
            if line.startswith("# "):
                continue
            elif line.startswith("## "):
                body.append(f"<h2>{inline(line[3:])}</h2>")
            elif line.startswith("- Supports: ") and line.endswith("*(from the headline or standfirst, not the body text)*"):
                body.append(f'<li class="sup"><span>Supports</span><q>{inline(line[12:line.rindex(" *(")])}</q><em class="hs">From the headline or standfirst, not the body text</em></li>')
            elif line.startswith("- Supports: "):
                body.append(f'<li class="sup"><span>Supports</span><q>{inline(line[12:])}</q></li>')
            elif line.startswith("- Source: "):
                body.append(f'<li class="src"><span>Source</span>{inline(line[10:])}</li>')
            elif line.startswith("- Note: "):
                body.append(f'<li class="nt"><span>Note</span>{inline(line[8:])}</li>')
            elif line.startswith("- "):
                body.append(f"<li>{inline(line[2:])}</li>")
            elif line.startswith("**") and re.match(r"\*\*\d+\.\*\*", line):
                n, txt = re.match(r"\*\*(\d+)\.\*\* ?(.*)", line).groups()
                body.append(f'<p class="entry"><b>{n}</b>{inline(txt)}</p>')
            elif line.strip():
                body.append(f"<p>{inline(line)}</p>")
        if in_ul:
            body.append("</ul>")
        page = f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Provenance manifest: {esc(self.title)}</title>
<style>
*{{box-sizing:border-box}}
:root{{--paper:#f5f3ef;--ink:#1b1d21;--muted:#5e6064;--rule:#dcd7cf;--card:#ebe7e0;--accent:#c4532f}}
@media (prefers-color-scheme:dark){{:root{{--paper:#121417;--ink:#ebe8e3;--muted:#a3a5a8;--rule:#2a2d31;--card:#1c1f23;--accent:#f08a64}}}}
html{{overflow-x:clip}}
body{{margin:0;background:var(--paper);color:var(--ink);font:1rem/1.55 "Charter","Iowan Old Style",Georgia,serif}}
main{{max-width:46rem;margin:0 auto;padding:2rem 1rem 4rem}}
a{{color:inherit;text-decoration-color:var(--accent);text-underline-offset:.15em;overflow-wrap:anywhere}}
.k{{font:700 .75rem "Avenir Next","Segoe UI",system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}}
h1{{font:800 clamp(1.7rem,5vw,2.4rem)/1.1 "Avenir Next","Segoe UI",system-ui,sans-serif;letter-spacing:-.02em;margin:.3rem 0 1.2rem}}
h2{{font:800 1.25rem/1.2 "Avenir Next","Segoe UI",system-ui,sans-serif;margin:2.4rem 0 .8rem;padding-top:1rem;border-top:3px solid var(--ink)}}
.entry{{margin:1.2rem 0 .3rem;display:grid;grid-template-columns:2.4rem 1fr;font-size:1.05rem}}
.entry b{{font:800 .85rem "Avenir Next","Segoe UI",system-ui,sans-serif;color:var(--muted);padding-top:.2rem}}
ul{{margin:0 0 0 2.4rem;padding:0;list-style:none;font-size:.92rem}}
li{{margin:.3rem 0}}
li>span{{font:700 .68rem "Avenir Next","Segoe UI",system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-right:.5rem}}
.sup q{{display:block;background:var(--card);border-left:3px solid var(--accent);padding:.4rem .7rem;margin-top:.2rem;quotes:none}}
.nt{{color:var(--muted)}}
.hs{{display:block;font-size:.85rem;color:var(--muted);margin-top:.2rem}}
code{{font-size:.9em}}
</style></head><body><main>
<p class="k"><a href="index.html">Back to the {getattr(self, "kind", "explainer")}</a></p>
<h1>Provenance manifest: {esc(self.title)}</h1>
{"".join(body)}
</main></body></html>
"""
        (self.folder / "manifest.html").write_text(page)


if __name__ == "__main__":
    pg = Page(sys.argv[1])
    pg.build()
    for w in pg.warnings:
        print("WARN", w)
    if pg.errors:
        print("\n".join("ERROR " + e for e in pg.errors))
        sys.exit(1)
    print(f"Built {pg.folder.name}: {len(pg.manifest)} manifest entries, no errors")
