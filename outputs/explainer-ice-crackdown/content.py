"""Storyline explainer: ICE immigration enforcement crackdown.

Every C(text, source, support) ties a piece of on-page text to the passage in
the fetched Guardian article that supports it. Two articles could not be
fetched in full (see CHECKS); for those, only the headline and standfirst in
the Storylines data are used. Build with:
python3 outputs/explainer-kit/build.py outputs/explainer-ice-crackdown
"""
from build import C

DATA_FILE = "trump-administration.json"
STORYLINE_INDEX = 2
PAGE_TITLE = "ICE immigration enforcement crackdown: a Storylines explainer"
KICKER = "Trump administration"

SRC = {
    "cage": "us-news/2026/sep/14/alligator-alcatraz-immigration-jail-cages-report",
    "preg": "us-news/ng-interactive/2026/sep/15/ice-detention-miscarriages-pregnancy",
    "eg": "us-news/2026/sep/18/us-men-deported-hotel-equatorial-guinea",
    "miller": "us-news/2026/sep/19/stephen-miller-trump-migrant-children",
    "austin": "us-news/2026/sep/20/man-shot-ice-agent-austin-texas",
    "third": "us-news/2026/sep/21/what-is-trump-third-country-deportation-policy",
    "evan": "us-news/2026/sep/24/citizen-injured-ice-mistaken-fugitive-arrest",
}

THEME = """
--paper:#f3f1ee;--ink:#1b1e22;--muted:#5c5f63;--rule:#dad6d0;--card:#e8e4de;
--accent:#c4532f;--accent-strong:#a23f1f;--accent-ink:#fff;--chip:#1b1e22;--chip-ink:#f3f1ee;--focus:#2c63d6;
--hero-bg:#161a1e;--hero-bg-solid:#171b1f;--hero-ink:#f1eee9;--accent-on-hero:#f08a64;
--hero-glow:radial-gradient(55% 70% at 90% 5%,rgba(196,83,47,.45),transparent 60%),radial-gradient(60% 70% at 0% 110%,rgba(110,140,170,.35),transparent 60%);
--opinion-bg:#e8e3f6;--opinion-ink:#2f2357;
--s1:#c4532f;--s2:#7b4f96;--s3:#2c6a8a;--s4:#4f7036;
"""
THEME_DARK = """
--paper:#121417;--ink:#ebe8e3;--muted:#a3a5a8;--rule:#2a2d31;--card:#1c1f23;
--accent:#f08a64;--accent-strong:#f5a384;--accent-ink:#121417;--chip:#ebe8e3;--chip-ink:#121417;--focus:#86adff;
--s1:#f08a64;--s2:#c39be0;--s3:#79bde0;--s4:#a6cc85;
"""

DEK = [C("In September, Guardian reporting followed the Trump administration’s immigration crackdown "
         "through each stage: arrests on the street, detention, the courts, and removal to countries that are not "
         "people’s own.",
         note="Summary of the page’s structure. Each stage is sourced in full below.")]

CHECKS = [
    "**Two articles could not be fetched.** The Content API refused (\"not permitted to access this content via your "
    "current user tier\") for \"ICE agent shoots and wounds Venezuelan man at traffic stop in Austin, Texas\" and "
    "\"Revealed: ICE lost count of miscarriages, while detaining a record number of pregnant women\". For these, the page "
    "uses only the headline and standfirst from the Storylines data. The Austin shooting is also described in the Evanston "
    "article, which is the main source for it here. Both articles are linked in Read more.",
    "**Dates.** The Evanston article (published Thursday 24 September) says the three incidents happened \"on Sunday\", "
    "which was 20 September. The third-country explainer (published Monday 21 September) says the appeals court ruled "
    "\"on Friday\", which was 18 September. The beating in Equatorial Guinea is dated 11 September in the article itself.",
    "**Children's removal orders.** The Stephen Miller article gives \"almost 200,000\" children ordered removed in one "
    "place and \"more than 200,000\" in another. The page uses \"almost 200,000\", the first and more cautious figure. "
    "The monthly figures for June, July and August carry no year in the article; the page gives them as 2026 because the "
    "article, published in September 2026, describes \"a rapid increase over this spring and summer\" and a period of "
    "20 months from January 2025.",
    "**Evanston injuries.** Police said the man reported head, face and neck injuries; the mayor said he was treated for "
    "minor injuries. The page gives both, attributed. The article's own summary line says agents \"allegedly beat\" "
    "the man; the page does not use the word, and gives only what the witness saw (agents pinning him down, one "
    "with a knee on his back) and that agents \"reportedly\" mistook him for someone else.",
    "**Equatorial Guinea.** The account of the beating comes from witnesses and human rights lawyers, and is attributed "
    "to them.",
    "**Left out.** Detail from the Miller article on inter-agency practices (ICE officers at sponsorship appointments, "
    "sharing of children's files, military lawyers), from the Alligator Alcatraz report on food, water and phones, and "
    "the \"Office of Remigration\". All well sourced, but not needed for a five-minute read.",
    "**No opinion.** The Storyline has no opinion pieces. \"Where they stand\" sets the administration's statements "
    "against what others say, each attributed.",
    "**Multimedia.** The video of protests in Austin is linked by headline only.",
    "**Images.** None. The cage graphic is drawn to scale from the figures in the inspector general's report as "
    "reported by the Guardian (about 18 sq ft against a 37 sq ft minimum); the squares' areas are in that ratio.",
]

