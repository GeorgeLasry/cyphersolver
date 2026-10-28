# LoC sweep coverage log (Oct 2026)

Every query run against loc.gov, with hit counts, so the coverage can be audited. Raw JSON responses are cached
in `raw/` (git-ignored). Counts are `pagination.of` from the loc.gov JSON API at the time of the query
(27-28 Oct 2026).

## Endpoints

- `https://www.loc.gov/manuscripts/?q=<term>&fo=json&c=100&sp=N`: all item records with original format
  "manuscript/mixed material" (Manuscript Division, plus manuscript items held by other divisions). The search
  is over the catalogue record **and** the full text of transcriptions (By the People crowd transcriptions,
  the Lincoln Studies Center transcriptions, ADST oral-history texts). It does **not** reach the page text of
  digitised collections that have no transcription (e.g. most of the Grant, Sherman, Sheridan, Stanton papers),
  nor container lists inside finding aids.
- `https://www.loc.gov/item/<id>/?fo=json` then the `tile.loc.gov/.../*.txt` transcription files: context for
  full-text hits (`ctx.py`).
- `https://findingaids.loc.gov/search?q=cipher`: **403 to a scripted request (not retried)**.

## Global /manuscripts/ queries (harvest.py)


### Term counts (`counts.py`, c=1 probes; loc.gov stems and ignores quotes, so "ciphered"/"ciphers"/"in cipher" = "cipher")

| term | hits | harvested in full |
|---|---|---|
| cipher | 1085 | yes |
| cypher | 201 | yes |
| ciphered | 1085 | yes |
| cyphered | 201 | same set as stem |
| ciphers | 1085 | same set as stem |
| cyphers | 201 | same set as stem |
| decipher | 351 | yes |
| deciphered | 351 | same set as stem |
| decypher | 11 | yes |
| decyphered | 8 | yes |
| undeciphered | 2 | yes |
| "in cipher" | 1085 | same set as stem |
| "in cypher" | 201 | same set as stem |
| "in code" | 7129 | no (too broad: generic "code"/"encoded") |
| cryptogram | 23 | yes |
| cryptograph | 3 | yes |
| cryptography | 105 | yes |
| "secret writing" | 4 | yes |
| "invisible ink" | 18 | yes |
| "sympathetic ink" | 1 | yes |
| nomenclator | 0 | no |
| chiffre | 20 | yes |
| chiffres | 20 | no |
| cifra | 14 | yes |
| cifrado | 0 | no |
| geheimschrift | 0 | no |
| "code telegram" | 5 | yes |
| "cipher telegram" | 25 | yes |
| "cipher key" | 4 | yes |
| "code book" | 100 | yes |
| "cipher book" | 4 | yes |
| decoded | 173 | yes |
| decode | 173 | same set as stem |
| encoded | 1438 | no (too broad: generic "code"/"encoded") |
| steganography | 0 | no |
| "secret code" | 42 | yes |
| "telegraph code" | 3 | yes |
| "private code" | 10 | yes |
| "cipher dispatch" | 5 | yes |
| "cipher despatch" | 8 | yes |
| "key to the cipher" | 4 | yes |

Distinct items harvested: **1948** (`hits.json`); transcription context fetched for **342** full-text hits (`context.json`).

### Harvested hits by collection

