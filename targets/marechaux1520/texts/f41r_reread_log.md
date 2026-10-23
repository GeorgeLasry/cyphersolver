# Re-reading log, f. 41r (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b30)

## Starting point

Reading audit (22 Oct): "decoded, not read", excerpt only: Lasry's decipherment of f. 41r exists only as red letters
drawn on three overlay crops (cryptiana GL.htm), with no text of it in the repository. Clean-sentence share before: no
text (0.00).

## What was done

1. **Every file on the DECODE record** (R2322; main checkout `targets/marechaux1520/decode/`, git-ignored): P1 = f. 41r
   (cipher, 3424 x 5240), P2 = f. 41v (cipher), P3 = f. 42r (blank), P4 = f. 42v (endorsement "Dupplicata des articles
   envoyez par messrs les marechaulx françoys au roy"); s1-s4, v*/r_band* are earlier crops of the same. No DOC_* text,
   no attachment beyond the images (`rec2322.htm`). No contemporary decipherment on the record.
2. **Existing text?** Yes: George Lasry's decipherment of f. 41r (24 May 2022), on the overlay crops
   `GL_BnFfr3081_f41_decipher1-3.png` (main checkout `prior/`). The three crops overlap by one cipher line each (the
   top unlabelled row of crops 2 and 3 is the last labelled row of the crop before), so together they cover the four
   heading lines and all 31 body lines with no gap. Transcribed at 3x-5x zoom, line by line, to
   `f41r_lasry_overlay.txt`.
3. **Figures checked** on P1 at native resolution (crops in the session scratchpad, research/reading_audit/b25_crop.py
   equivalents) at seven places, `f41r_corrections.tsv`:
   - l. 7 end: the sign before "= ⟂ꝰ" (A R) is the Rg sign with its descender, the P sign adopted on f. 41v in every
     occurrence; Lasry's overlay letter D is its look-alike. "par armes" (overlay "DAR"). Adopted (holds on f. 41v).
   - l. 1 end: the sign is the Rc shape (D) without the descender; the sense needs "par longue experience". Kept as
     [?par]: **1 letter of the reading rests on a look-alike alternate.**
   - l. 2 end "DE DOVM|AGE": the same Rc sign reads D here (de doumage), so Rc = D is not changed in the key.
   - l. 7 "LVNGAVOVLV" = "l'ung a voulu" (figures CON b ш q ꝫ d ≿ = ꞩt ⅁ ...), not "l'un ga".
   - l. 28 "TEMPSSIESPLORE": the ʃκ pair is two signs (S, I), 14 signs for 14 letters; "si esplore" (éploré, woeful),
     no D needed.
   - l. 13-14: "le siege apostolic / que le siege apostolicque": a repeated phrase, kept with [sic].
   - l. 22 "PACIFISQVE": the sign Lasry lettered S is the P-shaped C sign; "pacificque".
   No key value changed: Lasry's key as amended on f. 41v (Y, P, R, S) applies; nothing new adopted.
4. **Alignment, word by word** with the overlay letters: every word of the reading is a run of Lasry's letters (word
   division and apostrophes added); no word supplied; the one doubtful word is bracketed ([?par]). The f. 41r text ends
   "du roi tres cre-" and f. 41v begins "stien": the "[chre]stien" bracket at the head of f. 41v is now carried.
5. **Score** (research/reading_audit/b17_score.py, LANG_=fr, reading body): **0.429 (9/21)**; explicit holes
   (HOLES=1) **1.00 (21/21)**; `_check_reading.py --file` 0.419 on the whole file. Every unclean sentence fails on 1534
   spellings and names the modern list cannot know (crestiente, disention, cruelement, laquele, oficiers, apartenoit,
   ocupees, debeler, conbatre, conmung, enemi, noustre, chouses, difiles, doner, pencer, puisance, Tornon, Thurc);
   none fails on a hole. Reader's judgement: the sentences hold; it is a coherent preamble (the harm of the princes'
   wars, Campeggio's peace efforts, the Turk and the heresies, all needing the Most Christian King).

## Result

Read from George Lasry's decipherment, figures checked at seven places (grade B: an existing decipherment transcribed
from overlay images, not re-decoded sign by sign).

## Open

- l. 1 [?par]: the figures give D; blocker: illegible (the copyist's look-alike; the image is clear, the sign is Rc).
- The rest of f. 41r is Lasry's letters, not re-decoded sign by sign here (checked at seven places); blocker:
  not-attempted (no break in the sense calls for it).
