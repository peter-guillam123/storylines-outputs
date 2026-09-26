"""Storyline explainer: White House bans CNN, MS Now and Politico.

Every C(text, source, support) ties a piece of on-page text to the passage in
the fetched Guardian article that supports it. Build with:
python3 outputs/explainer-kit/build.py outputs/explainer-press-ban
"""
from build import C

DATA_FILE = "trump-administration.json"
STORYLINE_INDEX = 0
PAGE_TITLE = "White House bans CNN, MS Now and Politico: a Storylines explainer"
KICKER = "Trump administration"

SRC = {
    "ban": "us-news/2026/sep/18/trump-bans-cnn-msnow-politico-white-house",
    "sue": "us-news/2026/sep/21/white-house-news-organization-ban-lawsuit",
    "sullivan": "commentisfree/2026/sep/21/white-house-press-corps-boycott",
    "dinner": "us-news/2026/sep/24/judge-orders-trump-restore-white-house-access-cnn-ms-now-politico-media-ban",
    "pool": "media/2026/sep/25/trump-media-ban-white-house-pool",
    "af1": "us-news/2026/sep/25/white-house-cnn-air-force-one",
}

THEME = """
--paper:#f6f2ea;--ink:#16171c;--muted:#5f5c56;--rule:#ddd5c7;--card:#ede6d9;
--accent:#e5482c;--accent-strong:#bf3219;--accent-ink:#fff;--chip:#16171c;--chip-ink:#f6f2ea;--focus:#2d5bd8;
--hero-bg:#121318;--hero-bg-solid:#15161b;--hero-ink:#f6f2ea;--accent-on-hero:#ff7a5c;
--hero-glow:radial-gradient(55% 75% at 88% 8%,rgba(255,91,58,.55),transparent 62%),radial-gradient(45% 60% at 5% 105%,rgba(122,96,255,.28),transparent 60%);
--opinion-bg:#e9e3fb;--opinion-ink:#2f2357;
--neg:#e5482c;--neg-soft:#f7d3c9;--pos:#17835f;--pos-soft:#cfeadd;--mid:#c98a0b;--mid-soft:#f5e3b5;--hatch:rgba(229,72,44,.16);--court:#3148a8;
"""
THEME_DARK = """
--paper:#131419;--ink:#ece8e0;--muted:#a7a39c;--rule:#2e2f36;--card:#1d1e25;
--accent:#ff6a4d;--accent-strong:#ff8c73;--accent-ink:#16171c;--chip:#ece8e0;--chip-ink:#131419;--focus:#8fb0ff;
--opinion-bg:#211c35;--opinion-ink:#d8ccff;
--neg:#ff6a4d;--neg-soft:#4a211b;--pos:#4fd1a0;--pos-soft:#153a2d;--mid:#f0b43c;--mid-soft:#3d3014;--hatch:rgba(255,106,77,.16);--court:#9db0ff;
"""

DEK = [C("In nine days, a ban on three news organisations led to a lawsuit, a halt to the TV networks’ pool "
         "coverage of the president, a court order and a fresh exclusion. This is what happened, in order.",
         note="Summary of the chronology below: the ban was announced on Friday 18 September and CNN was kept off "
              "Air Force One on Saturday 26 September, nine days later counting both.")]

