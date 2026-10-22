# Method, figures, AI use and limits

[日本語](METHOD.md)

## Images
- BnF Baluze 103 (Gallica ark:/12148/btv1b9001389d): f. 50r = view 111, f. 50v = view 112, fetched at full size (4864×6996) from the BnF IIIF server (openapi.bnf.fr). The images are not in this repository.
- Sister letters used to check the key: f. 230r (view 486) and its period decipherment f. 232r (view 490). For the code groups: f. 171r (366), f. 189r (402), f. 200r (424), f. 230v (487).

## Key (`data/key.tsv`)
1. Base: Satoshi Tomokiyo's table (Cryptiana, louisxiv0.htm, "Le Tellier-Marca Cipher (1644)"), rewritten with our sign names; the signs of each column, in our names, are in `data/tomokiyo_table_signs.tsv`.
2. Lines 1–21 of the sister letter f. 230r were transcribed by sign name (`data/f230r_tx.txt`) and aligned line by line, by dynamic programming, with the matching part of the period decipherment f. 232r (`data/f232r_ref_l1-21.txt`); the letters each sign stands for were counted (`src/align_sister.py` → `data/f230r_sign_counts.tsv`; per sign in `data/f230r_aligned.tsv`). Of 424 signs, 406 fall on a key value with the key before the changes, 412 after. Values and signs not in the table were added: R = c, ʒc/ʒx = r, ꝺ = r, ℒ = M, Ꝺ = h, k = u, small o = z, small ʒ (z3) = s, ff = d (besides a), 6 = l (besides t).
3. Code groups: =9 pour, =11 que, =12 qui, =26 vous, =32 Barcelone, 81 faire, 39 Catalogne, =y Monsieur le Mareschal, =3 de La Motte, =11 =o la Reyne, =l =m du Roi, =83 le Gouverneur (f. 230r line 21). =3 was checked on f. 230r and f. 200r; =11 =o at three places of f. 189r against f. 190r.
4. Column source: T = Tomokiyo's table; S = checked on f. 230r/f. 232r; X = split after the AI cross-check; C = inferred from f. 50 alone.
- **Check against the table**: the main value of every row whose source includes T is in the matching column of `data/tomokiyo_table_signs.tsv` (command in NUMBERS.md). Most other values (6 = l, u = y, ...) are not in the table and come from the f. 230r alignment (S).
- Corrections made during the checks:
  - 6 and the σ sign, y and the barred y, are different signs (found in the AI cross-check; as in the table's columns). On f. 230r, however, 6 stands for l six times (la Vallee, lettre, ...), so the other value l of 6 is kept.
  - y had wrongly been given the main value n; it is g, as in the table. The three y of f. 50 are the g of soing and garde and the b of liberté; the four of f. 230r are g 3, b 1; none is n.
  - The curly x has two forms, without a bar (f column) and with a bar through it (c column); Codex called both "ae".
  - mz has two forms: with a barred tail (the m7 of the table's s column) and with an unbarred curled tail (the table's i column). Looking at the 17 places of f. 50 one by one on the image, the six barred ones are all s and the eleven unbarred ones all i; the latter are now named mi.
  - The q-like sign for i is taken to be the 9-shaped sign of the table's i column, and ℓ the sign of its x column.

## Transcription (`data/transcription_f50.txt`)
- Claude transcribed the full-size line images once, by sign name (`data/transcription_f50_before_xcheck.txt`).
- Second transcription: OpenAI Codex CLI (codex-cli 0.163.0-alpha.10.2 bundled with the ChatGPT app, default model) was given only the images and the list of sign names (shape descriptions only; no values, no first transcription, no key, no decipherment) and transcribed the page five times independently: passes 1–3 one image per line (`second/PROMPT.md`), passes 4–5 each line cut into two overlapping halves (`second/PROMPT_halves.md`). No pass ran a command or read a file (execution logs).
- First transcription vs Codex passes 1–3: 565, 554, 559 of 633 signs agree; all three agree on 546. Disagreements were checked on the full-size image; we corrected the barred y (9) and "2 4" read as one number 24 (2), among others. Of ten places first changed to the σ sign, only the two confirmed on the image were kept and eight were returned to 6 (`second/RESULT.md`; every correction is listed in `second/CORRECTIONS.md`).
- Five-pass vote: of the final 626 signs, all five agree on 572, the majority agrees on 604, the majority gives another name on 20, no majority on 2. The 15 majority disagreements before the last revision were checked on the image and 4 corrected (`second/VOTE.md`).
- The five passes above were used to correct the transcription, so they are a cross-check record, not an independent second reading. **Independent second transcription**: after the last correction (commit f30eee9), Codex read the page once more in a fresh context (`second/PROMPT_independent.md`, `second/codex_independent.txt`): same name on 568 of 626 signs (90.7%), 590 (94.2%) counting names with the same key value as one. The largest disagreement: nine barred y (n) read as plain y (g). The transcription was not corrected from this comparison (`second/INDEPENDENT.md`).
- **Agreement between AIs is not a substitute for checking by a person. No person has checked the transcription.**

## Controls (`src/control.py`, `controls/run.sh` → `controls/results.txt`)
Real key vs 1000 shuffles of its values, scored by French letter-trigram likelihood (built from the top 50,000 French words of wordfreq).

| transcription | key | real | max of shuffles | shuffles ≥ real |
|---|---|---|---|---|
| final (32 lines) | all signs (73) | −3.302 | −5.079 | 0/1000 |
| final | Tomokiyo's table signs only (61) | −3.203 | −4.741 | 0/1000 |
| final | without values inferred from f. 50 (source C only) (69) | −3.281 | −4.782 | 0/1000 |
| last fifth (f. 50v lines 7–12) | all signs | −3.008 | −4.450 | 0/1000 |
| last fifth | without inferred values | −3.008 | −4.625 | 0/1000 |
| Codex passes 1–5 | all signs | −3.751 / −3.589 / −3.540 / −3.716 / −3.527 | −5.011 / −4.996 / −5.006 / −5.041 / −4.976 | 0/1000 each |

The score moved with each correction (−3.421 before the cross-check, −3.458 after it, −3.446 after the y correction, −3.286 after splitting mz and mi, −3.302 after returning eight σ to 6); every version gives 0/1000. The Codex transcriptions have no mi, so their real scores do not depend on that split.

## Calibration (`calib/`)
Lines 12–24 of f. 171r were read with the same key and the reading frozen (SHA-256 in `calib/hashes_before_answer.txt`) before the period decipherment f. 172r was opened.

| measure | result |
|---|---|
| sign accuracy, main and other values (`src/score_signs.py`) | 0.913 (253/277); 0.924 (256/277) with the key at the time the reading was frozen |
| sign accuracy, main value only | 0.874 (242/277) |
| letter agreement of our reading (`src/calib.py`) | 93.6% (337/360) |
| letter agreement of the bare key | 84.2% (303/360) |

The drop from 0.924 to 0.913 is because the frozen calibration transcription predates the mz/mi split, so an mz that stands for i no longer matches under the current key. Only 13 lines; not fully blind (we had earlier read seven lines of f. 172r, the start of the page, in NoAutopilot's transcription, so lines 1–11 were not used). Two findings came after seeing the answer and were not added to the key: an unbarred "12 19" = qu'il, and a 9 with a small g above = Sr.

## What can be reproduced from this repository
- The checks of code groups on f. 189r, f. 200r and f. 230v, and the decisions made on enlarged images of f. 50, rest on images not included here (view numbers in SOURCES.md). The period decipherments of f. 190r and f. 205r were taken from NoAutopilot's transcriptions and are not included.
- The Codex execution logs (JSON) contain file paths and are not included. "No pass ran a command or read a file" is what we saw in those logs; it cannot be checked from this repository.

## Relation to earlier work
- Satoshi Tomokiyo: the table, and the listing of f. 50 as undeciphered.
- NoAutopilot/cipher-lab (`ciphers/baluze103-letellier-marca-1644/`, last commit f3dcded, 13 Oct 2026, Status: partial / Verdict: parked): a partial draft of f. 50 with Tomokiyo's table (451 of 630 signs valued). We used: the Gallica view numbers, the fact that openapi.bnf.fr serves the images, their note that 6 also stands for l on f. 200r, and their transcriptions of the period decipherments f. 190r and f. 205r (for the checks on f. 189r and f. 200r). Our transcription and reading of f. 50, the f. 230 alignment and the calibration were made without their files. Words their draft already shows are reproduced, not new (README).

## AI use
Transcription, key additions, decipherment, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5). Second transcription: OpenAI Codex. Choice of target, instructions and the decision to publish: a person.
