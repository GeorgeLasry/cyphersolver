# Re-reading log, R9660 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b34)

## Starting point

Reading audit (22 Oct): "decoded, not read": `reading_r9660.txt` is a working file of sign strings, spelled letters
and open groups in nearly every line; 10% of sentences clean in `docs/_check_reading.py`. Before: no reading file;
working file hole rate 0.28 (`_check_reading.py --file reading_r9660.txt`).

## 1. Is there a text already?

- DECODE R9660 (7 images, ff. 141r-147r): opened again (`IMG_R9660_I45473_P1.jpg` at full size). No attachment,
  transcription or comment on the record (Sept, `decode/view9660.json`). The head of f. 141r is marked
  **"Dup.da"**: this is the duplicate; the first copy is not among the DECODE records.
- **Neighbouring records.** Fetched the record pages of R9656-R9659 and R9667-R9669 (scratchpad): R9656-R9659 are RAH
  9/26 (Lope Hurtado, Sánchez, Adorno), R9667-R9669 are 9/28. The DECODE harvest (`research/catalogue_harvest/decode/
  batch_3.json`) lists exactly seven records in RAH 9/27, R9660-R9666: none holds a decipherment of R9660. The court's
  decipherment leaves of the sister letters (9/27 ff. 190, 342-343, 424-430) are not imaged.
- **Print.** CSP Spain 2 (Bergenroth 1866, archive.org `bub_gb_ZoY9AAAAcAAJ`, OCR grepped 23 Oct): the February 1523
  entries from Salazar A-27 are the Emperor's letter to Sessa of 15 Feb (no. 530) and the Pope's of 2-3 March; no
  Sessa letter of 20 Feb. Not calendared (confirms Sept).
- RAH Biblioteca Digital: returns 403 to automated access (lopehurtado NOTES); not tried again.

## 2. Key values added since the Sept transcription

The sessa1524 key gained about 75 values in passes 16, 17 and b23 (Oct), none of them applied to R9660 until now.
`research/reading_audit/b34_sessa_apply.py` applies them to the (b) lines of `reading_r9660.txt` (read only) and writes
`reading_r9660_b34.txt`; it lists every R9660 context each value lands in. 64 occurrences of 32 groups. Checked per
group:

- Reads in every R9660 occurrence: `net` halla (*si net-r-a disposicion de entender* = hallara), `len` buen-
  (*natura de len-o*), `boz` -io, `var` agora (*var V.Md. lo ha llamado*), `pof` exercito (*la conservacion del pof*),
  `Jam` llam-, `nah` govierno (*su nah baste para sostener el mundo*), `leg` mucho (*el papa ha sentido leg*), `bun`
  visorrey (*el bun con la compañia*), `lin` necesidad, `hut` primer (*ni quiere ser el hut-o ni … el ultimo*).
- Does not read in R9660 at every occurrence (left open for R9660, value kept in sessa1524): `cas` tien- (7: fits *el papa
  cas*, not *Alberto cas*), `rac` dize (5: fails in *con-se-r-va-r … rac*), `sir` supli- (4: fails in *lo sir se n*),
  `le` me (*[le] y t-a-e-a-p-a-r-c-u-a*: the line is garbled), `nuf` gente, `foh` ha.
- No key value adopted or changed in this batch (none could be checked against a decipherment).

## 3. Census and the paragraph that reads

`research/reading_audit/b34_sessa_holes.py` on `reading_r9660_b34.txt`: 436 segments (runs between `/` marks), 2,225
words; **open groups and queried letters: 472 (hole rate 0.21; 0.24 counting tentative values as open)**; 41% of the
short segments have no hole. Beyond the code groups, many spelled runs do not make words as transcribed
(*t-a-e-a-p-a-r-c-u-a*, *a-en-c-e-z-a*, *p-r-u-n-t-o*), so part of the residue is transcription, not key.

f. 141r, first cipher paragraph, re-checked against a full-resolution crop: the transcription holds sign for sign; with
the new values it builds sentences with about one hole in six words (`R9660_reading.md`, English `R9660_en.md`).
Word-by-word: every unbracketed word is a known group, spelled letters, or clear text (Notes of the reading).
Look-alike letters: none chosen in this paragraph.

| | before | after |
|---|---|---|
| reading body (f. 141r paragraph only), b17 plain | — | 0.273 (3/11) |
| same, HOLES=1 | — | 0.727 (8/11) |
| whole decode, hole rate | 0.28 | 0.21 |

## Result

**Kept decoded, not read.** One paragraph builds sentences; the letter as a whole has a hole every fifth word.

## Open (blockers)

- About 100 code groups (472 occurrences), most once or twice, none attested in a deciphered Sessa page: blocker:
  no-key-material (the code is not alphabetical, so no bracketing; pass 17).
- The court's decipherment of this letter or of its first copy, if it survives, is in the RAH volume, not imaged:
  blocker: needs-physical-access.
- Spelled runs that do not form words as transcribed (about a third of the remaining holes): blocker: not-attempted
  (a sign-by-sign re-transcription of ff. 141v-146v at full size, as done here for f. 141r).
