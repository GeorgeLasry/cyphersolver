# Re-reading log, R306 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.121). Four pages (IMG_R306_I2545-2548), heading
"Vienna 15. 7mbre 1629", register "A 93", page number "94" on the second page; almost all cipher.

## What was done

1. **Which despatch**: Kiewning 1897 Nr. 176, Pallotto an Barberini, Wien 1629 September 15, dechiffr. 3 Oktober
   (heading at edition line 25553; text from line 25576 "Passai efficaci uffitii ..."). Register letter A = the first
   despatch of the day. The alignment (`reread_b01/R306_align.txt`) puts every cipher run of the sheet on consecutive
   stretches of the print, from "Passai efficaci uffitii" (p. 321) to "Del padre Lamermain so, che la mattina della
   natività della Madonna parl-" (p. 324), at 0.12-0.75 cost per letter.
2. **Continuation**: the sheet ends in "... della madonna" + 22 02 3(6) = "par" at the foot of p. 4 (checked on the
   scan); R307 (register p. 97, no heading) begins with 66 50 24 ... = "l-iberissimamente" and continues the print
   ("parlò liberamente et efficacissimamente con S. M.tà ..."). R306 + R307 are one despatch, Nr. 176. The register
   numbers (A 93, p. 94; R307 p. 97) fit four pages + R307's three.
3. **Reading**: the print, OCR corrected (dnea -> duca, qnella -> quella, trk -> tra, 2o6uastalla -> Guastalla,
   destr&mente -> destramente, cbe/ehe -> che, Lamermain kept as printed; line numbers "io", "16", "26" removed from the
   text: "Lamermain s6, che io / la mattina" has the line number 10, not "io").
4. **Figures against print** (print kept, differences noted): the sheet spells "Lamormain" (print "Lamermain"); "non so
   ancora quello che habbia fatto" (733 = ancora; print "anche"); "vedremo gli incendii" (decode, print "l'incendio");
   "liberissimamente" (R307; print "liberamente"); "speraria ancora lui ariuar" (733; print "anche lui di arrivar").
   "Danneggiato il duca di Nivers": the figures are 369 8 730 = {Duca di Nivers} acciò (the decoder had split 36 90 =
   "re"); confirms 369 of the 6956 key.

## Group values from the alignment (proposals for extra_groups.json)

* 997 = lettera ("la minuta di [997]", print "minuta di lettera"); 497 is lettera too.
* 963 = Venetia ("residente di [963]", "e finalmente [963] che non sia per poter resistere": print "Venetia" both times).
* 652 = residente ("questo [652] di [963]", print "questo residente di Venetia"); one context.
* 965 = Ungheria / Ungheri ("il palatino di [965]", print "palatino d'Ungheria"; R307 "[965] erano qua", print
  "Ungheri erano quà").
* 424 = Fiandra ("le cose di [424] nel pessimo stato", print "Fiandra"; R307 "in [424] stanno ricevendo si gran rovine",
  print "in Fiandra"). (One more [424] in run 5.12, where the print has "delle cose d'Italia, come": a mis-segmentation.)
* 444 = Grisoni / Grigioni ("restasse S. M.tà in [444]", print "Grisoni"; also R305 "li passi de [444]").
* 429 = fortezze; 433 = Fiorenza; 537 = regni; 240 = Austriaco; 306 = confessore (single contexts, print words,
  groups in their alphabetical ranges).
* "Savoia [372] e [365]" = print "Savoia, Lorena e Guastalla": 372 and 365 are outside the L and G ranges, so this may
  be a mis-segmentation rather than two name groups; not proposed without a scan check.

## Holes

None in the text: the reading is the print. Not checked on the scan line by line beyond the end of p. 4 and the
continuation, since the figures and the print agree throughout.

## Result

Read from the print, checked against the figures. Clean-sentence share 0.938 (`docs/_check_reading.py --file`, 1564
words), up from 0.121. The coordinator should record R306 + R307 as one despatch (Kiewning Nr. 176, "A 93").
