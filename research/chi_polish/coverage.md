# Coverage log: Polish Museum of America (PMA), Chicago, and related Chicago holdings

Sweep run 28 Oct 2026 under `research/archive_sweep_2026-10/BRIEF.md`. Every source tried is listed, with what it gave.

## 1. PMA archive guide (the main finding aid)

- **Source:** *Guide to the Polish Museum of America Archives Collections* (Head Office of the State Archives,
  Warsaw / PMA, 2019; English version of the 2016 *Informator o zasobie archiwalnym Muzeum Polskiego w Ameryce*),
  e-book at `https://archiwa.gov.pl/wp-content/uploads/2022/03/PMA_EBOOK.pdf` (382 pp., 23 MB).
- **Route:** curl and WebFetch got an Imperva/Incapsula stub (no challenge page, just a JS cookie stub). The
  built-in browser loaded it without any check; the text was extracted in the page with pdf.js (750,631 chars,
  text layer clean). The PDF was not saved to the repo.
- **Search terms (regex, case-insensitive):** cipher, cypher, encipher, encrypt, decipher, decod-, cryptogra-,
  secret writing/ink/code/letter, szyfr, "in code", coded, code book, chiffr-, tajn-. **0 hits.**
- **Wider terms:** code, key, telegra-, cable, secret, confidential, intelligence, conspira-, underground,
  espionage, spy, courier, clandestin-, cyfr-, depesz-, tajny: 90 hits, all noise (secretary, "Kuryer"
  newspaper titles, telegrams of condolence, "703" collection code). One near-miss: Stanisław Ząbek papers
  (703/205) hold "operating instructions for French radiotelegraphs used during World War I" (equipment manual,
  not ciphertext).
- **Collections read in full for pre-1950 political or diplomatic correspondence** (where an undescribed cipher
  could sit): Royal Collection 703/215 (91 units, 1555-1868, royal letters: Sigismund II Augustus 1555/1566,
  Sigismund III 1597, Ossoliński 1646, John Casimir 1668/1672, Sobieski 1683/1691, Marie Casimire 1697/1710/1715,
  Radziejowski 1690/1698, Augustus II 1701/1704, Leszczyński 1708-1753, Augustus III, Stanisław August ...);
  Tadeusz Kościuszko Collection 703/213 (122 units, 1775-1818); Gen. Kazimierz Pułaski Collection 703/294
  (8 units, 1772-1779); Constitution of May 3 Collection 703/290; Polish National Department 703/8 (1916-26);
  Embassy of the Republic of Poland in Tokyo 703/11; Wacław Gawroński papers 703/161 (MFA official). None is
  described as containing cipher; item descriptions are one line each ("letter written by X to Y on Z").
- **Result:** no item the guide describes as ciphered. 211 collection titles listed (see README).

## 2. PMA online catalogue (PastPerfect Online)

- **URL:** `https://polishmuseum.pastperfectonline.com/search?search_criteria=<term>&onlyimages=false` (linked from
  the PMA site). It covers Object, Photo, Archive, Library and Container List records, but in practice almost all
  records are library books, photos and museum objects; archival letters are barely catalogued at item level.
- **Route:** curl gets HTTP 403 (bot filter). The built-in browser loads it; terms were fetched from inside the
  page one at a time, 3.2 s apart.
- **Results:** szyfr, szyfrem, szyfrowany, zaszyfrowany, cipher, cypher, ciphered, coded, codebook, cryptogram,
  encrypted, chiffre: **0 results each**. code: 89 (books, "Code name: Karski", subject codes; noise). decipher: 4
  (a genealogy handbook "Decipher German records", 3 photos). klucz: 8 (book titles; one is a Polish edition of
  Gregg shorthand). tajny: 1 (book "Tajny front"). secret: 22 (books: Karski, Dalerac's *Secret History of
  Sobieski*, etc.). telegram: 3 (the Chicago daily "Telegram Codzienny", jubilee books). **No ciphertext item.**

