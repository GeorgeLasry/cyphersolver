# Re-reading log, R28 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R28_decryption.txt` (character-model segmentation of DECODE's
transcription D1692 under Meister no. 40): the gist clear (garden, Gondi to Rome, Guise's debts) but garbled words in
most lines ("tione ne uo per certo e non [RE DI POLONIA]", "ormanetto", "si tarnen irritati"). Clean-sentence share 0.567.

## 1. Is there a text already?

- DECODE images: 7 cipher pages (142r–145r) and one "cleartext" image (f. 141), the covering letter in clear:
  "Seguiranno queste poche parole per far coperta all'occlusa cifra ... Di Bles a li viij Ottobre M.D.LXXXVIII". Not a
  decipherment. DECODE's header on 142r reads "dup.ta di li viij Otto." (the sheet is a duplicate). No interlinear glosses.
- Print: Tempesti, *Vita di Sisto V* (1754) II, book VII §§ X–XII (scratchpad OCR ll. 985–1012) paraphrases this
  letter: Girolamo Gondi sent to Rome on Montmorency's satisfaction; the garden walk with the King and his mother; Guise
  must be reassured, otherwise "Sua Maestà non sarebbe sicura in Bles"; Guise's debts; the King "per mezzo del Do" offers
  "sopra l'entrata dell'anno venturo un donativo di dugentomila scudi"; Guise refuses ("Sua Maestà aveva troppo bisogno
  di danaro"). Used for names and sense only. Rome's decipherments (Francia 27, Hübner) not imaged.

## 2. Word decode and hand re-parse

Started from `R28_worddecode.txt`. About one word in eight needed re-parsing; the corrections are in
`R28_corrections.tsv` (58 rows). The main causes:
- Spurious or missing nomenclator dots: 116 with the dot on the 6 (decoder: "[162?]"), 713 = interponersi (171 31 …),
  1^.7 in "l'istirpatione"; undotted codes 131 (cardinali, three times), 143 (guerra), 165 (quello), 232 (il già re di
  Nauarra) — the decoder had read 232 + 69 as "domani".
- Decoder chose the wrong homophone split where the figures were right: Gondi (142r l. 19, which it read "non di"),
  "che N. S., che non ha" (it read 115 Re di Polonia), "io le disi", "io non ne parlarei con", "et sano molto bene",
  "ci siano", "nodrire", "mons. d'O a dire", "l'entrate", "a le stanze", "contra".
- The -mente abbreviation m + 8 (as in R43): "ueram." (143r l. 2), "altram." (143r l. 13), "apertam." (144r l. 23).
- A plain number: "8 2 0 0 8" = 200 between nulls, then "milia scudi" (Tempesti: dugentomila).
- Single-figure slips taken from context (tsv "figures+context"): ale su[e] (113 for 153), uole (8 7 for 3 7), dirle,
  ela (2? for 5), disturbare, [sodi]sfatione (52 for 57).

## 3. Image checks (crops, scratchpad only)

- 142r ll. 1–2 (opening): "prima che" confirmed (3 3 1 7, not 3 3 5 7); a few untranscribed figures at the left margin
  ("1 0 1 0 1 2 X …") are faint; the opening stays unread.
- 142r l. 19: "8 4 0 9 1 0 1 6 2 1 7" = Gondi, as transcribed.
- 142v l. 12: "7 0 2 1 …" particolare (DECODE "3 0").
- 143r l. 18: the figures around "si [?stimaria]" are blotted; no better reading.

## Result

Before 0.567 → after 0.67 clean-sentence share (`_check_reading.py` on the "## Reading" body; it counts the clerk's
spellings — sodeto, necesità, apresentare — as holes). By hand: 10 unread stretches ([…]), 14 partly carried words
([?…] or bracketed letters) in about 1,160 words; every sentence of the argument carries. Grade B (about 20
figure-context corrections).

## Still open, and why

- The opening (142r l. 2: "1 1 1 2 2 7 9 6 5 5 4 4 9 0 8" and "1 7 1 3 0 2 1 5 0 5 2 5 0"): no parse; partly
  untranscribed margin figures, faint on the image.
- 142v ll. 3, 6–7 (two short stretches), 143v l. 9 ("lo faria […]"), 143v l. 23 ("si [?…]riano": figures say
  "con crenderiano"), 144r l. 11, 17, 22 (short stretches): no word parse of the transcribed figures; not all checked on
  the image (no outside blocker; a further image pass might close some).
- 144v ll. 7–9: paper damaged (DECODE's comment, confirmed on the image): blocker = damage.
- 145r ll. 3–4: the transcription line breaks off in corrupt characters; the closing formula is unread.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), looked at on the image (scratchpad `reread/r2p/crops`),
cancellation strokes looked for, parsed (`r2p_parseall.py`). R28's ink has spread and the verso's figures show
through as long diagonal strokes over the lines (142r l. 2, 142r l. 8, 143v l. 9); they look like crossings but could
not be told for certain from show-through, so nothing was treated as cancelled.
Filled:
- 142v l. 1 "non solo": "7 1 | 4 9 1 5 0 9" = non solo (71 is the word sign non; it was supplied).
- 142v l. 5 "desiderauano": "... 26 35 00 21 37 21 01 9", kept as written.
- 142v ll. 6-7 "tuto": "6 3 7 = | 1 5 1 9 1" (= the encipherer's hyphen).
- 143r l. 22 "non temino": "7 1 6 5 ..." (71 non).
Left, with blockers:
- 142r l. 2 the opening "1 1 1 2 2 7 9 6 5 5 4 4 9 0 8" and "mi facese […] piede" ("1 7 1 3 0 2 1 5 0 5 2 5 0"): both in
  a stretch with figures obscured by show-through. Blocker: illegible.
- 142r ll. 7, 9, 23 (144v) "sig[ri]" (the abbreviation, nothing written), 142r l. 8 "[?di] Gondi" (8 26, in the
  stretch obscured by show-through of l. 8), 142r l. 21 "[?et] di [?sodi]sfatione" (no figures), l. 22 "di [ri]tirarlo" (5 1 7).
  Blocker: no-key-material (l. 8: illegible).
- 142v l. 3 "[?…]" (dotted 187, not in the key), ll. 6-7 "tuto […] uenise" ("1 6 6 4 1 7 1 6", undotted), l. 8
  "[?mancariano]" ("8 2 0 2 1 0 1 2 5 2 [blot] 6 0 0 2 1 9 1 9"). Blocker: no-key-material (l. 8: illegible, a blot).
- 143r l. 5 "[?con]" (79 = come), l. 12 "habi[a]", ll. 18-19 "[?stimaria]" ("4 5 1 | 1 1 2 0 2 1 0 0 1 7 2"), 143v
  l. 2 "[?tanto]" (21 01 51 9, no t), l. 23 "[?…]riano" (nothing written). Blocker: no-key-material.
- 143v ll. 9-10 "faria […] Disi": "2 6 1 5 0 9 1 0 1 5 1 1 7 3 5 0 0 3 | 8 5 0 1 5 3" with figures obscured by show-through before it.
  Blocker: illegible.
- 144r l. 4 "su[e]", l. 11 "egli […] daria" ("0 1 3 9"), l. 16 "donatiu[o]", l. 17 "scudi […]" ("6 9 5 6 1 2 9"), l. 22
  "habia […]" ("5 8"). Blocker: no-key-material (l. 22: too-short).
- 144v ll. 5-6 "[?seminare]" ("4 3 2 7 0 1 2 1 | 0 0 5"), l. 6 "[?le]" (no figures), ll. 7-8 "fare […] la buona"
  ("8 1 7 1 5 | 1 9 4 9 1 0 0 1 7 9 6 2 6 2 1"), "[la quale]" ("1 7 1 3 1 3 1 1 2 2 1 2"), l. 17 "ilustris[simo]" (the
  abbreviation). Blocker: no-key-material.
- 145r l. 3 "auis[o]" and ll. 3-4 the close ("8 4 2 2 7 111. 2 | 2 7 9 1 5 4 9 6 0 166. 0 1 2"). Blocker: no-key-material.
Result: 4 holes filled; 31 left, each with its blocker.
