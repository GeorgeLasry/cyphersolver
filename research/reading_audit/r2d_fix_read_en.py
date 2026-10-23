"""r2d (23 Oct 2026): the English files of 423/2, 4, 6, 7, 8, 10 brought in line with r2d_fix_read.py."""
import pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nunzio1736' / 'texts'
FIX = {
 2: [("contained in [?them]", "contained in those [letters]"), ("[?above all] on seeing", "above all on seeing"),
     ("so [?hostile]; it is [?also] quite new", "so hostile; it is moreover quite new"), ("[?If] you learn", "When you learn")],
 4: [("Mons. [1513] of the\n[?Council]", "Mons. the Governor of the\nCouncil"), ("sounder [?counsels]", "sounder counsels"),
     ("these most thorny [?occasions]", "these most thorny junctures")],
 6: [("[?above all] under", "above all under"), ("into three [?Secretaries]", "into three Secretaries"),
     ("visited\nbeforehand in the [1582] of los Balbases", "visited\nbeforehand by the [1582] of los Balbases"),
     ("an example that [?that] Court", "an example that that Court"), ("my decisions, [?if], should", "my decisions, when, should"),
     ("put forward; [1204] it\nwould seem even much stranger", "put forward, although it\nwould seem now much stranger")],
 7: [("on the rights of the Holy See and on ecclesiastical\nliberty, which the same has [?always] had from time immemorial of conferring the [1449] [?benefices], and the bishops\n[?also] in",
      "on the rights of the Holy See and on that\nliberty which the same has had from time immemorial of conferring the ecclesiastical [?benefices], and the bishops\ntoo in"),
     ("the continual injuries", "the continual prejudices"), ("to the [1449] power in those", "of the ecclesiastical power in those"),
     ("Before taking even the most rigorous remedies", "Before taking, however, the most rigorous remedies")],
 8: [("that you inform [1601] of Ávila", "that you inform Mons. the Bishop of Ávila"), ("of [1845]; it will", "of [?answering]; it will"),
     ("take care,\n[?also] discreetly", "take care,\nalso discreetly"), ("what [?effects]", "what effects")],
 10: [("of the [1957] of last month", "of the 12th of last month"), ("from the [?complaints] that", "from the representations that"),
      ("false reports [1844] so unreasonable", "false reports to resolutions so unreasonable"),
      ("would [?already] be convinced", "would be convinced there"), ("false [?complaints] that", "false representations that"),
      ("groundless [?complaints] and", "groundless representations and"), ("Note also that", "Note, however, that"),
      ("[?but] for the rest", "while for the rest"), ("there [?being] no one", "there being no one"),
      ("by observing these false\nreports too", "by now observing these false\nreports"),
      ("[?If] [?even] [?His Majesty] were", "Even if His Majesty were"), ("well-founded [1843] then existed", "well-founded reports then came"),
      ("had been a burden on\nthe Holy See", "had been to the prejudice of\nthe Holy See"), ("nomination, [1864] the princes", "nomination, signifying to the princes")],
}
for n, reps in FIX.items():
    p = T / f'423-{n}_en.md'
    s = p.read_text(encoding='utf8')
    for a, b in reps:
        assert s.count(a) == 1, (n, a, s.count(a))
        s = s.replace(a, b)
    p.write_text(s, encoding='utf8')
    print(n, len(reps))