| collection | hits |
|---|---|
| Abraham Lincoln Papers at the Library of Congress | 347 |
| Theodore Roosevelt papers | 182 |
| The James Madison Papers at the Library of Congress | 176 |
| The Foreign Affairs Oral History Collection of the Association for Diplomatic Studies and Training | 164 |
| Motion picture copyright descriptions collection | 129 |
| The Thomas Jefferson Papers at the Library of Congress | 112 |
| Alan Lomax collection (AFC 2004/004) | 73 |
| Walt Whitman papers in the Charles E. Feinberg collection | 69 |
| Blackwell family papers | 61 |
| american folklife center | 56 |
| Alexander Graham Bell family papers, 1834-1974. | 53 |
| National American Woman Suffrage Association records | 52 |
| George Washington papers | 50 |
| veterans history project collection | 49 |
| NAACP Legal Defense and Educational Fund Records | 36 |
| Anna E. Dickinson papers | 32 |
| Mary Church Terrell papers | 30 |
| AIDS Memorial Quilt Records (AFC 2019/048) | 29 |
| Joseph Holt papers, 1797-1917 | 27 |
| Leonard Bernstein collection, circa 1900-1995 | 16 |
| Bess Lomax Hawes collection (AFC 2014/008) | 14 |
| Frederick Douglass Papers | 12 |
| Louis Malesherbes Goldsborough Papers | 10 |
| catalog | 10 |
| Radio Research Project manuscript collection, 1940-1942 | 10 |
| Thomas Biggs Harned collection of Walt Whitman papers | 9 |
| Andrew Jackson papers, 1775-1874 | 7 |
| Carrie Chapman Catt papers | 7 |
| John A. Lomax and Alan Lomax papers (AFC 1933/001) | 7 |
| defense pow/mia accounting agency | 7 |
| U.S. Work Projects Administration, Federal Writers' Project | 6 |
| Federal Writer's Project, United States Work Projects Administration (USWPA) | 6 |
| rare book and special collections division | 6 |
| Booker T. Washington papers. | 5 |
| William A. Gladstone Afro-American Military Collection | 5 |
| James A. Garfield papers | 5 |
| finding aids | 5 |
| American Federation of Labor records | 5 |
| Forms part of: W.P.A. California Folk Music Project collection | 4 |
| manuscript division | 4 |
| Mary Ann Bickerdyke Papers | 4 |
| Frederick Law Olmsted papers | 4 |
| Farm Security Administration - Office of War Information photograph collection (Library of Congress) | 4 |
| digital collections | 3 |
| Walt Whitman papers | 3 |
| The Seth MacFarlane Collection of the Carl Sagan and Ann Druyan Archive | 3 |
| navajo code talkers | 3 |
| George Brinton McClellan papers | 2 |
| Elizabeth Cady Stanton papers | 2 |
| Wm. Oland Bourne papers | 2 |
| omar ibn said collection | 2 |
| George S. Patton Papers | 2 |
| James Madison Papers | 1 |
| Herndon-Weik Collection of Lincolniana | 1 |
| selections of arabic, persian, and ottoman calligraphy | 1 |
| The Alfred Whital Stern Collection of Lincolniana | 1 |
| Everett Sanders papers. | 1 |
| Miller NAWSA Suffrage Scrapbooks, 1897-1911 | 1 |
| Woodrow Wilson papers | 1 |
| Branch Rickey papers | 1 |
| The Diary of Horatio Nelson Taft, 1861-1865 | 1 |
| lessing j. rosenwald collection | 1 |
| Joel T. Boone papers. | 1 |
| John and Ruby Lomax 1939 Southern States Recording Trip (AFC 1939/001) | 1 |
| the borinqueneers: a puerto rican regiment | 1 |
| george brinton mcclellan papers | 1 |
| african americans at war: pioneers | 1 |
| Charles L. Todd and Robert Sonkin Migrant Workers Collection (AFC 1985/001) | 1 |
| Maine Acadian Cultural Survey collection (AFC 1991/029) | 1 |
| Colorado Folklife Project collection (AFC 1991/031) | 1 |
| Pinelands Folklife Project collection (AFC 1991/023) | 1 |
| Harry A. Blackmun Papers | 1 |
| line by line: transcribed correspondence collections | 1 |
| this we'll defend: the u.s. army | 1 |
| Center for Applied Linguistics Collection (AFC 1986/022) | 1 |
| military intel: in harm's way | 1 |
| battle of the bulge | 1 |
| music division | 1 |
| Jean Lafitte National Historical Park and Preserve collection (AFC 1985/022) | 1 |

## Per-collection queries (`loc_collections.py`; /collections/<slug>/?q=term)

223 digital collections with manuscript material were listed; 116 relevant ones (papers, records, diplomatic, Hispanic/French/Dutch/Russian, World Digital Library) were queried for cipher / cypher / decipher. Folklife, music, dance, oral-history, motion-picture and non-European script collections were skipped.

| collection | cipher | cypher | decipher |
|---|---|---|---|
| Abraham Lincoln Papers at the Library of Congress | 329 | 13 | 8 |
| American Federation of Labor Records | 0 | 0 | 5 |
| Andrew Jackson Papers | 2 | 1 | 3 |
| Anna E. Dickinson Papers | 16 | 6 | 9 |
| Blackwell Family Papers | 21 | 7 | 23 |
| Blair Family Papers | 0 | 0 | 1 |
| Branch Rickey Papers | 0 | 1 | 0 |
| Carrie Chapman Catt Papers | 4 | 0 | 3 |
| Celebrating CHamoru Nobenas | 0 | 0 | 1 |
| Elizabeth Cady Stanton Papers | 1 | 1 | 0 |
| France in America | 11 | 11 | 7 |
| Frederick Douglass Papers at the Library of Congress | 5 | 1 | 5 |
| Frederick Law Olmsted Papers | 1 | 2 | 1 |
| George Brinton McClellan Papers | 2 | 0 | 1 |
| George Washington Papers | 22 | 21 | 10 |
| Herndon-Weik Collection of Lincolniana | 1 | 2 | 0 |
| James A. Garfield Papers | 5 | 1 | 1 |
| James Madison Papers, 1723-1859 | 162 | 40 | 4 |
| Joseph Holt Papers | 17 | 4 | 5 |
| Lessing J. Rosenwald Collection | 74 | 124 | 80 |
| Louis Malesherbes Goldsborough Papers | 3 | 1 | 4 |
| Mary Ann Bickerdyke Papers | 3 | 0 | 1 |
| Mary Church Terrell Papers | 16 | 2 | 9 |
| Meeting of Frontiers | 6 | 1 | 10 |
| Montgomery C. Meigs Papers | 0 | 0 | 1 |
| NAACP Legal Defense and Educational Fund Records | 8 | 15 | 8 |
| National American Woman Suffrage Association Records | 32 | 3 | 13 |
| Omar Ibn Said Collection | 0 | 0 | 2 |
| The Atlantic World: America and the Netherlands | 1 | 0 | 1 |
| Theodore Roosevelt Papers | 143 | 18 | 57 |
| Thomas Jefferson Papers, 1606-1827 | 63 | 44 | 0 |
| Washington During the Civil War: The Diary of Horatio Nelson Taft, 1861-1865 | 0 | 1 | 0 |
| William A. Gladstone Afro-American Military Collection | 3 | 2 | 0 |
| Wm. Oland Bourne Papers | 1 | 0 | 1 |
| Woodrow Wilson Papers | 1 | 0 | 0 |
| World Digital Library | 54 | 62 | 88 |

