# Jacques Vergier → Monseigneur, probably Jérôme de Pontchartrain, 10, 20, 26, 29 and 30 March 1696; 6 April 1696?, BnF Clairambault 1108

Status: no write-up of our own (result by George Lasry, presented on docs/vergier1696.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 1108): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

Report slug: `vergier1690`.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 17/17 pages transcribed; 12/12 cipher pages deciphered
- Ciphertext-only: No
- Sender: Jacques Vergier
- Recipient: Monseigneur, probably Jérôme de Pontchartrain
- Date: 10, 20, 26, 29 and 30 March 1696; 6 April 1696?
- Key: 152 codes: 31 letter codes, 116 nomenclature entries, 5 nulls
- Ciphertext: 1,212 elements, 1,209 identified (99.8%)
- Contents: Vergier reports the Anglo-Dutch fleet off Calais, Jacobite landing plans, and his conversations with James II’s entourage; he also discusses naval preparations at Dunkerque.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 1108
Contents: Vergier reports the Anglo-Dutch fleet off Calais, Jacobite landing plans, and his conversations with
James II’s entourage; he also discusses naval preparations at Dunkerque.
17/17 pages transcribed; 12/12 cipher pages deciphered
Ciphertext-only: No
Sender: Jacques Vergier
Recipient: Monseigneur, probably Jérôme de Pontchartrain
Year: 10, 20, 26, 29 and 30 March 1696; 6 April 1696?
Key: 152 codes: 31 letter codes, 116 nomenclature entries, 5 nulls
Ciphertext: 1,212 elements, 1,209 identified (99.8%)
Interlinear plaintext: Historical interlinear plaintext in the six letters, ff247r–251v,256v–257v,260v–
262r.
Gallica f247r
Gallica f256r
Gallica f260r

Excerpt and Translation
Excerpt
f249v
…dit seulement qu’il croyoit, et je trouve que c’est avec assez de raison, que l’affaire est à present
presque impraticable sur la coste de Kent, à cause des forces que le Prince d’Orange a mises de
ce costé-là. Et qu’il seroit à present necessaire de tenter le debarquement dans la province d’York,
où sont presque tous les haras d’Angleterre, et où par consequent on trouveroit les chevaux
necessaires pour l’armée, ou bien dans une des provinces de l’Ouest.
Translation
…said only that he thought—and with good reason, I believe—that the enterprise is now almost impracticable
on the coast of Kent because of the forces the Prince of Orange has stationed there. It would now be
necessary to attempt the landing in Yorkshire, where almost all England’s stud farms are situated and where
the horses needed for the army could consequently be found, or in one of the western provinces.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b90009665/f250.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b90009665/f259.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b90009665/f263.item>

## Images

- `lasry_p071_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p072_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b90009665/f263.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f260r "Boulogne ce 30 mars 1696", Monseigneur, signed Vergier (facing leaf); canvas f255 shows f251v numeric codes with interlinear ("277 14 176 143 259 186 50 ..." = "que je scache aussi qu ... ", "208 17 226 34 301 197 30 289" = "mon nouveliste"), confirming interlinear plaintext; f249v excerpt not compared symbol by symbol
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Slug says 1690 but every letter is 1696. Canvas f255 shows a letter "a Dunkerque ce 16e avril 1696" (f252r) - his "6 April 1696?" is probably 16 April. Interlinear decipherments throughout.

## Notes and corrections

Folder renamed from the report's slug vergier1690: every letter is dated 1696. The report's "6 April 1696?" is probably 16 April (f252r, "a Dunkerque ce 16e avril 1696").

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: Lasry's excerpt written out alone as lasry_excerpt_reading.md (the report page had been scored): plain 1.0. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/26_clairambault-1108.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.998 (v10_relabel.measure),
deciphered passages 1.0. His status: 17/17 pages transcribed; 12/12 cipher pages deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).
