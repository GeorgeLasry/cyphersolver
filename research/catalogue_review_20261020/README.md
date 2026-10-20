# Ten open catalogue candidates reviewed, 20 October 2026

**No new cryptanalytic solution was verified.** One catalogue correction is finished:
the three Costabili letters of 1493 are clear Italian, and R1163/R1164 carry identical
photographs. The earlier Costabili cipher correspondence stays open. This pass is not
a claim to have solved ten ciphers, nor an exhaustive attack on these ten entries.

The reviewed catalogue IDs are **348, 350, 351, 352, 353, 354, 355, 357, 358 and 360**.
Selection favoured accessible source material, surviving candidate keys, short passages
that could be screened cheaply, and unexplored siblings. The checkout was isolated from
existing uncommitted work and based on `origin/main` at `0258b8ab5` (82 open entries).

| ID | Candidate | Work in this pass | Result and next concrete step |
|---|---|---|---|
| 348 | Costabili, 1491–93 | Retrieved all 42 photographs attached to the ten records; inspected the three 1493 rectos and versos, the February letter, and the remaining contact sheet; SHA-256 comparison of the March duplicate records. | R1095–R1097 are clear Italian; all four photographs of R1163/R1164 are identical. Six distinct earlier despatches remain open. Transcribe their cipher passages and contemporary glosses; a contact-sheet survey is not a full reading. |
| 350 | Craven to Rupert, 1648 | Retrieved R8447 and its three full folios; inspected manuscript previews. | No reading or new key match established. Transcribe the cipher passages and then test the Add MS 72438 key tables; this full sweep was not performed. |
| 351 | Condé–Barrière, 1654–55 | Retrieved R8395 and R8398 plus the four key photographs on R8405/R8406. Inspected the 18 June letter and key. | R8395's heading is Barrière **to** Condé, not Condé to Barrière. The short June passage has meaningful diacritics; no validated token-by-token reading established. Transcribe those distinctions before applying the 1655 table. |
| 352 | Hyde to Milles, 1659 | Retrieved R4886 and its six photographs and the printed-source page. | The adjacent-name-list/key lead needs separate transcription and the R4887–R4913 keys. Those keys were not downloaded or exhaustively tested here. No new reading claimed. |
| 353 | Ormond to Arran, 1678 | Re-examined Tomokiyo's literal quotation and the rejected trial retained in his HTML comment. | The quotation has 20 numbers: the initial 445/342 plus runs of ten and eight. This is a correction to the catalogue's 22, not a solution. Reconstruct the actual 1678 code rather than accept the rejected 1680 trial. |
| 354 | Catinat, 1702 | Re-examined Tomokiyo's discussion, transcription links and previous key comparisons. | Prior rejected comparisons remain prior work, not new tests here. Obtain the archival signature and a same-key sibling or clear copy; no new reading established. |
| 355 | Durán to San Felipe, 1718 | Retrieved R10181's four photographs and both photographs on each of R10189–R10197. Inspected the cipher, 1718 key and key-sheet contact sheet, including full R10194. | The fetched tables do not supply an established match. A high number alone does not rule out a key (nulls, modifiers and transcription must be checked). Full transcription and group-by-group testing remain to be done. |
| 357 | Brussels intercept, 1660 | Extracted the 21 numbers from Birch's printed text and applied twelve existing transcribed key tables; all outputs retained. | No coherent reading identified among these outputs. Tables include partial reconstructions, so this does not exclude their cipher families. The specimen is too short to accept a contextual guess without independent evidence. |
| 358 | Sirtori, c.1599 | Read Caballero's own 2012 proposal and discussion of its unspecified abbreviation expansions. | His proposal is tentative and does not provide a deterministic complete key. Do not promote it to a verified partial decipherment. A new punctuation-preserving manuscript transcription and withheld-text prediction are needed. |
| 360 | Habsburg sheets, R1579 | Retrieved all nine attached files; inspected I7060, I7066 and an inverted preview of I7068. | Distinct systems appear in the record; no new key recovered. Transcribe I7066/I7068 separately. Do not apply Ernst's separate Piccolominea result as if it solved these sheets. |

## Finished correction

See [`targets/costabili1493/NOTES.md`](../../targets/costabili1493/NOTES.md) and
the [public write-up](https://dbourdeau.github.io/cyphersolver/costabili1493.html).
The writeup skill's ledgers, profile, manifest, explore exclusions and DECODE queue
are updated for this classification result. It is recorded as **not applicable / not a
cipher**, with no cryptanalytic credit or fabricated decipherment.

## Reproduce the source checks

Run from the repository root:

```powershell
python research/catalogue_review_20261020/fetch_sources.py
python research/catalogue_review_20261020/fetch_sources.py records 8405 8406 8447 10189 10190 10191 10192 10193 10194 10195 10197
python research/catalogue_review_20261020/fetch_sources.py images
python research/catalogue_review_20261020/check_evidence.py
```

Authenticated DECODE access needs an existing local session cookie; the fetcher reads
it from the primary checkout without printing or copying it. The ignored `decode/`
cache contains authenticated pages and restricted scans and must never be staged.
`evidence_manifest.json` contains only filenames, byte counts and hashes. Image rights
are not inferred from the ability to download a file. The restricted photographs are
not redistributed.

`brussels_key_screen.json` records the literal outputs, including unknown groups in
brackets. Applying an existing table is a key screen, not a trained statistical solver;
no general claim of unsolvability follows from it. No synthetic-control success or
statistical validation is claimed for an attack that was not run.

## Sources

- [Costabili records R1095](https://de-crypt.org/decrypt-web/RecordsView/1095),
  [R1096](https://de-crypt.org/decrypt-web/RecordsView/1096),
  [R1097](https://de-crypt.org/decrypt-web/RecordsView/1097), and R1162–R1168.
- [Craven R8447](https://de-crypt.org/decrypt-web/RecordsView/8447),
  [Barrière R8395](https://de-crypt.org/decrypt-web/RecordsView/8395),
  [Condé R8398](https://de-crypt.org/decrypt-web/RecordsView/8398),
  [key R8405](https://de-crypt.org/decrypt-web/RecordsView/8405),
  [key R8406](https://de-crypt.org/decrypt-web/RecordsView/8406).
- [Hyde R4886](https://de-crypt.org/decrypt-web/RecordsView/4886),
  [Durán R10181](https://de-crypt.org/decrypt-web/RecordsView/10181),
  [1718 key R10196](https://de-crypt.org/decrypt-web/RecordsView/10196),
  [Habsburg R1579](https://de-crypt.org/decrypt-web/RecordsView/1579).
- [Birch, Thurloe State Papers VII, p.869](https://www.british-history.ac.uk/thurloe-papers/vol7/pp860-869).
- [Tomokiyo, Ormond and Arran](https://cryptiana.web.fc2.com/code/charlesii2.htm),
  [Condé correspondence](https://cryptiana.web.fc2.com/code/louisxiv0.htm),
  [Catinat](https://cryptiana.web.fc2.com/code/louisxiv.htm#SEC9),
  [Habsburg ciphers](https://cryptiana.web.fc2.com/code/habsburg.htm).
- [Caballero's proposal and discussion, 2012](https://ciphermysteries.com/2012/06/14/girolamo-sirtori-cipher-mystery/#comments).
