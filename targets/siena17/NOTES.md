# Siena no. 17 — Bartolomeo Tantucci in the cipher of the Balìa, 25 August 1528 (DECODE R4805)

Status: read in part; key recovered from ciphertext-only by George Lasry with CTTS and Claude (about 85%). Contributed result, filed here 18 Oct 2026.

Archivio di Stato di Siena, Concistoro 2308, fasc. 2 ("Lettere in cifra"), no. 17; DECODE
[R4805](https://de-crypt.org/decrypt-web/RecordsView/4805) (Concistoro_2308_59), catalogued "1500-1599", no status.

## Source

George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (17 Oct 2026), consolidated report sent by email to
Daniel Bourdeau, pp. 25-27, section G "Sixteenth-century Sienese ciphers". His section is quoted whole in
[`lasry_report.md`](lasry_report.md); his key figure (signs cut from the manuscript) is [`key_lasry.jpg`](key_lasry.jpg).
His reading, translation and dating are not re-edited here.

## What the report gives

- **Status (Lasry):** solved about 85%; the opening words of two points and one phrase remain uncertain. 15-17 Oct
  2026, George Lasry with CTTS and Claude: key recovered by Claude (frequency and contact analysis, isomorphs, cribs).
- **Ciphertext:** 282 cipher signs in 8 lines (CTTS lines 5-12 of P1), set in a clear frame (heading, salutation,
  'In prima', 'Secundo', 'et', 'quando', 'Terzo', closing, signature, endorsement).
- **Key:** 41 distinct signs; homophonic substitution without word division, up to five signs per vowel, homophones
  for the frequent consonants, every double letter with two different signs, the ordinary "che" abbreviation as a
  cipher sign; four signs unknown.
- **Contents:** Bartolomeo Tantucci to messer Antonio del Vescovo, rector of the cathedral, absent from the Balìa;
  Sarteano(?), 25 (or 20) August 1528. Three matters: bishoprics promised to "the nephews" by "el Mustetto"(?); the
  Cardinal of Naples (Vincenzo Carafa?) and Pitigliano; the "Otto"(?) wanting to constrain Pitigliano. "Parlo breve et
  in substantia perché la cifra vuol così." Endorsed "questa cifara è quella di Balìa".

## Disagreements with the repository

- The siena1421 inventory (24 Sept) had "20 Aug 1528, to Bartolomeo Tantucci?" and the place "Siena(?)". The report
  reads Tantucci as the **sender** (signature "Deditissimo Bart[olome]o Tantucci"), the addressee as Antonio del Vescovo
  (address on P2), the place as Sarteano(?) and the day as 25 (or 20). The report is followed.
- The project's survey closed no. 17 as "too short" for ciphertext-only; George's ciphertext-only recovery shows it was not.

## One key, one entry: the three section-G keys compared

The report's contents page says "Pieces under one heading share a cipher key", but heading G ("Sixteenth-century
Sienese ciphers") holds nos. 17, 15 and 5? and each piece has its own key section. The three key figures (report
pp. 25, 28, 31) were compared sign by sign on 18 Oct 2026 (value, with the occurrence count from George's figure):

| shape | no. 17 (R4805) | no. 15 (R4803) | no. 5? (R4794) |
|---|---|---|---|
| square-bottomed U (Ш) | i (13) | n (10) | o (1); with dot d |
| bold b / h | n (21) | o (4) | - |
| Λ | - | c (14) | e (11); with dot o |
| θ / Θ | - | e (9) | z (1) |
| ÷ | o (8) | a code mark / d (with bars) | - |
| 9-shape | a (34) | h (3) | - |
| 3 | r (17) | - | - |
| 4 | s (13) | - | - |
| C (bold) | t (15) | - | a (3), e (1) |

Every shape the keys share has a different value, and the systems differ in kind: no. 17 is a digit-like cursive
alphabet with a "che" sign; no. 15 a Greek-like alphabet with Latin-letter code words (buf, abs, som, Za); no. 5? a
pigpen-like grid where a dot shifts a frame to another block of four letters, with a number nomenclator (26, 44, 67,
74). **Three different keys, so three entries:** this one, [`siena15`](../siena15/NOTES.md) and
[`siena5`](../siena5/NOTES.md). Heading G groups the pieces by period, not by key (as heading D says outright:
"one key each").

## Project's earlier attempt (siena1421 survey, 24 Sept 2026)

Agent A transcribed no. 17 from the DECODE photographs (`project_attempt/no17.txt`, `no17.tok`, moved here from
`targets/siena1421/transcripts/` on 18 Oct 2026). Homophonic annealing failed and filed keys R4760, R4768, R4778 did not
fit; the piece was closed as too short. Nothing of that attempt is claimed in the reading, which is George Lasry's
from his own CTTS transcription.

## Files

- `lasry_report.md`: the report's section, verbatim; `reading.txt`, `translation.txt`: his decipherment and translation, verbatim.
- `key_lasry.jpg`: his key figure; `key.md`: the same key written out as a table (shape names, values, his counts: 41 signs, 282 occurrences, matching the report).
- `project_attempt/`: the project's 24 Sept transcription (not used).

## Remaining gaps

- opening words of the second and third points and one phrase ("lco[??]stren[?]niare"), about 15% of the 282 signs - blocker: open-codes; uncertain in George Lasry's reading, workable from his CTTS transcription and the image, not retried here.
- "el Mustetto", the Cardinal of Naples (Carafa?), the Countess, the "Otto", the place Sarteano(?) - blocker: open-codes; historical identifications open in the report.

## Escalation

- [x] siblings: every piece of fasc. 2 opened (siena1421 survey); nos. 15 and 5? compared sign by sign: different keys.
- [x] clear-pages: P2 is the address only; no decipherment on the sheet.
- [x] known-keys: R4760, R4768, R4778 tried on 24 Sept; the "cifra di Balìa" not identified among the filed keys.
- [x] print: none known (siena1421 survey: Meister 1902, the 1952 inventory).
- [n/a] key-rebuild: the key is George Lasry's; extending it needs his CTTS transcription, which is not in the repository (asked for).
- [n/a] retry: no key extension was made here, so nothing to rerun; a question for George.
