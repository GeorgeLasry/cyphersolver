# Coverage: Pritzker Military Museum & Library, Chicago History Museum, Chicago Public Library (28-29 Oct 2026)

All requests 3 s apart or slower. No CAPTCHA or challenge was completed.

## 1. Pritzker Military Museum & Library (Kenosha WI; pritzkermilitary.org)

| endpoint | result |
|---|---|
| `/search?...` HTML pages by curl | blocked (Incapsula JS redirect). Built-in browser loads the pages, but the site search form ignores the keyword (returns all 3,023 pages), so it is not usable for term counts |
| `cdm16630.contentdm.oclc.org` (the "Digital Collections" SEARCH link) | CONTENTdm instance with 0 collections (`/digital/api/collections` empty; search times out, 504). Nothing to search |
| `pritzkerlibrary` WorldCat Discovery (`pritzkermilitarylibrary.on.worldcat.org`) | loads only a spinner and an empty body in the browser pane; catalogue (mostly printed books) not reached |
| `/resources/archival-collections` | 225 finding-aid PDFs listed (all of the "250 collections" the page names that carry a PDF); all 225 downloaded (`pmml_crawl.py`, ~100 KB each, git-ignored) and text-searched (`analyze.py`) |

Term hits in the 225 finding aids (documents containing the term; every hit read in context):

| term | hits (docs) | what they are |
|---|---|---|
| cipher | 3 (3) | WWII signal soldier trained on teletype cipher machines (Heinrich); "indecipherable" diary entries (Herz); "decipher his letters" (Beer) |
| decipher | 2 (2) | same two |
| cryptographic / cryptogram | 3 (1) | Rush collection: Navy Cryptographic Board duty memos, 1953 |
| code message / in code / coded | 5 (4) | Gralak WWII letters: "secret code to find out where he is going", "chatting in code with other operators"; coded synoptic weather reports (Vanitzian) |
| secret code | 1 (1) | Gralak |
| telegram / military telegraph | 1 (1) | Haff: an 1898 "military telegraph envelope" |
| cypher, cryptogram, code book, invisible ink, signal code, Confederate cipher, Northwest Conspiracy | 0 | ("Camp Douglas" hits are Camp Douglas, Wisconsin) |

Result: no ciphertext. Civil War content is a handful of items (Aldrich diary transcript; 26 finding aids mention 1861-65 dates).

## 2. Chicago History Museum (chicagohistory.org)

| endpoint | result |
|---|---|
| `chicagohistory.org/?s=` site search | WordPress pages only (education PDFs); not the catalogue |
| `images.chicagohistory.org/search/` | 403 (Cloudflare/WAF) by curl; not retried in browser |
| Chicago Collections `explore.chicagocollections.org` (hosts CHM finding aids) | Cloudflare "Just a moment" challenge by curl and in the built-in browser; **blocked, not completed** |
| CHM library catalogue "ARCHIE" = Primo `i-share-chm.primo.exlibrisgroup.com` (scope `MyInstitution`) | **works** in the built-in browser via the Primo `pnxs` JSON API with a guest JWT (fetch from inside the page; curl cannot). Item-level records for archives and manuscripts, with description, genre and call number |
| CARLI CONTENTdm `collections.carli.illinois.edu`, alias `chm_fa` | **works** by curl: CHM finding aids (323 PDFs), full-text searchable; PDFs fetched where a hit needed reading |

Primo ARCHIE (scope MyInstitution), total hits per query (all record types; most are printed books or noise, every manuscript-level hit read):

| term | hits | | term | hits |
|---|---|---|---|---|
| cipher | 16 | | cypher | 13 |
| ciphers | 13 | | cyphers | 10 |
| ciphered | 9 | | cyphered | 3 |
| in cypher | 13 | | secret cipher | 2 |
| cipher key / cypher key | 1 / 1 | | cipher telegram | 2 |
| decipher | 1 | | cryptogram(s) | 0 |
| cryptic | 3 | | enciphered | 0 |
| code book | 13 | | codebook | 2 |
| coded | 47 | | secret code(s) | 6 / 6 |
| secret writing | 5 | | invisible ink | 13 (printed noise) |
| Confederate cipher | 1 | | Northwest Conspiracy | 4 |
| signal code | 0 | | code telegram / telegram code | 0 / 0 |
| subject "cipher(s)" | 8 | | subject "cryptography" | 1 |
| genre "Ciphers (codes)" | 7 (5 as subject) | | subject "telegraph codes" | 3 |
| Camp Douglas (any) / subject | 50+ / 59 | | subject "Sons of Liberty" | 7 |
| Confederate (any) | 1,616 | | spy | 150 |

