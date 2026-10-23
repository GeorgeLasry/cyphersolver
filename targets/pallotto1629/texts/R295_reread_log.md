# Re-reading log, R295 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.111). One page (IMG_R295_I2519, 1413 x 2085),
headed "[Vi]enna 18 Agosto 1629 / All'Ill.mo Card. Padrone / B / 55".

## What was done

1. **Existing text?** Kiewning 1897 Nr. 161 (Wien 1629 August 18, dechiffr. 6 September; Nunz. di Germania 119
   fol. 40-41), edition lines ~24181-24197: a German regest of the opening ("Wenn Savelli wegen der Propstei Halberstadt
   spricht, wird es gut sein, dass man zuerst ..."), then the Italian from "motivasse qualche difficoltà" to "con la prima
   occasione", then the regest "Doch überlässt er es Barberini". The decode aligns with the Italian at 0.35 (run 5.1),
   0.43 (run 7.0) and 0.13 (run 9.0) cost per letter; that stretch of the reading is the print with its OCR corrected
   ("prepositnra", "dnbito", "veriti", "ayviso", "ottennta").
2. **Opening and close** read from the figures with `reread_b01_show.py` and full-resolution crops of the scan. The first
   cipher line carries a contemporary clear decipherment above it ("Quando s'inclini, e si trovino le cose in termine di
   poter"; DECODE read "erouiste"); the figures confirm it (772 = quando, 23 97 32 66 97 50 = s'inclini, 35 36 70 . 97 03 =
   trovino, 25 90 36 63 95 = termine).
3. Group-by-group checks on the scan (`R295_corrections.tsv`): 692 Signor (decoder had "6 97"); Stralendorf spelled
   92 36 72 90 29 33 07 36 44 in both places (decoder had made {Conte}{ancora}[644] / [729]...[644] of it); 577 = N. S.re
   after "buona volontà di" (DECODE 5 7? 2? -> decoder {uffitii}); 95 "ne" for DECODE's 94 in "quando ne parlerà";
   "verbi" 06 90 36 24 50; "domandata" 33 70 62 29 67 35 00; "e che n'è" 90 1 47 1 95; "ho che" 55 70 8 47 (DECODE
   "5 5 7 8 8"; the decoder's [557]).
4. "riconosciuta veramente": the figures after riconosciuta (36 50 52 07 23 32 50 06 25 00) are "6 25 00 8 06 90 36 2(0)
   8 755" on DECODE; the scan shows only one repetition of "2500" and then 06 90 36 20? 755 = ve-r-a-mente. The extra
   "6 25 00" is left out of the reading as a repeated/struck group (it reads "-ta" again).

## Print vs figures

* "alla quale si era data": the figures have 769 (qualche) and 69 (di) where the print has "quale si". Sense and print
  agree on "quale si"; read as a slip (7/9) and a 65/69 confusion.
* "ottenuta la gratia da S. B.ne": the figures have 577 (N. S.re); the print's wording kept.
* "con la prima occasione": the figures have no "la" (52 1 22 36 50 62 8 567); the print's wording kept.
* "possa dare altro avviso": figures "posa dar altra {aviso}"; print kept.

## Holes and why

* The closing "33" after the last "V. S. Ill.ma" (end of the line, followed by a dash): one letter d, no word; left `[…]`.

## Group values established here (proposals; extra_groups.json not edited)

* 692 = Signor confirmed twice in this record ("e 'l signor di Stralendorf", "al signor ambasciatore", "al signor di
  Stralendorf").
* 577 = N. S.re confirmed ("dalla buona volontà di N. S.re e dall'intercessione di V. S. Ill.ma"; "la gratia da 577",
  print S. B.ne).
* Stralendorf has no nomenclator group: it is spelled out, 92 36 72 90 29 33 07 36 44.

## Result

Read: every sentence holds; one trailing letter unread. Clean-sentence share 0.727 by `docs/_check_reading.py --file`
(the unclean "sentences" are the English header lines and the proper names Stralendorf/Alberstat).
