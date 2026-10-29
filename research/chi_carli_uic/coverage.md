# Coverage: CARLI (non-Newberry), Illinois Digital Archives, Chicago university and ethnic archives (28 Oct 2026)

Method note. CONTENTdm dmwebservices `dmQuery/all/CISOSEARCHALL^<term>^all^and` (all fields, including OCR full text; an AND
of words, so "in cipher", "code message", "code book" are not phrase searches and are mostly noise), 200 records per page,
3 s between requests. Raw hits: `carli_all_hits.jsonl`, `ida_all_hits.jsonl`; counts: `carli_counts.jsonl`, `ida_counts.jsonl`.
The CARLI run used alias `all` (414 collections; it includes the Newberry `nby_*` collections, already done in chi_newberry).

## 1. CARLI Digital Collections (collections.carli.illinois.edu), hit counts per term (all collections, page level)
cipher 71; cypher 16; ciphered 8; "in cipher" 68; decipher 385; cryptogram 11; cryptography 38; code message 941;
code telegram 62; code book 2108; coded 240; secret writing 2301; secret code 539; invisible ink 69; nomenclator 4;
chiffre 1; cifra 1; Geheimschrift 0; szyfr 0; sifra 33 (all Swedish "Chicago-Bladet" OCR); sifruotas 0; chiffriert 0.
Hits by collection for the real cipher words (cipher/cypher/ciphered/cryptogram/cryptography): student newspapers
(Illinois Wesleyan Argus, Knox Student, Millikin Decaturian, Western Courier, Augustana Observer, Xavierite, Evangelical
Beacon, Chicago-Bladet), SIU/Lewis/North Park magazines and catalogues, Swedish-American Historical Quarterly (rune-stone
cryptography debate), sermons (Landwehr), yearbooks. All noise on inspection (arithmetic "cipher", "a mere cipher",
crossword and cryptogram puzzles, runic cryptography reviews).
Manuscript-level hits read in context:
- chm_fa (Chicago History Museum finding aids, full text): James Wilkinson papers, 1764-1823 (chm_fa/2106) has calendar entries
  with "cypher" and "ciphered": 3 rows kept (candidates.json). The 12 Dec 1805 anonymous paper "From Burr" endorsed "Truly
  deciphered, F. Pinckney, Clk." has a decipherment, so it is excluded. Other chm_fa terms: secret 7 (Freuler, Alliance to End
  Repression, 1919 White Sox, Wilkinson; none a cipher), encoded 205 (metadata noise), enciphered 0, cryptic 0.
- wiu_ross (Gen. Leonard Fulton Ross papers, 1865): the printed Morse Line telegram form says "No liability for errors in cipher or obscure messages".
- uis_msc 84: Whitman proof sheet "Shakspere-Bacon Cipher" (a printed essay, not a cipher text).
- mls_uuarecord and mls_arisian (Meadville Lombard): "one cipher was omitted" (a digit), "sexual cipher" (20th-century prose).
- ben_listy: "deciphered Egyptian hieroglyphs" (student paper).
- nby_*: covered by chi_newberry.
- Second pass by alias for enciphered/encoded/secret/cryptic on chm_fa, dom_papal, dom_literary, uni_mmc, uis_msc, lfc_sc001: no
  cipher-family manuscript hit (the batch stopped on a connection error after "cryptic").
- The UIC `uic_*` collections (photographs, Hull-House, Nightingale letters) have no cipher-family hit.

## 2. Illinois Digital Archives (idaillinois.org, 266 collections), hit counts
cipher 286; cypher 76; ciphered 18; "in cipher" 284; decipher 334; cryptogram 9; cryptography 29; code message 1343; code telegram 124;
code book 3729; coded 250; secret writing 1947; secret code 858; invisible ink 110; nomenclator 1; chiffre 4; cifra 0; Geheimschrift 0;
szyfr 0; sifra 8; sifruotas 0; chiffriert 0.
By collection (cipher/cypher/ciphered/cryptogram): Elgin Area History 159+26+14+6 (local newspapers), Chicago Botanic Garden
Lenhardt Library 34 (botany books), Abraham Lincoln - Documents 37+3 (printed Lincoln volumes: arithmetic "cipher"), St Charles,
Westmont and Huntley newspapers, World War II - Documents 5 (a printed wartime periodical), World War I - Documents 1,
Jewish Sentinel 5+1 (newspaper), Register of Illinois Prison Records 1 ("cypher" in a registry entry), Illinois and the Civil
War - Documents 1 (printed), UIS oral history 1. No manuscript cipher found.

