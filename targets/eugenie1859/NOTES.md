# Napoleon III / Empress Eugénie (both directions) → Empress Eugénie / Napoleon III (both directions), June 1859, BnF NAF 11355 — Emperor–Empress code

Status: in progress. Lasry's reading; only four pages of tokens and three excerpts are in the repository (reading audit, 22 Oct 2026).

**22 Oct 2026, reading audit** (George Lasry's test): the token table of ff. 9r, 15r, 17r, 18r, taken in order, builds French sentences, and the three report excerpts (ff. 19r, 35r, 27r) read; both are *excerpts* of Lasry's reading, whose full text is not in the repository. Krajcovic's corrections file is *not prose*. fraction_read 0.841 (Lasry's identified elements) -> about 0.31, what the repository shows.

Earlier status (before the 22 Oct 2026 reading audit): no write-up of our own (result by George Lasry, presented on docs/eugenie1859.html)

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## Verification by Jozef Krajčovič (issue #39, 16 Oct 2026)

Jozef Krajčovič (GitHub kjfriedo) re-read f9r, f15r, f17r and f18r by hand, then applied Lasry's key; he says
plainly this is not a ciphertext-only re-solution. Crib and control pages f19r, f27r, f29r, f30r, f35r; negative
control f21r-v (headed Emperor to the War Ministry: values above the Emperor-Empress range, no French under this
key, so a different nomenclator). Agreements, for example f15r 1155 1113 660 1244 199 *sans résistance*, f18r 195
1265 563 608 888 *Castiglione*, f27r/f30r 1333 30 785 1342 *va à merveille*.

Proposed corrections to the token transcription (not applied here; the transcription and key are Lasry's, and the
list goes to him): f9r 1143 -> 1193 (501 419 1193 = expr-[419]-sion, so 419 = es); f18r 1268 -> 1265 (1265 = ti,
also in fa-ti-gue); f15r 1115 -> 1155; f17r 839 -> 889 and 353 -> 355; provisional f9r 1200 = sort (*en sortant
avec le roi*). He would keep f17r 1325 = une. His package (token streams, a verification script, page locators) is
attached to the issue.

He also pointed out that the page said "Extent: complete" against 9 of 11 cipher pages deciphered; the profile class
was corrected to read in part on 21 Oct 2026.

## Lasry's answer to the proposed corrections (22 Oct 2026)

George Lasry checked each proposal against his final transcription and key (10 Oct 2026) and against the Gallica
images of f9r and f17r. No change to his transcription or key follows. His token streams for the four pages are in
`lasry_tokens_f9_f15_f17_f18.tsv` (code, value, confidence, as in his working files).

- Already in his transcription: f9r 1193 = sion, f18r 1265 = ti, f15r 1155 = sans, f17r 889 = ons and 355 = der.
  The values these were to replace (1143, 1268, 1115, 839, 353) are not in his transcription or his key.
- f9r *expr-es-sion* is 501 **459** 1193, not 419. The middle digit is the scribe's long ʃ-shaped 5, as in 515,
  54 and 598 on the same page. 459 = es also sits in the alphabetical run 453 er, 457 er, 459 es, 462 esp; 419
  would fall before 425 em.
- f9r *en sortant avec le roi* is 432 **1210** 85 126 708 1132; 1210 = sort is in his key. The image shows 1210
  twice, in the struck-out first line and in the clean line. Not 1200.
- f17r line 2 begins **151**, not 751: the first stroke is the hooked 1 of 1232 on the line, not the barred 7 of
  753 and 708. His key has 151 = bataille (between 142 bai and 160 bien), so the passage reads *nous espérons une
  bataille sur Chiese*. That keeps 1325 = une, as Krajčovič suggested, and removes the anomaly of *une main*.
- f17r ends 237 **868** (*Min-ci-o*), not 808 (808 = mon in his key).
- Other differences in the token streams: f9r line 4 (ink blot) has 751? 717? 515 in his reading against ?51 773
  518; f15r, in the unread tail, 925 and 656 against 935 and 616 (not re-checked against the image); the header
  numbers 753 (f15r) and 1098 (f17r) are outside his cipher streams; 329 is his marked code 329z.
- He agrees that f21r-v uses a different nomenclator.
- Checked here (22 Oct 2026) against his TSV: 1193, 1265, 1155, 889, 355, 459 = es, 1210 = sort, 151 = bataille and
  868 = o all occur on the folios he names; 1143, 1268, 1115, 839, 353, 419, 1200, 751 and 808 do not. The images
  were not re-checked here.

## His metadata

