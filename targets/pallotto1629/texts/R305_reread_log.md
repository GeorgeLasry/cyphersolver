# Re-reading log, R305 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.094). Three pages (IMG_R305_I2542-2544), heading
"Vienna p.o di 7mbre 1629" with "In un lungo discorso" written on the page as a first-line decipherment; register p. 90 on
the third page. DECODE dates it "1679" (misread).

## What was done

1. **Which despatch**: Kiewning 1897 Nr. 170, Pallotto an Barberini, Wien 1629 September 1 (edition line 24849; "In un
   longo discorso, che hebbi avant' hieri co 'l signor principe d'Echembergh ..."). R305 begins the despatch: it does
   not continue R304.
2. **Printed stretch** (pp. 1-2 down to "si farà eseguir con la spada"): the alignment (`reread_b01/R305_align.txt`)
   puts every cipher run at 0.08-0.63 cost per letter on the print, and the clear words between runs are the print's
   words. The reading is the print, OCR corrected (tomö -> tornò, bnona -> buona, giorisditione -> giurisditione, oansa
   -> causa, Sasa -> Susa, havxebbe -> haverebbe, stüna -> stima, aiati -> aiuti, persistd -> persistè ...).
   Figures against print, no conflict found; the alignment fills several unknown groups (see below).
3. **The rest** (from "Al duca di Fridland pare ..."): Kiewning has a German regest only (Wallenstein not pressed;
   provisions, money, Spanish obstacles, "à disegno d'indebolir fra tanto con la spesa li Venetiani et altri principi
   d'Italia sino à tempo nuovo"; the Empire not to be stripped of troops "besonders wegen der Anstrengungen der
   Franzosen"; Aldringen advanced to the passes, Musterplätze and Etappen for 22000; Eggenberg on Savelli's
   representations about the promotion; "Wegen des Legaten ... der Papst wolle sich informieren"; Dietrichstein deputed
   at Matthias's wedding as King of Hungary, first place in the carriage, "che era fatto in modo, che non hà primo ne
   secondo"; Lorraine, "e che Francia apra seco molto ben gli occhi"). Read here: the clear lines on crops at full
   resolution (DECODE's clear transcription of this part is mostly guesses: "Frillano", "miniera", "giallì", "ploni"),
   the cipher runs group by group with `reread_b01_show.py` and on the scan (`R305_corrections.tsv`).
4. Points settled: "ritrovandosi le cose perturbate" (decode "pertu[262][400]te"; 36 24 for 26 24 on the scan);
   "de' Franzesi" (423 after clear "de"); "esagerandole acremente il medesimo signor principe" (Eggenberg); "uffitio
   passato da cotesto ambasciatore cesareo [in] materia della promotione, e che gli era stato risposto" (the decode's
   {Duca di Mantova} and [903] are segmentation/misreading artefacts, fixed on the scan); "che N. S.re s'informaria del
   solito" (scan 577, not 277); "nozze di Mathias, essendo re d'Ungheria" (643 = Re d'Ungheria on the 6956 key, which
   fits the 1611 wedding of Matthias, then King of Hungary, where Cardinal Dietrichstein was papal legate); "con Lorena"
   (75 36 90 29 00) and "che Francia apra seco" (422).

## Holes and why

* "aspett[ino]", "ne' Spag[?noli]": clear words cut by the right edge of the scan; "[?doppo]" is under a blot.
* "delle [?quali]": the figures are 67 67 (da da), no word; "quali" by sense.
* "ventiduemila [?huomini]": the last clear word is cut at the edge ("h..."); the regest's "22000 Mann" supports it.
* "risposto con […]": the figures give p-r-o-le-se-n (22 36 70 74 64 39) before clear "senza"; no word found
  (regest: answered "im allgemeinen", in general terms). Left open.
* "darsi [907] per obligato": 9 0 7 0 after "darsi" as on the scan; no reading.
* "[?circa] li [?affari] della pace": figures 32 50 3 0 0 / 66 50 / 00 743: "ci..." and "a far" carried, the rest of
  the two words is not.
* "[?specificato]": clear word split over the line, partly blotted ("Speci-/[fic]ato").
* "Del [?grado] di [?legato]": the clear word after "Del" is an abbreviation I cannot resolve ("gaw." on the scan);
  496 is an unknown group. 496 sits just before 497 (lettera) in the L range of the nomenclator, and both its
  contexts here ("Del ... di [496]", "si deputava ... per [496] il signor [277]") take "legato"; the regest speaks of
  "des Legaten". Marked [?legato]: two contexts in one record only.
* "[?informaria]": the end of the word is blurred at the page break (44 07 36 6.. / 36 50 20).
* "[?potrà]": clear abbreviation "pot.a".
* "il signor [277]" and "dal signor [207]": the regest names Dietrichstein in the second place; 277 and 207 are both
  unknown groups (207 occurs in other records in contexts that do not take a name, so it may be a misreading here).
  Not filled.
* "Mat[?hias]": t-h-i-a-s carried (25 55 50 00 23); kept marked because the decoder had made it a group.

## Group values from the alignment with the print (proposals for extra_groups.json)

* 444 = Grigioni ("li passi de [444]", print "li passi de Grigioni"); fits the G range. R305 only here.
* 443 = giurisditione ("alla dignità e [443] di S. M.tà Ces.a", print "giurisditione"); R307 "l'autorità e [443]
  universal" fits too.
* 206 = buona ("la [206]on intentione" - decoder letters overlap; print "buona"); B range.
* 720 = causa ("la [720]..a et interessi", print "la causa"); uncertain (7xx are common words).
* 496 = legato (see above), proposed with "?".
* 643 = Re d'Ungheria (already on the 6956 key; confirmed by sense here).

## Result

Read: paragraphs 1-3 from the print, 4-6 from the sheet; the sentences hold, with the holes listed (most of them single
words at the cut right edge or one unknown group). Clean-sentence share 0.722 (`docs/_check_reading.py --file`, 1082
words), up from 0.094.
