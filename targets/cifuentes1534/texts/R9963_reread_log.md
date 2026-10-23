# Re-reading log, R9963 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b25)

## Starting point

Reading audit (22 Oct): "decoded, not read"; no text of R9963 in the repository beyond fragments quoted in NOTES. The
f. 54r decipherment had been identified on 21 Sept but not transcribed.

## What was done

1. **Every file on the DECODE record**: the six images already fetched to the main checkout
   (`C:\Users\dbour\cypher\targets\cifuentes1534\decode\`, git-ignored) were all opened. No DOC_* text or other
   attachment on the record (`decode/rec9963.htm`). Order: P1 = address/docket (f. 54v), P2 = f. 53r (file _002),
   P3 = f. 53v (_003), P4 = f. 54r? right half, clear tail and subscription (_004), **P5 = file _006, the verso of the
   decipherment sheet (faint show-through), P6 = file _005, the decipherment itself** (NOTES of 21 Sept had images 5
   and 6 the other way round; the decipherment is record image 6).
2. **Existing text?** Yes: the contemporary decipherment, one leaf, secretary's hand, 28 lines. Transcribed line by
   line from native-resolution strips (research/reading_audit/b25_crop.py) into `f54_decipherment.txt`, spelling and
   abbreviations as written. Doubtful places zoomed: l. 5 "el termino dllos e viij meses", l. 18 "venian a v~se",
   l. 22 "me dixo dy/ V. mag." (read [?q]), l. 25 "el dho [?] a su casa", l. 28 the secretary's pointer to the clear tail.
   Not known in print: not on Tomokiyo's AGS Estado page (21 Sept check); Luo 2021's edition was not searched for leg. 862.
3. **Clear text** of the letter transcribed from P2 and P4 (opening, the struck cipher line's marginal gloss "tienen
   los fisicos poca esperança de su vida", the date "Rome iij Septembris MDxxxiiij", the subscription "besa los reales
   pyes y manos"). The signature is a flourish; "[?el conde de Cifuentes]" from the docket.
4. **Alignment with the figures.** No key table is in the repository, so the cipher was not decoded sign by sign. Checks
   made: (a) the decipherment carries the letter's clear islands "y en este proposito me dixo que havia un mes que le"
   and "Tambien" at the same places; (b) the cipher line on f. 53r before the first island ends with the clear numeral
   **xviij**, where the decipherment has "[?e] viij meses": the number is carried by the letter itself and the reading
   gives xviij; (c) the run "q L 20 4 m b" stands right after "Tambien ... q tt m o c" and again at the start of the next
   line, where the decipherment has "el dho embaxor q le havia dho el embaxor" (the repeated word). The key itself: not
   in AGS's online inventory for leg. 862; the 1530s Rome cipher of Charles V is reconstructed in Luo (2021) (memory note
   charles1536), not consulted here because the decipherment covers every cipher line.
5. **Reading** (`R9963_reading.md`) = clear text + decipherment, word for word, abbreviations expanded; spelling not
   modernised. Holes: [?de los], [?verse], [?que], "el dicho […]", [?el conde de Cifuentes]. No word supplied.
   Look-alike alternates: none used (no sign-by-sign decode; 0 letters rest on a look-alike alternate).
6. **Score** (research/reading_audit/b17_score.py, es, reading body): **0.756 (31/41)**; explicit holes (HOLES=1)
   **1.00 (41/41)**. Before: no text (0.00). The unclean sentences are 16th-century spellings and names the modern list
   does not know (scriui, offrescia, syn, ny, embio, lantzgraue, Nassao, yua, pyes); the sentences hold.

## Result

Read from the contemporary decipherment (grade A: coherent sentences, five scattered holes; figures checked at three
anchor points, not sign by sign).

## Open

- "el dicho […]" (f. 54r l. 25), a short abbreviation: blocker illegible.
- The cipher not decoded sign by sign against a key: blocker not-attempted (not needed for the reading).
