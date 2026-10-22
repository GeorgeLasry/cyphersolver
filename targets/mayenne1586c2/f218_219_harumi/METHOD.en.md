# Method and checks

[日本語](METHOD.md)

## Steps
1. **Images**: Gallica, BnF fr. 15572 (ark:/12148/btv1b9061879d), view 225 (f. 218r) and view 226 (ff. 218v–219r). Each page was deskewed (f. 218r −3.5°, f. 218v −0.7°, f. 219r −2.6°) and every line cut into three enlarged pieces. The images are not in this repository.
2. **Transcription**: each sign was given a name (`data/key.tsv`, column 1) and each line written as a row of sign names (`data/transcription_*.txt`). The vertical strokes of the manuscript (word dividers) are kept as `|`. A sign whose shape is uncertain carries `?`.
3. **Key**: Satoshi Tomokiyo's reconstruction (Cryptiana) of Mayenne–Forget's Cipher-2. Signs not in his table were given values that fit several words within this letter; they are marked `inferred`. The words they were checked on are in column 4 of `data/key.tsv`.
4. **Decoding**: `src/decode.py` applies the key to the transcription (`data/decoded_*.txt`). The reading ([READING.en.md](READING.en.md)) is that output with word division and punctuation added.

## Figures (`src/decode.py`, `src/control.py`, run on 20 Oct 2026)
### Share of signs given a value
| page | signs | valued by Tomokiyo's table alone | valued with inferred values |
|---|---|---|---|
| f. 218r | 713 | 657 (92.1%) | 704 (98.7%) |
| f. 218v | 926 | 836 (90.3%) | 921 (99.5%) |
| f. 219r | 498 | 446 (89.6%) | 485 (97.4%) |

### Shuffled-key controls (1,000 each)
The same transcription was decoded with keys in which the values of the letter signs were permuted, and its "Frenchness" compared with that of the real key. Frenchness is the mean log-likelihood of letter trigrams (built from the top 50,000 French words of `wordfreq`, with j→i and v→u). Code signs are left out of the score.

| page | condition | real key | shuffled keys (min / median / max) | shuffled ≥ real |
|---|---|---|---|---|
| f. 218r | with inferred values | −2.352 | −5.665 / −5.072 / −4.139 | 0 / 1000 |
| f. 218r | table signs only | −2.363 | −5.580 / −4.879 / −4.180 | 0 / 1000 |
| f. 218v | with inferred values | −2.597 | −5.608 / −5.041 / −4.485 | 0 / 1000 |
| f. 218v | table signs only | −2.630 | −5.685 / −4.851 / −4.121 | 0 / 1000 |
| f. 219r | with inferred values | −2.431 | −5.689 / −5.065 / −4.300 | 0 / 1000 |
| f. 219r | table signs only | −2.389 | −5.604 / −4.911 / −4.145 | 0 / 1000 |

This shows only that the table's values give text far closer to French than chance assignments do. It does not show that any single sign is read right.

### Inferred values that agree with another study's key
The values inferred here were compared with the key Brett Burford built for another Cipher-2 letter, fr. 15573 f. 385, against decipherments of the time (`data/key-cipher2.json` in BravoBravoIX/mayenne-forget-1586-cipher-reading, version of 19 Oct 2026). Sign names differ between the two studies, so signs were matched by shape.

| inferred here | Burford's key | when the value was found here |
|---|---|---|
| 17 = tant | 17 = tant (F) | before seeing his key (f. 218r) |
| underlined gg = par | gg = par (T?) | before seeing his key (f. 218r) |
| barred x = s | xbar = s / ss (T+E) | s before; ss (necessaire) after |
| 13 = tre | 13 = tre (F?) | after |
| ϕ = en | phi = en (T+E) | after |
| barred h (Qh) = armée | Qh = armee (F) | after (checked on « ladicte armée au partir de ce siege ») |
| ɞ with a stroke (curl) = pour | curl = pour (T+E-eye) | after |
| long rectangle (rect) = icy | rect = icy (E-eye?) | after |
| N-shape = ée | N = ee (F) | after |
| ꝶ-shape (zk) = p | zk = p (E-eye) | after |

ff. 218v and 219r were transcribed after seeing Burford's key. The "after" values were checked to fit their contexts in this letter, but they were not found independently.

