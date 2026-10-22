# Method and checks

[日本語](METHOD.md)

## Steps
1. **Images**: Gallica, BnF fr. 15573 (ark:/12148/btv1b90618780), view 246 (f. 120r) and view 247 (f. 120v). The folio number "120" at the top right of the leaf (with another, older number to its left) confirmed that this is the right leaf. The view number is 2 off from the « p.248 » in Tomokiyo's list. The images are not included here.
2. **Deskewing and cutting**: we searched for the angle at which the horizontal projection of the lines is sharpest (`src/angle.py`) and corrected f. 120r by −1.2° and f. 120v by −2.4° (`src/deskew.py`). Giving the baseline positions of the lines, we cut the pages into tiles of two lines, left and right halves, and enlarged them (`src/tiles.py`).
3. **Transcription**: line by line, in the sign names of Brett Burford's reference sheet v3 (made from the Cipher-2 letters of the same volume, fr. 15573) (`data/transcription_*.txt`). Signs not on his sheet were given names of our own (`inferred` and `unknown` in `data/key.tsv`). The word-divider slash of the original is kept as `/`, interlinear additions as `^(…)` and struck-out signs as `{…}`; the last two are not used for decoding or scoring.
4. **Key**: `data/key.tsv` was built from Burford's `data/key-cipher2.json` (commit cc0daf74). His origins beginning with T (Tomokiyo's table) are `table`; E and F (alignments with contemporary decipherments) are `burford`. Values added from this letter are `inferred`. The evidence is in column 4 (Japanese) and column 5 (English).
5. **Decoding**: `src/decode.py` applies the key to the transcription (`data/decoded_*.txt`). The reading ([READING.en.md](READING.en.md)) is that output with word divisions and punctuation added.

## Figures (`src/decode.py`, `src/control.py`, run on 20 October 2026, after the revisions following the calibration, the second transcription and the three-reader vote)
### Share of signs with a value
| Page | Signs | Table signs only | Table + Burford's alignments | Also inferred |
|---|---|---|---|---|
| f. 120r | 885 | 787 (88.9%) | 856 (96.7%) | 874 (98.8%) |
| f. 120v | 218 | 186 (85.3%) | 213 (97.7%) | 214 (98.2%) |
| Total | 1,103 | 973 (88.2%) | 1,069 (96.9%) | 1,088 (98.6%) |

Signs with two values, such as f (`i|s`), are counted as having a value. In the first reading (commit 6982c5d) the totals were 970 (87.9%) / 1,064 (96.5%) / 1,082 (98.1%), after the revision following the calibration and the second transcription (441b3e9) 975 (88.4%) / 1,069 (96.9%) / 1,084 (98.3%) (two signs were removed in the revision after the three-reader vote, so the count went from 1,103 to 1,101). Before the three-loop sign was taken as ooo = escus (inferred), the total including inferred values was 1,082 (98.3%). Before the image check (Record of checks 3) the totals were 974 (88.5%) / 1,067 (96.9%) / 1,085 (98.5%) of 1,101 signs.

### Control with shuffled keys (both pages, 1,000 times each)
The same transcription was decoded with keys in which the values of the letter signs were swapped among themselves, and the French-likeness was compared with that of the real key. French-likeness is the mean log-likelihood of letter trigrams (built from the top 50,000 French words of `wordfreq`, with j→i and v→u). Word signs and signs with two values are not scored.

| Transcription | Condition | Signs scored | Real key | Shuffled keys (min / median / max) | Shuffled ≥ real |
|---|---|---|---|---|---|
| First (revised) | Table signs only | 750 | −2.720 | −5.595 / −4.829 / −3.890 | 0 / 1000 |
| First (revised) | Table + Burford | 832 | −2.750 | −5.645 / −4.974 / −4.136 | 0 / 1000 |
| First (revised) | Also inferred | 843 | −2.767 | −5.692 / −4.990 / −4.221 | 0 / 1000 |
| Independent second (Codex, fifth run; see "Independent second transcription") | Table signs only | 709 | −2.979 | −5.609 / −4.738 / −3.896 | 0 / 1000 |
| Independent second (Codex, fifth run) | Table + Burford | 846 | −2.878 | −5.721 / −4.982 / −4.199 | 0 / 1000 |
| Independent second (Codex, fifth run) | Also inferred | 851 | −2.873 | −5.763 / −4.970 / −4.082 | 0 / 1000 |

