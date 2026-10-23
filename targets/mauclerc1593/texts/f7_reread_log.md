# Re-reading log, fr. 3985 no. 7 (f. 20) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b30)

## Starting point

Reading audit (22 Oct): "decoded, not read"; nothing of the letter in the repository. The 22 Oct note pointed to an
interlinear decipherment on views 6-13. Clean-sentence share before: no text (0.00).

## What was done

1. **Images.** Gallica btv1b90606498 through the openapi.bnf.fr IIIF (research/reading_audit/b29_gallica.py): views
   5-52 at 500-1000 px, views 15, 41, 42 at full size (about 4700 x 6600). The IIIF answered every request (no 403).
   No DECODE record is known for this letter.
2. **The volume's own inventory** (IIIF manifest, Description field, the BnF catalogue's item list) settles where the
   texts are: item 4 is "Deschiffrement de la lectre du docteur MAUCLERC a Mr de Creilg, a Rome. A Paris, ce IIIe aoust
   1593", item 7 "Lettre, avec chiffre, du docteur MAUCLERC ... a monseigneur de Creilg, a Rome ... De Paris, ce 4
   d'aoust 1593". **Views 6-13 are not the letter** (the 22 Oct note was wrong): the cipher letter is view 41 (folio
   20, one page; the address/endorsement on view 42), and the decipherment is a separate leaf, view 15 (folio 7). There
   is no interlinear decipherment on f. 20: the letter is written in a disguised cursive with code numbers (16, 22, 49,
   1730, 812 ..., and longer figure groups such as "8128155 0F").
3. **Existing text?** Yes: the contemporary decipherment, f. 7, one secretary's hand, 35 lines and the signature
   "Mauclerc", dated "3 d'aoust 1593" in the corner. Transcribed line by line (`f7_decipherment.txt`) from half-line
   strips at native resolution (research/reading_audit/b30_strips.py, b30_lines.py; zooms with b25_crop.py).
   The Latin passages are underlined in the original.
4. **Check against the figures of f. 20.** Not sign by sign (no key in the repository; the letter mixes a disguised
   alphabet with code numbers). The f. 20 lines carry the decipherment's words at these anchors: l. 1 "Mosieur mo Mre
   depuis mes dernieres ... bien amples ... vous sçauez ... passé"; l. 2 "par lesquelles vous iugerez que [16] ..."; l. 4
   "... Darrest pretende ... Mais"; the subscription "de Paris ... d'aoust 1593 ... serviteur". The date differs: f. 7
   "iii d'aoust", f. 20 and the inventory "4 d'aoust" (the decipherer's slip or the date of decipherment). Letters
   resting on a look-alike alternate: 0 (no sign-by-sign decode).
5. **Holes.** Doubtful readings of the hand: [?ae] (l. 2, before "In Guisium"), [?heurter], [?bel] (l. 4-5), [?iuré]
   (l. 18), [?et] (l. 20), [?perdroit] (l. 21), [?iure] (l. 26), [?encor] (l. 34). Not read: l. 1 "com[...]" under an
   ink blot; l. 7 the end of the line (struck words); l. 8 "d'[...]"; l. 9 two words; l. 12 one; l. 14 one; l. 17 one;
   l. 19 the end; l. 22 one; l. 24-25 five words (the hardest stretch). No word supplied.
6. **Score** (research/reading_audit/b17_score.py, LANG_=fr, reading body): **0.673 (37/55)**; explicit holes
   (HOLES=1) **0.909 (50/55)**. Most unclean sentences are the Latin passages the French word list cannot know; five
   fail on holes (l. 7-9, l. 24-25). Reader's judgement: the letter reads through as a coherent report (the Spanish
   offer of the Infanta and Guise, Mayenne's resistance, the truce in place of the election, the princes' oath never to
   make peace with Navarre, Nevers's embassy to Rome), with one obscure stretch (l. 24-25).

## Result

Read from the contemporary decipherment (grade B: sentences hold; the decipherment transcribed from a difficult
secretary hand with 14 short holes; checked against the cipher at anchor words only).

## Open

- l. 24-25 and the scattered […]: blocker illegible (the decipherer's cursive; a second reading by a palaeographer
  could close them; the cipher f. 20 could supply them once its alphabet is set out).
- The sign-by-sign decode of f. 20: blocker not-attempted (not needed for the reading).
- Siblings fr. 3983 f. 268, fr. 3984 f. 33 and the register summary fr. 3983 f. 140r (Dudout): not opened this session;
  blocker not-attempted.
