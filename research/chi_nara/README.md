# NARA Chicago sweep (28 Oct 2026)

Result: **0 candidates.** Nothing at the National Archives at Chicago turned up as an unsolved or possibly unsolved
ciphertext dated 1350-1950. `candidates.json` is an empty list. See `coverage.md` for term counts and what was opened.

## Method
- `client.py`: polite client (4 s spacing, stop on 403/429, cache in `cache/`, git-ignore it).
- `harvest.py`: filter `record.physicalOccurrences.referenceUnits.city:Chicago` AND ~65 terms (cipher family, coded,
  espionage, spy, Hindu/Ghadr/Gupta, secret/invisible ink, code AND message/telegram/letter/book, rum/liquor/radio AND
  code, Nazi, Bund, treason, named German agents ...). Output `raw/hits.jsonl` (3,607 records), `raw/harvest.log`.
- `triage.py` (noise/date filter -> `raw/triage.json`, 510 records), `show.py`, `series.py` (list a series),
  `ocr.py` (grep the OCR of a digitised file unit).
- Only 11 records at Chicago match "cipher"; all are noise (RG 15 newsletter, naturalization petitions, telegram
  boilerplate, civil transcripts).

## Findings worth passing on (not candidates)
1. **Hindu-German conspiracy, Chicago trial (Crim. 6082), is digitised** in the catalog: Bill of Exceptions naId
   540798683 (also Case Documents 540798684, 540798685). Government's Exhibit "Code" is Gupta's letter of 16 Nov 1916
   (to M. Albourge, Hotel des Alpes, Territet, Montreux, inside envelope for Chatterjee): seven sheets of
   three-digit groups, book cipher on Price Collier, *Germany and the Germans* (1914). Friedman's testimony
   (pp. 157-165 of the Bill) and the full decipherment ("Dear Ahatto: Am back from Japan ... Thakur real name Rash
   Vihari Ghose ... GUPTA") are printed. The numeral sheets themselves are not reproduced. **Relevance to
   `targets/gupta1917` and catalogue 694:** that target had only index cards for a Gupta cipher letter; the Chicago
   record gives a full plaintext for the Chicago exhibit (check whether it is the same letter as the M1194 card).
2. Detroit Behrens/Buchanan-Dineen (1943) and Stephan (1942) files are digitised but hold secret-ink and
   secret-writing testimony, not ciphertext.
3. Most Chicago court files that could hold exhibits (Hans Max Haupt, 661876551; criminal case files of the Prohibition
   era) have no digital objects and no description of a cipher. Exhibits "transferred from Chicago" sit at other
   facilities (326768051 etc.) and are indictments.

## Literature
Web searches (Hindu-German trial, Friedman at Chicago, Detroit/Great Lakes rum-running codes, WWI Chicago spy ciphers)
found nothing citing a NARA Chicago cipher exhibit beyond the Gupta "Code" exhibit. Rum-running code cases cited in
the literature (Friedman, CONEXCO, I'm Alone) are New Orleans, Gulf and Pacific, not Chicago.

## Not reached
- Undigitised RG 21 criminal case files and RG 118 US Attorney files: only reachable on site; their descriptions
  do not mention ciphers. An on-site request for Haupt (Chicago 1942) and the Prohibition conspiracy files would be
  the only way to find more.
- Full-text OCR search of all Chicago items (the proxy only returns hits, no snippets); only selected files were
  grepped.
- Termiology limits: parentheses in `q` fail (503), so queries were flat AND.
