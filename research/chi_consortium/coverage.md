# Coverage: Chicago Collections Consortium sweep (28-29 Oct 2026)

The Consortium portal itself could not be reached by script or browser (Cloudflare managed challenge, Turnstile
checkbox; not completed). The sweep therefore went through the member institutions' own open endpoints. Every
endpoint tried is listed.

## Blocked or unreachable

| endpoint | result |
|---|---|
| explore.chicagocollections.org (search, /api/search, /marcxml/...) via curl, WebFetch | 403 Cloudflare "Just a moment" |
| same via built-in browser | Turnstile checkbox page, not completed; tab closed |
| chicagocollections.org | 403 |
| bmrc.lib.uchicago.edu/portal/ (BMRC Archives Portal) | 302 to /turnstile/challenge/; not completed |
| bmrc.lib.uchicago.edu, /finding-aids/ | 200 landing page, 404 |
| archives.newberry.org, mms.newberry.org (ArchivesSpace) | curl 403 (search and archival_objects); mms.newberry.org no connection; browser: Turnstile, not completed |
| archivesspace.uic.edu (search) | curl 202 empty; browser 403 Forbidden |
| findingaids.library.uic.edu, digitalcollections.uic.edu, dc.uic.edu | no connection |
| findingaids.library.northwestern.edu | 403 |
| www.artic.edu (archives, library) | 403 |
| chsmedia.org (legacy CHM finding aids), researchcollections.chicagohistory.org | connection refused / no connection; no Wayback copy (404) |
| digital.chipublib.org, digital.library.depaul.edu, digitalcollections.library.luc.edu, digitalcollections.spertus.edu, digital-libraries.saic.edu | no connection |
| web.archive.org copies of the above | 404 |

## Endpoints that worked

| # | endpoint | what was done | result |
|---|---|---|---|
| 1 | collections.carli.illinois.edu/digital/api/search/collection/all/searchterm/<term> (CONTENTdm, 3 s spacing, up to 10 pages of 50) | 23 terms, `carli_all.py`, `hits.jsonl` | counts below; all hits read by title/description |
| 2 | CARLI collection chm_fa ("Finding Aids Collection, Chicago History Museum"), 320 PDF finding aids | `chm_fa.py`: all 320 enumerated, 319 downloaded and grepped (1996 = 404), 3 s spacing; PDFs not kept in the repo (dl/, git-ignore) | one real hit: James Wilkinson papers (items 91, 93, 116, 174). Other 205 hits were "Finding aid encoded by", "color-coded" maps, "difficult to decipher" |
| 3 | luc.edu/archives A-Z lists (special collections + university archives): 349 finding-aid PDF/DOCX | `luc.py`: all downloaded and grepped | 4 files matched: Insull papers and Ketting papers (1930-32 commercial code books and coded telegrams, see README), Hyde papers (modern SIGINT disk, DigiCipher HDTV), King papers (nursing nomenclature) |
| 4 | nt.newberry.org (Newberry Transcribe) /search/results?keyword=..&format=json | `nt.py`, 30+ terms, first page (20) per term | pointed to Augur, Grierson, Pinkerton |
| 5 | Newberry Transcribe bulk dump (gitlab.com/newberry-library/transcribe, bulk_data/newberry-transcriptions20261016.json, 150 MB) | `nt_bulk_grep.py`: 118,607 transcribed pages, 7,140 titles | counts below; 31 contexts read; real: Augur 1874 telegrams, Grierson 1869 key letter, Case MS 5017 "text in cipher" (already in repo, catalogue 849), Pinkerton 1888, Book of magical charms 1612 (Latin charm, not cipher), an invisible-ink recipe in an 1828-38 receipt book (recipe, not ciphertext) |
| 6 | Newberry checklist PDFs: English MSS 1500-1865 (Cusk), French MSS (Wall), Italian MSS (Wall), European MSS post-1500, Greenlee description, Medieval and Renaissance publications | downloaded, grepped for cipher/cypher/cifr/chiffr/cryptogr/code/secret | only Burr (Graff f*502) and the coach painter's cipher book (both in the earlier Newberry sweep); Italian list has a printed "carattere cifrati" model book (Luzzi 1799, Wing MS fZW 735, a calligraphy manual, not a cipher) |
| 7 | WebSearch, domain-limited to archives.newberry.org / mms.newberry.org / explore.chicagocollections.org / chsmedia.org / UIC / Northwestern / Loyola / DePaul / BMRC (about 16 queries) | | only Woolson "Life of Elijah Woolson (written in cipher)", Midwest MS, and the CHM Wilkinson papers surfaced |

## CARLI all-collections hit counts (fuzzy full-text; mostly OCR noise from student newspapers)

| term | total hits | real items |
|---|---|---|
| cipher | 65 | 0 (Newberry Book of magical charms, Whitman proof sheet "Shakspere-Bacon Cipher" at UIS) |
| cypher | 16 | 2 (Wilkinson papers CHM, Wilkinson memorandum Newberry Graff, both known) |
| ciphered | 8 | 0 |
| cipher letter | 13 | 0 |
| in cipher | 62 | 0 |
| decipher | 350 | 0 ("hard to decipher") |
| deciphered | 80 | 0 |
| cryptogram | 10 | 0 |
| cryptography | 32 | 0 |
| code message | 914 | 0 (phrase not enforced) |
| code telegram | 62 | 0 |
| code book | 1,890 | 0 (phrase not enforced) |
| secret writing | 2,203 | 0 |
| secret code | 526 | 0 |
| invisible ink | 69 | 0 |
| sympathetic ink | 52 | 0 |
| nomenclator | 4 | 0 |
| chiffre | 1 | 0 |
| cifra | 1 | 0 |
| cifrado | 0 | |
| en cifra | 1 | 0 |
| Geheimschrift | 0 | |
| szyfr | 0 | |

Per-institution breakdown of the hits (collection aliases in `hits.jsonl`): Newberry nby_* (cgs, dig, graff, mms,
teich), CHM chm_fa and chm_oh, Meadville Lombard mls_*, Garrett-Evangelical uni_*, Trinity tiu_*, North Park npu_*,
Saint Xavier sxu_*, Lewis lew_*, Benedictine ben_*, Governors State gsu_*, Columbia College col_bmrnews, Northeastern
Illinois nei_gutierrez, plus downstate collections (Knox, Illinois Wesleyan, Western Illinois, Augustana, Millikin,
SIU, Monmouth, UIS). UIC, Loyola, DePaul, Northwestern, CPL, Art Institute, Field Museum, Spertus, Roosevelt are not
in CARLI CONTENTdm; their only reach here was the Loyola PDFs.

## Newberry Transcribe bulk dump, term counts (118,607 pages)

| term | pages |
|---|---|
| cipher | 110 (almost all "ciphering" = arithmetic, telegram form text "errors in cipher or obscure messages", a "cipher" meaning zero) |
| cypher | 20 (same) |
| decipher / decypher | 93 (all "hard to read" or the army letter) |
| cryptogr* | 1 (crossword-style puzzles) |
| secret code / writing / alphabet | 0 |
| invisible / sympathetic ink | 1 (recipe) |
| in code / code letter / code message / code word | 4 |
| cifra / cifrado / cifrad- | 1 (navigation figures) |
| chiffr- / geheim-, nomenclat- | 2 and 3 (noise: Schiffrin; street nomenclature) |
| szyfr / šifr | 0 |
| telegraphic code | 1 (a hotel's telegraphic address) |

The dump holds only pages volunteers transcribed (about 7,100 titles of the Newberry's digitised manuscripts).
Absence there does not mean absence in the collection.
