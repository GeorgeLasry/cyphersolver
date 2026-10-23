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

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`; the pages are clean; the row grid of 534r runs short, so its lines were found by eye), cancellation
strokes looked for (none), the figures parsed (`r2p_parseall.py`).
Filled (every figure carries the word):
- 533v l. 12 "lettere del Re" (26 35 05); 534r l. 1 "con uno del duca" (3 01 191); 534r l. 31 "sua prudenza"
  (33 37 26 35 01 12 212; it was supplied).
Left, with blockers:
- 533r l. 4 "[…] questo […]": "0 4 9 5 7 2 2" (best parse "gosfcr"). Blocker: no-key-material.
- 533r l. 4 "[…] questo […] dele cose": "4 8". Blocker: too-short.
- 533r l. 16 "ocasione Entrata [?…] S M": "3". Blocker: no-key-material.
- 533r l. 27 "M tà […] il perdonò": "9 1 5 3 5 0 1 5" (best parse "oelt"). Blocker: no-key-material.
- 533v l. 14 "presto gli inuiar[i]a gente per": "1 7 1 0 1 3 7 1 7 2 1 0 0 2" (best parse "inuiara"). Blocker: no-key-material.
- 533v l. 16 "anco castelo […] et che": "5 3 5 0 0 1 7 8" (best parse "eeri"). Blocker: no-key-material.
- 533v l. 23-24 "che subito [?hauuti] s incaminarano": "1 4 | 2 1 3 7 3 5 1 7 1" (best parse "hauei"). Blocker: no-key-material.
- 533v l. 31 "dicono che […] molto inanzi": "5 3 5 0 0 5" (best parse "eull"). Blocker: no-key-material.
- 534r l. 5 "da Pluuiers [?doue] dice che": "8 2 6 1 7 1 2 6 9 1 3 7 5" (best parse "didoue"). Blocker: no-key-material.
- 534r l. 26 "del Re [?Adeso] certo che": "8 2 0 2 1 2 6 5 4 1 9 1" (best parse "mrdso"). Blocker: no-key-material.
- 534r l. 27 "corte hauendomi [p] ortate lettere": "2 0". Blocker: too-short.
Result: 3 holes filled; 12 left, each with its blocker.
