# US historical societies and university finding aids sweep (28 Oct 2026)

Part of the Oct 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`), with the owner's scope update: American
material is in scope (region "Americas", up to 1950). Output: `candidates.json` (21 rows, built by `make_candidates.py`).
`raw/` (harvests, EAD caches, 94 MB) is git-ignored by `research/us_societies/.gitignore`. None of the rows was viewed on
an image; all are scored from finding-aid text.

## Method and counts

| Source | Route | Terms | Hits | Result |
|---|---|---|---|---|
| **PACSCL "Philadelphia Area Archives"** (findingaids.library.upenn.edu, Blacklight `records.json`) | plain HTTP, 3 s spacing | 20 phrase terms | 36 "cipher", 17 "cypher", 3,228 "in code" and 896 "encoded" (stemmed, dropped), ~70 distinct records read | Aggregates HSP, Penn, Princeton, Haverford, Swarthmore, Lehigh, Drexel, PMA, Library Co. and others. Full record pages fetched for every hit and grepped. 4 rows |
| **Princeton** (findingaids.princeton.edu, `catalog.json`, `catalog/<id>.xml` EAD) | plain HTTP | cipher, cypher(s), "in cipher", "partly in cipher", "code letter", "coded letter", undeciphered, secret cipher ... | 44 cipher, 10 cypher, 12 undeciphered | 28 collection EADs fetched whole and grepped. The De Coppet Collection (item-level calendar of Revolutionary and Civil War autographs) gave 2 rows |
| **UNC Southern Historical Collection** (finding-aids.lib.unc.edu, `catalog.json`) | plain HTTP | same list | 59 "cipher" (almost all arithmetic "cipher books"), 4 "cypher", 11 phrase hits | 4 rows (Confederate letters, Gordon 1877) |
| **Massachusetts Historical Society** (solr behind masshist.org/search: `/projects/api/index.php/solrsearch?terms=...&configURL=/projects/api/configs/sitewide.json`) | plain HTTP | 11 terms | 1,100 records (574 Adams Papers digital edition, 226 JQA diary, 61 collection guides, Winthrop, Paine, C. F. Adams diaries) | Adams Papers / JQA / Winthrop Papers / Founders-type editions are printed and read, left out. 4 rows from collection guides and the Paine edition notes |
| **Harvard HOLLIS for Archival Discovery** (hollisarchives.lib.harvard.edu `/catalog.json`) | built-in browser, same-origin `fetch` (script ran in-page, 2.5 s spacing) | 18 phrase terms | cipher 80, cypher 36, "in cipher" 19, "in code" 24, cryptogram 8, "cipher telegram" 4 ... ~170 distinct | Houghton autograph files give 6 item-level rows, plus the Georgian government-in-exile series. Mostly book-plate "cipher" (monogram), Baconian and ciphering-book noise |

Terms: cipher, cypher, "in cipher", "in cypher", "in code", "partly in cipher", cryptogram, "secret writing", "coded message",
"coded letter", "code letter", "cipher letter", "key to the cipher", "written in cipher", ciphered, "cipher key",
undeciphered, "not deciphered", deciphered, "cipher telegram", "secret code", "secret cipher". Harvesters:
`bl_harvest.py` (UNC, Princeton), `mhs_harvest.py`, `pacscl_harvest.py`, `pacscl_ctx.py` (page-text greps),
`ead_grep.py`, `ctx_dedupe.py`, `show.py`. Harvard ran as a pasted in-page script (not saved; terms above).

## Noise (the reason the yield is low)

- "cipher book" / "cyphering book" = an arithmetic exercise book (about 50 UNC records, 10 Harvard, PACSCL county societies).
- "cipher" = monogram (book-plate ciphers in the Houghton Britwell/Mandeville listings, Tughra, royal cypher on stationery).
- Baconian "cipher" literature (Gallup, Bowditch, Kittredge, Covington, Newbold on Voynich - famous, skipped).
- "Code" = law code, zip code, code of conduct; "in code" and "encoded" are stemmed to EAD "encoded by" credits.
- Edited, printed collections: Adams Papers, JQA diary, Winthrop Papers (letters "in cipher" are read by the editors),
  Founders-type material, Holls telegrams (translations present), Hay 1899 telegrams (decoded copies).

## Best leads (ranked)

1. **Torcy to abbé Gaultier, London, 1711-14** (Penn Ms. Coll. 579): 79 letters "entirely or partially in cipher", with the
   original keys in the collection. French, Utrecht negotiations. Not in repo or DECODE. Digitisation unknown.
2. **Department of State (Monroe) to Barlow, 16 Jun 1812** (Princeton De Coppet C0063, box 26 f. 12): 2 pages "undeciphered
   code". The 1811 State Department code is keyed at NARA M34 v.16 (research/nara_triage_a), so this is a key-alignment job.
3. **Louis XIV to Catinat, 29 Aug 1691, "secret letter, partly in cipher"** (Houghton, Bliss autograph collection);
   Tomokiyo lists Catinat's 1691 code as unread.
4. **John Covert's code ledgers** (Philadelphia Museum of Art, fully digitised; key reportedly in the puzzles series; runs to 1959).
5. **Washington (probably) to Greene, Newburgh, 23 Apr 1782, "largely in cipher"** (De Coppet box 36a f. 37, digitised);
   check Founders Online first, it may be printed decoded.

Also: Charles V to Lope Hurtado, Regensburg 1532, partly in code (Houghton Autograph File K); Bestuzhev-Riumin cipher
documents 1742/1744 (Houghton, Vitte album); Georgian government in exile 1921-32 (Houghton microform, dozens of "Letters
in cipher" folders); Lehigh Johnston telegram letterbook 1912.

## Key leads (keys / material, no ciphertext)

- Princeton Tallmadge Collection (C0243): photostat of Tallmadge's secret-service code, correspondence with Washington.
- Princeton Rush Family Papers (C0079, box 37): "Code, or Cypher, for Correspondence Issued by Department of State", undated.
- Princeton Beauharnais Collection (C0645, military reports 1814): an undated cipher sheet.
- Princeton Cliosophic Society (AC016): partial key to the "Clio Secret Cipher", c. 1820, with a folder of the cipher.
- Princeton Woodrow Wilson Collection (MC168): "Mr. Polk ... Cipher Cable-Green Code", 10 Mar 1919 (State Dept Green code).
- Gratz autograph collection (HSP): "Nathan Arnaut's Cipher" among William Maclay's drafts.
- Harvard: PBK Alpha of Massachusetts laws with "key to the cipher" (hua47013, c. 1799-1816); Rocky Fork cipher
  code book (Baker Library bak00046); Gamble notebooks already decrypted by Erik Uzureau 2009-10 (Schlesinger sch02126).

## Seen and left out

- Princeton De Coppet: Barnabas Deane to Greene 3 Sep 1781 (number code, decoded copy printed in Greene Papers IX),
  Humphreys 1791 and Short 1790 (interlinear decipherments), 1778 and 1796 letters "deciphered", Civil War telegraph
  notes marked "Cipher" (Grant to Ord, Stanton, Thomas, Wallace, 1865; one-line notes, deciphered originals).
- Harvard: Prince Charles Edward's 1744 "Malloch" letters (cypher *name* only); Holls papers (cipher telegrams with
  transcriptions); Hay telegrams 1899 (translations); Gamble notebooks (decrypted).
- MHS: Winthrop Papers letters "in cipher" (read by editors, Martha and John Winthrop Jr.), Edward Howes "secret
  writing" (read, printed); Adams Papers cipher items (printed, decoded); C. F. Adams diary mentions of ciphered despatches.
- UNC: Berry Benson (codes, cryptograms: hobbyist, handwriting expert), "Cipher Explanation by E. Wray Martin c. 1890",
  M.C.S. Noble Masonic ritual "partly in code" (not a row: ritual, not correspondence).
- Skipped by the other US sweeps' ground: research/us_*, chi_*, nara_*, founders_emlo.

## Blockers and sources not reached

- **ArchiveGrid** (researchworks.oclc.org/archivegrid): Cloudflare Turnstile; the built-in browser sat on "Performing
  security verification" and curl got 403. Not bypassed. ArchiveGrid was the planned catch-all, so every repository below
  that is not reached otherwise remains uncovered.
- **Duke Rubenstein / archives.lib.duke.edu, Columbia (findingaids.library.columbia.edu), TARO / Texas State Library
  (txarchives.org), Cornell RMC**: Anubis proof-of-work or SPA with no discoverable search endpoint. The built-in browser
  passed Anubis at txarchives.org, but its `/api/finding_aid/search/` returns the full 10,000-record list ignoring query
  parameters; a POST/filter route was not found in the time available.
- **Yale archives.yale.edu**: 403 (the Beinecke sweep covered Yale through Quicksearch; see `research/us_beinecke_folger`).
- **American Philosophical Society** (search.amphilsoc.org, amphilsoc.org): 403 for scripts. APS holdings appear in PACSCL
  only if the finding aids are there; none surfaced. **Gilder Lehrman** (403), **Smithsonian SOVA** (403), **Newberry**
  (see chi_newberry), **Virginia Heritage / Library of Virginia / VMHC** (AWS WAF 202), **New-York Historical** (ArchivesSpace
  host unreachable), **Maryland Center for History and Culture** (host unreachable), **SC/GA/NC state archives**, **AAS**
  (site search only, no finding-aid text search), **Wisconsin, Cornell, Michigan** (Michigan done by Clements).
- **Granularity.** Most finding aids describe folders or whole papers; a single cipher letter inside "correspondence" is
  invisible. Only the item-level calendars (Princeton De Coppet, Houghton autograph files, MHS Paine edition) expose such
  items. Several rows therefore rest on a single phrase in a collection scope note.
- Browser tabs are shared with other sessions; the harvest ran in its own tab.
