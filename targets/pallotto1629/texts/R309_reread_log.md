# Re-reading log, R309 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.071). Two pages (IMG_R309_I2553, I2554; register
number 104), headed "Di Vienna 15 di 7mbre 1629". Most of the sheet is clear text with eleven cipher runs; an interlinear
decipherment covers only the first line ("Con l'ord.rio passato intendo che fu scritto da S. M.tà a N. S.re").

## What was done

1. **Despatch**: Kiewning 1897 Nr. 178 (Wien 1629 September 16, dechiffr. 3 October, Nunz. di Germania 119 fol. 89-91;
   edition lines 25927-25992) on the Verden church for Adam Schwarzenberg, with the Emperor's two letters as enclosures.
   Kiewning dates it 16 Sept; the sheet says 15 Sept. Not a continuation of R308: it begins with the heading.
2. **Clear text** read on crops of the scans (1465 x 2088 and 1372 x 2088): DECODE's clear-text transcription is
   garbled throughout ("havir? acconnato", "pregiufitiali", "Ichig.na Car.la"); the reading replaces it.
3. **Cipher runs** from the decode and the codes (`reread_b01_show`/dumpruns): "Adamo de Sfarzembergh", "Tilli per un
   suo parente", "parente del Tilli", "chiesa per essere [425]", "l'uno la nominatione di S. M.tà e l'altro del possesso
   ... come loro chiamano", "conte Adamo", "la nominatione", "a nominatione di S. M.tà", the long run "si farà con le
   dette conditioni ... obligo in scritto" (Kiewning prints it, 0.24-0.32 cost/letter), "l'Imperatore non gli
   s'i[m]pedisca", "medesimo", "Verden e ritrovandovisi dentro attualmente il suo presidio".
4. **Print vs scan**: Kiewning prints the paragraph from "perché si esprimerà" in Italian; the scan has "probabilmente"
   where the print has "publicamente" (the Roman decipherer or Kiewning misread the clear word), followed here. "sì come"
   (print "sicome") and "si provederà" agree.
5. **Verden** is spelled out twice as "Vuerden"/"Vuerte" (06 04 ...), i.e. the German W; the first is partly under a
   blot (corrections tsv).

## Holes and why

* "[596: principe Savelli]" (confirmed by R311, print "al signor principe Savelli" against figures "al Signor 596"): after "et al Signor"; the clear text later says "quella diretta al principe" and the
  regest names Savelli (the imperial ambassador in Rome, "principe Savelli"); 596 follows 592 principe and 595 principe
  d'Echembergh in the nomenclator, which fits "principe Savelli". Other contexts: R287 "intentione al 596", R297 "dir al
  596".
* "in […] del conte": 55 23 07 29 00 does not spell "favore"; unresolved (552 may be a group; see tsv).
* "[207: consigliero secreto]": "Ad uno 207" where the regest has "einem geheimen Rat"; established from R311, where
  "con alcuni de 207" stands against Kiewning's printed "con alcuni de consiglieri secreti" (R310 "co 207 pia" is a
  misparse of "copia").
* "[?già]": clear word after "che", partly legible.
* "[?Il Verdembergh]": the clear word before "mostrò molto senso" ends in "-bg"; the shapes allow "Il Verdbg"
  (Werdenberg, Bohemian chancellor and privy councillor) but this is not certain.
* "[425: ?Fiammingo]": "per essere 425"; the regest: "da er Flamänder sei". 425 sits between 423 Franzesi and 427
  fortificatione, in the F range; the word rests on the regest, so it stays bracketed.
* "[?fuori] di […] di esse": the clear words after "mostrassero" are partly struck/blotted.
* "per il [?senso] accennato": clear word uncertain.
* "[?il Tilli]": run 69 28 69 1 25 / 66 65 0 at the page edge; ends in "lli"; subject from the regest.
* "il medesimo [46]": two trailing figures after "medesimo" not read.
* "[?senz'ordine]": the last clear words of the line are cut at the page edge.

## Group values

* 460 = Imperatore (6956 key value, confirmed: "l'Imperatore non gli s'impedisca", regest "der Kaiser es nicht hinderte").
* 503, 507, 727 in the decode are not groups here: "ingerirsi" (50 36), "s'i-pedisca" (50 / 22), "alle" (print).
* 207 = consigliero/-i secreto/-i (R311 print alignment).
* Proposed: 596 = principe Savelli (R311: "comunicato al Signor 596" against the print's "principe Savelli" confirms it); 425 = Fiammingo (regest only).

## Result

Read: all sentences hold; the holes are the names above. Clean-sentence share 0.739 (`docs/_check_reading.py --file`, after the 207/596 values were settled;
69 sentences, 50 clean, hole rate 0.119, most of it the bracketed proposals).
