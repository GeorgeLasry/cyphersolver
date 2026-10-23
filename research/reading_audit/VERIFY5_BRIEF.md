# Verification 5: read documents in languages where the plain score is also the bar (23 Oct 2026)

`v3_sweep.tsv` flags `plain-only` the read documents whose reading passes the explicit-hole measure (v2_score: every
conjecture, supplied word, part-word and unread sign a hole) but scores under 0.60 on the plain word-list measure.
For old spelling the explicit-hole share is the bar. For French and Spanish after ~1600, Italian after ~1600 and
English after ~1700 the word lists know the spelling, so the plain share is the bar too (REREAD_BRIEF step 4).
`v5_plainbar_a.txt` / `_b.txt` list those rows: folder, idx, doc, lang, scored file, year (guessed from the folder
name or profile; check it), plain, explicit.

## Per row
1. Check the year and language. If the text is in fact older spelling (or another language), the explicit-hole share
   is the bar: note it in `reading_review.note` and keep read.
2. Find the proper reading body (cut headers, notes, line labels, token tables: `v3b_lines.py`, `v3b_body.py`) and
   rescore with `v2_score.py`. Many rows are false alarms of that kind; point `reading` at a clean reading file.
3. If the plain share is still under ~0.60, look at why: names and places the word list lacks (judge as a reader;
   a sentence whose only "holes" are proper names or period abbreviations holds), clerk's slips, or real holes.
   Read it yourself: do most sentences hold, at most about one hole in ten words?
4. Decide as in VERIFY3_BRIEF: keeps read (record both scores and why in `reading_review.note`), workable (lift it
   with REREAD_BRIEF steps 1-3: decipherment on the record, image, key), or demote (state "decoded, not read", note,
   remove reading_review, `set_fraction.py`, class, a gap with exactly one blocker: not-attempted, no-key-material,
   too-short, illegible, needs-physical-access; `set_state.py` with DROP_REVIEW=1 does the entry).
5. `python docs/_check_profile.py <folder>` → result: valid; dated NOTES block; a solution step.

Never modernise spelling in a reading; never touch fr. 3029 / fr. 3092. No pages, README or ledgers; no commit; no
helper agents. Images only in the session scratchpad `reread\v5\`.
Reply as a table: folder / doc / year+lang checked / body scored / plain, explicit before → after / decision / why.
