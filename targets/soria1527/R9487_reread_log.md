# Re-reading log, R9487 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b35)

## Starting point

Reading audit (22 Oct): "decoded, not read": the Claro (f. 34r) reads for A and the closing paragraph; B and the start
of C are torn half-lines. Before: `claro.md` scores 0.548 on `_check_reading.py` (file as a whole).

## 1. Is there a text already?

- DECODE R9487 re-fetched with the project cookie (`b35_fetch.py`): 4 images, no attachment, no comment. All four
  opened. The Claro on f. 34r is the only decipherment; the letter carries section marks A, B (f. 31r margin) and C.
- Neighbouring records R9486 (RAH 9/15) and R9488 (RAH 9/28): other volumes, nothing for this letter.
- Print: none found (not in the 1527 *Cartas* searched for soria1523).

## 2. The cipher, read on the image

The torn parts of the Claro are B and C, and their cipher is intact: **f. 31v, 8 lines (B)** and **f. 33r, 5 lines
(C)**. Both transcribed sign by sign from the DECODE images at full size (2.5x crops, scratchpad only):
`R9487_cipher_signs.txt` (sign names of `../soria1523/keyB.md`, a decode note per line). Decoded with key B:

- **B confirmed against the Claro where it survives**: *...presos en Roma ... de los ... se avian soltado* (Claro *se
  havian soltado*), *y huido a Narni* (∞ y m+ c y 4 = a-n-a-r-n-i), *es de maravillar de qualquiera
  des-con-cierto* (Claro *de qualquier desor[…]*), *esta la gente sin obediencia* (pob + y = si-n; xoc = gente, also in
  C *gentes*), *y con algunas diuisiones* (Claro *y con alg[…]*), *como conviene a su servicio* (peb h 4 r = servi-c-i-o),
  *alla era arrivado* (zeb = alla), *el [tob] del Vasto y dize que los ... venian* (Claro *el marques del Guasto y dize
  que los*).
- **New words where the Claro is torn**: *que si es cierto seria [xad] de inconviniente*; *qualquiera desconcierto que
  a [pur] en el dicho [yal]*; *algunas diuisiones*; *alla era arrivado el [?principe] [?de Orange]*; *venian con el
  [yal]*; in C *no [?devan] de usar de [?sacatamiento] ... contra [par] y hazer matrimonio con Francia*.
- Key observations (not adopted into keyB.md; one letter each): ∂ = s (*divisiones*, *algunas*, *usar*, *des-*;
  keyB has δ = e, a different sign); ꝗ = v and i (*maravillar*, *Narni* context, *diuisiones*); +o = y (the word *y*,
  three times); g = d (*soltado*). Code groups seen and valued by the Claro: zab = algun-, zuf = como, zeb = alla, xoc =
  gente, zif = -cierto, tob = marques (?). Groups left open: xad, soc, pur, pib, yod, ync, par, yal, tal, sab, saf, pil,
  pef, ꝑi.
- Where the Claro and the figures differ (C: Claro *por […] fazer*, figures *contra [par] y hazer*; Claro *dexan*,
  figures *devan*), the reading follows the figures with `[?]`.

## 3. Alignment

Every B and C word not in the Claro is in `R9487_cipher_signs.txt` with its signs; codes without value stay `[code]`;
partly carried words `[?word]`. Supplied words: none.

## 4. Score

| | before (claro.md, whole file) | after (R9487_reading.md, body) |
|---|---|---|
| b17 plain (LANG_=es) | 0.548 | 0.50 (11/22) |
| b17 HOLES=1 | — | **0.682 (15/22)** |

Early Spanish (1527): the explicit-hole figure is the bar, 0.68. Reader's judgement: A, the end of C and the closing
paragraph hold; B now holds in outline but has 9 holes in 4 sentences; the first sentence of C does not hold (the
Claro is torn and the cipher leaves *servido ... [par] [yof] ... era* unread). Polyphonic signs (ꝗ i/v, ∂) chosen by
sense in about 12 letters of B and C, over 3% of those passages. Stays **decoded, not read**; the reading is kept.

## Open

- Code groups xad, soc, pur, pib, yod, ync, par, yal, tal, sab, saf, pil, pef - blocker: no-key-material (key B
  lacks them; Soria's 1523 letters give no values).
- C1 *peb yic ƀ7∂ zog par yof m+r9c4m+ ƀ7cm+7c∞r* - blocker: no-key-material (signs read, sense not reached).
- Last cipher lines at the foot of f. 31r - blocker: illegible (torn and faded).
