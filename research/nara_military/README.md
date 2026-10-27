# US military, intelligence and captured records sweep (Oct 2026)

Slice: Civil War (RG 107/109/94/393, Eckert papers), Navy/ONI/Coast Guard and MI-8/RG 165/RG 457, captured and
foreign records (RG 242, RG 65 FBI, RG 59/60 cases), 1775-1950, classical hand systems only (machine traffic left
out). Worked from series and the literature (Schmeh/Cipherbrain, Tomokiyo, CryptoCellar, NSA/NARA guides); the
plain keyword sweep of the NARA catalogue is another agent's job. Brief: `../archive_sweep_2026-10/BRIEF.md`.

`candidates.json`: 13 rows. `add.py rows.json` appends rows (field check, dedup by title).

## Method

- NARA catalogue: `https://catalog.archives.gov/proxy/records/search?...` answers JSON in a browser-like fetch
  (WebFetch), but plain `curl` gets the SPA shell, and retrying with browser headers was refused by the session's
  permission classifier, so no scripted harvest. Useful forms: `?naId=<id>` (one record, ancestors, image URLs) and
  `?q=record.ancestors.naId:<series> <term>` (search inside a series). Free-text queries are swamped by OCR of
  microfilm (`"in cipher"` = 7,679 hits, responses of 1-3 MB), so they are useless without a series filter.
- Images: `catalog.archives.gov/medialive/...` URLs download directly; a handful viewed in the session scratchpad,
  none kept in the repo.
- Dedup: `known.py` for every lead (Johnston, Bunch, Greenhow, Truppenschlüssel, Schleswig, BBBTT, Eckert, Clinton
  Papers, Armstrong, Milroy, ADFGVX, Köhler, Yardley, Friedman ...).

## Best leads

1. **Greenhow cipher letters, NARA RG 59 Seized Correspondence of Rose O'Neal Greenhow** (NAID 1634036 mourning-paper
   letter, 1634051 Jordan→"Rachel", 6925618 burnt fragment). Images online, viewed. **Key found in the same archive**:
   RG 45 M1091 Confederate Navy subject file "DC - Codes and cryptography - Misc." (NAID 62017285, images 0483-0485),
   "Confederate cipher 1864", found on Greenhow's body off Fort Fisher: symbol alphabet, digraph signs, code signs
   for Washington, Richmond, Lincoln, Pennsylvania Avenue, Virginia etc. Same sign family as the 1861 letters, so
   this should be a key alignment (difficulty 2). The neighbouring file "DX - Courier and secret service" (NAID
   62017748, 34 images, contact-sheeted) holds typed transcripts of Greenhow's Dec 1861 dispatches as deciphered by
   the Confederates (Conf. War Dept. vol. 1) and says "the cipher is incoherent"; useful as cribs. No ciphertext there.
2. **Robert Bunch, British consul at Charleston**: four letter-group cryptograms (Schmeh 2018), Playfair and
   Vigenère failed; holding to be traced from Dickey's endnotes.
3. **German Army Truppenschlüssel messages, 1941**: 30 unbroken messages of a hand field cipher (Ostwald & Weierud,
   CryptoCellar list updated 27 Jul 2026), grouped here by net and day (pz6 4 July = 8 messages, 683 letters).
   Cryptoole's CryptoCellar rows were dropped wholesale as "Enigma" by `research/cryptoole/pull.py`; that filter
   also threw out these hand-cipher rows (DE1941-3 ... DE1941-35), so they were never considered.
4. **Eckert Papers ledgers** (Huntington): about 5,400 enciphered War Department telegrams, keys in the same papers;
   decipherment phase of "Decoding the Civil War" not reported. Overlaps a Cryptoole draft row (no shelfmark there).
5. **Japanese consular telegrams 1939-40 (BBBTT)**: a codebook system, Weierud's intercepts, probably RG 457.

## Key leads (no ciphertext)

- Greenhow 1864 cipher key, NARA M1091 (above); also a copy at North Carolina State Archives (Rose O'Neal Greenhow
  Papers 1863-64), used by the Rosenbach to read her Beauregard note.
- Same M1091 file: a printed Vigenère tableau ("Section 11 - The Cypher") and a 1864 symbol alphabet sheet.

## Checked and dropped (solved or out of scope)

- Johnston → Lee, 8 Apr 1862 (UNC): dictionary code, read by Davidsch 2017 (Webster 1857); also on cryptiana.
- Confederate envelope cipher (Rockbridge Artillery, Schmeh 2018): simple substitution, read in comments.
- Vicksburg bottle message 1863: read 2010 (Gaddy). Confederate Navy dictionary code, Milroy telegrams, Armstrong,
  D'Estaing 1779 (Clinton Papers), ADFGVX 1918, Köhler 1944, Orpo Doppelkasten: already in the repo.
- Witzke 1918, von Igel papers 1916, Hindu conspiracy: read at the time. Rum-runner traffic (E. S. Friedman):
  no named unsolved message found; Boersma's Cryptologia paper gives solved examples only.
- FBI crypto file 1935-75 (Black Vault): anecdotes, the 1942 Salina note judged meaningless.
- Pulp-magazine, newspaper, POW-postcard and puzzle cryptograms (Friedman dinner party) left out: not archival
  intelligence records. Stechovice notes: post-1950.

## Not reached

- Narváez, *Historia Mexicana* 2025 on Constitutionalist cryptography 1914-15 (PDF 403): may name undeciphered
  Carranza/Villa telegrams in RG 59/165 or the CEHM Carranza archive.
- RG 457 HCC box lists (no online folder list found), RG 165 MID 10,000-series case files, RG 109 "captured
  Confederate cipher messages" item level: need series-filtered catalogue queries (`record.ancestors.naId:`) once
  series naIds are found.
- Richmond newspapers 1864 that printed intercepted Union cipher telegrams asking for solutions (Plum 1882):
  readable now with the Eckert keys if located.
- Huntington blog on the Eckert project returned HTTP 429.