CHECKS = [
    "**Dates.** Most articles give days of the week (\"on Friday\", \"on Saturday\"). Calendar dates were worked out from "
    "each article's publication date: 18 September 2026 was a Friday. Each derived date is noted above.",
    "**Air Force One.** The article reporting CNN's exclusion was published before the Saturday flight. The page says the "
    "White House blocked CNN from travelling, as the article does, not that the flight took place without it.",
    "**Access after the ruling.** The articles confirm that all three outlets were let back into the building at midday on "
    "24 September, and that CNN's access was confirmed as restored on 25 September. They say nothing specific about MS Now's "
    "or Politico's access on 25 or 26 September, so the access row in the diagram describes the three outlets together and "
    "names CNN only where the articles do.",
    "**Left out.** The ban article also mentions stories by the Washington Post and Politico published on the day of the ban "
    "(on US service member deaths and on F-35 technology). Only CNN's story is mentioned here, to keep the page short. "
    "Trump's \"Oh, the ban on the free press, right?\" exchange is left out because the article describes him as \"seeming "
    "confused\" and a short summary could not carry that context fairly.",
    "**Opinion.** The Storyline contains one opinion piece, by Margaret Sullivan. It is labelled as opinion and her view is "
    "attributed to her. The page notes that the Storyline has no piece arguing the other way.",
    "**Multimedia.** The audio episode (The Latest) and the video of Betsy Klein arriving at the White House are linked in "
    "Read more by headline only. They were not used as sources.",
    "**Publication dates.** The header and Read more give each article's date as the Content API does, in GMT. Two "
    "articles published on Thursday and Friday evenings US time therefore carry the next day's date (25 and 26 "
    "September). Dates in the chronology are the days events happened, in US time.",
    "**Images.** None. The page uses type, colour and a diagram only.",
    "**Bylines.** The Storylines data gives no byline for most news pieces; bylines on the page come from the Content API.",
]

CSS = """
.days{display:grid;grid-template-rows:auto repeat(3,auto);grid-auto-flow:column;
  grid-template-columns:7.5rem repeat(9,minmax(0,1fr));gap:4px;margin-top:.4rem}
.days>div{min-width:0}
.lane-name{font:700 .74rem/1.25 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);
  display:flex;align-items:center;padding-right:.6rem}
.dh{padding:.5rem .45rem .55rem;border-radius:10px 10px 4px 4px;background:var(--paper);font-family:var(--sans)}
.dh .wd{display:block;font:700 .7rem/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.dh .dn{display:block;font:800 1.5rem/1.05 var(--sans);letter-spacing:-.02em}
.st{display:block;margin-top:.4rem;font:700 .68rem/1.2 var(--sans);padding:.28rem .35rem;border-radius:5px}
.st.neg{background:var(--neg-soft);color:var(--ink);box-shadow:inset 3px 0 0 var(--neg)}
.st.mid{background:var(--mid-soft);color:var(--ink);box-shadow:inset 3px 0 0 var(--mid)}
.st.pos{background:var(--pos-soft);color:var(--ink);box-shadow:inset 3px 0 0 var(--pos)}
.st.neu{background:var(--rule);color:var(--ink)}
.cell{background:var(--paper);border-radius:4px;padding:.35rem;min-height:4.2rem;display:flex;flex-direction:column;gap:.3rem}
.cell.paused{background:repeating-linear-gradient(135deg,var(--hatch) 0 6px,transparent 6px 12px),var(--paper)}
.cell.paused .ptag{font:700 .64rem/1.2 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--accent-strong)}
.ev{display:block;font:600 .8rem/1.28 var(--sans);text-decoration:none;padding:.4rem .45rem;border-radius:7px;
  background:var(--ink);color:var(--paper);transition:transform .15s}
.ev:hover,.ev:focus-visible{background:var(--accent);color:var(--accent-ink);transform:translateY(-1px)}
.ev.court{background:var(--court);color:var(--paper)}
.ev.court:hover,.ev.court:focus-visible{background:var(--accent);color:var(--accent-ink)}
.ev.tv{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 2px var(--ink)}
.legend .l-neg{background:var(--neg)}.legend .l-mid{background:var(--mid)}.legend .l-pos{background:var(--pos)}
.legend .l-hatch{background:repeating-linear-gradient(135deg,var(--accent) 0 3px,transparent 3px 6px)}
.cell.paused .ptag{visibility:hidden}
.cell.paused .ptag.first{visibility:visible}
@media (max-width:860px){
  .days{grid-auto-flow:row;grid-template-rows:none;grid-template-columns:5.2rem minmax(0,1fr);gap:0 6px}
  .days>div:first-child,.lane-name{display:none}
  .dh{grid-row:span 3;border-radius:10px;margin-bottom:8px}
  .dh .dn{font-size:1.3rem}
  .cell{min-height:0;padding:0;background:none;gap:0}
  .cell>*{margin-bottom:6px}
  .cell.paused{background:none}
  .cell.paused .ptag{visibility:visible;display:block;padding:.35rem .45rem;border-radius:7px;
    background:repeating-linear-gradient(135deg,var(--hatch) 0 6px,transparent 6px 12px)}
  .ev{font-size:.88rem;padding:.45rem .6rem}
  .lane-cap{position:static!important;width:auto!important;height:auto!important;clip:auto!important;
    display:block;font:700 .62rem/1.2 var(--sans);letter-spacing:.08em;text-transform:uppercase;opacity:.75;margin-bottom:.1rem}
}
.chron>li:target .what{background:var(--card);border-radius:10px;box-shadow:0 0 0 .6rem var(--card)}
.chron>li{scroll-margin-top:1.5rem}
"""

