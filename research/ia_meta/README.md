# Internet Archive, metadata route (Oct 2026)

Scripts: `harvest.py` (advancedsearch.php over ~60 cipher terms in 10 languages x title/subject/description, 1350-1950, mediatype texts,
2,156 raw hits in `raw_hits.json`), `q2.py`/`q3.py` (collection-targeted queries: openn, upenn, wellcome, smithsonian, americana,
library_of_congress, bostonpubliclibrary), `fts.py`/`fts2.py` (archive.org full-text search API, be-api.us.archive.org/fts/v1/search,
phrases such as "in cipher, undeciphered"), `cal_find.py`/`getcal.py`/`extract.py` (download ~58 djvu texts of printed calendars and pull
every "cipher ... undeciphered / not deciphered" note: 150 hits in `cal_hits.json`/`cal_hits.txt`), `build.py` (writes candidates.json).
Downloaded texts are in `_txt/` (git-ignored).

## Findings
- IA's catalogue metadata almost never describes cipher content. Title/subject/description searches return printed treatises, telegraph
  codebooks, CIA/NSA files, newspapers. Real manuscript hits: only Penn Ms. Codex 88 (cryptogram f. 80r, 1449), via OPenn.
- The productive route is full text of printed calendars on IA (LP Henry VIII, CSP Foreign/Domestic/Ireland, Clarendon calendar, HMC
  reports): their "cipher, undeciphered" notes identify individual unread manuscript items. 27 candidates written.
- Caveat on every calendar row: the note means no contemporary decipherment in the MS; LP editors may have read some of it.

## Best leads
1. Ghinucci/Worcester Rome despatches to Wolsey, Nov 1525 - Sep 1526 (5 rows; BL Cotton Vitellius B VII/VIII; key from targets/ghinucci1527).
2. Spinelly 1518 Spain despatches (3 rows; Spinelly key already known).
3. Gunpowder Plot "E. F. Mak to Bankes" letter, 2 Nov 1605, partly cipher.
4. Charles I -> Ormond Jan 1645 and Hyde -> Nicholas Apr 1646 (Clarendon calendar nos. 1815, 2505).
5. Penn Ms. Codex 88 f. 80r, 1449 (pre-1497).

## Key leads (not ciphertexts)
Cypher Collections vol. VI no. 35g (De Vaux/Du Chastel key); Collection of ciphers of Queen Elizabeth vol. I nos. 63-64 (Lee/Norton);
Pepys MSS note on Chaloner key; Finch/Turkey 1680s letters (key among the papers); Calendar of Stuart Papers ("great mass not
deciphered", Jacobite) not itemised; Lucrezia Borgia 1510 Modena letter (IA item `giornalino-lettera-cifrata-lucrezia-borgia_202501`) already decrypted by D. Palma.

## Dead ends / skipped
Deciphered or printed in full: Leverett letters (NEHGR 1894), Plan de conduite 1788, Salvetti (HMC Skrine), Du Bellay Oct 1529 (Lasry), Stile
"(In cipher)" abstracts. Tiny cipher words in Carew (1602), Scotland (Davison, Fowler), Ireland (1600-01) calendars not itemised.

## Not reached
Only ~58 of ~700 calendar volumes were scanned (CSP Venetian/Spanish/Colonial, Treasury, Cecil/Salisbury, HMC Reports left);
failed downloads: Letters&Papers vols 2.1/3.1/3.2 (404), Eighth HMC, Downshire. Nothing was checked against DECODE by R-number beyond
known.py; no manuscript images viewed. Web search done only for the Mak letter and Fanshaw.
