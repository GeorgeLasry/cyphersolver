# Where the numbers come from / 数字の出どころ

Every number in README.md, README.en.md and docs/METHOD*.md, and where it is computed. Recompute with the command shown.
README・METHOD の数字ごとに、出どころと計算し直す方法を示す。

| number | meaning | source / command |
|---|---|---|
| 32 lines (20 + 12) | cipher lines of f. 50r–v | `data/transcription_f50.txt` (ids r01–r20, v01–v12) |
| 568 (90.7%), 590 (94.2%) of 626 (576, 598 against the transcription of f30eee9) | independent second transcription: same name / same value class | `python3 src/independent.py data/transcription_f50.txt second/codex_independent.txt` (stderr) |
| 626 signs | signs of the final transcription | `python3 src/vote.py data/transcription_f50.txt second/codex_pass*.txt` (stderr: `signs 626`) |
| 572 / 604 / 20 / 2 | five passes all agree / majority agrees / majority differs / no majority | the same command (`all_agree`, `majority_agrees`, `majority_differs`, `no_majority`); per sign in `second/vote.tsv` |
| 15 → 4 corrected | majority disagreements before the last revision, and corrections | `second/VOTE.md`; the revision note in `data/transcription_f50.txt` |
| 633; 565 / 554 / 559; 546 | first transcription; agreement with Codex passes 1–3; all three agree | `python3 src/xcompare.py data/transcription_f50_before_xcheck.txt second/codex_pass1.txt second/codex_pass2.txt second/codex_pass3.txt` (stderr) |
| 10, 9, 2 corrections (σ, barred y, 24); 8 of the 10 σ later returned to 6 | corrections after the first cross-check, and the image re-check | `second/RESULT.md` (counted from the MAJ rows of `second/compare.tsv`); `second/CORRECTIONS.md` |
| −3.302, −5.079, 0/1000 (and the other rows of the control table); the earlier values −3.421, −3.458, −3.446, −3.286 | real score, max of 1000 shuffles, shuffles ≥ real | `sh controls/run.sh` → `controls/results.txt` (seed 1) |
| 73 / 61 / 69 signs | signs in the full key / table-only / without inferred values | `table_only=... signs=...` lines of `src/control.py`; `controls/key_without_target.tsv` |
| f. 50v lines 7–12 | the last fifth (6 of 32 lines) | `controls/heldout_last_fifth.txt` |
| 0.913 (253/277), 0.874 (242/277); 0.924 (256/277) with the key at freezing | sign accuracy on f. 171r lines 12–24 (the 3 signs lost since the 0.924 are mz = i; see the git history of `calib/signs_score.txt`) | `python3 src/score_signs.py data/key.tsv calib/f171r_tx.txt calib/f172r_ref.txt [--strict]` → `calib/signs_score*.txt` |
| 93.6% (337/360), 84.2% (303/360) | letter agreement of the reading / of the bare key | `python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt` and `calib/f171r_mech.txt` |
| 13 lines, 360 letters | size of the calibration | `calib/f172r_ref.txt` |
| 6 mz (s), 11 mi (i) | the split of mz, each checked on the image | names mz and mi in `data/transcription_f50.txt` |
| 620 signs, 617 (99.5%), 613 (98.9%) | cipher signs; with a value; without inferred values | `python3 src/valued.py data/key.tsv data/transcription_f50.txt` |
| 9 open items | signs or groups without a value | rows of the table in `docs/OPEN.md` |
| 451 of 630 | NoAutopilot's draft | header of their reading.txt (version f3dcded, 13 Oct 2026; not in this repository) |
| 21 lines, 424 signs, 406 / 412 | f. 230r aligned with f. 232r; signs falling on a key value with the key before / after the changes | `python3 src/align_sister.py data/key.tsv data/f230r_tx.txt data/f232r_ref_l1-21.txt` → `data/f230r_sign_counts.tsv` (sum the counts whose letter is among key_values); the 406 uses `data/key.tsv` of commit e009472 |
| every T row: main value in the table | check of the key against the table | `python3 src/check_table.py data/key.tsv data/tomokiyo_table_signs.tsv` (last line) |
| views 111, 112, 366, 368, 486, 490, 402, 424, 487 | Gallica view numbers | `SOURCES.md` |