WEEK = {18: "Fri", 19: "Sat", 20: "Sun", 21: "Mon", 22: "Tue", 23: "Wed", 24: "Thu", 25: "Fri", 26: "Sat"}


def diagram(k):
    k.section = "Diagram: nine days, day by day"
    ev = {  # day -> lane -> [(label claim, css)]
        18: {"wh": [C("Trump announces the ban on Truth Social", "ban",
                      "In a post on his Truth Social platform on Friday, the US president said he was expelling the news outlets")]},
        19: {"wh": [C("Badges disabled and taken", "sue",
                      "journalists from MS Now and CNN attempted to access the building on Saturday morning but were told that their badges had been disabled and were taken")]},
        21: {"wh": [C("CNN kept from Monday’s pool duty", "sue",
                      "But the White House removed the organization from the five-member group that provides video of the president’s activities to the rest of the news media.")],
             "court": [C("The three outlets sue", "sue", "The suit was filed on Monday morning in the US district court for Washington DC.")],
             "tv": [C("Pool stops filming the president", "pool",
                      "ceased recording and transmitting White House footage on Monday, in solidarity with CNN, MS Now and Politico")]},
        22: {"wh": [C("Letters give formal notice", "dinner",
                      "only received formal notice – in letters sent to each news organization on Tuesday")]},
        23: {"court": [C("Hearing before Judge Kelly", "dinner",
                         "Timothy Kelly, the US district judge who appeared skeptical of arguments from lawyers representing the White House during a hearing on Wednesday")]},
        24: {"court": [C("Judge orders access restored for 14 days", "dinner",
                         "issued an early morning order forcing the administration to return access for a 14-day period")],
             "wh": [C("Let in at midday", "af1", "were not granted entry until midday"),
                    C("CNN and MS Now reporters kept out of state dinner", "dinner",
                      "Journalists for CNN and MS Now were denied access to the White House state dinner in honor of Xi Jinping")],
             "tv": [C("No network video of Xi summit", "pool",
                      "a summit with Xi Jinping, China’s president, did not receive video coverage on the leading television networks")]},
        25: {"tv": [C("Pool resumes, with CBS", "pool",
                      "a producer for CBS News confirmed that the network would be serving as the TV pooler for the day as scheduled")]},
        26: {"wh": [C("CNN left off Air Force One", "af1",
                      "The White House has blocked CNN from traveling aboard Air Force One on Saturday")]},
    }
    status = {
        18: ("neu", C("Ban announced", "ban", "“effective immediately”")),
        19: ("neg", C("Barred", "sue", "had their badges disabled on Saturday")),
        20: ("neg", C("Barred", "dinner", "after days of being barred from the building")),
        21: ("neg", C("Barred", "dinner", "after days of being barred from the building")),
        22: ("neg", C("Barred", "dinner", "after days of being barred from the building")),
        23: ("neg", C("Barred", "dinner", "after days of being barred from the building")),
        24: ("mid", C("Let in at midday", "af1", "were not granted entry until midday")),
        25: ("pos", C("CNN access restored", "pool", "“CNN’s access to the White House has been restored")),
        26: ("mid", C("CNN off the plane", "af1", "The White House has blocked CNN from traveling aboard Air Force One on Saturday")),
    }
    paused = {21, 22, 23, 24}
    lanes = [("wh", "The White House"), ("court", "The outlets and the court"), ("tv", "The TV networks")]
    cells = ['<div aria-hidden="true"></div>'] + [
        f'<div class="lane-name" aria-hidden="true">{k.note(name)}</div>' for _, name in lanes]
    for d in range(18, 27):
        cls, sc = status[d]
        k.record(sc)
        cells.append(f'<div class="dh"><span class="wd">{WEEK[d]}</span><span class="dn">{d}</span>'
                     f'<span class="vh"> September. Access for the three outlets: </span>'
                     f'<span class="st {cls}">{sc.text}</span></div>')
        for lane, name in lanes:
            items = []
            for c in ev.get(d, {}).get(lane, []):
                k.record(c)
                items.append(f'<a class="ev {lane}" href="#d{d}"><span class="lane-cap vh">{name}<span class="vh">:</span> </span>{c.text}</a>')
            paused_here = lane == "tv" and d in paused
            extra = (f'<span class="ptag{" first" if d == 22 else ""}">TV pool paused</span>' if paused_here else "")
            cls2 = "cell paused" if paused_here else "cell"
            cells.append(f'<div class="{cls2}">{"".join(items)}{extra}</div>')
    k.record(C("TV pool paused", "pool", "ceased recording and transmitting White House footage on Monday"))
    k.record(C("Pool still paused on Thursday", "pool", "With the pool still inactive on Thursday afternoon",
               note="Shown as hatching on the TV lane from Monday 21 to Thursday 24 September."))
    title = k.note("Nine days, day by day")
    sub = k.note("Each box is one development. Select it to jump to the full account below. The top row shows whether "
                 "the three outlets could get into the White House.")
    legend = [("l-neg", "Barred from the building"), ("l-mid", "Partly restored or new exclusion"),
              ("l-pos", "Access confirmed restored"), ("l-hatch", "TV pool not filming")]
    lg = "".join(f'<li><i class="{c}"></i>{k.note(t)}</li>' for c, t in legend)
    return (f'<figure class="panel wide" aria-labelledby="dg-h"><p class="panel-h" id="dg-h">{title}</p>'
            f'<p class="panel-sub">{sub}</p><div class="days">{"".join(cells)}</div>'
            f'<ul class="legend">{lg}</ul></figure>')


