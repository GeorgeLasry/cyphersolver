# Re-reading log, R58 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R58_decryption.txt` (character model on DECODE's D1722 under Meister
no. 40): the news clear in outline (Jargeau, the Loire towns) but garbled in most lines ("riniperatore", "ne niolto
dicono esere giunti a tiam berini", "di francesi era haluario metersi in una trista"). Clean-sentence share 0.598.

## 1. Is there a text already?

- DECODE images: 3 cipher pages (533r–534r) and 3 "cleartext" images: clear despatches, not a decipherment. The cipher
  page carries a clear heading: "Molins à li v di Luglio 1589. dup.lo". No glosses.
- Not in Tempesti. Rome's decipherments (Francia 27) not imaged. The events (Jargeau, Pithiviers, Étampes, Soissons's
  escape from Nantes in a basket) are well known from French sources, but no copy of this letter was found.

## 2. Word decode and hand re-parse

From `R58_worddecode.txt`; corrections in `R58_corrections.tsv` (58 rows). Main causes:
- Place names outside the vocabulary: Giorgio (Jargeau), Gian (Gien), Pluuiers, Etampes, Montereo, Ciamberi,
  Ouernia, Meos, Longauila, Forges, san Marceo / san Uitor / san Iaches / san Germano (the decoder had "cuore san marco
  a nuire ora niarchese"), Nantes (decoder "di francesi").
- Plain-figure numbers between null 8s: 30 milia, 25 milia (decoder "un milia", "a emilia").
- Spurious dots: 191 (ha fato), 500 (hauere), 037 (di nuouo), 022 (parte).
- The m + 8 abbreviation: liberam., longam. (twice), amoreuolm., diritam., alegram.
- Decoder's wrong splits on correct figures: "et nondimeno da poi riceuti", "in iscambio", "et partito ancora",
  "due giorni dopo", "si era saluato con metersi in una cesta", "referisce ancora", "onde io non saprei".

## 3. Image checks (crops, scratchpad only)

- 533r l. 27 ("[…] il perdonò, ma però si tiene"): the crop caught the line; the figures before "perdonò" lie at the
  left edge and were not resolved further.

## Result

Before 0.598 → after 0.765 clean-sentence share (on the "## Reading" body). By hand: 6 unread stretches ([…]) and 6
partly carried words in about 990 words; every sentence of the news carries. Grade A.

## Still open, and why

- Opening (533r l. 4), "Entrata [?…]" (l. 16), "[…] il perdonò" (l. 27), "castelo […]" (533v l. 16), "che […] molto
  inanzi" (533v l. 31): short stretches with no word parse; no outside blocker, a closer image pass may close some.
- "[?Adeso] certo" (534r l. 23): figures "m a d s o".
- The last figures after "ala singolar sua" (534r l. 30) were not transcribed by DECODE.
