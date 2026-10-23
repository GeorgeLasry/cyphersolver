# Re-reading log, R300 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.167). Two pages: p. 1 (IMG_R300_I2531, 29 lines
of cipher, heading "Di Vienna 25 Agosto 1629 / All'Ill.mo Sig. Card. Padrone / B / 74", clear words "Dopo scritta" over
the first groups) and p. 2 (IMG_R300_I2532, 7 lines of cipher, the rest of the page blank with show-through). DECODE's
transcription covers p. 1 only; there was no `_align.txt`.

## What was done

1. **Despatch**: Kiewning Nr. 165 (Wien 1629 August 25, dechiffr. 13. September; Nunz. di Germania 119 fol. 57-58;
   edition lines 24538-24578), the second cipher of 25 August ("Vgl. die vorige Chiffre" = Nr. 164, register "A",
   R297+R299); register letter B matches. Matched by content: Bruneau sent to the Elector of Mainz, the League troops
   for Herzogenbusch, Aytona's equerry, Wallenstein, Guastalla, "ad sommam di centomila scudi", Don Cesare. German
   regest only, so the reading is from the figures; R300 does not continue R299 (its first words are a new opening,
   "Dopo scritta la [?cifra]").
2. **Page 1**: read through the decode with the codes (a dump script in the scratchpad, `reread_b01_show.py`,
   `reread_b01_ctx.py`); line positions found by a row-ink profile of the scan; breaks checked on crops:
   struck groups after "saputo" and "con il" and "il [quale]" (the writer's deletions), the overwritten group in
   "l'[?investitura]", the stray 5 at the start of l. 13, the end of p. 1 ("Fiandra camine-").
   Mis-segmentations of spelled-out words corrected: "nuouo" (not {Sua Maestà}), "Bolduch" (not bo{Roma}emi),
   "cavalerizo" (not caualer{Marchese}[607]), "d'Aitona" (not d{munitione}itona), "prometto" (not pro{tuttavia}to),
   "persona" (written per-to-o-na twice: 93 for 23 or a habit of the writer).
3. **Page 2**: DECODE has no transcription. I transcribed the 7 lines from the scan at 2.2-3x crops
   (`R300_p2_digits.txt`) and decoded them with the decoder's Viterbi (`decode_run`) and the same key. The sense comes
   through ("vantaggio", "ma senza pretender che ... per ciò addormentati quelli che devono star più vigilanti",
   "promuover", "dentro i termini prescritti", "la quale supplico a significarmi in caso che il trattato andasse ...",
   "di regolarmi circa il punto della promotione di Don Cesare", "motivato"), but many places hinge on 3/5/9, 2/7 and
   6/8 that I could not tell apart at the scan's resolution (e.g. "circa" came out as st-i-r-c-a, "della" as r-la,
   "Cesare" as p-e-s-a-r-e). Those words are read where the sense and Kiewning's regest fix them; the rest are holes.

## Holes and why

* "la [?cifra]": 326 + a; "cifra" fits the C range, Kiewning's note to Nr. 165 refers to "die vorige Chiffre", and R303
  "con la mia [326]" fits; not confirmed by a print alignment.
* "[che]": supplied; the figures there are struck.
* "il [?detto]": a struck group; only "-to" remains.
* "[?Baviera]" (259): B range just before 260 Boemia; Kiewning's regest "besonders von Baiern". 366 is also given as
  Baviera in extra_groups.json; 259 may be a second group or a stem.
* "della [?Lega]" (493): L range before 497 lettera; regest "Ligatruppen"; the figures before it are 56 75 "dello".
* "[?Se] che": the figures are 64 (se) 47 (che); probably a slip for "Quel che".
* "[?la]sciato": the figures give s-s-c-i-a-to.
* "l'[?investitura]": overwritten group (DECODE 966); regest "Investitur an Nevers"; 466 = investitura.
* "[546]dissima": 546 not identified (the decoder gives it in five records; "gran" is 746).
* "s'e[979]arsi": 979 not identified; Kiewning's regest "sich einem Kriege aussetzen" gives the sense.
* "ad sommam": the words are Kiewning's (his only Italian in Nr. 165); the figures are 270 677 06 77, 270 not identified.
* "lo porta molto […]": figures 62 ?99 94 26 09 at a line start, not resolved ("maggiore" does not fit them).
* Page 2: "camineranno […] loro [?s]vantaggio", "r[…]", "preparar[?si] […]", "[676] negotio, per […] e me […]", "da
  [976]", "[?dove] […]", "[…] veni[…] motivato […]": my transcription is uncertain at these places; a better image (or
  DECODE's transcribers) would settle them. 676 is S. E. elsewhere, which does not fit "promuover [676] negotio".

## Group values (proposals; extra_groups.json not edited)

* 394 = elettore: R300 "l'[394] nuovo di Magonza", "li altri [394] e particolarmente quello di [?Baviera]"; R293
  "[394] Palatino"; R311 "dalli altri [394]".
* 695 = segretario: R300 (regest "nicht seinen Sekretär"), R297 "giorni sono il [695] d'Aitona" (regest of Nr. 164
  "kehrte der Sekretär Aytonas zurück").
* 444 = Grigioni: R300 "con le genti imperiali a [444]" (G-H range between 439 generale and 457 heresia); R305 "li passi
  de [444]"; R306 "restasse S. M.tà in [444]". (R299 "gli [444] [664] preparato" against print "gli fusse preparato"
  does not fit: check that place.)
* 964 = Venetiani: R300 "molto meno a' Signori [964]" against regest "noch die Venetianer"; R297 "contro [964]", "per
  infestar [964]".
* 404 = espediente: R300 "parerà [404]"; R303 "per [404]", R313 "più [404] per S. M.tà".
* 424 = Fiandra: R300 "in Italia o in [424]" (regest "in Italien oder Flandern"); R302, R307 "perdere in [424]".
* 259 = [?Baviera], 493 = [?Lega], 326 = [?cifra]: see holes.

## Result

Read in part: page 1 reads as sentences (holes listed above, mostly single words); page 2 in part, the blocker being
the legibility of my own transcription of figures DECODE never transcribed. Clean share 0.557
(`docs/_check_reading.py --file`, 34 of 61 sentences), from 0.167.
