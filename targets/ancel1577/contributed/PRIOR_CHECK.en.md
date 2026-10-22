# Prior-work check (attempted refutation)

Japanese: PRIOR_CHECK.md

Aim: to find out whether the passages read here (the cipher on p.525–526, p.539, p.561–563, p.565 and p.570 of BnF Cinq Cents de Colbert 398 — Guillaume Ancel's letters of October–December 1577) have already been read and published, searching with the intention of showing that they have.

## Conclusion
- Category: **not found** — no decipherment of these cipher passages was found in the places below (as of 20 Oct 2026).
- We do not claim to be first; the "not checked" items below remain.
- Closest prior work:
  - The key is Satoshi Tomokiyo's reconstruction (Cryptiana); he writes that it allows reading the undeciphered letters but publishes no readings.
  - Damien Fontvieille's paper (April 2024) is on Jean de Vulcob's ciphered correspondence of the 1570s; according to the conference report, with no key available it relies on the contemporary interlinear decipherments that already exist. It does not overlap with Ancel's undeciphered 1577 passages read here.
  - G. Labouchère (1923) summarises the **clear-text paragraph** of the same letter of 22 October 1577 (the oath of the Estates of Austria) but nothing of its cipher passages.

## 1. Search by a reader who took no part in the decipherment (20 Oct 2026)
A separate reader (Claude) that had not taken part in the decipherment received the records and searched with the aim of showing the passages had already been read.

| place | version / date | result |
|---|---|---|
| Cyphersolver (dbourdeau/cyphersolver) | origin/main 0258b8ab (18 Oct 2026) | "Colbert 398" only as the comparison key of vulcob1573 (BnF fr.3318, G. Lasry); "Malstet", "Varembon": 0 |
| Cyphersolver issues and PRs | all (latest #49, 19 Oct 2026) | none |
| Lasry's paper excerpts (in Cyphersolver) | same | Vulcob not mentioned |
| Cryptiana unsolved.htm / GL.htm / ai.htm / verification.htm | 13 Oct / 15 Oct / 19 Oct / 15 Oct 2026 | Colbert 398 only in GL.htm as the comparison key for fr.3318 |
| Cryptiana frencheastern.htm | 15 Mar 2026 | source of the key; list of letters and "The reconstructed key below will allow reading undeciphered letters"; no readings |
| Cryptoole API | 854 cases | none |
| copy of the DECODE catalogue (aaymeloglu/unsolved-ciphers, c2436b0, 18 Sep 2026) | 10,106 records | no record of Colbert 398; "Vulcob": 0 |
| GitHub code search "Colbert 398" (14) and "Vulcob" | 20 Oct 2026 | Cyphersolver vulcob1573; NoAutopilot/cipher-lab birago-nevers-1571 (Colbert 398's **numerical** cipher table tested against another cipher, no fit); no reading of Ancel's 1577 cipher |
| NoAutopilot/cipher-lab | pushed 19 Oct 2026 | "Vulcob" only in fr4735 (1573) and a comparison table for vulcob1573 |
| BravoBravoIX, pangoleen/cipher-readings, el-descifrador/cabinet-noir | 20 Oct 2026 | none (by file and repository names) |
| Fontvieille, Cahiers Jean-Mabillon 2 (2021) | text layer of the PDF | "398": 0, "chiffr": 0, "Vulcob": 1 (as Morvillier's nephew) |
| web search: printed editions of Ancel's 1577 letters | 20 Oct 2026 | none found |

## 2. Further search by the reader who made the decipherment (20 Oct 2026)
Mainly places not covered above.

| place | what was done | result |
|---|---|---|
| H-Soz-Kult conference report (L. Oberdorfer, "Kryptographie in Theorie und Praxis im deutsch-französischen Kontext (1300–1800)", H-Soz-Kult, 18.11.2024, conferencereport fdkn-151312) | blocked by a bot check; read the Internet Archive capture of 5 Dec 2024 | summary of Fontvieille's paper: the ciphered third of Vulcob's correspondence of the 1570s can be analysed, despite the missing key, through decipherments already partly written between the lines. No mention of Ancel, 1577 or these pages |
| proceedings of the same colloquium | note in the French Foreign Ministry digital library ("Art du chiffre") | "C. Desenclos, S. Externbrink, E. Szarka et J. Ulbert (dir.), *Entre France et Allemagne. Théorie et pratique cryptographiques (1300-1800)*, dossier à paraître dans *Zeitschrift für Historische Forschung*". Publication not confirmed (publisher page returned 403) |
| G. Labouchère, "Guillaume Ancel, envoyé résident en Allemagne, 1576-1615", *Revue d'histoire diplomatique* 37 (1923) | searched the Internet Archive full text (revue-d-histoire-diplomatique_1923_37, OCR) and read the relevant pages | cites "Colbert 398" 7 times; for the letter of 22 Oct 1577 it summarises only the clear-text paragraph (the Estates of Austria swearing fealty in the presence of Archdukes Ernest, Matthias and Maximilian). In the whole volume: "déchiffr" 0, "Malstet", "Varembon", "Varambon", "Borgia" 0, "chiffre" 4 (all in the sense of "number") |
| HistoCrypt 2026 (Amiens, 22–25 June) | oral programme at histocrypt.org/program/ | no paper on Vulcob, Ancel or Colbert 398 (poster titles not seen) |
| Gallica printed material | search API: "Colbert 398" (non-manuscript) | 33 hits; no title related to cipher, Vulcob or Ancel |
| all Cryptiana articles | the 287 articles linked from crypto.htm, downloaded and searched | "Colbert 398" only in GL.htm, danzay.htm, frencheastern.htm, frenchnumerical.htm (key source, Danzay's p.63, the numerical cipher, the fr.3318 comparison key); "Ancel" in frencheastern, frenchnumerical (another cipher of 1601–02), henryiii, henryiv, louisxiii. None gives readings of these pages |
| Lasry's papers | web search (Cryptologia 2026, ResearchGate, academia.edu) | nothing on Colbert 398 found (the profile lists themselves were not opened) |
| studies of Archduke Matthias's journey to the Low Countries (1577) | web search (FR/EN/DE): Malstet, Varambon, Borgia, Ancel | no use of the French ambassador's cipher reports found |

## Not checked
- The ZHF dossier (proceedings above). The table of contents of Vol. 53 (2026), Issue 1 (publisher eLibrary, 20 Oct 2026) has no cryptography article and none of the editors; later issues were not yet found on the publisher eLibrary.
- Full-text search of Google Books and HathiTrust (printed editions of Ancel's letters). The Google Books API returned 429 (rate limit) on both tries on 20 Oct 2026.
- Document lists of DECODE records (login required; the catalogue has no record of Colbert 398).
- Unpublished decipherments by G. Lasry.

## Re-check before publication (20 Oct 2026, 08:40–08:50 JST)
A reader who took no part in the decipherment re-checked the main places for anything new since the checks above. The result is still "not found".
| Place | Date / version | Result |
|---|---|---|
| Cyphersolver ledger | origin/main 0258b8ab (18 Oct 2026, unchanged) | no entry for Ancel's letters in Colbert 398 |
| Its issues | up to #51 (19 Oct 2026) | titles and bodies for "Vulcob", "Ancel", "Colbert 398": no hits |
| Cryptiana frencheastern.htm | Last-Modified 15 Mar 2026 (unchanged) | no readings added |
| GitHub code search | 20 Oct 2026 | "\"Colbert 398\"": only NoAutopilot/cipher-lab and cyphersolver; the cipher-lab hits (e.g. the numerical-cipher table in birago-nevers-1571) are those listed above |

## Re-check after publication (2026-10-20 00:56 UTC)
| place | result |
|---|---|
| Cyphersolver ledger (origin/main 0258b8ab, unchanged) and issues (up to #54) | the only issue on Colbert 398 is this repository's report (#53) |
| Cryptiana unsolved.htm (Last-Modified 2026-10-19 23:08 GMT), GL.htm (10-15), frencheastern.htm (03-15) | changes concern other items; no mention of Colbert 398, Vulcob or Ancel |
| GitHub code search "Colbert 398" | NoAutopilot/cipher-lab and Cyphersolver only (as before) |
| NoAutopilot/cipher-lab: 70 commits since 2026-10-19 12:00 UTC and ciphers/ | nothing on Colbert 398, Ancel or Vulcob |
