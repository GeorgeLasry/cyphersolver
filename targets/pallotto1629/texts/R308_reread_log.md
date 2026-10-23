# Re-reading log, R308 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.1). One page (IMG_R308_I2552), heading "Vienna 15.
di [7]mbre 1629", register "B.", page 102; mostly clear text with cipher runs; an interlinear gloss over the first run.
DECODE dates the record to November 1629.

## What was done

1. **Which despatch**: the content (visitor for the diocese of Aquileia; the patriarch ill or dead; the negotiator who
   died at Trieste; a foreign visitor who would not know the language) is Kiewning 1897 Nr. 177, Pallotto an Barberini,
   Wien 1629 September 15, dechiffr. 3 Oktober (edition line ~25913), a German regest only. The "B." of the sheet
   matches: R306-R307 are "A 93" of the same day (Nr. 176). The date is 15 September 1629, not November.
2. **Clear text** read on full-resolution crops: DECODE's clear transcription is unusable in most lines ("Non lo ho?
   vorranno?" = "Non so se vorranno", "metende? chi ha" = "pretende, ch'ha", "cvolontà? di N.d." = "e volontà di N. S.").
3. **Cipher runs** read group by group (`reread_b01_show.py R308`) and on the scan (`R308_corrections.tsv`). The first
   run carries a contemporary interlinear gloss "restati quà contenti della risolutione" (the coordinator's brief has
   "più"; the gloss and the figures, 27 00, have "quà"); the cipher itself reads "restati contenti qua con la [662]",
   so 662 = risolutione.
4. Settled on the scan: "han però riservato di darmene risposta" (763 = però, 67 = da; the decoder had "ileriseruato di
   marmene"); "che non havendo la lingua" (249 is struck through on the page); "dar risposta" (76 for 36, a slip).

## Holes and why

* "d'[?Aquileia]": group 254, not on the key; the regest names the diocese (Aquileja). Proposed 254 = Aquileia (?).
* "il [?patriarca]": group 602 (P range); the regest "dass der Patriarch gestorben wäre". Proposed 602 = patriarca (?).
* "detta [?malattia]": figures 26 73 25 50 20 (z-la-t-i-a); 62 (ma) for 26 would give "malatia"; regest "aus Anlass der
  Krankheit".
* "habbiano [?discorso]": figures 64 23 32 0? 36 23 0? ("se-s-c-?-r-s-?"); "discorso" needs 69 for 64.
* "al [?capitolo]": group 327, not on the key (C-D range); regest "an das Capitel". Proposed 327 = capitolo (?).
* "per altro [?sufficiente]": figures a-si-c-e-n-t-e.
* "il quale però […] non pretende": the cipher 67 1 53 ("da non") between "però" and clear "pretende" does not parse.
* "all'[?alienatione] del lo quale pare ...": the clear word is abbreviated with a superscript I cannot resolve with
  certainty ("all'alienat."); the sentence that follows is as the figures and clear words give it, and its sense is
  obscure (the regest only says "Das wird Schwierigkeiten wegen der Kosten geben").
* "solite e [?durezze]": clear word with a flourish ("durelli"?).

## Group values

* 662 = risolutione (on-page gloss "della risolutione" over "con la [662]"; R-range).
* 763 = però (key value; decoder segmentation fixed here).
* 393 = elettione (extra_groups), 937 = trattato, 202 = consiglio, 670 = Sua Maestà, 996 = V. S. Ill.ma: all fit.
* Proposed with "?": 254 = Aquileia, 602 = patriarca, 327 = capitolo (each one context, from the regest).

## Result

Read in part: the first two paragraphs read as sentences (holes are single words named by the regest); the last
paragraph reads to "nel paese" and from "quando si tratta del gusto di S. M.tà" to the end; the clause between is carried
by the figures and the clear words but its sense stays obscure. Clean-sentence share 0.75 (`docs/_check_reading.py
--file`, 497 words), up from 0.1. The coordinator should correct the record's date to 15 September 1629 (Kiewning
Nr. 177, despatch "B").
