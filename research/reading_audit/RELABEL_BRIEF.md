# Relabel brief: targets the reading audit graded C or D (22 Oct 2026)

The reading audit (`research/reading_audit/`, rubric `llm/RUBRIC.md`, results `audit.csv`) asked of every published
reading George Lasry's question: can a reader build coherent sentences from it and translate them? Targets graded
**D** (holes in most sentences) or **C** (mixed: some documents read, others do not) are relabelled so that the
site and the paper data claim no more than what reads. This is labelling, not cryptanalysis: no key or reading is
changed here.

Worktree: `C:\Users\dbour\cypher\.worktrees\reading-gate`. Model: `targets/matignon1586/` after commit 021b4de9f
(profile `outcome.texts[].state`, NOTES status block, gaps, page).

## Per target in your list

1. **Check the grade yourself.** Open each `outcome.texts` entry's decryption (and any reading file the audit row
   names). Run `python docs/_check_reading.py <folder>`. For each document decide: does it build coherent sentences
   with only scattered holes? Read it; the score is a hint, the reading is the test. If you find the audit wrong for a
   document (it reads), leave it `read` and add `"reading_review": {"grade": "A" or "B", "by": "Claude (reading audit)",
   "date": "2026-10-22", "note": "<why>"}`.
2. **Mark each document** in `profile.json` `outcome.texts[]`: `"state": "decoded, not read"` for one that does not
   read (and a `note` saying why in one line), `"not prose"` for key sheets, word lists, worksheets. Set `"language"`
   (ISO 639-1) on every entry.
3. **Correct the claim** where it overstates:
   * a target classed `read` with any decoded-not-read entry becomes `read in part`;
   * if every entry is decoded, not read, the target is not a reading: set `outcome.class` to the class used for
     open targets (`"not read"`) and `outcome.method` to `not solved`, unless the text
     exists in print or in a contemporary decipherment the project transcribed (then the method that fits, with the
     printed or contemporary text as the reading);
   * `outcome.fraction_read`: re-measure as the share of tokens in documents that read (say how in
     `fraction_read_source`, keep the old figure there as "withdrawn as a reading figure"); if tokens per document are
     not available, set `fraction_read_method` to `estimated` and say so;
   * append a solution step (`kind: verification`, `result: failed` when the claim fell) describing the check.
   `python docs/_check_profile.py <folder>` must stay `result: valid`.
4. **NOTES.md**: a short dated block at the top of the status ("22 Oct 2026, reading audit: ...") naming what reads
   and what is decoded, not read; a `## Remaining gaps` line per decoded-not-read document with blocker
   `not-attempted` (workable) or the outside blocker that applies.
5. **The page** `docs/<slug>.html` (slug from `docs/_build_site.py` PAGES; usually the folder name): if its summary,
   At a glance or headline figure claims a reading that is now decoded-not-read, correct those sentences in the same
   plain style. Do not rebuild the site; do not touch other targets, the README or ledgers (the lead does those).
6. Reply with one line per target: old claim → new claim, documents relabelled, and any audit grade you overturned.

Do not commit. Edit only the files of the targets in your list.