CSS = """
.flow{list-style:none;padding:0;margin-left:0;margin-right:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:.4rem;counter-reset:st}
.stage{background:var(--paper);border-radius:14px;padding:1rem 1rem 1.1rem;position:relative;border-top:6px solid var(--sc);
  counter-increment:st;display:flex;flex-direction:column}
.stage:not(:last-child)::after{content:"";position:absolute;right:-12px;top:2.2rem;width:12px;height:2px;background:var(--rule)}
.stage .sn{font:800 .7rem/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--sc)}
.stage h3{margin:.3rem 0 .6rem;font-size:1.15rem}
.stage .big{font:800 clamp(1.9rem,3.4vw,2.5rem)/1 var(--sans);letter-spacing:-.03em;color:var(--sc)}
.stage .cap{font:500 .86rem/1.4 var(--sans);margin:.35rem 0 .8rem;color:var(--ink)}
.stage ul{list-style:none;margin:auto 0 0;padding:.7rem 0 0;border-top:1px solid var(--rule)}
.stage li{margin:.35rem 0}
.stage li a{display:grid;grid-template-columns:3.3rem 1fr;gap:.4rem;font:600 .84rem/1.3 var(--sans);text-decoration:none}
.stage li a:hover span:last-child,.stage li a:focus-visible span:last-child{text-decoration:underline;text-decoration-color:var(--sc)}
.stage .dt{font-weight:800;color:var(--sc)}
.s1{--sc:var(--s1)}.s2{--sc:var(--s2)}.s3{--sc:var(--s3)}.s4{--sc:var(--s4)}
.ribbon{margin:.6rem 0 0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(9,minmax(0,1fr));gap:4px}
.ribbon li{border-top:5px solid var(--sc);padding:.45rem .35rem 0;font:600 .76rem/1.3 var(--sans)}
.ribbon b{display:block;font:800 .95rem/1.1 var(--sans)}
.ribbon-h{font:800 .78rem var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:1.4rem 0 0}
@media (max-width:860px){
  .flow{grid-template-columns:1fr 1fr}
  .stage:not(:last-child)::after{display:none}
  .ribbon{grid-template-columns:repeat(3,minmax(0,1fr))}
}
@media (max-width:520px){.flow{grid-template-columns:1fr}.ribbon{grid-template-columns:1fr}.ribbon li{display:grid;grid-template-columns:4rem 1fr;border-top:0;border-left:5px solid var(--sc);padding:.3rem .6rem}}
.stage-sec{scroll-margin-top:1rem}
.stage-sec h2::before{background:var(--sc)}
.cage{display:flex;gap:1.4rem;align-items:center;flex-wrap:wrap;margin:1.2rem 0 1.4rem;font:600 .88rem/1.35 var(--sans)}
.cage-key{list-style:none;margin:0;padding:0;max-width:14rem}
.cage-key li{margin:0 0 .9rem}
.cage .k37{color:var(--ink)}
.cage .sq{border:3px solid var(--ink);border-radius:3px}
.cage .sq.small{background:repeating-linear-gradient(90deg,var(--ink) 0 2px,transparent 2px 9px);border-color:var(--s2)}
.cage b{font:800 1.4rem/1 var(--sans);display:block;color:var(--s2)}
.bars{margin:1.2rem 0 1.4rem;font:600 .88rem/1.3 var(--sans)}
.bars .row{display:grid;grid-template-columns:7.2rem 1fr;gap:.7rem;align-items:center;margin:.35rem 0}
.bars .track{position:relative;height:1.7rem}
.bars .fill{position:absolute;inset:0 auto 0 0;background:var(--sc);border-radius:4px;transform-origin:left;
  animation:grow 1s cubic-bezier(.5,.1,.2,1) both}
.bars .val{position:absolute;top:50%;transform:translateY(-50%);font:800 .85rem var(--sans);white-space:nowrap;padding-left:.45rem}
.bars .gap{font:italic .8rem/1.3 var(--serif);color:var(--muted);padding:.2rem 0 .2rem 7.9rem}
.bars .outline{background:none;box-shadow:inset 0 0 0 2px var(--sc)}
.bars-h{font:800 1rem/1.3 var(--sans);margin:1.4rem 0 .2rem}
.bars-note{font:500 .82rem/1.4 var(--sans);color:var(--muted);margin:.4rem 0 0}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@media (max-width:520px){.bars .row{grid-template-columns:5.6rem 1fr}.bars .gap{padding-left:6.3rem}}
.sides{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1rem}
.sides>div{background:var(--card);border-radius:14px;padding:1.1rem 1.15rem}
.sides h3{margin:0 0 .6rem}
.sides ul{margin:0;padding:0;list-style:none;font-size:1rem;line-height:1.5}
.sides li{padding:.55rem 0;border-top:1px solid var(--rule)}
.sides li:first-child{border-top:0;padding-top:0}
@media (max-width:640px){.sides{grid-template-columns:1fr}}
"""


