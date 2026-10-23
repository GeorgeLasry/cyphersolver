# Re-reading log, R8505 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b28)

## Starting point

Reading audit (22 Oct): "decoded, not read". `reading.txt` (word-split decoder output with clear-context fragments):
`docs/_check_reading.py --file reading.txt` **0.454 clean sentences (84/185), hole rate 0.154**. NOTES' open task:
ff. 263r and 264r never re-read sign by sign (only the versos were).

## 1. Is there a text already? No

- DECODE R8505 re-fetched with the cookie (`research/reading_audit/b28_fetch.py`, DOCONLY=1): four images, no DOC_
  attachment, no comment block; language still "English?".
- **DECODE R8010** ("Harley_ms_1582_8", BL, dates 1553-1596, 4 pages, status blank): its four images are **the same
  leaves, ff. 263r-264v**, at higher resolution (6856-7551 x ~10,000 px; R8010 P1 = f. 263r, P2 = 263v, P3 = 264r,
  P4 = 264v). A duplicate record, created 16 Apr 2024 by another DECODE user; noted for DECODE in NOTES.
  DECODE R8009 ("Harley_ms_1582_8", N/A) is empty.
- Print: web search for the title (23 Oct) found nothing; CSP Foreign 1583-86 (22 Sept) has no copy.
- Key: rebuilt here from the ciphertext (22 Sept); no Navarre graphic-sign key on DECODE or in Tomokiyo.

## 2. f. 263r read sign by sign; the other sides by beam over the documented look-alikes

- R8010 images deskewed (`b28_deskew.py`: f. 263r -2.2°, 263v -0.55°, 264r +0.3°, 264v -2.5°), line centres from the
  ink profile (`b28_lines.py`), every f. 263r line cropped (`b28_line.py`, `b28_grid.py`).
- **Decoder fix**: the old `reading.py` read every token starting with `#` as a code, so the `#` sign (d) was dropped
  and shown as `[#]` in every run; `b28_r8505_decode.py` decodes `#` as d and only `#<digits>` as codes. This alone
  restores words such as "de", "du", "desdain", "deuant".
- **Label corrections on f. 263r** (`R8505_corrections.tsv`, corrected transcription
  `R8505_transcription_f1_b28.txt`; `final/f1.txt` left as it was): 8 tokens. The first transcription of the rectos
  used `d` (crossed delta, a) for two shapes; four are the crossed epsilon `Eb` (t): "sen**t**ent du gouvernement",
  "presen**t** du [81]", "devan**t** Espernon", "allie e**t** a lui". Also `dd`->`Oi` and `b`->`T` in "des autres"
  (1.9), `b`->`T` in "du gouvernement" (1.2), `b`->`ne` at the start of 1.12.
- `b28_r8505_alt.py` scores every `d` in the four files as a vs t: on the rectos t wins 17 of 22, on the versos a wins
  35 of 44. **Key unchanged**: `d` = a holds where the shape was re-read; the rectos' t's are a label merge, not a
  second value. To be settled on f. 264r by a sign-by-sign re-read.
- `b28_r8505_beam.py`: beam decode with the fr-1530-despatches 5-gram, each token allowed its documented look-alike
  (d/Eb, ω+ʃ ligature/ω and ʃ, φ/ʃ, the two ε, the two stem-loops, χ/hourglass, the bar signs, dot groups/eq) at a
  penalty, a null at a higher penalty. It improves f. 264r only in places ("contrauentions on se plaint en uain",
  "couler tout a coup", "la peut retenir par plus fortes et asseurees"); most f. 264r runs stay garbled. Spot check
  on the image (2.2): the signs are as transcribed, so the remaining breaks there are not simple label slips.
- Clear French of f. 263r transcribed for its five cipher paragraphs (the lower half of the page, clear only, not
  transcribed). Clear French of the other sides only as recorded beside the runs in `final/f2-f4.txt`.

## 2b. Second pass (23 Oct 2026, same day, on the follow-up request)

- **Folio labels of the versos corrected.** R8010 P2 (the verso of f. 263, a left-hand page) holds the Languedoc text
  that `final/f4.txt` transcribes ("Beaucaire sur le Rosne", "Besiers"); R8010 P4 (the verso of f. 264; P3 carries the
  folio number 264) holds the text of `final/f3.txt` (the Queen, the marriage, "Le Roy de Navarre et Monseigneur le
  Prince de Condé"). So f3 = f. **264v**, f4 = f. **263v**; NOTES and the first reading had them the other way round.
  The memoir's order is 263r (his qualities, his lands), 263v (Languedoc), 264r (Saintonge, Poitou, the party's
  organisation, the war), 264v (the alliances, the Queen, the marriage).
