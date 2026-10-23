# Re-reading log, R311 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.126). Four pages (IMG_R311_I2559-I2562), headed
"Di Vienna 29 7mbre 1629" (September; DECODE's November dating is wrong), register "A", p. 117; cipher with clear-text
lines interspersed; the last page ends with the catchword "per".

## What was done

1. **Despatch**: Kiewning 1897 Nr. 184 (Wien 1629 September 29, dechiffr. 18 Oct., Nunz. di Germania 119 fol. 113-133;
   edition lines 26624-26792 for this sheet). Kiewning prints this despatch in Italian almost entire.
2. **Alignment** (`reread_b01/R311_align.txt`): 40 cipher chunks at 0.14-0.62 cost per letter cover "Trattai col signor
   principe d'Echembergh ... de gl'interess-"; chunks 5.5, 5.15, 23.0 and 25.0 (0.8-1.0) are garbled decodes of printed
   text (slips in the figures), still located in the print. The clear-text lines on the sheet (DECODE: "Ina uolonoa sw
   enoneorre", "partieolammiena per per laffettuosa offerra", "poora considerar lequillo confidenoemenn", "quando ecnanero
   tanti" ...) are the print's words ("la sua volontà se concorrerà", "particolarmente per l'affettuosa offerta", "potrà
   considerar se quello cessi quando confidentemente", "quando cessassero tanti"), checked on the scan where legible.
3. **Reading** = the print, OCR corrected ("nnntio", "qnella", "ginramento", "ripntatione", "Maroheville", "toroato",
   "Bia certo" = "sia certo", "6C vorrà" = "e se vorrà" ...).
4. **Continuation**: the sheet ends in the middle of "interessati" with the catchword "per"; R312 begins "giustificate in
   tutto o in parte", i.e. Kiewning's next words. R311 + R312 are one despatch.

## Figures against the print

* "che questo e simili altri concetti fecero" (figures 47 che, 775 questo, … "altri"): print "in questo e simili concetti,
  fecero". The figures are followed (the print's sentence lacks a conjunction).
* "havendone una per il giorno seguente assai bella" (figures' order): print "una assai bella per il giorno seguente";
  print kept.
* "Mr. di Marcheville": figures [622] di mar[234]auille; 622 presumably "Monsieur" (unconfirmed).
* "da Roma sino a [352] del suo stato": 352 = confini, confirming the extra-group value.
* "e che il medesimo andava dalli altri [394] ancora": 394 = elettori (print "elettori"; follows 393 elettione).
* "baron di Questembergh" spelled out in the figures; "baron Verda" garbled (diol?7).

## Holes

None in the reading except the supplied end of "interess[ati]" (cut by the sheet; the word continues on R312).

## Group values

* 394 = elettori (print alignment, R311 run 9.0) — new.
* 352 = confini; 309 = cattolico; 655 = religione cattolica; 909 = sede apostolica; 297 = casa d'Austria; 224 =
  arcivescovo; 393 = elettione; 937 = trattato; 244 = armi; 340 = Casale (here written twice, 340 340): confirmed.
* 596 again after "al Signor" where the print has "principe Savelli": supports 596 = principe Savelli (R309, R311).
* 207 = consiglieri secreti: R311 "ne parlai anche con alcuni de 207" where the print has "con alcuni de consiglieri
  secreti"; this fits R309 "Ad uno 207 diedi un cenno" (regest "einem geheimen Rat"). 203 = consiglieri: R312 "de 203 li
  quali" where the print has "de consiglieri, li quali"; fits R310 "essendo stati fuori 203 appresso S. M.tà" (regest
  "die geheimen Räte") and R307 "con li 203".

## Result

Read: clean-sentence share 0.879 (`docs/_check_reading.py --file`; 114 sentences, 101 clean). Rests on Kiewning's print
(the Roman decipherment) matched with the figures throughout.
