# Re-reading log, R303 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.152). Two pages (IMG_R303_I2537, I2538), no
heading, register number 83; p. 1 mixes cipher and clear words, p. 2 is cipher only. No `_align.txt`.

## What was done

1. **Despatch**: found by content in Kiewning. The clear words ("Quel che con altre mie ho scritto della [fretta ...
   Wolestain]", "Aspetto con desiderio la risolutione circa [il visitatore ... Aquileia]") and the decode match the last
   paragraph of the regest of Nr. 167 (28 August 1629, edition lines 24736-24763): Wallenstein's haste heard "aus dem
   Munde der Hauptminister, von Eggenberg und dem Kaiser selbst"; Leopold Wilhelm's indult; the imperial letter to
   Barberini; the closed letter for the Emperor; the visitor for Aquileia; Savelli and the promotion. So R303 is the end
   of despatch "A" of 28 August, whose first sheet is R302 ("A 79"); its opening words ("... non l'habbia, venerdì
   spedirò di nuovo") finish R302's last matter (the packet for Torquato Conti). Kiewning's print has no Italian here.
2. **Clear words** re-read on the scans (corrections in `R303_corrections.tsv`).
3. **Cipher** read with the codes; mis-segmentations fixed by sense: "uffitii passati" (572), "Spagnuoli" (966/926),
   "rimunera[tione]" (the decoder's [259][425]), "staccato" (s-ta-ta-c-a-to), "ma[no]" ({munitione} 520).

## Holes and why

* Opening "e m[…] non l'habbia, [?venerdì] spedirò": figures 90 77? 20 53 (m-a-non) and 8 6 9 0 9 5 3 6 6 9
  (?6 90 95 36 69 = venerdì if the first 0 was read as 8); the sentence's start is on the missing pp. 81-82 or at the end
  of R302.
* "[?quella] volta": the figures are 774 (quello); "questa volta" is the expected phrase.
* "dallo stesso ro[…]": figures 46 03 at the line end, the right edge cut; the regest has "dem Kaiser selbst".
* "accennato […] difficile": figures 36 50 22 62 50 63 625 (rip mai mi + Palatino) not read.
* "al [690] Leopoldo Guglielmo": 690 in the S range, "Serenissimo" would fit; not confirmed.
* "ma d[…] [930] […]rò moto alcuno": 33 930 40 46 07; sense "I shall make no move" (regest: "wird er sprechen, wenn
  Barberini es wünscht").
* "dalla Maestà [564]ma": 564 not identified (the regest: "das kaiserliche Schreiben an Barberini").
* "diocese di [?Aquileia]": 254 (A range); regest "für Aquileja".
* "a […] N. S.re et a cotesta […]": figures 99 06 00 (gua) and 99 20 (ga), not read.
* "ne […] havere conseguito": 95 06 236 07.
* "la mia [326] di […]": 326 (cifra?) and 99 07 29 03 309 369 20 73 644, not read.
* "cotesta [920] […]": 920 also in R301 ("cotesta [920], la sacra congregatione"); S-V range, "Santa Sede" would fit;
  the last figures (2, 722) not read.

## Group values (proposals; extra_groups.json not edited)

* 572 = uffitii confirmed here ("Delli [572] passati da cotesto ambasciatore cesareo"). 254 = [?Aquileia]; 920 =
  [?Santa Sede]; 690 = [?Serenissimo].

## Result

Read in part: all paragraphs build sentences; holes are single groups. Clean share 0.712
(`docs/_check_reading.py --file`, 47 of 66 sentences), from 0.152.