def flow(k):
    k.section = "Diagram: the system, stage by stage"
    stages = [
        ("s1", "arrest", "On the street",
         C("50,000", "evan", "resulted in a record 50,000 arrests in July alone"),
         C("arrests in July alone, a record", "evan", "resulted in a record 50,000 arrests in July alone"),
         [("20 Sept", C("US citizen hurt in arrest attempt, Evanston", "evan",
                        "An eyewitness has described how two federal immigration agents allegedly beat and badly injured a US citizen in a botched arrest attempt in Illinois")),
          ("20 Sept", C("ICE agent shoots man at traffic stop, Austin", "austin",
                        "ICE agent shoots and wounds Venezuelan man at traffic stop in Austin, Texas")),
          ("20 Sept", C("Man dies after reportedly fleeing officers, Michigan", "evan",
                        "In Michigan, authorities are investigating the death of a 36-year-old Guatemalan national who crashed his car into a tree at high speed after reportedly attempting to flee immigration officers"))]),
        ("s2", "detention", "In detention",
         C("79", "cage", "revealed 79 instances between July 2025 and January 2026 in which guards placed detainees in the metal cages"),
         C("times guards put Alligator Alcatraz detainees in small metal cages, July 2025 to January 2026", "cage",
           "revealed 79 instances between July 2025 and January 2026 in which guards placed detainees in the metal cages"),
         [("14 Sept", C("Guardian reports watchdog findings on cages at Alligator Alcatraz", "cage",
                        "Alligator Alcatraz held detainees in cages the size of phone booths, DHS watchdog says")),
          ("15 Sept", C("Guardian reveals ICE lost count of miscarriages", "preg",
                        "Revealed: ICE lost count of miscarriages, while detaining a record number of pregnant women"))]),
        ("s3", "courts", "In court",
         C("Almost 200,000", "miller", "Almost 200,000 children have been ordered removed from the US by immigration judges since Trump returned to the White House"),
         C("children ordered removed by immigration judges since Trump returned to office", "miller",
           "Almost 200,000 children have been ordered removed from the US by immigration judges since Trump returned to the White House"),
         [("19 Sept", C("Guardian reports Stephen Miller’s push to remove migrant children", "miller",
                        "Stephen Miller is leading an unprecedented and intense White House drive across a host of government departments to accelerate the removal of undocumented immigrant children from the US"))]),
        ("s4", "removal", "Sent away",
         C("25,000+", "third", "has deported more than 25,000 migrants, refugees and asylum seekers to countries that are not their own"),
         C("people deported to countries that are not their own since 2025", "third",
           "Since returning to office in 2025, Donald Trump’s administration has deported more than 25,000 migrants, refugees and asylum seekers to countries that are not their own."),
         [("11 Sept", C("Two deportees beaten in Equatorial Guinea, lawyers say", "eg",
                        ["Two men that the Trump administration expelled to Equatorial Guinea were bound, fitted with bags over their heads, beaten and pushed down a flight of stairs", "according to witnesses and human rights lawyers", "The beating, which occurred on 11 September"])),
          ("18 Sept", C("Appeals court rules third-country removals unlawful", "third",
                        "A US federal appeals court ruled on Friday that the Trump administration’s third-country removals policy was unlawful."))]),
    ]
    cards, dated = [], []
    for n, (cls, anchor, name, big, cap, items) in enumerate(stages, 1):
        k.record(big)
        k.record(cap)
        lis = []
        for when, c in items:
            k.record(c)
            lis.append(f'<li><a href="#{anchor}"><span class="dt">{when}</span><span>{c.text}</span></a></li>')
            dated.append((when, cls, c.text))
        cards.append(f'<li class="stage {cls}"><span class="sn">{k.note(f"Stage {n}")}</span><h3>{k.note(name)}</h3>'
                     f'<span class="big">{big.text}</span><p class="cap">{cap.text}</p><ul>{"".join(lis)}</ul></li>')
    k.record(C("Dates on the diagram", note="11 September is given in the Equatorial Guinea article. 14, 15, 19 and 21 September are "
               "the dates the Guardian published its reports, and the labels say so; the watchdog report's own "
               "publication date is not given. 20 September is derived from “on Sunday” in the Evanston article. "
               "18 September is derived from “on Friday” in the third-country explainer."))
    order = sorted(dated, key=lambda x: int(x[0].split()[0]))
    order.insert([i for i, x in enumerate(order) if x[0] == "20 Sept"][-1] + 1,
                 ("21 Sept", "s4", k.claims(C("Guardian explainer: the third-country deportation policy", "third",
                                               "What is Trump’s third-country deportation policy and whom does it target?"), cite=False)))
    rib = "".join(f'<li class="{cls}"><b>{w.replace(" Sept", "")}</b>{t}</li>' for w, cls, t in order)
    title = k.note("The system, stage by stage")
    sub = k.note("The reporting in this Storyline covers each step of the crackdown. Select an event to read about it below.")
    return (f'<figure class="panel wide" aria-labelledby="fl-h"><p class="panel-h" id="fl-h">{title}</p>'
            f'<p class="panel-sub">{sub}</p><ol class="flow">{"".join(cards)}</ol>'
            f'<p class="ribbon-h">{k.note("Events and Guardian reports in date order, September 2026")}</p>'
            f'<ol class="ribbon">{rib}</ol></figure>')