This shows only that the key's values produce text far closer to French than chance assignments do; it does not show that each sign is read correctly. In the first transcription some look-alike signs were chosen by context, which favours the real key. The second transcription (Sonnet) and the three-reader vote (Opus) were read by shape only and have no context bias. The vote's real-key score is about the same as that of the context-chosen first transcription.

### Values inferred in this letter
| Sign | Value | Times | Evidence |
|---|---|---|---|
| Lp (ℓ-shape) | i | 4 | n'y a (r c02), Guise (r c10), irai (r c24). The one place in r c04 was corrected to Lbar (p) in the image check (raportent) |
| curlo (stroke whose foot curls right) | o | 5 | auons (r c25), corps (r c27), offres (r c26), souffr- (r c03). Named curl in our first transcription |
| nous (gg struck through) | nous | 3 | que nous somes (r c12–13), mais nous somes (r c26), qui nous le (r c29) |
| 2c (2 with a swirl) | m | 1 | initial of a name (r c22, [M]ontablaye?) |
| hsb (ʃ with a bar and a dot) | nous | 2 | cent cinq mil escus ne [nous] sauroient relever (r c14), ce que l'on m'en dira. [Nous] avons de ce soir icy (r c24–25). The Opus vote also read r c14 as nous. The shape is close to Tomokiyo's nous but not confirmed to be the same |
| ooo (three loops in a row) | escus | 3 | trente mil [escus] en or (r c08), cinq mil [escus] pour venir icy (r c11), cent cinq mil [escus] ne … sauroient relever (r c14). At first given the same name as the two-loop sign (oo) in r c09; the image shows a different shape. Two independent readers also noted "three loops" |

### Values revised after the calibration and the second transcription
| Sign | Before | After | Reason |
|---|---|---|---|
| curl (large backslash with a small o; named bslash in our first transcription) | a (inferred) | pour | In the calibration on f. 104r the contemporary decipherment has pour in both places. It is the same sign as Burford's curl = pour (T+E-eye). In f. 120: pour venir icy (r c11), pour les [∞]voyer (r c09), pour [u] temps (v c03) |
| lambda (λ) | q | q or x | q in Tomokiyo's table; x in Burford's key (E) and in the calibration (where the decipherment has deux). In f. 120, q fits qu'une (r c09) and x fits d[i]x iours (r c22) |
| pdot (small loop half-way up a stroke) | unknown | puis | Re-examined because the second transcription read it as phi (en). Burford's sheet example of phi has two loops, a different form; we take it as the same form as Tomokiyo's puis (a stroke with a loop). je vous puis di[r]e que nous somes (r c12). The c (S) of dice may be a misread r (ls) |

Signs also named from Tomokiyo's table: dsi+ (ꝺ with a cross) = c, xd (u-shape with a dot) = x, w2 (ϖ with two humps) = il, 6b (б-shape) = f, R = h, yy = encore.

## Calibration (measured on a letter with a contemporary decipherment, 20 October 2026)
- Target: BnF fr. 15573 f. 104r (Mayenne to the King, September 1586, the same Cipher-2; Gallica ark:/12148/btv1b90618780, view 213). The contemporary decipherment is in the left margin and at the foot.
- Steps taken not to see the answer: done by a separate reader (Claude Opus 5.5) who had not seen the reading of f. 120, without opening the margin or a reduced image of the page. The amount of dark pixels per column and the line period (about 119 px for the marginal decipherment, about 150 px for the cipher) gave the border between margin and text (x ≈ 1,400 px). The left side of each line was blanked before deskewing (−1.6°), and only the text area was cut out and looked at.
  - At the left end of line 23 a faint grey trace (probably the edge of the marginal decipherment, about two letters) appeared. It was not read as a word. The left ends of lines 23–24 were then read on a binarised image that keeps only dark pixels (the grey writing does not show).
  - The only images opened were the top of the text area (folio number "104" and cipher lines 1–3) and the cuts of lines 18–24.
  - One note in `data/key.tsv` carries Burford's alignment mark « f. 104r l. 19 'menant' », which was seen before transcribing.
