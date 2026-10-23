# Re-reading log, SP 53/11 no. 50I (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b37)

## Starting point

Reading audit (22 Oct): "decoded, not read" (excerpt only). The repository held Tomokiyo's numeric transcription
(`../SP53_11_50b.txt`) and his published opening clause; no reading file: before = 0.00 (excerpt 0.09 by tokens).

## 1. Is there a text already?

- DECODE R3839 re-fetched (`b37_fetch.py`, scratchpad): three images (cover f. 132, a blank/backing view, the
  enclosure f. 138); no attachment, transcription or comment. No decipherment on f. 138 or the cover.
- Neighbours: R3838 (Somer's worksheet and key for SP 53/11 no. 35, another alphabet) and R3840 (clear extracts of
  Mary's letters) were checked in Sept (NOTES); nothing for no. 50I.
- Print/scholars: Tomokiyo, cryptiana mary3.htm (re-fetched 23 Oct): still only the opening "__The beirar is domestik
  servand to the erle of shrevisbvry__ ...", the numeric transcription and the glyph key image; "some symbols remain
  to be identified". Biermann and Lasry's 2023 decipherment is unpublished. CSP Scotland vi 45 calendars only the cover.

## 2. Reading on the image: the concordance

- A crib search on the numeric labels (`b37_wals_crib.py`, `b37_wals_crib2.py`: one-to-one letters, word signs inside
  words, up to 22 nulls) found **no** placement of Tomokiyo's opening: his labels are not one value each.
- Concordance built instead by reading f. 138 glyph by glyph against the label sequence, line by line (crops of the
  DECODE image, 3567 px wide, glyphs about 35 px; scratchpad), and taking each glyph's value from Tomokiyo's key image:
  `no50I_concordance.tsv` (label, glyph, value, where checked). The opening clause comes out exactly
  (*The beirar is domestik servand to the erle of shrevisbvry*: *the* = T + HE sign, *servand* = serv + AND sign),
  which checks the method.
- Lines 1-10 checked on the image; lines 11-14 only partly (the DECODE image is low-resolution and the lines slope, so
  the crops of the last lines cut the glyphs; two attempts).
- Problems found: Tomokiyo's label 10 covers the key's B and K (s-loop and long s: *beirar* / *domestik*, *havkes*,
  *kept*); label 35 covers the g-like null and, in *mai[d]* and *sov[l][d]*, apparently the 9 of D; label 84 is the
  round P in *capitane*, *importance*, *pacqvet* (x2), *kept*; label 13 is *l* in *himself* but a W-like glyph in l. 2.
  These are look-alike merges in the transcription, not key problems.
- 20 labels stay without a value (07, 09, 39, 44, 46, 49, 58, 59, 72, 77, 79, 82, 86, 87, 89, 91, 92, 95, 97, 98),
  seven of them the key's own "unknown" signs. Context suggests 58 THE QUEEN, 87 YOUR, 95 THE, 49 OF; not adopted.

Decode: `no50I_decode.txt` (`b37_wals_dec.py`). It reads in stretches: the bearer is Shrewsbury's servant, is to pass
in a captain's caravel to buy hawks, has offered to carry the packet, "I durst vryte nothing of importance be him",
"you may sovnd and try him, and be him send me ansver", "that there be nothing aganist [58] and [95] stait [49] the
realme, and faylle not to advertis me vhitner [72] the present pacqvet ... cvm to [87] handis vel closit or not".

## 3. Alignment

Every unbracketed word of `no50I_reading.md` is a run of `no50I_decode.txt` with word division supplied; words that need
a merged-label value or an unchecked glyph are bracketed [?word].

## 4. Bar

- `b17_score.py` LANG_=en: 0.077 (1/13); HOLES=1: **0.154** (2/13). Far below 0.60.
- Look-alikes: the merged labels (10 b/k, 35 d/null, 13 l/w) touch about 10 of 562 tokens; not the obstacle.
- Reader's judgement: three sentences hold (the bearer, "I durst vryte nothing of importance be him", "You may sovnd
  and try him"), the rest break on unknown signs.

Verdict: **decoded, not read** (partial reading kept). What would finish it: (a) re-check lines 11-14 glyph by glyph on
a better image (TNA SP 53/11 f. 138 at full resolution; the DECODE copy is small), (b) identify the 20 open signs from
their contexts once every line is checked, or (c) Biermann and Lasry's plaintext (ask George Lasry).
