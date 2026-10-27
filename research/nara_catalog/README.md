# NARA catalogue keyword sweep (27 Oct 2026)

Part of the October 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). A keyword sweep of the whole
National Archives Catalog (all record groups, series / file unit / item descriptions), looking for documents in
cipher or code dated before 1951 with no decipherment noted. Separate sweeps cover State Department despatch
microfilm, FRUS and the Papers of the Continental Congress (`research/nara_state/`), and the military and
intelligence record groups RG 38, 45, 65, 94, 107, 120, 165, 242, 393, 457 (`research/nara_military/`); rows here
that fall in those areas say so in `status`, for dedup at the merge.

Output: `candidates.json` (6 rows). Scripts: `harvest.py` (query runner), `triage.py` (date and noise filter),
`show.py` (print one record). `raw/` holds the harvest (`hits.jsonl`, 8,563 records), logs, triage tables and
the Greenhow series listing; it is regenerable and can be git-ignored.

## Method

- Endpoint: `https://catalog.archives.gov/proxy/records/search?q=<lucene>&limit=100&page=<n>` (JSON, no key).
  `?naId=<id>` returns one record; `?ancestorNaId=<id>` lists everything under a series or file unit.
- Quirks found:
  - Any parenthesis in `q` gives HTTP 503, so every query is a flat `A OR B` / `A AND B`.
  - A quoted phrase inside a field query (`record.title:"in cipher"`) returns 0.
  - `limit=2` returns the HTML app shell; 20 and 100 work.
  - Under load the proxy intermittently returns the HTML shell instead of JSON; a retry fixes it.
  - `startDate` / `endDate` do filter, but undated file units would be lost, so dates were filtered locally from
    the record, its series and its title.
- A plain `q=` also matches the OCR text and citizen transcriptions of digitised pages. Those hits come without a
  snippet. The per-object text is at `/proxy/extractedText/<naId>?objectId=<id>` and `/proxy/transcriptions/naId/<id>`
  (found in the site's JS bundle, not used in bulk).
- Field queries on `record.title` OR `record.scopeAndContentNote` for: cipher, ciphers, ciphered, cypher(s/ed),
  cryptogram(s), cryptographic, cryptography, cryptographer, undeciphered, decipher(ed/ment), decyphered,
  undecoded, decode(d), nomenclator, codebook(s), chiffre(s), Geheimschrift, cifra, cifrado, chiffriert,
  enciphered, encoded, intercepted. Then `code AND {message(s), telegram(s), cable(s), letter(s), dispatch,
  despatch, book, key}`, `secret AND writing`, `invisible/secret/sympathetic AND ink` and `cipher AND key`, each
  on title and on scope note.
- Full-text (OCR) queries: undeciphered (105), "not deciphered" (114), "not decoded" (89), "could not be
  deciphered" (130), "not been deciphered" (18), undecoded (29), "en chiffre" (233), nomenclator (38), cryptogram
  (128), "in cipher" (7,679; first 3,000 taken).
- Hit counts per query are in `raw/harvest.log`. Totals:
  - 8,563 distinct records; 6,411 are dated before 1951 or undated.
  - 4,768 came from field (metadata) queries.
  - After dropping RG 457 and RG 38 technical files and the noise (surname Cypher/Cyphers/Cifra in census,
    pension, service and naturalisation files; building, legal and NRA "codes"; Morse; post-1950), about 1,400
    field hits were read by title and scope note.
  - 485 rare-phrase full-text hits were grouped by series and sampled.
- Kept: 6 rows. The catalogue is mostly series- and file-unit-level. Item-level descriptions that name cipher
  content exist mainly in exhibit series (RG 59 Miscellaneous Letters M179, the Greenhow papers, the Lincoln
  assassination exhibits, Confederate telegrams).

## Best leads

1. **Astrea packet, 1798-99** (French consular dispatches in cipher to Talleyrand, captured at sea, sent by consul
   Gavino at Gibraltar). Adams's cover letter (RG 59 M179, naId 55028996) says the packet "has not been
   deciphered". Lovell could not make a key. Rozier later showed Pickering his cipher and some passages were
   checked. Where the ciphered papers are now is the open question.
2. **Rose Greenhow's cipher letters, 1861** (RG 59 series 873765; 4 cipher pieces, all imaged; more in RG 107
   series 642808, not imaged). This is a symbol cipher, and a key survives at the North Carolina State Archives.
   Her cipher was broken in 1861, but the readings of the individual NARA pieces have not been found.
