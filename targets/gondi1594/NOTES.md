# Girolamo Gondi → Duke of Nevers and Rethel, 15 May 1594, BnF Français 4700 — Gondi symbol cipher, ff9r–10r

Status: no write-up of our own (result by George Lasry, presented on docs/gondi1594.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 4700 — Gondi symbol cipher, ff9r–10r): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 5/6 pages transcribed; 1 more in part; 3/6 pages deciphered
- Ciphertext-only: No
- Sender: Girolamo Gondi
- Recipient: Duke of Nevers and Rethel
- Date: 15 May 1594
- Key: 54 symbols: 42 letter signs, 4 doubled-letter signs, 8 in nomenclature
- Ciphertext: 1,469 elements, 1,449 identified (98.6%)
- Contents: Negotiations over the Pope’s absolution of the French king, with warnings that the Duke of Sessa was delaying a settlement; references to Savoy and Monsieur de Maisse.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 4700 — Gondi symbol cipher, ff9r–10r
Contents: Negotiations over the Pope’s absolution of the French king, with warnings that the Duke of Sessa
was delaying a settlement; references to Savoy and Monsieur de Maisse.
5/6 pages transcribed; 1 more in part; 3/6 pages deciphered
Ciphertext-only: No
Sender: Girolamo Gondi
Recipient: Duke of Nevers and Rethel
Year: 15 May 1594
Key: 54 symbols: 42 letter signs, 4 doubled-letter signs, 8 in nomenclature
Ciphertext: 1,469 elements, 1,449 identified (98.6%)
Interlinear plaintext: Historical Italian interlinear decipherments accompany the selected cipher lines
on ff9r–10r / PDF21 and23.
Gallica ff9r–10r
Gallica separate PDF94 opening

Excerpt and Translation
Excerpt
f9v, rows 10–13
luogo di queste parti doppa la reductione di parigi non abbiamo auto qui alcuna lettere di
monsieur di reuol ne daltri ne fatta alcuna dimostratione di ralegramento con noi et si ua
dubitando che si sia stato fatto qualche cattiuo uffitio da
Translation
… place in these parts. Since the submission of Paris, we have received no letters here from Monsieur de
Revol or anyone else, nor any expression of congratulations; and there is suspicion that someone has done
us a disservice …
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b90582908/f19.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b90582908/f92.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90582908/f21/pct:0,0,52,100/1400,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p092_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p093_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90582908/f21/pct:0,0,52,100/1400,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f9v rows 10-13 (canvas 21): contemporary Italian interlinear "luogo di queste parti doppo la reductione di Parigi non abbiamo auto qui alcuna lettere di Mr di Revol ne daltri ne fatta alcuna dimostratione di ralegramento con noi et si va dubitando..." = his excerpt
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Only 3/6 pages deciphered though 98.6% of transcribed elements identified. f9r opens in clear to Nevers; Italian.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/37_francais-4700-gondi-symbol-cipher-ff9r10r.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.987 (v10_relabel.measure),
deciphered passages 1.0. His status: 5/6 pages transcribed; 1 more in part; 3/6 pages deciphered. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- ff9r-10r: cipher lines without interlinear (3/6 pages deciphered; 20 of 1,469 elements unidentified); docket [?] - blocker: no-key-material; his status: 5/6 pages transcribed, 1 in part; 3/6 deciphered; italic passages rest on the literal historical plaintext.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the deciphered passages known to this project (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