## 3. Archival finding aids and discovery layers
| Institution | Endpoint | Result |
|---|---|---|
| UIC Special Collections & University Archives | archivesspace.uic.edu (ArchivesSpace) | HTTP 403 Forbidden to curl, WebFetch and the built-in browser alike (every URL, including the root). Not worked around. NOT REACHED. |
| Chicago Collections Consortium (explore.chicagocollections.org; UIC, DePaul, Loyola, CHM and others) | search | Cloudflare managed challenge ("Just a moment"), not completed. BLOCKED. |
| DePaul Special Collections & Archives | archives.depaul.edu and via.library.depaul.edu/do/search | 403 and Cloudflare challenge. BLOCKED. Web search found no cipher item. |
| Loyola University Chicago Archives & Special Collections | luc.edu/archives A-Z lists link 360 finding-aid PDFs | Downloaded and grepped 99 of 360 (all 33 whose title carries a start year before 1900, plus the first ~66 in list order) for cipher, cypher, cryptogram, secret writing/code/ink, invisible ink, nomenclator, chiffre, cifra, code message/telegram/book, coded message. Hits: Samuel Insull papers (Series 4: coded and decoded telegrams with translations, Insull-Eaton Apr-Jun 1930; decipherments attached, so excluded); E. Ogden Ketting papers (Subseries 1-F: code books Apr 1931, Sep 1931, ca. 1932 for Insull's encoded telegrams; a key lead); Henry Hyde papers (1991 cipher-disk award). 261 PDFs (mostly 20th century) not read. |
| Loyola Special Collections digital (specialcollections.luc.edu, Omeka) | items/browse?search= | cipher 0, cypher 0, cryptogram 0, code 4 (noise). |
| North Park University (Swedish-American Archives of Greater Chicago, Covenant Archives) | northpark.libraryhost.com ArchivesSpace search | cipher 0, cypher 0, cryptogram 0, secret code 0, coded 0; "in code" 8 (code of ethics etc.). Also the CARLI npu_* collections above. |
| Archdiocese of Chicago Archives | archives.archchicago.org/finding-aids | 403 to curl and WebFetch; the built-in browser loaded the list of 49 PDF finding aids (Quigley, Feehan, Mundelein, Stritch, Cody, Meyer papers, Chancery correspondence 1929-58, parishes). PDFs not fetched or grepped. NOT SEARCHED. |
| Lithuanian Research and Studies Center / Lithuanian World Archives | lithuanianresearch.org/archives/individuals/ (names with role labels) | Database search is Lithuanian-only and not scripted; the individuals index (diplomats Bielskis, Kajeckas; resistance Prapuolenis, Baužys; Škirpa) has no cipher or code mention. No item-level catalogue seen. |
| Balzekas Museum | balzekasmuseum.org | Archive being processed, no finding aids online. |
| ELCA Archives (Elk Grove Village) | elca.org | Catalogue partly indexed on archives.com; no searchable finding aids reached. |
| Moody Bible Institute (Crowell Library) | library.moody.edu archives LibGuide | Finding aid for the D. L. Moody collection; no cipher mention found; not searched in depth. |
| Spertus / Chicago Jewish Archives; Illinois Holocaust Museum | web search only | Appointment-only; no online item-level catalogue. |
| Czech/Slovak, Hellenic, Ukrainian Institute, Japanese American Service Committee | not searched individually | No online item-level catalogues found; CARLI nei_japan (Japanese-American Redress, NEIU) gave 1 "coded" hit (noise). |
| Augustana Swenson Center, Lake Forest, Dominican, IIT, NEIU, Chicago State etc. | CARLI collections above | No cipher-family manuscript hit. |
