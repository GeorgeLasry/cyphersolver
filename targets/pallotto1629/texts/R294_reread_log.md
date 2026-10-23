# Re-reading log, R294 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read", clean share of the old decrypt 0.08. Two register pages: p. 51 (full) and four lines
on the next page.

## What was done

1. **Which despatch?** The end of Kiewning Nr. 160 (Vienna 18 Aug. 1629, "A. 43"), begun on R292 and continued on R293:
   the first words "[673]r da ma che desidera ancora di saper come pensa di trattar li cardinali" continue R293's
   "rispondesse che desidera cons[olar]". Kiewning's text for it: edition lines 24155-24168.
2. **Print stretch** (`reread_b01/R294_align.txt` run 1.0 at 0.28, 4.0 at 0.67): "S. M.tà, ma che desidera anche di
   sapere ... anco lo soffriranno", given in the print's wording (OCR: "sndditi", "ehe"). The figures have "ancora di
   saper" for the print's "anche di sapere"; the print is kept.
3. **The rest from the figures** with the clear words read on the scan (corrections in `R294_corrections.tsv`). Kiewning's
   regest checks the sense of each sentence: the advice to the cardinal to avoid singing Mass, the two excuses, the
   Camaldolese foundation stone where the nuncio stood in for him, and the Augustinian reform.
4. Values used: 255 = (ci)mento as in R292 ("aggiusta[255]"); 393 = elettione (R292 alignment); 654 = religione (R292:
   "della [654] [499]" = print "della religion Luterana"; here "questa [654] si veda tutta riformata", i.e. the religious
   order); 677 = S. S. Ill.ma ("supplito io in luogo di [677]", the nuncio standing in for the cardinal).

## Holes and why

* "Al Signor […] ho persuaso": the figures after "Signor" are "ma lo", not a name; by the regest the cardinal is Harrach
  ("Rarrach").
* [557] "et [557] supplito io": probably "ho"; [557] also in R291 ("volontà che [557]eno") unresolved.
* "li padri di S. Agostino […]": the figures "de dada" do not resolve (a house or a branch of the order).
* [553] "con [553] premura": an adverb or adjective (molta?); [327] "congregar [327]": by the sense "il capitolo".
* "p[?rovista] di [?huo]mini [?dotti]": groups 509 (decoder: ministri), 550, 620 and letters "d in ti".
* "re[…]si che si potranno […]": the last line on the second page is struck or blotted; the despatch breaks off.

## Group values proposed

* 654 = religione (religious order / religion): R292 against the print, R294 by sense.
* 677 = S. S. Ill.ma (see R293 log).
* 393 = elettione (R292 alignment; R294 "per l'[393] di provinciale").

## Result

Read in part: every sentence builds; clean-sentence share 0.711 (`docs/_check_reading.py --file`, was 0.08); the
remaining holes are unresolved groups and the struck last line.
