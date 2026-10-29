"""Builds profile.json for barbavara1447 (Barbavara + Pusterla, key R1857). Run from the repo root."""
import json
F = 'targets/barbavara1447/profile.json'
old = json.load(open(F, encoding='utf8'))
REV = {"grade": "A", "by": "Claude Opus 5.5 (session)", "date": "2026-10-28",
       "note": "Read as sentences; coherent throughout; holes only at the copyist's blanks for code signs, most now filled from R1857 and context."}
MISSING = ("The cipher leaf was not transcribed sign by sign: the late clear copy filed with it is a complete text "
           "(spot checks with the R1857 key agree).")
L = [  # id, folio, date, writer, from, decipherment, text file, copy folio, summary
 ('f13', 'f. 13', '21 Jan 1447', 'Pietro Pusterla', 'Gualdo Tadino', 'clear copy on f. 14', 'pusterla_copies_a', 'f. 14',
  "Pusterla tells Sforza he has reached Gualdo and will wait at Montefiascone or Monte Guiduzo for word where to join him, with Antonio da Trezzo, and asks for a guide."),
 ('f27', 'f. 27 (copy; the cipher original not located)', '6 Feb 1447', 'Pietro Pusterla', 'Ferrara', 'f. 27 is the clear copy', 'pusterla_copies_a', 'f. 27',
  "At Ferrara the Duca di Ferrara is suspicious for lack of news; Pusterla reassures him and urges a quick conclusion; Barbavara, going to the Pope and the King about the money, takes a copy of Pusterla's cipher."),
 ('f32', 'f. 32', '10 Feb 1447', 'Pietro Pusterla', 'Ferrara', 'clear copy on f. 33', 'pusterla_copies_a', 'f. 33',
  "A short note to the Count: no news from Sforza; Pusterla protests his loyalty and asks for instructions."),
 ('f40', 'f. 40', '13 Feb 1447', 'Marcolino Barbavara', 'Rimini', 'clear copy on f. 39', 'decipherments_18c', 'f. 39',
  "From Rimini: the courier is warned, a safe-conduct is sent for two of Sforza's men, and Barbavara will set out by San Giovanni in Marignano; he has dealt with Sigismondo Malatesta as instructed."),
 ('f42', 'f. 42', '14 Feb 1447', 'Pietro Pusterla', 'Milan', 'clear copy on f. 41r-v; 15th-c. decipherment on f. 43', 'pusterla_copies_a', 'f. 41r-v',
  "In Milan the Duke receives Pusterla gladly and is delighted with Sforza's disposition, but will not send him back without a good part of the money, to be collected at Ferrara."),
 ('f49', 'f. 49', '27 Feb 1447', 'Marcolino Barbavara', 'Rome', 'clear copy on f. 48r-v', 'decipherments_18c', 'f. 48r-v',
  "In Rome Barbavara finds Eugenius IV dead; the Camerlengo will wait for the new pope and is friendly; Capua and Fermo are tipped; a show of force in the Marche would loosen the cardinals' purses."),
 ('f56', 'f. 56', '3 Mar 1447', 'Marcolino Barbavara', 'Rome', 'clear copy on ff. 55r-v, 57r', 'decipherments_18c', 'ff. 55r-v, 57r',
  "King Alfonso agrees to pay Sforza's condotta, 94,000 ducats a year for two years, on a schedule that includes 20,000 owed by the Duca di Ferrara, which the King will make him pay."),
 ('f62', 'f. 62', '4 Mar 1447', 'Marcolino Barbavara', 'Rome', 'clear copy on f. 61r', 'decipherments_18c', 'f. 61r',
  "The cardinals have entered the conclave; letters go by Madonna Aura and Messer Angelo in Urbino; Alfonso's letters enclosed, the King pleased that Sforza has turned from the Kingdom."),
 ('f69', 'f. 69', '6 Mar 1447', 'Marcolino Barbavara', 'Rome', 'clear copy on f. 68', 'decipherments_18c', 'f. 68',
  "The new pope is proclaimed at about the seventeenth hour: Tommaso Parentucelli, Nicholas V (\"Monsignore da Cologna\" in the copy, for Bologna)."),
 ('f67', 'f. 67', '6 Mar 1447', 'Pietro Pusterla', 'Ferrara', 'clear copy on f. 66r-v', 'pusterla_copies_b', 'f. 66r-v',
  "Pusterla presses the Duca di Ferrara to help the Duke of Milan, with little hope, and complains of no answers since Reggio."),
 ('f71', 'f. 71', '7 Mar 1447', 'Pietro Pusterla', 'Ferrara', 'clear copy on f. 70r-v', 'pusterla_copies_b', 'f. 70r-v',
  "The Duca di Ferrara says his revenues cannot bear the cost of lord Guidemo's troops, but offers to join the war against Venice on terms he once proposed; three briefs enclosed."),
 ('f75', 'f. 75', '8 Mar 1447', 'Marcolino Barbavara', 'Rome', 'clear copy on f. 74r-v', 'decipherments_18c', 'f. 74r-v',
  "Barbavara at the new pope's feet; the pope sends the Camerlengo and the Vice-Chancellor to Alfonso about peace in Italy; the King says priests are men \"da bastonate, non da pregare\"."),
 ('f77', 'f. 77', '8 Mar 1447', 'Pietro Pusterla', 'Ferrara', 'clear copy on f. 76r-v', 'pusterla_copies_b', 'f. 76r-v',
  "Twenty thousand ducats wait at Ferrara for Sforza's messenger; the Venetian army came to Cremona crying \"viva San Marco\", but the town held for Sforza."),
 ('f81', 'f. 81', '10 Mar 1447', 'Pietro Pusterla', 'Ferrara', 'clear copy on f. 80', 'pusterla_copies_b', 'f. 80',
  "The Venetians have moved on Soncino; the Count of Urbino is negotiating; the Duca di Ferrara is heartened by Nicholas V's election; a Venetian hope of Cremona through a squad captain."),
]
docs, texts = [], []
for i, f, date, who, frm, dec, tf, head, summ in L:
    docs.append({"id": i, "shelfmark": f"BnF italien 1584 {f}", "date": date, "year": 1447,
      "country": "Italy (Sforza correspondence)", "route": f"{who} ({frm}) -> Francesco Sforza",
      "places": {"from": frm, "to": "Pesaro"},
      "language": "Italian", "pages": 1, "cleartext_in_document": "interspersed",
      "plaintext": {"location": ["separate folio"], "source": dec + " (late hand)", "partial": False},
      "length": {"tokens": "unknown", "unit": "symbols", "measured": False},
      "transcription": {"by": "llm from images", "source": "Gallica microfilm, ark btv1b100373864", "image_quality": "fair",
                        "notes": "Clear copy transcribed; cipher leaf not transcribed sign by sign."},
      "read": "read"})
    texts.append({"doc": i, "label": f"{who}, {frm}, {date} (cipher {f}; copy {head})",
      "decryption": f"texts/{tf}.md", "translation": f"texts/{tf}_en.md", "language": "it",
      "transcription_missing": MISSING, "state": "read", "summary": summ, "reading_review": REV})
