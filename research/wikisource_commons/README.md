# Wikisource / Wikimedia Commons / Gutenberg sweep (28 Oct 2026)

Result: `candidates.json`, 5 rows (cls C 4, B 1; all `seen: catalogue`). This source is thin: Wikisource and Gutenberg
carry almost no primary cipher texts, and Commons holds a handful of images with the right description.

## Method and counts
- `harvest.py`: MediaWiki search (`list=search`) on en/fr/de/it/es/nl/la Wikisource, main and Page/Seite/Pagina
  namespaces, ~75 phrase queries ("in cipher", "en chiffre", "in Chiffren", "in cifra", "cijferschrift", "litterae cifratae" ...):
  3,750 raw hits, 3,446 distinct pages (`raw_wikisource.jsonl`).
- `regex_harvest.py`: CirrusSearch `insource:/regex/` works on Wikisource. cipher-word AND a run of 7+ numbers: 591 pages (`raw_regex.jsonl`).
- `targeted.py`: cipher word AND a series name (Notes and Queries, Archaeologia, Camden Society, Calendar of, Bibliothèque de l'École des chartes, ...): ~10,500 hits.
- `fetch_pages.py` downloaded wikitext of ~9,000 pages (<=80 kB; `.work/`, git-ignored); `analyze_pages.py` kept pages with a cipher word within
  ~500 characters of a 8+ number run: 229 pages, hand reviewed (`page_hits.json`). Nearly all noise: "chiffre rond", Loyd puzzle book,
  Strand/detective fiction, encyclopaedias, indexes. Symbol-string ciphers cannot be detected this way.
- `commons.py` / `commons_meta.py`: 146 cryptography categories (depth 2) = 3,734 files, plus 28 file-description searches (6,698 titles);
  3,717 file descriptions fetched (`commons_meta.json`), 107 manuscript/letter-like rows reviewed (`commons_review.txt`).
- `gutenberg.py`/`gut_dl.py`/`gut_grep.py`: Gutendex was unreliable; used `pg_catalog.csv` instead (1,022 state-paper, letters, diplomacy titles; ~500
  downloaded when stopped, no printed figure-string cipher found). Gutenberg holds no Calendar of State Papers volumes.

## Kept (5)
Barlow 1807 (Cleveland PL, 26 images), Desvalls 1714 (AHCB), Ostermann 1737 (Astrakhan), Alexis I tarabarshchina (Kutepov 1898),
Aramon letter at Ecouen with partial decipherment. Best: Barlow 1807, Desvalls 1714, Aramon.

## Excluded (already solved or in repo)
- Wikisource N&Q: Sir Ralph Verney's cipher (N&Q 5 S xi 210, 1879): key printed in the same reply (28 numerals) = solved. Skelton's cipher, Urquhart's Cyphral Distich (N&Q 9 S iii 134): solved (Urquhart is in this repo).
- Commons: Rákóczi-era, Rudolf II/Pezzen 1597, Ferdinand I 1548 and Balassi/Kemény/Károlyi/Pongrácz/Jablonski letters (all scans from Szilas' book on Rákóczi-era
  ciphers, with decipherments); Cortés 1532 (published 1925); Charles V → Saint-Mauris 1547 (cryptiana: solved); Napoleon III 1859 dispatches (repo `eugenie1859`);
  Greenhow 1861, Arnold 1779, Culper, Walker → Pemberton 1863 (famous or known families); Golden Dawn cipher manuscripts; modern items.

## Key / thin leads (not rows)
- N&Q 12 S i 332 (22 Apr 1910): "A cipher of names" used by James II and his party in the Irish War 1689-91, from autograph letters to Sir Robert Southwell. Bare key; could read Jacobite letters in Southwell papers.
- N&Q 10 S ii 347, 411 (1904): "Monmouth cipher" (the Duke's cipher, query by Rev. J. Willcock). No document identified; Pepys 1666: Sandwich's long cipher letter to Carteret (not printed).
- Commons "Sophia letters to Golitsyn" file was in the category list but its description was not fetched.

## Blockers
Wikisource search matches words not digit patterns unless via `insource:` regex (slow, capped); gutendex timed out; no full-text search exists at Gutenberg.
Commons images were not viewed. Not reached: Wikisource Russian/Polish/Czech/Swedish, other-language N&Q equivalents (Intermédiaire des chercheurs not on Wikisource).
