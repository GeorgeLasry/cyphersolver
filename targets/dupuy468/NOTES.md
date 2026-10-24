# Ernestus dux and Joachimus; probably Ernst of Brunswick-Lüneburg and Joachim von Maltzan → Francis I, King of France, Eve of Saint Paul, at five in the morning; no year. Context suggests c.1518–1520;1519 remains, BnF Dupuy 468

Status: no write-up of our own (result by George Lasry, presented on docs/dupuy468.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Dupuy 468): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 2/3 pages transcribed; 1 more in part; 2/2 cipher pages deciphered
- Ciphertext-only: No
- Sender: Ernestus dux and Joachimus; probably Ernst of Brunswick-Lüneburg and Joachim von Maltzan
- Recipient: Francis I, King of France
- Date: Eve of Saint Paul, at five in the morning; no year. Context suggests c.1518–1520;1519 remains
- Key: 30 symbols, 20 letter signs, 6 in nomenclature, 3 nulls?, 1 unidentified
- Ciphertext: 684 elements, 660 identified (96.5%)
- Contents: A German princely league would admit new members by majority consent, promise pensions, and later bring in the French king.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Dupuy 468
Contents: A German princely league would admit new members by majority consent, promise pensions, and
later bring in the French king.
2/3 pages transcribed; 1 more in part; 2/2 cipher pages deciphered
Ciphertext-only: No
Sender: Ernestus dux and Joachimus; probably Ernst of Brunswick-Lüneburg and Joachim von Maltzan
Recipient: Francis I, King of France
Year: Eve of Saint Paul, at five in the morning; no year. Context suggests c.1518–1520;1519 remains
plausible.
Key: 30 symbols, 20 letter signs, 6 in nomenclature, 3 nulls?, 1 unidentified
Ciphertext: 684 elements, 660 identified (96.5%)
Interlinear plaintext: Interlinear decipherment accompanies most cipher runs on f28r–v,PDF65–
66/Gallica63–64.
Gallica Selected letter, f28r–f29r

Excerpt and Translation
Excerpt
f28r, final four cipher lines
Tunc optimum erit ut christianissimus hoc fedus petat velle inire; hoc modo etiam si aliquando
noluissent esse in federe cu[m] christianissimo, hoc modo astricti erunt esse confederatores
christianissimi.
Translation
Then it will be best for the Most Christian King to ask to join this alliance. In this way, even if some had not
wished to ally themselves with him, they will be bound to become his allies.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b10035959t/f63.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b10035959t/f63/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p077_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p078_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b10035959t/f63/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f28r l.2 V.⊔.ч.4.V.T.cc.m -> i n o p i d u m = "in oppidum" (interlinear agrees); signs match his table (i=V,n=⊔,o=ч,p=4,d=T,u=cc,m)
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Addressed Christianissime rex, signed Ernestus/Joachimus; interlinear on most runs; 96.5% identified, 2/2 cipher pages; 1 page only partly transcribed (clear text). Date c.1519 is his inference.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/29_dupuy-468.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.955 (v10_relabel.measure),
deciphered passages 0.982. His status: 2/3 pages transcribed; 1 more in part; 2/2 cipher pages deciphered. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- f28r-f28v: 3 unread groups and 24 unidentified elements (660 of 684 identified); f29r transcribed in part - blocker: no-key-material; the interlinear covers most runs, not these; one sign unidentified in his key.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the deciphered passages known to this project (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
