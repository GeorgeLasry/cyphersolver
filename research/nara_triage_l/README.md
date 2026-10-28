# NARA triage, slice L: caps and word detectors on the 15 early record groups

The 15 record groups scanned before `research/nara_reels/bulk_all.py` existed (`DONE_EARLIER`: RG 59, 84, 45, 38, 165,
107, 393, 76, 11, 457, 65, 360, 109, 242, 94) had been run only with the frame, phrase, desc and letters detectors.
`research/nara_reels/bulk_cw.py` (27 Oct 2026) ran the two missing ones, `caps` (runs of capital-letter groups) and
`word` (cipher vocabulary), over every export file of those groups (5,951 files, the full groups; the export splits
each group into at most 400 files), into `nara_reels/out/rg_<n>_cw.jsonl` (git-ignored).

Hits: RG 59 63,427; RG 38 25,138; RG 165 7,973; RG 94 5,108; RG 242 2,200; RG 107 1,679; RG 109 808; RG 65 806;
RG 84 624; RG 45 125; RG 11 18; RG 457 16; RG 76 15; RG 360 2; RG 393 0.

## Method

- `caps.py`: caps hits grouped by item, best run first (3,407 items with a run of 8+); kept the 109 items whose OCR
  holds a real run of 6+ capital groups of 4-7 letters that are not header words (`caps_runs.txt`); all 109 read.
- `neg.py`: word hits whose context says the text was not read (undecipherable, could not decipher, no key,
  cryptogram, secret/invisible ink ...), 694 items (`neg.txt`, split into `neg_59.txt` and `neg_rest.txt`), read by
  two triage agents (`agent_59.md`, `agent_rest.md`).
- `groups.py`, `enigma_pairs.py`: frame-level views of fetched reels (OCR cached in `nara_reels/cache/`).

## Caps runs (109 items)

- **Row: Auckland 1918** (RG 59, M367 roll 83, naId 27107744): the cable Washington sent to the US Consul-General,
  Auckland, which he could not read (`candidates.json`).
- German Army Enigma, 1938 (RG 242, T311 rolls 42 and 123, Heeresgruppenkommando 2, the Westwall "Limes" works).
  Slice G had set these aside as "Enigma, out of scope". That was wrong as a scope rule: the catalogue takes any
  unsolved historical cipher. Both reels were fetched and checked. They are still not candidates, for a different
  reason. T311 roll 42 f.0471-0472 is OKH 1. Abt. Gen.St.d.H. Nr. 2050/38 of 21 Sept 1938, printed by Deavours and Kruh
  (*Cryptologia* 14:4, 1990, p. 342) and decrypted by Frode Weierud (cryptocellar.org/enigma/tbombe.html). On T311 roll
  123 every message carries the receiving clerk's pencilled start positions and has its clear draft filed beside it:
  Ia Nr. 602/38 (24 June 1938; f.15344-15345, clear f.15343), Ia Nr. 1120/38 (1 Aug 1938; f.15248-15249, clear
  f.15247), the nine-part OKW order of 31 Aug 1938 (f.15203-15205; clear f.15201) and OKH Nr. 1240/38 (17 Sept 1938;
  f.15139, clear f.15137-15138). They were read at the time. They are known-plaintext pairs for 1938 Army Enigma, a
  resource if the day keys are ever wanted, not unread text. (Frame numbers here are the last five digits of the
  objectIds of naId 272014076.)
- RG 242 T1022 naval items (Las Palmas 1940, Norddeich Sonderblindfunk, Kalorlux 1938): already catalogue 705-707.
  T1022 roll 2839 is a Hansa-Tafel supplement (reciprocal table, not a message).
- RG 242 T83 roll 93 (naId 543802963): IG Farben (Anilinfabrik Ludwigshafen) → "Karwender" New York, RCA radiogram
  17 June 1935, about 50 cipher groups (f.543803961); the "Chiffriertes Kabel" decipherment is the frame before
  (f.543803960, on lead tetraethyl). Read at the time; a crib pair.
- RG 242 T179 roll 22 (naId 331947319): Deutsch-Asiatische Bank cipher telegrams, Tsingtau/Peking/Shanghai 1938-39,
  each with its "Chiffre Uebersetzung" on the same frame; one 7-group Hongkong telegram of 28 Nov 1938 too short.
- RG 59 State Department 1870s-80s five-letter cipher telegrams (M92, M34, M31, M46): settled in slice D (clear text
  beside each). RG 59 1936 Gray-code telegram (Egypt) and RG 165 M1513 Tokyo consul message: Gray code, published, the
  paraphrases filed; not candidates.
- RG 38 USS Jarvis radio log, 12 Aug 1945 (naId 83522635): US Navy machine-cipher traffic in a radio log; not a candidate.
- RG 84 Djakarta, 4 Oct 1965 (naId 75583397): the Apostolic chargé d'affaires' cipher telegram to the Vatican
  Secretariat of State, sent through the US Embassy during the 30 September crisis, c. 75 groups. Unread, but after the
  catalogue's 1945 limit; recorded here only.
- The rest: forms, tables, name lists, ship lists, call-sign lists, codebook inserts, Western Union headers, OCR noise.

## Word hits (694 items)

Read by two agents (`agent_59.md`, `agent_rest.md`); their one confirmed lead was re-checked here from the cached OCR.

