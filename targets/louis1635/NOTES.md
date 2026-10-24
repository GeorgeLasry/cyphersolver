# Louis XIII → Châtillon and Brézé, 30 June 1635, BnF Français 3758 — Louis XIII, 30 juin 1635

Status: no write-up of our own (result by George Lasry, presented on docs/louis1635.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3758 — Louis XIII, 30 juin 1635): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 10/10 pages transcribed; 6/6 cipher pages deciphered in part
- Ciphertext-only: No
- Sender: Louis XIII
- Recipient: Châtillon and Brézé
- Date: 30 June 1635
- Key: 53 mapped signs: 40 letter signs, 13 in nomenclature.
- Ciphertext: 967 elements, 722 identified (74.7%).
- Contents: Royal campaign instructions, the use of time and forces, cooperation with the Prince of Orange, and the need to cipher important dispatches.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3758 — Louis XIII, 30 juin 1635
Contents: Royal campaign instructions, the use of time and forces, cooperation with the Prince of Orange,
and the need to cipher important dispatches.
10/10 pages transcribed; 6/6 cipher pages deciphered in part
Ciphertext-only: No
Sender: Louis XIII
Recipient: Châtillon and Brézé
Year: 30 June 1635
Key: 53 mapped signs: 40 letter signs, 13 in nomenclature.
Ciphertext: 967 elements, 722 identified (74.7%).
Plaintext in another folio of the same volume: Actual historical plaintext copies appear in
blank/facing-page areas: PDF128 right lower and PDF129 left for f115r; PDF131 left (f116v) copies
selected f117r passages, including the Orange/route instructions and the warning about an intercepted
dispatch.

Excerpt and Translation
Excerpt
f117r
Quand vous m’escriprez quelque chose d’importance souvenez vous que ce soit en chiffre. Car sy la
despesche du xviiᵉ fust tombée entre les mains des Ennemis, ilz eussent appris [?] et en eussent
tiré ?duantage.
Translation
When you write something important to me, remember to put it in cipher. For if the dispatch of the
seventeenth had fallen into the enemies’ hands, they would have learned [?] and gained an [?] advantage
from it.
```

## Links

- No link in the report.

## Images

- `lasry_p104_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p103_1.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: none (no Gallica link; fr. 3758 ark not resolvable offline, gallica.bnf.fr behind Cloudflare)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his f117r crop: clear "quand vous mescriprez quelque chose dImportance souvenez vous que ce soit en chiffre" then 48(car) XX(y) 96(la) 61.. 54 du xvii(e) ... = "car sy la despesche du xviie" fits his codes at the start; rest not decodable from crop, many key values marked ?
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: 74.7% identified; key values heavily queried. Same volume as chatillon1635 (fr. 3758). Clear copies of some passages on facing pages.

## Notes and corrections

Fr. 3758 is also part of [targets/rohan1636](../rohan1636/NOTES.md).

## Verification 5, 23 Oct 2026

The plain-bar sweep scored `lasry_entry.md`, George Lasry's report entry (metadata, one excerpt and its
translation), which is not a reading of the document. His full decryption (BnF cipher research, 10 Oct 2026) is not in
the repository and is his to publish; the contemporary interlinear decipherment is on the Gallica images only. The
entry stays an **external pointer** to his decipherment, with a note saying so; not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/42_francais-3758-louis-xiii-30-juin-1635.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.908 (v10_relabel.measure),
deciphered passages 0.582. His status: 10/10 pages transcribed; 6/6 cipher pages deciphered in part. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- ff113v-118r: about 116 unread groups and 57 doubtful words in the deciphered runs (722 of 967 elements identified) - blocker: no-key-material; historical plaintext copies cover only f115r and parts of f117r; his status: 6/6 cipher pages deciphered in part.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the deciphered passages known to this project (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
