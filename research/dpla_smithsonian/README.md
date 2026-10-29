# DPLA and Smithsonian sweep (28 Oct 2026)

Part of the Oct 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`), scope widened to the Americas, up to 1950.
Output: `candidates.json` (22 rows, written by `make_candidates.py`). Nothing in catalogue.json, docs/ or git was touched.
`hits/` (raw DPLA matches, 812 files), `si_bulk_hits.jsonl`, `si_hits.json` and the `stage*.json`/`*.txt` triage files are
working data and should stay out of git (about 140 MB of `hits/` is not needed after merging).

## Method and why not the APIs

- **DPLA API** needs a key mailed to an address; I did not register one. Instead I used DPLA's public bulk export
  (`s3://dpla-provider-export/2026/10/all.jsonl/`, 812 gzip parts, about 91 GB, every hub), streamed and filtered on the fly
  by `dpla_bulk.py` (14 parallel workers, nothing stored but matches). Raw prefilter, case-insensitive, over the whole record:
  cipher, cypher, cryptogra*, secret writ*, decipher, in code, coded, code book, chiffr*, cifra, secret alphabet. NARA records
  (`nara--` ids) were skipped, as NARA has its own sweeps. Result: 135,193 matching records (116,531 are Harvard Library
  catalogue noise, mostly "coded"/"chiffre"), covering 39 hubs.
- **Smithsonian Open Access**: the API with `DEMO_KEY` returned 429 after about 15 requests (limit 10 per hour for that key), so
  the first harvest (`si_harvest.py`, `si_hits.json`, 10 terms) was abandoned for the public S3 bulk metadata
  (`smithsonian-open-access.s3-us-west-2.amazonaws.com/metadata/edan/<unit>/`). `si_bulk.py` streamed 20 units (aaa, acah,
  chndm, cfchfolklife, eepa, fbr, fs*, hsfa, naa, nasm, nmaa, nmaahc, nmah, nmai, npg, npm, sia ...; not the natural-history
  units) and kept 1,579 matches. The unit `sil` (Smithsonian Libraries, printed books) was still running at the end and
  is not needed: printed books are out of scope.
- Triage (`load.py`, `show.py`, `leads.py`): date filter (year <= 1950 or undated), then a tight regex (cipher/cypher as a
  word, cryptogra*, secret writing, "in code", "coded letter/message/telegram...", code book, "deciphered the letter ...");
  noise removed (artist's and owner's "cipher" monograms, Cypher/Cyphers surnames and St., "cipher book" = arithmetic copybook,
  royal ciphers, cryptogams, building codes). Stage 3 left 2,059 records, of which 661 Smithsonian objects, 413 HathiTrust,
  271 Getty and 62 Internet Archive printed books and 49 Rumsey maps were set aside as not ciphertexts; about 930 lines from
  the other hubs were read by eye (`s3_view.txt`), plus a second pass for Spanish/French/German and "undeciphered" terms
  (`s4.txt`). Leads were opened as full records (`leads.py`), deduped with `known.py`, and the strongest got a web search.
- Hubs seen: Smithsonian, Digital Library of Georgia, Plains to Peaks, DigitalNC, Minnesota, California (Calisphere), Wisconsin,
  Tennessee, Digital Commonwealth, Texas Portal, GPO, Heartland (Missouri), Illinois, PA Digital, Northwest Digital Heritage,
  Indiana, Ohio, NYPL, Mississippi, Empire State, South Carolina, Connecticut, NJ/DE, Florida, Digital Virginias, Michigan, OKHub,
  Kentucky, Maryland, Vermont, Big Sky. **Not present in the 2026-10 export under a matching hub name: Mountain West, Maine,
  Arizona, Louisiana, Alabama, Arkansas.** Absence may mean no match, not no holdings.

## Counts

| step | n |
|---|---|
| DPLA parts streamed | 812 / 812 (NARA skipped) |
| DPLA prefilter matches | 135,193 |
| after date + tight regex | 2,059 (stage3) |
| non-hub-noise lines read by eye | about 930 + 198 |
| Smithsonian bulk matches | 1,579 (acah 437, nmah 406, naa 318, chndm 174, aaa 60, sia 48 ...) |
| candidates written | 22 |

## Best leads (ranked)

1. **Fernández Cavada letters and "List of secret codes" sheets, Cuba 1870** (Miami CHC chc5006): letters plus what look like the
   key lists in the same file; class B; solvability 4.
2. **Loud postcards 1879-80** (Historic Newton): 54 cipher cards, one already transcribed, a ready crib; solvability 4.
3. **Godoi letters** (UC Riverside): three Paraguayan exile letters in code, 1878-84; open.
4. **Fitz-John Porter 16 Aug 1862 letter in code** (Lehigh) and **Milligan 1864 coded message** (Indiana State Library).
5. **Frick-Carnegie telegrams 1889-99** (19 records) and **Bunker Hill 1899 telegrams** (about 35, one with a handwritten gloss);
   both commercial-code traffic where a codebook may exist.