- **Row: Coahuila 1906** (RG 59, M862 roll 342, naId 19505183): Kickapoo-affair telegrams in a Mexican state code
  that the Mexican Embassy could not decipher (Root to Teller, 14 Nov 1907) (`candidates.json`).
- RG 59, other 333 items: about 150 telegrams in the Department's own codes that a post could not read (garbles,
  wrong tables), about 70 code-administration purport entries, about 40 illegible signatures, about 30 secret-ink
  mentions developed or only summarised, cipher inventors and newspaper puzzles. Pinckney 21 July 1795: deciphered on
  the copy sent to Congress (ASP Foreign Relations 1:534-35).
- Purport-only leads, followed up once the catalogue answered again:
  - **Row: La Paz 1941-42** (862.20224, purport naId 88161456): German, Japanese and French Legation code telegrams
    copied by informers; the FBI returned the German copies 'unable to decipher'. File not digitised.
  - **Row: Lima 1941** (862.20210 Transocean, purport naId 88159920): Dr. Otto Joseph's code messages, not decoded 'as
    cipher tables are not available'. File not digitised.
  - **Catalogue 669 unblocked**: the Soviet radio intercepts forwarded from Constantinople in 1921 (861.00/8575, 9071,
    9130-9133; purport naId 87657409) are filmed on M316 rolls 40-48, digitised as RG 64 copies: about 390 frames of
    typed Soviet and German cipher radiograms (Moscow-Berlin, Stockholm, Christiania, Nikolaev-Kharkov), about 62,000
    groups, with Bristol's despatches saying they could not be deciphered. Entry 669 (the RG 457 copies, not digitised)
    now points to them.
  - Grimes, Manila 1898-99 (naId 153563607, fetched): the seized cipher papers are not in the file. Van Ness, Madrid
    1832-33: closed, not a row. Livingston (12 Apr 1833, M77 roll 142 f.0024) says two despatches were 'written in a
    cypher to which we have no key' and sends the new cipher; Van Ness (M31-031-0184) answers that he had used the latest
    cipher in the legation archives, that each despatch held only 'a paragraph or two in cypher', and sends duplicates.
    Neither names the despatch numbers. Frames M31-031-0100 and 0113-0141 (Nos. 46-50, Dec 1832 - Feb 1833) were viewed:
    clear text and translations only; the OCR of vols 30-31 has no figure runs. The passages are not located and are a
    few lines at most; if found, try targets/jqa/code_table.tsv (the older Madrid code).
- Other groups (360 items): 249 already covered by slices A-K (all RG 165 and RG 65 items); the unread items they
  touch are catalogue 674-703; card-only MID leads already declined in slice E; RG 38 war diaries about the Navy's own
  undecipherable traffic and ONI ink formulas; RG 94 inventors' systems (Fuller 1878, O'Neill/McManus 1884; Wherry 1878
  deciphered); RG 107/242/76 noise.

## Result

Four rows: 757 (Auckland 1918), 758 (Coahuila 1906), 759 (La Paz 1941-42), 760 (Lima 1941); entry 669 unblocked (M316, 1921 Soviet intercepts). With this slice every detector has run over every record group
and collection of the export.

## Second pass: forwarded and intercepted foreign code telegrams in the purport lists

The negation filter above only kept entries that say a text was unread. The La Paz row showed that the 1940-44 purport
lists also record legations forwarding "code copies" of foreign telegrams without saying whether they were read, so
the RG 59 word hits were searched again for code-copy and intercept wording (`axis_copies.txt`, 601 items on a broad
pattern; 84 on the strict one: code copies of, copies of code/cipher telegrams, intercepted code/cipher/radio,
obtained copies of). Most are the Department's own code traffic. The foreign-traffic entries:

- Bolivia 1941-42 (862.20224): row 759. The purports add that the FBI identified the La Paz copies as "the German
  diplomatic code" (Jan 1942) and returned two Bolivia/Argentina → Germany code messages "undecoded" (8 Dec 1941).
- Paraguay 1933 (Kreeck #995, M973-339-0494): intercepted messages of General Kundt "together with code used to
  decipher" them. Read at the time; not a row.
- Navy Dept / USCG 1941-42 (862.20210 purports, M973-590): "Deciphered communications of German secret agents",
  the clandestine-radio decodes (Coast Guard). Read; not rows.
- São Paulo 1943 (M973-568-0661): German station DAN traffic, "machine enciphered for submarines": naval Enigma
  traffic, read by the Allies at the time; out of reach and not filed as text here. Not a row.
- Mexico 1941 (Justice, 812.614 purport M973-559-0637): intercepted radio message Mexico → Germany submitted
  "deciphered and translated". Not a row.
- Unresolved, purport only, no statement that the text was unread, so not rows: Chile #2431 (Dec 1940), one
  intercepted code message from the German Embassy Santiago to the Auswärtiges Amt (M973-540-1402); Mexico #10834
  (19 June 1940), copies of code messages of the Partido Nacional Socialista Mexicano (812.00N/220, M973-537-0643);
  Spain #784 (1942), messages of Agustín Mutiozábal that "may have been code messages" (M973-534-0750). A NARA
  catalogue search for the 812.00N purport list timed out on 27 Oct 2026, and no further requests were sent.