GLOSSED = [
 {"doc": "f135", "label": "Marcolino Barbavara, Rome, undated (late April 1447), f. 135, mostly clear with 4 cipher runs",
  "transcription": "texts/glossed_runs.tsv", "contemporary": "texts/glossed_letters.md",
  "decryption": "texts/glossed_letters.md", "translation": "texts/glossed_letters_en.md", "language": "it",
  "state": "read", "read_share": 1.0,
  "summary": "From what the Duke writes about Roberto da Montalboddo and what he has heard from the King, Barbavara thinks his staying in Rome is no longer needed, and asks Sforza to say so at once.",
  "reading_review": {"grade": "B", "by": "Claude Opus 5.5 (session)", "date": "2026-10-29",
                     "note": "All four runs read in sense; several signs (d- = r, the tall gate sign, the pairs glossed li, per le, cio) rest on the 15th-c. gloss, not on the late key copy."}},
 {"doc": "f143", "label": "Marcolino Barbavara and Simone Arrigoni, Rome, 4 May 1447, f. 143, mostly clear with 51 cipher runs",
  "transcription": "texts/glossed_runs.tsv", "contemporary": "texts/glossed_letters.md",
  "decryption": "texts/glossed_letters.md", "translation": "texts/glossed_letters_en.md", "language": "it",
  "state": "read in part", "read_share": 0.9,
  "summary": "The Malatesta coming over to the King, the bulls for their vicariates, the new pope stalling until the outcome is settled, and 4,000 ducats agreed with the Count of Urbino's ambassadors.",
  "reading_review": {"grade": "B", "by": "Claude Opus 5.5 (session)", "date": "2026-10-29",
                     "note": "46 of 51 runs read (9 from the key with the gloss agreeing, 31 key and gloss, 6 gloss alone); runs 143.17, .31, .35, .46, .51 unread: no gloss and blotted key cells."}},
]
p = old
p['title'] = ('Marcolino Barbavara and Pietro Pusterla to Francesco Sforza, Jan - May 1447: '
              'cipher letters in the R1857 key (BnF italien 1584)')
