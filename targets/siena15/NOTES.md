# Siena no. 15 — Mario Bandini at the imperial court, Innsbruck, 4 January 1547 (DECODE R4803)

Status: read in part (75 of 240 signs), key partly recovered from ciphertext-only by George Lasry with CTTS and Claude Opus 5.5. Contributed result, filed here 18 Oct 2026.

Status: in progress (20 Oct 2026): George Lasry's partial reading is filed; 165 of 240 signs and the code words buf/abs/som/Za are workable from his CTTS transcription and the clear context, not yet retried here.

Archivio di Stato di Siena, Concistoro 2308, fasc. 2, no. 15; DECODE
[R4803](https://de-crypt.org/decrypt-web/RecordsView/4803) (Concistoro_2308_57), catalogued "1500-1599", no status.

## Source

George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (17 Oct 2026), consolidated report sent by email to
Daniel Bourdeau, pp. 28-30, section G. Quoted whole in [`lasry_report.md`](lasry_report.md); key figure
[`key_lasry.jpg`](key_lasry.jpg). His partial reading and translation are not re-edited here.

## What the report gives

- **Status (Lasry):** partially read (75 / 240 signs), by Lasry with CTTS and Claude Opus 5.5 (crib guessing and dragging).
- **Ciphertext:** 240 cipher signs plus three Latin-letter code tokens, 8 lines of P2 and 6 of P6, eleven short
  passages inside the clear Italian of an eight-page letter.
- **Key:** about 65 distinct signs (71 transcription classes, several probably merged variants): homophonic alphabet of
  Greek-like and invented signs, two or more signs for e, n, o, i; Latin-letter nomenclator tokens (buf, abs, som, Za),
  each followed by a bar with three dots; probable nulls; no word dividers; about 30 signs unknown.
- **Contents:** Mario Bandini, Sienese orator, to the Signori of Siena, Innsbruck ("Eltspruch"), 4 January 1546
  Sienese style = 1547 (after the Schmalkaldic campaign of autumn 1546). Piergiovanni Salvestri at Innsbruck with the
  Florentine orator; the order of the Nove; in cipher, an occasion to be used, discord, someone who "redusse ale mani"
  of a coded party; on P6 a minister (Granvelle?) warning that a fire would be kindled in a coded place, then in clear
  Latin that princes would pay 100,000 crowns; refused gift; Sienese vases "all'antica" for Burgundy via Figueroa.

## Disagreements with the repository

- The siena1421 inventory read the date line as "Di Hellsprunth(?) alli 29 di X.bre MDXLVI" with a PS of 3 Jan and
  4 Jan 1546 s.s.; the report dates the letter Innsbruck, 4 January 1547 ("Eltspruch"). The 29 Dec / 3 Jan dates of
  the survey are not in the report; a question for George.
- Survey count 229-230 cipher signs; the report's 240 (CTTS) is used.

## One key, one entry

Compared sign by sign with the key figures of no. 17 and R4794 (same heading G of the report): every shared shape has
another value (Λ = c here, e in R4794; θ = e here, z in R4794; Ш = n here, i in no. 17, o in R4794), and the
systems differ (Latin-letter code words here; a "che" sign in no. 17; a dotted pigpen grid and number codes in R4794).
A different key: its own entry. Table and reasoning in [`siena17/NOTES.md`](../siena17/NOTES.md). The filed key
R4764 ("Cifra con m. Bernardino Buoninsegni oratore a S. M.tà"), the survey's candidate, was inconclusive.

## Project's earlier attempt (siena1421 survey, 24 Sept 2026)

Agents K and L transcribed the P2 and P6 runs (`project_attempt/no15.txt`, `no15v.txt` = verified version,
`no15.tok`; moved here from `targets/siena1421/transcripts/` on 18 Oct 2026) and compared R4764; closed as too short.
Not used in George's reading.

## Files

- `lasry_report.md`: the report's section, verbatim; `reading.txt`, `translation.txt`: his partial decipherment and translation, verbatim.
- `key_lasry.jpg`: his key figure; `key.md`: the same key as a table (70 classes incl. code words, 243 occurrences = 240 signs + 3 code tokens).
- `project_attempt/`: the project's 24 Sept transcriptions (not used).

## Remaining gaps

- 165 of the 240 cipher signs on P2 and P6 - blocker: open-codes; George Lasry's own partial reading, about 30 signs without a value and many readings marked uncertain. Workable (long clear context, transcription exists), not retried here.
- code words buf (3), abs (3), som (1), Za (1) - blocker: open-codes; no key in the busta gives them; R4764 inconclusive.

## Escalation

- [x] siblings: every piece of fasc. 2 opened; no. 17 and R4794 compared sign by sign: different keys.
- [x] clear-pages: the clear text of the letter is the context George used; no decipherment on the sheets.
- [x] known-keys: R4764 (Buoninsegni, orator to His Majesty) compared on 24 Sept: inconclusive.
- [x] print: none known for this letter (Cantagalli 1962 and Hook 1979 cited by the report for context only).
- [n/a] key-rebuild: the key is George Lasry's; extending it needs his CTTS transcription (71 classes), which is not in the repository (asked for).
- [n/a] retry: no key extension was made here, so nothing to rerun; a question for George.
