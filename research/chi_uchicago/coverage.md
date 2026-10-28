# Coverage log: University of Chicago Library SCRC sweep (Oct 2026)

| # | Date | Endpoint | Query | Result |
|---|------|----------|-------|--------|
| 1 | 28 Oct 2026 | www.lib.uchicago.edu/e/scrc/findingaids/ (curl) | landing page | **403 Forbidden** (not retried) |
| 2 | 28 Oct 2026 | www.lib.uchicago.edu/e/scrc/findingaids/search.php?q=cipher | cipher | 301 to /scrc/?q=cipher |
| 3 | 28 Oct 2026 | catalog.lib.uchicago.edu VuFind (curl) | cipher, Archives/Manuscripts | **403 + Anubis "checking if you're a robot" page**; stopped |
| 4 | 28 Oct 2026 | www.lib.uchicago.edu/scrc/?q=cipher (built-in browser) | cipher | **Cloudflare Turnstile verification page**; not completed (no bot-check bypass); stopped |
| 5 | 28 Oct 2026 | researchworks.oclc.org/archivegrid (curl) | cipher "University of Chicago" | **403 Cloudflare "Just a moment"**; stopped |
| 6 | 28 Oct 2026 | www.lib.uchicago.edu/ead/rlg/ (curl) | directory index | **200**: open Apache listing of every SCRC EAD finding aid, 2,025 .xml + 1,986 .pdf. This became the sweep route. |
| 7 | 28 Oct 2026 | www.lib.uchicago.edu/ead/pdf/ | directory | 403 (not retried) |
| 8 | 28 Oct 2026 | loc.gov collections/first-american-west JSON | cipher etc. | 404 (collection URL retired); loc.gov general "cipher durrett" = 1,051 newspaper hits, no Durrett MSS; dropped |
| 9 | 28 Oct 2026 | Web search (4 queries: site:lib.uchicago.edu findingaids cipher; UChicago "in cipher"; Durrett Wilkinson cipher; Gardoqui papers UChicago cipher) | | no item-level UChicago cipher hits; leads: Manly papers (cryptography folders), Gardoqui papers (Durrett) |
| 10 | 28 Oct 2026 | goodspeed.lib.uchicago.edu | landing | 200; Greek NT/Syriac/Ethiopic manuscripts, no cipher scope; not swept further |
| 11 | 28 Oct 2026 | fetch_ead.py | all 2,025 EAD XML, 3 s spacing, priority: Durrett, Douglas, Barton/Lincoln, Manly, Rickert, codex/MS, Italian/French first | see below |

## Result of row 11 (full EAD download and grep, 28 Oct 2026)

- 2,025 EAD XML finding aids listed; 2,024 downloaded and read (about 127 MB; EPSTEIND and PHYSIOLOGY failed once with a connection reset, retried; 2,026 files on disk at the end). 3 s spacing, no 403/429 during the crawl. The XML copies were deleted afterwards (re-fetch with fetch_ead.py); `ead_hits.json` keeps the matches.
- Pass 1 (grep_ead.py), 24 patterns (cipher, cypher, decipher, in code, coded, code letter/telegram/message/book, cryptogra*, secret writing, nomenclat*, chiffr*, cifra*, cryptic, codebook, invisible ink, encrypt*, cryptanaly*, geheimschrift, verschl*): **215 hits in 56 files**.
- Pass 2 (broader: secret code/letter/alphabet, private code/alphabet, steganograph, geheim, telegraphic code, "codes and ciphers", sympathetic ink ...): all extra hits false.
- Reading of the 215 hits: nearly all noise (statistical codebooks, "nomenclature" of botany/chemistry, coded survey forms, football signal nomenclature in Stagg, Maya "decipherment" grants in McQuown, modern cryptography notes in Bookstein/Rush). 
- Real cryptographic material, none of it an open historical ciphertext: Manly Papers (Series II, VI, VII: Voynich/Bacon worksheets, Army War College training cipher sheets 1917, a Spanish 'Tratado de Cryptografia' notebook 1894, 'Key to Aggas'); Rickert, Hulbert and D. H. Stevens papers (WWI MI-8 service, no ciphertexts); Hutchins presidential papers box 239 f.4 'World War II, codes and ciphers, 1940-1942' (university administration).
- Two item-level leads kept as weak candidates: Harper Papers Box 61 f.19 (Sisson documents code messages), Dennis Theosophical Collection Box 3 f.16 ('cipher' note, Leadbeater case).
- Durrett Collection: all seven Durrett finding aids (Misc, Government, Broadsides, Portraits, Trustees, R) plus the sub-collections James Wilkinson Papers (WILKINSONJ, 39 items), Shelby, Lyne, Todd, Hart, Wilson were read. **No cipher, code, or secret-writing term appears anywhere in them.**
