# Re-reading log, R992 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b12)

## Starting point

Reading audit (22 Oct): decoded, not read. read/R992.txt held the key decode as a syllable stream with unkeyed groups;
the gist in NOTES was a summary of it, not a reading.

## What was done

1. **Is there a text already?** No. The DECODE record (fetched again with the project cookie,
   research/reading_audit/b12_fetch.py) carries only the page images and DECODE's digit transcription; the cipher pages
   have no margin or interlinear decipherment (the ten margined letters of the series do), and no clear copy, minute
   or printed edition is known (NOTES, 19 Sept). The sibling series Ronquillo 1676 shares the key but not these letters.
2. **Read on the key decode.** read/R992.txt (frozen key.json) printed token by token per cipher line
   (research/reading_audit/b12_bal.py) and segmented into Spanish words by hand. Second values that hold across the
   letters were used and listed in the reading's alignment notes: 63 = s as well as no (los, demás, sus), 77 = t
   (no-so-77-ro-s nosotros, a-77-ra-he-r atraer), the r-sign = stra/tra (nue-r nuestra, tr-r-r tratar), 69 = ru
   (prudencia, prudente), 116 = carta (a margined letter's decipherment).
3. **Images** (IMG_R*_P*.png, 1616 px greyscale scans, kept in the scratchpad only) checked at the breaks; corrections
   that changed a reading are in R992_corrections.tsv (R992 l. 10: 42 vi, not 48, giving "resolución violenta").
4. **Result:** read/R992_reading.md, a partial reading with every unread stretch marked, English read/R992_en.md.
   _check_reading.py on the reading body: 0.29 (5/17 sentences clean). Below the 0.60 bar: the letter stays decoded,
   not read.

## What stays open and why

- Groups with no value in the key (rare 2-3 digit codes and signs: see the alignment notes): no key material; they
  occur once or twice in all fourteen letters and none falls in a margined letter.
- Stretches where the homophones do not segment into Spanish even with the second values above; the images at 1616 px
  do not settle the doubtful figures (several are struck or overwritten). A better image (the originals at the AGR,
  Brussels, SEG 2559) would be the next step.

## Failures

- The idea that "05 n+" opens a sentence ("para ...") is wrong: it is a start/end marker (both ends of R992 and R996).
- R998 l. 7: tx/ has "46 u 13 48 58 23" (de a do lo r); the image shows an H-like sign for u. Neither reading
  segments; left open.
