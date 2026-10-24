# Giovanni, cardinal Salviati → Not established, 16 October 1525, BnF Français 2933

Status: no write-up of our own (result by George Lasry, presented on docs/salviati1525.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 2933): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): the repository holds only
his three-line excerpt of f54r, which reads with three `[?]` and has his translation (reviewed B in `profile.json`).
His 704/838 elements identified is key coverage, not a reading figure; his report says 3/8 pages deciphered in part.
`fraction_read` 0.84 -> about 0.1 (held text that reads, estimated). Nothing relabelled decoded, not read: the rest of
his decryption is not here to grade.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 2/8 pages transcribed; 1 more in part; 3/8 pages deciphered in part
- Ciphertext-only: Yes
- Sender: Giovanni, cardinal Salviati
- Recipient: Not established
- Date: 16 October 1525
- Key: 78 symbols: 18 letters, 54 syllables, 3 doubled letters, 3 words
- Ciphertext: 838 elements, 704 identified; 2 further groups with unresolved boundaries; transcription
- Contents: Salviati discusses restoration of possession and imperial territory, defence and government of the state, nobles and people, captains and guards, the archbishop of Toledo, Modena, and correspondence sent by land and sea.
- Method category (our classification): key recovered from ciphertext-only; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 2933
Contents: Salviati discusses restoration of possession and imperial territory, defence and government of the
state, nobles and people, captains and guards, the archbishop of Toledo, Modena, and correspondence sent
by land and sea.
2/8 pages transcribed; 1 more in part; 3/8 pages deciphered in part
Ciphertext-only: Yes
Sender: Giovanni, cardinal Salviati
Recipient: Not established
Year: 16 October 1525
Key: 78 symbols: 18 letters, 54 syllables, 3 doubled letters, 3 words
Ciphertext: 838 elements, 704 identified; 2 further groups with unresolved boundaries; transcription
incomplete
Gallica f54r

Excerpt and Translation
Excerpt
f54r — complete lines 13–15
e bisogniera trovare qualche modo [?] Pure a me pare che l’essere restituita la possessione basti
[?] maxime. Stando ancora le cose [?] di Modena [?] come stanno hora, V.S.…
Translation
and it will be necessary to find some way [?] Yet it seems to me that having possession restored
should suffice [?] especially with matters [?] of Modena [?] still as they now stand, Your Lordship…
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b90600674/f55.item>

## Images

- `lasry_p031_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p032_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b90600674/f55.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f54r: interleaved clear words "Pure a me pare ... maxime. Stando ancora le cose ... come stanno hora" match his L13-15 excerpt; cipher sign after "pare" = H-10 = "che" per his key, consistent with "che l essere"; longer cipher run not decoded
- Verdict: **partly confirmed** (method key recovered from ciphertext-only, extent partial). The check is a sample, not a re-solution.
- Notes: Opening reads "Rdo Dno Lang. Ptri" - recipient looks named (Langeac?/Langi?), though he says not established. 704/838 identified, 3/8 pages in part.

## Notes and corrections

The recipient is in the heading: the letter opens "Rdo Dno Lang. Ptri". The report says the recipient is not established.

## Verification v8, 23 Oct 2026

The excerpt of f54r held here (`lasry_entry.md`) does not read on its own: `v2_score.py` 0.0 on explicit holes and plain
(0/2 sentences, a `[?]` in each, hole rate 0.152). The reading is George Lasry's (3/8 pages deciphered in part, not in
the repository); the entry's state is left as his pointer, with a note saying so.


## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/09_francais-2933.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.809 (v10_relabel.measure),
deciphered passages 0.758 (bare ? counted as unread). f54r-f54v build sentences with holes between the deciphered runs;
ff55r-57r are mostly unread (his status: 2/8 pages transcribed, 1 in part; 3/8 deciphered in part). Outcome: read in part.

## Remaining gaps

- f54r-f54v: unread groups between the deciphered runs - blocker: no-key-material; 838 elements, 704 identified in his key; no other key or plaintext known; his decipherment is the only one.
- ff55r-57r: not transcribed or deciphered in his report - blocker: no-key-material; outside this project's work, his transcription is incomplete (2/8 pages).

## Escalation

- [x] siblings: Français 2933 neighbours belong to Lasry's BnF survey; no sibling key on DECODE (record search 24 Oct 2026)
- [x] clear-pages: f54r-f57v opened on Gallica 13 Oct 2026; no decipherment or gloss
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of this letter found; DECODE has no record (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
