# Re-reading log, R301 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.136). Two pages (IMG_R301_I2533, I2534), headed
"Vienna 25 Agosto 1629 / All'Ill.mo Sig. Card. Padrone / C 76": cipher with many words in clear; the first clear line
("Avanti hieri mi conferì il P. Magno di haver fatto un'altra scrittura") is written above the first cipher line and is
also enciphered in it. The automatic alignment (`reread_b01/R301_align.txt`) found no verbatim print (costs 0.9-1.2).

## What was done

1. **Despatch**: Kiewning Nr. 166 (OCR "100."; 25 August 1629, dechiffr. 13 September; Nunz. di Germania 119 fol.
   59-61; edition lines 24580-24601): Valeriano Magni's new writing on the Carolina. Register letter C, the third
   despatch of the day (A = Nr. 164, R297+R299; B = Nr. 165, R300). Regest in German with two Italian passages:
   "quando l'efficacia et habilità ... e della sede apostolica" and "pupilla de gli occhi dell'imperatore". The first
   is in this sheet as a mixed clear/cipher stretch (p. 2 ll. 4-6) and the reading follows the print there; the
   alignment had missed it because the clear part ("s'impegnasse tanto avanti e facesse") interrupts the cipher.
2. **Clear words**: re-read on full-width strips and 2.5-3x crops of both scans; DECODE's clear text was often wrong
   ("miseria" for "materia", "rapportavi fui" for "rappresentateli fin", "d'impegnarmi tanto quanto e facevi" for
   "s'impegnasse tanto avanti e facesse"); corrections in `R301_corrections.tsv`. The right edge of p. 2 is cut off in
   the scan (last word of ll. 2, 11, 13, 17: "facesse", "haveva", "Veram-", "qu-").
3. **Cipher**: read run by run with the codes (dump script in the scratchpad). Points settled: "per dar a S. M.tà"
   (the "?" after 67 is the 0 of 670), "ma non volermela" (53), "con verità che io", "Carolina" (32 00 36 70 66 97 00),
   "veduta" (the decoder's [906] is 90 misread), "comunicarmi la" (the decoder's {Baviera} 366 is 36 63), "giorni"
   (999 426 is 99 94 36 misread), "la detta scrittura", "all'Imperatore" (460 at the end of p. 1 l. 18), "di questa
   maniera" (775), "[dell']Imperatore" and "[i]l P. Valeriano" (p. 2 ll. 3-4), "lettera a S. M.tà" (620 = 670 with the
   2/7 confusion), "dal P. Magno" (62 99 96, cf. the first-wave lesson).
4. Kiewning's regest checks the sense of each paragraph.

## Holes and why

* "[?contro] i PP. Gesuiti": figures 52 35 0 1? 62 0; "con-t-" is carried, the rest not; the regest says "noch mehr
  gegen die Jesuiten als die erste".
* "[?darla] […]", "potesse [?spiccar]", "che non per questo […] [?sarebbe] impedito di [?af]firmar": uncertain figures in
  DECODE's transcription (?) at those places, not resolved on the scan.
* "s[…] avanti almeno otto o dieci giorni": figures 43 22 02 36 25 00 64 (s-parta-se), sense "to hold it back"; not
  resolved.
* "correttione [?fra]terna": figures 4? 5/3? 6 2 0 35 90 46 29 0?; "fraterna" fits all but the first.
* "che […] et esser risoluto": 47 73 74 25 35 00 22 692 26, not resolved.
* "Nichil[spu]rgh": 29 50 49 66 232 236 36 99 55; Nikolsburg by the regest.
* "della fede […]": DECODE's figures there are all uncertain (7? 7? 8? 7? 3?).
* "a questa [662]": 662 in the R range (after 649 Republica, before 663 Roma); "risolutione" would fit.
* "[762]": between 759 nondimeno and 763 però; "onde" would fit the sense.
* "mostrando io aderire […]", "ragioni del Padre, […]", "persuaso [532] dar", "regola[665]", the sentence before "con
  pensiero": figures read but not making sense (per ma 692 ma da; o 270 no di fuso in altre dalle il fa; che che i
  mandato per e a).
* "domani qua […] egli venuto": figures "si o".
* "hanno fatta […] impressione", "toccar […] in cose particolari": "a il e", "e si que".
* "cotesta [920]", "la persona stessa di […]", "e di […] in questa materia": a group not identified / a group missing
  (probably N. S.re).
* "prudenza e […]": one cipher pair (20) between two clear words.
* "restino […] del negotio": figures "gl a so 922 a 926", not resolved.
* "di molto […]": 22 07 755.

## Group values (proposals; extra_groups.json not edited)

* 440 = Gesuiti: "li PP. [440] li quali non ha dubbio che sono pupilla delli occhi dell'Imperatore" (Kiewning: "Die
  Jesuiten sind die pupilla de gli occhi dell'imperatore"); "più [?contro] i PP. [440] della prima" (regest "gegen die
  Jesuiten"); "o per parte de' PP. [440]"; G range between 439 generale and 444.
* 662 = [?risolutione], 762 = [?onde]: see holes.

## Result

Read in part: all paragraphs build sentences; the holes are single words or short stretches whose figures do not
resolve (listed). Clean share 0.63 (`docs/_check_reading.py --file`, 58 of 92 sentences), from 0.136. The despatch
continues on register p. 78, which is not among the DECODE images (2534 is followed by 2535 = R302, "A 79", 28 August; R303 is the end of R302).
