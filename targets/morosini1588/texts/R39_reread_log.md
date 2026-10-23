# Re-reading log, R39 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R39_decryption.txt` (DECODE D1703, KaJo, Feb 2017) scored 0.694 clean;
a single leaf (289r–v), the duplicate ("dup. d.gli 8 di Decembre") of part of the cipher of 8 December 1588.

## 1. Is there a text already?

- DECODE "cleartext" image D1063 (checked on the contact sheet): a covering letter in clear, not a decipherment.
- Tempesti (1754) covers the Saluzzo crisis (book VII ff.) but no passage paraphrasing this sheet was found (searched
  Saluzzo, Guisa, Lione, artiglieria).
- Rome's decipherments: ASV Francia 27 (not imaged).

## 2. Hand re-parse

`R39_corrections.tsv` (13 rows): "né ho potuto", "longam. tratato", "la sola restitutione", "et quando sua Alteza si
contentase" (spurious dot 153), "a l'[e]stirpatione", "pezi d'artegliaria", "[I]o non poso sapere" (64 = per inside
sapere), "uedo" (spurious dot 191), "gagliardam.", "douerei". No image check was needed for the sense; the two open
stretches were not checked on the image.

Aligner (`reread_b00_align.py R39`): TOTAL R39: 384 words, 0 supplied, 2 partly (the two [?] words).

## Result

Before 0.694 -> after 0.688 on the checker (a short text: the clerk's spellings and the bracketed letters weigh more);
by hand the sentences hold throughout, with 4 unread stretches […] (the opening, one clause on 289r, the end of the
sheet) and 2 partly carried words in ~380 words. Grade A for what the sheet carries; the duplicate is incomplete (it
breaks off at the foot of 289v; the original despatch is not in this record).

## Still open, and why

- The opening figures and "che […] che egli" (289r ll. 7–8) do not parse; the end of the sheet (289v l. 15) is cut
  off. Blocker for the rest of the letter: the original of 8 December is not imaged with this record; Francia 27
  (physical access).

## r2m, 23 Oct 2026 (Claude Opus 5.5): partial image check (IMG_R39_I210_P1, scratchpad)
- 289r l. 5 "de [?la] S. M.tà": the row reads "... 6 1 7 5 1 1 1̇ 3 ..." with ink blots over the figures after it; the
  figures for "la" are not clearer on the image than in the transcription. Kept.
- The other holes of R39 (289r l. 2 opening, ll. 7-8, ll. 12-13, 289v l. 15) were cropped (bleed-through and blots
  make the digit rows hard to segment at this resolution) but not settled in this pass: R39 is not counted as done.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

The rest of R39 (after r2m's 289r l. 5): each hole located (`research/reading_audit/r2p_holes.py`), its line looked
at on the image (scratchpad `reread/r2p/crops`), cancellation strokes looked for, the figures parsed
(`r2p_parseall.py`). The encipherer added a 37 (u) above the end of 289r l. 12 ("consiglia-u-a"), an insertion, not a
cancellation.
Filled:
- 289v l. 6 "Io non": "8 7 1 9 1 7 1" on the image: a single null 8, io, non (as in R19/R20).
Left, with blockers (289r l. 2 the opening "5 111.": blotted at the line start, illegible):
- 289r l. 2 "[…] N S": "5". Blocker: illegible (blot).
- 289r l. 2 "N S […] A poco": "7 2". Blocker: too-short.
- 289r l. 7-8 "marchesato che […] che egli": "1 1 4 1 7 1 2 6 9 1 3 7 3 5 2 | 5 0 2 1 4 5 2 1 0 0 5 2 6 7 3 0 2 1 0 0 4 0 5 0 7 5 0 2 143^. 7 0 9 1 1 7" (best parse "xsidouealasaredifarglila[guerra]poi"). Blocker: no-key-material.
- 289r l. 12-13 "seuera dimostratione consigliaua[no] […] et": "1 9 4 5 1 7 4 0 5 0 1 7 2 1 3 7 | 2 1 2 6 1 9 1 7 7" (best parse "consigliauatoii"). Blocker: no-key-material.
- 289r l. 16 "a l [e] stirpatione del": "7". Blocker: too-short.
- 289r l. 23 "Maestà non l[o] faria": "5 0". Blocker: too-short.
- 289v l. 2 "egli mostraria al[a] S M": "2 5 0". Blocker: too-short.
- 289v l. 7 "queste cose [?che] pure si": "5 1 9 1 4 1 5 3 8" (best parse "tohe"). Blocker: no-key-material.
- 289v l. 15 "non douerei […] V S": "8 0 0". Blocker: too-short.
- 289v l. 15 "Ill ma […]": "4 7 9 9 169^. 0 2 1" (best parse "sioo[u.s.]na"). Blocker: no-key-material.
Result: 1 hole filled; R39 is now checked on the image throughout; 10 left (with r2m's 289r l. 5), each with its blocker.
