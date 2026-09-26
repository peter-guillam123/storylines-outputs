"""Storyline explainer: US-Iran war and Hormuz negotiations.

Every C(text, source, support) ties a piece of on-page text to the passage in
the fetched Guardian article that supports it. Build with:
python3 outputs/explainer-kit/build.py outputs/explainer-iran-hormuz
"""
from build import C

DATA_FILE = "trump-administration.json"
STORYLINE_INDEX = 1
PAGE_TITLE = "US-Iran war and Hormuz negotiations: a Storylines explainer"
KICKER = "Trump administration"

SRC = {
    "mahdawi": "commentisfree/2026/sep/14/iran-war-trump-semantics",
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
--opinion-bg:#e8e3f6;--opinion-ink:#2f2357;
--sea:#1b7f8c;--sea-soft:#cfe6e8;--us:#0f1d20;--iran:#1b7f8c;
"""
THEME_DARK = """
--paper:#0c1618;--ink:#e6eeec;--muted:#9fb0b4;--rule:#1f2e31;--card:#142326;
--accent:#f2a950;--accent-strong:#f6bd74;--accent-ink:#0c1618;--chip:#e6eeec;--chip-ink:#0c1618;--focus:#7fb4ff;
--opinion-bg:#1e1a33;--opinion-ink:#d8ccff;
--sea:#4fc3cf;--sea-soft:#133a3f;--us:#e6eeec;--iran:#4fc3cf;
"""

DEK = [C("The US has been at war with Iran since February.", "un",
         "since the US and Israel launched joint strikes in February"),
       C("Now Iran is offering to reopen a vital oil route within days, on terms that would require difficult "
         "concessions from Donald Trump.", "choices",
         ["Iran’s seven-day timetable to reopen the strait of Hormuz and start talks on its nuclear programme has been pitched as a deal that could rapidly extricate Donald Trump from a political crisis but requires the US president to make difficult concessions."])]

CHECKS = [
    "**Start of the war.** The UN speech article says the US and Israel \"launched joint strikes in February\" but gives no "
    "year. The page says \"February\" only.",
    "**Six days or seven?** Iran's offer is reported both as opening the strait \"in six days\" (headline, 24 September) and "
    "\"within seven days\" (Araghchi, same article). The 25 September article explains the timetable: the strait reopens on "
    "day six and nuclear talks begin on day seven. The diagram follows that article.",
    "**Oil prices.** The articles give Brent crude at $64 a barrel before the fighting and $103 \"at its peak\" (the CBO "
    "article, 15 September), below $100 on 23 September and about $107 on 24 September. The $103 peak conflicts with the "
    "later $107 figure, probably because the CBO report covered an earlier period, but the article does not say. The page "
    "uses only the $64 and $107 figures, each dated and cited, and does not use the word \"peak\".",
    "**Minab school strike.** The CBO article says the strike on the first day of the war killed 156 people including 120 "
    "children. Arwa Mahdawi's column describes a school strike \"in March\" that killed 150 people including 120 children. "
    "The two also conflict on timing: the war began in February, according to the UN speech article, so \"the first day "
    "of the war\" and \"in March\" cannot both be right. The page uses the news article's figures, says only \"on the "
    "war's first day\" without a month, places it under 15 September (when the Guardian reported it), and does not say "
    "who carried out the strike, because the article only says the Pentagon has an internal investigation.",
    "**The talks in New York.** The 23 September article does not say which day the three-hour talks took place. The page "
    "dates them as reported on 23 September.",
    "**Patrick Wintour's analysis.** The 25 September article is analysis. Judgments in it (for example, that ending "
    "Israel's attacks in Lebanon is \"probably most difficult of all\") are attributed to him.",
    "**Left out.** The UN speech article's material on Greenland, Cuba, Venezuela, Ukraine and AI; the 23 September "
    "article's material on Gaza and speeches by Emmanuel Macron and King Abdullah; the grounding of Iran's civil aircraft; "
    "and the Pentagon inspector general's figures. All are relevant but not needed for a five-minute read.",
    "**Opinion.** Arwa Mahdawi's column is the only opinion piece. It is labelled as opinion, and quotes from Trump and "
    "JD Vance that appear only in her column are introduced as quoted by her.",
    "**Images.** None. The page uses type, colour and a diagram only.",
]

CSS = """
.tt{display:grid;grid-template-columns:5fr 1.35fr 1.35fr;gap:6px;margin:.4rem 0 0}
.tt button{all:unset;box-sizing:border-box;cursor:pointer;border-radius:12px;padding:.8rem .8rem .9rem;
  background:var(--paper);box-shadow:inset 0 0 0 2px var(--rule);font-family:var(--sans);min-width:0;position:relative}
.tt button:focus-visible{outline:3px solid var(--focus);outline-offset:3px}
.tt button[aria-pressed=true]{background:var(--ink);color:var(--paper);box-shadow:none}
.tt .dl{display:block;font:800 .72rem/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;opacity:.7}
.tt .dt{display:block;font:800 1.05rem/1.2 var(--sans);margin-top:.35rem}
.tt .who{display:inline-block;margin-top:.5rem;font:700 .66rem/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;
  padding:.3rem .45rem;border-radius:4px;background:var(--sea-soft);color:var(--ink)}
.tt button[aria-pressed=true] .who{background:var(--accent);color:var(--accent-ink)}
.ticks{display:grid;grid-template-columns:repeat(7,1fr);margin:.5rem 0 0;padding:0;list-style:none;
  font:700 .7rem var(--sans);color:var(--muted);text-align:center}
.ticks li{border-top:2px solid var(--rule);padding-top:.3rem}
.ticks li.hot{border-color:var(--accent);color:var(--ink)}
.tt-detail{margin-top:1rem;background:var(--paper);border-radius:14px;padding:1.1rem 1.2rem}
.tt-detail h3{margin:0 0 .5rem}
.tt-detail ul{margin:.2rem 0 .8rem;padding-left:1.2rem}
.tt-detail li{margin:.25rem 0}
.snag{border-left:4px solid var(--accent);padding:.1rem 0 .1rem .8rem;margin:.6rem 0 0}
.snag strong{font-family:var(--sans)}
.cmp{margin-top:1.6rem}
.cmp-h{font:800 1rem/1.3 var(--sans);margin:0 0 .6rem}
.bar{display:grid;grid-template-columns:9.5rem 1fr;gap:.8rem;align-items:center;margin:.45rem 0;font:600 .9rem/1.3 var(--sans)}
.bar .track{height:1.9rem;border-radius:6px;background:var(--paper);position:relative;overflow:hidden}
.bar .fill{position:absolute;inset:0 auto 0 0;border-radius:6px;display:flex;align-items:center;justify-content:flex-end;
  padding-right:.5rem;font:800 .85rem var(--sans);color:var(--paper);background:var(--muted);transform-origin:left;
  animation:grow 1.1s cubic-bezier(.5,.1,.2,1) both}
.bar .fill.new{background:var(--accent);color:var(--accent-ink);min-width:3.2rem}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@media (max-width:600px){
  .tt{grid-template-columns:1fr 1fr}
  .tt button:first-child{grid-column:1/-1}
  .ticks{display:none}
  .bar{grid-template-columns:1fr;gap:.25rem}
}
.basics{display:grid;grid-template-columns:repeat(auto-fit,minmax(11.5rem,1fr));gap:.8rem;margin-top:1rem}
.basics .card{font-size:.95rem}
.basics .card{border-top-color:var(--sea)}
.table-list{list-style:none;margin:1rem 0 0;padding:0}
.table-list li{display:grid;grid-template-columns:8.5rem 1fr;gap:1rem;padding:.75rem 0;border-top:1px solid var(--rule);font-size:1rem;line-height:1.5}
.table-list li strong{font:800 .95rem/1.4 var(--sans)}
@media (max-width:600px){.table-list li{grid-template-columns:1fr;gap:.1rem}}
"""

JS = """
(function(){
  var btns=[].slice.call(document.querySelectorAll('.tt button'));
  var panes=[].slice.call(document.querySelectorAll('.tt-detail'));
  if(!btns.length) return;
  function show(i){
    btns.forEach(function(b,j){b.setAttribute('aria-pressed', i===j ? 'true':'false');});
    panes.forEach(function(p,j){p.hidden = i!==j;});
    document.querySelectorAll('.ticks li').forEach(function(t){
      var d=+t.dataset.d; t.classList.toggle('hot', i===0 ? d<=5 : d===i+5);});
  }
  btns.forEach(function(b,i){b.addEventListener('click',function(){show(i);});});
  show(0);
})();
"""


def timetable(k):
    k.section = "Diagram: Iran’s seven-day timetable"
    steps = [
        ("Days 1 to 5", "The US acts", "US",
         [C("Lift the naval blockade on Iran’s oil ports", "choices",
            "the US would have to lift the naval blockade on Iran’s oil ports"),
          C("Restore the waiver that lifted sanctions on Iran’s oil exports", "choices",
            "restore the waiver that lifted sanctions on Iran’s oil exports"),
          C("End the war on all fronts", "choices", "end the war on all fronts"),
          C("Allow the release of some of Iran’s frozen assets", "choices",
            "permit the release of some of Iran’s frozen assets")],
         [C("Patrick Wintour writes that the hardest step for Trump is probably ordering Benjamin Netanyahu to end "
            "Israel’s attacks on Hezbollah in Lebanon.", "choices",
            "probably most difficult of all, order Benjamin Netanyahu to end Israel’s attacks on Hezbollah in Lebanon"),
          C("Iranian diplomats say a deal would be feasible if Trump could rein in Netanyahu in Lebanon.", "choices",
            "Other Iranian diplomats say Trump’s willingness to rein in Netanyahu in Lebanon remains key. If he could do that, a deal would be feasible.")]),
        ("Day 6", "The strait reopens", "Iran",
         [C("Iran reopens the strait of Hormuz", "choices", "On the sixth day, the strait of Hormuz would be reopened by Iran"),
          C("Ships use a new route designated by Oman and Iran", "choices",
            "with ships using a new route designated by Oman and Iran")],
         [C("The new route runs mainly through Iranian waters. Wintour writes that the strait would reopen largely on "
            "Iran’s terms.", "choices",
            "It is a difficult deal for Trump to swallow since the strait would reopen largely on Iran’s terms, with the new route predominantly going through Iranian waters."),
          C("Saudi Arabia is concerned that the route deal is between Iran and Oman only, without the other Gulf states as "
            "joint signatories.", "choices",
            "Saudi Arabia is also concerned that the route deal is bilateral between Iran and Oman, and not with the Gulf states as joint signatories.")]),
        ("Day 7", "Nuclear talks begin", "Both",
         [C("Talks start on the future of Iran’s civil nuclear programme", "choices",
            "negotiations would start on the future of Iran’s civil nuclear programme"),
          C("Including a protocol to let UN nuclear inspectors back in to Iran’s damaged sites and its stockpile of highly "
            "enriched uranium", "choices",
            "including a protocol to allow UN nuclear inspectors back in to look at Iran’s damaged sites and the stockpile of highly enriched uranium")],
         [C("Under the June agreement, these talks would not have started for 60 days.", "offer",
            "Talks on the nuclear program under the MoU would not have started for 60 days.")]),
    ]
    btns, panes = [], []
    for i, (label, title, who, items, snags) in enumerate(steps):
        k.note(label)
        btns.append(f'<button type="button" aria-pressed="{"true" if i == 0 else "false"}" aria-controls="tt{i}">'
                    f'<span class="dl">{label}</span><span class="dt">{k.note(title)}</span>'
                    f'<span class="who">{k.note({"US": "Up to the US", "Iran": "Up to Iran"}.get(who, "Both sides"))}</span></button>')
        lis = "".join(f"<li>{k.claims(c)}</li>" for c in items)
        sn = k.p(*snags)
        panes.append(f'<div class="tt-detail" id="tt{i}" role="region" aria-label="{label}: {title}">'
                     f'<h3>{label}: {title}</h3><ul>{lis}</ul>'
                     f'<div class="snag"><strong>{k.note("The catch")}</strong> {sn}</div></div>')
    ticks = "".join(f'<li data-d="{d}">{d}</li>' for d in range(1, 8))
    k.note("Days 1 to 7")
    cmp_h = k.note("When would nuclear talks begin?")
    bars = (f'<div class="bar"><span>{k.claims(C("June agreement", "choices", "from 60 days in the June agreement to seven"), cite=False)}</span>'
            f'<span class="track"><span class="fill" style="width:100%">{k.claims(C("Day 60", "choices", "from 60 days in the June agreement"), cite=False)}</span></span></div>'
            f'<div class="bar"><span>{k.claims(C("Iran’s new offer", "choices", "to seven"), cite=False)}</span>'
            f'<span class="track"><span class="fill new" style="width:{7 / 60 * 100:.1f}%">{k.claims(C("Day 7", "choices", "This accelerates the point at which nuclear talks would begin, from 60 days in the June agreement to seven.", note="“Seven” is shown as the figure 7."), cite=False)}</span></span></div>')
    title = k.note("Iran’s seven-day timetable")
    sub = k.claims(
        C("Iran’s offer, as reported by the Guardian from New York on 25 September.", "choices",
          "Iran’s seven-day timetable to reopen the strait of Hormuz and start talks on its nuclear programme",
          note="The article was published on 25 September 2026 with the dateline New York."),
        C("A Guardian headline the day before described it as opening the strait “in six days”:", "offer",
          "Iran awaiting response from Trump on proposal to open strait of Hormuz in six days"),
        C("the strait reopens on day six and nuclear talks follow on day seven.", "choices",
          ["On the sixth day, the strait of Hormuz would be reopened by Iran", "And on the next day, negotiations would start"]),
        C("Select a stage to see what it involves.", note="Instruction to the reader."), cite=False)
    return (f'<figure class="panel wide" aria-labelledby="tt-h"><p class="panel-h" id="tt-h">{title}</p>'
            f'<p class="panel-sub">{sub}</p>'
            f'<div class="tt">{"".join(btns)}</div><ol class="ticks" aria-hidden="true">{ticks}</ol>'
            f'{"".join(panes)}'
            f'<div class="cmp"><p class="cmp-h">{cmp_h}</p>{bars}</div></figure>')


def body(k):
    out = []
    k.section = "In short"
    out.append('<section aria-labelledby="s-short"><h2 id="s-short">' + k.note("In short") + '</h2><ol class="inshort">')
    out.append("<li>" + k.claims(
        C("The US and Israel launched joint strikes on Iran in February.", "un",
          "since the US and Israel launched joint strikes in February"),
        C("Since early in the war Iran has had a stranglehold on energy shipping through the strait of Hormuz,", "un",
          "Iran has maintained a stranglehold over energy shipping through the strait of Hormuz since early in the war"),
        C("and reopening it is expected to relieve pressure on global energy markets.", "choices",
          "the proposed reopening of the strait, which is expected to relieve pressure on global energy markets")) + "</li>")
    out.append("<li>" + k.claims(
        C("The war is hugely unpopular in the US, the Guardian reports.", "talks",
          "a hugely unpopular war that the Americans think they are losing"),
        C("Congress’s budget office puts the cost at $38bn or more, and the House of Representatives has voted three "
          "times to end it.", "house",
          ["The US House of Representatives has voted for a third time to end the war in Iran",
           "a Congressional Budget Office (CBO) report showed the conflict had cost at least $38bn"])) + "</li>")
    out.append("<li>" + k.claims(
        C("During the UN general assembly in New York, Iran offered to reopen the strait within days if the US makes "
          "big concessions, including an end to the fighting in Lebanon. Iran is waiting for Trump’s answer.", "offer",
          ["Iran said it has told Donald Trump it is willing to open the strait of Hormuz in six days",
           "so long as the US lifts sanctions on Iran’s oil exports in return, ends the war on all fronts – including in Lebanon – and releases some of Iran’s frozen assets",
           "Abbas Araghchi, the Iranian foreign minister, said he was waiting to hear a response from the Americans to the proposal."])) + "</li></ol></section>")

    # ---- basics ----
    k.section = "The basics"
    out.append('<section aria-labelledby="s-basics"><h2 id="s-basics">' + k.note("The basics") + '</h2><div class="basics">')
    out.append('<div class="card"><h3>' + k.note("What is the strait of Hormuz?") + '</h3>' + k.p(
        C("A key waterway for transporting oil.", "talks", "a key waterway for transporting oil"),
        C("Oman lies on its south side.", "choices", "Oman, located on the south side of the strait"),
        C("The latest published figures suggest fewer than five identifiable tankers a day are getting through, though "
          "US navy estimates are much higher.", "talks",
          "Latest published figures suggest the number of identifiable tankers making it through the strait is fewer than five a day, but estimates of the US navy are much higher.")) + '</div>')
    out.append('<div class="card"><h3>' + k.note("What was the June deal?") + '</h3>' + k.p(
        C("On 17 June the US and Iran agreed a memorandum of understanding.", "talks",
          "He has said the memorandum of understanding (MoU), agreed with the US on 17 June, remained the starting point."),
        C("Trump signed it.", "offer", "the Islamabad memorandum of understanding that was signed by Trump"),
        C("Its implementation fell apart after each side accused the other of breaking it by trying to take control of "
          "the strait, though Iran’s president says it remains the starting point.", "talks",
          ["Implementation of the MoU fell apart after the two sides accused one another of breaching its terms by trying to take control of the strait.",
           "He has said the memorandum of understanding (MoU), agreed with the US on 17 June, remained the starting point."])) + '</div>')
    out.append('<div class="card"><h3>' + k.note("How is the US squeezing Iran?") + '</h3>' + k.p(
        C("Through sanctions and a naval blockade that makes it nearly impossible for Iran to export oil, depriving it "
          "of badly needed foreign currency.", "talks",
          "Iran is under ever more intense pressure from sanctions, and a US naval blockade is making it nearly impossible for Iran to export oil, depriving the country of badly needed foreign currency.")) + '</div>')
    out.append('</div></section>')

    # ---- chronology ----
    k.section = "What happened, in order"
    out.append('<section aria-labelledby="s-chron"><h2 id="s-chron">' + k.note("What happened, in order") + '</h2><ol class="chron">')

    def entry(when, small, head, *paras, note):
        k.record(C(f"{small} {when}".strip(), note=note))
        return (f'<li><div class="when"><small>{small}</small>{when}</div>'
                f'<div class="what"><h3>{k.note(head)}</h3>{"".join(paras)}</div></li>')

    out.append(entry("February", "", "The war begins",
        k.p(C("The US and Israel launched joint strikes on Iran.", "un",
              "since the US and Israel launched joint strikes in February"),
            ),
        note="The UN speech article dates the joint strikes to “February” without a year."))

    out.append(entry("June–July", "", "A deal, and votes to end the war",
        k.p(C("The US and Iran agreed a memorandum of understanding on 17 June; its implementation later fell apart.", "talks",
              ["agreed with the US on 17 June", "Implementation of the MoU fell apart"]),
            C("In June and July the House passed resolutions to end US action in Iran.", "house",
              "The House first approved a war powers resolution in June and followed up with another one in July, all seeking to halt US action in Iran.")),
        note="Months as given in the articles."))

    out.append(entry("15 Sept", "Tuesday", "The bill arrives",
        k.p(C("A Congressional Budget Office report put the cost of the war at $38bn or more, and estimated it would grow "
              "by $3bn for every month it continues, depending on its intensity. Defending against Iranian missiles and "
              "drones has used up so many interceptor missiles that rebuilding the stockpile “would probably take at "
              "least five years, even if production was increased”, the CBO said.", "house",
              ["showed the conflict had cost at least $38bn",
               "It estimated that the costs of the war will grow $3bn for every month the conflict continues, depending on its intensity",
               "Fending off Iranian ballistic missiles and drones has consumed such a large share of the US stockpile of Patriot, Thaad and navy interceptors that the CBO said rebuilding it “would probably take at least five years, even if production was increased”."]),
            C("A few hours after the report, the House voted 220 to 204 to end the war, its third such vote.", "house",
              ["approving a war powers resolution a few hours after a Congressional Budget Office (CBO) report",
               "The final tally of 220-204 was similar to earlier votes"]),
            C("In a White House statement responding to reports of shortages, Trump said the US had “far more munitions "
              "than anyone in the world”.", "house",
              "In a White House statement responding to reports of shortages, Donald Trump said the US had “far more munitions than anyone in the world”")),
        k.p(C("None of the House resolutions has "
              "reached the president, who would almost certainly veto them.", "house",
              [
               "None of the resolutions have made it to the president’s desk, where Trump would almost certainly veto them."]),
            C("Earlier, the Senate also passed one, on its 10th attempt, but Republican senators reversed course the next day after "
              "Trump berated them.", "house",
              "The Senate on its 10th try also approved a war powers resolution to end the conflict, but Republican senators quickly reversed course the next day after Trump berated them during a closed-door lunch.")),
        k.p(C("The Pentagon’s own review of the war, released the day before, did not address its internal investigation "
              "into a strike on a school in Minab on the war’s first day, which killed 156 people, including 120 children.", "house",
              ["The economic report came a day after the Pentagon’s inspector general finally released its own first review of the war",
               "The Pentagon’s report did not address its own internal investigation of the Minab school strike on the first day of the war, which killed 156 people including 120 children."])),
        note="Date: the article, published on 15 September 2026, says the vote was “late on Tuesday”; 15 September 2026 was a Tuesday."))

    out.append(entry("22 Sept", "Tuesday", "Trump at the UN",
        k.p(C("In a speech to the UN general assembly, Trump said: “I call on all nations to help to enforce the complete "
              "economic isolation of Iran.” He said he had a “big decision” to make: a deal, or “do I annihilate the "
              "Islamic republic and do it quickly”.", "un",
              ["“I call on all nations to help to enforce the complete economic isolation of Iran,” Trump said in a speech to the UN general assembly on Tuesday.",
               "“I have a big decision to make: will a deal be made with Iran that let them rebuild and create a far greater country than ever was before,” he said. “Or do I annihilate the Islamic republic and do it quickly, never giving them a chance to kill or destroy people and continents?”"]),
            C("He said the midterm elections would not affect his decisions: “The only thing that does is that Iran will "
              "never have a nuclear weapon.”", "un",
              ["said the midterm elections would have absolutely no influence on his decision-making around the conflict",
               "The only thing that does is that Iran will never have a nuclear weapon."])),
        note="Date: the article, published on 22 September 2026, says the speech was “on Tuesday”."))

    out.append(entry("23 Sept", "Reported", "Talks in a UN room",
        k.p(C("Iran’s foreign minister, Abbas Araghchi, met Trump’s envoys Steve Witkoff and Jared Kushner for three "
              "hours at the UN headquarters, with Qatar mediating. Trump said the talks had been very productive, and "
              "the price of Brent crude oil fell below $100 a barrel for the first time in two weeks.", "talks",
              ["in surprise talks held in New York under the mediation of Qatar between Tehran’s foreign minister, Abbas Araghchi, and Donald Trump’s envoys Steve Witkoff and Jared Kushner",
               "Trump said the three-hour talks held in a room at the UN headquarters had gone very well and been very productive.",
               "which led to the price of a barrel of Brent crude to fall to below $100 (£75) for the first time in two weeks"]),
            C("Iran denied it had dropped its conditions. Its foreign ministry said the aim was to convey demands "
              "including “the end of the war in all its dimensions”.", "talks",
              ["Iran has pushed back on claims that it dropped former preconditions for reopening the strait of Hormuz",
               "This interaction was aimed at conveying Iran’s conditions, including the end of the war in all its dimensions"])),
        note="The article, published on 23 September 2026, does not give the day of the talks."))

    out.append(entry("24 Sept", "Thursday", "Iran’s offer",
        k.p(C("Iran said it had told Trump it would reopen the strait and start nuclear talks within a week if the US "
              "met its conditions. “We have introduced a plan to the US through the mediators,” Araghchi said.", "offer",
              ["Iran said it has told Donald Trump it is willing to open the strait of Hormuz in six days, and to start talks on its nuclear program the day after",
               "“We have introduced a plan to the US through the mediators that if certain conditions are met, the strait will be open within seven days and talks will start.”"]),
            C("Saudi Arabia had been expected to endorse the new shipping route the week before but pulled back, partly out of anger at "
              "attacks on it by the Iranian-backed Houthis in Yemen.", "offer",
              "Saudi Arabia had been expected to endorse the Oman-Iran route through the strait last week, but pulled back partly due to anger that Iranian-backed Houthis had started attacking Saudi Arabia"),
            C("Brent crude was trading at about $107 a barrel,", "offer",
              "Brent crude was trading at about $107 (£81) a barrel on Thursday."),
            C("against $64 before the fighting.", "house", "Brent crude jumped from $64 a barrel before the fighting",
              note="Pre-war price from the CBO article; see Checks on oil prices.")),
        note="Date: the article, published on 24 September 2026, gives the oil price “on Thursday”; 24 September 2026 was a Thursday."))
    out.append("</ol></section>")

    out.append(timetable(k))

    # ---- positions ----
    k.section = "Who’s who, and where they stand"
    out.append('<section aria-labelledby="s-who"><h2 id="s-who">' + k.note("Who’s who, and where they stand") + '</h2><ul class="cards">')

    def card(name, role, *paras):
        return f'<li class="card"><h3>{k.note(name)}</h3><p class="role">{k.note(role)}</p>{"".join(paras)}</li>'

    out.append(card("Donald Trump", "US president",
        k.p(C("Says he must choose between a deal and whether to “annihilate the Islamic republic”, and that the only "
              "thing on his mind is that “Iran will never have a nuclear weapon”.", "un",
              ["Or do I annihilate the Islamic republic and do it quickly",
               "“It doesn’t even enter my mind. The only thing that does is that Iran will never have a nuclear weapon.”"]))))
    out.append(card("Abbas Araghchi", "Iran’s foreign minister",
        k.p(C("Says Iran’s conditions are “nothing new”. He doubts Witkoff can deliver: twice, he said, Witkoff called "
              "their talks “productive and good”, only for the US to bomb Iran the next day.", "choices",
              ["“The conditions we have asked the US to meet is nothing new, nothing more than what was already in the Islamabad agreement, which was signed by the US president,” Araghchi said.",
               "In particular, he admitted to being sceptical that Witkoff could deliver. He recounted how he had twice held talks with Trump’s special envoy, after which Witkoff had described them as “productive and good”, only for the US to bomb Iran the next day."]))))
    out.append(card("Masoud Pezeshkian", "Iran’s president",
        k.p(C("Admits Iranians want the war to end, but says the public has withstood sanctions for 45 years.", "choices",
              "Pezeshkian, who handed all questions about the talks to Araghchi, admitted Iranians wanted the war to end and did not deny the economic pressure, but said the public had withstood sanctions for 45 years."))))
    out.append(card("Other voices in Iran", "Inside the system",
        k.p(C("A faction in Iran argues that Tehran should escalate the conflict while the US president is vulnerable, "
              "rather than let the deadlock drift. Praising Pezeshkian’s UN speech, the Revolutionary Guards commander, "
              "Ahmad Vahidi, said: “We are not afraid of war.”", "offer",
              ["A faction inside Iran is arguing that Tehran should seek to escalate the conflict with a vulnerable US president",
               "rather than let the crisis drift in its current deadlock",
               "Maj Gen Ahmad Vahidi, commander-in-chief of the IRGC, praised Pezeshkian’s speech, saying: “We are not afraid of war."]))))
    out.append(card("Congress", "Divided",
        k.p(C("Democrat Seth Moulton: “Remember when Donald Trump said that this war would last just a few weeks?” "
              "Republican Brian Mast says Trump is against “forever wars, and that is what he is ending”, meaning decades "
              "of hostilities from Iran.", "house",
              ["“Remember when Donald Trump said that this war would last just a few weeks?” said Democrat Seth Moulton before the vote.",
               "Mast said Trump is against “forever wars, and that is what he is ending”, meaning decades of hostilities from Iran."]))))
    out.append("</ul>")
    out.append('<h3>' + k.note("Around the table") + '</h3><ul class="table-list">')
    rows = [
        ("Israel", C("Iranian officials fear Israel will pull Trump away from the deal. Israel may object to giving Iran "
                     "such clear control over the shipping route.", "offer",
                     ["fear Israel will use its influence to pull the US president away from the proposal",
                      "Israel may object to giving Iran such clear control over the route through which ships would travel through the strait of Hormuz."])),
        ("Oman", C("Has agreed the new route with Iran, Iran says.", "offer",
                   "Iran says a deal on the temporary route through the strait of Hormuz has been agreed with Oman")),
        ("Saudi Arabia", C("Concerned that the route deal leaves out the other Gulf states as joint signatories.", "choices",
                           "Saudi Arabia is also concerned that the route deal is bilateral between Iran and Oman, and not with the Gulf states as joint signatories.")),
        ("China", C("Fully supports the proposal, according to Araghchi.", "offer",
                    "He added that he had consulted on the plan with China, which fully supported the proposal.")),
        ("UK", C("Its foreign secretary, Ed Miliband, met Araghchi in New York, the first meeting between UK and Iranian "
                 "ministers for a year. He said the UK wanted a diplomatic solution and freedom of navigation in the "
                 "strait.", "offer",
                 ["It was also the first meeting between UK and Iranian ministers for a year",
                  "Miliband made clear that the UK was committed to freedom of navigation in the strait and wanted a diplomatic solution"])),
    ]
    for name, c in rows:
        out.append(f"<li><strong>{k.note(name)}</strong><span>{k.claims(c)}</span></li>")
    out.append("</ul></section>")

    # ---- opinion ----
    k.section = "Opinion: is it a war?"
    out.append('<section aria-labelledby="s-op"><h2 id="s-op">' + k.note("Is it even a war?") + '</h2>')
    out.append('<aside class="opinion" aria-label="Opinion">'
               f'<span class="tag">{k.note("Opinion")}</span>'
               f'<p class="by">{k.claims(C("Arwa Mahdawi, Guardian columnist", "mahdawi", "Arwa Mahdawi is a Guardian columnist"), cite=False)}</p>'
               + k.p(C("Mahdawi argues that the administration keeps insisting this is not a war, and that this matters because "
                       "only Congress can declare one. She quotes JD Vance, the vice-president: “I wouldn’t call it a war.” "
                       "And she quotes Trump at a fundraising dinner in March: “They don’t like the word ‘war’ because "
                       "you’re supposed to get approval.”", "mahdawi",
                       ["as government officials keep insisting, what’s happening in Iran isn’t actually a war",
                        "the constitution is very clear that a president can’t unilaterally start an official war on a whim; only Congress has the power to declare a war",
                        "“I wouldn’t call it a war,” JD Vance told reporters early this month",
                        "“They don’t like the word ‘war’ because you’re supposed to get approval.",
                        "Trump said at a fundraising dinner in March"]))
               + f'<blockquote class="pull">{k.claims(C("“What we call this ‘military conflict’ isn’t just semantics, it matters greatly.”", "mahdawi", "What we call this “military conflict” isn’t just semantics, it matters greatly."))}</blockquote>'
               + '</aside>')
    out.append(k.p(C("This is the only opinion piece in the Storyline.", note="Framing text: describes the contents of the Storyline data.")))
    out.append("</section>")

    # ---- next ----
    k.section = "What happens next"
    out.append('<section aria-labelledby="s-next"><h2 id="s-next">' + k.note("What happens next") + '</h2>')
    out.append(k.p(
        C("Araghchi said he would stay in New York over the weekend to wait for an American answer, but was not in a "
          "hurry.", "offer",
          "Araghchi said he was staying in New York over the weekend to await an American response, but added he was not in a hurry."),
        C("The US midterm elections are in November, and the White House is under pressure to bring down oil prices "
          "before then.", "talks",
          "The US side is under pressure to leverage down oil prices and increase the availability of refined oil before the midterm elections in November."),
        C("For Patrick Wintour, the real question for Trump is whether he is prepared to go back to war after the "
          "midterms, and if not, whether he believes the US can squeeze Iran’s economy until its leadership gives in.", "choices",
          "Is he prepared to go back to war with Iran after the midterms and, if not, does he believe the US can squeeze the Iranian economy so hard that the leadership will succumb.")))
    out.append("</section>")
    return "\n".join(out)