Manuscript-level results (collection or archival_material records): Walpole letter 1769 (cypher portion), Plum papers (7 cipher notebooks), Army of the Potomac Jan 1863 (cypher and secret code), Department of State 1827 (cipher code), Febiger papers 1779-91 ("perfect cypher" is a joke, not cipher), plus noise (Strang diary "deciphered" = published decipherment of a diary in a private script, 1961, a book; "Chicago conspiracy trial scrapbook, 1865" = newspaper clippings). Camp Douglas / Northwest Conspiracy: only clippings, reminiscences (Strong 1908) and printed books; no cipher manuscripts.

CHM finding aids on CARLI (`chm_fa`, 323 documents): terms cipher 0, cypher 1, ciphered 1, deciphered 1, decipher 2, secret writing 1, secret code 2, code message 3, coded 2, Northwest Conspiracy 1 (a magazine index), cryptogram 0, Confederate cipher 0, signal code 0, invisible ink 0, Camp Douglas 1, Haymarket 5, Burr conspiracy 2. The one real manuscript hit is the James Wilkinson papers (already taken by `research/chi_carli_uic/`: Eustis letters of 4 and 10 May 1809, item 174 "numerical cypher notations"; the 12 Dec 1805 paper "Truly deciphered" is excluded). Ninian Edwards papers, Hoffman, Flerlage, Freuler, Alliance to End Repression, CCDBR finding aids were opened: no cipher.

## 3. Chicago Public Library (chipublib.org), Special Collections

| endpoint | result |
|---|---|
| site search `?s=` | results load dynamically (BiblioCommons); static HTML has no result list. Not usable |
| WordPress REST API | 401 ("Missing key") |
| sitemaps | `sitemap.xml` lists `bccms_archival_post` (675 URLs, finding-aid summaries, 239 read) and `page` sitemaps (506 pages with slug `fa-*`, the full finding aids, e.g. 242K characters for the Civil War collection). All 506 `fa-*` pages fetched (`cpl_fa_urls.py`, `cpl_fa_crawl.py`, ~28 min) plus 239 archival summaries (`cpl_crawl.py`, stopped once the `fa-` pages were found to hold the full text); text-searched (`analyze.py`) |
| CPL digital collections, CONTENTdm `cdm16818.contentdm.oclc.org` (29 collections: Chicago Examiner 1908-18, Theater, Civil War "wha", Illinois Writers' Project, ...) | search works by API. Hits for every term are the Chicago Examiner newspaper (OCR, thousands of hits, printed puzzles and stories) and theatre programmes; the Civil War collection (`wha`) returns 0 for all terms; IllWriters: "Report on Camp Douglas" (no cipher) |

Term hits in 745 CPL pages (documents containing the term):

| term | hits (docs) | what they are |
|---|---|---|
| cipher | 7 (3) | "Circles and Ciphers" youth programme (Kaba papers); a "Robinson Telegraphic Cipher" 1897 (printed code book, grain trade, City-Wide Collection Box 6 Folder 16); "undecipherable" audio |
| cryptogram | 6 (2) | Mamet play, Steppenwolf records |
| decipher | 2 (1) | audio |
| code message / in code / coded | 10 (3) | **Civil War documents collection: "Encoded dispatch" Rosecrans to Burnside, Chickamauga, Sept 1863, Item 72.407.1, with a 1907 translation (72.407.2): excluded, decipherment attached; Ruggles orders 19 Feb 1864, Item 86.40.15, "possibly in code": candidate**; coded greeting cards (Volland) |
| secret code | 3 (1) | play title |
| code book | 1 (1) | union ethical code books |
| telegram | 1 (1) | O'Sullivan/Gardner photograph of the US Military Telegraph Construction Corps |
| Camp Douglas / Sons of Liberty | 18 (7) | Camp Douglas letters from soldiers, pamphlets, photographs, a ballroom; no cipher or Northwest-conspiracy ciphertext |
| cypher, invisible ink, secret writing, signal code, Confederate cipher, Northwest Conspiracy | 0 | |

Not reached: the CPL catalogue (BiblioCommons, `chipublib.bibliocommons.com`) for item-level manuscript records outside the finding aids; the 175 `archival_post` pages not fetched (their finding aids are in the `fa-` set); WorldCat Discovery for PMML; CHM `images.chicagohistory.org` and Chicago Collections (blocked).
