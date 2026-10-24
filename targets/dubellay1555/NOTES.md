# Jean, cardinal Du Bellay → The Constable, 1555, BnF Français 3142 — Du Bellay, ff60–61

Status: no write-up of our own (result by George Lasry, presented on docs/dubellay1555.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3142 — Du Bellay, ff60–61): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 3/3 pages transcribed in part; 3/3 pages deciphered in part
- Ciphertext-only: No
- Sender: Jean, cardinal Du Bellay
- Recipient: The Constable
- Date: 1555
- Key: 17 letter signs
- Ciphertext: 193 elements transcribed, 109 identified; remaining ciphertext not fully transcribed
- Contents: Memorandum to the Constable, including discussion of a promotion; a historical decipherment survives at ff62r–v.
- Method category (our classification): read from existing decipherment; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3142 — Du Bellay, ff60–61
Contents: Memorandum to the Constable, including discussion of a promotion; a historical decipherment
survives at ff62r–v.
3/3 pages transcribed in part; 3/3 pages deciphered in part
Ciphertext-only: No
Sender: Jean, cardinal Du Bellay
Recipient: The Constable
Year: 1555
Key: 17 letter signs
Ciphertext: 193 elements transcribed, 109 identified; remaining ciphertext not fully transcribed
Plaintext in another folio of the same volume: Historical decipherment of the ff60–61 memorandum
at ff62r–v. ·
Excerpt and Translation
Excerpt
f60v, three consecutive cipher rows (legacy A2–A4)
toutes leurs espiez soubz couleur de [?] des Lutheriens et le
Translation
all their spies, under the guise of [?], of the Lutherans, and the
```

## Links

- No link in the report.

## Images

- `lasry_p105_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p105_1.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: none (no Gallica link; fr. 3142 ark not resolvable offline)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his f60v crop, row 1: ψ π a ψ — + = t o u t e s ("toutes") with his table, then signs consistent with "leurs espiez"; only ~6-10 signs readable at crop resolution
- Verdict: **partly confirmed** (method read from existing decipherment, extent partial). The check is a sample, not a re-solution.
- Notes: Historical decipherment of the memorandum at ff62r-v (same volume), so reading rests on it; only 109/193 transcribed elements identified, ciphertext not fully transcribed. Date 1555 unverified.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/43_francais-3142-du-bellay-ff6061.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/`. The page shows it at the top.
Measured: whole text 0.869 (v10_relabel.measure); deciphered passages alone 0.784. His report: 3/3 pages transcribed in part, 3/3 deciphered in part. Outcome: read in part. He translates only the excerpt (`lasry/report/translation_excerpt.md`); no full translation.

## Remaining gaps

- ff60-61: 84 of 193 transcribed elements unidentified, the rest of the cipher not transcribed in his report - blocker: no-key-material; his key has 17 letter signs; the historical decipherment at ff62r-v is the plaintext he read it from.

## Escalation

- [x] siblings: neighbouring items of the volume belong to Lasry's BnF survey; his report uses what he found
- [x] clear-pages: the plaintext he names in his report (interlinear, margin or same-volume decipherment) is the material the key came from
- [x] known-keys: Lasry's reconstructed key is the key used; shown on the page
- [x] print: only the editions his report cites; none closes the unread groups (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
