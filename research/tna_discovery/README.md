# TNA Discovery sweep (28 Oct 2026)

Sweep of the UK National Archives Discovery catalogue for ciphertexts not yet in `catalogue.json`.
Output: `candidates.json` (26 rows, many of them grouped families: one row lists the item references in `folio_note`).

## Method

- Endpoint `https://discovery.nationalarchives.gov.uk/API/search/records` (`sps.searchQuery`, `sps.dateFrom/dateTo`,
  `sps.resultsPageSize=100`, `sps.page`). Python `requests` is reset by the server (TLS); `tna.py` shells out to `curl`.
  Results cap at 10,000 per query, so broad terms were split into date windows (`harvest.py`, inline window loop).
- About 90 term variants (cipher, cypher, ciphers, "in cipher", "in cypher", "partly in cipher", decipher*/decypher*,
  undeciphered, "key to the cipher", "in code", "in figures", "number cipher", "secret writing", cryptogram,
  unintelligible, hieroglyphic ...). Window queries of `"cipher" OR "cypher" OR "ciphers"` returned about 2,400 records
  for 1350-1899; all later terms added nothing new for those words, so that set looks complete. `hits.jsonl` holds 15,121
  distinct records (including noise from fuzzy matches of "cypher"/"cryptic" and 1900+ files).
- `filt.py` keeps 1350-1950 records whose description names a cipher/code, drops "royal cipher", monograms, nomenclature,
  and descriptions that say deciphered/decoded unless "not/partly deciphered". 2,897 remain; 1,699 of those are 1900-1950
  (HW/AIR/KV/ADM administrative cipher files, WW1-WW2 telegrams), which I did not treat as ciphertexts.
- Pre-1900 rows were read by hand and grouped by volume and correspondent (`make_candidates.py`). Dedup with
  `archive_sweep_2026-10/known.py` per shelfmark and name; prior-art web searches for the importance 3+ rows.

## Candidates: 26 (top leads)

1. Prince Rupert to Legge, D(W)1778 (Staffordshire RO), 1644-45, about 14 letters in code, two noted not deciphered (imp 4)
2. Atterbury Plot ciphers SP 35, 1722-24, with Plunket's numeral cypher copies as keys (imp 4, solvability 4)
3. Charles I (Newport) to Ormonde, cipher letter copy, 28 Oct 1648, Northumberland Archives ZSW/554/1 (imp 4)
4. Cornwallis Papers PRO 30/11, 4 letters called undeciphered plus about 100 "mostly cipher" (key known: Saberton)
5. Carleton Papers PRO 30/55, Clinton/Cornwallis/Haldimand ciphers 1779-82

## Left out and why

- **Already in repo/catalogue:** SP 95/136 and SP 87/24/33 (catalogue entry on Swedish and Spanish intercepts),
  SP 84/157 Charles I and Nicholas to Boswell (solved, targets/boswell), Roe/Gerbier to Elizabeth of Bohemia, Balfour
  intercepts (balfour1781), Cornwallis-Clinton Friedman copies (id 781).
- **Decipherment attached or implied:** D239 Throckmorton to Coleman 1674 (interlineated transcription), SP 36/73/3/66
  (deciphered copy at 71), Abercromby to Cornwallis PRO 30/11/128 (transcriptions), SP 92/14/239 ("modern copy"),
  SP 87 Prince Ferdinand / Bute / Clavering 1758-62 (about 60 "partly in cipher" letters: deciphers written over them
  in the volumes; descriptions never say they are missing), SP 87/13 "'101' [undeciphered]" (a name, not a cipher).
- **Calendars that already give the sense:** Bodleian Carte Papers entries "in cypher" (1660-80) and Lambeth Carew
  MSS (Ireland 1579-1602) are calendar entries from which the decipherment was evidently printed or summarised.
- **Routine bulk with decipherments in the volume, not listed individually:** SP 91 (Russia), SP 87 (Germany),
  SP 89 (Portugal), SP 90 (Prussia), SP 105; SP 78 1700s items mention cipher only administratively.
- **Kenyon family letters (Lancashire DDKE, 47 letters 1586-1694 "in code"):** private family code, importance 1.
  Worth a second pass if family ciphers are wanted. Grantham to Frederick Robinson 1778-79 (Bedfordshire L 30/15/54)
  has "[In Cypher]" passages that the catalogue already summarises, so likely transcribed.
- **Not ciphertexts:** "cipher" = arithmetic, monogram, "mere cipher" (a nobody), cypher boards (PRO 30/70/2/9),
  Cyphers Lane (Bristol), HCA 32/1208 Hebrew/Arabic papers, Persian translation IOR/L/PS/9/71/128.
- **1900-1950:** no ciphertext rows. HW (GC&CS), AIR, KV, ADM and WO files describe ciphers and telegrams
  administratively; not reviewed one by one.

## Key leads (bare keys, no ciphertext)

- SP 106/1-6 (cipher collections, Elizabeth to Anne), SP 106/14-64 (printed ciphers A.. 1737-57), PRO 31/17/2/1-2
  (Venetian ambassadors' keys 1500-1530, 1554-66), PRO 31/11/11 (keys 1527-34), PRO 30/57/11/25 ("Six code cipher"),
  WWM/Str P/3 (Strafford letter-book, key at front), Warwickshire CR 2017/C89 and C157 (Feilding/Morton cypher, Venice 1635),
  SP 35/73/50-52 and 35/47/52 (Plunket's cyphers), SP 78/163/10 (copy of a Jacobite cypher key 1719), SP 36/64/458
  (Jacobite cypher 1744), SP 54/10/175 (cipher taken from Lords North and Grey, 1715), SP 46/170/137 (prospectus for a cypher system).

## Blockers and limits

- Discovery gives descriptions only; no row was viewed on an image (State Papers Online is subscription, TNA images are by order).
- Elizabethan SP 12/63 etc. descriptions are brief and rarely mention cipher; nothing from them surfaced.
- Local-archive records (Staffordshire, Kresen Kernow, Isle of Wight) need a request to the archive for images.
- Files here: `tna.py`, `harvest.py`, `filt.py`, `make_candidates.py`, `hits.jsonl`, `matched.json`, `kept1.json`,
  `candidates.json`; `v*.txt` and `view_1660.txt` are working views.
