# Re-reading log, R53 and R54 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b21)

## Starting point

Reading audit (22 Oct): both decoded, not read. Lasry's partial F22b key (about 70 elements) through the segmenting
decoder gave R53 in fragments and R54 mostly noise; a key rebuild from the 1,448 figures (14 Oct) had failed.

## 1. Is there a text already?

Yes. Every file on DECODE R53 and R54 fetched with the project cookie (`research/reading_audit/b17_fetch.py`, into the
session scratchpad). Only the DOC_*.txt files had been in `decode/`; five png attachments filed as "[cleartext]" had
never been opened:

| attachment | folio | what it is |
|---|---|---|
| R53 DOC_R53_D1080 | 499r | the clear letter: 'Giunsi à Molins ...', Morosini's illness (bleeding, physicians), his journey |
| R53 DOC_R53_D1094 | 498v | address to Cardinal Montalto, docket '1589, 4 di maggio ... da Molins' |
| R54 DOC_R54_D1081 | 502v | address to Montalto, docket (with the R54 cipher bleeding through) |
| R54 DOC_R54_D1099 | 500r | **contemporary decipherment of R53** ('Il Navarro per quello che mi disse domenica ...') |
| R54 DOC_R54_D1095 | 500v | **contemporary decipherment of R54**, continuing 500r ('se gli andavano ingrossando ...') |

The two cipher passages are one text deciphered on one leaf: R53's last clause ('... di Umena, al quale si tiene')
runs on into R54's first ('se gli andavano ingrossando ogni giorno'). R53 is therefore from Moulins too, early May
1589 (the clear letter on f. 499r; docket 4 May), not 'Tours, spring 1589'.

## 2. Transcription

`R53_decifrato_f500r.txt`, `R54_decifrato_f500v.txt`, from native-resolution strips. The decipherer's hand writes
final e much like i; the capital N looks like H (so Lasry's 'h.s.re' for code 1̇51 is N.S.re, Nostro Signore). The
decipherer wrote the code figure '1̇85' over 'Navarro' and added 'non' in the margin of f. 500v ('1 non').

## 3. Alignment with the figures

`research/reading_audit/b21_moro_align.py`: dynamic programming over DECODE's digit transcription and the
decipherment's letters, with Lasry's key (elements of 1-2 figures; 3 for nomenclator codes; unkeyed elements may
stand for 1-4 letters; the decipherer's doubled consonants as letters without figures). Output `R53_align.tsv`,
`R54_align.tsv` (element by element) and `R53_words.tsv`, `R54_words.tsv` (word by word: figures and what the key gives).

- **4 = c**, unkeyed in Lasry's list, stands for 'c' at all 17 of its places in the two records (`f22b_values_b21.tsv`):
  adopted. With it, 4 98 and 4 9 5 read c-he / c-h-e, the decipherer's 'che' everywhere; Lasry's 495/498 = 'chi' is
  not borne out (no 'chi' in the decipherment).
- The undotted '1 85' of D1717 (three places) is the Navarro code 1̇85; 216 = me, 130 = ma as in Lasry's list.
- 29 single elements take a value only from the decipherment (57 q, 117, 637, 42, 53 0, 81, 38, 27 lu, 75, 11 ...):
  one place each, not adopted. 89 is 'se' (fosero, disegnaua) and 'si' (si tiene): left as Lasry's si.
- Letters: R53 603 of 693 the figures' own value (0.87); R54 468 of 622 (0.75) plus 61 on digits DECODE marks '?',
  fixed by the decipherment. **No letter rests on a look-alike alternate.**

## 4. Where the figures and the decipherment differ

The reading follows the figures where they give another word: R53 *grosa* ('grandi'), *la fece* ('lo'), *la quale
giunte* ('Le quali'), *che ne fossero* ('che vi'), *Lemans* ('Limans'), *erano* ('sono'; checked on the image, last
line: 1̇16 5 41 36 130 = re e-ra-no ma-); R54 *non lo habbia* ("non l'habbia"), *dagli* ('dalli'), *tutto quello*
('tutti quelli'). Where the figures slip or have no value the decipherment carries the word: R53 'dabene' (written
76 28 70, da-gi-ne, checked on the image), 'mi disse domenica', 'francesi', 'seco', 'dissegni', 'al quale si tiene';
R54 'di qui', 'fin hora', 'perche', 'distrutti i primi', and 'non' (the decipherer's marginal insertion; no figures).

## Result

| doc | before (decode file) | after (`_check_reading.py` on the reading body) | rests on |
|---|---|---|---|
| R53 | 0.40 (6/15), decoded, not read | 0.833 (10/12) | decipherment f. 500r + figures (0.87 of letters) |
| R54 | 0.42 (5/12), decoded, not read | 1.0 (11/11) | decipherment f. 500v + figures (0.75, +0.10 on '?' digits) |

Both read, grade A. Open: the 29 single-occurrence elements (too short to fix a value) and the figure stretches that
give no word (DECODE's '?' digits; not re-transcribed from the image here).

Example (R53): 'Onde si è fatta una mescolanza alla Corte di heretici et di Catholici, che è odiosa à tutti li
huomini dabene.' — So a mixing of heretics and Catholics has come about at the court, which is hateful to all honest
men.