def body(k):
    out = []
    k.section = "In short"
    out.append('<section aria-labelledby="s-short"><h2 id="s-short">' + k.note("In short") + '</h2><ol class="inshort">')
    out.append("<li>" + k.claims(
        C("On Friday 18 September, Donald Trump announced that he was banning CNN, MS Now and Politico from the White "
          "House over their coverage.", "ban",
          "Donald Trump abruptly announced that he is banning outlets CNN, MS Now and Politico from the White House over their coverage.",
          note="Date: the article, published on 18 September 2026, says the post was made “on Friday”.")) + "</li>")
    out.append("<li>" + k.claims(
        C("The three sued.", "sue", "have sued to regain their ability to enter the building"),
        C("A federal judge ordered the White House to let them back in for 14 days, saying their passes had probably "
          "been taken away without due process.", "dinner",
          ["issued an early morning order forcing the administration to return access for a 14-day period",
           "argued in his ruling that the way in the which the White House banned the organizations had likely violated due process protections for journalists"])) + "</li>")
    out.append("<li>" + k.claims(
        C("Even after the ruling, CNN and MS Now journalists were kept out of a state dinner that evening,", "dinner",
          "Journalists for CNN and MS Now were denied access to the White House state dinner in honor of Xi Jinping, China’s president, on Thursday evening, hours after a federal judge ruled"),
        C("and CNN was then blocked from Air Force One.", "af1",
          "The White House has blocked CNN from traveling aboard Air Force One on Saturday")) + "</li>")
    out.append("<li>" + k.claims(
        C("The White House argued the ban was needed for national security;", "dinner",
          "Department of Justice lawyers argued that the ban was necessary for national security reasons"),
        C("the judge was sceptical that this was the real motive.", "dinner",
          "“skeptical … that defendants’ interest in safeguarding national security is the actual motivation for, or is even advanced by, the revocation of Plaintiffs’ hard passes”")) + "</li></ol></section>")

    out.append(diagram(k))

    k.section = "What happened, in order"
    out.append('<section aria-labelledby="s-chron"><h2 id="s-chron">' + k.note("What happened, in order") + '</h2><ol class="chron">')

    def day(d, label, head, *paras, note=None):
        k.record(C(f"{label} September", note=note or "Date derived from the article's publication date and day of the week."))
        return (f'<li id="d{d}"><div class="when"><small>{label.split()[0]}</small>{d} Sept</div>'
                f'<div class="what"><h3>{k.note(head)}</h3>{"".join(paras)}</div></li>')

    out.append(day(18, "Friday 18", "The ban",
        k.p(C("On Truth Social, Trump said he was expelling the three outlets “effective immediately” over their "
              "“constant ‘reporting’ FAKE NEWS!” He added: “Other Fake News Media Outlets to follow.”", "ban",
              ["In a post on his Truth Social platform on Friday, the US president said he was expelling the news outlets “effective immediately” over what he called their “constant ‘reporting’ FAKE NEWS!”",
               "Other Fake News Media Outlets to follow."])),
        k.p(C("That day CNN had reported that an “entirely false” intelligence report about a Chinese ship, made with the "
              "help of AI, had “almost started a war”. Trump said the ban was unrelated to that day’s reporting: “It’s "
              "really just cumulative stories over the last few years.”", "ban",
              ["CNN revealed that an “entirely false” intelligence report about a Chinese ship in the Middle East generated with the help of artificial intelligence (AI) had “almost started a war”",
               "Trump said his decision to ban the three outlets was unrelated to the stories. “It’s really just cumulative stories over the last few years,” he said"])),
        note="Date: the article, published on 18 September 2026, says the post was made “on Friday”."))

    out.append(day(19, "Saturday 19", "Badges switched off",
        k.p(C("Journalists from MS Now and CNN tried to enter the White House and were told their badges had been "
              "disabled. The badges were taken.", "sue",
              "journalists from MS Now and CNN attempted to access the building on Saturday morning but were told that their badges had been disabled and were taken")),
        note="Date: the lawsuit article, published on Monday 21 September 2026, says “on Saturday”."))

    out.append(day(21, "Monday 21", "The lawsuit, and the cameras stop",
        k.p(C("The three sued in the federal court in Washington DC and asked for an order lifting the ban while the "
              "case goes on. “Without notice or process, the White House revoked our journalists’ credentials because it "
              "objected to our reporting,” they said.", "sue",
              ["The suit was filed on Monday morning in the US district court for Washington DC.",
               "The parties are seeking a temporary restraining order that would immediately lift the ban – and return access for the journalists – while the case plays out.",
               "“Without notice or process, the White House revoked our journalists’ credentials because it objected to our reporting."])),
        k.p(C("CNN was due to film the president that day for the rest of the media, as the TV pooler. The White House "
              "removed it from the pool.", "sue",
              ["CNN was scheduled to serve as the television pooler on Monday. But the White House removed the organization from the five-member group that provides video of the president’s activities to the rest of the news media."]),
            C("In solidarity, the other pool networks (NBC, ABC, CBS and Fox News) stopped filming White House events, "
              "leaving an effective TV blackout of the president during the UN general assembly.", "pool",
              ["the pool – which also includes NBC, ABC, CBS and Fox News – ceased recording and transmitting White House footage on Monday, in solidarity with CNN, MS Now and Politico",
               "led to an effective TV blackout of coverage of the president during the United Nations general assembly"])),
        k.p(C("Responding to news of the lawsuit, Trump wrote on Truth Social: “The White House is not instituting an assault on the Free Press, something which I "
              "cherish. It is instituting an assault on the FAKE NEWS, something that has grown like Cancer in our "
              "beloved United States of America.”", "sue",
              "Trump responded to news of the pending lawsuit in a post on Truth Social, writing: “The White House is not instituting an assault on the Free Press, something which I cherish. It is instituting an assault on the FAKE NEWS, something that has grown like Cancer in our beloved United States of America.")),
        note="Date: the article, published on Monday 21 September 2026, says the suit was filed “on Monday morning”."))

    out.append(day(22, "Tuesday 22", "Formal notice, after the fact",
        k.p(C("Letters to each outlet accused them of behaviour that broke White House standards, “including by "
              "trafficking in verifiable falsehoods about national security and other issues, and publishing sensitive or "
              "classified information”. They gave the outlets until 5pm on Friday to contest the ban.", "dinner",
              ["only received formal notice – in letters sent to each news organization on Tuesday – that they “exhibited behavior in violation of the standards of professionalism and decorum expected of those given access to the White House Complex, including by trafficking in verifiable falsehoods about national security and other issues, and publishing sensitive or classified information”",
               "which informed each news organization that they had until 5pm on Friday to contest the ban"])),
        note="Date: the article, published late on Thursday 24 September 2026 (US time), says the letters were sent “on Tuesday”."))

    out.append(day(23, "Wednesday 23", "In court",
        k.p(C("Earlier in the week, in a court filing, justice department lawyers had argued the ban was needed for "
              "national security. At a hearing on Wednesday, Judge Timothy Kelly appeared sceptical of the White House’s "
              "case.", "dinner",
              ["Department of Justice lawyers argued that the ban was necessary for national security reasons",
               "Timothy Kelly, the US district judge who appeared skeptical of arguments from lawyers representing the White House during a hearing on Wednesday"])),
        note="Date: the article says the hearing was “on Wednesday”. It dates the justice department filing only as “earlier this week”."))

    out.append(day(24, "Thursday 24", "A ruling, then a closed door",
        k.p(C("Early in the morning, Kelly ordered access restored for 14 days. He found the outlets were likely to show "
              "their passes had been revoked without due process, and was “skeptical … that defendants’ interest in "
              "safeguarding national security is the actual motivation” for the ban.", "dinner",
              ["issued an early morning order forcing the administration to return access for a 14-day period",
               "“Plaintiffs are also likely to succeed in showing that their hard passes were revoked without constitutionally adequate due process,” he wrote.",
               "The judge also wrote that he was “skeptical … that defendants’ interest in safeguarding national security is the actual motivation for, or is even advanced by, the revocation of Plaintiffs’ hard passes”."])),
        k.p(C("Lawyers for the outlets told the judge their journalists were turned away that morning. The White House’s "
              "director of press operations said in a sworn statement that badges were reactivated as of 9.07am.", "dinner",
              ["“This morning journalists from each of CNN, MS Now, and Politico attempted to enter the White House and were turned away",
               "She said that US Secret Service indicated that badges were re-activated as of 9.07am"]),
            C("The journalists were not let in until midday.", "af1",
              "CNN, MS Now and Politico’s journalists sought to enter the White House on Thursday morning, but were not granted entry until midday."),
            C("That evening, CNN and MS Now journalists were kept out of the state dinner for China’s president, Xi "
              "Jinping. CNN reported that it was allowed only a photojournalist and an audio technician, not its reporter "
              "and producer.", "dinner",
              ["Journalists for CNN and MS Now were denied access to the White House state dinner in honor of Xi Jinping, China’s president, on Thursday evening",
               "“About an hour before Xi’s arrival was scheduled, the White House said CNN could cover the event, but only with a photojournalist and audio technician, notably excluding the network’s editorial team consisting of a reporter and producer,” CNN reported."])),
        note="Date: the article, published late on Thursday 24 September 2026 (US time), describes the dinner as “on Thursday evening”."))

    out.append(day(25, "Friday 25", "Cameras back on",
        k.p(C("The TV pool resumed, with CBS as the day’s pooler. “CNN’s access to the White House has been restored, and the TV pool "
              "appears to be functioning as normal,” the CNN anchor Pamela Brown told viewers.", "pool",
              ["The primary White House television pool has resumed filming administration events",
               "a producer for CBS News confirmed that the network would be serving as the TV pooler for the day as scheduled",
               "Pamela Brown, a CNN anchor, told viewers on Friday morning: “CNN’s access to the White House has been restored, and the TV pool appears to be functioning as normal.”"])),
        note="Date: the article, published on Friday 25 September 2026, quotes Brown speaking “on Friday morning”."))

    out.append(day(26, "Saturday 26", "Off the plane",
        k.p(C("The White House blocked CNN from Saturday’s Air Force One flight with Trump to a college football game in "
              "Tennessee, leaving it off the schedule guidance sent to reporters. The White House did not immediately respond to the Guardian’s request for "
              "comment.", "af1",
              ["The White House has blocked CNN from traveling aboard Air Force One on Saturday",
               "CNN had been scheduled to fly with Donald Trump to Tennessee for a college football game, the network said on Friday.",
               "The White House confirmed CNN’s exclusion when it did not list the network on guidance sent to the press corps regarding Trump’s schedule for Saturday.",
               "The White House did not immediately return the Guardian’s request for comment."])),
        note="Date: the article was published at 01.31 GMT on 26 September 2026 (Friday evening in the US) and refers to the flight as “on Saturday”."))
    out.append("</ol></section>")

    # ---- who's who ----
    k.section = "Who’s who, and where they stand"
    out.append('<section aria-labelledby="s-who"><h2 id="s-who">' + k.note("Who’s who, and where they stand") + '</h2><ul class="cards">')

    def card(name, role, *paras):
        return (f'<li class="card"><h3>{k.note(name)}</h3><p class="role">{k.note(role)}</p>{"".join(paras)}</li>')

    out.append(card("Donald Trump", "US president",
        k.p(C("Says the outlets write “FICTION and LIES”. “I don’t think that a court should allow fake news to be "
              "written day after day after day.”", "ban",
              ["Media Outlets shouldn’t be able to constantly write or report FICTION and LIES",
               "“I don’t think that a court should allow fake news to be written day after day after day."]))))
    out.append(card("The White House and justice department", "Defending the ban",
        k.p(C("Argue the ban protects national security, pointing to articles that relied on non-public information.", "dinner",
              "Department of Justice lawyers argued that the ban was necessary for national security reasons, and listed examples of articles that relied on non-public information."))))
    out.append(card("CNN, MS Now and Politico", "Suing to get back in",
        k.p(C("Say they are being punished for what they report, and had no chance to contest the ban before their passes were revoked. Their "
              "lawsuit says “this ban could not be a more direct assault on the First Amendment”.", "sue",
              ["Defendants took these actions in express retaliation for Plaintiffs’ First Amendment-protected newsgathering and speech because they dislike that speech’s content and viewpoint",
               "further alleging that the news organizations were unfairly deprived an opportunity to contest the ban as required by the fifth amendment of the US constitution",
               "“this ban could not be a more direct assault on the First Amendment nor a more blatant violation of our most fundamental constitutional principles.”"]))))
    out.append(card("The rest of the press", "Correspondents and TV networks",
        k.p(C("Jacqui Heinrich, president of the White House Correspondents’ Association: “This is about more than the "
              "rights of journalists … It is about the right of the American people to receive a full and independent "
              "account of the activities, policies and decisions of whoever occupies the nation’s highest office.”", "ban",
              ["Jacqui Heinrich, president of the White House Correspondents’ Association (WHCA)",
               "“This is about more than the rights of journalists,” Henrich wrote in a statement. “It is about the right of the American people to receive a full and independent account of the activities, policies and decisions of whoever occupies the nation’s highest office.”"]),
            C("The five pool networks, CNN among them: “No administration should restrict a news organization because it objects to its "
              "reporting.”", "sue",
              "No administration should restrict a news organization because it objects to its reporting."))))
    out.append(card("Press freedom advocates", "Backing the outlets",
        k.p(C("Jameel Jaffer of the Knight First Amendment Institute: “The first amendment prohibits the president from "
              "punishing journalists because he doesn’t like their coverage.”", "ban",
              ["Jameel Jaffer, executive director at Knight First Amendment Institute at Columbia University",
               "“The first amendment prohibits the president from punishing journalists because he doesn’t like their coverage"]))))
    out.append("</ul></section>")

    # ---- context ----
    k.section = "Not the first time"
    out.append('<section aria-labelledby="s-ctx"><h2 id="s-ctx">' + k.note("Not the first time") + '</h2>')
    out.append(k.p(
        C("The Associated Press was banned from Oval Office and Air Force One pool events after it kept using “Gulf of "
          "Mexico” instead of “Gulf of America”. It sued, and that case is still going.", "ban",
          ["including the Associated Press, which was banned from press pool events in the Oval Office and on Air Force One after it continued to use Gulf of Mexico instead of Gulf of America in its coverage.",
           "The AP sued, and that case remains in litigation."]),
        C("Since 2025 the White House, not the correspondents’ association, has chosen which outlets join the pool each "
          "day.", "af1",
          "Since the beginning of Trump’s second administration in 2025, the White House has decided which outlets cover the president via the pool each day, a task previously coordinated by the White House Correspondents’ Association."),
        C("But the courts have sided with reporters before: in Trump’s first term, legal challenges won back the press "
          "badges of Jim Acosta, then of CNN, and Brian Karem, then of Playboy.", "sue",
          "past legal challenges that successfully returned the press badges of journalists Jim Acosta – then of CNN – and Brian Karem, then of Playboy magazine, during Trump’s first presidency.")))
    out.append("</section>")

    # ---- opinion ----
    k.section = "Opinion: should the press walk out?"
    out.append('<section aria-labelledby="s-op"><h2 id="s-op">' + k.note("Should the press walk out?") + '</h2>')
    out.append('<aside class="opinion" aria-label="Opinion">'
               f'<span class="tag">{k.note("Opinion")}</span>'
               f'<p class="by">{k.claims(C("Margaret Sullivan, Guardian US columnist", "sullivan", "Margaret Sullivan is a Guardian US columnist writing on media, politics and culture"), cite=False)}</p>'
               + k.p(C("Sullivan argues that suing is right but not enough. She wants the biggest newspapers and TV "
                       "networks to boycott the White House briefing room until their colleagues get their credentials "
                       "back, and says reporters can do the job from outside the building.", "sullivan",
                       ["The legal action is the right move, of course",
                        "But something else, beyond legal action, is necessary, too.",
                        "should take collective action by boycotting that briefing room and similar White House events until their journalistic colleagues get their credentials back.",
                        "reporters do not need to do their journalistic duty from inside the White House"]))
               + f'<blockquote class="pull">{k.claims(C("“And principle should trump access.”", "sullivan", "And principle should trump access."))}</blockquote>'
               + '</aside>')
    out.append(k.p(C("This is the only opinion piece in the Storyline. It has no piece arguing against a boycott.",
                     note="Framing text: describes the contents of the Storyline data.")))
    out.append("</section>")

    # ---- next ----
    k.section = "What happens next"
    out.append('<section aria-labelledby="s-next"><h2 id="s-next">' + k.note("What happens next") + '</h2>')
    out.append(k.p(
        C("The judge’s order runs for 14 days, and a hearing on a preliminary injunction is due within that time.", "dinner",
          ["issued an early morning order forcing the administration to return access for a 14-day period",
           "A hearing for a preliminary injunction will be expedited to be held during the 14-day period in which the passes are returned, the judge said."]),
        C("Trump has said the White House would appeal any ruling against it,", "dinner",
          "Trump already said in a post on Truth Social earlier this week that the White House would appeal any adverse ruling."),
        C("and on the day of the ban he said more outlets might follow: “There may be others to join them.”", "ban",
          "“There may be others to join them,” Trump said.")))
    out.append("</section>")
    return "\n".join(out)
