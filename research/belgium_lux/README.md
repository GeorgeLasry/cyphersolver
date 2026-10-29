# Belgium and Luxembourg sweep (28 Oct 2026)

A sweep of the State Archives of Belgium (Archives de l'État / Rijksarchief, AGATHA) and the Archives nationales de
Luxembourg (ANLux) for undeciphered ciphertexts, aimed at the Spanish (and Austrian) Netherlands traffic. It produced
25 candidate rows (`candidates.json`, brief: `../archive_sweep_2026-10/BRIEF.md`). None has been opened or viewed:
every row is `seen: catalogue`. Every row carries `needs_archive_scan` and `access_note`: 24 rows are `yes`
(nothing online: reading room, scan order or e-mail request), 1 is `partly` (Cobenzl index cards on DiVa).

## Method

### Belgium: AGATHA (agatha.arch.be)

- `search.arch.be` is retired and now redirects to an end-of-life notice. Its successor, **AGATHA**, searches at
  inventory level only. POST the form to `/en/search/ead/results/` (fields `FREE`, `HOLDING`, `HEADING`), then page
  through `POST /en/search/ead/ajax.php` with `method=getResults&pageNumber=N&pageSize=50` in the same PHP session
  (`list_inventories.py`).
- Each inventory exports as full EAD: `GET /en/data/ead/<eadid>.ead.xml`. The item-level search therefore runs
  locally. `fetch_ead.py` downloaded **649 inventories** (540 MB in `ead/`, git-ignored): every inventory under
  headings A1 (Spanish/Austrian Netherlands, 219), A2 (Liège, 34), A3 (Stavelot, 1), B (regional ancien-régime, 131)
  and I13 (Foreign Affairs, 31), plus the free-text hits before 1900 for `chiffr*`, `déchiffr*`, `cijfer*`,
  `ontcijfer*`, `geheimschrift` and `chiffré*`.
- `grep_ead.py` walks every component (with its parent chain) for cipher words in French, Dutch, Spanish, German,
  Italian and Latin, and drops number and statistics noise. The result is 342 hits (`ead_hits.json`), cut by hand to about 30
  real ones (`hits_review.txt`, then the rows below). `context.py <eadid> <regex>` prints a hit's ancestors and children.
- Second pass: the envoy series of the SEG summary inventory, the SEA and the Audience core archive, where cipher is
  likely but the inventories never say so (`context.py ... "ambassad|envoy|gezant|résident"`).
- **Images.** DiVa scans (`/data/images/550/...`, a Mirador viewer) need a free AGATHA account. I did not create one.
  Most ancien-régime series are not scanned. Only 48 of the 416 heading inventories have any digitised item, and of
  those only the Cobenzl index (47,414 cards), the Starhemberg index (506) and the Vienna–Brussels ministerial
  correspondence (358) concern diplomacy.

### Luxembourg: ANLux (archives.services-publics.lu, Archeevo)

- The portal's search pages redirect to the eAccess (LuxTrust/GouvID) login, but its JSON API answers anonymously:
  `GET /api/descriptions/search?filter.*.ContainsAllWords=<term>&page=N&perPage=100` (total in `Total`);
  `GET /api/descriptions/<ID>`; `GET /api/descriptions/<ID>/representations` (file list, `Published` flag).
- `lux_harvest.py` runs 33 terms (chiffre/chiffré/déchiffr*, Chiffre/chiffriert/Geheimschrift/Ziffer, cifra, cijfer,
  code, câble chiffré ...). That gives 475 unique hits (`lux_hits.json`). Almost all are "chiffre d'affaires", Roman numerals,
  COLUMETA steel-cartel telegraph codes (1949-64, commercial code books, out of scope) and statistics.
- ANLux's ancien-régime holdings (Conseil provincial, Trois États, abbeys, seigneuries) have **no cipher hit**: the
  Spanish Netherlands government correspondence for the duchy sits in Brussels, not Luxembourg. The State Archives in
  Arlon (AGATHA holding 521) were covered by the Belgian pass and gave nothing either.

## Best leads

| # | Item | Date | Why it stands out |
|---|---|---|---|
| 1 | Audience 1409/18, Nicolas Perrenot de Granvelle (ambassador in France) → Margaret of Austria, "gecodeerde brieven" | 1526-27 | Charles V's embassy after Madrid and Cognac; no decipherment noted; keys 1520-1621 in Audience 646/1. Check Devos (1950) first, who studied the 1521-27 Habsburg ciphers |
| 2 | La Boëssière-Thiennes 1487 (Mons), Guillaume Portugal, secretary of the Spanish legation in Prague, "correspondance chiffrée" | 1619 | Oñate's embassy at the outbreak of the Thirty Years War |
| 3 | Famille d'Ursel: Archduke Albert → Hoboken, ambassador in England, one letter in cipher, **with "Chiffre pour le baron d'Hoboken", 20 Mar 1605** | 1605-09 | Class A: key and text in the same fonds; Hoboken's despatches in Audience 365 may use the same key |
| 4 | SEG 1051 ff. 358-380v, J. J. Zamboni, news from London to Botta Adorno, "en partie en chiffre" | 1751-52 | Only item in the modern (2013) Botta inventory flagged as cipher |
| 5 | SEG 314-451 and 602-606, the Cardinal-Infante's correspondence with his ambassadors (Castañeda, Oñate, Melo, Necolalde/Cárdenas/Velada/Malvezzi, Saavedra Fajardo, Castel Rodrigo, La Roca) and Brun–Peñaranda | 1633-50 | The core Spanish Netherlands cipher traffic. Not on DECODE (DECODE has only SEG 2559 and 1236); keys in SEG 2 (DECODE R958-R965) |
| 6 | Cobenzl ministry index (DiVa), cards headed "Correspondance chiffrée" from Vienna | 1753-67 | Scanned index points to the letters; van Swieten → Cobenzl (SEG 1236) already read here |
| 7 | Mercy-Argenteau 799 (Liège), "code de chiffrement et pièce cryptée" | late 17th c. | Small self-contained key + text |
| 8 | Bournonville 5/16, ciphered service letter | 1674 | Imperial general on the Rhine against Turenne |

## Key leads (keys and decipherments, no ciphertext)

- **Audience 646/1-3, "Sleutels voor cijferschrift" 1520-1621, 1533-1615, 1535-1692**, the Brussels government's own key
  collection. The French analytic inventory (BE-A0510_000799_003354) itemises 646/BIS: keys of Gabriel Sánchez (secretary of the
  King of the Romans), Antoine Perrenin, Ferrante Gonzaga, the Empress, the ambassadors in Rome, Venice, Milan and
  Genoa, Bousschot (England 1575), Thomas Gramaye (1609), Pierre de Visscher, Fürstenberg ... **Not on DECODE.** This is
  the most useful find of the sweep: it could key many open Habsburg items in the catalogue (Charles V and Philip II
  ambassadors).
- SEG 2 "Chiffre de la correspondance secrète. Liasse de chiffres divers. 1647-1698" = DECODE R958-R965; SEA 1
  "Chiffres et sigles (cryptographes)" = DECODE R937-R953 (already known).
- SEG 3 "Discours sur l'art de déchiffrer sans clef ...", printed by J.-P. Devos and H. Seligman, *L'art de
  deschiffrer* (1967). Also Manuscrits divers 676, "Traité de l'art de déchiffrer", end of the 17th century.
- Audience 92: Nicolas Perrenot de Granvelle → Charles V, 3 Jan - 31 May 1543, ciphered copies **with decipherment**
  (closed as a target; a key source for 1543).
- Manuscrits divers 874: 19th-century decipherment of J. B. de Tassis (Paris) → Parma, 12 June 1584; 665: copy of
  Tassis–Philip II 1581-83. These give cribs for Tassis cipher items elsewhere (catalogue has Tassis → Farnese 1583).
- Liège, Conseil privé 5: "Chiffre en usage pour la correspondance diplomatique" (18th c.). Ghent Jesuits 55/12:
  "Sleutel voor het ontcijferen van geheime brieven" (17th c.). Béguinage Saint-Christophe (Liège) 1485: "Code chiffré" (18th c.).
- Royal Palace, Archief Mexico (Félix Eloin) 302: code for Maximilian's cabinet despatches, 1864-67.

## Dead ends and exclusions

- Broqueville 400 (WWI telegrams, "transcription en clair"), Carton de Wiart 1078 (Bucharest telegram 1916,
  "décodé"): clear only, excluded.
- Eupen 32/40 (1788 ban on declarations "en chiffre"), Huy and Hainaut "feuillets chiffrés" (foliation),
  "basse chiffrée" (music), "cijfermuziek", Belgacom/elections/statistics: false positives.
- Luxembourg COLUMETA telegraph code books (ARBED, 1949-64): commercial codes, out of scope.

## Not reached

- AGATHA's item-level search inside the 3,000-item Conseil privé and Chancellerie autrichienne cartons only finds
  what the inventory text says; the envoy series need images.
- The Archives of the Royal Palace and the Foreign Affairs archive of the Belgian ministry (not State Archives;
  diplomatic archives at Egmont) were only touched through AGATHA's copies of their inventories.
- Bibliothèque royale (KBR) manuscripts and the Bibliothèque nationale de Luxembourg: not swept.
- AGATHA account: the DiVa images (Cobenzl index cards) can be viewed once someone signs in. ANLux images need an
  eAccess login or an e-mail request.