def body(k):
    out = []
    k.section = "In short"
    out.append('<section aria-labelledby="s-short"><h2 id="s-short">' + k.note("In short") + '</h2><ol class="inshort">')
    out.append("<li>" + k.claims(
        C("The Trump administration’s immigration crackdown has escalated with enforcement “surges” into "
          "Democratic-run cities and states, and resulted in a record 50,000 arrests in July alone. Much of it is "
          "carried out by Immigration and Customs Enforcement (ICE), which is overseen by the Department of Homeland "
          "Security.", "evan",
          ["Biss condemned Donald Trump’s immigration crackdown, which has escalated through the president’s second term with enforcement “surges” into Democratic-run cities and states in particular, and resulted in a record 50,000 arrests in July alone.",
           "The Department of Homeland Security (DHS), which oversees the Immigration and Customs Enforcement (ICE) agency"])) + "</li>")
    out.append("<li>" + k.claims(
        C("On a single Sunday, a US citizen was hurt near Chicago when agents reportedly mistook him for someone else, an ICE agent shot a man in "
          "Texas, and a man died in Michigan after reportedly trying to flee immigration officers.", "evan",
          ["The incident was one of three separate violent Sunday events involving federal immigration officers.",
           "US citizen injured after ICE agents reportedly mistook him for fugitive",
           "In Austin, Texas, an ICE agent shot and seriously wounded a 28-year-old Venezuelan man",
           "In Michigan, authorities are investigating the death of a 36-year-old Guatemalan national who crashed his car into a tree at high speed after reportedly attempting to flee immigration officers"])) + "</li>")
    out.append("<li>" + k.claims(
        C("Reports on the rest of the system found detainees held in metal cages,", "cage",
          "detainees at Florida’s “Alligator Alcatraz” federal immigration jail were frequently locked in outside metal cages no bigger than a phone booth"),
        C("court orders to remove children doubling,", "miller", "a doubling of such court orders since January 2025"),
        C("and two deportees in Equatorial Guinea beaten, according to witnesses and lawyers.", "eg",
          ["were bound, fitted with bags over their heads, beaten and pushed down a flight of stairs", "according to witnesses and human rights lawyers"])) + "</li></ol></section>")

    out.append(flow(k))

    def stage(anchor, cls, head, *parts):
        return (f'<section class="stage-sec {cls}" id="{anchor}" aria-labelledby="h-{anchor}">'
                f'<h2 id="h-{anchor}">{k.note(head)}</h2>{"".join(parts)}</section>')

    # ---- 1 street ----
    k.section = "1. On the street"
    out.append(stage("arrest", "s1", "1. On the street",
        k.p(C("On Sunday 20 September in Evanston, a suburb of Chicago, a witness saw two immigration agents pinning a "
              "Black man to the ground, one with a knee on his back, as the man shouted: “I’m a citizen, leave me "
              "alone.”", "evan",
              ["Bystander Ryan Garton told the Associated Press that he saw the agents pinning down the man, who is Black, on the side of the road as he was driving home on Sunday in Evanston, a suburb of Chicago.",
               "Garton, 56, said one agent had his knee on the man’s back and was “beating up on him”, even as the person shouted: “I’m a citizen, leave me alone.”"],
              note="Date: the article, published on Thursday 24 September 2026, says “on Sunday”."),
            C("He was a US citizen. Police said he told them he had head, face and neck injuries; the mayor said he was "
              "treated in hospital for minor injuries.", "evan",
              ["An eyewitness has described how two federal immigration agents allegedly beat and badly injured a US citizen",
               "A police statement said the alleged victim told officers he received head, face and neck injuries during the beating.",
               "the man was treated at St Francis hospital for minor injuries"])),
        k.p(C("The Department of Homeland Security, which oversees ICE, said officers had “encountered an individual who "
              "resembled the target” of an operation, and that he “was not cooperative and refused to identify "
              "himself”.", "evan",
              ["The Department of Homeland Security (DHS), which oversees the Immigration and Customs Enforcement (ICE) agency, said in a statement that ICE officers had “encountered an individual who resembled the target” of an enforcement operation.",
               "“The individual was given lawful commands but was not cooperative and refused to identify himself,”"])),
        k.p(C("The same day, in Austin, Texas, an ICE agent shot and seriously wounded a 28-year-old Venezuelan man at a "
              "traffic stop while he worked as a DoorDash delivery driver.", "evan",
              "In Austin, Texas, an ICE agent shot and seriously wounded a 28-year-old Venezuelan man in a traffic stop while he worked as a DoorDash delivery driver."),
            C("Protesters gathered at the scene to demand transparency.", "austin",
              "Anti-ICE protesters gather and demand transparency at site where 28-year-old was shot in torso"),
            C("In Michigan, authorities are investigating the death of a 36-year-old Guatemalan man who crashed his car "
              "into a tree at high speed after reportedly trying to flee immigration officers.", "evan",
              "In Michigan, authorities are investigating the death of a 36-year-old Guatemalan national who crashed his car into a tree at high speed after reportedly attempting to flee immigration officers that were trying to detain him."))))

    # ---- 2 detention ----
    k.section = "2. In detention"
    cage_label = k.claims(C("Two squares drawn to scale. The cage, about 18 square feet, is less than half the 37 square feet "
                            "ICE requires for a single-person space.", "cage",
                            "Each cage, the report noted, offered only about 18 sq ft of floor space, less than half the minimum 37 sq ft required for single-person spaces by ICE’s own published national detention standards."), cite=False)
    l18 = k.claims(C("18 sq ft", "cage", "Each cage, the report noted, offered only about 18 sq ft of floor space"), cite=False)
    t18 = k.claims(C("The cage (shaded)", "cage", "Each cage, the report noted, offered only about 18 sq ft of floor space"), cite=False)
    l37 = k.claims(C("37 sq ft", "cage", "less than half the minimum 37 sq ft required for single-person spaces by ICE’s own published national detention standards"), cite=False)
    t37 = k.claims(C("ICE’s own minimum for a single-person space (outline)", "cage", "less than half the minimum 37 sq ft required for single-person spaces by ICE’s own published national detention standards"), cite=False)
    cage = (f'<figure class="cage" role="img" aria-label="{cage_label}">'
            f'<div class="sq" style="width:9.4rem;height:9.4rem;display:flex;align-items:flex-end">'
            f'<div class="sq small" style="width:6.55rem;height:6.55rem;margin:-3px 0 -3px -3px"></div></div>'
            f'<ul class="cage-key" aria-hidden="true"><li><b>{l18}</b>{t18}</li><li><b class="k37">{l37}</b>{t37}</li></ul>'
            f'</figure>')
    out.append(stage("detention", "s2", "2. In detention",
        k.p(C("“Alligator Alcatraz”, an immigration jail in the Florida Everglades run by Governor Ron DeSantis’s "
              "administration for the federal government, closed in June after a year.", "cage",
              ["the controversial camp in the remote Florida Everglades",
               "Ron DeSantis, the Republican Florida governor whose administration ran Alligator Alcatraz on behalf of the federal government",
               "The notorious immigration jail closed in June after a year of operation"]),
            C("A report by the Department of Homeland Security’s own inspector general has now found that guards "
              "repeatedly locked detainees in outdoor metal cages, a practice it said “does not align with standards "
              "for humane treatment”.", "cage",
              ["detainees at Florida’s “Alligator Alcatraz” federal immigration jail were frequently locked in outside metal cages no bigger than a phone booth, according to a damning government watchdog report that said the practice “does not align with standards for humane treatment”",
               "the office of the inspector general of the Department of Homeland Security (DHS)"])),
        cage,
        k.p(C("Records showed 79 occasions from July 2025 to January 2026 when detainees were put in the cages, for up "
              "to two hours at a time. Staff called them “calming areas” and said detainees asked to spend time in them;", "cage",
              ["revealed 79 instances between July 2025 and January 2026 in which guards placed detainees in the metal cages for up to two hours at a time",
               "facility staff insisted they were used as “calming areas” for detainees",
               "“Staff further maintained that detainees asked to spend time” in them"]),
            C("inspectors found at least one case where a cage was used as punishment.", "cage",
              "inspectors found at least one time in which a cage was documented to have been used as a disciplinary tool"),
            C("DeSantis’s office had dismissed the claims as “fabrications” when Amnesty International first reported "
              "them. Responding to the report, its communications manager, Alex Lanfranconi, said the area “adheres to all federal standards for criminal "
              "confinement”, adding: “We’d make it even smaller if we could.”", "cage",
              ["dismissed the claims now confirmed by the DHS report as “fabrications”",
               "In a statement, Alex Lanfranconi, DeSantis’s communications manager, contended that",
               "“the leftwing media wants to focus on a confinement area” which “adheres to all federal standards for criminal confinement”",
               "His statement added: “We’d make it even smaller if we could.”",
               "the Guardian was the first to report an Amnesty International dossier"])),
        k.p(C("A separate Guardian investigation found that ICE was detaining a record number of pregnant women. ICE says "
              "it has no updated information on miscarriages after 3 October 2025. Lawmakers and lawyers have warned that "
              "pregnant detainees are not getting basic prenatal care.", "preg",
              ["Revealed: ICE lost count of miscarriages, while detaining a record number of pregnant women",
               "ICE says it has no updated information on the number of miscarriages after 3 October 2025. Lawmakers, advocates and immigration attorneys have raised alarms that pregnant detainees are not receiving basic prenatal care and screenings"]))))

    # ---- 3 courts ----
    k.section = "3. In court: the children"
    months = [("January 2025", 7366, C("7,366", "miller", "Removal orders rose from 7,366 a month in January 2025")),
              ("June 2026", 16200, C("16,200", "miller", "to 16,200 in June", note="Year derived: see Checks.")),
              ("July 2026", 16750, C("16,750", "miller", "16,750 in July", note="Year derived: see Checks.")),
              ("August 2026", 14744, C("14,744", "miller", "and 14,744 in August", note="Year derived: see Checks."))]
    rows = []
    for i, (lab, v, c) in enumerate(months):
        k.record(C(lab, note="Month as given in the article; year derived for June to August (see Checks)."))
        k.record(c)
        pct = v / 16750 * 84
        rows.append(f'<div class="row"><span>{lab}</span><span class="track"><span class="fill" style="width:{pct:.1f}%"></span>'
                    f'<span class="val" style="left:{pct:.1f}%">{c.text}</span></span></div>')
        if i == 0:
            rows.append(f'<p class="gap">{k.note("No monthly figures given for February 2025 to May 2026")}</p>')
    chart = (f'<figure class="bars s3" aria-labelledby="bh3"><p class="bars-h" id="bh3">{k.note("Children ordered removed from the US each month")}</p>'
             + "".join(rows)
             + f'<p class="bars-note">{k.claims(C("Source: analysis by the advocacy group Mobile Pathways of Justice Department immigration court data, shared with the Guardian.", "miller", "according to analysis of data from the Department of Justice’s executive office for immigration review (EOIR) conducted by the California-based advocacy Mobile Pathways and shared with the Guardian"))}</p></figure>')
    out.append(stage("courts", "s3", "3. In court: the children",
        k.p(C("Stephen Miller, the White House deputy chief of staff, who is seen as the mastermind and enforcer behind "
              "Trump’s anti-immigration agenda, is leading a drive across at least five government "
              "departments to speed up the removal of undocumented children, the Guardian has learned.", "miller",
              ["Miller is seen as the mastermind and enforcer behind Donald Trump’s hardline anti-immigration agenda",
               "As deputy chief of staff at the White House, focused on immigration policy",
               "Miller has harnessed personnel and power for his task from at least five cabinet-level government departments",
               "Stephen Miller is leading an unprecedented and intense White House drive across a host of government departments to accelerate the removal of undocumented immigrant children from the US"]),
            C("Almost 200,000 children have been ordered removed by immigration judges since Trump returned, and such "
              "orders have doubled since January 2025. Of the children ordered removed, 70% were under 13.", "miller",
              ["Almost 200,000 children have been ordered removed from the US by immigration judges since Trump returned to the White House, a doubling of such court orders since January 2025",
               "70% were under the age of 13"])),
        chart,
        k.p(C("Sources warned of a White House push to hurry children in large numbers, without lawyers, before asylum "
              "officers and immigration judges who are “either inclined or are under pressure to take a hard line”.", "miller",
              "hurrying them in vast numbers, without lawyers, in front of asylum officers and immigration judges who are either inclined or are under pressure to take a hard line and get them out of the US"),
            C("The White House did not deny that Miller is leading the effort but said it was not new, and framed it as "
              "an anti-trafficking effort: agencies are “working to locate and rescue these children”, a spokeswoman said.", "miller",
              ["The White House did not deny that Miller is orchestrating a multi-agency effort to speed up the removal of undocumented children but claimed the effort was not new.",
               "framed their endeavors as an anti-trafficking initiative instead of a means to enforcement",
               "are working to locate and rescue these children"]))))

    # ---- 4 removal ----
    k.section = "4. Sent away"
    pv = [("Cameroon", 1000, 44, C("Cameroon: $30m pledged to UN operations there for 1,000 people; 44 sent so far", "third",
                                   "$30m was earmarked for Cameroon, in order to support UN operations in the country, in return for accepting 1,000 migrants. The US has so far sent only 44.")),
          ("DR Congo", 2000, 15, C("Democratic Republic of the Congo: $50m pledged for 2,000 people; 15 received, and flights are on hold because of an Ebola outbreak", "third",
                                   "The Democratic Republic of the Congo was promised $50m towards UN operations there in return for accepting 2,000 migrants. It has only received 15, and flights to Kinshasa are on hold because of the country’s Ebola outbreak."))]
    rows = []
    for name, promised, sent, c in pv:
        k.record(c)
        rows.append(f'<p class="vh">{c.text}</p>'
                    f'<div class="row" aria-hidden="true"><span>{name}: deal</span><span class="track"><span class="fill outline" style="width:{promised / 2000 * 84:.0f}%"></span>'
                    f'<span class="val" style="left:{promised / 2000 * 84:.0f}%">{promised:,}</span></span></div>'
                    f'<div class="row" aria-hidden="true"><span>sent</span><span class="track"><span class="fill" style="width:{max(sent / 2000 * 84, .6):.1f}%"></span>'
                    f'<span class="val" style="left:{max(sent / 2000 * 84, .6):.1f}%">{sent}</span></span></div>')
    chart2 = (f'<figure class="bars s4" aria-labelledby="bh4"><p class="bars-h" id="bh4">{k.note("People each deal was meant to cover, and how many the US has sent")}</p>'
              + "".join(rows) + f'<p class="bars-note">{k.claims(C("Figures from internal state department records reviewed by the Washington Post as part of the Deportation Project.", "third", "according to internal records reviewed by the Washington Post as part of the Deportation Project"))}</p></figure>')
    out.append(stage("removal", "s4", "4. Sent away",
        k.p(C("US law bars sending people back to countries where they are likely to be persecuted. Human rights lawyers "
              "say the administration gets round this by deporting them to third countries instead, which often send "
              "them on to the places they fled.", "third",
              ["Human rights lawyers say the administration is using a loophole: under US law it is illegal to send people back to countries where they are likely to be persecuted, and so the Department of Homeland Security is deporting migrants and asylum seekers to third countries instead.",
               "In many cases, however, the receiving countries then deport them onwards to the very place they fled."]),
            C("The US has struck 35 such deals and pledged at least $410m. About 20,000 people have been bussed to Mexico "
              "and at least 5,000 flown elsewhere.", "third",
              ["The Trump administration has struck 35 deals",
               "The US has pledged at least $410m (£307m) to secure such agreements with 35 countries",
               "About 20,000 people have been bussed to Mexico, while at least 5,000 more have been put on planes to countries in Latin America, Africa, central Asia and the Caribbean."])),
        chart2,
        k.p(C("Equatorial Guinea has taken at least 66 people, and received $7.5m. About 30 are held in a run-down hotel "
              "near Malabo.", "eg",
              ["The US has sent at least 66 people from different African countries, Cuba and Brazil to Equatorial Guinea, which has received $7.5m as part of a deal",
               "About 30 detainees from the US remain trapped at a hotel in the outskirts of the coastal city of Malabo",
               "a run-down establishment that has served as a detention center for US deportees"]),
            C("On 11 September, according to witnesses and human rights lawyers, two of them, Ahmed Soliman, 31, from "
              "Egypt, and Samson Birhane, 47, from Eritrea, were bound, had bags put over their heads, and were beaten "
              "and pushed down a flight of stairs. They were taken to a prison. US judges had ruled that both would face "
              "persecution or torture if sent home.", "eg",
              ["The beating, which occurred on 11 September",
               "Two men that the Trump administration expelled to Equatorial Guinea were bound, fitted with bags over their heads, beaten and pushed down a flight of stairs, all in plain view of other US deportees, according to witnesses and human rights lawyers.",
               "Ahmed Soliman, 31, of Egypt, and Samson Birhane, 47, of Eritrea – have since been transferred to a prison in Malabo",
               "a judge had determined he would face persecution and torture if he were to return to Egypt due to his sexuality",
               "He was allowed to remain in the US after a judge ruled he faced torture in Eritrea"]),
            C("ICE said: “When an individual is no longer in ICE custody, ICE is no longer responsible for them.”", "eg",
              "“when an individual is no longer in ICE custody, ICE is no longer responsible for them”")),
        k.p(C("On Friday 18 September a federal appeals court ruled unanimously that the third-country policy was "
              "unlawful, because people were not given enough notice or the chance to challenge their removal. The "
              "government has 90 days to appeal and is expected to. The Department of Homeland Security’s general "
              "counsel said: “The third country deportation policy continues.”", "third",
              ["A US federal appeals court ruled on Friday that the Trump administration’s third-country removals policy was unlawful. A three-judge panel unanimously agreed that the policy violated due process by failing to give people enough notice of the decision to deport them, or the chance to legally contest it.",
               "But the government has 90 days to appeal against the court’s decision, and is expected to do so.",
               "“The third country deportation policy continues,” James Percival, the Department of Homeland Security’s general counsel, said in a statement."],
              note="Date: the article, published on Monday 21 September 2026, says the court ruled “on Friday”, which was 18 September."))))

    # ---- sides ----
    k.section = "Where they stand"
    admin = [
        C("The White House says agencies are “working to locate and rescue” migrant children and reunite them with "
          "their families in their home countries.", "miller",
          "“The Department of Homeland Security, the US Department of Health and Human Services, and the Homeland Security Council are working to locate and rescue these children. We are ensuring these children are reunited with their parents and families in their home countries,” said White House spokeswoman Lauren Bis."),
        C("The administration says its deportation drive focuses on removing criminals.", "third",
          "The Trump administration says its deportation drive is focusing on removing criminals from the US."),
        C("ICE says of those sent to Equatorial Guinea: “All of these illegal aliens were deported to a safe third country.”", "eg",
          "“All of these illegal aliens were deported to a safe third country.”"),
    ]
    critics = [
        C("Senator Ron Wyden, a Democrat: “The Trump administration has sacrificed every element of ORR’s child welfare "
          "mission on the altar of higher deportation numbers.” (ORR, the Office of Refugee Resettlement, is part of the "
          "health department and cares for children who arrive alone.)", "miller",
          ["“The Trump administration has sacrificed every element of ORR’s child welfare mission on the altar of higher deportation numbers,” US senator Ron Wyden, an Oregon Democrat, told the Guardian.",
           "HHS’s office of refugee resettlement (ORR)",
           "unaccompanied children are supposed to be quickly transferred from that department’s agencies into the custody of ORR"]),
        C("People deported to third countries whom the Guardian interviewed said they had no criminal histories.", "third",
          "The state department claims that its priority is to deport people with criminal histories, but people interviewed by the Guardian said they had none."),
        C("Amnesty International USA said the report on Alligator Alcatraz showed “the horrific treatment of people "
          "detained at Alligator Alcatraz was real, not a hoax”.", "cage",
          "“The findings confirm what we documented months ago: the horrific treatment of people detained at Alligator Alcatraz was real, not a hoax, as Trump administration officials were on the record saying."),
        C("Daniel Biss, the Democratic mayor of Evanston: “This violence must end.”", "evan",
          ["Daniel Biss, the Democratic mayor of Evanston", "“This violence must end."]),
    ]
    a = "".join(f"<li>{k.claims(c)}</li>" for c in admin)
    cr = "".join(f"<li>{k.claims(c)}</li>" for c in critics)
    out.append('<section aria-labelledby="s-sides"><h2 id="s-sides">' + k.note("Where they stand") + '</h2>'
               + k.p(C("The Storyline has no opinion pieces. These are the positions of the people quoted in its reporting.",
                       note="Describes the contents of the Storyline data."))
               + f'<div class="sides"><div><h3>{k.note("What the administration says")}</h3><ul>{a}</ul></div>'
               f'<div><h3>{k.note("What others say")}</h3><ul>{cr}</ul></div></div></section>')
    return "\n".join(out)
