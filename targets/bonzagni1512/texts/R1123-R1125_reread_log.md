# Re-reading log, R1123, R1124, R1125 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b14)

## Starting point

Reading audit (22 Oct): all three "decoded, not read": the letters were read at the time (interlinear glosses on
R1123/R1124, a decipherment slip with R1125), but nothing was transcribed in the repository and no key exists here.

## What was done

1. **Every file on the records opened.** research/reading_audit/b14_fetch.py re-fetched the three DECODE record pages
   and every linked file into the session scratchpad: page images only (R1123 4, R1124 2, R1125 5), no attachments,
   no transcription, no comment blocks. The Vestigia photographs in the main checkout (img/v/, 3072x4096) are the same
   shots at the same resolution as DECODE's (3240x4320); the sheet fills about 60% of the frame. Kristóf 2018 (cited by
   Vestigia for nos. 4 and 6) was not found online; a web search turned up only her 2025 article on the Eger diocese.
2. **R1125.** The slip (image 5, a later clear hand) transcribed in full. Aligned with the 12-line cipher block of p. 3
   group by group (texts/R1125_align.tsv): every group has its slip word, and the sign values recur (a, c, d, e, i, l,
   m, o, p, r, s, t). Found: Latin-looking words stand in the cipher among the invented signs ("valent" keyed in from
   the margin, which the slip writes and glosses "denaro"; "indigeo", copied in brackets; "parte", for which the slip
   leaves a blank before "in campo"), and a number ".31." that the slip omits.
3. **R1124.** The interlinear gloss over the eight cipher lines transcribed at 1.5-2.2x; aligned group by group
   (texts/R1124_align.tsv). Two more cipher words in the clear text below, glossed "tazze grande". The clear text of
   pp. 1-2 transcribed so that the reading is the whole letter; the right edge of p. 1 is torn from l. 12 down, which
   leaves [...] at line ends.
4. **R1123.** The clear opening and the first cipher block (ll. 5-9, glosses "a milli ducati d'oro cum poco interesse
   et haveva deliberato mandarci ma la sopragiunta commissione del Re d'Ungaria che li genti habbiamo omnino a
   cavalcare questa nostra donna de [?agosto] come per l'altra ancora copia vederà quella mi ha fatto [?intepidir]"),
   the clear ll. 10-13 and the start of the lower block (fiorini trecento d'oro; madonna Beatrice ... fino ala suma de
   fiorini ducento ...) transcribed. Checks of gloss against cipher: ducati (ϸδλdf3: d u c a t i), dona, del, fiorini
   (σ3nƶ3ϸξ, i in places 2 and 5), trecento (eight signs, t in 1 and 7), che (λθ7), cavalcare split over the line
   end (λdϑϙm|ʧdƶƶ, 9 signs). "potest" (l. 7) is glossed "Re d'Ungaria", "valent" (l. 15) "argenti".
   Not finished: the lower block from "valerano" (about eleven lines, an inventory: coppe, dorate, tondi dodici,
   pesano, marche, oncie cinque, pesetti due ... are legible) and the glossed cipher of p. 2 (il Cardinale de [?],
   Strigonio a Roma, Buda, una certa congregazione). The brown gloss ink there is too faint at this resolution to follow
   word by word, and the key was not rebuilt to decode the signs underneath.

## Result

_check_reading.py on the reading bodies (b14_score.py, it): R1125 0.857 (6/7), R1124 0.625 (20/32; the misses are
mostly inventory words the Italian lexicon does not hold: coppa, tazette, anelle, coramo, el), R1123 0.632 on the
part read. R1124 and R1125 set read. R1123 kept decoded, not read: most of its cipher (the lower block of p. 1 and
p. 2) is not read; the partial reading and its English are kept in texts/.

## Open

- R1123 lower block and p. 2: illegible at the available resolution (faint glosses); not-attempted: a key rebuilt
  from the ~170 aligned words of R1124 and R1125 (sign substitution with homophones for the vowels, a few
  Latin-looking code words) would decode the signs and settle the faint glosses. This is the next step.
- R1125: the code word "parte" and the number .31. (no key material: the slip leaves them out).
- R1124: the torn right edge of p. 1.

## Failures

- A first attempt to read R1123's lower block from blue-channel enhanced crops did not make the faint glosses legible
  enough; several gloss words read in it ("sette", "vinti cinque", "Isadro") stay marked [?].
