# Nicodemo Tranchedini → Francesco Sforza, 28 June 1452, BnF Italien 2242 — Tranchedini, 1452

Status: no write-up of our own (result by George Lasry, presented on docs/tranchedini1452.html; his full report text extracted 24 Oct 2026)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Italien 2242 — Tranchedini, 1452): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 3/3 pages transcribed in part; Partly deciphered
- Ciphertext-only: No
- Sender: Nicodemo Tranchedini
- Recipient: Francesco Sforza
- Date: 28 June 1452
- Key: 55 symbols: 23 letter forms, 32 in nomenclature
- Ciphertext: 852 elements deciphered; transcription incomplete
- Contents: The 28 June postscript discusses the bishops of Parma and Novara, the pope’s response, and the bishop’s reputation.
- Method category (our classification): read from existing decipherment; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Italien 2242 — Tranchedini, 1452
Contents: The 28 June postscript discusses the bishops of Parma and Novara, the pope’s response, and the
bishop’s reputation.
3/3 pages transcribed in part; Partly deciphered
Ciphertext-only: No
Sender: Nicodemo Tranchedini
Recipient: Francesco Sforza
Year: 28 June 1452
Key: 55 symbols: 23 letter forms, 32 in nomenclature
Ciphertext: 852 elements deciphered; transcription incomplete
Key elsewhere: Domnina (2018), Figure 5: reconstructed Tranchedini key from the 1449 letter and a
1454 decipherment. Matching values are checked against the 1452 manuscript. · Source
Plaintext in another folio of the same volume: Literal historical decipherment on f88r–v, immediately
before the cipher on f89r (PDF84–85).
Gallica f89r
· Source
Plaintext available
```

## Links

- <https://ep.liu.se/ecp/149/007/ecp18149007.pdf>
- <https://gallica.bnf.fr/ark:/12148/btv1b100387843/f83.item>

## Images

- `lasry_p050_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p049_1.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b100387843/f83.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f89r "Post data ... Signore" cipher postscript dated 28 Jun 1452, signed Nicodemus; facing f88v carries the contemporary decipherment (clear: "vescovo de Novara ... la V. Ill. hauria ben facto ... paragonata ... Certificandone Signore"), which matches the clear islands on f89r and his contents; no symbol-level decode of a run done
- Verdict: **partly confirmed** (method read from existing decipherment, extent partial). The check is a sample, not a re-solution.
- Notes: A literal 15th-c. decipherment sits on f88r-v next to the cipher, and the key is Domnina 2018s reconstruction, so little is new beyond alignment. Transcription incomplete; status Partly deciphered.

## Verification 3, 23 Oct 2026

The v3 sweep scored this entry's `lasry_entry.md` (0.588), but that file holds only the metadata of Lasry's report
page: unlike his other entries it carries no excerpt, and his transcription and decryption are not in the
repository. So there is no reading here, and `outcome.texts[0]` is now **decoded, not read**. The reading source is
on Gallica: the contemporary literal decipherment, f. 88r (lower half, "Post dat. Signore …") and f. 88v
(btv1b100387843, canvases 82-83, opened 23 Oct 2026), about thirty lines of abbreviated 15th-century cursive. The
result remains Lasry's (class already solved).

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF, extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the full Readable text by folio). The page shows it at the top. Measured: whole text 0.718 (v10_relabel.measure), deciphered passages 0.542 (bare ? counted as unread). His status: 3/3 pages transcribed in part; Partly deciphered. Outcome: read in part.

## Remaining gaps

- f89r (28 June 1452) and the historical decipherment ff88r-v: unread groups between the deciphered runs - blocker: no-key-material; left as George Lasry marks them; no other key or plaintext known; his decipherment is the only one
- f89r, partly deciphered: not transcribed or deciphered in full in Lasry's report - blocker: no-key-material; his report status says so; outside this project's work, no other key or plaintext known

## Escalation

- [x] siblings: neighbours belong to George Lasry's BnF survey; no sibling key found here
- [x] clear-pages: the report's pages and the manuscript on Gallica checked against his text; no further decipherment held
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the unread passages found
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