- **f. 264r, all 25 cipher lines, compared with the image** (R8010 P3 deskewed +0.3°, grid crops `b28_grid.py` at
  0.5-0.55 and single-line crops at 0.8-1.0). Nine label corrections (`R8505_corrections.tsv`, corrected file
  `R8505_transcription_f2_b28.txt`): `II` + `eq` is one f-sign ("une forme"), `T` -> `u` ("d'avoir"), `q` -> `Eb`
  ("conduite"), `Pi` -> `Gm` (2.3), `II :` -> `eq eq` ("affaires", 2.3), `:` -> `eq` ("deffiance", 2.8), `d` -> `Eb`
  ("l'edict", 2.9). Spot checks of 2.2 (whole line), 2.5, 2.6 confirm the remaining tokens as transcribed: the
  breaks there are in the ciphertext as written (clerk's slips or values the key lacks), not label errors. Decoder and
  beam now read every cipher field of a line (2.5, 2.8, 2.21 have two).
- **f. 264v ll. 3.38-3.46 re-transcribed sign by sign** (R8010 P4 deskewed -2.5°, line crops at 1.0;
  `R8505_transcription_f3_b28.txt`). The provisional September tokens had dropped and merged signs; re-read, the
  block decodes with the unchanged key to "... ni selon sa qualite ni selon la leur, les a abandonnees en [leur]
  besoin, les a laissees ... en risee et en proie a leurs ennemis ...", "indignement", "moiennant certaines". So the
  block is **not illegible**: it reads in part; the rest are fragments.
- **Clear French transcribed**: the lower half of f. 263r (the King's person; his lands in sovereignty and in homage,
  Béarn, Navarrenx, Foix, Bigorre, Marsan, Albret, Armagnac, Rouergue, Périgord, Limoges; the commanders), and the
  clear paragraphs of f. 264r around the cipher (Condé at St-Jean-d'Angély, the nobility of Saintonge and Poitou,
  the party beyond the Loire, the Council, the defensive). Doubtful words `[?]`; names and words not made out `[…]`.
  f. 263v's clear text not re-transcribed (only as recorded in `final/f4.txt`).

## 2c. Third pass (23 Oct 2026)

f. 263v's clear French (R8010 P2, deskewed -0.55°, grid crops at 0.5) transcribed in full, spelling as written, and
the cipher runs 4.1-4.11 set in it: the nobility of Marsan, Albret, Armagnac, Rouergue, Périgord, Limousin; the
King's northern lands (Vendôme, Marle, Thimerais) and their officers; his four Chambres des comptes and his Council
(du Ferrier named for Paris); Quercy, Lauragais, Albigeois; Bas Languedoc, Provence, Dauphiné; the forces of Guyenne.
Doubtful names `[?]`. The alignment script now anchors each run at the earliest place among its first four words
(the cipher repeats "monsieur" at a line break, which had thrown the anchor forward).

## 3. Reading and alignment

`R8505_reading.md`, `R8505_en.md`, in leaf order. `b28_r8505_align.py`: decoded words (3+ letters) found in order in
the reading — **f. 263r 45/56, f. 263v 45/65, f. 264r 89/194, f. 264v 29/152** (the rest are `[…]` stretches).
Look-alike letters in the reading: **11** (f. 263r 9: q+u for the ω+ʃ ligature 2, t for the crossed sign 4, s for
the lunate ε 3; f. 264r 1, "[?et]"; f. 264v 1, "traitées").

## 4. Score

| | clean-sentence share (b17_score.py, fr) | explicit holes only (HOLES=1) |
|---|---|---|
| before: `reading.txt` (_check_reading.py) | 0.454 (84/185) | - |
| first pass | 0.518 (71/137) | 0.613 |
| second pass | 0.530 (124/234) | 0.650 |
| **third pass, whole memoir (all clear text in)** | **0.529 (185/350)** | **0.691 (242/350)** |
| third pass by side: f. 263r / 263v / 264r / 264v | 0.691 / 0.519 / 0.351 / 0.407 | |

French is not among the languages for which the brief allows the explicit-hole figure as the bar, and a reader
agrees with the checker: ff. 263r and 263v build (their clear text dominates and the cipher runs on 263r read),
but the cipher clauses of ff. 264r and 264v are still strings of fragments. The document **stays decoded, not
read**.

## Open

- f. 264r and f. 264v cipher clauses that do not build after the image check — blocker **no-key-material**: the
  tokens are confirmed on the image and the key (rebuilt from this text alone) gives no French there; values for
  rare signs or the clerk's slips would need a second text in the same key, and none is known.
- Doubtful names and words in the clear text of all four sides, marked `[?…]` — blocker **illegible** (fine
  secretary hand at the photograph's resolution).
- Nomenclator numbers 6, 21, 36, 51, 57, 72, 81, 99, 721: blocker **no-key-material**.
