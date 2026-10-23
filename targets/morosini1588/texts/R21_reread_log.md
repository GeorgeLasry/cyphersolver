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
