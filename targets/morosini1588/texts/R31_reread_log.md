# Re-reading log, R31 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R31_decryption.txt` (DECODE D1695 under Meister no. 40) gave the topics
(Martinengo, Cardinal of Guise and Avignon, Florentine marriage, Gondi, Épernon, the fundamental law, the Parlement and
the legation faculties) with a garble in most lines.

## 1. Is there a text already?

- DECODE "cleartext" images D1035–D1036 (contact sheet): a clear letter page, not a decipherment. No interlinear glosses.
- Clear docket on 173r (as transcribed by DECODE): "Dal S.r Car. Mo[rosini] 23 d'Ottobre da Bles".
- Rome's decipherments (Francia 27) not imaged; Tempesti summarises the Gondi mission and the Saluzzo affair but not
  this letter's text.

## 2. Page order

The record is bound 172r–174v, but the letter begins on 173r (date docket) and 174v breaks off at "Ulise Martinengo
heretico" while 172r begins "[uenuto] a Lione per tratare con li Ugonotti"; 172v ends the cipher (DECODE's transcriber:
"end of cipher?"). Reading order: 173r–174v, 172r–v.

## 3. Hand re-parsing

About one word in seven re-parsed; nearly all carried by the transcribed figures (`R31_corrections.tsv`):
- Names the decoder missed: Hiero[n]imo Gondi, Momoransi, mons. di Mases, mons. di Santa Maria, mons. di Uins, la
  Ualeta, cardinale Santa Seuerina, Ulise Martinengo, Mandelot, Horatio Ruc[e]lai, "sua Alt." (2 27 8).
- The encipherer writes "int-" as 171 + 31 (nt): intentione, intendendo, intendeua.
- m + 8 for -mente (grandem., facilm., sicuram., diretam.); 8 after other abbreviations (Serenis., Alt., Ualeta).
- Spurious dots: 719 (= io), 252 (= in caso), the dot on 2 in "capitoli", on 5 in "ordine di".
- Image checks: 172r ll. 11–12 ("di 1 9 1": no 5 on the image, so the code for Avignon is miswritten or another
  place), 173r l. 9, 173v l. 9 (113 with its dot after "da").

## Result

Before: 0.617 clean-sentence share (`R31_decryption.txt`). After: 0.742 (1,044 words) on the "## Reading" body. By hand: 9 unread or code holes and 10
partly carried words in about 1,150 words; all sentences carried except the first few figures and the last line.

## Still open, and why

- The opening figures on 173r and the closing line on 172v; "considerando gli […]" (174r l. 14); "di questa […]"
  (174r l. 16); "[141]" (172v l. 4); one stretch before "esendo nato" (172v l. 2). The transcribed figures do not
  parse; most were not re-checked on the image (no outside blocker; left for a second image pass). Rome's
  decipherment (Francia 27) would settle them (physical access).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), looked at on the image (scratchpad `reread/r2p/crops`),
cancellation strokes looked for, parsed (`r2p_parseall.py`). As on R30, long diagonal strokes lie over runs of figures
(173r l. 17, 174r ll. 14-16, 172r l. 8, 174v l. 20); enlarged (174r l. 15) they are the verso showing through the
spread ink, not cancellations, but they make the runs hard to read.
Filled:
- 173v l. 12 "dar[?li] hora": "26 21 00 | 50 7? | 14 91 00 2": the figures give hora, not alhora; the li stands next to
  a figure obscured by show-through.
Left, with blockers:
- 173r l. 2 opening "9 9 1 2 1 2 5 2 7 7 9 165. 0 0 9 1 0 5 8": as transcribed, no parse. Blocker: no-key-material.
- 173r l. 9 "Hiero[n]imo": a blot where the n would stand. Blocker: illegible.
- 173r l. 17 "[?sia]" (4 17 171, in a stretch obscured by show-through), 174r ll. 14-15 "gli […] che" and l. 16 "questa […] il quale"
  (lines obscured by show-through). Blocker: illegible.
- 173v l. 6 "[?io]" (171), l. 9 "[de] come [?lei]" (26 35 | 79 | 50 5 171: lei is carried but the sense wants le).
  Blocker: no-key-material.
- 174v l. 1 "apost[olica]" (the abbreviation), l. 20 "[?deta]" ("2 6 3 5 3 5 2", in a line obscured by show-through). Blocker:
  no-key-material (l. 20: illegible).
- 172r l. 1 "[?uenuto]" ("3 7 1 1 9"), l. 4 "scriuer[e]", l. 8 "[?posa]" (70 91 54 5 = pose, figures obscured by show-through after it),
  l. 11 "[191 = Auignone?]" (dotted 191, not in the key), l. 20 "[con]" (a null 8), l. 21 "[che]" (a lone 1), l. 22
  "Ruc[e]lai" (00 37 25 25 at the line end). Blocker: no-key-material.
- 172v l. 1 "[il]" (nothing written), l. 2 "Loreno […]" ("8 0 3 5 1 7 9 7 5 0 7"), l. 4 "[141]" (clero, which does not
  fit), l. 7 "Alt[ezza]" (abbreviation), l. 8 "[?ui]" (173), ll. 9-10 the close (ended by a rule). Blocker:
  no-key-material.
Result: 1 hole partly filled; 25 left, each with its blocker.
