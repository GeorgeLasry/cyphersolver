# Re-reading log, R27 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". DECODE's transcription of 137r–v (HeHan, April 2016) carries some 60 "?"
marks; the character decode (`R27_decryption.txt`) and the word decode (`R27_worddecode.txt`) were mostly garbled
("rets artois deprauati angolo embiar").

## 1. Is there a text already?

- DECODE "cleartext" images D1018–D1020 (contact sheet): a clear letter page and address leaves, not a decipherment.
- The leaf is a fragment (begins "[m]archesato", ends 137v l. 4 with a flourish); the preceding cipher sheet is not in
  this record. Not paraphrased in Tempesti. Rome's decipherments (Francia 27) not imaged.

## 2. Reading on the image

Because of the transcriber's "?" marks the whole leaf was re-read on crops (137r in six 4-line strips plus close crops of
l. 1; 137v ll. 1–4). The image settles nearly every "?": e.g. l. 1 "8 2 6 7 4 5 2 1 5 0 3 7 1 2 9 1 8 1 6 1 6^. 5" =
"di Saluzo et quello", l. 4 "1 3 2" (principe), not "8 3 2". Names that came out: Saluzo, Angolem[me] (m + 8),
Xantonge (11 = x), Cognach, Metz (20 35 15 12), Bologna, Casimiro, Momoransi (Montmorency), with codes 119 (Queen of
England) and 232 (Navarre). Words the decoder missed: "raferma", "certisime proue", "spero" (4 + 64), "innimico",
"mete conto", "sostenerli".

## Result

Before: 0.524 clean-sentence share (`R27_decryption.txt`). After: 0.526 (237 words; the clerk's spellings and the fragment's short sentences count heavily) on the "## Reading" body. By hand: 2 unread stretches ([…]) and 6
partly carried words in about 230 words; the sentences hold.

## Still open, and why

- 137r l. 13 "onde […]" (19 figures) and the last line of 137v: the image confirms the figures; no word parse found.
  "[?uiuere]" (l. 3) is under an ink blot. The beginning of the letter is missing (fragment): blocker = the leaf is
  not in the record; Rome's decipherment (Francia 27) needs physical access.

## 23 Oct 2026, r2d (Claude Opus 5.5)

Regraded on the v2 measure (research/reading_audit/r2d_score.py, body only, every conjecture and unread stretch a hole): see the profile reading_review for the scores; now read. DECODE attachments re-opened (no decipherment). Image checks this pass (crops in the session scratchpad, r2d/morosini/crops): 137r l. 13 ("onde [...]": 3 7 1 7 1 7 0 3 7 7 2 9 1 8 4 2 5 2 1 0 0 5, no parse fits) and 137v l. 3 (as transcribed); both left open, encipherer's slips.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

The rest of R27 (after r2d's 137r l. 13 and 137v l. 3): each hole located (`research/reading_audit/r2p_holes.py`),
looked at on the image (scratchpad `reread/r2p/crops`), cancellation strokes looked for, parsed (`r2p_parseall.py`).
- 137r l. 6 "li a": "65 | 50 17 212 | 0 35 05 212" = perché li a nela; every figure carries it (a for ha, as written). Filled.
- 137v ll. 1-2 "fauorir[?li]": l. 1 ends "30 21 37 91 00 17 00 5" (fauorire), l. 2 begins "1 7 1 | 1 5 3" (i, è); a long
  stroke runs through "1 7 1 1" on the image, but it may be show-through from the verso rather than a cancellation, so
  the reading is left as it was. Blocker: illegible.
- 137r l. 1 "[m]archesato": the m is not written (21 00 56 45 21 51 91 = arche-sato). "Angolem[me]": "... 50 35 20 8" =
  Angolem. with the abbreviation null 8. Blocker: no-key-material (the m); the second is an abbreviation, not a hole.
- 137r l. 2 "per [?]uno": "64 | 1 | 173 01 91": a lone 1 between per and uno. Blocker: too-short.
- 137r l. 3 "[?uiuere]": "3 17 37 7? [blot] 5 00 5": a blot over one figure. Blocker: illegible.
- 137r ll. 10-11 "[?serate]": "4 | 35 00 35 2 15 153" (s e r e a t e) as transcribed. Blocker: no-key-material.
- 137r l. 20 "poi [?che]": "16" (et) as transcribed. 137v l. 2 "d[i]": "26". Blocker: no-key-material.
Result: 1 hole filled; R27 is now checked on the image throughout; 7 left with blockers.
