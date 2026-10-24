# Not established → Not established, 1650–1653 volume; individual dates unchecked, BnF Clairambault 460 — numerical cipher, pp289–303

Status: no write-up of our own (result by George Lasry, presented on docs/clair460num.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 460 — numerical cipher, pp289–303): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 9/9 pages transcribed; 9/9 pages deciphered in part
- Ciphertext-only: No
- Sender: Not established
- Recipient: Not established
- Date: 1650–1653 volume; individual dates unchecked
- Key: 104 numerical codes: 32 letter values, 55 syllables, 10 word values, 7 nulls
- Ciphertext: 2,080 visible elements, 1,558 identified; additional ciphertext hidden or damaged
- Contents: Letters about the Prince’s military resources, negotiations for war or peace, promised payments, and secure correspondence through Compiègne and other couriers.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 460 — numerical cipher, pp289–303
Contents: Letters about the Prince’s military resources, negotiations for war or peace, promised payments,
and secure correspondence through Compiègne and other couriers.
9/9 pages transcribed; 9/9 pages deciphered in part
Ciphertext-only: No
Sender: Not established
Recipient: Not established
Year: 1650–1653 volume; individual dates unchecked
Key: 104 numerical codes: 32 letter values, 55 syllables, 10 word values, 7 nulls
Ciphertext: 2,080 visible elements, 1,558 identified; additional ciphertext hidden or damaged
Interlinear plaintext: Literal interlinear plaintext on the same cipher pages, pp289–303.

Excerpt and Translation
Excerpt
p296
Il vous suplie de le vouloir informer clairement de vos intentions, soit pour la guerre, ou pour la
paix.
Translation
He begs you to inform him clearly of your intentions, whether for war or for peace.
```

## Links

- No link in the report.

## Images

- `lasry_p117_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p116_1.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: none (no Gallica link; Clairambault 460 ark not resolvable offline)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his p296 crop: interlinear "Il vous suplie de le vouloir informer clairement de vos intentions soit pour la guerre ou pour la paix" over 3-digit groups = his excerpt; numeric values not decoded by me
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: 1,558/2,080 visible (74.9%), 9/9 pages only in part; sender, recipient, dates not established.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/49_clairambault-460-numerical-cipher-pp289303.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/`. The page shows it at the top.
Measured: whole text 0.999 (v10_relabel.measure); deciphered passages alone 0.685. His report: 9/9 pages deciphered in part. The whole-text measure (0.999) is high because the interlinear plaintext carries most of the words; the deciphered runs alone are 0.685. Outcome: read in part. He translates only the excerpt (`lasry/report/translation_excerpt.md`); no full translation.

## Remaining gaps

- pp289-303: 522 of 2,080 visible elements unidentified (the [?] groups and doubtful words in the deciphered runs) - blocker: no-key-material; no value in his 104-code key; the interlinear plaintext does not cover them.
- pp289-303: further ciphertext hidden or damaged - blocker: illegible; his report: additional ciphertext hidden or damaged.

## Escalation

- [x] siblings: neighbouring items of the volume belong to Lasry's BnF survey; his report uses what he found
- [x] clear-pages: the plaintext he names in his report (interlinear, margin or same-volume decipherment) is the material the key came from
- [x] known-keys: Lasry's reconstructed key is the key used; shown on the page
- [x] print: only the editions his report cites; none closes the unread groups (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