3. **Cornwallis ↔ Balfour cipher letters, 1780-81**, in PCC Intercepted Letters vols. 1-2 (imaged; "some
   decoded"). Probably in Saberton's edition. PCC overlap.
4. **Johnston → Seddon, 16 Jun 1863** (RG 109, naId 3854726, imaged). Five Vigenère-style cipher words; the three
   known Confederate keys failed in a quick test. Check the Official Records first.
5. **PCC Miscellaneous Papers (item 59)**: "communications in cipher" filed with the Franklin / Jay / Dumas keys.

Then: the Union Army cipher telegram books 1864-68 (RG 107, 108, 393; series only, low priority).

## Key leads (bare keys, no ciphertext)

- RG 55 (Government of the Virgin Islands, Danish period), General Correspondence: "Cipher Keys (Chiffre
  dechiffrant for General Gouverneuren i West Indien), n.d." (naId 311875940, not imaged). It may read ciphered
  letters of the Danish West Indies governors in RG 55 or in Rigsarkivet.
- RG 360 PCC item 59: "Cipher With Keywords" (naId 631635424) and "Ciphers Belonging to the Various American Peace
  Commissioners" (naId 2450021, imaged).
- RG 109, Reports and Other Confederate Papers (series naId 2524780): "an incomplete copy of the 'Rebel Cypher'".
- RG 153, Lincoln assassination exhibits: Exhibit 7, "Secret Cypher found among John Wilkes Booth's effects"
  (naIds 85696363, 38995511), the Confederate Vigenère table.
- RG 59 M179: Mr Forrest to Daniel Brent, 4 Nov 1817, "submits the cipher" (naId 80608078).
- RG 59 Code Books series (naId 2034503) and "Codebooks of the Department of State, 1867-1876" (naId 417267710,
  587 images). These are State Department codes that can read consular/diplomatic code telegrams of 1867-76.
- RG 104 "Telegraphic Code Key" (1902, naId 1132821); RG 350 "Code Translation Volume" (1898, naId 562007).

## Leads not confirmed as cipher (worth a look, not rows)

- RG 59 "Miscellaneous Intercepted Correspondence, 1789-1814" (M588 roll 7, naId 222577038, 593 images):
  intercepted British military letters 1780-1807, British Foreign Office correspondence July-Nov 1812, and private
  letters 1812-14. Whether any are in cipher was not checked.
- RG 59 "Intercepted Letters and Papers" (Confederate agents abroad, series naId 875749); RG 109 "Intercepted
  Confederate Letters" (2524782); RG 111 "Intercepted Letters" 1864 (2668866, examined "for possible hidden cipher
  code messages"); RG 107 intercepted letters 1864 (643052, copies only).
- RG 109 "Dispatches Intercepted by the Confederate Department of South Carolina, Georgia and Florida" 1863-64
  (734537): copies of intercepted Union dispatches at Charleston, probably Union signal-flag traffic as read by the
  Confederates.
- RG 59 Adams to Pickering, 10 Oct 1798 (naId 53770456): enclosed letters "to be deciphered" (probably US
  despatches deciphered at State; not checked).
- RG 45 Lt. Albert P. Niblack letters 1896-97 (naId 1729196): a few cablegrams "in cipher code" (US Navy code; the
  companion "Cipher Messages Received and Translated" series exists). RG 45 overlap.
- RG 457 "Mexican Ciphers Intercepted, 1918 (November)" (naId 7827047) and "Correspondence re Solution of a
  Mexican Cipher" (NR 2088). These are MI-8 work, probably solved. RG 457 overlap.

## Dead ends and noise

- "Cypher/Cyphers/Cifra" is a common surname. About 40% of the field hits are name files: census, pension,
  compiled service records, naturalisation, alien files.
- Full-text "undeciphered" / "could not be deciphered" almost always mark an illegible word in a citizen
  transcription (Revolutionary prize cases, pension files, Indian treaties). They also turn up as garbled-telegram
  notes in State Department despatches and decimal files (1897-1944), which is the nara_state sweep's ground.
- "Translations of Messages Sent in Cipher" (RG 45), consular "True Readings of Cipher/Code Telegrams" (RG 84)
  and the Lincoln assassination Exhibits 60, 61 and 79 (RG 153, decoded, or "with key") all carry their
  decipherments.
- "Letter from Wilkinson, 1813" (RG 59 M179, naId 60385152) includes its own deciphered copy.
- The Zimmermann telegram items (RG 59) are solved and famous.
- Venona (RG 263, naId 2775191) is a Soviet one-time pad, largely unbreakable, and outside this sweep's scope.
- RG 457 / RG 38 field hits (about 2,600) are almost all post-1930 technical files (cipher devices, CSP manuals,
  TICOM, SRH histories), left to the nara_military sweep.

## Not reached

- Snippets for the 3,000 "in cipher" full-text hits. The phrase is not matched exactly, and most hits are telegram
  forms and boilerplate. A per-object text pass through `/proxy/extractedText/` was not run.
- Item-by-item paging of the imaged PCC volumes, the M588 intercepted correspondence and the RG 59 M179
  Miscellaneous Letters for unindexed cipher.
- The Official Records check for the Johnston telegram and the Greenhow pieces.
