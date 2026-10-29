# National Archives of Australia (RecordSearch) sweep, 28 Oct 2026

Goal: find ciphertexts in the NAA (recordsearch.naa.gov.au) that are unread and not yet in the catalogue.
Result: **18 candidate rows** in `candidates.json`, all low to middling. Australian government files are mostly
about cipher *use* (cypher books, security committees, cipher sections, personnel). Code telegrams to and from
London normally have the decypher on file. Very few files describe ciphertext that nobody read.

## Method

- **Blocker: Cloudflare.** Plain HTTP clients (curl, requests) get a 403 "Just a moment..." challenge. A real
  browser passes it without any interaction, so the harvest ran as same-origin `fetch` calls inside the built-in
  browser pane. No captcha was solved.
- **Search flow** (ASP.NET WebForms; the session dies after 30 min or on a navigation away):
  1. GET `SearchScreens/BasicSearch.aspx` for the viewstate.
  2. POST `ctl00$ContentPlaceHolderSNR$tbxKeyword` + `btnSearch` to it. This returns `PleaseWait.aspx`, whose
     form posts to `BasicSearch_Result.aspx`. Post that form to run the search.
  3. On `ListingReports/ItemsListing.aspx`, post `__EVENTTARGET=ctl00$ContentPlaceHolderSNR$ddlResultsPerPage`
     with value 200, then GET `ItemsListing.aspx?page=N`.
  4. Parse the rows: checkbox id `ContentPlaceHolderSNR_cb<barcode>`, then series, control symbol, title,
     access status, dates and the digital-copy icon.
- Advanced item search (`AdvSearchItems.aspx`) takes `txbIteBarcode`, `txbKeywords`, `cbxKwdTitleNotes`, `txbSerNo`
  and so on. A barcode search lands on `ItemDetail.aspx?Barcode=`. `ItemDetail.aspx` only renders an item that is in
  the session's current result set, so details are fetched through a barcode search.
- Images: `NAAMedia/ShowImage.aspx?B=<barcode>&S=<page>&T=P&R=0` serves the page JPEG. A few pages were viewed; none
  were downloaded.
- The browser JS lives only in the page. The data were exported by returning JSON from the JS tool, which spills
  large results to a file, and were then converted to `hits.jsonl` / `hits2.jsonl`.

Terms (basic keyword search, titles): cypher (507), cipher (331), cyphers (120), ciphers (88), decoded (183),
decode (44), intercepted (265), code book(s) (94/36), codebook (20), code telegram(s) (8/48), cypher telegram (15),
code message (43), coded message(s) (16/13), secret code (35), secret writing (26), secret message(s) (20/60),
invisible ink (10), secret ink (2), decipher/decypher/deciphered/decyphered/ciphered/cyphered/enciphered (6/16/18/2/5/2/5),
cryptography (54), cryptographic (256), cryptogram(s) (1/1, both irrelevant), code key (54), cipher key (7),
cypher key (4), cypher/cipher book (12/3), code words (69), code letter(s) (34/35), cipher letter (5), cypher message (7),
unknown code (9), mystery code (1), Japanese code (39), German code (9), German wireless (35), enemy code (41),
encoded (654), Somerton (423, noise), Tamam Shud (1). "undeciphered", "undecipherable", "encyphered" returned 0.
A second pass searched titles and notes (`cbxKwdTitleNotes`) for phrases such as "unable to decipher", "could not be
decoded", "not deciphered", "coded notebook" and "in cypher". It added only 41 records, all irrelevant. Notes add
little, and the advanced form's date limit was ignored.

**Totals:** 3,553 distinct item hits (`hits.jsonl`), plus 41 from the notes pass (`hits2.jsonl`).
`filter.py` keeps 1,633 that start before 1951 and flags 373 of them as administrative noise (`review.tsv`). The
remaining 1,260 were read by title. 18 rows were kept.

## Best leads

1. **MP1049/1, 1914/0467 (item 405327), digitised.** Fanning Island W/T intercept, 11 Jan 1918: about 14
   two-letter groups that the Admiralty put down to "a Japanese man-of-war". Viewed (pp. 5, 8, 12, 20). The rest of
   the file (WWI intercepts, "unknown wireless signals" 1918) is worth paging through for more unread traffic.
2. **A989, E1943/350/9/7 PART 1 and 1944/350/9/7.** Intercepted telegrams between the French Committee and the
   French Delegation in Australia, 1943-44 (Free French cipher). Not digitised.
3. **C443, J427.** "Japanese messages in code", from the Japanese Consul-General's own seized papers, 1939-41. Not
   digitised. C439/5 (1946, 3 pages) is a smaller sibling.
4. **A6662, 50.** London cypher telegram to the Governor-General, 1902-03, "untranslated", with its opening code
   words quoted in the title. The NAA holds CO cypher books (see key leads), so it may be readable.
