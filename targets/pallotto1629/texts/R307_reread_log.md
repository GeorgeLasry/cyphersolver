# Re-reading log, R307 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.105). Three pages (IMG_R307_I2549-2551), no heading,
register numbers 97 (p. 1) and 98 (p. 3); cipher with long clear passages on pp. 2-3.

## What was done

1. **Continuation of R306**: R306 (Nr. 176, "A 93") ends at the foot of its p. 4 with "... la mattina della natività
   della Madonna" + 22 02 36 ("par"); R307 begins 66 50 24 90 36 50 65 62 8 755 ("l-iberissimamente") and runs on
   through the rest of Kiewning Nr. 176 to its last words ("per quanto dice, molto grata S. M.tà", checked on the scan).
   No "lò" is written between the sheets: the writer seems to have let one "l" serve both words. R307 is therefore the
   last three pages of Nr. 176, 15 September 1629, not a separate letter. DECODE has no date for it.
2. **Reading**: the print (Kiewning pp. 324-326), OCR corrected (eftetto -> effetto, cfhcacissirai -> efficacissimi,
   awiso -> avviso, rinvestitnra -> l'investitura, cheio -> che [line number 10], etc.); line numbers removed.
   The cipher runs align at 0.00-0.6 cost per letter (`reread_b01/R307_align.txt`; run 70 at 0.77 is "col padre Magno":
   the figures are 62 99 96 = Magno, which the decoder had made [629]{V.S. Ill.ma}, as in the first-wave lesson). The
   clear passages were compared with the scan at sample points; DECODE's transcription of them is not usable.
3. **Figures against print**: "li aiduchi e grandi" (cipher 20 50 33 06 47 50 between clear "li" and "e grandi" =
   "aiduchi", the Hajdú soldiery; Kiewning prints "arciduchi", which makes no sense in Transylvania: the figures are
   followed); "liberissimamente" (figures; print "liberamente"); "delle quali ho esortato" (figures 55 07
   = ho; print "hà", read here as the OCR of "hò" and given as "ho"); "Lamormain" spelled so on the sheet (print
   "Lamermain", kept).

## Group values from the alignment (proposals for extra_groups.json)

* 203 = consigliero / consiglieri ("si scaricava con li [203]", "con li [203]", "detto [203] che egli spera": print
  "consiglieri", "consiglieri", "consigliero"; 202 = consiglio on the key). Three contexts.
* 209 = cancelliere ("monsignor [209] d'Ungheria", print "monsignor cancelliere d'Ungheria").
* 949 = Transilvania ("principessa di [949]"; also "lettere di [449]", print "lettere di Transilvania", where DECODE's
  4 is probably a 9); 950 = Transilvano ("principal [950] et eretico", print "principal Transilvano").
* 965 = Ungheri ("li sopranominati [965] erano qua"), see R306.
* 424 = Fiandra ("in [424] stanno ricevendo"), see R306.
* 443 = giurisditione ("l'autorità e [443] universale", print "giurisditione"), see R305.
* "Coi[mbra]": the decoder's "coi{quando}[496]" is 772/496 split wrongly from the letters of "Coimbra"; so 496 here is
  not a group (bears on the R305 proposal 496 = legato, which rests on R305 alone).

## Holes

None: the reading is the print, the first word's "par-" is on R306.

## Result

Read from the print, checked against the figures and (at sample points) the clear text of the sheet. Clean-sentence share
0.851 (`docs/_check_reading.py --file`, 1121 words), up from 0.105.