## Calibration (a letter with a decipherment of the time, 20 Oct 2026)
- Letter: BnF fr. 15573 f. 103v (Mayenne to the King, September 1586, same Cipher-2; Gallica ark:/12148/btv1b90618780, view 212). Its left margin carries the decipherment made at the time.
- Procedure: cipher lines 1–6 (157 signs) were transcribed with the same sign names and the same key **before** the decipherment was looked at (`calib/transcription_f103v_l1-6.txt`). Fragments of the margin decipherment show at the left edge of the line cuts; they were not read. The decode was then compared letter by letter (`src/calib.py`) with the decipherment of the time: Brett Burford's eye reading, checked on view 212, with one abbreviation corrected (« lad[icte] riviere ») (`calib/ref_f103v_l1-6.txt`).
- Result: against 214 reference letters, edit distance 54 (21 substitutions, 24 letters missing, 9 extra). **Letter agreement 74.8%** (71.0% with the table alone).
- What the differences are (sorted by eye):
  - code signs with no value in the key, for a place name and a long word: Dordoigne, extremement (its "extreme"). Most of the missing letters are these;
  - confusions of similar signs: ϖ with two humps (il) and three (est); # and barred tt (les); round ℒ (n);
  - key values that do not fit here: χ° stands where the decipherment has « pour » (q in the key); the barred h stands where it has « tous » (armée in the key);
  - the first three signs misread (Nous).
- Following this, the sign written as il in f. 218r lines 9–10 was corrected to tt (les): « pour veoir les ennemis », « de les empescher ». The key was not tuned on the six calibration lines.
- Meaning: the reading, transcription and key together, may be wrong in about one letter in four. In this letter, values of ambiguous signs were chosen by context, so errors are expected to be fewer than in the six calibration lines (read without context). That has not been checked.

## Second transcription (Codex, 20 Oct 2026)
To compare with the first transcription (Claude), OpenAI's Codex CLI (codex-cli 0.163.0-alpha.10.2, bundled with the ChatGPT app; default model, whose name does not appear in the run log) transcribed the line images into sign names without seeing the first transcription, the key or any values. It was run four times. In every run, each page was a separate `codex exec --ephemeral -s read-only` call with the prompt on standard input. Names that reveal a value (=que, =pour, par2 …) were replaced by neutral names such as W01–W18 (`second/names_map.tsv`). The line images were cut by `second/crop_lines.py` from the same deskewed images as the first pass, each line into a left and a right half (f. 218r 27 lines, f. 218v 34, f. 219r 19).

| run | folder | input | run log | status |
|---|---|---|---|---|
| v1 | `second/v1/` | prompt (sign names and shape descriptions only) | no shell commands; but see "Image-passing fault" below | used in the review, so a cross-check record (not called independent) |
| v2 | `second/v2/` | prompt + sign specimen sheet (below) | ran `ls ../img` and `rg --files ../img` (file names of the line images) | used in the review, so a cross-check record |
| v3 | `second/v3/` | as v2; after the review, in a fresh context | on all three pages, ran `ls` of its input folder (which held only the line images, the specimen sheet and the prompt; the working-folder path in the log is replaced by `<scratch>`) | independent second transcription |
| v4 | `second/v4/` | v3's prompt plus "do not run commands or open files"; after the review, in a fresh context | no commands and no file reads (one reply per page) | independent second transcription |

- **Sign specimen sheet** (v2–v4): the shapes of 65 signs cut one by one from the image of Tomokiyo's Cipher-2 table (see "It rests on" in the README), labelled with our sign names and rearranged. No value cells, and the order is unrelated to the table's columns (values). Signs not in the table are described in words only. The sheet image is not in this repository (no images in the repository). Prompts: `second/v3/PROMPT.md`, `second/v4/PROMPT.md`.
- **Image-passing fault**: in v1–v3 the `-i` arguments meant to pass the line images reached Codex as one long string (the shell, zsh, did not split it), which Codex saw as "file name too long". This came to light in v4, where Codex, told not to open files, replied that it could not see the images. In v1–v3 Codex apparently opened the images itself from the paths in the error. Opening images is not recorded in the run log, and Codex's own log (~/.codex/logs_2.sqlite) has no rows for these runs, so what it opened cannot be checked. No answer (first transcription, key) was within reach of what it listed (v2's `../img` held only line images; v3's input folder only line images, the specimen sheet and the prompt). For v4 the arguments were passed one image at a time; that the images of all three pages arrived (55, 69 and 39 including the sheet) is shown by the replies transcribing every line.
- The previous version of this METHOD (commits 044cf00–8e3a50b of 20 Oct 2026) said of v1 that "only the line images and the prompt" were given and that there were "no commands and no file reads". Because of the fault above, the first statement was not accurate.

### Review on the images (ff. 218v and 219r, 20 Oct 2026)
With v1, the value agreement on ff. 218v and 219r fell below 70% (the level required to present a partial reading; see "Assessment" below). The disagreements with v1 (193 places after relabelling; `second/v1/diff_after_relabel.tsv` refers to the transcription before the review), plus 4 places outside that list noticed alongside the v1 and v2 readings — 197 in all — were rechecked one by one on the line images, with the v2 readings alongside. A sign was corrected only where the image confirmed it.

