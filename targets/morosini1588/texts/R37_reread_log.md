# Re-reading log, R37 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R37_decryption.txt` (character model on DECODE's D1701 under Meister
no. 40): subject clear (Saluzzo) but garbled words in most lines ("otio roiaume", "sifate tolerati [RE DI SPAGNA]",
"in calci ando mila partita"). Clean-sentence share 0.567.

## 1. Is there a text already?

- DECODE images: 4 cipher pages (256r–257v) and 2 "cleartext" images: clear despatches, not a decipherment. DECODE's
  header: "dup.ta di li XXI Nobre" (a duplicate of 21 November 1588).
- Print: Tempesti (1754) II, book VII §§ XVIII–XX covers the Saluzzo affair from other letters (Poigny's mission,
  Nemours offered as governor) but does not paraphrase this one. Rome's decipherments (Francia 27) not imaged.

## 2. Word decode and hand re-parse

From `R37_worddecode.txt`; corrections in `R37_corrections.tsv` (43 rows). Main causes:
- Undotted or misplaced codes: 129 and 196 (duca di Sauoia, several times), 131 (cardinale), 114, 147 (dot on 4),
  217, 219, 221.
- The m + 8 abbreviation for -mente (facilm., chiaram., prontam., publicam., particolarm.) and "Sua Alt." with a null 8.
- Decoder's wrong splits on correct figures: "incalciandomi la partita del ordinario" (decoder "in calci ando mila
  partita"), "sciegliese", "giustificaria", "lodarono le loro maestà", "conosciuta", "bastaua", "Pugni" (Poigny),
  "Sauoia" written out in letters (257r l. 8), "marchesato" with 56 che inside.

## 3. Image checks (crops, scratchpad only)

- 256v l. 14 ("obligarlo a … in Piemonte"): transcription matches the image ("2 1 2 3 0 1 7 3 5 3 5 0 0 5"); no word.
- 256r l. 20 ("si … negotio"): image reads "4 5 1 7 2 0 7 0 3 5 4 0 9 1 5 1 1 7 9" (DECODE "2 0 9 0"); still no word.

## Result

Before 0.567 → after 0.746 clean-sentence share (on the "## Reading" body). By hand: 5 unread stretches ([…]) and 3
partly carried words in about 780 words; every sentence carries. Grade A (few holes; the corrections are mostly
decoder splits, about 12 single-figure slips from context).

## Still open, and why

- Opening (256r l. 2) and "con le loro maestà, […] feci" (ll. 2–3): no parse.
- 256r l. 20 "si […] negotio" and 256v l. 14 "a [?…] in Piemonte": checked on the image, figures as read, no word; an
  encipherer's slip (no outside material to settle it).
- "a li [?17] del presente": a plain number or a null + i.
- The closing formula (257v ll. 7–8) not read.
