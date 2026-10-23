# Re-reading log, R22 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R22_decryption.txt` (DECODE D1690, KaJo, March 2016, under Meister
no. 40) gave the topics (Council of Trent, the faculties and the Parlement, the Vendôme/Soissons absolution, the
vice-legate of Avignon, Épernon) with a garble in most lines; `_check_reading.py` 0.582.

## 1. Is there a text already?

- DECODE "cleartext" images D948–D949 (contact sheet): the covering letter in clear, "Di Bles il 7 di ottobre 1588"
  (answers Montalto's letters of 19 September "con l'altro cifra"; Florentine marriage, Horatio Rucellai), and its
  address leaf with the Roman docket "Di Bles 7 d'ott.re 1588". Not a decipherment. No interlinear glosses on the eight
  cipher pages. The cipher's first line carries "dup." in clear (a duplicate).
- Rome's decipherments of the legate's ciphers (Francia 27) are not imaged. Tempesti (1754) tells the Soissons
  absolution only in outline; not used for words.

## 2. Page order

132r–135v as bound and transcribed; the sense runs on across every page turn. 135v ends in mid-sentence ("il gouerno
dela Prouenza [et] quello dela …"): the cipher's last leaf is not among the DECODE images (blocker: not imaged).

## 3. Hand re-parsing (R22_corrections.tsv)

About one word in eight re-parsed. Nearly all are carried by the transcribed figures as they stand:
- Spurious nomenclator dots: 130, 212, 545, 435, 615, 101, 926, 213, 137, 534, 209, 721, 713, 216; 132 is 113 with
  the dot on the 3 ("che fa il Re medesmo"). Codes written without a dot: 221 (lettere), 131, 151 (Francia), 195
  (Auignone), 226 (catolica).
- Words the decoder's vocabulary lacked or split: esprese (46 = spr), sapere (64 = per inside the word), pensasi,
  "la esequisca o la ritardi", "che la mi manda", "non che comeso", "più tosto", sodisfare (57 = sf), abiurare,
  importase, capitorono, comonicato/comonicare (the clerk's spelling, twice), "g[l]i pareua", contentauano,
  in diligenza, "cardinale di Sans", afetionatis., Fiorauanti, "a comodo", piaciute, spero (4 64 191), somam.
- m + 8 for -mente (liberam., separatam., somam.) and for "parlam."; 8 closes "Ecel.", "sig.", "ilustris.".
- Numbers between null 8s: "di 12", "di 2", "di 20", "di 4".
- Recurring transcription habits: 30 for 70 (p) in parlamento and parerà (three times); 05 read as 01 in nela and
  fratelo (three times); "pr"/"fr" written 7 0 0 0 / 3 0 0 0.
- Image check (crop, scratchpad only): 132r l. 11, DECODE "7 5?" is 7 1 = non ("Non lasarò di continouare"). The
  opening of 132r l. 2 was looked at; the figures are ink-burnt and not legible enough to settle the open group.

## 4. Alignment (reread_b00_align.py)

`TOTAL R22: 1482 words, 3 supplied, 20 partly`. The three "supplied" words are aligner artefacts: "di" after 131
(cardinale di Sans: the code carries "di"), and "catolica"/"né" on 134v l. 1–3, where 226 (catolici) is written
without its dot and the aligner does not expand the singular forms; the figures carry them. The "partly" words are
single letters at slips already in the tsv (oficio, esprese, sariano, acusare, comandato, comodo, gouerno …).

## Result

Before: 0.582 clean-sentence share (`R22_decryption.txt`). After: 0.72 on the "## Reading" body (1,508 words). By
hand: 19 unread stretches ([…]), 8 partly carried words ([?]) and 16 supplied letters or words in about 1,480 words;
every sentence is carried, the holes are short (one to eight figures each). Grade B: several figure+context
corrections and nineteen short holes.

## Still open, and why

- Short figure groups that parse into no word (listed in the reading's notes): 132r l. 2 opening and l. 3 "2 0 0";
  132r l. 16, 21, 22; 132v l. 1 ("senza anima …"); 133r l. 9 (two stretches), l. 12; 133v l. 4, 11–12, 17; 134r l. 6;
  134v l. 13; 135r l. 10 ("mons. […]"); 135v l. 5, l. 15. None was re-checked on the image beyond 132r l. 1–2 and
  l. 10–11: the page images are ink-burnt and the crops do not resolve single figures reliably. No outside blocker for
  most; a second image pass at higher resolution could close some.
- The end of the letter: the last cipher leaf is not imaged (outside blocker).
- Rome's decipherment in Francia 27 would settle all of them (physical access).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located on its line (`research/reading_audit/r2p_holes.py`), looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for, figures parsed under Meister no. 40 (`r2p_parseall.py`).
The ink of R22 (132r-135v) has spread and bled through: many figures are blurred, the paper has small holes (132r
l. 11, 132v l. 10, 133v l. 17), and the verso's figures show through as dark diagonal strokes, which look like
crossings over some groups (132r ll. 2-3, 132v l. 1, 133r l. 6, 133r l. 9, 133v l. 13, 134r l. 6, 135v l. 5); no
stroke there could be told for certain from show-through, so no group was treated as cancelled.
Filled or withdrawn:
- 132v l. 1 "anima" (212 01 17 20 21); the "[…]" after it (DECODE 216. auisi, blurred) stays.
- 133r l. 6 "precisem[ente]" (33 35 25 17 45 35 20 8: the -mente abbreviation, as elsewhere).
- 133r l. 9 "che hauendole io": "5 6 8 | 14 21 37 35 01 26 91 50 5 | 171 9" (the le was a hole). The "1? 5 3" heading
  the line (after "querela") is a blot of spread ink; the "[…]" before "che" stays. Blocker: illegible.
- 133v l. 13 "ama": "111 2 0 2 2 1 2" on the image = N. S. a m a.
Left, with blockers:
- 132r l. 2 "Questo […]" ("2 4 9 1 0 0 8"), l. 3 "pasato […]" ("2 0 0"), l. 11 "capito[li]", l. 16 "presentate […]"
  ("2 1 1 3"), l. 19 "hau[en]do" (a blot over the middle), l. 21 "che […] mi" ("2 0 2 1 2"), l. 22 "le […] facoltà"
  (nothing legible between): ink spread, blots and paper holes on 132r. Blocker: illegible.
- 132v l. 10 "[?aspetare]" (paper holes in the group), l. 11 "asolut[i]one" (a blot over the i). Blocker: illegible.
- 133r l. 9 "intendere […]" ("2 6 [blot] 1 1 4"), l. 12 "questo […]" ("2 1 6 1 9", blurred), l. 15 "del[a]". Blocker:
  illegible (the last: no-key-material, the a is not written).
- 133v ll. 4-5 "breue […] andase" ("4 5 8 5 | 3 1 7 2 0 2 1 6", show-through around it), l. 9 "g[l]i", l. 10 "[l']", l. 12
  "dire […]" (nothing written), ll. 12-13 "[?uiene]", l. 13 "[che]" (nothing written), l. 17 "efeto […]" (a paper hole
  beside "5 6 7 6 5 3 7 1 7 1"), l. 21 "del[a]". Blocker: no-key-material (l. 17: illegible).
- 134r l. 6 "spedisca […]" ("7 3 0 2 1 7"), l. 11 "[?procede]" (the figures give procedi), l. 14 "[?me]" ("2 0 1 5 9"),
  134v l. 13 "questo […]" ("2 1 7"), l. 14 "[?con]" ("3 6 1"). Blocker: no-key-material.
- 135r l. 1 "[h]onore", l. 7 "[r]agione" (the first letters not written), l. 10 "mons. […]" ("1 7 4 0 8"). Blocker:
  no-key-material.
- 135v l. 4 "de[l]", ll. 5-6 "da […] p[e]l" ("219. [obscured 7 0 7 3] ... 0 2 | 1 9 1 7 0 5 0"), ll. 10-11 "o[r]dini",
  l. 12 "grand[i]", l. 15 "uita […]" ("8 6 4 9 5 0 2"), l. 22 "goue[r]no", "[et]" (a null 8), "dela […]" (the last
  figures of the letter, "2 6 3 5 0 8 2 1"). Blocker: no-key-material (ll. 5-6: illegible, figures obscured by show-through).
Result: 4 holes filled; 40 left, each with its blocker.
