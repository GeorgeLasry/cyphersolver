# Verification brief: every hand-built reading checked word by word (22 Oct 2026)

Readings built today by reading a decode sentence by sentence (matignon1586, carpio1677, sauli1579, alessandrino1568,
ronquillo1676, nevers1574, selve1535, and later re-read batches) must not contain a word that neither the figures nor a
named contemporary/printed text carries. A spot check of fiesque1567 found 82 such words in 23 letters (25 supplied
outright, 57 only partly carried), e.g. "Il dict depuis" where the figures give "il depuis". This pass is an
independent check by a reader who did not write the readings.

Worktree: `C:\Users\dbour\cypher\.worktrees\reading-gate`. Method example: `research/reading_audit/reread_b02_align.py`
(aligns a reading with its decode letter by letter, counting the known sign confusions as matches, codes expanded) and
`reread_b02_mark.py`.

## Per target in your list, per reading file built on 22 Oct 2026

1. Find what the reading rests on: its header names the decode, the corrected transcription and leaf key, and any
   contemporary decipherment, copy or print (transcribed in the folder).
2. Align the reading word by word with that source. For a reading that follows a contemporary text, the contemporary
   text is the source and the figures the check; for one built from the key, the decode (re-run with the leaf key if
   the corrected transcription differs from the decode file) is the source.
3. Bracket every word neither source carries: `[word]` supplied, `[?word]` partly carried. Do not rewrite; do not
   remove brackets that are there; if a word is wrong (the source has another word), replace it with the source's word
   and list the change.
4. Re-score the reading body only (cut the header and notes off to a scratch file): `python docs/_check_reading.py
   --file <scratch>`. The rule used so far: a document stays `read` at about 0.60 clean sentences or more on the reading
   body and when a reader finds its sentences coherent; below that it becomes `state: "decoded, not read"` with the
   reading kept as a partial reading and a note (what blocks it).
5. Change the English translation to match any word you bracketed or replaced.
6. profile.json (targeted edits, save after each change; `relabel_docs_0.py` splice helper): only `state`/`note` when a
   document falls below the rule, and the `reading_review.note` (append "verified word by word 22 Oct 2026: N words
   bracketed, M replaced"). `python docs/_check_profile.py <folder>` must say valid. Do not edit NOTES, pages, README.

Reply: per target and document — words bracketed (supplied / partly), words replaced, clean share before → after,
state changes.
