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

1. **Is there a text of it already?** Open every image and attachment already on the DECODE record first: acciaiuoli1757's
   decipherments were png attachments listed as "work images" and never opened, nuncio1566's R87 decipherment was its
   "cleartext" image, ronquillo1676's margins were in DECODE comment blocks. A contemporary decipherment (interlinear, margin, slip, a clear copy or minute
   bound nearby — look at the neighbouring folios/records, not only the one listed), a printed edition or calendar, or
   another scholar's decipherment (DECODE record, Lasry, Tomokiyo's cryptiana, an article). If yes: transcribe it (or the
   part not yet in the repository), align it with our decode, and the reading follows it, with the figures checked where
   they disagree. Record where it is. A copyrighted modern edition is cited, not copied (then `texts_withheld` or a note).
2. **If not, read it on the image.** Fetch full-resolution images: Gallica through openapi.bnf.fr IIIF
   (`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<n>/<x,y,w,h>/<w>,/0/default.jpg`; gallica.bnf.fr/iiif
   gives 403), BL through bl.digirati.io IIIF (memory note: 1024-px tiles, stitch them), DECODE images if they are
   already in the main checkout (`C:\Users\dbour\cypher\targets\<folder>\`, git-ignored folders such as `img/`,
   `decode/`), and DECODE records and images through the project's cookie
   (`C:\Users\dbour\cypher\targets\bordeaux\decode\cookie.txt`, working on 22 Oct 2026; see the sauli1579 reread log for
   the request form). Only if all of these fail is a text out of reach — say which failed. Go sentence by sentence; at each break look at the
   figures, correct the transcription label (keep a tsv), adjust the key only with values that hold across the
   document, re-decode, continue.
3. **Do not invent.** Every word of a reading is carried by its figures or by a contemporary/printed text you name.
   `[?word]` for partly carried, `[word]` for a word you supply that nothing carries (a verb or article the sense
   needs), `[…]` for unread, `[47]` for an unidentified code. **Before you finish, align each reading word by word with
   its decode (and the contemporary text) and bracket every word neither carries**: an unbracketed supplied word is an
   invented word (a spot check found "Il dict depuis" where the figures give "il depuis").
4. **The bar, applied the same way to every document:** a document is `read` when a reader finds its sentences
   coherent **and** its reading body (header and notes cut off) scores about 0.60 clean sentences or more on
   `_check_reading.py`; below that it stays `decoded, not read`, with your reading kept as a partial reading and a note.
   **Look-alike alternates:** count the letters that rest on the other member of a look-alike pair rather than the
   figure's own value; above about 3% of a reading's letters, keep it decoded, not read unless a contemporary or printed
   text confirms them (sense alone can then drive the reading).
   **Never modernise spelling in the reading to pass the score** (modern spelling goes only in the English file).
   When the word list cannot know the period spelling (English before 1700, early Spanish, Dutch, German), score the
   reading body counting explicit holes only (`research/reading_audit/b17_score.py` with `HOLES=1`) and record both
   figures; the bar is then about 0.60 on the explicit-hole share plus a reader's judgement that the sentences hold.
   (Kept unread at 0.47-0.56 so far: matignon1586 f. 124r, fiesque1567 10 Sep 1569, smith1562 no. 15, nunzio1736
   423/9, 423/11.)
5. **Stop** when the sentences hold (most sentences with at most one hole in ten words; `python docs/_check_reading.py
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
