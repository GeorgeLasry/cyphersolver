# Catalogue 653: Powhatan Ellis (Mexico) to John Forsyth, 1836–40, coded despatches

NARA RG 59, Despatches from US Ministers to Mexico, vols. 7–9 = M97 rolls 8–10. Frames named `vol. 7 frame NNN` are
M97-008-0NNN (roll 8), vol. 8 = M97-009, vol. 9 = M97-010.

- `reading_19may1836.md`: the coded part of the 19 May 1836 despatch, the clerk's clean copy with `[?word]` where the
  decode does not give the word, and the read-share measure.
- `ct_*.txt`: the code groups of every coded page, transcribed from the images (`ct_f015L` = vol. 7 frame 15, left
  page; `ct_v8f099L` = vol. 8 frame 99; files without L/R are single pages).
- `ellis_values.tsv`: new values and corrections for the jqa table, each with the words that fix it (T = one context,
  tentative).
- `code_table.tsv`: copy of `targets/jqa/code_table.tsv`, used as the base table.
- `cleantext_19may1836.txt`, `print_*.txt`: the clean texts the decode is measured against (the clerk's copy of
  19 May; passages of Bosch García, *Documentos de la relación de México con los Estados Unidos* III, UNAM 1984, by
  date).
- `dec.py`: decode a transcription (`python3 dec.py ct_f015L.txt`).
- `readmeasure.py`: read share of a passage (`python3 readmeasure.py cleantext_19may1836.txt --corr --variants`;
  other passages with `--files`, e.g. `python3 readmeasure.py print_1221.txt --corr --variants --files v8f211L`).

Passages and their pages (for `--files`): 0528 = f025L,f025R,f026L,f026R,f027L; 0625b = f071L,f071R; 0803 = f123,f124L;
0924 = f203R,f204L,f204R; 1026 = f323; 1130 = v8f099L; 1214 = v8f208R,v8f209L; 1221 = v8f211L;
1839 = v9f298,v9f299,v9f302,v9f303.


## Provenance (added in this repository)

Copied unchanged on 28 Oct 2026 from https://gist.github.com/brackxm/541493ba267c2a224b8ff5006215bc38 (revision
a98948e7db62, 27 Oct 2026) with Michael Brackx's permission on issue #120: text and data under CC BY 4.0, code under
MIT, with credit. `code_table.tsv` is left out: it is a copy of `targets/jqa/code_table.tsv`.
