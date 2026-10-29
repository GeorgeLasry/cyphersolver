# Canada / Latin America sweep (28 Oct 2026)

Scope (owner update): the whole hemisphere, region "Americas", to 1950. 4 candidates written (`candidates.json`,
built by `make_candidates.py`); all `seen: catalogue`, none viewed. Yield is low: most catalogues here cannot be
scripted, and the scriptable ones hold no cipher manuscripts.

## What was reached, and what it gave

| Source | Method | Result |
|---|---|---|
| Canadiana (canadiana.ca) | `search/?q0.0=ti:/su:/tx:term`, 20 terms EN/FR/ES, 1500-1950, `canadiana.py` -> `canadiana_hits.json` (61) | Printed material only: commercial telegraphic cipher codebooks (Law 1880, Barnard 1895, Maguire, CPR mining code), music primers, newspapers, histories. No manuscript ciphertext. |
| World Digital Library (now a loc.gov collection) | loc.gov JSON API, 21 terms, `wdl.py` -> `wdl_hits.json` (432 raw) | Only 4 records name a cipher: Greenhow cipher letter (already in repo, targets/greenhow1861) and noise. wdl.org itself is behind Cloudflare. |
| loc.gov, all collections, manuscripts 1500-1950 | `loc_all.py` / `loc_all2.py` -> `loc_hits.json` (35; both scripts hung on a request and were cut off before the last terms) | OCR noise only (Roosevelt, Blackwell, Goldsborough "chiffre"). US material belongs to research/us_wars. |
| Biblioteca Nacional Digital de Chile / Memoria Chilena | engine.bibliotecanacionaldigital.gob.cl `find.cgi` JSON, 18 terms, `bnd_chile.py` -> `bnd_chile_hits.json` (132) | Poetry and articles ("Cifrado en la Villa Adriana", Tomeo's "carta cifrada"). Nothing. `mchile.py` was an abandoned first try. |
| Nova Scotia Archives | site search | Digitised-content search only; no cipher hits. |
| Web search (descriptions only) | about 10 searches: Haldimand/LAC, HBCA, Nouvelle-France, Bolívar, San Martín, AGN Mexico, Brazil | Found the Narváez literature and the Kerlérec lead. Nothing for Bolívar, San Martín, Brazil, New France or HBCA. |

## Candidates (ranked)

1. Kerlérec despatches 1758-59, some in cipher (Ministère des Armées inventory; later sibling of the Huntington Kerlerec items already catalogued). Cote not read; host refused connections.
2. Obregón (Washington 1825) coded despatches, AHGE-SRE; Narváez decoded two of a "small sample".
3. Torrens (Bogotá 1826) reserved notes 2-3; Narváez admits his code analysis was thin.
4. Michelena (London) cipher letter 6 Oct 1824, AHDSREM leg. 40-11-3; Narváez 2011 attribution.

Items 2-4 are the Mexican cryptography family of Roberto Narváez (*Criptografía política, diplomática y militar en
México 1813-1926*, SRE). He has deciphered much of it, so solvability is 1-2 until his articles show what is still
open. His published systems are the key leads for the family. The 1860-79 military cryptography article
(Historia Mexicana, redib record) was not opened; research/nara_military also lists a 2025 Narváez article as not reached.

## Blockers (not scrapable; not bypassed)

- **Library and Archives Canada** Collection Search: Cloudflare security check, also in the built-in browser (stuck on "validating"). Not bypassed. LAC holds the Haldimand papers (MG 21; BL Add MS 21661-21892 is covered in research/us_wars) and MG 1 C11A transcripts; heritage.canadiana.ca reels have no full text.
- **BAnQ / Pistard**: Radware captcha. **wdl.org** and **bndigital.bn.gov.br** (Brazil): Cloudflare. **SIAN** (Arquivo Nacional, Brazil): "Request Rejected".
- BC Archives: TLS certificate error (no verification bypass used). Archives of Ontario and GNB: no usable search URL found. HBCA: no search endpoint; its "ciphers" are address marks on covers.
- AGN Argentina, Biblioteca Nacional Perú/Argentina, Biblioteca Nacional de Colombia: unreachable from here. AGN Colombia, Archivo Nacional de Chile, AGN Mexico: home pages load, catalogues are dynamic and were not searched.
- ministère des Armées digital library: ECONNREFUSED on fetch.
- Not reached: dLOC (JS-only), Cuban/Caribbean archives, Hemeroteca Digital, AGN Mexico Inquisición/Infidencias series, the Narváez articles read in full.

## Next steps for a human or a normal browser session

Run `Result?q=cifra|chiffre|cipher` on LAC Collection Search and the BAnQ Pistard search from a regular browser;
open the Kerlérec inventory page; read Narváez's articles for the undeciphered remainder.
