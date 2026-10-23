# Re-reading log, R40 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R40_decryption.txt` (DECODE D1706, KaJo, May 2016, Meister no. 40):
clean-sentence share 0.619, hole rate 0.117.

## 1. Is there a text already?

- DECODE "cleartext" images: D1064 = the address leaf ("Dup.ta Blois 8 Decembre … Cardinale Montalto"), D1065–D1066 =
  the covering letter in clear (f. 292, Blois 8 December 1588). Not decipherments.
- 293r: clear docket "dup.to di li 8 [dicembre]": this is the duplicate.
- Francia 27 (Rome's decipherments) not imaged.
- Tempesti not used for this letter (nothing taken from it).

## 2. Decode and repairs

- Batch decoder, scratch variant `dec2.py`, hand re-parsing with `fit.py`, as R32.
- New observation: sums are written in plain figures closed by a null 8 ("1 5 8 milia" = 15 milia, "5 0 0 8 milia",
  "3 0 0 8 milia"); the decoders had turned them into letters ("emilia", "norini"). "oto milia" is spelled out
  (8 9 1 5 1 9 1, with 8 null).
- Names carried by the figures: Macone (Mâcon), Momiliano (Montmélian), Borgo in Bresa, Fifer (Pfyffer), Basompier,
  Mirone, d'O, Umena, Guisa; undotted codes 129 196 (duca di Sauoia), 146 (danaro), 129 (duca di Guisa).
- Spurious dots: 535 and 074 on 293v l. 1 ("se li Stati").
- Failures: "longhi" (293r l. 8) only with a stray figure; the name after "Lanzi con" (f r e c h, twice) not
  identified; "monsig. di c e n a g l i … a capo dele sue finanze" not identified; the verb in "che ne … uenire".

## 3. Image checks

None decisive (corroded leaves); all corrections `figures` / `figures+context`.

## Result

Before 0.619 → after 0.61 clean-sentence share on the "## Reading" body (hole rate 0.117 → 0.123): the checker scores
the reading no higher because of the names (Macone, Momiliano, Bresa, Fifer, Basompier, Mirone), the plain-figure
sums and the clerk's spellings; read by hand the before text has garbles in most lines ("emilia suizeri di tomi il
icnania", "russe rma oppor", "norini") and the after text carries every sentence. Holes: 8 unread stretches […] and 6
partly carried words in about 480 words. Grade B (several figure-context corrections; two names unidentified).

## Still open, and why

The opening (293r l. 2, previous sheet missing), the name after "Lanzi con" (twice), "senza … danari" (293r l. 15),
the body offering money "et il …" (293r l. 21), the verb at 293v l. 5, 293v ll. 10–11 (probably the Queen Mother),
293v l. 19 (noun after "risolutione dela"), the minister dismissed (293v l. 21), the closing (294r l. 8). No parse
fits the transcribed figures; the image cannot be compared figure by figure; Francia 27 would settle them.

## Word-by-word alignment (`reread_b00_align.py`, REREAD_BRIEF step 3)

- First run TOTAL R40: 464 words, 1 supplied, 14 partly. Changed Altezza → Alteza and caualli → cauali (single figures); moved the [f. 294r] marker to the page break inside finan-/-ze. The supplied "di" is the undotted 129 196 (duca di Sauoia), whose figures the aligner does not expand; left.

## r2m, 23 Oct 2026 (Claude Opus 5.5): partial image check (IMG_R40 P1, scratchpad)
- 293r l. 15: the stretch after "esendoui" is crossed through on the page with looped strokes (a cancellation, one
  blot); the figures under it are those transcribed. Read through the strokes: 56 … senza (54 35 01 12 21) 2 191 76 70
  91 56 146 = "che si oferisce senza [a] o con poche danari": reading now "senza [?o con poche] danari" (bracketed
  because the figures stand under the cancellation strokes).
- 293r l. 21 "et il […]": "7 2 2 1 2 0 3 5 1 5 1 7" sits between two cancelled stretches (looped strokes over "1 7 1 0
  2 1 0 1 7 1 5 0" and "6 7 5 4 5 9 1 0 0 1 3 5"); no parse; kept […] (the cancellation makes the figures uncertain).
- Not checked in this pass: 293r ll. 2, 5, 8, 10, 19; 293v ll. 5, 10-11, 19, 21; 294r l. 8. R40 is not counted as done.
- Finding for the remaining records: some holes are cancelled stretches (crossed through by the encipherer) that
  DECODE's transcription gives as ordinary figures; each hole should be looked at for cancellation strokes.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

The rest of R40 (after r2m's 293r ll. 15 and 21): each hole located (`research/reading_audit/r2p_holes.py`), its line
looked at on the image (scratchpad `reread/r2p/crops`), cancellation strokes looked for (besides r2m's two looped
cancellations on 293r, the dark strokes over 293r ll. 8-10 and 293v ll. 10-21 are show-through), the figures parsed
(`r2p_parseall.py`).
Filled:
- 293v l. 21 "monsig. di Cenagli": "25 35 01 21 40 50 17", every letter carried (was "[?Cenagli]").
Left, with blockers:
- 293r l. 2 "[…] N S": "7". Blocker: too-short.
- 293r l. 5 "confini dela [?Sauoia] et dela": "1 9 6". Blocker: no-key-material.
- 293r l. 5 "dela Bresa [?ui] erano intorno": "8 1 7". Blocker: no-key-material.
- 293r l. 8 "prouisioni dopo [?longhi] discorsi fu": "5 0 9 1 0 1 4 0 5 4 1 7 1" (best parse "longesi"). Blocker: no-key-material.
- 293r l. 10 "milia Suizeri [et] di oto": "(none)". Blocker: nothing written there; no-key-material.
- 293r l. 10 "Lanzi con [?Frech] et di": "3 0 1 3 5 2 5 1 4 8" (best parse "unech"). Blocker: no-key-material.
- 293r l. 19 "de Lanzi [?Frech] et con": "3 0 1 3 5 2 5 1 4 8" (best parse "unech"). Blocker: no-key-material.
- 293v l. 6 "che ne […] uenire che": "3 0 3 7 1 9 1" (best parse "fuo"). Blocker: no-key-material.
- 293v l. 10 "è uenuta […] ho ben": "8 1 7 3 7" (best parse "iu"). Blocker: no-key-material.
- 293v l. 11 "ben ritrouata […] deto le": "1 161^. 6". Blocker: too-short.
- 293v l. 19 "risolutione dela […] S M": "1 4 3 1 7 1 5 0" (best parse "huil"). Blocker: no-key-material.
- 294r l. 7 "Di quello [che] sucederà non": "(none)". Blocker: nothing written there; no-key-material.
- 294r l. 8 "tenerla auisata […]": "167^. 4 7 9 2 2 7 9 0 0 5 5 5 4 7 9 7 166^. 9 4 7 2" (best parse "[u.s."). Blocker: no-key-material.
Result: 1 hole filled; R40 is now checked on the image throughout; 14 left (with r2m's two), each with its blocker.
