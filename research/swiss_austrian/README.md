# Swiss, Austrian, Bohemian and Hungarian platforms sweep (28 Oct 2026)

Brief: `research/archive_sweep_2026-10/BRIEF.md`. Metadata sweep for ciphertexts not yet in the repo. **25 candidate rows**
in `candidates.json` (`build_candidates.py` writes it; edit there). All scored from catalogue descriptions (`seen: "catalogue"`),
no image viewed. Raw harvests are in `raw/` and the large `manu_hits*.jsonl` (git-ignored, see `.gitignore`; re-creatable with the scripts).

## Where the yield was

| Source | Route | Result |
|---|---|---|
| **Hungaricana** (Hungarian regests of the Vienna archive, DL charters) | server-rendered `https://www.hungaricana.hu/en/search/results/?list=<base64 {"query":..}>&per_page=100&page=N`; needs a browser User-Agent | **by far the best**: the Bécsi Magyar Levéltári Kirendeltség regests of HHStA Türkei I and Ungarische Akten say "sifrír ... feloldás nélkül" (cipher, no decipherment). 2,633 "sifrír*" hits, 416 with "without decipherment"; 438 detail pages fetched; 15 candidate rows |
| **Manuscriptorium** (`castor` Solr API behind the SPA) | `https://www.manuscriptorium.com/castor/manuscriptorium/search/formSearch?query=[{"fieldId":"globIndex","queryRow":T,"logOp":""}]&coreId=manuscriptorium&rows=100&start=N&aster=true|false` (public, no key) | ~50 term variants, ~2,000 records; 95% printed-book noise (Trithemius, "Cifra de ..."), but the Biblioteca Nacional de Portugal records are item-level letters: 8 rows |
| **Staatsarchiv Zürich** (scopeArchiv, `https://suche.staatsarchiv.djiktzh.ch/`) | form postback, same as AIS (`scope_harvest.py`) | 270 hits over 27 terms, 99% modern (Opernhaus, Chiffre-Inserate, patents); 2 rows + key leads |
| **e-manuscripta.ch / e-rara.ch** | OAI-PMH `https://www.e-manuscripta.ch/oai?verb=ListRecords&metadataPrefix=oai_dc` (the HTML search is behind a JS bot check) | ~75k oai_dc records read (Basel UB 25k, ZB Zürich 23.7k, SNB 12.7k, Schaffhausen, Zofingen, Solothurn, Luzern, Bern, plus 6k/7k default-order samples of e-manuscripta/e-rara): **no ciphertext**. Only hits: Musculus's secret signature note (1548), Jung-Stilling diary 1806 (already rejected in central_archives README) |
| **Kramerius** (NKP) | Solr `https://kramerius5.nkp.cz/search/api/v5.0/search`, 36 terms | 0 manuscripts: Dan Brown books, a 2007 edition of Mácha's diary. Other Kramerius hosts (MZK, KNAV, SVK) gave 403/404/non-JSON |
| **Staatsarchiv Bern** (`www.query.sta.be.ch`, scopeArchiv) | same postback | 1 hit (1943 Bundeshaus Chiffrierbüro), nothing relevant |
| **Slovakiana, Kramerius libraries, ÖNB** | see blockers | nothing |

Terms used: Chiffre/chiffriert/chiffrirt/Chiffren/Chiffrenschrift/dechiffriert/Geheimschrift/Ziffernschrift/Entzifferung/verschlüsselt/Kryptogramm/
Geheimzeichen/Geheimsprache; šifra/šifrovaný/tajné písmo/tajnopis; cifra/cifrada/cifrado/decifrada; chiffré; titkosírás/titkos írás/rejtjel/
sifrír*/feloldás nélkül; szyfr*/cyfr*. Date filter 1350-1950 applied by hand.

## Candidates, ranked

1. **MNL DL 46150, Maffeo da Treviglio → Thomas Bakócz, 30 Nov 1490**, four pages in cipher. The repo has the Maffeo key (buda1489-maffeo). A new ciphertext for a known key, 15th century (importance 3, solvability 4).
2. **Philip III → Spinola, seven ciphered letters of 1618** (BNP MSS. 41 n. 5), "decipherment absent", with the 1614 letter deciphered and a letter on the change of cipher (solvability 3; images not located).
3. **Wesselényi 1663 and the Fasc. 327 "Chiffres 1664-68"** (HHStA Ungarische Akten, Verschwörerakten): ciphers of the Hungarian conspiracy with keys in the same Faszikel.
4. **Habsburg Constantinople despatches 1573-1648, ten cluster rows** (Rym, Ungnad, Sinzendorff, Breuner, Eizing, Pezzen, Kreckwitz, Starzer, Lustrier, Schmid, Greiffenklau, Czernin): about 420 entries "without decipherment". Pezzen 1588-91 (59 entries) and Starzer 1611-20 (55) are the longest single-resident runs. They overlap catalogue rows 342/343 (Ungnad 1576, Sinzendorff 1578) and Láng's inventory; no scans on AIS per earlier repo sessions, so solvability is 2.
5. **João IV → Cascais 1643-44, BNP MSS. 14** with cipher-plus-decipherment pairs in MSS. 13.

