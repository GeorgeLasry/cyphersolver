# Re-reading log, R75 and R84 (22-23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b18)

## Starting point

Reading audit (22 Oct): both "decoded, not read". The second-pass decodes (`r75.read2.txt`, `r84.read2.txt`, Lasry's
key + 23 element values) were unspaced with an open element in nearly every line; `_check_reading.py` 0.00 clean
sentences on both. The 1632 interlinear on R75 (`r75.interlinear.txt`) covers lines 12-35 and is partly illegible.

## 1. Is there a text already? Yes: two complete contemporary decipherments

- Every file on DECODE R74-R84 fetched with the project cookie (`research/reading_audit/b18_ceva_fetch.py`, scratchpad
  only): 20 page images and **39 png attachments that no earlier session had opened** (`decode/` held only the DOC_*.txt
  files).
- **R75**: DOC_R75_D1143 (docket "1632 ... 25 sett."), D1144 (the clear covering letter, f. 80r), **D1145 = f. 82r,
  labelled "082r.jpg [cleartext]": a complete decipherment of the cipher** ("Le vittorie di Schombergh et della forza
  renderanno per aventura più facile ..."), D1146 (f. 82v, blank but for show-through).
- **R84**: DOC_R84_D1176 (a clear covering letter, Rome 11 Dec 1632: "Scrivo a Mons. Bichi una cifra con ordine che
  trovandosi lei alla Corte serva per V.S."; the victory "degl'Imperiali con la morte di Gostavo"), **D1177 = f. 136r: a
  complete decipherment** ("ricordando a V.S. che si vaglia della vittoria contro Gostavo ...").
- The other records' pngs (R74, R76, R78-R83) are the same kind of material for Lasry's letters; not needed here.
- Transcribed from native-resolution strips (`b18_ceva_crop.py`): `R75_decifrato_f82r.txt`, `R84_decifrato_f136r.txt`.
- Print not searched further: with complete contemporary decipherments the Nuntiaturberichte question no longer
  decides the reading (recorded as not done in Escalation).

## 2. Alignment and key

`b18_ceva_align.py` aligns the decoded units with the decipherment's letters by dynamic programming over the whole
letter and lists every disagreement per manuscript line. Findings, each adopted only where it holds at every
occurrence:

| value | evidence |
|---|---|
| 88 = del (keyed "quel") | R75 "della forza", "dell'accomodamento", "quello dell'unione", "della quale", "del Regno" x2, "dello Sueco"; R84 "della potenza", "del Regno" x2, "del negotio"; Lasry's 28 contexts read as well or better ("la pietà ~", "a danno ~ Francia", "~ fratello") |
| 33 = gli (a "dead" pair) | R75 "per ~ interessi", "compor ~ esterni", "chi ~ li sugerisca", "contro ~ infedeli", "ne ~ affari"; Lasry 346/5 "lege a ~ altri" |
| 541 = armi | R75 x3 ("l'unir le ~", "le medesime ~", "l'~ di Francia"); parsed io<128>, io{1} before |
| 171 = Regno | R75 x2, R84 x2 ("del Regno"); parsed i<129>, i<124>, i{1} before; 129 dropped |
| 473 = mentre | R75 x2 ("sotoposto ~ hano", "Però ~ vi è tema") |
| 497 = tutt- | R75 "da tutti", R84 "tutto quello"; Lasry "abbino a ridurre ~ le difficoltà" |
| 491 = quell- | R75 "quello dell'unione", "di quello che sia stato"; R84 "tutto quello che"; Lasry "a ~ unione", "in ~ piazza" |
| 104 = Olandesi | f. 82r "gli Olandesi", interlinear "Oland.si"; the second pass's "Svedesi" (from a blotted "...desi") withdrawn |

Read off the decipherments and consistent where met again (used in the readings, not added to the decoder): 153 = pace
(R75 x2 as `15 3 20`, `o 3`; R84 `o 3`), 451 = fatto (Lasry "ha ~ con S.E."), 471 = molto (Lasry "si sta ~ fiso"),
485 = perche, 110 = Principe/i (R84 x2), 998 + 3 = nella (R84 x3); one-off names: 357 Schomberg, 581 Card. Richelieu,
197 Religione Cattolica, 844 Gostavo, 309/107 S.M.tà, 930/957 Mons.r Nuntio.

Failures: 491 at R75 l.16 is "Goto" in the interlinear and "Gostavo lo Svedese quella natione" in f. 82r; not adopted
(quell- at nine other places; "di quella natione" reads). 494 ("se ne serva ~ li stimi"): f. 82r paraphrases; open.

`b18_ceva_redecode.py` decodes both letters again with the adopted values (in memory; cipher.py untouched):
`r75.read3.txt`, `r84.read3.txt`. The decoder now parses armi x3, Regno x4, mentre x2, gli x5 by itself.

## 3. Readings

Written on the figures, the decipherments carrying the code words; where the decipherer improved or glossed, the
figures are followed (R75: "a V.S. il negotio", "che ancora a detto", "Si asicura", "che S.E. cominci a conoscere
quanto sia", "di quella natione", "estendere", "del Sueco", "quanto alla Germania", "le cose con Monsieur", "contro gli
infedeli", "presente"; R84: "Vega V.S.", "gelosie", "vol", "tengano"). Two labels corrected on the image
(`R75_corrections.tsv`, `R75_transcription_corrected.txt`): l.3 01 (m) for 00 ("motivi"), l.21 94 (se) for 97 ("cose").
Clerk's slips left in the figures: 85 for v ("salvar"), 51/80 for g ("grado", "gloria"), 70 for t ("ritrovar"), R84 78
for r ("l'altro").

Word check (`b18_ceva_check.py`): R75 392 words, 0.92 found in the decode, 0.96 in f. 82r, two carried in part
("d'augumentarla", "ritrovar" from the interlinear); R84 275 words, 0.87 / 0.98, none uncarried.

## Result

| record | before (audit) | after: clean-sentence share of the reading body (`b18_ceva_score.py`) | rests on |
|---|---|---|---|
| R75 | 0.00, decoded, not read | 0.774 (24/31), 3 holes | f. 82r decipherment + figures under Lasry's key, 2 labels corrected |
| R84 | 0.00, decoded, not read | 0.826 (19/23), 1 uncertain word | f. 136r decipherment + figures under Lasry's key |

Content corrected by the decipherments: R75's victories are Schomberg's (Castelnaudary, 1 Sept 1632), not the
Swede's; the power reaching for great things is the Dutch; R84 is about Gustavus (the victory over him), the Valtellina
peace and Monsieur's flight.

Open: R75 "li stimi […]", "[…]" at the head of l.21, "la […] loro" (no key value, the decipherment paraphrases or is
unclear: no-key-material); R84 "da [?N.S.re]" (illegible in both witnesses).
