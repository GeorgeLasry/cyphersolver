# Re-reading log, R9241 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b19)

## Starting point

Reading audit (22 Oct): two entries, both "decoded, not read": Beck's literal layer (PR #18) had connected clauses in
passages B and D but gaps in A and C; Nur's 1565-key rendering (PR #21) was dictionary fragments between ellipses.

## 1. Is there a text already?

- DECODE R9241 re-fetched with the project cookie (`research/reading_audit/b19_fetch.py`): two images, no attachment,
  no transcription, no comment; status "Non-decrypted". Both images opened: Forbes's copy has only the cipher passages
  (1)-(4) under the heading naming the Queen Mother, de Foix and 15 Jan 1563; no interlinear or marginal decipherment.
  The neighbouring copies on the same pages (ff. 148r: passages (15)-(24) of a Coligny letter, R9238/coligny1563; f. 149
  foot: Throckmorton to the Queen, 3 Jan 1562/3, a different cipher) are other letters.
- Print and calendars were searched before (NOTES: Forbes ii, CSP Foreign vi, La Ferrière i-ii): not found.

## 2. Re-reading

- Base: Beck's sign transcription and key v13 (`texts/beck_transcription.txt`, `beck-preliminary/data/key.json`), the
  only transcription with a key that yields running French. Added the 1565 cipher's word signs (key_k0.json, independent
  of this letter) for the numbers Beck left open: 10 dict ("du dict"), 26 bien ("seroit bien aise", "feiz ie bien
  entendre", "dont ie ueoi bien", "ueti bien que"), 34 tant ("peust auoir tant de faueur", "ia tant escript"), 40 faict
  ("aiant faict"), 70 toute ("de toute ce qui"), 82 ceulx, 37 me/car. Each fits every occurrence. f = u twice (K0: f =
  l/u/s): "aussi" (D6), "roiaulmes" (A18) (`R9241_corrections.tsv`). Decoder `research/reading_audit/b19_foix_decode.py`,
  output `R9241_decode.txt`.
- Every trouble spot looked at on the photographs (line strips cut with Beck's line coordinates, scratchpad only): A2
  "prolizgnaulx", A4 "laquelmme ... cgnoistre", A8 "eaulx [20]ancemens de la iueie" (Beck's 20 is written "zo"), A12
  "in sentira", A14-A16 "uoulrigniuir" and "desineramoii", B1 "langai[SWASH]e a[CAP_D]ompain…", B3 "cresin", C1
  "prou[N]ice", C2 "aie", D0 opening "37 Xp ꝉ6 X 70 30 10", D6-D8 "aduertdrez", "r[N]ert", "Marissriuere". The signs
  are as Beck transcribed; the problems are values, not labels. No label was changed.
- New readings found: A8-A10 "et ioue durant noz trouble [:] le personnaige que vous scauez assez" (the colon and 93 =
  le; Beck had split the clause), "aiant faict les [?beaulx] [?auancemens] de la [?guere]" (40 = faict from the 1565 key),
  B1 "langaige accompaignee" (partly carried), D0 "[?car] ... toute est dict, ie n'en espere riens".
- Failures: A2, A14-A16, B3, D7 and the closing name do not build words under Beck's values, the 1565 values or Nur's
  fitted values (2 = i/l, ny = n/z, z = i/p, # = i/g tried at each place). No value was adopted that does not hold
  across the letter.

## 3. Reading and scores

`R9241_reading.md`, `R9241_en.md`. Word check (`b19_wordcheck.py` against the passage literals): every unbracketed word
is carried. Clean-sentence share of the reading body:

| measure | share |
|---|---|
| `_check_reading.py` (fr) | 0.361 |
| `b17_score.py` LANG_=fr | 0.391 (9/23) |
| `b17_score.py` HOLES=1 (explicit holes only) | 0.609 (14/23) |

The French list does not know the 1563 spelling (uisitation, actendoie, scai, uerez, esperit), but even counting only
explicit holes the share is at the threshold, and the long sentence of passage (1) breaks twice in the middle. Below the
bar on the checker (0.36, against 0.47-0.56 for the French documents kept unread so far), so R9241 stays "decoded, not
read", with this reading kept as the partial reading. Blocker for what is left: no-key-material (the open signs have no
value in the 1565 chart or in any decipherment of a de Foix letter of 1563; de Foix changed his key in early 1564).
