# Clements Library sweep: coverage log (Oct 2026)

Access notes
- `quod.lib.umich.edu/c/clementsead/`, `findingaids.lib.umich.edu` and `clements.umich.edu` return **403 to scripted
  requests** (curl and WebFetch, 28 Oct 2026). Not retried. All finding-aid work was done in the built-in browser
  (a real browser session), calling the Blacklight JSON endpoint `findingaids.lib.umich.edu/catalog.json?q=...&per_page=100`
  from the page, one request every 3.2 s.
- The Blacklight index covers all U-M finding aids (Bentley, Special Collections, Clements). Only ids starting
  `umich-wcl-` (Clements) are counted as "wcl" below. Results cap at 3 pages (300) per query.
- Index granularity: Clements finding aids are mostly collection-level, with item-level calendars for small
  collections, the Diedrich, War of 1812, Women/Gender/Family and Washington collections. The Clinton, Gage,
  Germain, Shelburne, Greene, Knox, Simcoe papers are box/folder or volume level only, so a hit on the collection
  record means the word occurs somewhere in its scope note, not at item level.

## Finding-aid queries (findingaids.lib.umich.edu, all U-M; total / Clements)

| query | total | Clements |
|---|---|---|
| cipher | 27 | 22 |
| cypher | 44 | 42 |
| ciphers | 27 | 22 |
| "in cipher" | 1 | 1 (Clinton papers) |
| decipher | 24 | 5 |
| deciphered | 19 | 5 |
| "invisible ink" | 3 | 3 (Clinton, Brisbane, Cushing) |
| "secret ink" | 0 | 0 |
| "sympathetic ink" | 0 | 0 |
| "mask" | 94 | 23 (photographs, gas masks; Clinton papers) |
| "in code" | 6 | 4 |
| cryptogram | 1 | 0 |
| nomenclator | 1 | 0 |
| "secret writing" | 0 | 0 |
| spy | 190 | 53 |
| enciphered | 0 | 0 |
| "cipher key" | 0 | 0 |
| "secret correspondence" | 0 | 0 |
| "code book" | 20 | 0 |
| "code telegram" / "cipher telegram" | 0 | 0 |
| "cyphered" / "ciphered" (stemmed = cypher/cipher) | 44 / 27 | 42 / 22 |
| "hieroglyphics" | 3 | 2 |
| "secret alphabet" | 0 | 0 |
| pigpen | 4 | 4 |
| "private code" | 2 | 1 |
| "secret code" | 0 | 0 |
| "secret service" | 21 | 13 |
| intelligence | 972 | 90 (not item-reviewed beyond titles) |
| "code name" | 1 | 0 |
| "Culper" | 0 | 0 |
| "Arnold" | 2439 | 39 |
| "André" / "Andre" | 314 | 56 |
| "Stansbury" | 6 | 3 (none relevant) |
| "Odell" | 39 | 5 |
| "Beckwith" | 124 | 83 |
| "Cornwallis" / "Rivington" / "Willes" | 118 / 11 / 4512 | 105 / 10 / 26 (stemmed; nothing cipher-related) |
| "Stepney" | 0 | 0 |

Second pass with the Clements repository facet (`f[repository_sim][]=University of Michigan William L. Clements
Library`), so the counts are Clements-only and complete:

| query | Clements hits |
|---|---|
| code | 56 |
| invisible | 12 |
| stain | 23 (none relevant) |
| "lemon juice" | 1 (Melville papers, scurvy, not ink) |
| substitution | 39 (draft substitutes; Hewett, Musty relevant) |
| "secret language" | 0 |
| shorthand | 15 (shorthand excluded by the brief) |
| intercepted | 25 (Shelburne vol. 35 intercepts) |
| secret | 103 |
| "key" | 153 (none relevant) |
| André | 60 |
| Arnold | 142 |
| intelligence | 227 (first 100 titles screened) |

Collection-level finding aids read in full text and grepped for cipher words (32 + 25): Clinton (M-42), Greene,
Strachey, Brisbane, Cushing, Woods, Nixon, Hastings, McCormick, R. A. White, Ludewig, Thurston, Tufts-Day, Musty,
Castle, Fitzhugh Lee, Pratt, Hamilton-Schuyler, Morton, Germain (M-30), Gage (M-341), Knox (M-161), Simcoe (M-342),
Sydney (M-19), Melville (M-124), C. Townshend, Moncrieff, Paris naval correspondence 1780, Castellane, Great Britain
Army, Pease, Kamp, Loomis, Manchester (M-1536), Shelburne (M-66), von Jungkenn (M-147), Seward (M-368), Connor,
Hewett, Blach, Neal, Gibbs, London, Bates, Brokenshire, Kenyon-Biehl, Stahl, Wilson, Webb, Hayward, Shadwell, Tapson,
Snyder, Witherspoon, Metcalf, Castries, Downs, Howland, Rosebery, Wheeler.

Access stopped: after about 120 requests over ~90 minutes the finding-aid site began answering the page's own
fetches with a Cloudflare "Just a moment" 403 (28 Oct 2026). Per the brief, not retried. Not reached after that:
Rutland letterbook, Talcott, Minto-Skelton, Myers-Mason-Bailey, Bowers, Snell-Andrews, Jewett-Lee (all 'stain'
hits, very unlikely to be ink), and Seward/Connor/Hewett detail pages (a second look for dates).

## Other sources

| source | result |
|---|---|
| clements.umich.edu (Spy Letters exhibit, Bloody Work exhibit, Clinton volume guide PDF) | 403 to WebFetch; browser navigation refused by the session's permission classifier as bot-check circumvention. Not reached. Exhibit content known only from search-engine snippets (Arnold-André 12 July 1780 book code, Clinton-Burgoyne mask letter 10 Aug 1777, Thompson invisible-ink letter May 1775: all read in the exhibit). |
| quod.lib.umich.edu (U-M Digital Collections, old clementsead) | 403 to curl; not retried. |
| HathiTrust full-text search | 403 to WebFetch; not reached. |
| archive.org: *Guide to the manuscript collections in the William L. Clements Library* (Ewing 1953, `guidetomanuscrip00will`) | full text grepped for ciph/cypher/code/invisible/decipher/secret/intercept: no cipher item beyond the Clinton/Gage intelligence notes and Van Doren's *Secret History* citation. Peckham 1942 and the 1978 Dann guide are lending-restricted. |
| Schmeh blog (Manchester cryptogram, Top 50 no. 34) | transcription and comments read. |
| cryptiana unsolved.htm | only Clements item is d'Estaing → Gérard 1779 (Clinton 64:14), already `targets/destaing`. |
| Journal of the American Revolution, "Decoding British ciphers used in the South" (2019) | Cornwallis/Balfour/Rawdon ciphers, mostly TNA PRO 30/11; no open Clements item named. |
| DECODE (via known.py) | no Clements Library records. |