glossed = [d for d in old['documents'] if d['id'] in ('f135', 'f143')]
for d in glossed:
    d['places'] = {"from": "Rome", "to": "Pesaro"}
    d['plaintext'] = {"location": ["interlinear"], "source": "15th-c. glosses over part of the cipher runs; runs deciphered with the R1857 key", "partial": True}
    d['read'] = 'read' if d['id'] == 'f135' else 'read in part'
    d['transcription']['notes'] = 'Clear text and every cipher run transcribed (texts/glossed_letters.md), signs named approximately.'
p['documents'] = docs + glossed
p['system']['sibling_key'] = "One key for Barbavara, Simone Arrigoni and Pietro Pusterla (R1857 header)."
pr = p['conditions']['prior_solution']
pr['where'] = ("Late clear copies filed with every copied cipher leaf (Barbavara ff. 39, 48, 55/57, 61, 68, 74; Pusterla "
               "ff. 14, 27, 33, 41, 66, 70, 76, 80); 15th-c. decipherment of f. 42 on f. 43; 15th-c. interlinear glosses, in "
               "part, on ff. 135 and 143. Key copy DECODE R1857 P11 (identified for f. 69 by Tomokiyo).")
p['solution'] = [s for s in old['solution'] if not s['what'].startswith(("Pusterla's", 'Code signs'))] + [
 {"date": "2026-10-28", "kind": "literature search", "what": "Pusterla's cipher leaves (ff. 13, 32, 42, 67, 71, 77, 81 and the 6 Feb letter) checked: late clear copies for all; f. 43 a 15th-c. decipherment of f. 42.", "result": "worked"},
 {"date": "2026-10-28", "kind": "transcription", "what": "Pusterla's eight clear copies transcribed and translated (two subagents, checked against the images).", "result": "worked"},
 {"date": "2026-10-29", "kind": "reading", "what": "ff. 135 and 143: clear text transcribed and the 55 cipher runs deciphered with the R1857 key and the 15th-c. glosses (subagent); 50 read, 5 runs of f. 143 unread (no gloss, blotted key cells); several values rest on the gloss only.", "result": "partial", "technique": ["key matching", "crib testing", "contextual inference"]},
 {"date": "2026-10-28", "kind": "key from source", "what": "Code signs the copyist left blank: R1857's label 'Duca di Ferrara' over d+÷ fits all five blanks; d.7 = Veneziani and 9+o = qui (labels fit); the Z-like sign = Micheletto Attendolo [?] from context; the angle sign and four others open.", "result": "partial", "technique": ["key matching", "contextual inference"]},
]
o = p['outcome']
o.update({"class": "already solved", "method": "read from existing decipherment", "key": "partial",
  "method_basis": ("Every cipher letter of Barbavara and Pusterla in ital. 1584 has a decipherment: a late clear copy filed "
                   "with it (14 letters) or 15th-century glosses (f. 43; ff. 135 and 143 in part). The work is finding, "
                   "transcribing and translating them, checking them against the R1857 key, and filling the copyist's "
                   "blanks for code signs."),
  "contribution": ["transcription", "key extended or corrected", "catalogue correction"],
  "codes_open": {"open": 7, "total": "unknown", "tokens_open": 9},
  "verification": ["contemporary decipherment", "key confirms", "historical consistency"],
  "key_file": "key_R1857_codes.tsv",
  "texts": texts + GLOSSED,
  "gaps": [
   {"item": "code signs angle (x3), A, z-loop, stroke-9, reversed-c-o (x1 each)", "blocker": "open-codes",
    "detail": "unlabelled on R1857 or absent; one to three contexts each"},
   {"item": "Z-like sign = Micheletto Attendolo [?]", "blocker": "open-codes", "detail": "context only, three places"},
   {"item": "f. 143 runs 143.17, .31, .35, .46, .51 and words inside 143.4, 143.41", "blocker": "no-key-material", "detail": "no gloss (or too faint) and the signs' cells are blotted on the only key copy"},
   {"item": "6 Feb 1447 cipher original (copy f. 27)", "blocker": "needs-physical-access", "detail": "not found on the microfilm"},
  ],
  "notes": "Leads 1313 and 1314 closed 28 Oct 2026. Pusterla folded in from targets/pusterla1447 (one key)."})
for k in ('fraction_read', 'fraction_read_method', 'fraction_read_source'):
    o.pop(k, None)
o['credits'][0]['note'] = ("Late clear copies of all fourteen copied letters (archive hand, probably 18th c.); 15th-c. "
                           "decipherment f. 43 and interlinear glosses on ff. 135 and 143.")
with open(F, 'w', encoding='utf8') as fh:
    json.dump(p, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