- **Corrected: 19 places** (f. 218v 14, f. 219r 5). Main ones: x→r before a divider (f. 218v line 1); a barred x from * or x to xs (3); a long f without a bar from f to fi (2); a θ-shape from a to th (f. 218v line 22); the χ with a small o from =pour to xo (6); a missing r added in f. 219r line 13; in f. 219r line 18, where the image has a single sign, "r5 | s zk" to "zk?".
- **Not changed: 178 places**, where the image agrees with the first reading or the two shapes could not be told apart (4H, # and 4; fn and y2; 2 and J …). The change 4H?→# in f. 219r line 16 was first made and then undone, to match the other 4H/# places that were not told apart.
- List (place, first, v1, decision, reason): `second/review_f218v_f219r.tsv`. f. 218r was not reviewed.
- The six places changed to xo (χ°) take the value q in the key. In context each fits pour, and the same shape stands at a « pour » in the calibration lines ([OPEN.en.md](OPEN.en.md)). The reading ([READING.en.md](READING.en.md)) keeps pour.
- The review above was done by a single reader, the same one (Claude) that made the first transcription. The 19 corrections were therefore rechecked by two other models, OpenAI Codex (codex-cli 0.163.0-alpha.10.2, default model) and Claude Sonnet. Each was given only the line images, the specimen sheet and the two readings (before and after the correction, in random order as A/B), no values, key or reading. Both chose the corrected reading at 8 places; they disagreed, or one could not tell, at 11; both chose the earlier reading at none (`second/recheck_f218v_f219r.tsv`). As no place had both choosing the earlier reading, none of the 19 corrections was undone. Six of the 11 split places are the χ° sign (=pour or xo): Codex chose the earlier reading, Sonnet the corrected one.
- Caution: the same kind of check (correct only where both models agree) was tried on five pages of fr. 15573 that have a decipherment of the time, on 297 disagreements between the first reading and Codex's. Of the 38 places both models agreed to change, 9 came to agree better with the decipherment and 21 worse. Agreement of two models is weak evidence; these 19 corrections are to be taken as uncertain too.

### Comparison with the first pass (`src/compare2.py`)
Edit distance between the sign sequences of each page, divided by the number of signs in the first pass (dividers `|` left out). "Value" counts aliases with the same value in the key as equal. "Relabelled" renames each second-pass name to the first-pass name it was most often aligned with (fitted to the same data, so it runs high; not used for the assessment). Figures are against the current transcription, after the review.

| run | f. 218r name / value | f. 218v name / value | f. 219r name / value |
|---|---|---|---|
| v1 (record) | 76.7% / 77.4% | 64.3% / 66.3% | 62.4% / 64.7% |
| v2 (record) | 74.3% / 75.5% | 83.4% / 85.9% | 81.9% / 84.7% |
| v3 (independent) | 82.6% / 83.7% | 82.9% / 85.7% | 77.7% / 81.7% |
| v4 (independent) | 68.6% / 72.1% | 79.4% / 82.5% | 70.9% / 73.9% |

- Against the transcription before the review, v1's value agreement was 77.4% (f. 218r), 65.6% (f. 218v), 63.9% (f. 219r) — the figures in the previous version.
- Disagreements with v4 left after relabelling: `second/v4/diff_after_relabel.tsv` (not rechecked on the images).

### Assessment
- Figure used: for each page, the lower value agreement of the two independent second transcriptions, v3 and v4 (`python3 src/compare2.py --judge`): f. 218r 72.1% (v4), f. 218v 82.5% (v4), f. 219r 73.9% (v4).
- All three pages are at 70% or above, which meets the level required to present a partial reading. The level required to call it a full reading (85% or above) is not met on any page.
- Decoding v4 with the same key and running the shuffled-key control (1,000 each): the real key scores −3.792 (f. 218r), −3.307 (f. 218v), −3.427 (f. 219r), above the best shuffled key (−4.084, −4.374, −4.347); shuffled ≥ real 0/1000 on all three pages.

## Use of AI
- Transcription of the images, inferred values, decoding, scripts and documents were done by Anthropic's Claude (Claude Code, model Claude Opus 5.5). A person (the owner of this repository) chose the target, saved the images and decided on publication.
- In the first pass each line was transcribed into sign names once, without voting. A second transcription by another AI (Codex) is described in the section above.
- The review of the disagreements on ff. 218v and 219r against the images, and the corrections, were also done by Claude (Claude Opus 5.5).
- **No human has checked the transcription.** Both transcriptions were made by AI; agreement between AIs is not a substitute for human checking.
- For ff. 218v and 219r, the plain text was first read from the images, and only then were the lines transcribed into sign names. The transcription may have been pulled toward that first reading.

## Limits
- The calibration covers six lines (157 signs) only, and the accuracy of the transcription alone (sign by sign) was not measured separately.
- Similar signs (f / long f / ƒ; δ / 8 / ɣ; ꝗ / 4; the hooked ʃ family; ∝ and ∝ with a loop below; round ℒ and angular ∠) were chosen by context in places. This favours the real key in the controls.
- Most inferred values were checked on only two or three places in this letter. Those checked on one place only say so in `data/key.tsv`.
- Signs with no value and unread passages are in [OPEN.en.md](OPEN.en.md).
