# Re-reading log, R9414 unread bands (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b37)

Entry: outcome.texts[1], R9414 P1.12-32, P2.15-19, P3.01-09, P3.39-P4.01, P4.21-35, P5.05-07 ("decoded, not read").
The other lines of the letter (texts[0]) read since the 22 Oct audit.

## Starting point

`reading_v5.txt` bands scored here for the first time (`b17_score.py` on the band lines joined, `<...>` doubtful runs and
`[..n]` holes as holes): **0.310** clean sentences (9/29, de word list), **0.379** on explicit holes; hole rate 0.26.
For comparison the reading lines score 0.561 / 0.848.

## 1. Is there a text already?

- DECODE R9414 record re-fetched 23 Oct (`b37_fetch.py`, scratchpad): six images, **no** DOC, xlsx, transcription or
  comment attachment; status unchanged. The only decipherment on the leaves is the interlinear gloss over P1 l. 6-8
  (already the key's seed).
- Neighbouring records of KAA 4591 checked by record page: R9408-R9410, R9413 (System A′, other letters), R9411/R9412
  (Sperantio), R9415 (system L), R9416 (r9416 target), R9417 (System B); R9404-R9407 and R9418-R9422 viewed in Sept.
  None is a copy, minute or decipherment of the Wardein letter, and none is in system G.
- Print: none known (web search of 22 Sept: Zápolya's letters to the Bavarian dukes, Wardein 1537). Not re-searched.

## 2. Read on the image

The fourth pass of 5 Oct 2026 already did what step 2 asks, gap by gap at full resolution (`pass4.txt`, 74 entries,
each with the signs seen, the alternatives under `keyb.txt` + `cp12/alt_p12.txt`, and the decision). Re-checked here
against `decrypt_v2.txt` for P1.12-P1.16: the entries hold (e.g. P1.13b ends in an ink blot; P1.14a has σ under a blot;
P1.15 *und ander* is not in the signs). No new value holds across the letter: the open signs are the Ψ, swash X and K
code signs (no key), the barred ∂ (five places, unidentified), blots and scribal deletions, and words whose signs spell
no German word under any of the homophone alternatives.

No change to the key or the reading. No new transcription labels.

## 3. Alignment

Unchanged reading (`reading_v5.txt`); its words were aligned with the signs in pass 4.

## 4. Bar

0.310 (0.379 on explicit holes) against about 0.60: the bands stay **decoded, not read**. Reader's judgement: P1.12-32
gives the sense in outline (the princes of the Empire should consider what Christendom stands to lose; a Latin letter
written in his name; the Duke's alliance and aid) but most clauses break; P2.15-19 and P4.21-35 break in nearly every
clause.

Blockers: code signs without a key (no-key-material), blots and deletions (illegible), legible words that spell nothing
under the recovered homophone alternatives with no further key source in the volume or on DECODE (no-key-material).
