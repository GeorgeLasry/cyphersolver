# Chicago sweep: Pritzker Military Museum & Library, Chicago History Museum, Chicago Public Library (28-29 Oct 2026)

Result: **3 candidate rows** (`candidates.json`), all weak (importance 2, none viewed, all need an archive scan).
The three institutions hold almost no unread cipher text. Full counts per endpoint and term: `coverage.md`.
The Pritzker (Kenosha, WI), 225 finding aids: nothing. CHM and CPL each gave one or two real items.

## Method
- **CHM**: the library/archives catalogue is Primo (`i-share-chm.primo.exlibrisgroup.com`, scope `MyInstitution`). Curl cannot
  reach it, but the built-in browser can: a guest JWT from `/primaws/rest/pub/institution/01CARLI_CHM/guestJwt` and the
  `pnxs` JSON search API, called from inside the page, 3 s apart (about 60 queries; code was typed into the page, not
  saved as a script). Plus the CHM finding aids on CARLI CONTENTdm (alias `chm_fa`, `chm_cdm.py`, `chm_cdm2.py`).
- **CPL**: the site search is dynamic, so the finding aids were taken from the sitemaps: 506 `fa-*` pages (full finding aid
  text) and 239 archival summaries, all grepped (`cpl_fa_urls.py`, `cpl_fa_crawl.py`, `cpl_crawl.py`, `analyze.py`).
  CPL digital collections (CONTENTdm, `cpl_cdm.py`): newspaper and theatre noise only.
- **Pritzker**: HTML pages sit behind Incapsula, but the list of 225 finding-aid PDFs was read in the built-in browser from
  `/resources/archival-collections` and the PDFs download by curl (`pmml_crawl.py`, `pmml_list.txt`); grepped in `analyze.py`.
- Dedup with `archive_sweep_2026-10/known.py` (Walpole, Goodricke, Plum, Ruggles, Rosecrans, Chickamauga, Wilkinson,
  Army of the Potomac, Eustis); prior-art web searches for each row.
- Raw caches (`raw/`) are git-ignored. `hits.txt` and `counts.json` are the output of `analyze.py`.

## Candidates, best first
1. **Walpole (Paris) to Sir John Goodricke (Stockholm), 8 Oct 1769**, CHM Small Manuscripts, CHS MSS Alpha Walpole, Robert
   B0020C (Primo `alma991000655679709882`). 5 pp., "Cypher for portion of letter". Probably a British Northern Department
   numerical cipher; Goodricke's papers at the Bodleian reportedly hold cypher letters with transliteration (only seen in a
   search snippet; the Bodleian site refused automated access), so a decipherment may exist elsewhere. Needs a scan.
2. **Ruggles orders, 19 Feb 1864**, CPL Special Collections, Civil War documents collection spe-w00073, Box 8 Item 86.40.15.
   "orders to move troops, possibly in code". May well be clear text. Needs a scan.
3. **William Rattle Plum papers**, CHM, CHS MSS Lot William Rattle Plum B0602C #1/HB (`alma991000660089709882`): 7 military
   telegraph cipher notebooks used by Capt. W.G. Fuller and Plum, Department of the Tennessee, 1863-64, plus 389 pp. of
   Fuller's letterpress copies. Probably route-cipher tables and working copies of the published Union system (Plum 1882;
   Eckert books, `targets/eckert1862`); kept as a row because the contents are not described. Needs a scan.

## Key leads (bare keys, not rows)
- CHM, **Army of the Potomac document, Jan 1863** (CHS MSS Alpha U.S. Army. Army of the Potomac B0019H; acc. M1954.0038;
  `alma991002347399709882`): 1 page 25 x 20 cm, "Cypher and secret code of the Army of the Potomac at Washington and New York".
  Genre "Ciphers (codes)". Could key Army of the Potomac telegrams; see catalogue 834 (Hooker 1862) and Castle's journal.
