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

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located on its line (`research/reading_audit/r2p_holes.py`), the line looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for (none inside a hole; one overwritten figure on 88v l. 9), figures
parsed under Meister no. 40 (`r2p_parseall.py`).
Filled (every figure carries the word):
- "Io" five times (88v l. 8, 89r l. 11, 89v l. 21, 87v l. 4, 87v l. 12): "8 7 1 9 1" on the image, a single null 8 + io.
- 89r l. 4 "il Nauarro. A che io disi": "8 2 5 6 7 1 9 1" = (null 8) a, che, io (was "[?che non]. [I]o disi").
- 88r l. 10 "tenire" (6 35 01 17 00 5); 88r l. 15 the "[…]" between "o" and "uerificarle" withdrawn (173 = u, nothing
  left over); 88v l. 14 "nouam." (0 91 37 21 20 8: the -mente abbreviation of nouamente, no u missing); 88v l. 16 the
  "[…]" after "Suisone" held only a null 8: withdrawn; 89r l. 16 "si" (111. 4 171).
- 87r l. 13 "daria" (26 2 1 171 2); 87r l. 23 "editi" (35 26 17 15 171 after suoi 4 37 91 171).
- 87v ll. 1-2 "aperteneua" (2 64 51 | 35 01 35 37 2; the first figure of l. 2 is 3 or 7 on the image).
- 87v l. 4 "se": the image has "5 6 4 1 5 3" (DECODE "4 1 3 3"); 87v l. 11 "temese" (8 6 35 20 35 45 153).
- 87v ll. 17-18 "ma che S. M.tà doueua anco": "5 6 1 1 3 | 2 6 9 1 3 7 3 5 3 7 2": 113 (no dot seen) + doueua.
Left, with blockers:
- 88r l. 2 opening "5 0 9 1 5 7 2 1 2 0 7 1 111. 2" and 88r ll. 2-3 "8 3 3 5 0 1 5" before "a ritrouarmi": as transcribed,
  no parse. Blocker: no-key-material.
- 88r l. 12 "[?lo]" (50, l), 88r l. 15 "[l']" (nothing written), 88r l. 20 "Di[se]" (8 26 7 = di): as transcribed.
  Blocker: no-key-material.
- 88v l. 9 "[?come]": "7 6 9" with the 6 overwritten in darker ink. Blocker: illegible.
- 88v l. 13 "esortandoli […]": "716. 4 1 9" (no dot seen) no parse. 88v l. 19 "[?la]" (21) and "[?per]" (4). Blocker:
  no-key-material.
- 89r l. 10 "premese […] la": a lone 6 (darker). Blocker: too-short.
- 89r l. 22 "[112] [?da]": "1 1 1 2 6 2 1" on the image; neither 112 (l'imperatore) nor 111 + letters fits. Blocker:
  no-key-material.
- 89v l. 1 "proc[u]rate": a hole in the paper after "3 3 9? 7? 2 1". Blocker: illegible.
- 89v l. 13 "lo tratener […] nostra": "1 7 2 9 2 161. 7 0 1 7 1 7 3 7" (... quanto più ...), no sentence. Blocker:
  no-key-material.
- 90r l. 6 the close "8 4 7 2 7 2 9 1 7 1 2 7 9", ended by a rule: no parse. Blocker: no-key-material.
- 87r l. 1 "[…] che io": nothing written before; the second sheet starts mid-text (the join 90r -> 87r is missing).
  87v l. 23 "si diceua […]": the page ends there. Blocker: needs-physical-access.
- 87r l. 23 "er[a]": the a is not written at the page turn. Blocker: no-key-material.
Result: 20 holes filled or withdrawn; 18 left, each with its blocker.
