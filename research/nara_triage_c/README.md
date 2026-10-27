# NARA bulk-scan triage, slice C: military, naval, intelligence, law enforcement (27 Oct 2026)

Brief: `research/nara_reels/TRIAGE_BRIEF.md` and `research/archive_sweep_2026-10/BRIEF.md`. Input: the bulk-scan
hits in `research/nara_reels/out/` for RG 38, 45, 65, 107, 11, 165, 360, 393 and 457. Classical hand ciphers and
codes only, 1775-1950; machine traffic (Enigma, Purple, Hagelin, SIGABA, Fish) left out. Checked against
`research/nara_military/README.md` and `research/nara_catalog/README.md` (catalogue entries 628-648) and with
`known.py`: no row here duplicates them (the PCC Intercepted Letters, Greenhow, Johnston, Astrea and Eckert leads
are theirs).

Files: `candidates.json` (22 rows), `rows.py` (the rows as code; `python research/nara_triage_c/rows.py`
rewrites candidates.json), `rg457_desc_titles.txt` (all 1,703 RG 457 description hits, naId + title, as read).

## Method

- Read every `desc` hit title (RG 457: all 1,703; RG 38: 699; RG 45: 16; RG 165: 25; RG 107: 5; RG 65: 2;
  RG 393: 5; RG 360: 6).
- Grouped `frame` hits by item and parent series (`agg_rg_*.tsv`) and read the OCR snippets of the top items per
  series; grouped `phrase` hits by item and read every non-boilerplate context.
- Fetched 52 catalogue records with `reels.py fetch` (4 s spacing): every RG 457 / RG 38 / RG 45 / RG 165 / RG 393
  lead below. **None of the RG 457, RG 38 A6-3, ONI attaché, CNSG or RG 393 leads is digitised** (no digital
  objects), so those rows are catalogue-only, solvability 1-2.
- Fetched and searched the OCR of five digitised reels: M1024 roll 310 parts 1-2 (War College Division files
  10018-10049), M1085 roll 598 part 3, M1085 roll 259 part 2, M1085 roll 940 part 4 (Bureau of Investigation case
  files), and the RG 65 Sacramento field-office box. No page images were downloaded.

## Coverage and conclusions, per record group

| RG | hits (frame / phrase / desc) | what they are | kept |
|---|---|---|---|
| 457 NSA HCC | 9 / 0 / 1,703 | Descriptions: ~85% codebooks, cipher machines, TICOM, SRH, Japanese JN systems, training texts. Frames: Turing's treatise (machine). | 13 rows (unsolved-problem file, suspect messages, WWI/WWII intercept files) |
| 38 CNO/ONI | 57,145 / 120 / 699 | Frames: 42,908 flagged in 5,030 WWII war diaries (position/time tables, logs), 989 in 174 submarine patrol reports, tide/moon tables, maps, ship-casualty lists, attaché statistics (M975). Phrases: "in cypher"/"undecyphered" in Admiralty war diaries and patrol reports (WWII naval traffic, machine or out of scope). Descs: 600+ US Navy cipher publications (CSP/USF/NCB/RIP/JN), GCCS liaison files. | 3 rows (ONI A6-3 civilian/Coast Guard submissions; attaché "code messages"; POW letters, merged with RG 457) |
| 45 Naval Records | 3,201 / 52 / 16 | Frames: Confederate Navy subject files (clothing, provisions, yard labour accounts: 80 items) and officers' letters (postage-stamp returns, pay abstracts). Phrases: all 52 are the telegraph-blank clause "errors in cipher or obscure messages". Descs: "Translations of Messages Sent in Cipher" and "Cipher Messages Received and Translated" (decoded, 1898-1911); Roosevelt→Dewey 1898 (famous, decoded); the CSN "DC codes" file (Greenhow key, already catalogued). | 0 |
| 165 WDGS/MID | 7,033 / 176 / 25 | Frames: M1024 War College Division files (statistics, range tables, census tables, microfilm roll lists), MID regional files. Phrases: "in cipher" in ordinary correspondence; 14 non-trivial contexts read, 4 kept from the MID/WCD name indexes (M912, M1194). | 4 rows (Tampico 1917, Guaymas 1918, San Luis Potosí 1918, German agent via Switzerland 1918) |
| 107 Sec. of War | 2,304 / 1,075 / 5 | Frames: name/subject index volumes (M420, M492), accounts. Phrases: M473 telegram books, where "In cipher" heads the plain-text office copy (read at the time), plus form boilerplate. Desc "Telegrams in Cipher" (628803) carries its decipherment worksheets. | 0 |
| 11 General Govt | 205 / 2 / 0 | Indian treaties, colour-bar targets, amendments. | 0 |
| 65 FBI | 591 / 111 / 2 | Frames: JFK assassination records (out of period), crime reports, steel price tables. Phrases: Western Union form clause (90+), plus 6 real contexts in the Old German Files (M1085). | 1 row (1920-21 Communist Party book code) |
| 393 Army commands | 51 / 0 / 5 | Frames: hospital liquor ledgers, fort plans, census. Descs: three cipher-telegram series 1865-68 (not digitised). | 1 row |
| 360 Continental Congress | 36 / 0 / 6 | Frames: colour targets; the Peace Commissioners' cipher table (a key, already listed by nara_catalog). Descs: "Translation of Resolution in Cipher Regarding Fisheries" (1782, interlinear translation, read); Intercepted Letters (already catalogued). | 0 |

