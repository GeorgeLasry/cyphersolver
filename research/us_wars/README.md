# US wars and intelligence ciphers, literature-and-web sweep (28 Oct 2026)

Part of the Oct 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`), scope widened to the Americas, up to 1950.
Output: `candidates.json` (4 rows, written by `make_candidates.py`). Nothing in catalogue.json, docs/ or git was touched.

## Method

- Read first: the READMEs of `us_friedman`, `us_loc`, `nara_military`, `nara_catalog`, `us_clements` (they already take the
  Clinton/Cornwallis/Rochambeau family, Greenhow, Wharton, Wilkinson, the Madison/Jefferson/Founders cases, Lincoln telegrams,
  Huntington Decoding the Civil War, Manchester 1783, Friedman papers and the NARA record groups).
- WebSearch queries (about 25) on: unsolved Civil War/Confederate ciphers, Revolutionary War Loyalist/Church/Jay/Haldimand/Rumford/Bancroft,
  Knights of the Golden Circle, Mexican-American War (Trist), Van Lew, Booth, WWI German agents (Witzke, Waberski), Hindu-German
  conspiracy, Fenians, Republic of Texas, Latin American independence (Bolivar, Miranda, San Martin, Inconfidencia Mineira).
- The productive source was Klaus Schmeh's Cipherbrain blog (scienceblogs.de), which prints American cryptograms with the
  thread of reader attempts; each post was fetched. Tomokiyo's `cryptiana.web.fc2.com/code/unsolved.htm` was fetched for the
  American entries. `known.py` was run for ~45 names and shelfmarks.
- WebFetch is blocked (403) on media.defense.gov (NSA Revolutionary Secrets 2012), oreilly.com (Masked Dispatches) and gives a
  certificate error on web.lib.unc.edu / blogs.lib.unc.edu (UNC Civil War Day by Day), so those were not read.

## Result: 4 candidates, all low importance

The American war ciphers that can be named have almost all been read or are already in the repo; the web has little left that is
both identifiable and open. Rows: Adventure July 1934 (90 digits, truly open), the Rawlings Confederate cipher cover (partly read in
comments), two Yardley-published cryptograms (partly read). None is viewed on an image.

## Seen and left out (reason)

- Johnston to Lee, 8 Apr 1862 (UNC Civil War Day by Day): Webster dictionary book code, solved in the thread and listed solved on Tomokiyo.
- Barney to Mallory 1863 (CSS Harriet Lane dictionary code): Tomokiyo lists it as solved.
- Mumford to E. P. Alexander, 16 Aug 1861 (captured Bull Run cipher, Alexander Papers, UNC): Alexander's solution is on the back.
- Detective Story Magazine c. 1920 personal-column cipher: solved in the comments; already noted in `research/chi_riverbank`.
- Ohio State Penitentiary 1934 (Marshall Library): Vigenere variant, solved by the War Department in 1934.
- Friedman folding puzzle (Marshall Library): solved in comments, a holiday card.
- Booth's Vigenere table and cipher letter (1865): documented, entered at the trial; the dispute is about use, not reading.
- Knights of the Golden Circle coded letter, 14 Apr 1861, Texas State Library (Hobart Huson Collection): the page carries only a clear transcription, no cipher text.
- Pitman-shorthand letter 1863 (Camp Stoneman, "Smith D."): shorthand, excluded by the brief.
- Waberski, Witzke, Hindu-German conspiracy: all solved by MI-8 or the Friedmans.
- D'Estaing 1779, Armstrong 1808, Milroy telegrams, Macdonald telegrams: in the repo or solved (Tomokiyo list).
- Kansas library cipher in a Hobb novel, Callimahos cryptograms, James Hampton notes (to 1964), Freemason medal 1952: after 1950 or not historical.
- 1932 police-journal cryptogram (Kriminalistische Monats-Hefte, Dresden): German, not American.

## Key leads (bare keys, no ciphertext)

- **Elizabeth Van Lew papers, NYPL MssCol 3135, item "Cipher used by her"** (image on dh.scu.edu/exhibits/items/show/3292):
  her numerical cipher key (a Smithsonian blog says it was found in her watch). Could read any Van Lew/Union Richmond letters;
  the ciphertext side is not located. Not viewed.
- **Texas Papers of the Revolution vol. 4 (Jan-Mar 1836):** a letter describing a cipher (double alphabet, A for Z); mechanics
  only, no ciphertext located (archive.texashistorytrust.org).
- **Nicholas Trist** designed a code for his 1847 dispatches to Buchanan (Masked Dispatches ch. 15; LoC Trist Papers). Unverified
  whether any ciphertext survives undeciphered; worth a look in the LoC finding aid and Masked Dispatches. known.py: no hits.

## Not reached

Masked Dispatches (Weber) and NSA "Revolutionary Secrets" could not be fetched; they are the most likely sources of further
named-but-unread American items (Trist, Dunmore, Haldimand/Vermont negotiations at BL Add MS 21661-21892 / LAC MG 21, Jay's
"puzzling" letters per Mount Vernon). Latin American independence ciphers (Bolivar, Miranda, San Martin, Brazilian conjuracoes):
searches returned nothing; AGI/AGN catalogues were not searched. Fenian, Spanish-American War, Prohibition (us_friedman holds it)
and the Mormon "Anthon transcript" produced no identifiable open ciphertext.