- Report status: 15/15 pages transcribed; 9/11 cipher pages deciphered; 2 more in part
- Ciphertext-only: Yes
- Sender: Napoleon III / Empress Eugénie (both directions)
- Recipient: Empress Eugénie / Napoleon III (both directions)
- Date: June 1859
- Key: 233 codes, 12 letter signs, 220 in nomenclature, 1 separator
- Ciphertext: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?
- Contents: Napoleon III’s policy toward the Pope, his criticism of diplomatic speculation, and reports from the Italian campaign; private family news exchanged with Empress Eugénie.
- Method category (our classification): key recovered from ciphertext-only; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
NAF 11355 — Emperor–Empress code
Contents: Napoleon III’s policy toward the Pope, his criticism of diplomatic speculation, and reports from the
Italian campaign; private family news exchanged with Empress Eugénie.
15/15 pages transcribed; 9/11 cipher pages deciphered; 2 more in part
Ciphertext-only: Yes
Sender: Napoleon III / Empress Eugénie (both directions)
Recipient: Empress Eugénie / Napoleon III (both directions)
Year: June 1859
Key: 233 codes, 12 letter signs, 220 in nomenclature, 1 separator
Ciphertext: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?
Literal plaintext: f35r: L’ennemi s’est retiré cette nuit. — One ciphered sentence only; fatigue passage not
printed. · L’Écho saumurois, 28 June 1859, p. 1 ·
Gallica ff3r–5r
Gallica f9r
Gallica ff14r–15r
Gallica ff17r–19r
Gallica f27r
Gallica ff29r–30r
Gallica ff32r–35r

Excerpt and Translation
Excerpt
f19r — the Pope and diplomacy
Je suis bien peiné au milieu de mes travaux d’avoir à répondre à toutes les sotte[s] suppositions de
la diplomatie. Je maintiens le pape à Rome avec mon armée. Je ne me mêle en rien du reste de
ses États.
Translation
I am very distressed, amid my work, to have to answer all the foolish suppositions of diplomacy. I keep the
Pope in Rome with my army. I do not interfere in any way with the rest of his States.

Excerpt
f35r — the battle and the Austrian emperor’s room
Impossible de donner des détails sur la bataille d’hier. Tout [le] monde était mort de fatigue. L’ennemi
s’est retiré cette nuit. J’ignore le nombre précis de canons, de drapeaux et de prisonniers. J’ai couché
cette nuit dans la chambre où l’Empereur d’Autriche a déjeuné hier matin. Niel est nommé Maréchal. La
bataille prendra le nom de Solférino.
Translation
It is impossible to give details of yesterday’s battle. Everyone was dead tired; the enemy withdrew during the
night. I do not know the exact number of cannon, flags and prisoners. I slept last night in the room where the
Emperor of Austria had breakfast yesterday morning. Niel has been appointed Marshal. The battle will be
named Solferino.

Excerpt
f27r — Eugénie’s message
Je suis désolée de vous avoir fait de la peine, ce n’était? pas mon intention. Ne vous inquiétez
pas du petit, il va à merveille. J’écris aujourd’hui par la poste.
Translation
I am sorry to have caused you sorrow; that was not? my intention. Do not worry about the little one; he is
doing wonderfully. I am writing today by post.
```

## Links

- <https://archives.ville-saumur.fr/_depot_amsaumur/_depot_arko/fonds/echo_saumurois/pdf/1859/FRAC049328_ECHSAU_1859_06_28.pdf>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f11.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f23.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f33.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f39.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f57.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f61.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f67.item>

## Images

- `lasry_p027_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p026_1.png, p028_3.png, p029_4.png, p030_5.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f67.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f32r = Solferino telegram "Cavriana 24 juin 1859, Empereur a Imperatrice", clear text + code "941 325 274 1155 / 163 1142 1162"; his key gives 274=connais, 163=ble, 1142=s (fragmentary, no excerpt covers this run); f19r/f35r excerpts not image-checked
- Verdict: **partly confirmed** (method key recovered from ciphertext-only, extent partial). The check is a sample, not a re-solution.
- Notes: 84.1% identified, 50 ?; 2 cipher pages only in part. Telegrams of 1859 were partly printed in the press (he cites L Echo saumurois 28 June 1859) - external plaintext available for f35r.

## 23 Oct 2026: verification 3 (explicit-hole score)

The v3 sweep scored the Lasry-tokens entry on `lasry_tokens_f9_f15_f17_f18.tsv` itself (one value per row; 0.0): the
entry had no reading file. Lasry's values are now divided into words per folio in
`texts/eugenie1859_f9_f18_reading.md` (letters no value carries bracketed, his "?" tokens as [?]): 0.625 explicit-hole
(5/8 sentence windows), plain 0.5, the unknown words being the place names. ff. 9r, 17r, 18r and the first sentence
of 15r hold; the end of 15r is a run of tokens without values. Keeps read, barely.

## Verification 5, 23 Oct 2026

Plain-bar check (French 1859). `texts/eugenie1859_f9_f18_reading.md`: plain 0.5, explicit 0.625; two of the failing
windows fail only on place names (Chiese, Mincio, Lonato, Castiglion), the real hole is the unvalued run at the end of
f. 15r. Keeps read. The report-excerpt file had been scored with its English and page furniture (plain 0.488); the
French excerpts alone are now `texts/eugenie1859_lasry_excerpts_reading.md`, plain 1.0; keeps read.

## Remaining gaps

- Lasry's full decipherment of the eleven cipher pages, not in the repository - blocker: not-attempted; ask George Lasry for his transcription and decryption files

## Escalation

- [x] siblings: not this project's reading; George Lasry's report covers the volume
- [n/a] clear-pages: not looked for here; the result is Lasry's
- [x] known-keys: Lasry's key is the key; his key table is not in the repository
- [x] print: Lasry's report (BnF cipher research, 10 Oct 2026) is the source
- [n/a] key-rebuild: not this project's work
- [ ] retry: ask Lasry for his full transcription and decryption
