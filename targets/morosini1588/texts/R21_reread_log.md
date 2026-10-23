# Re-reading log, R21 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R21_decryption.txt` (character-model segmentation of DECODE D1689, KaJo,
March 2016) scored 0.684 clean.

## 1. Is there a text already?

- DECODE "cleartext" images D950–D953 (contact sheet; the dating lines cropped): the covering letter in clear, "Di Bles
  li X di Sett.re MDLXXXVIII", which gives date and place. Not a decipherment.
- Tempesti (1754) II, book VI §§ XXIII–XXVI (pp. 78–79) paraphrases this letter closely, in its order: the dismissal
  of Cheverny, Bellièvre, Villeroy, Pinart and Brulart; Guise and the Queen Mother's jealousy; the plan confided to the
  Queen Mother on leaving Chartres; the legate's audience; the King's answer ("imparar dal Papa a farmi ubbidire",
  "ormai ho trenta sett'anni", the Estates would have asked for their removal, "partiti"); the legate's plea to keep
  them in his devotion; Épernon, his physician, Boulogne and Metz, Montmorency and Navarre, "quattrocentomila scudi
  sopra il sale". It was used to recognise names and sense (Beleure, Feriero, Montmoransi, 37, 400 milia, partiti); no
  word was taken into the reading that the figures do not carry.
- Rome's decipherments: ASV Francia 27 (not imaged).

## 2. Hand re-parse

`R21_corrections.tsv` (33 rows). Main causes: dotted groups mis-grouped (161 for 116 Regina Madre, image-checked;
spurious dots 211, 971); codes without dots (129, 226); the decoder's vocabulary (priuandosi, nondimeno 77, dominati,
lodino, Sciartres, comonicò, risolutisimo, Montmoransi, Feriero, tratenirlo, quanto poso); numbers between null 8s
(37 ani; 400 milia). Image checks: 94r rows 13 and 20–22.

Aligner (`reread_b00_align.py R21`): fixed "che i[o]" (94v: only 7), "se così facese" (95v: one si), "Con tuto che"
(96r: the figures give 56, not ciò), moved the 96v page mark before "400". Left: "secretari" (215 secretario: the
aligner's list has only the singular), "città" and "indefesa[m]." (words split across a page break), one "io" next to
the spurious dotted 971. TOTAL after fixes in the report.

## Result

Before 0.684 -> after 0.702 (reading body; the clerk's spellings count as holes). By hand: 6 unread stretches […], about
10 partly carried or supplied words in ~1,050 words; every sentence of the audience carried. Grade A (sentences hold
throughout; Tempesti's paraphrase agrees with the reading point by point).

## Still open, and why

- Opening figures before N. S. (94r) and the closing (96v): no parse.
- "Et […] audientia" (94v), "dei […] paterni consigli", "in [?stato] […] migliore" (95v): short stretches.
- "[?tenir]" (96r): the group 1 6 3 5 0 1 1 7 0 0 recurs in R20 ("[?tenire]"); possibly a variant spelling of t.
- No outside blocker but Francia 27 (physical access).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located on its line (`research/reading_audit/r2p_holes.py`), looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for (none on these pages), figures parsed under Meister no. 40
(`r2p_parseall.py`).
Filled (every figure carries the word):
- 94r ll. 17-18 "minorità" (20 17 0 191 0|0 17 15 212: the t is the 15).
- 94v l. 7 "Et io andai a l'audientia" (171 9, 2 01 26 21 171, 2, 50).
- 95v ll. 14-15 "in stato migliore": the last figure of l. 14 is 4 on the image (DECODE 9): 17 10 4 | 15 21 51 9; the
  second "[…]" withdrawn.
- 96r l. 5 "tenir" (6 35 01 17 00, then 2 50 212 = a la); 96r l. 6 "ofenderli" (... 00 50 171 8).
- 96r l. 16 "per che si": "8 6 4 | 5 6 4 1 7 1" = per, che, si (was "per[ché] che si").
Left, with blockers:
- 94r l. 1 opening "1 7 1 5 9 2 7 2 2 3 4 5 2 9 9" before N. S.: as transcribed, no parse. Blocker: no-key-material.
- 94r l. 1 "dal[a]" (26 21 50, no a), 94r l. 22 "[?hebe]" (che + 4 2 5), 94v l. 13 "i[o]" (a lone 7), 96r l. 7 "[?esi]"
  (esa), 96v l. 7 "s[ia]" (4 17 171): as transcribed. Blocker: no-key-material.
- 95r l. 23 "indefesa[m]": "1 7 1 0 1 6 2" at the foot of the page. Blocker: no-key-material.
- 95v l. 3 "[che]": nothing written. 95v ll. 9-10 "[?partiti]": "1 | 2 1 0 0 1 5 1 7 1 5 1 7 1", no p. 95v ll. 11-12
  "[I]o lodai [?a]": "8 | 1 9 1 5 0 ..." (no 7 here). Blocker: no-key-material.
- 95v ll. 12-13 "dei […] paterni": "4 2 1 3 7 9 1 0 1 | 6 9" on the image, no parse. Blocker: no-key-material.
- 96v l. 13 closing after N. S. "8 4 7 2 2 4 4 7 7 9 2 1 1 1 2 0 2", ended by a rule: no parse. Blocker: no-key-material.
Result: 7 holes filled or withdrawn; 13 left, each with its blocker.
