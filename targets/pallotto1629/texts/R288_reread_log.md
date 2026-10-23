# Re-reading log, R288 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.136). Available: DECODE's transcription
(`decode/R288.txt`, three pages, images 2495-2497, with garbled clear-text annotations), the batch decode
`reread_b01/R288_dec.txt` and its alignment `reread_b01/R288_align.txt`.

## What was done

1. **Despatch identified**: Kiewning 1897, Nr. 154 (OCR "164"), Pallotto to Barberini, Vienna 4 August 1629, dechiffr.
   22 August, Nunz. di Germania 119 fol. 19-20 (edition lines ~23275-23321). The sheet's head reads "Di Vienna 4 di
   Agosto 1629 ... B 24"; it is the second (B) despatch of 4 August, after Nr. 153 (R286 + R287, "A").
2. **Print**: Kiewning prints only two stretches in Italian; the decode aligns there at 0.19-0.46 (runs 5.5-5.8) and
   0.46-0.73 (runs 5.16-5.17, 7.0). The rest is a German regest; the alignment's other runs (cost > 1) land on unrelated
   edition text and were disregarded.
3. **Figures**: the remaining text was read from the decode, re-segmented by hand with `reread_b01_show.py`, and each
   break checked on the scans (crops of every row of pp. 1-3 at full resolution). Main results (all in
   `R288_corrections.tsv`): "effettuatione" (decoder's 902/620 were a mis-segmentation), "occasione" (567),
   "dargliene segni", "P. F. Valeriano" (the initials P. F. in cipher), "pregarla", "pregavo" (both had become an
   unknown group 223), "io, superior di lui" (decoder: "al e si et {Germania}"), "fuor de' suoi stati",
   "beni ecclesiastici di Boemia" (407), "governarmi", "uscirà", "si determinasse".
4. **Clear text** read on the scans: the heading over the first cipher line ("Nel particolar delli nuovi Vesc.di da
   erigersi in Boemia", which the cipher repeats) and the clear sentence on p. 3 ("Ho voluto tutto questo significar a
   V. S. Ill.ma acciò si compiaccia ordinarmi come doverò"); DECODE's clear-text transcriptions of both were unusable.
5. The regest was used only to check the sense: "nicht ohne Erfolg" (non senza speranza), "Ankunft der Breven und
   Schreiben", "P. Fra Valeriano unzufrieden", "Er hat die Schriften nicht gesehen, obwol der Pater sie ihm zeigen
   wollte ... und bat darum" (= "ma pregarla ... a farle veder"), "als Vorgesetzter des Paters" (= "superior di lui"),
   "den Pater ausser Landes zu verweisen" (= "volerlo fuor de' suoi stati"), "bis die Angelegenheit der geistlichen
   Güter in Böhmen erledigt wäre", "das zweite Mal", "Er wünscht darüber Anweisungen" (= the clear sentence).

## Where the figures differ from Kiewning

* "e che però pensava" — figures 763 = però; Kiewning "perciò". Reading follows the figures.
* "tanto impertinenti come quelle del Francese" — the figures have 747 (= havere on the 6956 key) where Kiewning
  prints "come" (737); kept as printed, since "havere" does not construe. A 4/3 confusion (the A-shaped 4) is likely.
* "che è cervello", "le haveva promesso", "haveva fatto il contrario" (figures 544 = negotio, a misreading of 744 =
  fatto), "con mille inventioni" (figures garbled, "con dalle"): print kept.

## Holes and why

* "[?gli] porta", "[?della] S. M.tà": one uncertain digit each (5?7 for 37; 66 for 56).
* "[?fatto dar]": 744 67 36 + a stray 9.
* "lo [?tenessi] in me stesso": the verb ending is a lone 6 after "tene".
* "non [?perdessero] per far […] dal padre": the figures read plainly 57 33 90 43 36 07 ("per-d-e-s-r-o") and, after
  743 = far, 23 60 07 22 07 96 29 90 ("s-u-o-p-o-no-n-e"); neither makes a word I can stand behind. Not in the print.
* "[?quando] egli [?passasse]": 77[1]2 and 22 02 8 30 26 4, both partly blotted.
* "[?finché]": figures 59 60 47.
* "per quale [332] [993] è molto [697] e necessario": three groups not in the key and not in the print (the passage is
  underlined on the sheet). 697 also stands where "in" is wanted in "parte [6]97 questo negotio", so it may be 6 + 97
  there; here "molto [697]" needs an adjective.
* "haveria [249] a deliberar", "[?havesse] giudicato": 249 is not in the key; "havesse" from 55 20 6 90 23.
* "Vede V. S. Ill.ma […] già la seconda volta": the figures 74 03 99 20 ("le o ga") do not make the expected "che è
  già" (47 90 would); a digit reversal is possible but not visible on the scan.

## Group values (proposals, not entered in extra_groups.json)

* 956 = vescovati (the clear heading "nuovi Vesc.di da erigersi"; 9xx range S-V).
* 260 = Boemia (heading "in Boemia"; four contexts in this record, all "di/in Boemia"; 2xx range A-C).
* 762: not in this record.
* 629 + 996 after 22 ("p") = padre Magno again (Valeriano Magni, the Capuchin; "il padre Magno mi haveva detto di
  farmele veder"), as in R286/R287. 996 = V.S. Ill.ma holds in its other contexts ("vedo quanto 996 mi comanda",
  "vede 996"), so the run "22 [1 1] 629 996" as a whole stands for "padre Magno" in six places (R286 x3, R287 x2, R288
  x1) and its segmentation is not settled; the decoder's "{V.S. Ill.ma}" inside it should not be read.
* 223 is not a group in "ma [223]esto" or "ma [223]digovo": both are 22 36 = "pr" (pregarla, pregavo). In "in modo
  [223]a{Savoia}" Kiewning reads "in modo alcuno"; that stretch was taken from the print.

## Result

Read: the sentences hold, with the holes listed (one sentence, "non [?perdessero] per far […] dal padre", stays
unclear). Clean-sentence share 0.136 -> 0.727 (`docs/_check_reading.py --file`, 66 sentences, 48 clean).
