# Re-reading log, R957 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b36)

## Starting point

Reading audit (22 Oct): "decoded, not read". The ciphertext-only key (`key.json`) gave "On promet (?) de toujours de
la part des François" and "le prince de Con[…] [323 441] qui vous formez des prétensions". Old reading body
(READING.md, R957 section), b17 plain LANG_=fr: **0.571 (4/7)**.

## 1. Is there a text already? Yes, on the DECODE record

- `research/reading_audit/b36_fetch.py` fetched R957 logged in: four images (1616 x 2309) and SofPe's transcription
  D1822. Every image opened (scratchpad `reread/R957/`): P1 the cipher page (f. 327v?, the figures, the clear close
  *Bonn ce 14 de Jan. 1759*), P2-P3 the clear letter (ff. 327-328: Lamberg, Frankfurt, Soubise, Hamburg, Crefeld, a
  postscript on the commission at Liège and the comte de Pergen), **P4 the contemporary decipherment of the cipher
  passage**, a separate leaf in another hand, never opened before (the September work rebuilt the key ciphertext-only
  without it). Transcribed: `R957_decipherment.txt`. The decipherer wrote *232* above the first *France*.
- Neighbours R954 (1635 Cardinal-Infant draft) and R958 (a 1647-98 key sheet) are unrelated. No print found (NOTES).

## 2. Alignment with the figures

`cipher/R957.txt` decoded group by group with `key.json` (`python dec.py R957a R957b`) and set against the decipherment.
They agree word for word once seven values are corrected; each holds at every occurrence in R956 and R957:

| group | was | now | occurrences | evidence |
|---|---|---|---|---|
| 232 | G? | France | 2 | decipherment, and *232* written over *France* by the decipherer |
| 327 | om | oc | 1 | pro-c-ède; then 327 < 330 *of* (one of the table's seven order breaks closed) |
| 131 | av | ay | 1 | *ayons* (decipherment); between 127 *au* and 135 *b* |
| 170 | con | cr | 2 | *Croÿ*; R956_14 *Crillon* (was "con il l on") |
| 323 | nous | o | 1 | Cr-o-ÿ; between 322 *non* and 324 *o* |
| 440 | vous | y | 1 | *qui y forme*; between 439 *x* and 441 *y* (a second order break closed) |
| 316 | ne | ni | 3 | preve-ni-r; R956_13 *Dume-ni-l*; R956_16 an unread name |

One disagreement: *supposition sans*, where the figures give `suppositi` + 357 (*pr* at its six other occurrences) +
*sans*; the decipherer wrote *Sa*, struck it and wrote *supposition*. An encipherer's slip; the reading follows the
decipherment.

## 3. Reading and score

`R957_reading.md` (the cipher passage, the decipherer's spelling), `R957_en.md`. Every word is in the decipherment and
carried by the figures (except the slip above). Supplied words: none. Look-alike letters: 0.

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=fr) | 0.571 (4/7) | **0.857 (6/7)** |
| reading body, b17 HOLES=1 | - | 1.000 (7/7) |

The unclean sentence is *beaucoups de mesintelligences* (period spellings). Reader's judgement: every sentence holds.

## Result

Read from the contemporary decipherment on the record, aligned with the figures; grade A. Side effect for R956 (already
read): 170 *cr* gives *Crillon* in run 14 ("prussien, Crillon, le prince Camille") and 316 *ni* gives *Dumenil*.

## Open

- Nothing in R957. The excerpt leaves the clear text of the letter on the images (not a gap of the cipher).
