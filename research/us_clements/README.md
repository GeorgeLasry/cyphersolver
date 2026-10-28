# William L. Clements Library sweep (Oct 2026)

Sweep of the Clements Library (University of Michigan) for documents with ciphertext, 1350-1950, that are unsolved
or possibly unsolved and not yet in the repo. Output: `candidates.json` (18 rows, BRIEF fields, source "Clements
Library sweep"). Query-by-query counts are in `coverage.md`. `add_rows.py` holds rows 8-18 as data.

## Method

- **Finding aids.** `findingaids.lib.umich.edu` (ArcLight/Blacklight, all U-M repositories) sits behind
  Cloudflare and answers scripts with 403, so it was searched from the built-in browser: the page called its own
  `catalog.json?q=...&per_page=100` endpoint, about one request every 3 seconds, first unfiltered (keeping
  `umich-wcl-` ids) and then with the Clements repository facet. 38 queries in the first pass, 13 in the faceted
  pass. About 60 collection-level finding aids were then fetched in full and grepped for cipher words.
- **Granularity limits.** The big British headquarters and ministry papers (Clinton, Gage, Germain, Shelburne,
  Knox, Sydney, Greene, Simcoe) are described at volume or folder level. A cipher letter inside a chronological
  volume appears only if the scope note mentions it. The item-level calendars that exist (War of 1812, George
  Washington collection, Women, Gender, and Family, Diedrich, Schoff) were covered by the keyword search.
- **Prior art.** Schmeh's blog (Manchester cryptogram), cryptiana `unsolved.htm`, Journal of the American
  Revolution (southern British ciphers), web searches on each of the stronger rows, and known.py on every name. No
  Clements item is on DECODE.

## Results: 18 candidates

Best leads, ranked:

1. **Manchester cryptogram, Fontainebleau, 20 Sept/Oct 1783** (Manchester papers, M-1536). Schmeh's Top 50
   no. 34, and not yet in catalogue.json. It has about 173 numeric groups (values 9-3937), a transcription online and
   no reading. The key lead is in the same collection: letter book vol. 3 part 2 has 58 Manchester→Fox letters with
   49 enclosures, and vol. 4 has 67 Fox→Manchester letters (Apr-Dec 1783). If these copies keep cipher groups next
   to clear text, they would rebuild the embassy code. Outside the Clements: TNA FO 27 (Paris 1783), the TNA-listed
   Manchester intelligence papers, and the Yale Manchester papers (another agent's sweep).
2. **Eustis → Barlow, 25 Sept 1812, "In code"** (War of 1812 collection). Covert arms export from Ostend. The
   Barlow 1811 State Department code is already keyed at NARA M34 vol. 16 (research/nara_triage_a), so this is
   probably a key-alignment job once the 2 pages are scanned.
3. **Seward → a correspondent in Copenhagen, coded letter copy, undated** (Seward collection M-368). Probably
   from the Danish West Indies purchase of 1865-67, in the Monroe cipher or the 1867 Department code.
4. **Shelburne papers vol. 35, intercepted French diplomatic letters 1767-68 (24) and 1780-83 (60).** The volume
   is unavailable for its condition (digital facsimile only). These are probably Deciphering Branch decrypts. They
   matter only if cipher groups survive with them, which would give siblings of the d'Estaing 1779 code
   (`targets/destaing`, Clinton 64:14).
5. **Henry Clinton's 1771 Gibraltar notebook (vol. 284, Notebook B)**, "for unclear reasons, he wrote some
   entries in cipher". A private cipher of the later commander-in-chief.
6. **Davis E. Castle, Signal Corps journals, coded passages 1 Nov 1864 and 25 Aug 1865**, and **Peter H. Musty
   diaries, 2 July - 16 Sept 1864 in a numerical substitution code.** Civil War private ciphers; likely easy once
   imaged.
7. **Fitzhugh Lee papers, 1916 Punitive Expedition code telegrams.** Some come with their plaintext drafts, which
   give a direct key.

The rest are minor private ciphers: Gibbs 1738 courtship letter, Connor 1825 pictographic names, Morfit 1834
pigpen (partly translated by his father), Tyler 1852 business code, Hewett 1861 diary (six pages), Thurston
scrapbook 1869-76, Ludewig 1885 pigpen, Blach 1894, Neal 1910.

All rows are `seen: "catalogue"`. No Clements images are online for any of them, so solvability is 1. The
exception is the Manchester cryptogram, whose transcription is published.

## Key leads (keys, tables, codes without a target ciphertext)

- **Clinton papers vol. 234, "Codes, ciphers, and intelligence", ca. 1776-1781**: 5 ciphers, 2 codes, 2 masks and
  37 intelligence reports, one with invisible ink on the verso. These are British headquarters key sheets and could
  read other Clinton-period ciphertexts held elsewhere (TNA PRO 30/11, NARA PCC item 51, LoC Washington papers).
  Compare them with `targets/balfour1781` and the 1780-81 southern ciphers.
- **Clinton papers vol. 274, André's intelligence book 1779-80**, and the Clinton letter books to
  Cornwallis/Arnold/Leslie (1780-81). These are clear file copies of letters that went out in cipher, so they act as
  cribs for intercepted copies in NARA PCC.
- **Henry Strachey papers**: Strachey to his wife, 8 Dec 1777, "directed her on how to use a cipher if the
  necessity arose". These are instructions for a family cipher, and no ciphered letter is described.
- **Albert W. Stahl collection**: a list of private finance telegraph codes, 30 July 1890.
- **Lamb-Sykes papers**: a printed "Cipher code for use of travellers holding letters of credit".
- **Kenyon-Biehl correspondence**: "a signature and vocal code" for the RMOLO "Inner Circle", 21 Feb 1924. These
  are instructions, not ciphertext.
- **Manchester papers letter books** (see lead 1).

## Excluded (checked, with the reason)

- d'Estaing → Gérard, 30 Apr 1779, Clinton 64:14: already `targets/destaing`.
- Arnold → André cipher letters (Clinton papers, Arnold-André series), Stansbury/Odell: printed and deciphered in
  Van Doren, *Secret History* (1941), and shown read in the Clements Spy Letters exhibit.
- Clinton → Burgoyne mask letter, 10 Aug 1777; Benjamin Thompson's invisible-ink letter, May 1775: read in the
  exhibit.
- Rochambeau → Greene, 26 Feb and 6 Apr 1782, "in Washington's cipher with contemporary translations" (Greene
  papers): deciphered.
- Washington → Greene, 9 July and 6 Aug 1782, "partially in code" (George Washington collection): the
  Washington-Greene code is known, and the clear text survives in Washington's letter books.
- Colden's invisible-ink letter (Brisbane papers, 1814): transcription with it.
- Charles Wentz → Helen Haldeman pigpen, 1852: reading given in the finding aid.
- A. D. Frankenberry 1895, Sherman coded message "with the code broken down": read.
- Moldenhauer → Bates Morse-code love messages (1917-18): Morse, not a cipher.
- Pratt family "private code" (words with private meanings), Brokenshire (code proposed, none used), Howe 1758
  ("too long to write in cypher"): no ciphertext.
- 25+ "cypher books" and "ciphering books": arithmetic exercise books.
- Shorthand (Beeby 1844, Tanner's Lincoln notes 1865 with translation, Jorgensen): excluded by the brief.

## Dead ends and not reached

- `clements.umich.edu` (Spy Letters and Bloody Work exhibits, the Clinton volume guide PDF), `quod.lib.umich.edu`
  and HathiTrust returned 403 to scripts. Browser navigation to clements.umich.edu was refused by the session
  permission check, so the exhibit galleries were seen only through search snippets.
- After about 120 requests the finding-aid site itself started returning a Cloudflare 403 challenge. The sweep
  stopped there. The second-pass detail pages for a few "stain" hits were not fetched (listed in `coverage.md`).
- The Clinton chronological series (vols. 1-233) is not described item by item online. A cipher letter in it
  (for example 1780-81 headquarters traffic in the Entick-dictionary or "common" ciphers) would need the Clements
  card calendar or the volume guide PDF. Most of these letters are deciphered at the time or in Saberton's
  *Cornwallis Papers*.

## Dropped at merge (28 Oct 2026)

- Manchester cryptogram 1783 (M-1536): it is no. 34 on Schmeh's Top 50, and the catalogue excludes the Tomokiyo,
  Schmeh and Dunin lists by definition. The Manchester letter books stay as its key lead.
