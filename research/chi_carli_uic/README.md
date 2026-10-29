# Chicago sweep: CARLI (non-Newberry), Illinois Digital Archives, university and ethnic archives (28 Oct 2026)

Result: 3 candidate rows in candidates.json, all weak (importance 2, one source: the Chicago History Museum's James
Wilkinson papers calendar). The rest of the scope holds almost no cipher manuscripts; the hits are printed matter, student
papers and noise. All counts: coverage.md. Scripts: `carli_all.py` (CONTENTdm sweep of all CARLI collections via alias
`all`), `ida_all.py` (same for idaillinois.org), `luc_fa.py` (Loyola finding-aid PDFs), `snip.py` (item full text around a
term), `chm.py` (second pass on finding-aid collections).

## Candidates (best first)
1. CHM Wilkinson papers vol. 3, p. 67, item 93: Eustis to Wilkinson, 10 May 1809, "part of message in cypher" (needs archive scan).
2. CHM Wilkinson papers vol. 4 (undated), p. 125, item 174: fragment with "numerical cypher notations".
3. CHM Wilkinson papers vol. 3, p. 66, item 91: Eustis to Wilkinson, 4 May 1809, "receipt of ciphered message" (probably a clear acknowledgement).
All three come from the full-text CHM finding aid on CARLI (https://collections.carli.illinois.edu/digital/collection/chm_fa/id/2106).
Importance 2: US War Department cipher traffic in Wilkinson's 1809 New Orleans command; the Spanish-code Wilkinson letters are
already in the catalogue (Papeles de Cuba, leg. 2374). Excluded: the 12 Dec 1805 anonymous paper "From Burr" endorsed "Truly
deciphered, F. Pinckney, Clk." (decipherment attached).

## Key leads (no ciphertext, or decipherment attached)
- E. Ogden Ketting papers (Loyola UA, https://www.luc.edu/media/lucedu/archives/pdfs/ketting.pdf), Subseries 1-F: Insull encoded-telegram code
  books April 1931, September 1931, ca. 1932 (Box 6). Could key the coded Insull telegrams of the 1932 collapse.
- Samuel Insull papers (Loyola, insull1.pdf), Series 4, Box 16: Insull-Eaton coded and decoded telegrams Apr-Jun 1930, with translations.
- Newberry Graff 4668 Wilkinson memorandum (chi_newberry) explains the Burr-Wilkinson numerical cypher and may help with CHM item 174.

## Dead ends
- CARLI and Illinois Digital Archives hits for cipher, cypher, decipher, cryptogram are student newspapers, yearbooks, sermons, printed
  Lincoln volumes, botany books, Swedish-American Historical Quarterly rune-stone "cryptography". No manuscript cipher letters.
- North Park ArchivesSpace (Swedish-American Archives, Covenant Archives): 0 hits for cipher terms.
- Loyola Omeka digital collections: 0.

## Not reached (blocked or not searched)
- UIC SCUA ArchivesSpace (archivesspace.uic.edu): 403 for every client including the built-in browser; not circumvented.
- Chicago Collections Consortium explore site and DePaul (archives.depaul.edu, via.library.depaul.edu): 403 / Cloudflare challenge; not completed.
- Catholic Research Resources Alliance VuFind (Loyola and DePaul MARC records): Cloudflare.
- Archdiocese of Chicago finding aids (49 PDFs, bishops' papers): listed, not grepped.
- Loyola: 261 of 360 finding-aid PDFs unread (mostly 20th century).
- Lithuanian World Archives manuscript database (Lithuanian-only form), Balzekas, ELCA, Moody, Spertus, Holocaust Museum, Czech/Slovak,
  Hellenic, Ukrainian, JASC: no usable online item-level catalogue found; see coverage.md.
