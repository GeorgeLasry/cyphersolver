# Signed DC → Not established, 20 May; year not established, BnF Français 3321

Status: no write-up of our own (result by George Lasry, presented on docs/fr3321dc.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3321): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: Transcribed; Deciphered
- Ciphertext-only: No
- Sender: Signed DC
- Recipient: Not established
- Date: 20 May; year not established
- Key: 32 symbols, 25 letter signs, 5 in nomenclature, 1 null ?, 1 unidentified
- Ciphertext: 49 elements, 46 identified (93.9%); 2 ?, 1 unidentified
- Contents: A political letter says the union can impose its terms and describes an escape from execution, drowning and plunder; several named opponents remain uncertain.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3321
Contents: A political letter says the union can impose its terms and describes an escape from execution,
drowning and plunder; several named opponents remain uncertain.
Transcribed; Deciphered
Ciphertext-only: No
Sender: Signed DC
Recipient: Not established
Year: 20 May; year not established
Key: 32 symbols, 25 letter signs, 5 in nomenclature, 1 null ?, 1 unidentified
Ciphertext: 49 elements, 46 identified (93.9%); 2 ?, 1 unidentified
Interlinear plaintext: Interlinear plaintext on the same page, f103r. ·
Gallica f103r

Excerpt and Translation
Excerpt
f103r, first four lines
Les affaires sont en tel termes qu'infalliblement la Ruyne de Espernon s'en ensuivra, ou de cest estat.
Car l'union est si forte qu'elle peult mieux donner la loy que la recepvoir. Demain la req[ueste] s'en
doibt partir, vous en aurez Incontinent la coppie Comme on vous envoye du reste.
Translation
Affairs have reached such a point that Épernon’s ruin, or the ruin of this state, will inevitably follow. The union
is so strong that it can dictate the law rather than receive it. The petition is to be sent tomorrow; you will
immediately receive a copy, as the other material is being sent to you.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9060212v/f105.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060212v/f105/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p080_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p081_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060212v/f105/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f103r l.2 after "Car": l u n i o n [est] s i f o r t (14 signs incl. est code) = "lunion est si fort"; also Espernon code after "Ruyne de"; matches excerpt and interlinear
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Only 49 cipher elements; 93.9% identified (<95%). Signed with monogram, "xxme may". Ligue context (union vs Epernon) suggests 1588.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/31_francais-3321.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.996 (v10_relabel.measure),
deciphered passages 0.889. His status: Transcribed; Deciphered. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- f103r: 3 of 49 cipher elements unread (2 ?, 1 unidentified), several named opponents uncertain - blocker: too-short; 49 elements in all; the interlinear does not resolve them.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the deciphered passages known to this project (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
