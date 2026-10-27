# Work log, poinsett1813

- 2026-10-27 literature: Manning vol. 2 doc. 442 (archive.org djvu text) read; ten "(undeciphered cipher)" places; web search for a decipherment or the 1810 cypher: none.
- 2026-10-27 access: M37 roll 2 frames 0091-0102 fetched from the NARA catalogue (naId 213803757); letter at 0092-0094.
- 2026-10-27 transcription: P1-P9 on frames 0093-0094, 437 groups / 256 distinct (`transcription.tsv`); P0 on 0092 illegible after background flattening.
- 2026-10-27 known keys: JQA/Department 1803-40, Armstrong THE=972, Pinckney, 1788 legation, Jefferson 1787, Mountflorence 1801 applied directly: noise.
- 2026-10-27 known keys: `shift_test.py`, every constant shift and mod 1600/1700 of the same tables, scored with lang en-modern: best z 4.3 of ~9,000, junk decodes; ruled out.
- 2026-10-27 sibling: Sumter, Rio 1813 (M121 vol. 1A frames 0035-0039, interlinear decode): the = 798, of = 1399; not this code.
- 2026-10-27 sibling: Poinsett 14 June 1814 (M37 roll 2 frame 0098, duplicate 0100) found in the same code with a clerk's interlinear decode; 88 values aligned (`key_1814.tsv`).
- 2026-10-27 decode: key applied to the 1813 groups (`decode.py`): 158/437 = 0.362 have a value; fragments, no sentence reads yet.
- 2026-10-27 key-rebuild: context pass over the 1813 decode; only "Lima" (249 413, twice in the Lima paragraph P4) cross-checks sibling syllables; the other unknown groups occur once or twice in contexts that do not fix them; no values added.
- 2026-10-27 literature: Weber 1979 not online (BL on-premises only); HSP "Calendar of Joel R. Poinsett papers in the Gilpin collection" (1941) is full view on HathiTrust (mdp.39015034759822) but behind a bot check; not searched.
- 2026-10-27 lead: Manning vol. 2 (Lowry to Graham, 30 Nov 1816) says Lowry, sent to Caracas in 1810, got a cypher to correspond with Shaler and Gelston and used it once to the Department; possibly the 1810 agents' code. M84 roll 1 (La Guaira, rg-059/302031/M84/M84-01) sampled every 6th frame to 0187: no code run seen at thumbnail scale; M37 roll 1 (Shaler, frames ~0400-0760) has no code frames per the NARA triage. Not yet checked frame by frame.
- 2026-10-27 sibling: M84 roll 1 frames 0014-0090 (Lowry 1810-12, Scott 1812) viewed frame by frame: all clear text, struck-out passages on 0057-0058 are cancelled words, no code; Lowry's ciphered letter not in this file. Lead closed for now.
- 2026-10-27 catalogue 651: 14 June 1814 RC (0097-0098) and Duplicate (0099-0100) transcribed line by line with the clerk's glosses (`transcription_1814.tsv`); merged text 123 groups / 90 distinct (`ciphertext_1814.txt`).
- 2026-10-27 prior art: Manning vol. 1 (1925) doc. 201, pp. 335-336, prints the 14 June 1814 letter with the code passages in clear (the clerk's decode, from MS. Consular Letters, Buenos Aires I). Catalogue 651 already deciphered.
- 2026-10-27 key corrections from the two copies and Manning: 964 principle (not prince), 1236 it (not 236), 1087 two (not 1037), 737 between (not 727), 1179 ct / 765 ion (resplit), 480 t added; key_1814.tsv 95 values.
- 2026-10-27 reading 1814 (`decode_1814.py` -> `reading_1814.txt`): 122/123 = 0.992 have a value; 39 open (unglossed by clerk and Manning).
- 2026-10-27 re-ran decode.py on 1813 with the corrected key: 161/437 = 0.368 (was 158); still fragments.
- 2026-10-27 Manning vols. 1-2 searched for other Poinsett letters with code: none decoded besides 1814.
