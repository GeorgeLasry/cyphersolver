# Relabel brief, second wave: single documents that fail (22 Oct 2026)

The per-document pass (`llm/docs_*.jsonl`, merged into `reviews.json` under each target's `docs`) graded every
document of the targets that had passed on a sample. The failures per target are in `docs_fail.json` (`fails`:
[doc key, grade, missing]) and the excerpt-only documents under `excerpt`. Follow `RELABEL_BRIEF.md` for each failing
document, with these additions:

1. **Check the grade yourself** on the document (the reviewer's reason is in `reviews.json`). Overturn it where the
   document does build sentences; record your own `reading_review` on the entry then.
2. **C or D**: `state: "decoded, not read"` with a one-line `note` (what fails, what would fix it), the claim and
   `fraction_read` cut back, NOTES gaps (blocker `not-attempted` unless an outside blocker applies) and
   `Status: in progress` if any gap is workable, the page's claims corrected.
3. **N, not prose** (a worksheet, key sheet, list of corrections, a three-line address): `state: "not prose"` with a
   `note` saying what it is.
4. **N, missing** (`missing: true`: the text is on images, behind a login, in print, never transcribed): if the text
   can be reached now — Gallica through openapi.bnf.fr IIIF, BL IIIF, archive.org or HathiTrust prints, files already in
   the main checkout `C:\Users\dbour\cypher\targets\<folder>\` — note it as a workable gap (`not-attempted`) for the
   re-reading wave and mark the entry `decoded, not read` (or, if nothing of ours exists, leave the entry out of the
   reading and say so); if it cannot (DECODE login, a book Google blocks), blocker `needs-physical-access` or
   `no-key-material` as fits, and the claim must not rest on it.
5. **Excerpt-only documents** (`excerpt` list): the reading is someone else's (usually Lasry's report) and only an
   excerpt is in the repository. Keep `state: "read"` only for what the excerpt shows; add to the entry's `note`:
   "excerpt only: the full decipherment is <where>"; make sure `fraction_read` and the page do not claim more than the
   repository shows (say "read by <who>; excerpt here").
6. Keep each profile.json's layout (`relabel_r0.py` splice approach, copy as `relabel_docs_<n>.py`); `python
   docs/_check_profile.py <folder>` must say valid. Do not touch README, ledgers, or other targets; do not commit.

Reply: one line per target — documents relabelled (with new state), grades overturned, claim old → new, missing texts
that are reachable (where), excerpt notes added.
