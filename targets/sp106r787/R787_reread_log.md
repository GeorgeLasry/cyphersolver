# Re-reading log, R787 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b35)

## Starting point

Reading audit (22 Oct): "decoded, not read": no text of the letter in any checkout. Before = 0.00.

## 1. Is there a text already?

- DECODE R787 fetched with the project cookie (`b35_fetch.py`): 2 images (ff. 216-217), Pettersson's transcription
  (D1811), Lasry's key SP106-2 (D3071), plaintext (D3072), interlinear (D3073); files now in `decode/` (git-ignored).
- Images opened at full size: no decipherment. **Found: a covering note in cipher in the margins of f. 217** (four
  lines of dot-separated figures, two along each edge, the second pair upside down to the first), in no transcription
  and not in Lasry's plaintext. Transcribed: `R787_margin_signs.txt`. It decodes with the same key: *Celle ici est un
  duplicata, auquel je joins le pacquet ci-enclos que j'ai receu de la cour. A [75] ce vint e[t] trois aoust* and in
  clear *sty. vet.* The duplicate was forwarded on 23 August O.S. from the place coded [75], the place of the f. 219
  letter of the same key ("[103] a [75] ce [30] aoust").
- Neighbours: R786 (Hungarian, other archive), R788 (ff. 218-221, f. 219 in this key; images cipher only).
- Print: none found (Lasry's note; Adolph's *Collected Letters of Jermyn* has no letter of 19/29 July 1645 in French).

## 2-3. Decode and alignment

- Signs `R787_signs.txt` (Pettersson's rows + `R787_corrections.tsv` + Lasry's & signs), decode `R787_decode.txt`
  (`b35_sp106.py`). Corrections: the dates 19/29 (head and foot) are fractions in clear, not groups 29 19 / 19 29;
  "9" and "1." are numerals in clear; 06 is 6 with the 0 struck (PREVAULT).
- The & sign: Pettersson leaves it out; Lasry's plaintext has 20; two checked at full size (after 64 on P1 l. 5,
  after [116]s on l. 4): drawn as an 8 with a flourish. Kept from his plaintext.
- Encipherer's slips, each checked on the image (the figures are as transcribed), read with `[?word]`: 58 for P twice
  (*imprimer*, *apres*; 58 = I at its six other occurrences), 4 for U (*heure*), 13 for R (*Parlement*), 31 for L
  (*lui*), 33 for T (*utile*), 24 for L (*il*), 22 for E (*le*), 16 for A (*Orleans*), 27 for X (*paix*), 53 for L
  (*la*), 21 for I (*distribution*), 41 for E (*le*): 13 letters of 1,643 = 0.8% (under the 3% look-alike limit).
- Code 116 = *lettre* adopted by sense (flagged): holds at all five occurrences in this key (here 2, f. 219 3, one of
  them "vos deux [116]s des douze et vint six d'aoust").
- Alignment with the decode (`b35_align.py`): 18 differences, all the slips above, the [lettre] code and the clear
  *sty. vet.*; supplied letters bracketed (*apr[e]s*, *e[t]*).

## 4. Score

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=fr) | 0.00 | **0.457 (16/35)** |
| reading body, b17 HOLES=1 | — | 0.657 (23/35) |

French of 1645: the plain figure is the bar. The sentences are built, but the nomenclator numbers carry the names
(64 ×6, 103 ×3, 61 ×3, 62 ×3, 104, 75, 74 ...) and fall in most sentences. Stays **decoded, not read**, with the
partial reading kept (`R787_reading.md`, `R787_en.md`).

## Open

- Nomenclator numbers 61-121 (18 distinct, 30 tokens, besides 116) - blocker: no-key-material (Lasry's key lists
  none; f. 219, the only other letter in the key, gives no values).
- *[?quartage]* (P2 l. 6, "un eschec grand quartage de Montrosse"): the figures are clear and read QUARTAGE; no
  word fits and no parallel text exists - blocker: no-key-material.
