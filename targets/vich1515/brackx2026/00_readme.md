# AHN Estado 8715 N.73 (vich1515): reading, tables, keys, scripts and work files

Files for dbourdeau/cyphersolver#94. Gists are flat, so the folders are prefixes:

- **Texts:** `n73_reading.md` (all 124 lines, writer's spelling, holes sized), `n73_en.md` (English, same marks),
  `n73_decryption.md` (decryption against the transcription), `n73_tokens.tsv` (one row per token: line, position,
  token, split label, value, status, reading word), `n73_sin_x_tokens.tsv` (every `sin`/`sim` and `X` token, value,
  basis image-checked or model-assigned, model margin), `n73_codebook.md`, `n73_legend.md`.
- **Keys:** `key_*` (sign and group values; `key_groups.json` gives each group's status).
- **Scripts:** `script_*` (the joint sign/group annealer `script_wsa4.c` and its drivers, the matched Lazarillo
  control `script_control_matched.py`, the `sin`/`X` split scripts, the notation and hole-check scripts). They were
  written to run side by side in one folder under their names without the `script_` prefix, with the Spanish model and
  word lists built by `script_build_lm.py` and `script_make_wide.py` from Project Gutenberg 1619 and 2000.
- **Work files:** `work_*` (the split transcriptions, the per-token choices, the reading and English bodies before
  and after the notation change).
- **Notes:** `notes_solve.md` (method, score history, controls).
