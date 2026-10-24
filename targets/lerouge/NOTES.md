# F. Le Rouge → the Chancellor, 11 July, year unestablished, BnF Français 2971

Status: no write-up of our own (result by George Lasry, presented on docs/lerouge.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 2971): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: Transcribed; Deciphered
- Ciphertext-only: No
- Sender: F. Le Rouge
- Recipient: the Chancellor
- Date: 11 July, year unestablished
- Key: 28 symbols, 22 letter signs, 2 in nomenclature, 4 unidentified
- Ciphertext: 623 elements, 610 identified (97.9%)
- Contents: A Venetian diplomatic report about the king’s letters, an affront involving Milan, and warnings of a conspiracy; its closing fragment mentions England.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 2971
Contents: A Venetian diplomatic report about the king’s letters, an affront involving Milan, and warnings of a
conspiracy; its closing fragment mentions England.
Transcribed; Deciphered
Ciphertext-only: No
Sender: F. Le Rouge
Recipient: the Chancellor
Year: 11 July, year unestablished
Key: 28 symbols, 22 letter signs, 2 in nomenclature, 4 unidentified
Ciphertext: 623 elements, 610 identified (97.9%)
Interlinear plaintext: Interlinear plaintext on the same page, f32r. ·
Gallica Gallica source
Excerpt and Translation
Excerpt
f32r, cipher lines 1–3
… lettres du Roy à Seigneurie n’eussent sceu arriuer à meilleur poinct, aultant qu’elle [e]stoit mal
contente apres la demonstration qu’elle auoit faicte pour le roi…
Translation
… letters from the king to the Signoria could not have arrived at a better moment, given that it was displeased
after the show of support it had made for the king …
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9059907g>
- <https://gallica.bnf.fr/ark:/12148/btv1b9059907g/f61.item> — f32r = image 61 (the report links the volume only)
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059907g/f61/pct:0,35,100,25/2000,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p079_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p079_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059907g/f61/pct:0,35,100,25/2000,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: Gallica f61 = fol. 32 (his link had no folio); interlinear over cipher lines 1-3 reads "lres du Roy a la Sgrie neussent sceu arriver a meilleur point... quelle estoit mal contente apres la demonstration" = his excerpt; symbol-by-symbol decode not done (dense small script)
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Meta link points to volume, not folio; letter signed Le Rouge on f61, 11 July. 97.9% identified.

## Notes and corrections

f32r is Gallica image 61; the report links the volume only.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/30_francais-2971.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.937 (v10_relabel.measure),
deciphered passages 0.987. His status: Transcribed; Deciphered. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- f32r: 2 unread groups, 4 unidentified symbols (610 of 623 elements), clear passages with holes - blocker: no-key-material; the interlinear plaintext does not cover them; whole text 0.937.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the deciphered passages known to this project (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
