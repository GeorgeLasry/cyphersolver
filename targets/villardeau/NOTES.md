# De Villardeau (Holstein letter, signed on p125); testament memorandum anonymous → Unestablished, Undated selected sheets; Russian-correspondence dossier, 1725–1730, BnF Clairambault 531 — testament and Holstein marriage

Status: no write-up of our own (result by George Lasry, presented on docs/villardeau.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 531 — testament and Holstein marriage): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 6/6 pages transcribed; 5/5 cipher pages deciphered
- Ciphertext-only: No
- Sender: De Villardeau (Holstein letter, signed on p125); testament memorandum anonymous
- Recipient: Unestablished
- Date: Undated selected sheets; Russian-correspondence dossier, 1725–1730
- Key: 214 code assignments: 44 letter codes, 170 in nomenclature; 43 corresponding offset pairs
- Ciphertext: 1,248 elements, 1,237 identified (99.1%)
- Contents: The Czarina’s disputed will and succession; the Holstein wedding and confidential comments on the duke’s reputation and ability to produce heirs.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 531 — testament and Holstein marriage
Contents: The Czarina’s disputed will and succession; the Holstein wedding and confidential comments on
the duke’s reputation and ability to produce heirs.
6/6 pages transcribed; 5/5 cipher pages deciphered
Ciphertext-only: No
Sender: De Villardeau (Holstein letter, signed on p125); testament memorandum anonymous
Recipient: Unestablished
Year: Undated selected sheets; Russian-correspondence dossier, 1725–1730
Key: 214 code assignments: 44 letter codes, 170 in nomenclature; 43 corresponding offset pairs
Ciphertext: 1,248 elements, 1,237 identified (99.1%)
Interlinear plaintext: Historical interlinear plaintext on pp77, 79, 81 and 123–124.
Gallica Testament — p77
Gallica Holstein — p123

Excerpt and Translation
Excerpt
p124
Veue d’egayer ma lettre, mais parce que je sçais qu’il est important qu’un ministre sache si un
prince qui aspire à une couronne est en estat d’avoir des successeurs.
Translation
The purpose is not to enliven my letter, but because I know it is important for a minister to know whether a
prince who aspires to a crown is capable of having successors.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9000658k/f47.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b9000658k/f72.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9000658k/f73/full/1400,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p124_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p125_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9000658k/f73/full/1400,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: p124 (canvas 73): clear "Veue degayer ma lettre mais parceque je scais" then interlinear over 3 code rows "quil est important quun ministre sache si un prince qui aspire a une couronne est en estat davoir des successeurs" = his excerpt; signed De Villardeau on p125
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Mentions Campredon ill at St Petersburg, so 1725-26 (Holstein wedding 1725). Interlinear present on the cipher pages; 99.1% identified.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: Lasry's excerpt written out alone as lasry_excerpt_reading.md (the report page had been scored): plain 1.0. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/52_clairambault-531-testament-and-holstein-marriage.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/`. The page shows it at the top.
Measured: whole text 0.997 (v10_relabel.measure); deciphered passages alone 0.993. His report: 6/6 pages transcribed, 5/5 cipher pages deciphered; 1,237 of 1,248 elements identified. Outcome: read. He translates only the excerpt (`lasry/report/translation_excerpt.md`); no full translation.
