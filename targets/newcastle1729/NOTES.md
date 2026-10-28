# newcastle1729: Port Sainte-Marie intelligence report in numerical code, 1729

Status: in progress

Catalogue #826. Huntington Library, William Blathwayt papers addenda, mssBLA 191 (HDL p15150coll7 id 61008),
p. 5 (HDL 61005). Contributed by johonn; the work was done by Claude Code under johonn's direction.

## State at the first push (28 Oct 2026, work in progress)

Pushed as a work-in-progress checkpoint; the write-up, translation and checks below are still to do.

- Code table rebuilt from five sibling letters (383 groups, 1,078 glossed groups): `codetable.tsv`, built by
  `build_table.py` from `transcription/sib*.txt`. The code is a syllable-and-word nomenclator, roughly alphabetical.
- Report (HDL 61005) transcribed, 141 groups; `decode.py` gives a firm value to 116, a doubtful one to 2, and
  leaves 22 tokens (20 distinct groups) open. `decryption/report_61005_reading.txt` is the French with holes in
  place; by `docs/_check_reading.py` it is "decoded, not read" (no clean sentences, hole rate 0.25).
- Not done yet: this NOTES.md in full (## Remaining gaps, ## Escalation), the English translation, the full
  solution steps and outcome in `profile.json`, the DECODE queue entry, the print search, the three checkers.
- `validation.tsv` is written but `docs/_validate.py` could not run here (Gutenberg corpora unreachable).
- The step-by-step record is `WORKLOG.md`.
