# Re-reading log, Espagnol 318 no. 92 (ff. 116r-v) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b26)

## Starting point

Reading audit (22 Oct): "decoded, not read". `f116_reading.md` is a line table (transcription and gloss per line,
three passes of 21 Sept); ll. 8-11, 16, 18-21, 26-31, 34 of f. 116r keep open codes and unplaced letter runs.
Fix asked: re-read those lines on the full scans and write a running text with a translation.

## What was done

1. **Existing text?** No DECODE record of this letter (harvest searched for Espagnol 318 / Gonzalo / Suárez: none).
   The later interlinear glosses on f. 116r ll. 8-16 are already used (`ct92_glosses.txt`); Tomokiyo's commented-out
   partial reading of ll. 6-7 already used; no printed clear copy (CODOIN, Zurita, Sanuto, BRAH Noticias searched in
   September). **Key in the holding archive:** the *Cifra general* manuscript, RAH 9/15 ff. 7-9 (Salazar), is not in
   the RAH digital library (searched again 23 Oct: no hit); Galende's printed plates are the only key.
2. **Images.** `full/f116r.jpg`, `full/f116v.jpg` from the main checkout are already the Gallica maximum (4155 x 5322;
   the manifest gives the same size), so no higher resolution exists. Strips cut with
   research/reading_audit/b26_strips.py; ll. 8, 9, 21, 30, 31 re-read on them.
3. **Codes re-checked against Galende's printed values** (`keys/cifra_general.txt`):
   - `zems` = *Ostia* fits: "quando el me llamo para el cerco de Ostia" (Gonzalo took Ostia for Alexander VI in 1497).
     The September notes listed `zems` among the codes that contradict the plates; it does not. Adopted.
   - l. 21 opens with `vog` (*acatamiento*, as on l. 11), not the letter run O S S Y.
   - `vur` = *ciudad* and l. 32 *…rachina*: "ciudad … [Ta]rachina" (Terracina), flagged (signs between unread).
   - `xob` (*Certificacion*), `zeb` (*Malta*), `zer` (*Ochocientos*), `zog` (*Maravilla*), `bog` (*Rey de Portugal*),
     `bue` (*Quanta*) still do not fit in context; left as codes.
   - l. 8: `boe` = *Quanto*, `bit` + I A = *seria*: "que esta quanto seria", read as printed.
4. **Running text** `texts/f116_running_reading.md` written from the line table with these changes, words carried by
   neither figures nor glosses bracketed, doubtful values `[?word]`, unresolved codes as `[code]`. English
   `texts/f116_en.md` with the same holes. Value changes in `texts/f116_corrections.tsv`.
5. **Look-alike alternates.** No new letter chosen between look-alikes in this pass; the line table's own choices
   (the q-shaped N vs the reversed-9 S, `zer` read as `zec`, `zap` as `zag`, `bac` as `vac`) are unchanged and listed
   in `../f116_reading.md`.
6. **Score** (b17_score.py, es, reading body): 0.604 (29/48); explicit holes (HOLES=1) 0.792 (38/48). Before: a line
   table, not scored as a running text.
   Reader's judgement: the clear opening and the stretches on the harbours (ll. 21-27), Ostia and Garcilaso (ll. 29-
   36) and the verso hold; ll. 8-14 (the conditions: [xob], [zeb], [?fablara], [zer]) and ll. 18-21 (the ports held by
   Venice, [bue] twice, unread runs) do not build sentences. The plain figure reaches the bar only because the clear
   passages make up a third of the text.

## Result

Kept *decoded, not read*: the clean-sentence share is at the bar but the sentences of ll. 8-14 and 18-21 do not hold.
Partial running reading and translation written.

## Open, with blockers

- Codes `xob`, `zeb`, `zer`, `zog`, `bog` (x3), `bue` (x2): **needs-physical-access** (the key manuscript RAH 9/15
  ff. 7-9, not digitised; Galende's plates misprint some values).
- Letter-sign stretches of ll. 11, 18, 20, 27, 28, 31-32, 34, 36 and f. 116v l. 10: **illegible** (the q-shaped N and
  the reversed-9 S are not separable at the Gallica maximum, 4155 px).
