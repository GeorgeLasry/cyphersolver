# f. 168 (Nevers to Pisany, 14 Oct 1593): re-read log, 22 Oct 2026 (Claude Opus 5.5, batch mix1)

Brief: research/reading_audit/REREAD_BRIEF.md.

## 1. Is there a text of it already?

- On the leaf: no. f. 168 is a register copy; the cipher has no interlinear or marginal decipherment and the clear
  text around it does not repeat it.
- Neighbouring folios: the same register (fr. 3986) holds the other Nevers letters of Oct 1593 (Revol, ff. 146v,
  157v; see targets/revol1593) in the Court cipher no. 60, not this letter.
- Print / others: Tomokiyo (cryptiana nevers.htm) reads only line 1 ("ne sera receu come Ambassadeur pour pluseurs
  resons. Je luy ay demandé"). No edition of the Nevers-Pisany letters of 1593 was found (NOTES, 17 Sept). The
  original letter as received by Pisany is not located.

## 2. Read on the image

Image: openapi.bnf.fr IIIF `ark:/12148/btv1b9060631k/f332`, full size 4948 x 6958, fetched into the scratchpad;
cipher lines located by an ink projection (centres y 1410, 1555, 1690, 1820, 1950, 2085, 2215; last line y 3675),
cropped in thirds at 1.4-1.6x and the doubtful places at 2.0-2.2x.

What moved (all in f168_corrections.tsv; corrected transcription ct_3986_f168_r2.txt):
- Bars were mis-assigned in the first pass: 30̄ 8̄ is one bar over 38 (ne); 5̄ 67 is 56̄ 76 (je y); 6 81̄ is 68̄
  (faire); 26̄ 5 12 32 is 26̄ 52̄ 32 (par·le·r = parler); 3̄ 6 is 36̄ (non); 47̄ is 47̄ 9̄ (lettre qu'il); 69 in line 4
  and 15 in the last line are barred (faict, propos).
- Segmentation: "ı ϑ" before 6 9 in line 2 is 18 (s), not 1 0 8; the line-3 tail 1 ϑ 3 5 | ϑ 3 is 18 35 83 (sui);
  line 5's "15 8 79" is 15 18 79 (the 8 was the crop overlap); "58 71 77 4̄" is 57 17 74̄.
- Copyist's habits seen across the page: 24 (plain "sa") for a twice (ch-a-rge, j'y alle) while it is "sa" proper
  in "savoir" (line 7); 27̄ (on) for 29̄ (ou) in "ou non"; 51 for 57 in "Go[n]di"(?). These are copy slips, kept as
  slips, not new key values.
- New sentences: "Je luy ay demandé come [...] le Pape voloit que j'y alase; elle m'a dit n'avoir autre charge, ne me
  declarans que j'y alle ou non"; "Je me suis content[é] de cela, et luy ay faict plainte ..."; "pour en parler";
  "Ce qu'il faict tenir segret, et le faire savoir a [Cardinal Gondi]".

Tried and failed:
- line 2 `7 69 2` after come: "comment" (92 46 49 49 79 57 12), "si le" (87 / 17 63 + 52̄), "ce que" (85̄ 11̄); none
  fits the figures even allowing 1/7 and 2/9 swaps.
- line 4 `27 9` after content and `58 76 12` after "m'est": "contenté" needs 79/69; "nuyt" (58 15 76 12) lacks the u;
  "n'y t[..]" gives no word.
- line 5 `43 45 8 13`: "alleguant" (40 15 34 58 13) needs 3 read as 0 plus a missing figure; "a l'entour", "aller
  tant" tried; marked [?alleguant] only.
- last line: `15̄ 18 12 63 26 57` "propos + stion"; "question" would need 19 15 79; `45 76 22 74 80 34 77` read "tout
  yra · a l": the line ends the letter before the subscription and no closing formula fits.
- `_check_reading.py` on the reading text alone: 3 of 10 sentences clean (0.30); by hand, 4 of 8 sentences read
  with at most one hole (lines 1, 2-3 first half, line 6, line 7).

## 3. Where it stops

The figures are legible on the image. The remaining breaks are in the copy itself: the register copyist dropped or
swapped figures (the same habits as in f. 209: 61 for 65, 11 for 15, 14 inside "de"), and with no second witness
(no decipherment, no original, no edition) a corrupt group cannot be restored except where the sense forces it.
State stays "decoded, not read": about half the sentences hold, holes in lines 4, 5 and the last line.
