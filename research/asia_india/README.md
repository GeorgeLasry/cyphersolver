# National Archives of India (Abhilekh Patal) sweep, 28 Oct 2026

Goal: find digitised records in the National Archives of India (abhilekh-patal.in) that contain ciphertext, 1600-1950,
that may be unread. Result: **18 candidate rows** in `candidates.json`, all scored from catalogue metadata only (the
page images need a login, which this sweep did not use). Most of the strong leads are East India Company secret
consultations of 1779-1813 and three intercepts (Mandalay 1879, Nanking-Lhasa 1930, a 1799 enclosure).

## Method

The portal is now an ASP.NET Core front end over DSpace 7 (the old `/jspui/` routes return 404). No login is needed
to search; the item metadata is public; the page images are not (see Blockers).

* `AdvanceSearchV3?<field>=<value>,contains&sort=...` returns the first 10 hits and `Page.TotalElements`.
  Several fields are ANDed (`title=cypher,contains&keywords=Kabul,contains`). Multi-word values are phrases.
  The free-text route `QuerySearch?query=` applies fuzzy matching (`cypher~0.7`: 8,145 hits), so it was not used.
* `PaginationScroll?<same>&number=N&viewtype=list` (XHR) returns page N as JSON `{partialView: html}`; page size is
  fixed at 10. The default sort (accession date) repeats and skips items across pages; `sort=dc.title,asc` is stable.
* `Category/ItemDetails/ItemDetails?itemId=<uuid>` carries the record as escaped JSON: department, branch, file
  number (e.g. "Cons. 28 July 1788; No. 5"), pages, and auto-extracted **keywords**, which come from the page OCR.
  That keyword field is the only route to items whose titles do not mention cipher.

Scripts: `ap.py` (search client, paged harvest), `narrow.py` (first-page-only queries under four sorts, used
while paging was blocked), `details.py` (item metadata -> `details.jsonl`), `make_candidates.py` (hand-curated rows
-> `candidates.json`). Raw hits: `hits_old/*.jsonl` (first pass, unstable sort), `hits/narrow.jsonl`,
`hits/title_cypher_dateasc.jsonl`; `narrow.log` lists each query with its hit count.

### Hit counts (title field unless stated)

cypher 4,505 (stemmed: cyphered, decypher fold in); cipher 365; decypher 70; decipher 42; undeciphered 7;
cryptogram 4 (all "Cryptogam Botanist"); secret writing 5; secret character(s) 3; invisible ink 2 (1971);
sympathetic ink 13; ramz 6 (Urdu poetry titles); رمز 0; intercepted 3,057; intercepted letter 297;
intercepted telegram 41; code book 17; secret code 6; Ghadr 195, Ghadar 80 (no cipher titles; Ghadr + keyword
cipher/code/key: 0); Silk Letter 33; keywords=cypher 1,656, keywords=cipher 660; subject=cypher 302, subject=cipher 101.
About 2,300 records were read (title, year, identifier, pages, keywords) and about 70 queries were run with
title=cypher/cipher ANDed with a place or subject keyword (Kabul, Amir, Persia, Kashgar, Tibet, Nepal, Mandalay,
German, Russian, Holkar, Sindia, Mysore, Lahore, French, key, Resident and others).

### What the hits are

Nearly all the cypher/cipher titles (well over 95%) are the Government of India's own administration of its codes:
safe-custody reports, distribution lists, issue and withdrawal of Foreign Office and India Office cyphers, keywords
for the Civil Cypher System, paraphrase rules, cypher-branch staff. Those are out of scope. The ciphertext-bearing
files are the eighteenth- and early nineteenth-century Secret and Political consultations (found through the OCR
keywords), a few intercept files, and Persian letters whose machine-translated titles mention a secret code.
Government telegram files titled "Decypher of telegram" (1933-42) carry the decypher and were dropped as read.

## Best leads (ranked)

1. **1930, External Affairs, Sikkim (Political) 5-P, NAIDLF03824535** (49 pp.): interception of cypher telegrams
   from Nanking to the Dalai Lama. Could be plain Chinese telegraph code (easy) or an enciphered code. 3/2/3.
2. **1879, Foreign Dept Secret Progs Nov 1879 Nos. 233-34 and 276-78; Notes C-983**: cipher telegrams between the
   court of Mandalay and Italian/Swiss agents (Genoa, "Durazzo Adorno"), and "steps taken to decipher" them. 3/2/4.
3. **1802, Foreign Secret Cons 23 June 1802 Nos. 90-91**: Barry Close (Poona) to Wellesley on Holkar, "partly in
   cypher code". Martin's *Wellesley Despatches* vol. 3 was grepped and does not print it. 3/3/3.
4. **1799, Foreign Secret Cons 8 Apr 1799 No. 29**: enclosure from the Persian Translator; OCR keywords Cypher,
   Colonel, Vieux. Possibly an intercepted French or Tipu letter on the eve of Seringapatam. 3/2/3.
