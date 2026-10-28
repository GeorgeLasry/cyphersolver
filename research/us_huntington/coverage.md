# Huntington Library sweep: coverage log (Oct 2026)

Polite access: one request every 3 s per host, User-Agent `cyphersolver-archive-sweep/1.0`.

## 1. OAC (oac.cdlib.org), full-text finding aids, repository facet "Huntington Library, Manuscript Collections"

OAC sits behind an AWS WAF: plain curl gets HTTP 202 `x-amzn-waf-action: challenge`, so the search was run from the
built-in browser (same-origin fetch, 100 results per page, 3 s apart). After 13 page requests the WAF served a
"Let's confirm you are human" CAPTCHA page (HTTP 405). Stopped there (no CAPTCHA bypass).

| query (Manuscript Collections facet) | hits |
|---|---|
| cipher | 156 |
| ciphers | 156 (same set, stemmed) |
| cypher | 12 |
| cyphers | 12 |
| decipher | 11 |
| deciphered | 11 |
| decypher | 0 |
| cryptogram | 0 |
| nomenclator | 1 (Lieber pseudonym, not a cipher) |
| chiffre | blocked (CAPTCHA) |
| "in cipher", "partly in cipher", "secret writing", "invisible ink", "sympathetic ink", code, codes, "telegraphic code", cifra, "in code", cryptography, "cipher letter" | not run (CAPTCHA) |
| same terms, facet "Huntington Library, Rare Book Collections" | not run (CAPTCHA) |

