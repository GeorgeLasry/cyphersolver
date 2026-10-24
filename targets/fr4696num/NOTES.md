# Not established → Not established, 1589?, BnF Français 4696 — numerical cipher, ff54r–55r

Status: no write-up of our own (result by George Lasry, presented on docs/fr4696num.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 4696 — numerical cipher, ff54r–55r): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 3/3 pages transcribed; 1/3 pages deciphered; 2 more in part
- Ciphertext-only: No
- Sender: Not established
- Recipient: Not established
- Date: 1589?
- Key: 70 codes: 49 letter signs, 19 in nomenclature, 2 unidentified
- Ciphertext: 1,744 elements, 1,692 identified; 1 obscured group of unknown length
- Contents: Intercepted letters disclose political loyalties in France. The Pope knows the cipher; the writer urges changing it, writing more cautiously to Italy, and sending the Duke of Mantua news of France by a secure route.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 4696 — numerical cipher, ff54r–55r
Contents: Intercepted letters disclose political loyalties in France. The Pope knows the cipher; the writer
urges changing it, writing more cautiously to Italy, and sending the Duke of Mantua news of France by a
secure route.
3/3 pages transcribed; 1/3 pages deciphered; 2 more in part
Ciphertext-only: No
Sender: Not established
Recipient: Not established
Year: 1589?
Key: 70 codes: 49 letter signs, 19 in nomenclature, 2 unidentified
Ciphertext: 1,744 elements, 1,692 identified; 1 obscured group of unknown length
Interlinear plaintext: Historical interlinear plaintext on ff54r–55r.

Excerpt and Translation
Excerpt
f55r, full cipher lines 1–6
Piu sobria sara V.Ecc. nel scriuere in Italia, masime in modo che posi risapersi tanto. Sara meglio
l’auuisare il serenisimo signor duca di Mantua frequentemente et per uia sicura de i sucesi di
Francia. Sara sopra modo grato a S.A. a quale et a V.Ecc. tornara molto a conto.
Translation
The more restrained Your Excellency is in writing to Italy, especially in a way that could become known, the
better. Informing the Most Serene Duke of Mantua frequently, and by a secure route, of events in France will
be exceedingly welcome to His Highness and will greatly benefit both him and Your Excellency.
```

## Links

- No link in the report.

## Images

- `lasry_p106_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p107_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: none (no Gallica link; fr. 4696 ark not resolvable offline)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his f55r crop: contemporary interlinear over 6 digit rows "piu sobria sara V.Ecc. nel scrivere in Italia ma simeinmodo che posi risaper si tanto sara meglio lavisare il serenisimo signor duca di mantua frequentemente et per via sicura de i sucesi di francia..." = his excerpt; digits not decoded by me
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Sender/recipient/date (1589?) not established; only 1/3 pages fully deciphered though 97% of elements identified. Italian.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/44_francais-4696-numerical-cipher-ff54r55r.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/`. The page shows it at the top.
Measured: whole text 0.996 (v10_relabel.measure); deciphered passages alone 0.991. His report: 1/3 pages deciphered, 2 more in part. Outcome: read in part. He translates only the excerpt (`lasry/report/translation_excerpt.md`); no full translation.

## Remaining gaps

- ff54r-55r: 2 unidentified codes among 52 unidentified of 1,744 elements - blocker: no-key-material; no value in his key; the interlinear plaintext does not cover them.
- ff54r-55r: one obscured group of unknown length - blocker: illegible; his report: obscured on the leaf.

## Escalation

- [x] siblings: neighbouring items of the volume belong to Lasry's BnF survey; his report uses what he found
- [x] clear-pages: the plaintext he names in his report (interlinear, margin or same-volume decipherment) is the material the key came from
- [x] known-keys: Lasry's reconstructed key is the key used; shown on the page
- [x] print: only the editions his report cites; none closes the unread groups (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