5. **CP506/1, 1.** Radiotelegraphic messages of Japanese residents in the Pacific, intercepted by the Navy, Jun-Aug 1918.

The other rows are censorship or security files whose titles mention a secret code or an intercepted message.
None states that the message was left unread.

## Key leads (code or cipher books and keys, not ciphertext)

- Colonial Office / Foreign Office cyphers held in Canberra: **A11804 1912/23** "Cypher R (1903 Edition)",
  **A9553/1** "Decypher Colonial Office 1, No. 98" (1922), **A9552/1-2** Interdepartmental Cypher and Decypher 1941,
  **A9554/1-2** the same for 1936, **MP960/4 NN** "Cypher B, copy No 37" (1921), **A12000** (Governor-General codes
  and cyphers, Cyphers M, V, AC, CO1, 1915-28), **B197 1997/2/*** (Cypher R, V, G, BW, stencil cypher),
  **D845 1910/1** Cypher R, **D1919 SS1016** "Cipher 'D' - instructions and key" (1942). These could read
  untranslated Governor-General telegrams such as A6662/50.
- German WWI codes: **AWM27 311/36** HVB code book (Berlin 1913), **MP1049/1 1914/0351** HVB code taken from SS
  Hobart (translation and distribution), **AWM46 91/1** German codebook, **A1 1917/13892** German ABC Code,
  **MP1049/1 1921/0328** German merchant ship code captured 1914.
- **D1918, S7** (digitised): MI5 summary "Cyphers used by enemy agents in United Kingdom", 1917-18, with the
  systems explained (e.g. Sanderson's Rotterdam ship-report code).
- **AWM25 189/*** and **AWM27 311/*** hold AIF code word lists, BAB trench code material and field cipher key
  tables (1915-19). **SP1141/1 S6/1/2, /63, /82** hold Playfair keywords (1915-26). **AWM193 21 PART 1** concerns
  the Playfair cipher (1922-43).
- **A9363/1**: Indian word code, 6th edition, 1924.

## Seen and left out

- **Kormoran / Detmers notebook**: A12982/1 (photographs of the coded notebook, 1941), B5823/1 ("decode and
  translation", 39 pp.) and A14195 2004/128 (the original returned in 2004). Already decoded, so out of scope.
- **Somerton Man (Tamam Shud) code**: C673 BOX 39 (ABC "Inside Story" 1977-78 image of the code) and C475 1047151
  (GTK segment, 1969). Famous; out of scope.
- **A6201/206**: Royal Commission on Espionage exhibit, a code name on notepaper (1954, after the cut-off).
- **D1901 A3363** "ANDERHOLDT [intercepted message]", 1944, viewed: a clear telegram to an internee.
- **SP1141/1 S6/1/48** "Secret Code - Trial Bay", 1917, viewed: a code book missing at the internment camp, not a message.
- **A816 19/304/420**: Japanese Consul-General intercepts, 1940, viewed. Dominions Office cables relaying their
  content, so already read.
- **C320 S111** "Secret writing" (1942-43), viewed: censorship returns about tests for secret writing.
- **A11804 1919/18** (Dalley-Scarlett cipher code), **MP76/1** (Army Inventions Directorate submissions 1941-45),
  **A1336** copyright entries for commercial codes, and the patents: these are proposals, not historical traffic.
  **A1336/29169** is Piddington's "Text of de Quiros MSS 1605 Now First Deciphered" (1936-37), a palaeographic
  transcription, not a cipher.
- **AWM252 A228**: F. W. Wheatley's account of unravelling a German code (1933). This is the known RAN break of the
  WWI German naval code, so read.
- **CP78/28** (168 "Decoded copy of telegram ..."), **MP1074/8** decypher logs, **A6662** cypher telegrams "with
  translation", **BP4/2** censors' reports, **B6390** cipher-section routine orders, **A10857/A471/B883**
  personnel: all read or administrative.
- Invisible ink files (**A2023 B217/1/767**, **MP16/1 1915/3/590** Henry Austin, **D1921 1918/16**, 1915-18): secret
  ink, usually read once developed. Not listed as rows, but they could be checked for coded content.

## Other Oceania portals (not reached)

- **Archives New Zealand Collections** (collections.archives.govt.nz): Imperva protection; the browser gets a
  "tick the box" human check. Not attempted, by rule.
- **Trove API** (api.trove.nla.gov.au v3): needs an API key (401 without one). Skipped. NLA manuscripts could be
  searched by hand on the Trove website.

## Files

- `hits.jsonl`: 3,553 basic-search hits (bc, series, ctrl, title, dates, access, dig, term).
- `hits2.jsonl`: the title+notes pass (994 rows, 41 new).
- `filter.py` -> `review.tsv` (pre-1951, noise-flagged).
- `make_candidates.py` -> `candidates.json`.
