# Re-reading log, R7486, R7488-R7494, R7496 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b05)

## Starting point

Reading audit (22 Oct 2026): nine of the fifteen Vienna -> Schenck letters "decoded, not read" (R7486, R7488, R7489,
R7490, R7491, R7492, R7493, R7494, R7496); their files `reading/R74xx.txt` are diplomatic transcriptions with the
letter-table runs decoded in braces, the person codes open, and many `[?]` marks for clear German words the two 9 Oct
transcription agents could not read. `_check_reading.py` on those files: 0.16-0.41 clean.

## What was done

1. **Existing text?** None. No contemporary decipherment beyond the recipient's superscripts over three runs of R7486
   and his gloss on R7493 p. 1 ("der" over o., "von Kayser" over "5 83"); no clear copy; no edition or calendar (searched
   9 Oct 2026, see NOTES "Prior work"). The neighbouring DECODE records (R7460-R7467, R7501-R7507) belong to other
   files. So every reading rests on the images.
2. **Images.** The 32 DECODE page images of the nine records fetched with the project cookie
   (`research/reading_audit/b05_fetch.py`; saved only in the session scratchpad, not in the repository). Each page read
   in strips of 25-45% height at 1,700 px (`b05_crop.py`); margins rotated; one contrast-enhanced crop for the
   water-stained foot of R7490 f. 296v.
3. **Transcription.** The `[?]` words re-read line by line; corrections in `R74xx_corrections.tsv` (about 170 lines in
   all). The earlier transcription's "illegible" was mostly a hard Kurrent hand rather than lost ink: R7489 (called
   faded) and R7493 (called "water damage on all leaves") read largely; only the feet of some pages are really faded.
   Examples: R7489 "Lehns affaire", "allergnädigstes Decret", "6000 teutsche gegen 25 m. Frantzosen", "Feldstücke",
   "alea belli"; R7491 "Herr von Heinisch", "in Lateinischen eröffnen", "Est modus in rebus"; R7492 "allerunterthänigst",
   "Ihro Mt dem Herrn Rath", "zu welchem Ende Sie auch das 189 schreiben an sich genommen"; R7490 "vor der gerechten
   Partheÿ", "Drusenheim", "Jauer oder Schweidnitz"; R7486 "aber-mahls" (not "alt-mahl"), the P.S. "nec superiorem,
   nec parem, aut inferiorem".
4. **Runs.** Every letter-table run re-decoded (`b05_dec.py`); no key change. New readings of runs: R7488 "morgen oder
   übermorgen" (letters dropped by the writer), "Plessen" (a name), "eine convoy"; R7496 "ein leben ... führen so von
   vanitäten entfernet" (67 = v); R7490 "a[u]s Muscau" (u written oo). Code 131 (not 181) in R7489 P2 l.4; 268 (blotted,
   possibly 258) in R7494.
5. **Readings.** `R74xx_reading.md` built sentence by sentence (holes marked as in the brief: `[187]` unvalued code,
   `<e>` unvalued dotted sign, `[?word]`, `[word]`, `[…]`), English in `R74xx_en.md`.
6. **Word-by-word check** (`research/reading_audit/b05_align.py`): every unbracketed word of each reading looked up in
   the transcription, the corrections file and the run decodes. The check caught invented or normalised words, all
   corrected: R7491 "also sinister" (not written: the run is 58 31 61 32 48 44 = "sition", end of "proposition"),
   "erachtet ... improbiret [wird]" (MS "erachten ... improbiren"), "Zeitungen verlanget" (MS "Zeitung verlangen"),
   "wesswegen ... die Welschen wunder", "Vermuthlich" (unsure, now `[…]`); R7490 "cauta" (MS "Cives"), "unseren"
   (MS "unserem"), "prätendiret" (MS "prätendiren"); R7489 "ehe bevor ... einfindet" (MS "erwarten ... einfinden"),
   "es scheinet, dass Er nicht" (faded line, now `[…]`); R7486 "hat" (MS "habe"), "könnte" (MS "können"), "Heute hat"
   (unread, now `[…]`), "betrifft" (MS "betreffend[?]"); R7494 "um Vergebung" (MS "mit"), "Königl" (MS "König");
   R7492 "abstatten" (MS "ablegen"). The words left on the list are run decodes split across line ends, hyphenated
   words joined, and words read on the images that stand in the corrections files.
7. **Score** (`b05_score.py`: `_check_reading.score_text` on the reading body only, header, notes and close cut off;
   language de). Signs printed without their dot and abbreviations without the point, so the count is not cut at them.

## Result per letter (clean-sentence share, body only; before = audit figure on the whole file)

| letter | before | after | state | with clear-text numerals counted as words |
|---|---|---|---|---|
| R7486 | 0.338 | 0.29 | decoded, not read | 0.29 |
| R7488 | 0.265 | 0.556 | decoded, not read | 0.556 |
| R7489 | 0.333 | 0.545 | decoded, not read | 0.636 |
| R7490 | 0.29 | 0.551 | decoded, not read | 0.565 |
| R7491 | 0.316 | 0.609 | **read** (B) | 0.674 |
| R7492 | 0.306 | 0.371 | decoded, not read | 0.371 |
| R7493 | 0.16 | 0.23 | decoded, not read | 0.23 |
| R7494 | 0.412 | 0.611 | **read** (B) | 0.611 |
| R7496 | 0.35 | 0.421 | decoded, not read | 0.421 |

The bar (about 0.60 and coherent to a reader) is met by R7491 and R7494. In every other letter the clear German now
builds sentences; what keeps the share down is the code layer, not the reading of the hand: the open person codes
(187, 181, 166, 190, 258 ...), the unvalued dotted signs (<3>, <d>, <e>, <oo>, <ooo>) and, in R7486, R7490 and R7492,
passages where code follows code ("<d> [349] wird [187] ...", "<3> [355] <d> [349]") so that a sentence has three or
four holes. R7489 scores 0.636 when its clear-text numerals (6000, 25 m., 3 brigadiers, 400 officers, dates) are
counted as words; the checker counts every bare number as a hole, so it stays below the bar on the standard count.

## What stays open and why

* The person codes and dotted signs (outcome.gaps): no key material, as before. This is the blocker for R7486, R7488,
  R7490, R7492 and R7496, whose clear text is now read.
* R7493: the lower halves of ff. 303v-304 and the feet of ff. 305v-306v are faded or tide-marked; read only in part
  (blocker: illegible on the DECODE images; a reading of the original might do better).
* R7489, R7490: a few faded lines (R7489 P3a foot, P3b l.21; R7490 P5a ll.20-25 and the P.S. in the margin of p. 6).
* R7491: a three-line upside-down P.S. at the head of p. 4 and the margin note at "Hagenau", faded, not read.
