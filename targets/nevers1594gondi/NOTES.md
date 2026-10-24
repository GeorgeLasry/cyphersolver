# Duke of Nevers → M. de Gondi, 27 March 1594, BnF Français 3622

Status: no write-up of our own (result by George Lasry, presented on docs/nevers1594gondi.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3622): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 3/3 pages transcribed in part; Deciphered
- Ciphertext-only: No
- Sender: Duke of Nevers
- Recipient: M. de Gondi
- Date: 27 March 1594
- Key: 54 symbols: 39 letter signs, 1 double-letter sign, 14 in nomenclature
- Ciphertext: 245 elements, 230 identified (93.9%)
- Contents: Arrangements to send money to Lyon and check Swiss muster rolls; a promised payment by the end of April and a mission to the aldermen of Lyon.
- Method category (our classification): read after matching with key from external sources; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3622
Contents: Arrangements to send money to Lyon and check Swiss muster rolls; a promised payment by the
end of April and a mission to the aldermen of Lyon.
3/3 pages transcribed in part; Deciphered
Ciphertext-only: No
Sender: Duke of Nevers
Recipient: M. de Gondi
Year: 27 March 1594
Key: 54 symbols: 39 letter signs, 1 double-letter sign, 14 in nomenclature
Ciphertext: 245 elements, 230 identified (93.9%)
Key elsewhere: Original key in a different volume: Français 3995, ff122v–123r (Cryptiana no66). ·
Source
Gallica f91r

Excerpt and Translation
Excerpt
f91r — four complete body lines
facent monstre sur les vieu? rooles parce qu’il y va grand perte. Rasseure le Roy qui l’auroit le
tout à la fyn d’avril selon que vous me dites. Au demeurant, j’ay despesché aussy ? Asdrubal vers
le Corse et eschevyns de Lyon pour l’affaire
Translation
[They] muster on the old? rolls, because a great loss is at stake. Reassure the King that he would have
everything by the end of April, as you tell me. Meanwhile, I have also sent ? Asdrubal to the Corsican and the
aldermen of Lyon about the business.
```

## Links

- <https://cryptiana.web.fc2.com/code/nevers.htm#no66>
- <https://gallica.bnf.fr/ark:/12148/btv1b9058938q/f100.item>

## Images

- `lasry_p044_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p043_1.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b9058938q/f100.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f91r opens "Monsieur de Gondy", clear French with mixed letter/number cipher runs; his key image is the original Fr. 3995 f122v-123r table (A=7/1/9, B=6/9 ..., Monosillables, Nulles 17 22), and the cipher sign repertoire (digits, Greek-like letters, nulls) matches it; a full 10-symbol decode was not completed
- Verdict: **partly confirmed** (method read after matching with key from external sources, extent partial). The check is a sample, not a re-solution.
- Notes: 93.9% identified and pages transcribed only in part. Key also in Cryptiana (no. 66), i.e. previously published key.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF, extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the full Readable text by folio). The page shows it at the top. Measured: whole text 0.903 (v10_relabel.measure), deciphered passages 0.911 (bare ? counted as unread). His status: 3/3 pages transcribed in part; Deciphered. Outcome: read in part.

## Remaining gaps

- ff91r-92r: unread groups between the deciphered runs - blocker: no-key-material; left as George Lasry marks them; no other key or plaintext known; his decipherment is the only one
- all 3 pages, transcribed in part: not transcribed or deciphered in full in Lasry's report - blocker: no-key-material; his report status says so; outside this project's work, no other key or plaintext known

## Escalation

- [x] siblings: neighbours belong to George Lasry's BnF survey; no sibling key found here
- [x] clear-pages: the report's pages and the manuscript on Gallica checked against his text; no further decipherment held
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the unread passages found
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