- CHM, **Department of State document, 1827** (CHS MSS Alpha U.S. Department of State B0020B; `alma991002347459709882`):
  2 pp. 52.5 x 45 cm, "Cipher code used by the Department of State". A State Department code table of 1827 (compare the
  1807/JQA State Department codes in memory `state-dept-codes-1807`); could read Adams-era despatches.
- CPL, **Rosecrans to Burnside, encoded dispatch, Chickamauga, Sept 1863** (Civil War documents collection, Box 1 Item
  72.407.1) with a **1907 translation by James McCarney** (Item 72.407.2). Excluded as a row (decipherment attached), but the
  pair is a ready crib for the Union Army of the Cumberland cipher of Sept 1863 (an Official Records receipt for a "cipher
  dispatch for Major-General Burnside" signed by a McCartney is in O.R. xxx pt. 3).
- CHM, printed code books (no ciphertext): Cross' telegraphic cipher code for the provision and grain trade (1899, CHS F38PT .C8),
  Preston, Kean & Co. Telegraph code (1883, CHS F38PT .P74), National Association of Professional Baseball Leagues, Private
  telegraphic code (1933); CPL City-Wide Collection Box 6 Folder 16, "Robinson Telegraphic Cipher" (Grain Dealers Journal, 1897).
  These key commercial telegrams (Chicago grain trade) if any turn up.
- CHM holds Plum, *The Military Telegraph during the Civil War* (1882, CHS E608 .P73) and Bates, *A rebel cipher despatch* (1898,
  CHS E608 .B2): printed, with the Union and Confederate cipher systems described.

## Dead ends
- **Wilkinson papers** (CHM, mounted in volumes): Eustis letters 4 and 10 May 1809 (items 91, 93) and item 174 "numerical
  cypher notations" were already written up in `research/chi_carli_uic/` (three rows); the 12 Dec 1805 "From Burr" paper
  "Truly deciphered, F. Pinckney" has a decipherment attached. Not duplicated here.
- **Camp Douglas / Northwest Conspiracy 1864**: CHM has the 1865 "Chicago conspiracy trial scrapbook" (newspaper clippings), a
  1908 reminiscence, printed books and treason-trial reports (CHS E458.8, E459); CPL has soldier letters and photographs;
  Pritzker none. No Confederate cipher manuscript at any of the three. The Hines papers (Kentucky) and the Pitman
  trial record (cipher exhibits, "secret cipher and key") are the places for those, outside this scope.
- **Haymarket**: CHM's Haymarket Affair Digital Collection and the Parsons papers were searched by web only; no cipher found. The
  1893 Aikin cryptogram to Voltairine de Cleyre (Reddit/Schmeh) is already read and is not a CHM item.
- **Chicago Examiner 1908-18** (CPL CONTENTdm): all the "cipher/code" hits are newspaper text (puzzles, serials).
- CHM Primo hits for Febiger (1779, "perfect cypher" is a joke), Strang diary (published decipherment), Steuben, Chalmers
  ("secret writing" noise).
- Pritzker finding aids: WWII letters mention a "secret code" with family (Gralak) and cipher-machine duties (Heinrich, Rush),
  none with ciphertext.

## Not reached / blocked
- **Pritzker** website search (Incapsula; form ignores the keyword in the browser), WorldCat Discovery catalogue (spinner only),
  Pritzker digital collections (the linked CONTENTdm has no collections), oral histories (excluded by the brief),
  the rare-book room (no list).
- **CHM** images.chicagohistory.org (403) and **Chicago Collections** explore portal (Cloudflare challenge; not completed).
  Item-level descriptions for CHM finding aids not on CARLI (e.g. other Civil War and Lincoln collections) are therefore
  seen only through Primo.
- **CPL** BiblioCommons catalogue (item-level records outside the finding aids) and ~175 archival summary pages (their
  `fa-` pages were all read).
- CHM Prohibition/gangster material: no coded-message hits in Primo (queries "code message", "coded", "secret code"
  returned printed or administrative records only).
