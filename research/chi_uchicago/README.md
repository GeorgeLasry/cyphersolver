# University of Chicago Library, Hanna Holborn Gray SCRC: cipher sweep (28 Oct 2026)

**Result: 2 candidates, both weak (importance 1-2, description-level only). The Durrett Collection holds no described cipher material.**

## Method

1. The usual routes are bot-walled: `www.lib.uchicago.edu/e/scrc/findingaids/` returns 403, the `/scrc/?q=` search redirects to a Cloudflare Turnstile page, `catalog.lib.uchicago.edu` serves an Anubis proof-of-work page, ArchiveGrid returns a Cloudflare "Just a moment" page. Per the brief these were not worked around (the built-in browser reached the Turnstile page and stopped there).
2. Open route found: `https://www.lib.uchicago.edu/ead/rlg/` is a plain Apache directory listing of every SCRC EAD finding aid (2,025 `.xml`, 1,986 `.pdf`). `fetch_ead.py` fetched all XML at 3 s intervals (about 100 min, priority: Durrett, Douglas, Barton/Lincoln, Manly, codices/MS, Italian/French first); `grep_ead.py` greps the full text and writes `ead_hits.json`. Details and every query are in `coverage.md`.
3. Hits were read by hand and checked with `known.py` (Sisson, Leadbeater, Wilkinson, Gardoqui, Innes, Sebastian, Manly).

Counts: 2,024 finding aids read; 215 raw term hits in 56 files; 2 rows kept.

## Candidates (candidates.json)

1. Harper Papers Box 61 f.19, "Memoranda on translations and code messages found with the Sisson documents (1918-1920)": importance 2. Probably discussion of the forged Sisson telegrams, not independent ciphertext.
2. Dennis Theosophical Collection Box 3 f.16, copy of a "cipher" note in the Leadbeater affair (1905-06): importance 1.

Both: access "archive", seen "catalogue", cls C.

## Durrett / Wilkinson (the stated priority)

- The Durrett Collection of James Wilkinson Papers (1784-1882, 1 box, 39 items + Codex 203 transcripts) has **no cipher or code description**. It holds clear letters (Marshall 1787, Hamilton 1799, Gallatin 1803, Adair 1804, Morales (Pensacola) to Wilkinson 3 Feb 1807 on Burr's plans, Smith 1807, Madison 1811, Austin 1823). The Spanish-conspiracy ciphers (catalogue 761, Papeles de Cuba leg. 2374) are not here; the Chicago material is a different set.
- Durrett Miscellaneous: "The Gardoqui Despatches", 6 volumes + 3 notebooks (Cdx74, 1784-89, manuscript transcripts of Diego de Gardoqui's despatches, about 2,000 pp) and "Sebastian Papers" with a copy of a Carondelet letter to Benjamin Sebastian (Cdx162). The finding aid says nothing about cipher. Gardoqui used Spanish ciphers with Madrid, so these transcripts could contain deciphered text or marked cipher passages; worth a look in the codex itself, but nothing here counts as ciphertext. Lead only.
- No Burr, Innes or Sebastian cipher items are described. Innes, Sebastian, Jefferson, Gardoqui and Wilkinson items are ordinary letters, wills, legal papers or transcripts.

## Key leads (no ciphertext)

- Manly Papers (ICU.SPCL.MANLY), Series VI-VII: "Key to Aggas", Bacon Cipher notebooks, "Worksheets on related ciphers: Galen's Anatomy and Kazwini", Army War College codes and cipher sheets 1917, sliding letter scales; notes "ciphers in other Mss" (c. 1915-21). These are working papers and training material (Voynich/Bacon: excluded as famous); could hold Manly's own breaks of WWI intercepts.

## Dead ends

- Lincoln/Barton, Douglas (DOUGLASSA, DOUGLASFAMILY), Goodspeed, Italian and French codices (MS/CRMS series): no cipher term at all. Bacon (Sir Edmund Bacon family letters 1638): "cryptic comments" only. 'Cypher' in FISHBEIN is a surname.

## Not reached

- Item-level catalogue records (catalog.lib.uchicago.edu, Turnstile/Anubis blocked) and the site search; the finding aids describe collections at folder level, so a single cipher letter inside a folder described only as "correspondence" is invisible to this sweep.
- Rare-book printed material, maps and digital collections (campub, collex) not searched; Goodspeed only checked at landing-page level.
- Unlisted or uncatalogued collections and EADs not in `/ead/rlg/` (a few newer finding aids may live elsewhere).
- Folder-level text in the 1,986 PDFs was not compared with the XML.
