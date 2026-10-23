# Re-reading log, R287 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.111). Available: DECODE's digit transcription
(`decode/R287.txt`, four pages, images 2491-2494), the batch decode `reread_b01/R287_dec.txt` and its alignment with
Kiewning `reread_b01/R287_align.txt`.

## What was done

1. **Existing text.** The sheet is the second half of the despatch of 4 August 1629 whose first half is R286:
   Kiewning 1897, Nr. 153, pp. 280-282 (edition lines ~23019-23125), from the Roman decipherment (Nunz. di Germania
   119). R287 begins inside the word "l'acquista|sse" of the sentence that starts on R286. Every chunk aligns at
   0.13-0.61 cost per letter (0.70 for the chunk that straddles the OCR's page break, lines 23102ff.): the print
   carries the whole sheet verbatim, and the reading is the print with its OCR corrected (giastitia, daca, Sasa,
   mntatione, govemo, qnanto, rA/rd/rt = re, k = a, etc.).
2. **The print and the figures compared** chunk by chunk; the disagreements checked with `reread_b01_show.py` and, where
   the decode broke, on the DECODE scans (`R287_corrections.tsv`).
3. **Docket** (p. 4, right margin, vertical, clear): "Vienna / li 4 Agosto 16[29] / Con […] del Nun[…] / Decif.ta li 22
   d[etto]". The third line is not legible to me beyond "Con" and "del Nun". The date of deciphering agrees with
   Kiewning's heading ("dechiffr. 22. August"). The "6." at the head of p. 3 is a page number.

## Where the figures differ from Kiewning (reading follows the figures)

| figures (this sheet) | Kiewning Nr. 153 | evidence |
|---|---|---|
| preeminenze e prerogative della persona e famiglia del duca | preeminenza e prerogative della persona del duca e sua famiglia | 44 00 63 37 00 8 56 354 = "famiglia del duca" |
| in altro modo dar gelosia al re | in altro modo per gelosia al re | 67 36 = "dar", checked on the scan (p. 2 l. 4) |
| Moncalvo e li altri luoghi accordati al duca | luoghi occupati | 20 32 07 36 67 35 50 = a-c-o-r-da-t-i (p. 2 l. 8) |
| questa mattina il padre Magno ha mandato | questa mattina ha mandato | "il p[adre Magno]" (22 + the 629/996 run that stands for "padre Magno" in all R286-R288 contexts) |
| il detto padre per nascita suddito de' Spagnoli, per il domicilio di più di trent'anni in queste parti | il detto padre suddito de Spagnuoli et il domicilio per più di trent'anni in questa corte | 57 29 00 23 42 50 35 00 = "per nascita"; 775 22 02 36 35 50 = "questo/e parti" |
| provisioni di guerra | provisioni da guerra | 69 437 (p. 3 l. 18) |
| ma io non deporò con tutto ciò promover e facilitar quanto potrò detta trattatione | mà io non mancherò con tutto ciò per quanto potrò di promuover ò facilitar detta trattatione | 33 09 22 07 36 07 = d-e-p-o-r-o, clear on the scan |

Points where the print was kept although the decode first disagreed (the figures, once checked, support the print):
"al re, mentre" (decode "al mi i mentre"), "per parte dell'imperatore" (decode "del r e"), "era restato con Echembergh"
(decode "del e stato [562] ne"), "del principe d'Echembergh" (decode "del ne ne"), "promover" (decode "promo[690]r"),
"dal detto padre" (decode "b deto": DECODE "3? 4" for 54 = dal), "Questo e quello" (decode "{questo} e mi": 77 4(0)
taken as 774 = quello), "per haver penetrato" (747 = havere), "Sabran spedisce" (23 [0] 02 24 36 ... = s-a-b-r..., the
decoder had found {Germania}), "metter" (77 9 25 9 36 with 9 for 90 = e), "il loro capo, il duca di Michelburgh"
(75 36 70 = lo-r-o, read by the decoder as {molto}{Sua Maestà}; 7[6] 354 = il duca), "sinché" (figures 04 96 47 = "u no
che", probably 65 = si misread), "ricuperar molti feudi occupati (con uno de' quali" ("con" not seen in the figures).

## Holes and why

* "[?Cardinal di Richelieu]": in its place the figures have one group 290, which is not a reliable code (its other
  contexts in the batch read as letters 29 0 / 2 90); the name rests on Kiewning. R289 has the same group where
  Kiewning prints "richiamatovi il Cardinal di Richelieu", so 290 = Cardinal di Richelieu is likely; kept marked.
* "[?deporrò]": the figures read "deporò" plainly; the verb sits oddly with "promover" (Kiewning's text has "mancherò ...
  di promuover"), so the word is marked.

## Group values (proposals, not entered in extra_groups.json)

* 409 = feudi — "ricuperar molti [409] occupati", Kiewning "molti feudi occupati"; alphabetically in the F range of
  the 4xx block.
* 562 = con — "non cessano [562] ogni" (Kiewning "con ogni") and "era restato [562] [5]95" (Kiewning "restato con
  Echembergh").
* 437 = guerra (6956 key) confirmed on the scan; DECODE's 937 in "provisioni di 937" is a misreading.
* 322 and 307 = Christianissimo (both against Kiewning "Christ."); one of the two may be a misreading.
* 444 = da Grigioni (one alignment); 236 = (sc)ritto; 526 = consid(erationi); 524 = confi(dentissima); 596 = principe
  Savelli; 939 = trattatione; 237 = accordo; 546 = negotiato (two alignments); 550 = moti(vo); 453 = che non (one
  alignment each, from `R287_align.txt`).
* 762 lies between 759 nondimeno and 763 però and reads "onde" before "hoggi Sabran spedisce" (Kiewning "Onde"); in
  "per il passato [762] duca di Mantova" Kiewning has "al", so that instance may be a slip or a misreading.

## Result

Read: all sentences hold; clean-sentence share 0.111 -> 0.829 (`docs/_check_reading.py --file`, 82 sentences, 68
clean). The two marked holes are a name carried only by the print and one doubtful verb.
