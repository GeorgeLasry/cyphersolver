# Re-reading log, R20 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R20_decryption.txt` (character-model segmentation of DECODE D1688, EH,
Feb 2016, speech recognition) scored 0.626 clean.

## 1. Is there a text already?

- DECODE "cleartext" images D968–D971 (contact sheet): the covering letter in clear plus an address leaf; not a
  decipherment. No interlinear glosses on the cipher pages.
- Tempesti (1754) II, book VI §§ XXVII–XXIX (pp. 79–80) paraphrases this letter: the Parisians' petition to the
  Parlement, Guise's gentleman sent to the legate at Blois, then the legate's audience (the King: the decree frees the
  Count "dalle pene temporali … in vigore de' nostri editti"; the legate: "più cura del suo particolar servitio che di
  compiacere altri"). It confirms the page order (88r–90r, then 87r–v), the place (Blois) and the sense of "[?editi]";
  no word was taken from it.
- Rome's decipherments: ASV Francia 27 (not imaged; physical access).

## 2. Transcription layout and page order

- D1688 writes each page as one run of figures with the next page header embedded ("#IMAGE NAME: 087v.jpg" inside the
  line), so the decode's line numbers are cuts by length, not manuscript lines; crops were placed by the image's own
  row grid (`reread_b00_crop.py --rows` agrees on 23 rows a page).
- Page order by sense and by the sheets themselves: 88r carries the clear heading "9. di Settembre" and a start cross;
  89v "fermata la boca a tuti" runs into 90r "per la corte"; 90r is a six-line closing page. 87r–v (bound first, marked
  "2" at its head) opens and ends in mid-sentence and continues the story (Vendôme's anger, the audience with the King),
  so it is read last. The join 90r → 87r does not parse; a leaf may be missing.

## 3. Word decode and hand re-parse

`R20_corrections.tsv` (48 rows). Main causes:
- Spurious nomenclator dots: 179 (dominio), 694 (et buona), 191 (intorno), 153 (se non), 714 (gli haueuo), 261 (di
  impedirli), 224 (asai), 150 (asolutione), 945 (conseruare).
- 111 = N. S. mis-grouped: 89r the image shows "1 1 1" dotted, then "4 1 7 1" (si); DECODE's grouping gave 114 (Re di
  Spagna). 87v "115" read the same way (figures+context). 89r "112" (l'imperatore) left as a code.
- Vocabulary/segmentation: esciuino, io esortauo, facilm. tornariano, da le pene temporali, che bene le doleua asai, non
  apperteneua, perché questo non pasase in esempio, il migliore rimedio che si poteua, comprobò, intrinsicam., alhora
  presentare, al parlamento (not "a limpedimento"), intacaua.
- Image checks: 89r rows 15–18 (the 111 grouping), 87r rows 9–12 (the doubled line is on the manuscript: the encipherer
  wrote "di stimare asai il mio consiglio tutauia" twice), 88r and 87r heads (heading, cross, the "2" on 87r).
- Aligner (`reread_b00_align.py R20`): "il già re di Nauarra" (232) is five words, past the aligner's four-word code
  expansion: rendered "il re di Nauarra"; "ugonoti" respelled as the code's "ugonotti"; "l[o]" made [?lo]; Ill.ma made
  Il[l].ma (one l in the figures). Left: "catolica/catolico" (226 catolici, the aligner's word list has only the plural),
  "si" after N. S. (the image shows 4 1 7 1; the aligner counts the DECODE grouping), "era" (its a is the first figure
  of 87v). TOTAL after fixes in the report.

## Result

Before 0.626 -> after 0.69 (reading body). By hand: 12 unread stretches […], one code [112], about 12 partly carried or
supplied words in ~1,240 words. Grade B (several figure+context corrections; page order inferred; the start of 88r and
the joins open).

## Still open, and why

- 88r opening (before "qui domenica") and "[…] a ritrouarmi"; 89v "che lo tratener […] nostra"; 87v "ma che […]ueua";
  the closing of 90r and the end of 87v; the link between 90r and 87r. No outside blocker except the decipherment in
  Francia 27 (physical access); a further image pass could test the figures of these stretches.
- The lone "o" (191/91) where the sentence wants "Io" (six places), as in R19.
