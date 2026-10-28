# Coverage: Marshall Foundation William F. Friedman Collection sweep (27-28 Oct 2026)

## 1. The item-level guide (main source)

Rose Mary Sheldon, *The Friedman Collection: An Analytical Guide* (George C. Marshall Foundation, Sept 2014),
646 pp. It is no longer on marshallfoundation.org (the old `/library/` WordPress site is gone; the URL now returns
the library portal). Recovered from the Wayback Machine:
`http://web.archive.org/web/20220124223550/http://www.marshallfoundation.org/library/wp-content/uploads/sites/16/2014/09/Friedman_Collection_Guide_September_2014.pdf`
(first request cut at 1 MB; resumed with a range request). Text layer extracted with PyMuPDF to `cache/guide.txt`
(git-ignored).

- `parse_guide.py` splits it into **2,655 item entries** (Items 1 to 3004, with sub-items such as 796.6).
- Keyword pass 1 (cryptogram, unsolved, undeciphered, cipher letter/message, coded letter, in cipher, enciphered,
  secret writing, submitted, challenge, puzzle, treasure, mystery, decipher ...): **444 hits** (80 about the
  famous/excluded ciphers: Voynich, Beale, Shakespeare/Bacon, Dorabella).
- Pass 2 (strong words: unsolved, never deciphered, not solved, for solution, challenge, treasure, cipher letter,
  mystery): **73 items** read in full.
- Pass 3 (unsolved-status phrases: "without success", "not yet deciphered", "could not be deciphered",
  "uncompleted", "partially reconstructed" ...): **31 items** read in full.
- Pass 4 (historical correspondence: Confederate, Civil War, Clinton, Cornwallis, Franklin, Mexico, Napoleon,
  Mary Stuart, Rossignol, papal, Venetian, nomenclator, consul + photostat/letter/message): **~55 items** read.
- All of the 796 series (American Revolutionary ciphers, 796.1-796.11), 675-675.4 (Burr-Wilkinson), 677, 678-679,
  187 (Federal Army cipher books), 1956 (folder of messages sent for solution), 1064 (Hindu ciphers), 1719 (TR-Dewey
  cable), 951, 835, 822, 1040, 1931, 2023 read in full.
- Result: 10 candidate rows from the guide (Items 796.6, 796.7, 796.8, 14, 796.1, 611, 1040, 1931, 1956, 212).
- The guide describes contents; no scans of the folders are online. All guide rows are `seen: catalogue`.

## 2. Marshall Foundation library portal (Soutron), digitised items

`library.marshallfoundation.org` (Soutron Portal; results rendered by JavaScript, read through the built-in browser).

- Saved search "William F. Friedman" (userSearchId=5): 586 photograph records paged (12 pages x 50), **574 unique
  titles**; Documents facet: 19 records (digitised publications: Methods for the Solution of Ciphers, Federal Army
  Cipher Books, The Enciphered Letter, Manual for the Solution of Military Ciphers, Black Chamber annotated, ESF
  memoirs ...). Books 11, Audio 4: not opened (publications).
- Saved search "Elizebeth Smith Friedman" (userSearchId=1): 272 photographs paged, 264 unique titles; 2 documents.
- Title filter for cipher material: ~35 records; record pages fetched for **CID 1785-1836, 1907, 1910, 1966** (55
  records) with `soutron_records.py` (3 s spacing; metadata in `cache/records.json`).
- Images viewed (thumbnails ~240 px, the portal's download size): CID 1806 (Congress code letter, 5 Nov 1782), 1818
  (Davis → J.E. Johnston, Confederate), 1819 (Coded Letters, F-441, 15 of 21 prints: Egyptian cartouches, Meister's
  papal key, Argenti tables, Pepys MS, Arnold-André 1779-80), 1826 (LoC photoduplication order: Benjamin Church 1775),
  1815 (Lovell 1781, clear), 1835 (Poe note card), 1792, 1793, 1799, 1802, 1803, 1807, 1808, 1809, 1812, 1820, 1834.
- Finding: the F-series photographs (F-404 to F-590) are Friedman's lecture illustrations of famous, solved items
  (Arnold-André, Church, Davis-Johnston, Congress codes, papal and Venetian keys). **No new candidate** from the portal.

## 3. NSA "William F. Friedman Collection of Official Papers" (nsa.gov)

nsa.gov returns 403 to scripts (tested once, not retried); read through the built-in browser, pages fetched from
inside the page with 3 s spacing.

- 8 topic pages harvested: Panel/Committee/Board 2,226 rows; Correspondence 2,167; Pearl Harbor 175; Lectures 235;
  Publications 216; Patent/Equipment 1,296; Reports/Research 1,450; Supplemental 171. **7,936 document rows**
  (7,789 unique PDFs) and **665 folder titles** (11 "not releasable").
- Title filters: (a) unsolved/challenge/cryptogram/submitted/WW1/Riverbank/Mexico/rum-running terms: 183 titles;
  (b) historical terms (Revolution, Civil War, centuries, Arnold, Jefferson ...): 270 titles; (c) decipher/intercept/
  espionage/manuscript terms, excluding Japanese/machine/post-1940: 238 titles; (d) folder titles: 74. All read.
- PDFs opened (text layer via pdf.js in the page; page images rendered for two): A67090, A64707, A273674 (14 pp.,
  pp. 1 and 6 viewed), A67868, A62872, A4148539, A272888, A70100, A69348, A4148613, A40699, A4148659, A4148934,
  A4127218, and supplemental A2918506, A2918477, A2919882. **17 PDFs.**
- The collection is Friedman's official working files (1930-1955): SIS/SSA/AFSA/NSA administration, machine
  ciphers, Japanese and WWII intercepts (excluded), training texts. Result: 2 low-weight candidate rows (A273674,
  A67868). Most "historical" items are lecture slides of famous solved ciphers.

## 4. Not reached / blocked

- Internet Archive was "temporarily offline" on 27 Oct (CDX 504 later); the availability API worked on 28 Oct and
  gave the guide. The old Marshall `/library/collection/...` pages and `Friedman_William.pdf` /
  `Friedman_Elizabeth.pdf` (2012 ESF box list) have no Wayback snapshot found.
- No scans of the physical Friedman Collection folders (Items 1-3004) are online; every guide candidate needs a
  scan request to the Marshall Library (librarian@marshallfoundation.org) or the original archive (Clements Library
  for the Clinton Papers items).
- The Elizebeth Smith Friedman papers box/folder list (manuscript collection, not the photo set) was not found online.
- NSA PDFs were not downloaded to disk (direct download is 403 to scripts; navigating to a PDF in the browser
  triggers a save dialog, so text was read in-page instead).
