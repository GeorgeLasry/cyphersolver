# Work log, poinsett1813

- 2026-10-27 literature: Manning vol. 2 doc. 442 (archive.org djvu text) read; ten "(undeciphered cipher)" places; web search for a decipherment or the 1810 cypher: none.
- 2026-10-27 access: M37 roll 2 frames 0091-0102 fetched from the NARA catalogue (naId 213803757); letter at 0092-0094.
- 2026-10-27 transcription: P1-P9 on frames 0093-0094, 437 groups / 256 distinct (`transcription.tsv`); P0 on 0092 illegible after background flattening.
- 2026-10-27 known keys: JQA/Department 1803-40, Armstrong THE=972, Pinckney, 1788 legation, Jefferson 1787, Mountflorence 1801 applied directly: noise.
- 2026-10-27 known keys: `shift_test.py`, every constant shift and mod 1600/1700 of the same tables, scored with lang en-modern: best z 4.3 of ~9,000, junk decodes; ruled out.
- 2026-10-27 sibling: Sumter, Rio 1813 (M121 vol. 1A frames 0035-0039, interlinear decode): the = 798, of = 1399; not this code.
- 2026-10-27 sibling: Poinsett 14 June 1814 (M37 roll 2 frame 0098, duplicate 0100) found in the same code with a clerk's interlinear decode; 88 values aligned (`key_1814.tsv`).
- 2026-10-27 decode: key applied to the 1813 groups (`decode.py`): 158/437 = 0.362 have a value; fragments, no sentence reads yet.