173 distinct component hits. 118 are Eckert Papers volumes (already catalogue 648) or Grant correspondence items
marked "Not marked cipher" (Grant's drafts, plaintext). The remaining 55 were read one by one; relevant ones:

- Loudoun papers (mssLO), Series 2: Kerlerec → Machault, 28 Jan 1757, "In cipher" (Box 151, Folder 17); Kerlerec →
  unidentified, 12 Dec 1756, "In cipher", enclosed in Lyttelton → Loudoun 5 Apr 1757 (LO 3293) (Box 145, Folder 14). Kept.
- Blathwayt papers addenda (mssBL addenda; intelligence to Alexander Hume-Campbell / Newcastle, 1720-1734): 9 items with
  cipher. "Deciphered" noted on 4 (Pareti 7 Jun 1725; To [-----] Jan 1728; Port Ste Marie 14 Jul and 4 Aug 1729; To [-----]
  c. 1729). Not noted as deciphered on: Statement re M. Rottembourg [1727-28]; Madrid intelligence 13 Sep 1728 (two lines);
  Port Ste Marie 23 Jun 1729 enclosing "a cipher"; Cesnok 8 Aug 1729 enclosure (a) undated in cipher; copies of 3 letters
  Cesnok 29 Jun-19 Jul 1729 with intelligence report in cipher. Kept as candidates (class A: deciphered siblings).
- Hamond collection: Francis Drake (Munich) → Charles Stuart, 20 Sep 1803, "partly in cipher with three pages partly
  obscured", no reading noted; siblings 31 Oct 1803 and 14 Feb 1804 carry Stuart's autograph reading. Kept (class A).
- L. Dennis Shapiro collection: J. Q. Adams → Madison, St Petersburg, 7 Jan 1811, partly in diplomatic cipher. Checked
  against prior art (see README).
- Joseph Hooker military papers, Box 4 Folder 5, "Crossing the Potomac" Jan-Mar 1862: ciphered telegrams. Kept (low).
- SP de México collection: ciphered telegrams Kruttschnitt → Epes Randolph 30 Jun 1910 (Box 9 item 4) and Shoup → Hale
  Holden 18 Nov 1929 (Box 12 item 10); finding aid quotes their meaning, so they were read (railroad company code). Not kept.
- Townshend family papers Box 13: Ferdinando Warner → Selwyn c.1765 with "An Explanation of the Cyphers in Mr. Selwyn's
  Letters" (key lead, not kept).
- Beaufort papers: "Solution to Sir Francis Beaufort's cipher, 1974": solved. Not kept.
- Business cipher books / "ciphers" in Henry E. Huntington, Bicknell, Shorb, Lamoureaux, Janin papers (commercial telegraph
  codes, 1878-1907); Chang Hong Yen 1910 cipher cable (meaning given in finding aid); cyphering (arithmetic) books
  (Duryea, Stevens, Lossing). Not kept.

### OAC second pass (28 Oct 2026, 10 s between requests; CAPTCHA again after 12 requests)

| query (Manuscript Collections facet) | hits | new relevant |
|---|---|---|
| "in cipher" | 17 | none (all in the first pass) |
| "partly in cipher" | 4 | none |
| "secret writing" | 2 | Beaufort "Cryptography, a System of Secret Writing" (solved 1974); Bendikson (imaging) |
| "invisible ink" | 1 | Bendikson papers |
| "sympathetic ink" | 0 | |
| "in code" | 7 | Henry E. Huntington papers series note (H.E. ↔ C.P. Huntington "often in code"); Fuller code letter |
| "cipher letter" | 0 | |
| cryptography | 3 | Davies WWII cryptographer correspondence (no ciphertext) |
| chiffre | 1 | Karpinski map ("les chiffres marquent"), not a cipher |
| codes | 456 (400 read) | noise (legal codes, coded negatives); SP code book 1892-97 (key lead) |
| "telegraphic code", cifra; all Rare Book Collections queries | not run (CAPTCHA) | |

## 2. Huntington Digital Library (hdl.huntington.org, CONTENTdm dmwebservices API, all collections)

Script `hdl_sweep.py`; raw hits `hdl_hits.json`, item records `hdl_items.json`. 832 distinct non-Eckert objects: 683 are
Otis Marston Colorado River photographs matched only on 'code' (photo codes), so the item-record fetch was stopped after 431;
all non-Marston objects (149 plus 1 print-ephemera room plan) were fetched and read.
Searches CISOSEARCHALL, which includes page transcripts/OCR (Eckert ledgers, Ellesmere calendar typescript, annual reports).

| term | hits (records incl. pages) |
|---|---|
| cipher | 1974 (almost all Eckert ledger pages) |
| ciphers | 1771 |
| in cipher | 1517 |
| code | 881 |
| cyphers | 54 |
| coded | 32 |
| secret writing | 27 |
| deciphered | 15 |
| telegraphic code | 9 |
| cypher | 8 |
| decipher | 8 |
| invisible ink | 6 |
| ciphered, sympathetic ink | 1 each |
| cyphered, decypher, decyphered, cryptogram, nomenclator, chiffre, cifra, cypher key | 0 |

Kept from HDL: Blathwayt addenda mssBLA 184, 186, 191 (images viewed; BLA 187 enclosure viewed: deciphered
interlinear, same code); HM 64; HM 744. Read and dropped: La Luzerne → Destouches 1781 (mssDE 37, 55, 68, 108B: all
decoded by Destouches or "in another hand"; key leads); HU 1051 (vowel cipher, cataloguer gives the reading); Book of
Hours HM 25773 (a bookseller's "cipher" number); Robert Bristow ledger (binder's cypher); Emmet → Jefferson 1826
(handwriting "deciphered"); Ellesmere calendar typescript hits (6900: 1620 Oñate dispatch "deciphered by Phillips", a
summary; Todd memorandum book "difficult to decipher" = handwriting); annual reports (acquisitions of printed cipher
books, Bendikson's imaging); oral histories, maps, photographs (noise). HDL Stowe Papers collection (77 objects, chiefly
Brydges letter books ST 57/58 1694-1714) has no transcripts, so cannot be keyword-searched.

## 3. Huntington library catalog (catalog.huntington.org, III WebPAC keyword search)

Script `catalog_sweep.py`; `catalog_hits.json`, `catalog_records.json` (100 full records of manuscript hits).
5 s between requests; one connection reset (resumed).

| term | hits | manuscript hits |
|---|---|---|
| cipher | 202 | 15 |
| cypher | 41 | 2 |
| ciphers | 149 | 7 |
| cyphers | 20 | 0 |
| deciphered | 56 | 1 |
| decyphered | 9 | 0 |
| decipher | 7 | 0 |
| cryptogram | 15 | 0 |
| nomenclator | 34 | 0 |
| chiffre | 5 | 0 |
| secret writing | 92 | 5 |
| invisible ink | 8 | 1 |
| sympathetic ink | 8 | 0 |
| in cipher | 141 | 14 |
| partly in cipher | 1 | 1 |
| cipher letter | 11 | 5 |
| code telegram | 2 | 1 |
| cipher telegram | 3 | 2 |
| ciphers and codes | 25 | 3 |
| cryptography | 160 | 3 (Davies, Arensberg Baconian microfilm, Eckert) |
| cifra | 1 | 0 |
| cipher key | 6 | 0 |
| in code | 714 | 76 (mostly dealer catalogues; read all) |
| cipher manuscripts | 11 | 7 |
| cyphers manuscripts | 0 | 0 |
| cryptography manuscripts | 4 | 1 |

Kept from the catalog: Bothmer/Robethon 1713 (HM 44710); EIC Philippine expedition 1769-80 (HM 80328-80338); Cleary
journal (HM 80821). Read and dropped: Lady Pecunia "in cipher" c.1605 (mssFAC 716, a facsimile; Robert Robinson's
phonetic transcript, not a cipher); Salvetti (HMC Skrine, printed); JQA → Armstrong 1809 (HM 22922, discusses the need
for a cipher, no ciphertext); Grant → Stanton 1866 (HM 25081, marked cipher, printed in Papers of U. S. Grant 16);
Welbeck extracts 1687-88 (MSS MFilm 00361, microfilm of BL original; list of numerical ciphers = key lead elsewhere);
Parker newsletters 1635-93 (HM 66704-66716, key to an alphabetic code sent to Sir Gilbert Hoghton: key lead);
Marconi Morse code; Farnsworth "Co-hab code" (description only); Wheatstone; Arensberg/Bendikson/Bacon Foundation
(Baconian); HMS Centurion commercial code signals list.

## 4. Printed guides and calendars

- archive.org: Guide to British historical MSS (1982), Guide to American historical MSS (1979), Guide to literary MSS
  (1979), Guide to medieval and Renaissance MSS (1989): lending-library scans, search-inside refused ("Item not
  available"). Not searched.
- HMC Hastings IV (1947, DLI scan in.ernet.dli.2015.282710): full text grepped for cipher/cypher/decipher: 3 hits
  (Bramhall 1638 proposes a cipher; Bramhall → Ormonde 1653 partly in cipher, cited from Ormonde MSS, not a Huntington
  item). HMC Hastings I-III not found online.
- Ellesmere/Bridgewater calendar typescript (HDL, 10 vols, OCR): covered by the HDL term search above.

## Not reached

- OAC: Rare Book Collections facet; "telegraphic code", cifra; per-collection browsing of Stowe (STG/STT/STB), Hastings
  (HA), Ellesmere (EL), Battle Abbey (BA), Pulteney (PU), Loudoun (LO) container lists beyond keyword hits (WAF CAPTCHA).
- Item-level descriptions for Stowe, Hastings, Ellesmere, Battle Abbey and Pulteney are mostly in PDF/legacy guides, not
  in OAC full text; no hit in any of them for cipher/cypher/decipher.
- Huntington blog/Verso pages (huntington.org) not searched.
