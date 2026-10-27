# NARA / State Department sweep (27 Oct 2026)

Part of the October 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Slice: FRUS (1861 onward), the
State Department despatch microfilm (RG 59: M30-M46, M37, T-series) and the printed state papers, and the Papers of
the Continental Congress (M247). The Founders Online pass (`research/founders_emlo/`, c. 1775-1830) and the targets
armstrong, erving1807, jqa, murray1801, king1801, mountflorence1801 and graham1806 were taken as already covered.

Output: `candidates.json` (9 rows), built from `rows_1.json` and `rows_2.json` by `add_rows.py`. `frus_search.py`
harvests history.state.gov full-text search into `frus_hits.json` (raw, regenerable); `frus_triage1.txt` is a dump of
the pre-1951 hits.

## Method

- **FRUS.** history.state.gov search works by plain HTTP (`/search?q=<phrase>&within=documents&start=N`, 10 per
  page). The GitHub TEI repository (HistoryAtState/frus, 14 GB) is not code-search indexed, so it was not used.
  Phrases searched, with hit counts: "not deciphered" 2, undeciphered 3, "could not be deciphered" 3, "cannot be
  deciphered" 1, "not been deciphered" 1, "not decoded" 1, "could not be decoded" 2, "not been decoded" 2, "unable to
  decipher" 1, "not decipherable" 2, indecipherable 13, undecipherable 28, "no key" 7, "partly in cipher" 5, "in
  cipher" "not printed" 11, "telegram in cipher" 51, "cypher" "not" 39, "garbled in transmission" 46, "badly
  garbled" 50, "key to the cipher" 3, "cipher key" 1, "code book" 12, "German cipher" 4, "cipher text" 83, "cipher
  message" 36, "code message" 18, "cipher not printed" 1, "follows in cipher" 1, "code groups" 3, "group(s) omitted"
  15; "[cipher]" (1050) and "in cipher" (284) only to 150 hits each. Zero: "undecoded", "cipher text not", "code text
  not", "illegible in code", "key not found", "partly in code", "not yet deciphered", "undecyphered", "lost cipher",
  "remainder in cipher" and similar. Result: FRUS prints decoded telegrams; its "undecipherable"/"garbled" notes are
  transmission faults in 1915-1950 telegrams whose ciphertext is not kept with the file copy. One row kept (German
  cipher telegram passed by Grew, 1916). The 1863 Confederate cipher letter in FRUS 1864 (Seward to Lyons: "some of
  the proper names undecipherable") was checked in Bates, *Lincoln in the Telegraph Office* (1907): read in full by
  Tinker, Bates and Chandler, and the key was captured in Richmond in 1865. Dropped.
- **Weber, *Masked Dispatches* (NSA, 3rd ed. 2013; govinfo PDF).** Text extracted and searched for unread or
  lost-key items. Two rows: Keefer's 1866 intercept of the French Mexico cable, and the 1867-code Vienna cable that
  "was never deciphered". Weber's *United States Diplomatic Codes and Ciphers 1775-1938* (1979) was not available
  (Internet Archive print-disabled loan only), so its lists of unread despatches were not reached.
- **Wharton, *Revolutionary Diplomatic Correspondence* (1889, 6 vols, archive.org djvu text).** 15 bracketed cipher
  notes ("[Here follows a page of cipher to which there is no key]", "key ... not to be found", "Here follow N lines of
  cipher"). Each was checked on Founders Online (Jay, Franklin, Adams Papers): Jay to Huntington 6 Nov 1780,
  Livingston to Jay 1 Nov, 28 Nov and 13 Dec 1781, Livingston to Franklin 5 Sept 1782 are all decoded by the modern
  editions, except one passage of 28 Nov 1781 that the Jay editors call undecipherable (row). Wharton's "no key"
  only means the 1889 editor had none.
- **Letters of Delegates to Congress (25 vols, archive.org text).** Searched for undeciphered/undecoded/no key: the
  hits are illegible handwriting or shorthand (Thomson, Middleton), Lovell passages already decoded by Weber, and
  Dana 1783 (catalogue 485). Nothing new.
- **Founders Online gap check.** The earlier sweep did not search "undecipherable", "indecipherable", "not been
  deciphered", "never deciphered", "cipher key". Searched now through the built-in browser: all handwriting/fading
  cases except Livingston to Jay 28 Nov 1781 (row). Pinckney to Jefferson 24 May 1802 "unidentified code" carries an
  interlinear decipherment.
- **Manning (ed.), *Diplomatic Correspondence ... concerning the Independence of the Latin-American Nations*
  (1925, 3 vols)** and *Inter-American Affairs 1831-1860* vols 1-4 (1932-34; archive.org/DLI texts). These print
  RG 59 despatches with notes on cipher. The 1925 volumes gave five rows: Poinsett 1813 (nine "undeciphered cipher"
  passages), Poinsett's 1811 reports "part in cipher" (from the HSP list filmed on M37 roll 2), Revenga 1822 (no key
  sent), Appleton 1823 (18 groups printed, "no decodification") and Everett 1825 (six lines "without
  decodification"). Inter-American Affairs vols 1-4: every cipher passage noted as deciphered; nothing kept.
- **NARA catalogue.** Proxy JSON (`/proxy/records/search?q=...` with `Accept: application/json`) used only to locate
  the microfilm volumes of the rows (M31 vols 22 and 25, M37 vol. 3). The general NARA keyword harvest is
  `research/nara_catalog/` (another sweep), so it was not repeated here.

## Best leads

1. **Appleton → J. Q. Adams, Cadiz, 6 Aug 1823** (M31 reel 24). 18 code groups printed by Manning; the code is the
   one rebuilt in `targets/jqa` (of = 1576, that = 1384, and = 668), which gives values to 16 of the 18 groups now.
   Solvability 5, a one-session read once the frame is found (frames 150-236 are mostly Cadiz gazettes; the despatch
   frame was not located).
2. **Everett → Clay, Madrid, 25 Sept 1825** (M31 reel 27): six lines of cipher, not decoded in Manning; test the
   same code first.
3. **Poinsett → Monroe, Santiago, 20 Feb 1813** (M37 vol. 3): nine cipher passages, importance 4 (Carrera
   period). The HSP Poinsett Papers vol. 4 hold his own copies and other 1811 reports "part in cipher".
4. **Bazaine/Castelnau → Napoleon III, Mexico, 3 Dec 1866**: 373 groups of a French numeric code copied by
   Sheridan's telegrapher Keefer (Seward Papers reel 98); plaintext published by Girard 1930, so a known-plaintext
   code rebuild.
5. **Revenga → Gual, Madrid 1822**, partly in cipher, intercepted by the French and sent to Washington in 1824 with
   no key (Despatches from Colombia vol. 3).

Lower: the 1867-code Vienna cable (item not located), the German cipher telegram of 5 Dec 1916 (probably read by
Room 40), Livingston → Jay 28 Nov 1781 (one undecipherable passage).

## Key leads (no ciphertext row)

- `targets/jqa/code_table.tsv` (the London/St Petersburg code) was in use at the Madrid legation in 1823: worth
  running over all coded passages of M31 vols 20-25 (Forsyth, Nelson, Appleton, Everett).
- FRUS 1912 doc. 1419: a Guatemalan/Nicaraguan revolutionary **cipher key** (Gámez to Estrada Cabrera, with
  letters by M. Antonia Zaldívar), copied by the US legation in San Salvador, Jan 1912 (decimal file 817.00/1759).
- The 1867 State Department code and Haswell's 1876 Red Code are printed in Weber 1979.

## Dead ends

- Confederate cipher letters of 18 and 22 Dec 1863 (FRUS 1864 doc. 257): read at the time; key found 1865.
- Wharton's "no key" passages (Jay 1780, Livingston 1781-82): decoded in the Jay and Franklin Papers.
- FRUS 1890 doc. 389, 1906 doc. 319, 1931-1950 "undeciphered groups": transmission faults; no ciphertext.
- Rush → Adams, London, 20 July 1820 (Manning doc. 778): Forsyth's cipher letter to Rush was partly unreadable to
  Rush; that letter is in Rush's papers (Princeton), not RG 59. Not pursued.
- Livingston → Lafayette 2 Nov 1782 and Livingston → Dana 18 Sept 1782 (Wharton "lines of cipher"): not on Founders;
  Livingston's drafts at NHi normally carry the plaintext, so not kept. Unchecked.

## Not reached / blockers

- Weber 1979 (the inventory of State Department codes and of despatches left undecoded) is not online.
- HathiTrust full-text search and vanburenpapers.org sit behind a Cloudflare bot check (not bypassed), so Manning's
  later Inter-American volumes (5-12), the Canadian Relations volumes and the Van Buren Papers were not searched.
- The FRUS TEI bulk repository was not downloaded (14 GB); the site search covers the same text.
- Papers of the Continental Congress (M247) were reached only through the editions; no PCC frames viewed.
- Founders Online needs the browser (WAF); only the gap phrases above were run.
- Frames for the Appleton and Poinsett letters were not located on the microfilm.