Zero hits for all three terms (80): Alexander Hamilton Papers; Alexander Hamilton Stephens Papers; American Colony in Jerusalem, 1870-2006; Andrew Johnson Papers; Anna Maria Brodeau Thornton Papers; Associated Press News Dispatches, 1915-1930; Benajah Jay Antrim Journals; Benjamin Franklin Papers; Benjamin Harrison Papers; Betty Herndon Maury Maury Papers; Bronislava Nijinska Collection; Calvin Coolidge Papers; Charles S. Hamlin Papers; Charles Wellington Reed Papers, 1776 to 1926; Charles William Le Gendre Papers; Chester Alan Arthur Papers; Christian A. Fleetwood Papers; Clara Barton Papers; Confederate States of America Records; Donald Benham Civil War Collection; E. B. Washburne Papers; Edwin McMasters Stanton Papers, 1818-1921; Eltaher Collection; Eugene Meyer Papers; Franklin Pierce Papers; Freedom's Fortress: The Library of Congress, 1939-1953; George S. Patton Papers: Diaries, 1910-1945; Gideon Welles Papers; Grover Cleveland Papers; Hans Peter Kraus Collection of Spanish American Documents, 1433-1877; Henry Rowe Schoolcraft Papers; Horace Greeley Papers; Horace H. Lurton Papers; James Buchanan and Harriet Lane Johnston Papers; James K. Polk Papers; James Monroe Papers; Jean Lafitte National Historical Park and Preserve Collection; Jedediah Hotchkiss Papers; John Carvel Arnold Papers; John G. Nicolay Papers; John J. Pershing Papers; John Tyler Papers; Jubal Anderson Early Papers; Lewis H. Machen Family Papers; Margaret Bayard Smith Papers; Martin Van Buren Papers, 1787 to 1910; Matthew Fontaine Maury Papers; Millard Fillmore Papers; Miscellaneous Manuscripts Collection; Myrtilla Miner Papers; Nathan W. Daniels Diary and Scrapbook; Nelson W. Aldrich Papers; Olmsted Associates Records; Pacific Encounters in Nineteenth-Century Japan; Parallel Histories: Spain, the United States, and the American Frontier; Philip Henry Sheridan Papers; Phillips/Mathée Collection; Polish Declarations of Admiration and Friendship for the United States, 1926; Robert H. Terrell Papers; Robert Lansing Papers; Salmon P. Chase Papers; Samuel J. Gibson Diary and Correspondence; Shippen Family Papers; Spanish Legal Documents (15th-19th Centuries); Susan B. Anthony Papers; Thaddeus Stevens Papers; The Heineman Foundation Collection; The United States and Brazil: Expanding Frontiers, Comparing Cultures; Ulysses S. Grant Papers; Vietnam-Era Prisoner-of-War/Missing-in-Action Database; Warren G. Harding-Carrie Fulton Phillips Correspondence; William Alexander Marshall Papers; William Farquhar Correspondence; William H. Taft Papers; William Henry Harrison Papers; William McKinley Papers; William Speiden Journals; William T. Sherman Papers; Yudin Collection of Russian-American Company Records, 1783-1946; Zachary Taylor Papers.

Zero usually means *no item-level text*, not *no cipher*: Hamilton, Franklin, Monroe, Polk, Grant, Sherman,
Sheridan, Stanton, Pershing, Andrew Johnson, the Confederate States of America Records (Pickett Papers) and others are
digitised as folder images without transcriptions, so keyword search cannot see ciphertext in them.

## Other routes

- `coll_hits.py`: hit lists for World Digital Library, Rosenwald, France in America, Meeting of Frontiers, Atlantic
  World (Netherlands): all hits are printed books/maps except the Greenhow cipher letter (already `targets/greenhow1861`).
- Finding aids: `findingaids.loc.gov` search and its PDF path returned **403** to scripted requests (not retried); the
  built-in-browser route was refused by the session's safety classifier. The old `tile.loc.gov/.../gdcfindingaidpdfs/`
  PDFs return 404. **Container lists were therefore not searched.**
- Theodore Roosevelt Center (Dickinson State, LoC TR Papers images): subject pages "Ciphers" (15) and "Cipher and
  telegraph codes" (18) read item by item.
- Founders Online: blocked by its WAF for WebFetch; relied on `research/founders_emlo/founders_hits.tsv`.

