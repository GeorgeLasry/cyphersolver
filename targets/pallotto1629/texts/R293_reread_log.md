# Re-reading log, R293 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read", clean share of the old decrypt 0.061. Four register pages (pp. 47, 48 and two
unnumbered), cipher with clear words.

## What was done

1. **Which despatch?** Not a separate despatch: R293 continues R292 (Kiewning Nr. 160, Vienna 18 Aug. 1629, "A. 43",
   Nunz. di Germania 119 fol. 29-37). Its first cipher words finish R292's last sentence ("conformarsi per la
   [di]spositione della [...]"), and its text runs on Kiewning's edition lines 24006-24155; R294 continues it.
2. **Print stretches** (`reread_b01/R293_align.txt`, runs 9-45 and 65.2-67 at 0.07-0.75 per letter): "Quanto alle
   provisioni ... alla sede apostolica" and Kiesel's speech. Given in the print's wording, OCR corrected (conrenienza,
   qaelli, Hl, tanio, condennar, snppliche, procnrarei, eompntati = compattati, coüatione ...). Figures that differ from the
   print: "[527]" where the print has "N. S.re" ("che [527] non sia ben affetto") and "Papa" ("quelle del [527]"), so
   527 = Papa; the print has "si potesse avanti il segnar le suppliche", where the figures have "ti il [649]ster", a word
   is probably lost in the print or the OCR: left as "si potesse […] il segnar".
3. **Regest stretches** read from the figures and the scan:
   * the opening: clear "et in questo parimente mi ha promesso la sua assistenza. Non hebbi per bene" + cipher "parlarne
     con S. M.tà prima di haver sentito il principe" + clear "Onde intanto" + cipher "S. M.tà è tornata fuori alle caccie,
     dove" + clear "si tratterrà qualche settimana. Nella seguente io uscirò a servire S. M.tà" + cipher "e gli parlerò
     [609] questo negotio" (regest: "Der Kaiser ist zur Jagd gereist und wird einige Wochen ausbleiben");
   * the Dohna paragraph (regest: Dohna wants two places in Silesia held in pledge by Breslau, with the title of prince;
     Eggenberg's answer): read from the figures with the clear words "Prima di parlar[ne]", "e dicendo che lo
     domanda[rò]", "per non dar occasione", "che da molto tempo in qua", "caldissimamente", "Sì che con questa apertura";
     "la città di Uratislavia" (= Breslau) is spelled out in the figures;
   * the opening of the baldachin paragraph: clear "Circa il particolare del baldachino aspettarò l'ordini che a V. S.
     Ill.ma parerà di darmi; di qua non so che aggiungere a [quanto] scrissi con altre, se non che" + cipher.

## Holes and why

* [609] "gli parlerò [609] questo negotio": probably "sopra"; unresolved.
* Dohna paragraph: [269] (title of Dohna; by the context "burgravio" — Karl Hannibal von Dohna — not on the key), [264],
  [702], [337], [690], [330], and several garbled letter stretches ("sti[629]na[322]no di e{Conte} e mal[550]uarne",
  "f{Duca di Mantova}dic[290]o"); the sense is fixed by the regest, many words are not.
* "il P. La[…]": by the regest Lamormain; only "la" is carried.
* [540] "mi disse [540]": by the regest Kiesel (Cardinal Klesl); 540 in the M-P range does not fit the name; left.
* [642] [992] "come [642] [992]"; "[?gli] […]steria gran gloria se […] la sodisfattione".
* 677: the batch value is "Sua Santità", but on this record and R294 it stands for "S. S. Ill.ma" (Sua Signoria
  Illustrissima): "Che [677] non ci poteva rimediare" = print "S. S. Ill.ma" (Klesl), and R294 "supplito io in luogo di
  [677]" (the nuncio standing in for Cardinal Harrach). Read so here: "con lu[i]. S. S. Ill.ma soggiunse", and in the
  Dohna paragraph "l'intercessione di S. S. Ill.ma" / "serviria S. S. Ill.ma" (Barberini, who had ordered the
  recommendation).

## Group values proposed

* 677 = S. S. Ill.ma, not Sua Santità (see above; R293 three contexts, R294 one).
* 527 = Papa (two contexts against the print "N. S.re"/"Papa").
* 670 = Sua Maestà confirmed at "Onde intanto [670] è tornata fuori".

## Result

Read in part: the print stretches (about two thirds of the record) and the opening read in full; the Dohna paragraph
holds as sentences with holes. Clean-sentence share 0.78 (`docs/_check_reading.py --file`, was 0.061).