6. **NYPL Spencer Greek MS, scribe's prayer "in a cryptographic system", c. 1150**: possibly the oldest cipher this sweep found.

## Key leads (bare keys, not rows)

- Silas Deane Papers, Barnabas Deane code books 1780 (Connecticut Historical Society, hdl 11134/40002:12831): two numbered codes.
- Arthur Lee, letter 27 Apr 1779 enclosing a "cipher code for correspondence" (NYPL, item 37d37320-0e21-0134-db03-00505686d14e).
- Balfour → Campbell 25 Jan 1781, "encloses a cypher" (NYPL 5e44f560-6a3d-0139-aef4-0242ac110002) and letter to Alexander Hamilton
  11 Jun 1799 "with explanation of cypher code" (NYPL b957f390-3732-0134-7a40-00505686d14e).
- Elizabeth Van Lew cipher (NYPL acce9040-c618-012f-81d2-58d385a7bc34): already in `research/us_wars`.
- James Wilkinson memorandum explaining the Burr-Wilkinson cypher (Newberry Graff 16326, via Illinois hub).
- "La cifra por la qual ha de escribir Lázaro Moreno de León" 1583 (Miami asm0491 id 96, Spanish Tenerife governor): a Spanish
  cipher sheet (class key lead for the Spain sweep).
- Private Cipher Code, Seoul 1901 (Bostwick/Sands, Catholic Historical Research Center Philadelphia items 7938, 7973); FDIC Cipher
  Code 1934 (FRASER); Boilermakers 1909, IAM 1901, Pan American Airways 1929/36 cable codes (commercial code books).
- Huntington Library (cdl hub) "Cipher Book #5", "Cipher for Telegraphic Correspondence", War Department cipher ledgers, Eckert's
  cipher book: all in `research/us_huntington` and `targets/eckert1862`.

## Seen and left out

- **Rinzi enciphered journal 1898-1903** (University of Illinois): marked "undeciphered" in the catalogue but broken by Tony Gaffney
  in 2017 (Schmeh's blog, Gaffney/Schmeh ECP 158 paper). Not a candidate.
- Read or printed: Monroe → Washington 24 Mar 1796 (decoded below the cipher), Thomson → Jay 7 Jun 1780 (decoded by Jay), La Luzerne →
  Destouches 1781 (decoded by Destouches), Huntington Blathwayt Newcastle/Townshend letters 1725-29 (deciphered in French; in
  `us_huntington`), Grant → Lincoln/Sherman 1864 (marked "cipher" and "copied": clear copies), Poe/Thomas/Tomlin cryptograms 1841-45
  (Poe solved them), Missouri Historical Society dance-card "coded message" 1888 (reversed text), Michigan WWI POW "secret code" (deciphered
  by the censors), Wesley's diary 1736 (partly in cipher/shorthand; believed read by Wesley scholars, not checked).
- Coded language, not cipher: Bulmash/Fleischmann Bratislava Working Group letters 1942-43 (Kenyon), Olmstead radio messages, Warren
  Johnston letters.
- Noise classes: ex libris "cipher" initials (Illinois, 94 records), Raku and Meissen marks (Smithsonian, about 300), Napoleon III
  "Service à chiffre", Hebern/Typex/Bombe objects and photographs (NMAH), Cryptogramma ferns, Cyphers surnames (Oklahoma, Kansas),
  Massachusetts building codes, arithmetic "cipher books" (Calisphere, DigitalNC), Pierpont telegrams (clear text).
- Smithsonian: nothing usable. NMAH holds the Hebern papers (objects, drawings, patents) and cipher machines; ACAH holds
  Friedman-related finding aids and telegraph code books of firms; AAA holds only the Jim Sanborn "Kryptos" commission files; SIA has an
  OSS-era "secret writing on glass" folder. None is a ciphertext in the sense of the brief.
- Famous: Kryptos (Sanborn papers, AAA).

## Blockers and not reached

- DPLA API key not obtained (needs an email address); the bulk export covered the same data without it.
- Smithsonian API DEMO_KEY rate limit (10/hour); replaced by S3 bulk.
- Metadata only: no scan was viewed (seen = "catalogue" on every row). Many hub records have no description, so manuscripts whose
  cipher is only visible on the image are missed.
- Hubs absent from the export (see above) and any institution whose catalogue never uses the word cipher/code.
- The Harvard Library records (116k matches) were not triaged beyond a regex pass; Harvard's Houghton cipher material (e.g. Sparks,
  Adams) sits outside this export.
- Next steps: view the top rows, then look at HathiTrust/Getty/IA "manuscript" subsets (not done), and run the same term list over the
  Europeana-like DPLA "text"/"image" types after year 1950 only if scope widens.
