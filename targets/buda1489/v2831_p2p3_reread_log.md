# Re-reading log, Vestigia 2831 p. 2 ll. 17-30 and p. 3 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b25)

## Starting point

Reading audit (22 Oct): the V2831 entry split; p. 2 ll. 17-32 and p. 3 "decoded, not read" (lines of fragments, the
stacked crops drift from l. 18). Before: the same lines in `v2831_reading.md` score 0.158 clean sentences (6/38, it),
explicit holes 0.342.

## What was done

1. **Existing text?** Vestigia record 2831 (`vestigia/doc2831.json`): four page images (duplicated from two sources),
   no attachment, no edition ("publikaciok" empty). DECODE has no record of 2831. Print: Somogyi 2016 prints ll. 1-2
   only; MDE IV (Nagy & Nyáry 1878) prints Maffeo's extracts from 12 Jan 1490 on, nothing for 22 Nov 1489 (print search
   of 9 Oct 2026, main-checkout NOTES); Labancz 1491 and Berzeviczy 1914 have nothing for it. No contemporary
   decipherment.
2. **The key in the archive's holdings.** The DECODE list was searched for Milan key records of the 1480s-90s: R1099
   (MTA MS 4937/II/0063) and R1169 (ASMi Sforzesco 650/3) are the key of the 1488 Arcimboldo-Oliva embassy to
   Matthias ("Cum Francisco Oliva profecturo cum D. Guidantonio Arcimboldo ad Ser. D. Regem Hungariae, Mediolani 27
   Febr. 1488"), a different key (che = ds, a+ = Protonotario, m^a = Re de Hungaria). Then the headings of all 134 key
   records of ASMi Sforzesco cart. 1597 on DECODE (PDFs from the it1583 download; contact sheets
   research/reading_audit/b25_keysheets.py) were read: **cart. 1597 no. 111 (DECODE R5411) is headed "Cum Mapheo
   Triviliensi"**: the original key of this cipher, with alphabet (torn at T-&), doubles, nulls, a syllable table and a
   22-entry nomenclator (Rex Hungariae M:, Regina M+, Jo. Corvinus, Ludovicus dux Bari, Dux Mediolani, Papa, Imperator,
   Vostra/Sua Dominatio, Sua Maiestas, Sua Sanctitas, Ep. Varadinensis, Madonna Bianca). Transcribed in `key_R5411.md`.
   It confirms Somogyi's reconstruction letter by letter where both exist. A second key "Cum Mafeo Triviliensi" is
   cart. 1597 no. 107 (R5407), a different alphabet, not this letter's.
3. **Sign by sign from the plates** (two helper agents, run to completion, one per page; per-row crops at 2-4x;
   research/reading_audit/b25_buda_rows.py, b25_buda_rows3.py, b25_buda_strips.py): first pass with key.md, second with
   R5411. Line counts corrected: p. 2 has 30 lines (the old L25/L26 and L29/L30 were halves of one line), p. 3 has 31
   (three lines below the old L28 never transcribed). Files: `trans/v2831p2_b25.md`, `trans/v2831p3_b25.md` (sign
   strings, decodes, per-line notes, look-alike counts), `..._corrections.tsv`.
4. **Key values adopted** (from R5411, checked on every occurrence on the page): x̄ (x with a bar above) = Ma, distinct
   from x̸ = et, giving **Roma** for the recurring q^s x̄ (p. 3 L11, L17 twice, L19), "affirmatione", "ma"; M+ = Regina
   (p. 3 L01, L04, L08; were "la Sua Maesta"); a# = Vostra Dominatio (p. 2 L20, L28; p. 3 L18; was "Ex.tia Vostra");
   Q. = Ill.mo Duca de Milano (p. 2 L20); Ra = madonna Bianca (p. 3 L28); + = Vescovo Varadino (p. 3 L24); ƀ = fa
   ("fa con arte", "favore", "facesse"); m: = bi ("bisogno"); B = null; 1 = a; n^o = pp; n^u = rr; ʒ = r.
5. **Flagged for review, not adopted:**
   - the key gives o and o-with-a-tail as **b**, but on these pages an o-form reads t in many words (intercepte,
     state, contentione, constantemente, ducati, arte; p. 3 hundreds) and b in others (habia, ambasiatore, comproba,
     deliberata, bon). Probably two o-forms (the key's T column is torn after its first sign); kept as read (t / b by
     shape class), 9 letters on p. 2 rest on the t reading against the key;
   - δ+ (p. 2 L20) read Papa (the key's Papa sign; look-alike Fe gives no word): sense-supported;
   - g/8 = x in "excusar/excusatione" (p. 3 L13-14; the key's X column is torn): sense only;
   - x̄/x̸ = "mes-" before "sere": sense only;
   - plain q = e (not in the key outside the syllable rows): holds at every occurrence (p. 3 six words, R1098).
6. **Look-alike alternates**: p. 2 ll. 17-30: 15 letters rest on a look-alike choice (+ 9 o-form letters read t against
   the key); p. 3: 59 of about 1,360 decoded letters (4%).
7. **Reading** `v2831_p2p3_reading.md` (English `v2831_p2p3_en.md`) assembled from the two pages; aligned word by word
   with the per-line decodes in the trans files; words not carried are bracketed.
8. **Score** (b17_score.py, LANG_=it, reading body): **0.322 (19/59)**, explicit holes **0.542 (32/59)**; p. 2 alone
   0.294 / 0.588, p. 3 alone 0.341 / 0.537. Before 0.158 / 0.342.

## Result

Stays **decoded, not read**. p. 2 ll. 17-27 now build sentences with scattered holes (the intercepted letters; the
honour of the Duke of Milan and of Ludovico in his contention with the Pope; "either no faith is to be given to any
man in the world, or this must be believed"), and about half of p. 3 does (the Neapolitan ambassador will not stay at
Rome more than eight or ten days; Djem, "fratello dil Turco"; Ferrante; madonna Bianca). But p. 2 ll. 28-30 and eleven
lines of p. 3 remain fragments, and the body is well under the bar.

## Open (blockers)

- p. 2 ll. 19, 21, 23-30 and p. 3 ll. 2, 3, 5, 7, 9, 11, 24, 25, 27, 29, 31: legible letter groups that do not yet
  segment into words: not-attempted beyond these two passes (the key now in hand makes a third pass worthwhile).
- p. 3 l. 15, signs under an ink blot: illegible.
- r̥ (p. 3 L15) and the X, Y, Z, & and T columns of the key (torn): no-key-material.
- the o-form value (b by the key, t in most words): needs review against the other Maffeo letters (R1098, V267).
