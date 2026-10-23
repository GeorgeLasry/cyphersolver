# Re-reading log, R4936 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b15)

## Starting point
Reading audit (22 Oct): decoded, not read. A provisional transcription and an unspaced mechanical decode with open
q/g, c/p, i/n confusions; `_check_reading.py` 0 of 16 sentences.

## What was done
1. **Is there a text already?** The DECODE record has two images and no document attachments. Image 1 has a later
   pencil gloss under the first cipher line only ("persvadealni kell..."). Print: Lukinich (Századok 1908, second
   instalment) describes the 1645 Warsaw mission and cites Bethlen's originals in the Keresd archive, with no
   decipherment; Szilágyi's *A linzi béke okirattára* (1885) and *Erdély és az északkeleti háború* I were grepped:
   nothing. No contemporary or printed text.
2. **Transcription** redone line by line from 2.4-3x crops (`R4936-transcription-b15.txt`); 215 label changes
   against the provisional transcription (`R4936_corrections.tsv`). The hand's g/q, c/e, h/r, i/n and a/v are close;
   labels keep the shape seen, and the reading resolves the pair.
3. **Reading** sentence by sentence with the family key unchanged (`R4936_reading_lines.txt`, then
   `R4936_reading.md`, `R4936_en.md`).
4. **Alignment** letter by letter (`research/reading_audit/b15_align.py`, `R4936_align.tsv`): 1,932 reading letters,
   1,794 on the figure's own value, 130 on the other member of a look-alike pair, 6 on another figure inside
   `[?words]`, 2 supplied (`e[s]`). 26 figures unused (the `[...]` runs and stray minims).
5. **Score.** `_check_reading.py` 0.03 on the body. The same checker gives 0.07 and 0.0 on genuine printed 1645
   Hungarian letters from Szilágyi 1885 (`b15_score.py`): its modern word list does not know 17th-c. spelling. With a
   period word list from the 1640s prints the controls reach 0.53-0.60, this reading 0.09 (the cipher's spelling: oe
   for ö, cz, no accents, run-together words). Explicit holes only (`b17_score.py` with `HOLES=1`,
   the brief's rule for period spelling): 0.94 (32 of 34 sentences). Set read, grade B.

## Open
`[?helyes]`, `[?mint]`, `[?oe]`, `[?harom]`, `[?sinceritassal]`, `[?calumnialkosassannak]`, `[?dragont]`, `[?feloele]`;
two unread runs (l. 9 `ngayioqfyi`, l. 16 `vngqxvuv`). The writer (the prince's "we", probably György I Rákóczi) is
not named on the images.

## Failures
- The earlier statistical key (c=u, g=t, q=p) and the noisy-probe hypotheses were not used; the family key stands.
- Segmenting the old transcription against a period word list (scratch) gave many short false words; reading on the
  images was needed.
