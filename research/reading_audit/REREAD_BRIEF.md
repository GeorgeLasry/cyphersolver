# Re-reading brief: turn "decoded, not read" documents into readings (22 Oct 2026)

George Lasry, 22 Oct 2026: *"The requirement should be that the LLM can build coherent sentences - that can later be
translated to English, and iteratively improve the transcription and the key until this is the case."* The reading
audit marked documents that do not build sentences `state: "decoded, not read"` in `profile.json`. This brief turns
them into readings where the evidence allows, and says plainly why where it does not.

Worktree: `C:\Users\dbour\cypher\.worktrees\reading-gate`. Worked examples, read before you start:
* `targets/carpio1677/` — contemporary margin decipherments transcribed and aligned with the key decode: all ten letters
  read (`read/R1008_reading.md`, `_en.md`; NOTES "22 Oct" blocks).
* `targets/matignon1586/` — no copy: each break checked on full-resolution crops, labels corrected, the reading built
  by hand from the key's letter sets (`texts/reading_f173_log.md`, `reading_f110_log.md` for a re-transcription against an
  exemplar set); two unrecorded clear copies found on neighbouring folios (`reading_f177_vs_copy.md`).

## Per document, in this order

1. **Is there a text of it already?** A contemporary decipherment (interlinear, margin, slip, a clear copy or minute
   bound nearby — look at the neighbouring folios/records, not only the one listed), a printed edition or calendar, or
   another scholar's decipherment (DECODE record, Lasry, Tomokiyo's cryptiana, an article). If yes: transcribe it (or the
   part not yet in the repository), align it with our decode, and the reading follows it, with the figures checked where
   they disagree. Record where it is. A copyrighted modern edition is cited, not copied (then `texts_withheld` or a note).
2. **If not, read it on the image.** Fetch full-resolution images: Gallica through openapi.bnf.fr IIIF
   (`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<n>/<x,y,w,h>/<w>,/0/default.jpg`; gallica.bnf.fr/iiif
   gives 403), BL through bl.digirati.io IIIF (memory note: 1024-px tiles, stitch them), DECODE images if they are
   already in the main checkout (`C:\Users\dbour\cypher\targets\<folder>\`, git-ignored folders such as `img/`,
   `decode/`); DECODE behind its login is out of reach — say so. Go sentence by sentence; at each break look at the
   figures, correct the transcription label (keep a tsv), adjust the key only with values that hold across the
   document, re-decode, continue.
3. **Do not invent.** Every word of a reading is carried by its figures or by a contemporary/printed text you name.
   `[?word]` for partly carried, `[…]` for unread, `[47]` for an unidentified code.
4. **Stop** when the sentences hold (most sentences with at most one hole in ten words; `python docs/_check_reading.py
   --file <reading>` as a pointer; your own reading is the test), or when the remaining breaks have an outside blocker
   (illegible, image not reachable, no key material) — name it.

## Files

* `<dir>/<doc>_reading.md` (the reading, holes marked, a header saying what it rests on), `<dir>/<doc>_en.md`
  (English, same holes), `<dir>/<doc>_reread_log.md` (what was tried, including failures), transcription
  corrections as `<dir>/<doc>_corrections.tsv` and a corrected transcription file when labels changed. `<dir>` is the
  folder of the document's decryption file.
* `profile.json`, with targeted edits keeping the layout (`research/reading_audit/relabel_r0.py` splice approach, copy
  as `reread_<batch>.py`): when it reads, set `state` to `read` (remove the decoded-not-read `note`), add `reading`,
  `translation`, `language`, and `reading_review` {grade A|B, by: "Claude Opus 5.5", date: "2026-10-22", note: what it
  rests on}; when it does not, keep the state and rewrite the `note` with what was tried and the blocker. Re-measure
  `fraction_read` as tokens of documents that read / all (say how in `fraction_read_source`), and if every document now
  reads and nothing workable is left, the `class` can return to `read`. Append solution steps (failures too).
  `python docs/_check_profile.py <folder>` must say `result: valid`.
* `NOTES.md`: a dated block, the Remaining gaps lines updated (closed, or the blocker named), Escalation ticked.
* Do not edit pages, README or ledgers; do not commit; save images only in
  `C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\`.

Reply per document: before → after (clean-sentence share), what it rests on, what stays open and why, one sentence
with its translation.
