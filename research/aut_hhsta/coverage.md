# Coverage: Austria sweep (28 Oct 2026)

Every query run, with the result count. All requests were spaced 3 s or more. AIS = Archivinformationssystem
of the Austrian State Archives (https://www.archivinformationssystem.at, scopeArchiv, covers HHStA, AVA, FHKA, Kriegsarchiv).
"img" = the result row carries the "Ansichtsbild" icon (scans viewable online).

## AIS full-text search (`ais_search.py`, `run_terms.py`)

| Term | Hits | img |
|---|---|---|
| Chiffre (exact) | 0 (the engine returns nothing for the bare word; central_archives got 1,500 via a different form) | 0 |
| Chiffre* | 0 | 0 |
| chiffriert* | 243 | 130 |
| chiffrierte* | 84 | 27 |
| dechiffriert* | 134 | 77 |
| Chiffrenschlüssel | 244 | 2 |
| Ziffernschlüssel | 13 | 0 |
| in Ziffern | 43 | 4 |
| Ziffern | 43 | 4 |
| Geheimschrift | 22 | 1 |
| Dechiffrierung | 29 | 11 |
| Chiffren | 40 | 3 |
| Chiffrierung | 2 | 0 |
| Chiffrierbüro | 0 | 0 |
| verschlüsselt* | 94 | 5 |
| Kryptographie | 1 | 1 |
| Chiffrenbrief, Chiffreschrift, Ziffernschrift, cifrato, chiffré* | 0 each | 0 |
| Cifra | 3 | 1 |
| ciffra | 1 | 0 |
| Zifra | 5 | 0 |

665 unique records in all. 162 image-bearing records that were neither key folders nor already named in the repo
were fetched in full (`details.py`, two passes; the second pass added the `Unterteilung/Enthält` and `Inhalt` fields).
Of these 48 say "interlinear dechiffriert" or similar and were dropped as sibling keys.

Not searched: the `Entzifferung`, `entziffert`, `Klarschrift`, `Chiffern`, `Ziffer`, `chiffrés` terms (already done by
research/central_archives, with counts in its README); Kriegsarchiv WWI "Chiffrierbüro" returned 0 hits, so the
WWI intercepts are not described under that word in AIS. Only 1914-18 Kriegsarchiv hit: AT-OeStA/KA FA NFA HHK AK 4. Armee AK 70
("Reservate: Index ..., russische Streitkräfte", an index, not a cipher).

## ÖNB (onb.digital), `onb_search.py`

The site's own `Frontend/insert_query` then `/search/<id>` flow (the search API at digital.onb.ac.at answers 401 to a direct call).
Geheimschrift 33 (printed books on cryptography, papyri), Chiffre 19 (medieval codices matched on the word "chiffre" in other senses),
chiffriert 0, Chiffrenschlüssel 1 (a 1934 poster), Ziffernschrift 1, Dechiffrierung 2, Chiffrierschlüssel 0, Cifra Brief 0,
Geheimschrift Brief 2. No ciphertext of a letter or register: all hits are treatises, printed books or unrelated codices.
Cod. Vindob. Pal. 2398 (Tranchedino) is a treatise and is already on DECODE (about 130 records).

## DECODE (research/catalogue_harvest/decode/list.json, in the main checkout; the worktree lacks the git-ignored dumps)

Vienna-held DECODE records are almost all HHStA Staatskanzlei Interiora Chiffrenschlüssel Kt. 13-20, Geheime Staatsregistratur
Fasc. 46, Ung. Akt. Spec. Verschwörerakten Konv. D, Handarchiv Kaiser Franz, and Cod. Pal. 2398: keys and a treatise, no
Türkei I or Maximiliana letters. So none of the candidate rows has a DECODE id.

## Unreachable or not worked around

| Site | Result |
|---|---|
| Archives Portal Europe (archivesportaleurope.net) | 403, Cloudflare "Just a moment" bot wall; not worked around |
| zobodat.at (MGSL 125, 395-399, Ludwig on Lang 1526) | 403 to a script (WebFetch); not worked around; row 12 records it as a lead |
| search.onb.ac.at (Primo) | page is JavaScript only; pnxs API returns the app shell, not used |
| digital.onb.ac.at/rep/discovery API | 401 without the site's own session; the onb.digital front end was used instead |
| ÖNB Handschriften catalogue / manuscripta.at | no search endpoint found that accepts a cipher keyword; reached only through web-search snippets (Cod. 10172 'Ars cryptographica novissima', Cod. 2398) |
| Archivportal-D | not queried (research/central_archives already worked through 200 of its 171+ 'chiffriert' hits) |
| Kriegsarchiv online (outside AIS) | no separate catalogue reached |
