# Siena R4794 (unnumbered) — a slip wholly in cipher on pieces of artillery, 16th century (DECODE R4794)

Status: read; key recovered from ciphertext-only by George Lasry with CTTS and Claude (four number codes open). Contributed result, filed here 18 Oct 2026.

Archivio di Stato di Siena, Concistoro 2308, fasc. 2, slip with a faint pencil number "5"(?); DECODE
[R4794](https://de-crypt.org/decrypt-web/RecordsView/4794) (Concistoro_2308_48), catalogued "1500-1599", no status.

## Source

George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (17 Oct 2026), consolidated report sent by email to
Daniel Bourdeau, pp. 31-32, section G. Quoted whole in [`lasry_report.md`](lasry_report.md); key figure
[`key_lasry.jpg`](key_lasry.jpg). His reading and translation are not re-edited here.

## What the report gives

- **Status (Lasry):** solved (the four number codes unidentified). 15-17 Oct 2026, George Lasry with CTTS and Claude:
  transcription by Claude, refined by the author in CTTS; initial key from CTTS cryptanalysis (23 values), corrected
  and completed by Claude with crib guessing and dragging.
- **Ciphertext:** 165 symbols, 160 letter signs and 5 number codes (26 twice, 44, 67, 74), six lines, no clear text.
- **Key:** 35 letter signs plus four number codes. A pigpen-like grid: the alphabet in blocks of four letters, each
  block written with one family of frames (open angles, round arches, square brackets, T-shapes); a dot moves the same
  frame to another block (e, f, g, h without a dot read o, p, q, r with one); a dozen free symbols as extra homophones;
  the numbers a small nomenclator for places, titles and persons; no word dividers.
- **Reading:** "Di alcuni pezzi [d']i artigliaria 44 di 26. Le Signorie Vostre, come so, faranno si governin con
  prudentia, perché ancho 67 ha qualche impressio[n], non è la mente che Vostre Signorie s'intendino col presente 74
  di 26." Two encipherer slips corrected in brackets; the first letter D and the s of impressione rest on single signs.
- **Dating:** 16th century (Tuscan spellings, numbered nomenclator, geometric hand; DECODE 1500-1599); unverified. No
  key in Concistoro 2308 fits it; pigpen-type keys R4776 and R4786 (c. 1530-55) share its style.

## Disagreements with the repository

- **Piece number.** The report calls it "No. 5?". The siena1421 inventory (24 Sept) lists **no. 5 = R4791**, a clear
  private letter to "Maffeo da Siena" (pencil "1460?"), and R4794 as unnumbered ("erased pencil 4/5";
  `project_attempt/r4794.txt` notes a faint "5" in the left margin). Either two sheets carry a 5 or one of the two
  readings of the pencil number is wrong; a question for George. **Settled 18 Oct 2026**: George's email lists R4794 as
  "unnumbered, wrongly attributed by Lasry to No. 5". The page and ledgers now call it R4794 (unnumbered); the
  folder and page slug stay `siena5` so existing links keep working.
- The survey closed R4794 as too short for ciphertext-only; George's recovery shows it was not.

## One key, one entry

Compared sign by sign with the key figures of nos. 17 and 15 (same heading G): a different key (Λ = e here, c in
no. 15; Θ = z here, e in no. 15; Ш = o here, n in no. 15, i in no. 17), and a different system (the dotted frame grid
and number nomenclator are unique to this slip). Its own entry; table in [`siena17/NOTES.md`](../siena17/NOTES.md).

## Project's earlier attempt (siena1421 survey, 24 Sept 2026)

Transcription `project_attempt/r4794.txt` (moved here from `targets/siena1421/transcripts/` on 18 Oct 2026; sign
names W., J, C., P ... with the digits 2 4 6 7) and `homsolve.py` annealing; no key found. Not used in George's reading.

## 20 Oct 2026: his key checked on this project's transcription

`research/siena2308/verify_lasry.py r4794` and `r4794b` (moved from `targets/siena1421/` with the split): his key
table matched by shape and count to the sign names of `project_attempt/r4794.txt` (24 Sept, before his work); our
160 tokens deciphered with his key, without fitting, and aligned with his reading: **134 agree (83.8%)**. His table
has **no H and no R column**, though his reading has h 7 times and r 11 times: our A (alpha, 11 occurrences) aligns
with r every time and our N (∩, 4) with h. With those two values added and nothing else (`r4794b`): **149 of 160
(93.1%)**. So the missing columns are a gap in his key figure, not in his reading (the count question below); worth
telling him. Independent verification of his reading.

## Files

- `lasry_report.md`: the report's section, verbatim; `reading.txt`, `translation.txt`: his decipherment and translation, verbatim.
- `key_lasry.jpg`: his key figure; `key.md`: the same key as a table.
- `project_attempt/r4794.txt`: the project's 24 Sept transcription (not used in the reading; the basis of the 20 Oct check).

**Count question for George:** the report's text gives 35 letter signs and 160 letter occurrences; the key figure shows 31 letter signs (no column for b, h or r) with 143 occurrences, plus the four codes (5 occurrences). The 20 Oct check above finds the h and r signs: our A = r, our N = h.

## Remaining gaps

- number codes 26 (twice), 44, 67, 74 - blocker: no-key-material; the nomenclator is lost and no key in the busta fits the slip.

## Escalation

- [x] siblings: every piece of fasc. 2 opened; nos. 17 and 15 compared: different keys.
- [x] clear-pages: the slip has no clear text and no decipherment.
- [x] known-keys: no key in Concistoro 2308 fits (report); R4776, R4786 similar in style only.
- [x] print: none known.
- [x] key-rebuild: the letter key is complete per the report; the number codes cannot be rebuilt from five tokens.
- [x] retry: 20 Oct 2026, his key run on the project's own transcription (`research/siena2308/verify_lasry.py r4794b`): 93.1% with r and h added; nothing else left to rerun except the codes, which occur once or twice each with no context to narrow them.
