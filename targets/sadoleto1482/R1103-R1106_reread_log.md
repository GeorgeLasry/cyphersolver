# Re-reading log, R1103 and R1106 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b22)

## Starting point

Reading audit (22 Oct): both decoded, not read. R1103: `r1103_image_audit.md`, one isolated word ('vostro') from the
four-line block. R1106: `r1106_parallel_reading.md`, local cipher spans read sign by sign (grade C) beside the clear
slips 26a/26b, never written out as text; `_check_reading.py` on that file 0.456 (88/193, mostly its own prose).

## 1. Is there a text already?

- DECODE R1103 and R1106 fetched with the project cookie (`b17_fetch.py`): two page images each, no attachment, no
  comment block. R1103's record names the receiver as Ferdinand I (King Ferrante): Vestigia 1294 is titled 'Nicolò
  Sadoleto Ferdinando I d'Aragona részére' (incipit 'Per altre mie le...', explicit 'pagara una volta').
- R1103: no clear witness. Vestigia's neighbouring items are 13a (1295, the clear copy of R1104) and no. 13 (1296); the
  sweep of b. 1/9 recorded in NOTES found no 11a. No printed text of Sadoleto's despatches is known (MDE skipped him).
- R1106: yes, the two contemporary decipherment slips 26a (Vestigia 1319) and 26b (Vestigia 4004), cached in the main
  checkout's `img/v/`. Before this pass only local anchors had been read from them. Transcribed here in full as far as
  the photographs allow: `R1106_slips_26a_26b.txt`. 26a (10 lines, the p. 2 cipher paragraphs) is legible except two
  words; 26b (12 lines, the p. 3 cipher) is legible on its left half and faded on its right half on the only
  photograph, even in blue-channel local-contrast views.

## 2. R1106 reading

`R1106_reading.md` follows the slips and, where the cipher spans read under the working key give another word, the
cipher (apreso/compreso, suoi/soi, ha firmo/ha firmato, guera a X/guerra cum la Signoria de Venetia, potessi/potesse,
no sia/non sia, a me parla/cum mi parla, potro/potero, nel/neli). Translation `R1106_en.md`. No key change.
b17_score on the body 0.731 (19/26 'sentences', commas splitting them), explicit holes 0.846; but the third paragraph
(26b, p. 3) has holes in most of its sentences and does not build a continuous text. By the reader's test it stays
**decoded, not read**: paragraphs 1-2 (26a) hold, paragraph 3 does not. Blocker: illegible (the right halves of 26b and
of the letter's p. 3 are faded on the one photograph of each; the cached duplicate exposures add nothing).
Word-by-word alignment with the cipher was possible only for the spans already read in `r1106_parallel_reading.md`;
the cipher's faded right halves are the same blocker.

## 3. R1103

The block re-cropped from photograph (116) at native resolution, grey autocontrast, line by line (scratchpad). Line 1
shows the che (|2б) and non (636) groups and the sign shapes of the working key, but several words lose strokes (the
right end of l. 1, the middle of l. 2) and segmentation into signs is not stable, as the 20 Sept audit found. No word
beyond 'vostro' accepted. Stays decoded, not read. Blocker: illegible (faded signs on a single exposure; no clear
witness).

## Result

| doc | before | after | state |
|---|---|---|---|
| R1103 | one isolated word | unchanged | decoded, not read (illegible) |
| R1106 | 0.456 (collation notes) | 0.731 on a partial reading; 26a part holds, 26b part fragmentary | decoded, not read (illegible) |

Example (R1106, end of 26a and start of 26b): 'Et questo Re ha firmo proposito de non se scoprire et in niuno modo, anzi piu tosto
monstrarse neutrale [...] che involverse in guera a [X].' — And this King has firmly resolved not to show his hand, and
in no way, but rather to show himself neutral [...] than to involve himself in war with [the Signoria of Venice].