## 3. Web searches (WebSearch, 28 Oct 2026)

Queries and outcomes (none produced a ciphertext item):
- "Polish Museum of America archives cipher szyfr letters collection": found the 2019 guide (section 1), nothing on cipher.
- "Muzeum Polskie w Ameryce archiwum szyfrowane listy": museum news (stolen royal/Napoleon/Pułaski letters
  returned), nothing on cipher.
- "Kościuszko cipher letter Polish Museum of America": only the 1977 PMA edition *Autograph letters of Thaddeus
  Kosciuszko in the American Revolution*; no cipher mentioned.
- "Archiwalia polskie USA przewodnik Chicago szyfr": PMA guide (2019) and the 2024 guide to the American Relief for
  Poland / Rada Polonii Amerykańskiej records (Targońska, Archiwa Państwowe 2024; print only, PMA news page
  `https://www.polishmuseumofamerica.org/completion-and-launch-of-the-first-ever-guide-to-the-american-relief-for-poland-records/`).
  ARP is a relief charity (1939-1974); no cipher mentioned.
- "Polish Roman Catholic Union archives Chicago manuscripts ...": PRCUA's archive *is* the PMA (founded 1935 as the
  PRCUA Archives and Museum). Wolanin, *Polonica Americana* (1950) is a catalogue of printed Polonica, not
  manuscripts; not online.
- "polonika.pl Muzeum Polskie w Ameryce archiwalia ...": polonika.pl columns and the PMA early-printed-books
  catalogue (BN); nothing on manuscripts in cipher.
- "Chicago Polish archive coded telegrams Polish National Department 1918 ... cipher": hits are Hoover Institution
  Polish legation telegram registers (not Chicago; out of scope) and the HistoCrypt 1919-20 codebreaking paper.
- "Paderewski archive Polish Museum of America telegrams 1919 code ...": PMA Paderewski room; Hoover holds the
  Paderewski papers proper. Nothing in cipher at PMA.
- "Polish Museum of America letter 1863 insurgent secret/cipher/szyfr": nothing.
- "Polish Museum of America archives Haller army ... recruiting records": Haller's Army recruitment forms
  (Polish National Department, 703/8) are personnel forms, not cipher.
- "NDAP baza Polonika zagraniczne ... Chicago": no such searchable database surfaced; szukajwarchiwach is behind
  an Imperva human check (see research/polish_archives/README.md), not retried.

## 4. Ukrainian National Museum, Chicago

- `https://ukrainiannationalmuseum.org/archives/`: archives cover "from the beginning of the 20th century to our
  days", Chicago Ukrainian community, organisations, churches, personal correspondence. **No online catalogue or
  finding aid**; access only in person with the director's written permission. Nothing to search; not reached.

## 5. Not reached

- **ArchiveGrid** (`researchworks.oclc.org/archivegrid`): curl 403; the browser got a Cloudflare "Just a moment"
  check. Stopped there, per the no-CAPTCHA rule.
- **HathiTrust catalogue/full text**: curl 403 (Cloudflare). Not retried in the browser (shared tab cap reached).
  It would only add the 1977 Kościuszko letters edition, which is a printed edition of clear letters.
- **szukajwarchiwach.gov.pl** ("zbiory za granicą"): Imperva human check, recorded as blocked by the earlier
  Polish sweep; not retried.
- **PMA item-level inventories** ("printed inventory (working file)" for most fonds) are not online. The Royal,
  Kościuszko and Pułaski collections are described letter by letter in the guide, but only by sender, date and
  subject. An unflagged cipher passage in, e.g., a Sobieski, Leszczyński or Stanisław August letter cannot be
  excluded without seeing the items.
- **Ukrainian National Museum**: no online finding aid; in-person access only.

## Result

0 candidates. No PMA, PRCUA or UNM item described anywhere online as containing cipher, code or secret writing.