5. **1788, Foreign Secret Cons 28 July 1788 No. 5**: enclosure in Capt. Kennaway's private letter (Hyderabad
   mission), keyword Cypher. Sibling: "Decyphered copy of a letter from the Resident with Mahadji Sindia",
   Secret Cons 25 Jan 1788 No. 4 (NAIDLF00942662), a decipher of the same years' residency cipher. 3/2/3.

The other OCR-keyword rows (1779, 1788, 1796, 1807, 1808, 1809, 1813, 1853) are Calcutta's secret letters to Madras,
Bombay, Penang and Admiral Elphinstone; the keyword shows a cipher is mentioned, not that the text is in cipher.

## Key leads (keys, code books, decipherments; no ciphertext of interest)

* **"Cypher Code Book", 1777**, Home Miscellaneous Vol/88, 73 pp. (PR_000006128785, duplicate record
  PR_000004044749): the East India Company's Fort William cypher of Hastings's time. The first thing to try on any
  1777-1800 Company cipher passage in these consultations.
* **Decyphered copy, Resident with Mahadji Sindia, 8 Jan 1788**, Foreign Secret Cons 25 Jan 1788 No. 4
  (NAIDLF00942662, 8 pp.): a decipher, so a crib for the 1788 Company cipher.
* **Major Biddulph's cipher for Gilgit**, Foreign Secret Progs May 1880 Nos. 50-52 (NAIDLF02189603).
* **Tipu Sultan's name cipher** with the Carnatic Nawabs (key captured at Seringapatam 1799): printed in Martin,
  *Despatches of the Marquess Wellesley* vol. 2 (archive.org in.ernet.dli.2015.173336, around the Carnatic inquiry).
* **"Introduction of a Letter Cypher for the use of District officers"**, 1891 (NAIDLF00136743, 51 pp.); "Punjab
  Cryptograph" for militia posts, 1904 (PR_000006228846); "Transposition cipher code", 1939 (NAIDLF00679439); Playfair
  system for the Rajputana states, 1942 (NAIDLF03436754); key sentences for the Indian Army Transposition Cypher,
  Aug-Dec 1922 (PR_000004050806); key words for the Civil Cypher System (several files 1907-1952).
* Sympathetic-ink news-letters of the British Agent at Kabul, 1886 and 1891-92 (NAIDLF00567285, NAIDLF00567424,
  PR_000006228794): secret ink, not cipher.

## Dead ends

* "Undeciphered" in titles mostly means an illegible seal (Hyderabad revenue papers, OR_ series). The 1812 Home
  Public item is kept at importance 1 for one look.
* "Mr. Read's proficiency in deciphering the Flash letter", Home Public 13 July 1826 No. 46: reading a difficult
  script (a College of Fort William test), not a cipher.
* Intercepted-letter files (297) are censorship copies of clear letters (Gandhi, Nehru, Congress, Afghan officials,
  1902-1946); none says cipher. "Intercepted letters from hostile foreigners in Afghanistan", 1920 (PR_000006071120)
  and "Maulvi Bashir ... to the King of Afghanistan", 1934 (PR_000004242835) could be checked for cipher.
* Ghadr / Ghadar / Silk Letter / German plot titles: no cipher in any title or keyword. The Silk Letter file (1918,
  233 pp., PR_211200019101) holds the Persian silk letters, which are clear.
* 1913 Kashgar "copy of the figures of a cypher telegram" (PR_000006222227): the British consul's own telegram.

## Cross-check with QDL

`research/qdl/` holds only a harvest script, no candidates yet, so nothing could be deduplicated against it. NAI
holds the Calcutta side (consultations), the British Library IOR holds the London side; the same despatch can exist
in both. When QDL rows exist, compare by date and correspondent, not shelfmark. `known.py` finds none of these
items (NAIDLF, abhilekh, Kennaway, Barry Close, Lhasa, Mandalay, Elphinstone, Prince of Wales Island: no hits).

## Blockers and what was not reached

* **Images need a login.** The item page posts to `/Category/itemdetails/ReadContent`, which requires an
  Abhilekh Patal account. No login was used, so no candidate was viewed (`seen: catalogue` throughout), and whether
  each file holds ciphertext, and whether it has a decipher, is unconfirmed. Solvability is capped at 2-3 for that reason.
* **Rate limit.** Two parallel paged harvests drew HTTP 403 from the CloudFront WAF on `PaginationScroll` after about
  ten minutes; the first-page route stayed open. Paging came back about an hour later. The client now waits 4-8 s
  between pages and stops on 403. The server also returns 500 on date-filter parameters and is slow (10-30 s/page).
* **Not harvested in full:** title=cypher (4,505) was paged only to 691 records (stopped by hand at the end of the sweep); keywords=cypher (1,656) and
  keywords=cipher (660) were only sampled (first page under four sorts). The OCR-keyword route is the productive one
  for 1770-1860 consultations and should be paged in full, slowly, sorted by title.
* No Hindi/Urdu/Persian-script search beyond رمز (0 hits); Persian letters are catalogued with English machine
  translations of their titles, so "secret code" in English found one.
* The Calendar of Persian Correspondence was not checked for the 1787 and 1808 Persian letters.
