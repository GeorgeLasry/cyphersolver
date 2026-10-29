# Northwestern University Libraries sweep (28 Oct 2026)

**Result: 0 candidates.** The one place where NU's manuscripts are described (the ArchivesSpace portal findingaids.library.northwestern.edu, which holds McCormick, University Archives, Herskovits, Transportation, Music) is behind a Cloudflare managed challenge for curl, WebFetch and the built-in browser; no EAD directory, sitemap, API or mirror was found. Everything else that could be queried was searched and is noise.

## Method
- Digital Collections JSON API (dc_search.py): 24 terms, no cipher item (counts in coverage.md).
- NU catalogue, Primo NDE pnxs with a guest JWT (primo_search.py, primo_local.py): the NU catalogue has no archival records; hits are Central Index items not held at NU.
- Web searches restricted to the finding-aid host found no cipher descriptions (search engines index only a sample).

## Best leads
None ranked. Weak, unverified: the McCormick Library holds the Charles Dawes archive and FDR/Leopold-Loeb material (20th century, possible code telegrams) and the Herskovits Library's Claude Barnett collection; no cipher is described anywhere we could see.

## Key leads
None found (no bare keys).

## Dead ends
Glenn family cipher book (ProQuest History Vault, almost certainly arithmetic "cipher"/ciphering book, not NU); Prague NKCR Tassis Cryptographia 1627 and 1685 Cryptographia (treatises, in Manuscriptorium, not NU); DC hits (captions "cannot be deciphered", colour-coded maps).

## Not reached
- Full ArchivesSpace grep: needs either a human running the search in a normal browser (findingaids.library.northwestern.edu/search?q[]=cipher, then cypher, cryptogram, "in cipher", "code telegram", "secret ink", etc.), or an email to specialcollections@northwestern.edu for an EAD export. A CSV/XML export from a person's browser would let the grep be scripted.
- Evanston History Center, Garrett-Evangelical (Styberg), Rotary International archives: no searchable endpoint found or reached (Rotary 429).