- Transcription: cipher lines 18–24 (181 signs), in the same sign names, read once by shape only (`calib/transcription_f104r_l18-24.txt`). Signs were not chosen by context. Three line-initial signs were cut off at the blanked border and could not be read.
- References (fetched after the transcription was finished):
  1. Characters: the part of the contemporary decipherment corresponding to these seven lines, « [empor]ter pour plusieurs … qu'il en fallu[st] » (`calib/ref_f104r_l18-24.txt`), copied from `data/known-text/f104r-decipherment.txt` in Burford's repository (commit cc0daf74, CC BY 4.0; according to his note, read by eye by Claude from the Gallica images). The calibration work did not check it on the image (that would have meant looking at the margin); it was checked later, as follows.
  2. Signs: his `data/known-text/ref-104r-l18-24.txt` (commit 22ab58c3, CC BY 4.0; checked against the contemporary decipherment). He counts lines from 0, so his lines 18–23 are lines 19–24 of this transcription (`calib/ref_signs_f104r_burford.txt`).
- The character reference was checked on the image (after the calibration transcription, in the work that read f. 120): compared with the left margin and foot of view 213, only his « qui reste icy » was changed to « qui restent icy » (on the image there are about four letters after res; the second may also be an o). The other words agree with the image.
- Results (`src/calib.py`):
  | Key | Character agreement (reference 248 characters) | Table signs only |
  |---|---|---|
  | Key at the time of the calibration (backslash sign = a) | 70.6% (edit distance 73) | 62.9% (edit distance 92) |
  | Key revised after the calibration (backslash sign = curl = pour; see "Kinds of difference") | 73.4% (edit distance 66) | 65.7% (edit distance 85) |

  The revised values were decided after seeing the answer (by following Burford's key), so the first row (70.6%) is the blind measurement; `src/calib.py --key-at-calibration` reproduces it. Before the reference was corrected on the image, the figure was 69.5% (62.6% with table signs only). Signs with two values (`a|n` etc.) count with their first value; signs with no value count as mismatches.
  - Sign agreement (lines 19–24, 137 reference signs):
    | Counting | Agreement |
    |---|---|
    | Strict (edit distance; line-initial signs missing from the reference count as errors; `src/calib.py --signs`) | 78.1% (edit distance 30; 77.4%, distance 31, before the renaming) |
    | As Burford counts: a match if equal to any of the reference's alternatives (a｜b); the 12 transcribed line-initial signs missing from the reference are not counted (`--lenient --no-alias`) | 86.9% (18 errors) |
    | As above, also counting different names with the same value (dots and :, ooC and phi) as matches (`--lenient`) | 89.1% (15 errors) |

    Burford's reader accuracy on the same lines of f. 104r was 91.1–93.5% for single passes and 92.9% for a vote of three passes (either name accepted for look-alikes; his README, "Measured numbers"). The details of the counting are not the same, so this is not a strict comparison.
    The remaining 15 errors: 2o read as "a 0" and "a" (two places), .24. read as "2 q+", # read as 4t (two places), w read as w2, z9 read as 9, rC read as Lp and :, unreadable (?) or extra signs, etc. Searching the transcription of f. 120 for these types: all five places of 4t are where the context requires e (prince, fasché, Guise, le mar[eschal], etc.), both places of w2 are il, and there is no "a 0" or "2 q+".
- Kinds of difference (classified by eye; one place may count more than once):
  - One sign read as two: 2o (qui) read as "a 0" and "a a" (twice); the number sign .24. (peu) read as "2 q+".
  - Look-alike signs confused: # (r) read as 4t (e) twice (« desgarnie », « resoluant »). The start of line 18 (« pour plu[sieurs] » in the decipherment) read as Gamma, 2u (vous de). The start of line 22 (« tout des[garnie] ») read as Qh, .12. (armée des). The humps of ϖ counted as two (w2) instead of three.
  - Different key values: the sign named bslash (backslash with o; now renamed curl) in this transcription is Burford's curl, and the contemporary decipherment has pour in both places (« emporter pour », « parle pour »). The key of this letter had inferred bslash = a, curl = o. λ stands where the decipherment has « deux », in line with Burford's x (dx = deux); the key of this letter had q.
  - Spelling differences between cipher and decipherment (not misreadings; Burford's sign reference has the same signs): faicts/faictz, principales, dificultes, restent, Guyenne, estans, campes, etc.
  - Place names (Xaintonge, Poitou): signs with no value in the key, or not read. Three line-initial signs cut off.
- Following the calibration, bslash in the key of f. 120 was renamed curl (pour), the former curl renamed curlo, and λ given q or x (see "Values revised"). The confusions of # and 4t, and of 2o and "a 0", were not re-examined in the transcription of f. 120.
- **Calibration by the same way of reading as the published transcription (20 October 2026)**: the calibration and the vote above read by shape only. The published transcription (`data/`) was written by one Opus reader decoding with the key while reading, choosing between look-alike signs by both the sentence and the shape. A blind Claude Opus reader was therefore asked to read the same seven lines in that way (`calib/transcription_f104r_l18-24_context.txt`). It was given the line cuts with the margin side blanked, the reference sheet, the sign names with shape descriptions, and a key of names and values only (no notes, evidence words or mention of f. 104r). It was told not to open the references, the full page or other transcriptions, and reported that it did not.
  | Counting | Result |
  |---|---|
  | Signs (as Burford counts, reference alternatives only) | **90.5%** (13 errors, 8 of them naming differences: 24 vs .24., : vs dots, ooC vs phi) |
  | Signs (also same-value names) | 95.6% |
  | Signs (strict) | 81.8% |
  | Letters (current key) | 79.4% (70.2% with table signs only) |

  Caveats: a single measurement. The key value curl = pour was learnt from these seven lines in the earlier calibration, so this reader may have had a slight advantage when choosing by context. Through a bug of ours, the row for the sign # (value r) was missing from the key list given to the reader (the reader wrote # by shape, so sign accuracy is not affected).
- Meaning: a transcription read once by shape, combined with the key, may contain about 30% character errors. In f. 120 signs were chosen by context, so fewer errors are expected, but this was not checked. This is of the same order as the calibration of matignon1586-public on f. 103v (74.8%).

## Record of checks 1: Claude Sonnet transcription (20 October 2026)
A key value of the first (pdot = puis) was revised after looking at differences with this transcription, so this comparison is not called independent. The independent second transcription is "Independent second transcription (Codex)" below.
- Another AI (Anthropic's Claude Sonnet) was given the same image tiles (two lines, left and right halves), Burford's reference sheet, and a list of sign names with descriptions of shape only (no values, plaintext or evidence words), and transcribed by shape only, without seeing the first transcription, the key, the decoded text or the notes (`second/transcription2_f120r.txt`, `f120v.txt`). Turning signs into plaintext was forbidden. Its list of names was the one before renaming, so for comparison bslash→curl and curl→curlo were applied (`second/transcription2_f120_all.txt`).
- The second reader's own report: only two places were enlarged; the rest was read on the tiles at their own size. About a fifth of the signs (226) were marked as uncertain.
- Comparison with the first (`src/compare2.py`; against the first transcription before the three-reader vote. Against the current first transcription (after the image check): recto 81.0% / 87.5%, verso 80.3% / 88.5%):
  | Page | Agreement of sign names | Agreement of values (different names with the same value count as agreeing) |
  |---|---|---|
  | f. 120r | 81.4% (887 signs, edit distance 165) | 87.7% (edit distance 109) |
  | f. 120v | 78.7% (216 signs, edit distance 46) | 87.0% (edit distance 28) |
- Most differences that change a value fall in three look-alike pairs: ls (r) and S (c), 24 places; r (e) and xbar (s), 18; 8s (m) and 8 (t), 8. In every case the first reading gives a French word (asseure, ordre, lettre, derniere, passé, trente, mil, mar[eschal], etc.). That means these were chosen by context, not decided by shape.
- The only revision prompted by the second reading is pdot (puis), one kind of sign in two places (see "Values revised"). The second reader also read the ⊏-shape as ⊣ (plus) (r c23), the first sign as tt (les) (r c01), and qx as r (v c02); all are left as candidates in [OPEN.en.md](OPEN.en.md).
- Decoded with the same key, the second transcription also gave 0 / 1000 in the control (table above).

## Record of checks 2: vote of three Claude Opus readers (20 October 2026)
The first transcription was corrected after looking at differences with the vote on the image, so its comparison with the first is not called independent (the accuracy on f. 104r is a blind measurement).
- Three blind Claude Opus readers read the same material separately: f. 104r lines 18–24 (the calibration lines; only the line cuts with the margin side blanked were given) and all 39 lines of f. 120. They were given the line images, Burford's reference sheet, and a list of sign names with shape descriptions only (no values, plaintext or evidence words). They were told not to open the first transcription, the key, the decoded text, the notes, the references or the full page of f. 104r, and all three reported that they did not. Turning signs into plaintext was forbidden. Readings: `third/*_pass1–3.txt`; vote: `src/vote.py` (on each line the reading closest to the others is the pivot, and the majority name is taken at each position) → `third/*_vote.txt`.
- Share of positions where all three gave the same name (relative to reader 1's signs): f. 104r 94.8% (164/173), f. 120r 89.3% (781/875), f. 120v 84.3% (182/216).
- **Accuracy on f. 104r lines 18–24** (137 reference signs; `src/calib.py`):
  | Reading | Signs (as Burford counts, reference alternatives only) | Signs (also same-value names) | Signs (strict) | Letters (key at the time of the calibration) |
  |---|---|---|---|---|
  | First calibration (a separate reader who had not seen the reading of f. 120, one pass) | 86.9% | 89.1% | 78.1% | 70.6% |
  | Reader 1 | 89.1% | 94.2% | 80.3% | 73.4% |
  | Reader 2 | 87.6% | 94.2% | 78.8% | 73.8% |
  | Reader 3 | 89.8% | 94.9% | 81.0% | 73.0% |
  | **Vote of the three** | **90.5%** | **95.6%** | 81.8% | 74.2% |

  Burford's figures on the same lines: 91.1–93.5% for single passes, 92.9% for a vote of three (either name accepted for look-alikes). Of the 13 errors left in the vote (reference alternatives only), 8 are differences of naming (the reference's 24 vs .24., : vs dots, ooC vs phi) and 5 are misreadings that change the value (z9→9, rC→Lp, w→w2, rC missing, x?|uC|y→9). Letter agreement is lower than sign accuracy because of code signs with no value (place names etc.) and spelling differences between cipher and decipherment (see "Calibration").
- **Comparison on f. 120**: agreement of values between the current first transcription (after the image check) and the vote is 93.1% recto (885 signs, edit distance 61) and 88.1% verso (218 signs, edit distance 26), higher than for the Sonnet transcription (87–88%).
- **Places corrected after the vote**: there were 23 places where all three readers agreed on a value different from the first transcription. Each was looked at on the image, and the following 7, confirmed on the image, were changed to the readers' reading (at first 9 were changed, including v c05 and v c07; on re-checking under the rule "correct only where the image confirms it", those two were returned to the first reading):
  | Where | First | Corrected | Reason |
  |---|---|---|---|
  | r c03 | x (u) | r (e) | on the image an x with a dot, the sheet's r. qu'il souffre ne soit a desseing |
  | r c04 | hs (r) | r (e) | on the image the sign after the box is the dotted r, not ʃ. les efects |
  | r c12 | S (c) | ls (r) | on the image a thin ʃ. je vous puis dire |
  | r c16 | H (l) | # (r) | on the image the bar runs beyond the uprights, as in #. de s[en] aler et partir |
  | r c17 | 4 (a) | removed | the 4 was counted twice in the overlap of the two tiles (one on the image). qu'il saura ce que |
  | r c19 | z9 (de) | removed | on the image there is only one sign (Ee) between 6 and 4 |
  | v c03 | ls (r) | S (c) | on the image a round S, unlike the ʃ before it |

  Sixteen were checked and not changed: x in v c07 (an x with a bar at its foot, no dot of r visible), ls in v c05 (a small 5-shape, neither S nor ls can be decided), curlo read as curl in two places (taken as caused by our shape descriptions; souffre and rapportent need o), w2 in r c20 (two humps on the image; il seroit), hb in r c15 (ʃ with a bar; tout resolu), dbar in r c09 (a separate sign from the 4 on the image), Tl in v c01 (plus de fondement), 6b in v c06 (faire), L and xbar in v c07–c08 (the signs are on the image), r in v c01 (pauureté), f in v c07 (efects), + in r c01 (a run of signs with no value), oo in v c08 (at the end).

- Why the vote was not made the main transcription: in many places the vote breaks words that read in the first transcription (« plus de dix iours » becomes « de di[?] iour[?] », « cardinal » becomes « mn…nal », the curlo of « auons » and « corps », etc.). So the first transcription remains the main one, and only the places where all three agreed against it were checked on the image and corrected.

## Record of checks 3: image check of the differences with Codex (20 October 2026)
- The 77 differences of value between the first transcription and Codex's independent reading (the third run in "Independent second transcription" below) were judged by shape by Codex and Claude Sonnet, from the straightened line images and the reference sheet only (`check/`). Where both models said the shape is Codex's and the difference is a misread shape, 9 places were corrected: Lp→Lbar in r c04 (raportent), 8→8s in r c24 (l'on m'en dira), 9→q+ in r c26, 8s→B in r c30, delta→curlo in r c31, q+ added at the start of v c02 and hs between r and f (estrangers), 8→8s in v c03, x→r in v c07 (efects). The value of qx was cleared.
- Ten places where both said Codex's shape were not changed: pairs where the value of the near name on the sheet does not fit the context (curlo/curl, 2/2u, 6b/B, 9/d; [OPEN.en.md](OPEN.en.md)). Places where the two models disagreed or one could not decide (28), or both said the first transcription's shape (30), were not changed. The list of decisions is `check/DECISIONS.md`.
- Because corrections were made from this check, the comparison with Codex's third run used here is not called independent. A new independent reading was taken after the corrections (see "Independent second transcription").

## Independent second transcription (OpenAI's Codex, 20 October 2026)
- Read by OpenAI's Codex CLI (codex-cli 0.163.0-alpha.10.2 bundled with the ChatGPT app, default model; no model name appears in the configuration or the run record). `codex exec --ephemeral -s read-only` was run from an empty folder, given only straightened line images (each line in left and right halves, 78 images), Burford's reference sheet and an English prompt (`codex/PROMPT.md`: sign names and shape descriptions only; no values, first reading, key or plaintext).
- **The run used for the judgement (fifth run, `codex/transcription_codex_*`)**: run after the first transcription had been corrected in "Record of checks 3" above, with each image passed with its own `-i`. The run record contains only the reply (apart from records of reconnecting), with no command execution or file reading.
- **Runs not used for the judgement**:
  - First run (`codex/run1_misaligned/`): some right halves were one line off; also the list of images was passed as a single string, so the images may not have been passed one by one.
  - Second run (`codex/run2_ls/`): straightened images, but passed as in the first run; the run record has a listing of the image folder (`ls`).
  - Third run (`codex/run3_before_check/`): images passed correctly one by one. The first transcription was corrected after checking the differences with this run on the image (Record of checks 3), so it is not used as an independent comparison.
  - Fourth run: stopped before replying because of the ChatGPT usage limit (no transcription).
- Agreement with the (revised) first transcription:
  | Run | Page | Sign names | Values (same-value names count as agreeing) |
  |---|---|---|---|
  | fifth (used) | f. 120r | 83.8% (885 signs, edit distance 143) | 92.2% (edit distance 69) |
  | fifth (used) | f. 120v | 82.1% (218 signs, edit distance 39) | 89.9% (edit distance 22) |
  | third (used for the check before correcting) | f. 120r | 86.8% (edit distance 117) | 94.2% (edit distance 51) |
  | third (used for the check before correcting) | f. 120v | 85.3% (edit distance 32) | 92.2% (edit distance 17) |

  The lower value of the fifth run (values, 89.9%) is used for the judgement. Agreement by name (83.8%, 82.1%) is lower than by value because of pairs whose near names on the sheet have the same value (: and dots, 4 and 2x, etc.) and pairs treated as a question of value (curlo/curl, 2/2u, etc.; [OPEN.en.md](OPEN.en.md)).
- The first transcription was not corrected from this comparison.
- Decoded with the same key, the Codex transcription also gave 0 / 1000 in the control (table above).

## Use of AI
- The image transcription, the inferred values, the decipherment, the scripts and the documents were made by Anthropic's Claude (Claude Code, model Claude Opus 5.5). A person (the repository's maintainer) chose the target, saved the images and decided to publish.
- The first transcription (`data/`) is one reading of each line by Claude Opus 5.5. Differences from the transcriptions used for checking (`second/` by Claude Sonnet, `third/` by three Claude Opus readers) were looked at on the image, and the seven places the image confirmed were corrected. After that, OpenAI's Codex made the independent second reading (`codex/`). No person checked the transcription. Agreement between AI readings is not a substitute for a human check.
- While transcribing, lines already written were read with the key. Some look-alike signs were chosen by context (e.g. the second sign of r c04 read as r rather than x, giving desseing; written `r?` in the transcription).

## Limits
- The calibration covers only seven lines of f. 104r. The measurement by the same way of reading as the published transcription was made once (sign accuracy 90.5%, letter agreement 79.4%). The first, shape-only calibration gave 70.6% letter agreement in the blind measurement (62.9% with table signs only). In the work that read f. 120, part of the contemporary decipherment came into view when a reduced image of f. 103v was opened while preparing, so the calibration was done in a separate reader who had seen neither the margin nor the reading of f. 120.
- Look-alike signs (r and x, 8 and 8s, S and ls and hs, f and f2, th and 4t, # and 4t and tt, 2o and "a 0") are easily confused. In the calibration, # / 4t and 2o were actually confused. The choices made by context favour the real key in the control.
- Most inferred values are checked in only one to five places in this letter.
- Signs with no value and unread stretches are in [OPEN.en.md](OPEN.en.md).
