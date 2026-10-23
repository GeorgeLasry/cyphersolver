# Re-reading log, R18 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R18_decryption.txt` (character-model segmentation of DECODE D1686, TimB,
Jan 2016) gave the gist (Council of Trent, Gallican liberties, Estates General) with garbles in most lines.

## 1. Is there a text already?

- DECODE "cleartext" images (D973, D1111, D1112): contact sheet checked — the covering letter in clear (ff. 30–31) and
  an address leaf; not a decipherment. No interlinear glosses on the cipher pages (32r–35r).
- Rome's decipherments are in Segr. Stato Francia 27 (Hübner), not imaged: blocker = physical access.
- Tempesti does not paraphrase this letter closely (the Trent negotiations of summer 1588 are summarised only).

## 2. Word decode and hand re-parsing

Started from `R18_worddecode.txt`. About one word in eight needed re-parsing; nearly all are carried by the
transcribed figures as they stand (`R18_corrections.tsv`, basis "figures"):

- Decoder vocabulary gaps or wrong choices: "o conditione" (191 + 76 con), "sentire a modo alcuno", "acetarlo",
  "aquistarlo", "restritione", "odiosa", "condurci", "uado leuando dele sospecioni", "ala stirpatione", "hauti
  rinfrescamenti", "ch'egli non li uorebe", "io non mancarò di" (decoder "iormania cardi"), "io disi" (decoder
  "promisi"), "come a uero re".
- The abbreviation m + 8 for -mente (uniuersalm., impertinentem., facilm., precisem., liberam., segretam., chiaram.,
  manifestam., apertam.) and 8 for other abbreviations: "di bo. mem." (26 7 42 91 8 20 35 20 8) = di bona memoria.
- New names: "mons. il uescouo di Rimini" (135 + 00 17 20 17 01 17; G. B. Castelli, nuncio 1581–83), "Sciartres"
  (Chartres: 45 25 17 21 00 15 00 35 45), "l'arciuescouo di Lione" (133 genuine), "Aragone" (initial a not carried).
- Encipherer's slips kept as such: "contrauenire" written twice (033r l. 15–16); 129 alone for "il duca"; 166 where
  161 (quanto) is meant (035r l. 5).

## 3. Image checks (crops in the scratchpad)

- 32r l. 2 (opening): figures as transcribed ("1 9 1 5 2 2 9 4 7 2 2 1 0 9 1 8"); no parse. Left open.
- 32v ll. 10–12: l. 11 begins with 2, not 7 ("dela Sorbona" confirmed); l. 12 "6 2 [mark] 2 2 8 4 5 2 5 ..." = da
  Sciartres with one figure too many.
- 33r ll. 20–21: "6 4 5 4 9 6 9 5 0 2 1 / 4 5 2 1 3 7 2 1 2" as transcribed; no parse (left "per […]").

## Result

Before: 0.715 clean-sentence share (`_check_reading.py` on `R18_decryption.txt`). After: 0.80 on the "## Reading"
body of `R18_reading.md` (1,480 words; the clerk's spellings count as holes).
By hand: 7 holes ([…], [162], [quanto]/[contrauenire]/[di] supplied or bracketed) and 4 partly carried words in about
1,450 words; every sentence of the letter carried. Grade A-/B: a dozen single-figure corrections from context.

## Still open, and why

- The opening group (32r l. 2), "per […]" (33r l. 20), "nela […] N. S." (33v l. 6), the dotted [162] (32v l. 14) and
  the closing figures (35r l. 19): no parse fits the transcribed figures, and the image shows them as transcribed. No
  outside text: Francia 27 (Rome's decipherment) needs physical access.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located on its line (`research/reading_audit/r2p_holes.py`), looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for, figures parsed under Meister no. 40 (`r2p_parseall.py`).
The -m[ente] and bo[na] me[moria] expansions are the encipherer's abbreviation (m or word + null 8), not holes.
- 32r l. 2 opening "191. 5 2 2 9 4 7 2 1 0 9 1 8" (seen before, as transcribed): no parse. Blocker: no-key-material.
- 32r l. 3: the image has "8 7 1 9 1" = io: filled.
- 32r l. 4 "[?oporsi]": "8 7 1 9 1 0 7 9 1 4 5 9" as transcribed (i o p o r s o); kept partly. Blocker: no-key-material.
- 32r l. 9: the image has "2 6 8 2 1 0 0 2 1 4 0 9 1 0 1 3 5" (DECODE drops a 2): "d'Aragone" filled.
- 32v l. 12 "[di]": only a null 8 between "Sciartres" and "dimostrare"; supplied, kept.
- 32v l. 14 "[162]": "8 1 6 2" after "Dio"; no dot is clear on the image; neither 162 (not in the key) nor the letters
  (rta / et a / d) fit. Blocker: no-key-material.
- 32v l. 22 "[?dato]": the image reads "8 6 2 1 1? 1 9 1" (DECODE "8 6 2 1 5 1 1 9 1"); no reading gives dato. Kept
  partly. Blocker: illegible (one figure in doubt).
- 33r l. 16: the repeated "contrauenire" is struck through with a line on the image: a cancelled dittography, now left
  out of the reading (was "[contrauenire]").
- 33r ll. 20-21 "per […] sopra": as transcribed (seen before); no parse. Blocker: no-key-material.
- 33v l. 3 "d[i] Dio": "6 2" at the line end (d), as transcribed; kept. Blocker: no-key-material.
- 33v l. 6 "nela […] N. S.": "1 2" before 111 on the image (z or r a). Blocker: too-short.
- 35r l. 5 "[quanto]": the figure is 166 (questo) on the image, as transcribed; kept. Blocker: no-key-material.
- 35r l. 19 closing "8 4 2 2 2 7 5 2 111. 0 9" (the image has a third 2): no parse. Blocker: no-key-material.
Result: 3 holes filled (io, Aragone, the cancelled repetition removed); 10 left, each with its blocker.
