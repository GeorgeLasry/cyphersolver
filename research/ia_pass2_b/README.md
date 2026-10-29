# Internet Archive, second pass B (series list), 28 Oct 2026

Brief: `research/archive_sweep_2026-10/BRIEF.md`. Output: `candidates.json` (22 rows, built by `rows.py`). No edits to catalogue.json or docs/.

## Method
* `find.py`, `find2.py`, `ids*.json`: advancedsearch title queries for the assigned series (about 700 volumes listed). `dl2.py`: downloaded the djvu OCR of about 330 volumes into the session scratchpad (not the repo): Stuart Papers (all 7), Thurloe (7), Ormonde calendars (old and new series, 15), Clarendon calendar II-V, Treasury Papers/Books (about 25), CSP Colonial (9), CSP Ireland (about 17), CSP Scotland (3), Carew IV, about 90 HMC reports (Rutland, Portland, Lonsdale, Buccleuch, Mar & Kellie, Kenyon, Egmont, Downshire, Stopford-Sackville, Middleton, Denbigh, Pepys, Finch ...), Nicholas Papers, Rawdon, Egerton, Birch's Royal Society, Home Office Papers 1760-75, Burnett's Letters of Members of the Continental Congress I-VI, VIII, Manning's Latin-American diplomatic correspondence, Monroe calendar, Montereul (SHS).
* `extract2/3/4.py`, `ex5.py`, `allc.py`, `allc2.py`: regex families (cipher word within 70 characters of undeciphered / not deciphered / uninterpreted / no key / illegible; "partly/chiefly in cipher" with no decipher nearby). `fnd.py`, `cn.py`, `hdr.py`: print the window and find the entry heading; every row was read by hand. `fts_deep.py`: 20 phrase queries x 8 pages on the archive.org fts endpoint (3,001 volumes seen, 89 in the assigned series), results in `fts_deep.json`, `fts_view.txt`.
* Dedup with `known.py` (Norreys, Yard, Poinsett, Anderson, Everett, Jay, Hyde, Fontenay, Liggons, Chichester ...). 
* Counts: about 330 volumes read by regex, about 700 windows read by hand, 22 rows kept (class A 8, B 5, C 9), 0 viewed on images (`seen: catalogue`).

## Best leads
1. **Clarendon calendar II no. 540** (Hyde's instructions to Edgeman, 13 Jul 1651): plain draft plus two copies mostly in the King's cipher and Nicholas's cipher; a built-in crib pair (solvability 4).
2. **Mary Queen of Scots, SP 53/15 nos. 81-82** (Liggons, c. 30 Apr 1586): copy "undeciphered" beside the copy deciphered by Phelippes; **SP 53/16 no. 1** Fontenay to Nau, 1 Jul 1585 (interpretation illegible); **Chateauneuf to Courcelles, Sept 1586, nos. 72-73** (two French embassy cipher letters, no decipher listed).
3. **CSP Ireland James I 1606-08 no. 634**: Chichester to Salisbury, printed numbers with the cipher "sent unto me"; **HMC Ormonde n.s. VI pp. 192-193** Jenkins to Ormond, printed numerals with a printed partial key (solvability 4).
4. **Hyde to Ormonde, Dec 1654** (Clarendon II no. 2092, "undeciphered by Ormonde") and the other undeciphered scraps in Clarendon II-III (nos. 1667, 1824, 1867, 595, 874).
5. **Laud to Wentworth, Sept 1636** and **Bennet to Ormond, 12 Dec 1668**: CSP Ireland omits "a passage in cipher".
6. John Jay to Congress, 28 Jan 1781 ("largely in cipher and undeciphered", Burnett vol. VI); Montereul to Mazarin June 1647 (8 lines) and Bellievre to Brienne (9 lines).

## Dropped as already in the repo
Norreys to Leicester/Cecil in the Pepys MSS (catalogue id 872); Yard to Manchester 12 and 16 Oct 1699 (targets/yard1699, solved); Poinsett 20 Feb 1813, Anderson/Revenga 19 Jan 1824, Everett 25 Sept 1825 (nara_state rows). Also dropped: items where the same entry or the editor deciphers (Finch/Turkey 1661-62, Lee letters in Burnett vol. III key = Entick's dictionary, Egmont/Percivall 1647 draft with no identifiable sender, Rebbe/Gail letters in Downshire IV which are name-code words not ciphertext).

## Key leads (not rows)
* Burnett vol. III p. 231 note: Lee family book cipher = Entick's New Spelling Dictionary (page, column a/b, roman word number); editor already decoded.
* Ormonde n.s. VI Introduction p. xix: key to Longford's cipher; Ormonde n.s. I (1643-47): printed key (Muskerry letters, "1-3 k, 19-21 q ...").
* Stuart Papers IV p. 103: "no key" to the Mar-Tullibardine-Campbell of Glendarule cipher; Stuart II p. xlii and III pp. 97-98: lists of cipher names "not deciphered in the originals".
* Clarendon III: "copy of the cipher" sent with Thurloe-side letters (c. no. 1031); CSP Domestic Commonwealth 1659-60 has many "cypher to which there is no key" notes (not in this series, not itemised here).
* Heathcote/Finch/Pepys notes per pass 1.

## Dead ends
Thurloe State Papers (1742): printed letters give decyphers in clear, no undeciphered notes. Calendar of Stuart Papers: only name lists, no item-level "undeciphered". Treasury Papers/Books, Colonial (America and West Indies), Mar & Kellie, Rutland, Lonsdale, Buccleuch, Home Office (apart from no. 301), Nicholas Papers, Rawdon, Egerton, Royal Society history: cipher words only in the sense of "cipher = nought", decipherers' salaries or deciphered letters. Thorpe's Scotland calendar marks hundreds of entries "[Chiefly in cipher]" but these are summarised from the deciphers, so they are not unread. Monroe/Madison calendars: Madison's own decipherment is in the Papers of Madison.

## Not reached / blockers
* Failed or restricted downloads (HTTP 401/403): Stuart Papers 2016 reprint, Treasury Books 1702, HMC Downshire vols 1-6 other than V1Pt1, Supplementary Hamilton, Rutland (bwb), Burnett vol. VII, VIII (one copy), Eighth Report only via a differently named file.
* Hardwicke State Papers, Journals of the Continental Congress, Official Records (Army and Navy) and Calendar of Home Office Papers after 1775 were not searched in full (OR/War of the Rebellion have thousands of telegram "cipher" mentions that are not European classical ciphers).
* Entry numbers marked "to confirm" (Ireland 6146 sender spelling, Montereul/Bellievre date, Clarendon dates taken from margins) need the printed page. Web checks: only the Mary Queen of Scots rows were searched online (no decipherment found); the rest are "printed edition only".
