# Chicago Collections Consortium + BMRC sweep (28-29 Oct 2026)

Result: 4 candidate rows in candidates.json, one good (US Army cipher telegrams of 1874 at the Newberry) and three
weak. The portal itself (explore.chicagocollections.org) and the Black Metropolis Research Consortium portal are
behind Cloudflare/Turnstile and were not reached; nor were Newberry's ArchivesSpace finding aids, UIC's or
Northwestern's. The sweep went round them through endpoints that are open. Full list with counts: coverage.md.

## Method
1. CARLI CONTENTdm API (`collections.carli.illinois.edu/digital/api/search/...`, scripts `carli_all.py`): 23 terms over
   all CARLI collections; mostly OCR noise from student newspapers; nothing new except Chicago History Museum's
   finding-aid collection `chm_fa`.
2. CHM finding aids: the 320 PDFs in CARLI `chm_fa` were all downloaded and grepped (`chm_fa.py`). Only the Wilkinson
   papers matter.
3. Loyola Archives and Special Collections: all 349 finding-aid PDFs/DOCX from the luc.edu A-Z lists grepped
   (`luc.py`).
4. Newberry Transcribe (nt.newberry.org): keyword search, then the project's full bulk dump (118,607 transcribed pages,
   7,140 titles) grepped (`nt.py`, `nt_bulk_grep.py`). This was the only route to item-level Newberry text, and it
   produced the best lead.
5. Newberry checklist PDFs (English, French, Italian, European post-1500, Greenlee) grepped: nothing beyond Burr and the
   coach painter (already in research/chi_newberry).
6. About 16 domain-limited web searches for Newberry/UIC/Northwestern/Loyola/DePaul/BMRC finding-aid text.

## Candidates, best first
1. **Augur telegrams, Jan 1874**: Newberry Ayer MS 3008 (Christopher C. Augur papers, Department of Texas
   letter-books), box 02, scan 00045-1. Three telegrams, 12 and 17 Jan 1874, to Sheridan and Maj. Russell, copied as
   scrambled English words (a word-transposition cipher). Scans free online
   (https://collections.newberry.org/asset-management/2KXJ8ZSFQY9EQ). The method is described in an 18 Feb 1869
   letter in the Grierson papers (Ayer MS 3039 box 03 f.153: 4-9 columns, key-word substitution). Score 3/4/2.
2. **Eustis to Wilkinson, 4 and 10 May 1809**, CHM Wilkinson papers items 91 and 93 (ciphered message / part in
   cypher). Finding aid only; reading-room access. Score 3/1/3.
3. **Wilkinson papers item 174**, undated fragment with numerical cypher notations. Score 2/1/4.
4. **Pinkerton reports on the CB&Q strike 1888**, Newberry CB&Q records box 106 f.811: a cipher between a striker and
   an operative is mentioned; telegrams not located. Score 2/1/3.

## Key leads (keys and code books, no ciphertext)
- Gordon key letter, 18 Feb 1869, Ayer MS 3039 (Grierson papers) box 03 f.153, asset 2KXJ8ZSC7CU0W: the army's
  column-transposition cypher key; only the first page is transcribed, the second page (substitution list) is not.
  Needed for candidate 1.
- Insull papers (Loyola, UA, 1799-1970, Series 4: Cyrus Eaton negotiations April-June 1930, "coded and decoded
  telegrams ... translations of coded telegrams") and E. Ogden Ketting papers Box 6 subseries 1-F "Code": commercial
  code books of April 1931, September 1931 and about 1932 used for Insull office telegrams. Plaintext translations
  exist for the 1930 set, so they are key/crib material rather than open ciphers. Out of the classical-cipher scope
  but cheap to check for the paper's 1901-1950 band.
- Woolson family papers (Newberry Midwest MS): "Life of Elijah Woolson (written in cipher)", Ira K. Woolson, about
  1850s, box 1 f.30, with a copy transcribed from the cipher by Alvin M. Woolson, f.31
  (https://mms.newberry.org/repositories/2/archival_objects/63888 and /63889, seen through a web search only; the
  mms host did not respond to scripts). A cipher manuscript with a contemporary plaintext copy: not open, but a
  ready-made known-plaintext case. Not a row because the description says it was copied out (deciphered).
- CHM Wilkinson item 116 (12 Dec 1805, "Truly deciphered, F. Pinckney, Clk.", "From Burr"): the decipherment
  of a Burr letter; left out.
- Newberry Case MS 5017 "text in cipher" lines (Book of magical charms): already catalogue 849.

## Dead ends
- All CARLI full-text noise (student newspapers OCR "cipher", "code book"); Whitman "Shakspere-Bacon Cipher" proof
  sheet at UIS (Bacon cipher, printed, not in scope).
- Newberry checklists (Cusk English, Wall French/Italian): no cipher entries other than the two already known.
- Newberry Transcribe: "cipher" = arithmetic, telegram-form boilerplate, "no cipher" meaning zero; an invisible-ink
  recipe in a receipt book (not ciphertext).
- Loyola: Hyde papers (SIGINT cipher disk award, DigiCipher), King papers (nursing nomenclature).
- CHM Wilkinson 1805-1809 "cypher" items beyond the three listed.

## Not reached
- explore.chicagocollections.org (all ~40 members' finding-aid records), BMRC Archives Portal: Cloudflare/Turnstile.
  Not completed (no bot-check bypass). The portal's marcxml pages for CHM can be seen only through search engines.
- Newberry ArchivesSpace (archives.newberry.org / mms.newberry.org): Cloudflare; Midwest MS, Ayer, Graff, Greenlee,
  Case, Wing, Louis H. Silver, Philippine/Mexican Spanish material, Italian/French manuscripts item-level notes
  remain unsearched. Only transcribed pages (Newberry Transcribe) and checklists were covered.
- UIC (ArchivesSpace 403), Northwestern (403), Art Institute Ryerson & Burnham (403), Chicago Public Library, DePaul,
  Field Museum, Spertus, Roosevelt, Columbia College (no usable endpoint; no web hits).
- Legacy CHM finding aids (chsmedia.org) refused connections; only the 320 aids in CARLI were read.
- No page images viewed, so every row is `seen: catalogue` and the Augur scrambled-text reading rests on a volunteer
  transcription.

## Files
`carli_all.py` (CARLI all-collection search), `chm_fa.py`, `luc.py`, `nt.py`, `nt_bulk_grep.py`, `make_candidates.py`;
outputs `hits.jsonl`, `chm_fa_hits.json`, `luc_hits.json`, `nt_hits.json`, `nt_bulk_hits.json`, `candidates.json`.
`dl/` (PDFs and the 150 MB Transcribe dump) is working data and should stay out of git.
