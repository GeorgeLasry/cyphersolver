# JACAR (Japan Center for Asian Historical Records) sweep, 27 Oct 2026

Goal: find original ciphertexts in JACAR (jacar.archives.go.jp) that are unread and not yet in the catalogue.
Result: **3 new catalogue entries (361, 362, 363)**, key leads, and a map of what JACAR does and does not hold.

## Method

`/aj/search` is server-rendered and needs no login; the browser tool gets 403 but plain HTTP works (`jacar.py`).
Parameters: `kw`, `page`, `rows` (up to 200), `sf`. Item pages `/das/meta/<ref>` carry the 内容 field, which is a
transcription of the document text, and the raw PDF is at `/das/image/<ref>` (recipe from `targets/sunyatsen/jacar_fetch.py`;
`pdf.py`, `sheet.py` here). Scripts: `jacar.py` (client), `harvest.py` (term list -> `hits/*.jsonl`),
`filter.py` (merge, dedupe, pre-1951, title filter), `details.py` (item pages), `pdf.py`, `sheet.py` (contact sheets).

28 terms harvested, 22,440 unique records: 暗号 (9,862), 暗号電報 (1,644), 暗号書, 暗号文, 暗号解読, 解読, 解読不能, 未解読,
判読不能 (2,387, mostly 'illegible' noise), 密電 (3,902), 密書 (5,380), 秘密電報, 符牒, 電信暗号, 傍受, 謎, 暗号 不明,
数字電報, 符号電報, 電報 検閲, 暗号表, 暗号 外国, 隠語 and others, plus ten multi-word probes (意味不明 暗号電報, ソ連 領事館 暗号電報 ...).
The search is AND over words and also matches 内容, but the hit lists are dominated by administrative records about
cipher *use* (telegraph rules, code-book issue and burning, radio intercept logs), not ciphertext.

## What JACAR holds

Almost all cipher material is Japanese: army and navy code books, issue and destruction reports, and Japanese
decipherments of others' traffic (Soviet and Chinese weather codes 1938-40, C01004816xxx and C04120906900; the Kurama
incident intercepts 1920, C10080363300, which carry Japanese translations; the Moscow weather codes with 乱数表 solutions).
Those are read, so they are not catalogue material. Foreign ciphertext appears only where a police or consular file
copied out an intercepted message.

## Second pass: description scan (27 Oct 2026)

The record text (内容) is a transcription of the document, so ciphertext in digit groups is searchable after the fact.
`scan.py` fetched the item page of 4,136 records (all B-series hits to 1945 plus every A/C hit whose title mentions
telegram, cipher, intercept or decipherment) and scored runs of four- and five-digit groups (`scan_hits.jsonl` keeps the
records with 4 or more groups; the full `scan.jsonl` is git-ignored). Only 7 records had 4+ groups: the Hakodate file,
the 1901 Fukushima telegrams, the 1914 Newcastle telegram, and four false positives (book lists, a cable log, an
instruction on the Army information code book). Flagged 'meaning unknown' descriptions led to the sibling volume
B14090579100 (more Hakodate telegrams). The earlier remark about 'volume-level records' was wrong: every hit is an item.
104 fetches failed once and were retried.

## Added to the catalogue

* **id 361, B14090576500 + B14090579100**: Soviet consul at Hakodate (Kiselev) and trade offices, five-digit-group telegrams
  copied by the Hokkaido police, Oct 1929 - Apr 1930, about 8 telegrams over 7 + 2 frames, 'meaning unknown', no key. Class C, 3/2/5. Viewed.
* **id 362, C09122808300 / 808400 / 809400 / 810100 / 812300**: Army General Staff telegrams with Yamaguchi and Fukushima in
  China, Feb-May 1901: five-digit groups plus enciphered romaji, about 73 groups, no key. The clear telegram of 8 Mar
  (C09122810200) is a possible crib. Class C, 3/2/4. One record viewed.
* **id 363, C11080235200**: Japanese Navy numeral telegram to HMS Newcastle, 20 Aug 1914, 38 groups. Class C, 2/1/5. Not viewed.

## Key leads (keys or tables, no ciphertext; they can read other traffic)

* **C01004002600** (1933, 155 frames): Soviet trade-mission code obtained by the gendarmerie at Hakodate. Probably the
  family of the 1929-30 telegrams above; look at it first when working entry 361.
* **C06031209700** (1922, 16 frames): cipher tables of Soviet Primorye communist agents and Red army units (Russian letter ->
  two-digit number, some syllables). **C06031133000** (1921): Korean independence groups' argot word list.
  **C06031196100** (1919): Korean secret oath plus a sign table found in a wallet at Harbin.
* **C01003763300 / C01003762400** (1927): KMT kana-telegram code tables supplied by the Kwantung communications bureau.

## Already in the repository (excluded)

Sun Yat-sen telegrams: B03050738800, B03050731500, B03050088300-B03050090200 (`targets/sunyatsen/`).

## Not done

* No web search for a published reading of the Hakodate telegrams.
* Titles are the only filter for the 9,862 暗号 hits; a record whose title says nothing about cipher but whose frames hold
  one (the Hakodate file's title does say so) would be missed. Volume-level (簿冊) records, where a whole file is one hit,
  were not opened: 144 undated volume hits are in `cands_raw.json` (git-ignored).
* The Chongqing broadcast, Moscow weather and Chinese air-force weather series were judged read or non-cipher from titles and
  descriptions and not opened.
* Records after 1950 and the Imperial-Japanese-only code series were left out.
