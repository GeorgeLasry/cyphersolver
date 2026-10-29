# Coverage log: Northwestern University Libraries sweep (28 Oct 2026)

| # | Endpoint | Query | Result |
|---|---|---|---|
| 1 | findingaids.library.northwestern.edu (ArchivesSpace) via curl: /, /sitemap.xml, /robots.txt | landing | **403 Cloudflare "Just a moment"** (managed challenge) |
| 2 | same, built-in browser, /search?q[]=cipher | cipher | Cloudflare "Performing security verification" page that never resolved in ~16 s; no interactive check clicked; tab closed. **Blocked** |
| 3 | same, WebFetch | /search?q[]=cipher | 403 |
| 4 | findingaids.../api/ | | 404 (public API not exposed; backend host unknown) |
| 5 | web.archive.org availability/CDX for findingaids.* | | one snapshot of /search (Aug 2025) only; CDX prefix query empty; no usable harvest |
| 6 | archivesspace./archives.library.northwestern.edu | | no such host |
| 7 | WebSearch restricted to findingaids.library.northwestern.edu, 3 queries | cipher/coded | no cipher hits; returned Sorabji letters, registrar cards, Dawes/Leopold-Loeb, Barnett, etc. |
| 8 | api.dc.library.northwestern.edu/api/v2/search/works (dc_search.py) | 24 terms, size 100 | cipher 0, cypher 1 (a concert), decipher 2, deciphered 3, coded 5, encoded 1, all others 0. All noise (OSPAAAL poster, photo captions, colour-coded maps, music concerts). DC is photographs, maps, music, Africana images, not manuscripts |
| 9 | dc.library.northwestern.edu/search (HTML) | | 403 (CloudFront); not needed, API works |
| 10 | search.library.northwestern.edu Primo NDE, guest JWT + /primaws/rest/pub/pnxs, vid 01NWU_INST:NULV_NDE (primo_search.py), scope MyInst_and_CI, facet_rtype=archival_material_manuscripts | 26 terms | cipher 5, cypher 5, deciphered 1, cryptogram 1, cryptograph* 22, coded 1, nomenclator 57, chiffre 1, cifra 1, Geheimschrift 1, rest 0. Every hit is Central Index material (ProQuest History Vault "Glenn family cipher book" = arithmetic copybook probable, John W. Hayes labor-union papers, Czech Manuscriptorium: Tassis Cryptographia 1627 NKCR 17 G 416, Cryptographia oder Geheime schrifft 1685 NKCR 8 G 14, Basel/St Gallen/Einsiedeln glosses). None held at NU |
| 11 | same, scope MyInstitution (local only), manuscript facet (primo_local.py) | 20 terms | 0 hits for every term. Unfiltered local scope "cipher" = 1,906 hits, first 100 all books/video/audio/score/journal: the NU catalogue holds no archival or manuscript records (those are only in ArchivesSpace) |
| 12 | library.northwestern.edu McCormick page, alpha-correspondence.pdf (cited by search) | | page 200 but links only to findingaids.*; the PDF URL is 404 |
| 13 | evanstonhistorycenter.org, garrett.edu | landing | 200; no searchable finding-aid endpoint found; not swept |
| 14 | rotary.org archives | | 429 on first request; archive.garrett.edu / Rotary: not reached |

Term hit counts: only the DC and Primo columns above exist; the ArchivesSpace column (the real target) is "not obtained".
Manuscript-level hits read in context: Glenn cipher book, Tassis and 1685 Cryptographia (printed or Prague copies of treatises, not ciphertext, not NU). All noise for this project.

## Finding aids reached later (29 Oct 2026)
The ArchivesSpace finding aids blocked above were searched from the user's Chrome after the user passed the Cloudflare check: 27 terms, no ciphertext. Counts and hits are in research/chi_chrome_pass/README.md.
