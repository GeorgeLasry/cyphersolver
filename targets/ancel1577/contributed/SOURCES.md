# Sources / 資料

Images and PDFs are not redistributed here. / 画像・PDF は再配布していない。

## Manuscript / 写本
BnF, Département des Manuscrits, **Cinq Cents de Colbert 398**, "Recueil de lettres originales sur les affaires d'Allemagne, adressées aux rois Charles IX, Henri III et à la reine Catherine de Médicis…". Gallica ark:/12148/btv1b525218133 (1,022 views). Images used through the BnF IIIF Image API (`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b525218133/f<view>/full/2400,/0/default.jpg`), 20 Oct 2026.

Page → Gallica view (from the IIIF manifest labels) / 頁→コマ:

| page | view | use |
|---|---|---|
| p.33 | f59 | calibration (margin decipherment) / 較正 |
| p.257–258 | f289–290 | calibration p.258 (margin decipherment) / 較正 |
| p.523–524 | f557–558 | heading "22. octob. 1577", clear text; cipher begins at the end of p.524 |
| p.525–526 | f559–560 | read here / 読んだ部分 |
| p.539 | f573 | read here ("2 novemb. 1577") |
| p.561–563 | f595–597 | read here ("14 decemb. 1577") |
| p.565 | f599 | read here ("21 decemb. 1577") |
| p.569–570 | f603–604 | p.569 has a margin decipherment, whose last line deciphers the single cipher line at the top of p.570 |
| p.284–285, 311, 321, 366, 439–440, 443, 449, 467–468, 501, 514, 599, 621 | f316–317, 345–346, 355, 400, 473–474, 477, 483, 501–502, 535, 548, 633, 655 | viewed: cipher with a contemporary margin decipherment (not read here) |

## Key / 鍵
- S. Tomokiyo (友清理士), "French Ciphers for German (and Eastern) Affairs", Cryptiana, https://cryptiana.web.fc2.com/code/frencheastern.htm (Last-Modified 15 Mar 2026; viewed 20 Oct 2026). Table image "Vulcob and Ancel's Cipher (1575-1584)" (easternVulcob.png), not included here; `data/key.tsv` rewrites it in symbol names.

## Prior work checked (20 Oct 2026) / 調べた先行
| place | version / date | result |
|---|---|---|
| Cryptiana unsolved.htm | Last-Modified 13 Oct 2026 | Colbert 398 not listed |
| Cryptiana GL.htm (George Lasry's decipherments, 56 entries) | 15 Oct 2026 | no entry for these pages; fr.3318 (1573) entry names "Comparison key … Colbert 398" |
| Cryptiana blog (all 399 posts) | latest 15 Oct 2026 | no mention |
| Cyphersolver (dbourdeau/cyphersolver), origin/main 0258b8ab | 18 Oct 2026 | only target vulcob1573 (fr.3318, Lasry) |
| Cyphersolver issues and PRs (all, latest #49) | 19 Oct 2026 | no mention of Vulcob, Ancel or Colbert 398 |
| GeorgeLasry/cyphersolver, WAINUTAI/cyphersolver (forks) | 20 Oct 2026 | no own commits on this |
| GitHub search (repositories, issues, code: vulcob, "Colbert 398", btv1b525218133) | 20 Oct 2026 | only the above, and NoAutopilot/cipher-lab keyhunt tables listing this ark as out of range for another key |
| NoAutopilot/cipher-lab ciphers/ | 19 Oct 2026 | no folder for these letters |
| BravoBravoIX repositories | 19 Oct 2026 | none |
| Cryptoole API (854 cases) | 20 Oct 2026 | no case |
| Web search (EN/FR) | 20 Oct 2026 | D. Fontvieille, "Du bon usage du chiffre par les ambassadeurs. L'exemple de la correspondance chiffrée de Jean de Vulcob, ambassadeur dans le Saint-Empire (1570–1576)", colloquium "Entre France et Allemagne : théorie et pratique cryptographiques (1300-1800)", Heidelberg, 11 Apr 2024 (programme: chssc.u-picardie.fr). Content and any proceedings not checked. |
Re-checked before publication on 20 Oct 2026 (docs/PRIOR_CHECK.en.md, last section): nothing new. Not checked: DECODE database search, G. Lasry's unpublished reports, D. Fontvieille's publications.

## Software / ソフトウェア
- wordfreq (French word list for the trigram model). OpenAI Codex CLI 0.163.0-alpha.10.2. Python 3, Pillow, NumPy.
