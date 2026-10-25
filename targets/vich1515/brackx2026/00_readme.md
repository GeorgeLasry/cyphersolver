# AHN Estado 8715 N.73 (vich1515): reading, tables, keys, scripts and work files

Files for dbourdeau/cyphersolver#94, updated after the Terrateig crib (Barón de Terrateig, *Política en Italia del
Rey Católico, 1507–1516*, vol. I, CSIC 1963, pp. 631–634) and four rounds after it. The 1963 text is not included:
the files give page references, alignment results and short phrases only. Gists are flat, so folders are prefixes.

- **Texts:** `n73_reading.md` (all 124 lines, the letter's spelling, holes sized), `n73_en.md` (English, same
  marks), `n73_decryption.md` (decryption against the transcription, with the token splits and the four
  image corrections), `n73_tokens.tsv` (one row per token: line, position, token, split label, value, status,
  reading word), `n73_sin_x_tokens.tsv` (every `sin`/`sim` and `X` token: value, basis image-checked, crib or
  model-assigned, model margin), `n73_codebook.md`, `n73_legend.md`.
- **Keys:** `key_*` (sign and group values; `key_groups.json` gives each group's status and basis).
- **Scripts:** `script_*`: the joint sign/group annealer `script_wsa4.c` and its drivers, the matched Lazarillo
  control `script_control_matched.py`, the `sin`/`X` split scripts, the crib scripts (`script_crib_apply.py`,
  `script_crib_reading.py`), the round scripts (`script_rounds_apply.py`, `script_rounds_reading.py`,
  `script_assemble.py`, `script_ctx2.py`), and the notation and hole-check scripts. They run side by side in one
  folder under their names without the `script_` prefix, with the Spanish model and word lists built by
  `script_build_lm.py` and `script_make_wide.py` from Project Gutenberg 1619 and 2000.
- **Work files:** `work_*`: the transcriptions (`work_n73_tokens.txt` as in the repository; `work_v15x.txt` with the
  context splits; `work_v15c.txt` with the crib splits and image corrections), the per-token crib values
  (`work_crib_tokens.tsv`, letters and page references only), and the reading and English bodies at each stage.
- **Notes:** `notes_solve.md` (method, score history, controls, the crib, the rounds, what remains).
