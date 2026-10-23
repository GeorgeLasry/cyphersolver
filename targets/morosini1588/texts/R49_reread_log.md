# Re-reading log, R49 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R49_decryption.txt` (character-model segmentation of DECODE's
transcription D1714, KaJo, Feb 2016, under Meister no. 40) scored 0.68 on 19 sentences; the gist (the Archbishop of
Lyon's refusal) was visible but with garbles ("gena signament", "no se interogato dal uescouo di boue sola asistenza").

## 1. Is there a text already?

- DECODE: one cipher image (404v), no cleartext images. The page is the middle of a letter (begins and ends in
  mid-sentence); the rest of the letter is not in this record.
- Tempesti (1754): no paraphrase of this page was found in the scratch OCR (searched for Primate, Beauvais).

## 2. Word decode and hand re-parsing (R49_corrections.tsv, 17 rows)

The decoder had most words. Re-parsed: "con gl'asignamenti", "con l'asistenza" (not "la sola asistenza"), "Boues"
(Beauvais), "primate di Francia", "simplicem." (m + 8). Image check (crop, scratchpad only): ll. 7–8, where the
transcription's dotted "713" is not on the page (the line begins 2 5 1 7 1 7 0 9 1 1 5 4 5: the end of eclesiastici,
then a stretch that does not parse before "interogato").

## 3. Alignment

`python reread_b00_align.py R49`: `TOTAL R49: 218 words, 0 supplied, 0 partly`.

## Result

Before: 0.68 (on the run-together character decode). After: 0.59 clean-sentence share on the "## Reading" body (hole
rate 0.117): on a page of 220 words the checker's sentences are short, and the clerk's spellings (procurarano,
asicurato, comisari, simplicem.) and the "tà" of "S. M.tà" each count as holes, so seven of seventeen sentences fail on
two such words. By hand: 3 holes ([…] twice, one [?fose]), every sentence carried. Grade A by the sentences; the
checker's number stays below the 0.60 bar for the reasons given.

## Still open, and why

- l. 8: "1 7 0 9 1 1 5 4 5" before "interogato" (the verb that says the archbishop should be questioned) does not parse
  on the image either; the encipherer's slip.
- The page begins and ends in mid-sentence; the rest of the letter is not in the record (outside blocker).

## r2m, 23 Oct 2026 (Claude Opus 5.5)
- The one cipher hole (l. 8, "1 7 0 9 1 1 5 4 5" before "interogato") was checked on the image on 22 Oct (as
  transcribed); its parses enumerated here (research/reading_audit/r2d_mparse.py: rporse, inores, iquxes ...): none is a
  word. Kept. The opening and the end are the edges of the sheet (the rest of the letter is not in the record). R49 is
  done: no hole left unchecked.