## Best leads

1. **Communist Party of America book code, 1920-21** (RG 65, M1085 roll 940, case 202600; digitised PDFs). 77
   runs of line/letter fractions in letters seized at 170 Bleecker St.; 27 carry the Bureau's "Decode:" line, about
   50 do not. The decodes are cribs for the key page; the party's own instruction sheet is copied in 940C. The one
   lead here that can be worked from images online now.
2. **The "Tampico message", 1917** (RG 165, WCD/MID file 10020-60): Riverbank reported it could not solve it, and
   sent monthly lists of "undeciphered messages" (10020-64). File transferred to MID (withdrawal card, M1024 roll
   310 frame 0051); not digitised.
3. **GC&CS CCR "Unsolved Problems" 1944** (RG 457, 47647A): a register of traffic GC&CS could not read; hand
   systems in it unknown.
4. **Code messages found in the ex-German Embassy archives, Buenos Aires** (RG 457 NR 2054, 1945) with the
   clandestine-radio file NR 1403.
5. **British naval officer's request for US help with ciphers, Sept 1915** (RG 457 NR 4841), and the 1917
   censorship/German espionage codes file (NR 4458).

## Key leads (no ciphertext)

- RG 457 holds many commercial and government code books that could read stray code telegrams: Peruvian
  Commercial Code Book 1912 (NR 404), Spanish Commercial Code Books 1894 (NR 516), Larrabee Cipher Code 1876
  (NR 1025/2239), Portuguese Code Books 1910 (NR 513), Russian code books "1900" (NR 1300/1302/3485), Greek
  cryptographic lexicons 1927-41, Brazilian Diplomatic & Consular Code 1939 (NR 3923), "Monroe's Cipher" (7655N),
  "Ciphers of the Revolutionary Period" (7623N), "Nikolai Imperial Russian Cipher Table" (6700). None digitised.
- RG 38: CSP 423 State-Navy Department Cipher, 1921 (naId 7531417); CSP 579 Naval Attaché's Cipher (7531445/6);
  Radio Cipher "C", US Atlantic Fleet 1912 (7531838); N.C.B. cipher boxes 1917-18. Keys for US naval traffic.

## Dead ends (read at the time or not cipher)

- **M1085 roll 598, case 193804** (frame 2195): a mail censor's report on I.W.W. letters "written in cipher ...
  characters containing dots up to three in number" (a pigpen). He "worked out the following key" in the same
  report, so it was read at the time. Not a row.
- **M1085 roll 259, Otto Carl Doerrier** (Redondo/Hermosa Beach, April 1917): newspaper clippings about a "code
  book" and map paper; the file has no ciphertext, and Doerrier was held as insane. Not a row.
- M1085 Agassiz clipping (San Diego, 1918): chalk "hieroglyphics" on the captured schooner, newspaper only.
- RG 457 MI-8 Mexican ciphers 1917-19 (25757 series, NR 2079, 2088, 2242), Witzke/Waberski (NR 2061), Zimmermann,
  Fellers, Goertz, Baarn/Kopff explanation (NR 4061), Martinique decipherments (NR 1023), Colombian and Swiss
  cablegrams "showing decoding" (NR 4017, 4224), Vichy decodes: all solved at the time.
- RG 457 NR 3471/3470 secret-ink letters (not cipher); NR 4086 "Information on Code Messages" (too vague to row;
  order with NR 2054 if visiting).
- RG 107 M473 and M504 "in cipher" (1,075 phrase hits): plain office copies of telegrams sent in cipher.
- RG 45 and RG 65 "errors in cipher" (140+ phrase hits): telegraph-form boilerplate.
- RG 165 M1444 China file: "two telegrams which could not be decoded" (Soviet embassy, 1920s) is a report
  statement, no ciphertext.
- RG 38 WWII war diaries, patrol reports, Admiralty war diaries: WWII naval/machine traffic, out of scope.

## Not reached / blockers

- **Nothing in RG 457, the RG 38 A6-3 and CNSG files, the ONI attaché registers or RG 393 cipher series is
  digitised.** All those rows need a College Park visit or a reproduction order.
- MID file 10020 (Riverbank 1917) and the MID files behind the M1194 index cards are in RG 165 entry 65, not
  digitised. The index reels (M1194, M912) are digitised and could be searched further for "cipher", "code",
  "decipher" across all 261 M1194 rolls; only the cards that the bulk scan flagged were read.
- Other parts of Bureau case 202600 (M1085 roll 940 parts 1-3) were not searched for more book-code letters (a
  catalogue query was still pending when this was written).
