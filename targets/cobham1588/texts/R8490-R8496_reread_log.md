# Re-reading log, cobham1588 R8490, R8492, R8495, R8496 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b13)

## Starting point

Reading audit (22 Oct): all four letters "decoded, not read": READING.md gave isolated cipher words with grades between
ellipses; the clear English had never been transcribed as running text, and no sentence of cipher text could be built.
The repository held the sign inventory from the glossed siblings (`signs.tsv`), a sign-level transcription of 22 runs
(`runs.txt`), the candidate-set solver (`solve.py`, `wordfreq.tsv`) and the 21 Sept passes (`reading_f88*.md`,
`reading_ff80_92_96_full.md`, `reading_f96v.md`).

## Step 1: is there a text already?

* **Contemporary decipherment.** None on ff. 80r-80v, 88r, 92r, 96r-96v (checked again on every page of the four
  records); the glossed letters of the volume are the siblings R8481, R8488, R8489, R8493 (already used for the key).
* **Clear duplicate / print.** CSP Foreign 21 pt 4 calendars Cobham letters of 1, 4, 9, 13, 24, 29 May and 3, 6, 10 June
  1588 (SP 77), none of these dates (21 Sept); not repeated. No edition prints Harley 287 ff. 80-97.
* **Neighbouring records.** R8491 (ff. 82-87), R8493 (f. 89, glossed), R8494 (ff. 90-91): no clear copy of these four
  letters. f. 97r (P3 of R8496) is blank: the "f. 97r runs" of the old gap list do not exist.

## Step 2: read on the images

The DECODE images are in the main checkout (`C:\Users\dbour\cypher\tmp\cobham\`, 7,200 x 10,200 px, BL images, not
committed). New on 22 Oct: the clear English of f. 80r-80v, f. 92r and f. 96v transcribed as running text from strips at
0.42-0.45x (the secretary hand read only as far as the crops allow; uncertain words bracketed), the clear of f. 88r
re-checked against the 21 Sept reading; f. 96r (wholly clear) not transcribed. The cipher runs were re-read at 0.5-1.0x
(`research/reading_audit/b13_crop.py`; crops in the scratchpad only). What the images settle
(`R8490_corrections.tsv`, `runs_corrected.txt`):

* **f. 80r "armada(s)" is "treaties" / "treaty of Breda".** At 1:1 the third sign of `AV?ATA` and `AV?AT` is the 7-form
  (e), not the ∽ loop (m): t-r-e-a-t-s, t-r-e-a-t + `dH -V7∞∞` (of b-r-e-d-d). The passage now reads as a sentence about
  hostages: *Touching hostages, yt ys honorable for [7] to […] their surety to these termes, as usuall yn all treaties …
  that at the treaty of Breda … and the subiects ther were delivered* (clear) *Julio Romeo, Cristophero Mondragon, Mor
  Daussy*.
* **f. 80r l. 18 is `ϸcAAUӾLA`** (h-o-s-t-a-g-e-s): the first sign is the h-stem, not the barred H.
* **The f. 80r l. 19-20 run is eight barred words**: `7 | Ac | ∞7γǂǂcL | Aϸ7γ | A··VA⊥ | AT | Aϸ7A | AcV∽7A`, of which
  *surety* (s-u-r-t-y) is new; `∞7γǂǂcL` stays unread.
* **f. 80v**: *22 hath a desire to retourne from theym, yf he be not more [?restrained]* (the run read as one sentence).
* f. 88r, f. 92r, f. 96v: no run changed its reading. The unglossed signs (K, W, Q/ɔ, the square) and the polyphonic
  ones (wide/narrow caret s/t/a, γ r/y, c o/a/e, ϕ l/t/p) leave most groups without a word, as on 21 Sept; the solver's
  near matches were re-checked on the strips and kept only where one sign or one edit is in doubt (`[?word]`).

## Step 3: alignment

Each reading (`R8490_reading.md` … `R8496_reading.md`) carries alignment notes per run: a cipher word is plain only where
every sign has its glossed value (H grade), `[?word]` where one sign is doubtful or the solver allows one edit (M grade),
`[…]` for the I-grade guesses of 21 Sept (Rain, spoil, Portugals, noblemen, Roper, Iohn, Naples as certain, seventy …),
which are withdrawn as readings. Supplied words are bracketed (*[of the] north east*, *[had been]*, *[be]*).

## Step 4: result (`research/reading_audit/b13_score.py`, LANG_=en; E=1 maps common Elizabethan spellings first)

| doc | before | after (plain / E=1) | state | why |
|---|---|---|---|---|
| R8490 (ff. 80r-80v, 5 May) | decoded, not read | 0.114 / 0.514 | decoded, not read | the hostages/treaty sentence and the f. 80v run now read; the l. 8-11 and l. 31-34 runs (`c∪ǂǂ8ϕ`, `WLϕΛ`, `Xd+c:·87`, the 22/27 passage) still have holes in most words |
| R8492 (f. 88r) | decoded, not read | 0.0 / 0.118 | decoded, not read | the densest cipher; only *the haven*, *there*, *Italians*, *Antonio* and a few M-grade words |
| R8495 (f. 92r, 27 May) | decoded, not read | 0.0 / 0.074 | decoded, not read | the clear news reads; the ten cipher lines give scattered M-grade words |
| R8496 (ff. 96r-96v, 9 June) | decoded, not read | 0.2 / 0.35 | decoded, not read | f. 96r not transcribed; the f. 96v runs give scattered words |

The plain figures are depressed by Elizabethan spelling (the en lexicon is modern); E=1 is a pointer only. The test is the
reader's: in none of the four letters do the cipher passages build sentences, R8490's hostages passage excepted.

## One sentence per document (partial readings)

* R8490: *Touching hostages, yt ys honorable for [7] to […] their surety to these termes* — "Touching hostages, it is
  honourable for [her Majesty] to […] their surety on these terms."
* R8492: *There ys captayne Mongomery of latt gone into Schotland* (clear) — the cipher after it does not read.
* R8495: *ys also in [?prison] […] [?Bruges], the cause whereof ys not knowen* — "is also in [?prison] […] [?Bruges], the
  cause of which is not known."
* R8496: *I pray let me knowe … whether yow have receaved the cypher that I sent yow* (clear).

## What stays open and why

* The unglossed signs (K, W, ɔ/Q, the square ◻) and the codes 22, 27 occur in no glossed sibling: **no-key-material**.
  The polyphonic signs leave several readings for most groups; without a gloss or a clear copy there is nothing to choose
  between them: **no-key-material**.
* Words of the secretary-hand clear text bracketed as `[?]` and f. 96r (not transcribed this session): **not-attempted**.
