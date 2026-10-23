# R1054 reread log (r2q, 23 Oct 2026, Claude Opus 5.5)

**Before.** `R1054.md`, keyed decode with codes and brace-inferred syllables: translation wave v7 scored 0.54 on explicit
holes; set to decoded, not read. Measured again here on its reading body (v5a_body.py): plain 0.607 (17/28), explicit
0.643 (18/28), hole rate 0.097.

**Register copy.** Fagel register, NA 1.10.29 inv. 5186 scans 248R-249L, margin "Dat: 19. Juïllet 1757. A: à B:".
Scans fetched through the NA IIIF server (`research/reading_audit/b32_na_iiif.py`, 2400 px) and WAINUT's Gemini
transcription (`wainut/register_clear.txt`) checked line by line on both pages: it agrees with the scans word for word
(only capitals differ, which the reading does not use). Text joined with `v5a_affry_reg.py 5186 248R 249L`.

**Alignment.** `wainut/align/R1054.tsv`: 319/364 keyed groups at the register's word (0.876; shuffled 0.144). Every
disagreement looked at, with the cipher image I5511 (main checkout `img/`, rotated, rows 2, 4, 6, 13, 20, 21, 27
cropped):

| groups | key gives | register | decision |
|---|---|---|---|
| 38-42 | cu ses parti france que | tous les Partisans | parse error: the image has 851 . 831 (a 6 above the 8), not 86 31; 851 831 = parti-sans (as at 304-305); 750 at the line end is cut by the wrinkled margin. Register |
| 17-20 | c est un [101] | c'est | 1045 101 stand on the image; 101 has no value anywhere (3 occurrences, none aligned). The register passes over them; left out of the reading |
| 70 | en [760] usage | en usage | 760 on the image; value "leur" never confirmed (2 occurrences, no register word). Left out |
| 80-81 | d [6] [900] sent | D'autres disent | 6 is the last group of row 6 at the wrinkled margin, 6 = ma at 31 other places: a cut group. Register |
| 162-168 | envoye des ordres sur le char [338] p | envoyer ordre de demander sur le Champ | 992 is r/er in practice (er, ur, ter in other letters); 1136 338 371 = cha-m-p. The figures have no group for "de demander", which the register and Bussemaker no. 75 both have; the register's words stand (omission in the encipherment or the decipherer's addition; no figure gives another word) |
| 255-258 | m en rai maréchal | au Cte. | parse error: the image has 196 . 878 (a digit above the last 8) . 185 = M. le maréchal. **Figures followed**: "à M. le Maréchal d'Estreés" |
| 271 | sa | la | **Figures followed**: "de sa communication"; "du" has no group, kept from the register |
| 362 | v | empéche | 479 stands at "empecher" in R1067 too: the key value v is wrong. Register |
| 370-371 | par le | je le voudrois | 306 = par at 34 other places. **Figures followed**: "que par le [...]"; the page and the record end here |
| others | spelling, abbreviation (roi/Roy, s.a.r., quequ/que, aucune/aucun, sent/sens) | | register |

**Reading.** `R1054_reading.md`: the register text of the cipher page (to "que par le"), clerk's spelling, with the three
figure readings above; the rest of the register entry is printed below the reading as not on this record. Scores
(v2_score.py, French): plain 1.0 (22/22), explicit 1.0 (22/22), hole rate 0.003 (the closing [...]). No look-alike
alternates: the words rest on the register, the figures checked where they differ.

**Open.** The groups 101 and 760 (no value; the contemporary decipherer read no word for them); the second page of the
letter, which is not on the DECODE record (register only). English: `R1054_en.md`.
