# Verification 3: read documents that fail even the explicit-hole measure (23 Oct 2026)

The 23 Oct verification pass found that `b17_score.py` with `HOLES=1` let a bracketed `[?word]` count as a known
word, so some readings passed the bar on conjectures. `v2_score.py` counts every `[?word]`, supplied `[word]`,
part-word and unread sign as a hole. `v3_sweep.py` rescored every `read` entry with it (`v3_sweep.tsv`); the rows
flagged `below` (explicit-hole share under 0.60 even before the word list is consulted) are listed in
`v3_below_a.txt` / `v3_below_b.txt` as `folder<TAB>idx<TAB>doc<TAB>lang<TAB>scored file`.

The sweep scores whichever file the entry names (its `reading`, else its `decryption` list), the body after
`## Reading` or else the whole file, so a row can be a false alarm: a file with a long header or notes, a token
table, a sign list, a key file, a whole-volume file covering several entries, or the wrong language. Work out which.

## Per row

1. Open the entry in `targets/<folder>/profile.json` (by index) and the scored file. Find the actual running text
   of this document. If the file is not a reading (tsv, token stream, key, raw decode with no word division), the
   entry has no reading yet: that is a finding, not a false alarm.
2. If there is a proper reading body (possibly in another file, or after cutting header/notes), score it:
   `python research/reading_audit/v2_score.py <file> <lang>` (put the body in a scratch file if needed). Read it
   yourself: do most sentences hold, with at most about one hole in ten words, every unbracketed word carried by the
   figures or a contemporary/printed text?
3. Decide, by REREAD_BRIEF step 4:
   * **keeps read** — the reading body scores about 0.60 or more on the explicit-hole measure (plain too, for
     languages whose word list knows the spelling: modern-spelling French after ~1600, Italian, Spanish after ~1600,
     English after ~1700) and the sentences hold. If the entry pointed at the wrong file, point `reading` at the
     right one (or write `<doc>_reading.md` from the existing text, holes marked, header saying what it rests on).
     Record the score in the entry's `reading_review.note`.
   * **workable** — below the bar but a contemporary decipherment, print, or full-resolution image is reachable and
     an hour's work would lift it: do it, following REREAD_BRIEF steps 1-3 (save sign transcriptions, align word by
     word, never modernise spelling), then decide again.
   * **demote** — otherwise set `state` to `decoded, not read` with a `note` saying what fails and the score, remove
     its `reading_review`, recompute `fraction_read` (`set_fraction.py`), set the class back if no document reads,
     and add an `outcome.gaps` line with exactly one blocker: not-attempted, no-key-material, too-short, illegible,
     needs-physical-access.
4. Edit profiles with a targeted splice by index (copy `reread_b35.py` as `v3_<a|b>.py`; shared doc values: by
   index). `python docs/_check_profile.py <folder>` must say `result: valid`. Dated NOTES.md block; Remaining gaps
   and Escalation updated; a solution step appended (failures too). If a target ends with a not-attempted gap, make
   sure `Status: in progress` is in the first forty lines of NOTES.md.

Withheld material: never touch fr. 3029 / fr. 3092 files beyond what is already there. Do not edit pages, README or
ledgers; do not commit; no helper agents. Images only in
`C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v3\`.

Reply as a table: folder / doc / scored file → body actually scored / score before → after / decision / why.