## Excluded, and why

- **HHStA Türkei I 1557-1572** (34 regest entries): the same despatch is "sorközben feloldva" (deciphered between the lines) in one copy and an undeciphered duplicate in another. The text is already read.
- **Hungaricana "sifrír" entries without a "no decipherment" phrase** (about 1,270 Türkei I entries, "other" class): ambiguous, may include deciphered copies; not rowed.
- Medieval scribal colophon ciphers on Manuscriptorium (MZK A 50 1374, NKCR IV H 16, V G 16, I A 29B; Wrocław I Q 153 1441; St Gallen Cod. Sang. 845): vowel or letter shifts, already decoded in the catalogue note.
- Teplice alchemical codices (1665, "tajné písmo", symbol use) and the Iceland Lbs 946 8vo "Napoleon cipher" key (key lead, a Dulmálslykill): not letters.
- BNP letters that carry or are paired with a decipherment (MSS. 41 n. 3 Zúñiga 1613, MSS. 41 n. 5 doc 1, COD. 4419, COD. 6441, COD. 8721 Turin 1750s, MSS. 201 n. 26, MSS. 146 Ennes letters).
- Printed cryptography (Trithemius, Schott, Breithaupt, Vigenère editions) and "Cifra"/"Cifras" as titles.
- StAZH patents, newspapers, Opernhaus MAG.

## Key leads (bare keys or tables)

- StAZH A 241.3 / C I Nr. 3580: Ziffernschrift-Schlüssel for secret correspondence with Bern's Stadtschreiber Johannes Matthey, 11 Apr 1653, and one for Bürgermeister Waser (about 1653).
- StAZH A 235.2 (Erster Villmergerkrieg, 1655): dossier "mit 3 Chiffrierschlüsseln".
- StAZH E II 360 fol. 255: Wolfgang Musculus's own secret writing (also e-manuscripta 3223471).
- DF 293290 (MNL photo collection of ASMi Archivio ducale Sforzesco 642), 27 Feb 1488: "titkosírás-táblázat", a cipher table.
- HHStA Verschwörerakten IV Fasc. 312 Konv. A ("Titkosírás kulcsa"), Fasc. 314 Konv. B (key with letters), Fasc. 317 Konv. D (a key "that is not 17"...), Türkei I Kt. 1 Konv. 4, 1530 (fol. 70-71 with key made for it).
- BNP COD. 10566//3 "Cifra de nomes antigos ... Jesuitas Faro 1759" and MSS. 223 n. 29 "Abedecedario ... la cifra" (1750-1801).
- Iceland Lbs 946 8vo f. 8r-8v: dulmálslykill for Napoleon's correspondence.

## Dead ends and blockers

- **ÖNB**: onb.digital is a JS single-page app over 3.9M items, mostly newspapers, with no manuscript filter via URL; the Primo catalogue (`search.onb.ac.at`) returns 403 to scripts; `digital.onb.ac.at` OAI times out. Not reached. ÖNB manuscripts reach us only through Europeana/Manuscriptorium (not many).
- **Basel Staatsarchiv** (`query.staatsarchiv.bs.ch`), **Archives d'Etat de Genève**, **DAVEL (Vaud)**, **manuscripta.at**: 403 to scripts. Not tried in the built-in browser. Luzern, St Gallen, Aargau, Graubünden, Thurgau scopeArchiv hosts did not resolve under the guessed names. Archives Quickaccess covers only topical subsets.
- **ETH-Bibliothek** records on e-manuscripta are not in any OAI set (set `emanuszut` is empty); only reachable in the default 222k-record listing, of which about 6k were read. e-rara (165k, mostly printed books) was sampled only (7k).
- **Hungaricana** archive pages return only regest titles; images are on the AIS (no scans for Türkei I per earlier repo sessions) or MNL DL online.
- **Slovakiana, Czech archive portals (Archivní portál, ebadatelna)**: not reachable or not scripted. Kramerius gave nothing in metadata fields.
- Prior art checks (web search, 28 Oct 2026) were limited to Láng 2018 (Real Life Cryptology) and Spinola/Retortillo Atienza 2019; Láng's appendix (about 1,600 partly or fully enciphered Hungarian-related letters) was not read item by item, so some Türkei I and Ungarische Akten rows may already be listed there as "undeciphered".

## Scripts

`oai_harvest.py` (Visual Library OAI, per set), `oai_filter.py` (cipher-term filter), `manu.py` + `manu_filter.py` (Manuscriptorium castor API), `kram.py` (Kramerius Solr),
`scope_harvest.py` (scopeArchiv postback: Zürich, Bern), `hungaricana.py` + `hung_details.py` + `hung_cluster.py` (Hungaricana harvest, detail fetch, clustering),
`build_candidates.py`, `probe.py` (quick URL probe). Intermediate results: `hung_clusters.json`, `hung_nolos.json`, `bnp_cifra.json`, `manu_strong.tsv`, `oai_hits_all.json`.
