# Polish archives sweep (Oct 2026)

Sweep of Polish state archives and Polish digital libraries for unsolved historical ciphers, run 26 Oct 2026 under
`research/archive_sweep_2026-10/BRIEF.md`. Output: `candidates.json`, with 38 rows built by `gen_candidates.py`.

## What was reachable

| Source | Route | Result |
|---|---|---|
| **szukajwarchiwach.gov.pl** (main target) | curl gets an Imperva stub. The built-in browser gets an Imperva "Additional security check" page that asks for a checkbox. | **Blocked.** Solving bot checks is off-limits, so not one search ran. Archives Portal Europe (which carries Polish finding aids) is also behind a Cloudflare check that never cleared. Google does not index unit pages for "szyfr". |
| **AGAD's own online inventories** | `https://www.agad.gov.pl/inwentarze/<name>.xml` (HTML despite the extension). 84 files are listed by `https://agad.gov.pl/pomoce/eagpln.xml` and `inwentarze/testy.html`. All 84 were downloaded and grepped with `agad_inventory.py`. Hits are in `agad_inventory_hits.txt`. | **Main source of rows.** Zbiór Popielów (fonds 12) has 36 cipher units. Archiwum Publiczne Potockich (335), Nabytki I (420) and Zbiór dokumentów papierowych (c02p) have one each. Archiwum Radziwiłłów, Archiwum Koronne, Archiwum Zamoyskich, the Metryka Koronna correspondence and Zbiór Branickich have **no** inventory in this set. Their finding aids are only on szukajwarchiwach. |
| **AGAD scan server** `agadd2.home.net.pl/metrykalia/<fonds>/...` | Plain HTTP, open. Some Popiel units have letter-level lists (`inwentarze/ZbPop<sygn>.xml`) linking every image. APP 335 has 452 scanned units. | The Deboli cipher files for 1788-1792 (ZbPop 428, 17, 4, 5, 416) are online. One page each of ZbPop 4 and 17 was viewed. |
| **Polona** (BN, including the Czartoryski Library manuscripts) | `POST https://polona.pl/api/search-service/search/simple?query=..&page=..&pageSize=..` (body `{}`), with detail at `GET /api/search-service/search/<uuid>`. Scripts: `polona.py`, then `polona_detail.py`. | 3,766 fuzzy hits, about 200 of them manuscripts. Only 17 really mention a cipher, and **none is a usable candidate**: Rps 6537 I (1864) has its decipherment attached, and the rest are AK telegrams (after 1939), "cyfra" as a page number, and similar. Czartoryski descriptions are too thin to flag ciphers. |
| **Europeana API** (`wskey=api2demo`, `qf=COUNTRY:poland`) | `europeana.py` | 498 hits. The only manuscript leads are already in the repo: Niedźwiecki, Kórnik BK 02411 (`research/oldest`), and the Szembek "List zaszyfrowany", BK 1560 (target szembek1689). |
| **dLibra libraries** (WBC/Kórnik, KPBC Toruń, RCIN and others) | `dlibra.py` (old-UI HTML results) and `dlibra_meta.py` (record metadata). | WBC gave two new items: BK 401 (a row) and BK 1560-3 (a key, see below). KPBC and RCIN gave only print noise. PBC Gdańsk, JBC, ŚBC and BCUWr run the new React/GraphQL dLibra, so the HTML scraper sees 0. In the browser their hits are full-text OCR of periodicals. |
| **DECODE dump** (`research/catalogue_harvest/decode`) | Records held by the Archiwum Narodowe w Krakowie: 77 in all, every one status N/A. | 27 record ids are not mentioned anywhere in the repo. They are grouped into 11 rows. The others belong to targets potocka1714 and sieniawski1708. |
| AP Gdańsk, AP Toruń | Their own sites have no searchable inventory, and DECODE holds no Gdańsk records. | Not reached. Szukajwarchiwach only. |

Search terms: szyfr, szyfrem, szyfrowany/-a/-e/-ych, zaszyfrowany, szyfrowy, szyfrów, szyfru, cyfra, cyfrą, cyframi,
"pisane szyfrem", klucz szyfrowy, Chiffre, chiffre(s), chiffré, Ziffer(n), chiffriert, Geheimschrift, cifra,
ciffra, zifra, kryptogram, tajnopis, nomenklator.

The raw hit dumps (Polona 4.7 MB, Europeana, dLibra) were moved out of the repo because they are noise. Rerun the
scripts to regenerate them; `polona_detail.py` needs `polona_hits.jsonl` from `polona.py`.

## Best leads

1. **Deboli → Stanisław August, St Petersburg cipher despatches, 1788-1792** (AGAD Zbiór Popielów 428, 17, 4, 5,
   416). There are about 500 despatches, all scanned on agadd2. One page was viewed: a full page of about 270
   numeric code groups (3-4 digits, some with a/b suffixes) and no interlinear decipherment. Each cipher despatch
   has a Polish text of the same day in ZbPop 417/419/420/421/415. **Correction, 27 Oct 2026:** these are not open
   despatches but the cabinet's decipherments. For 1790 all 109 were paired and two were aligned group by group
   (`targets/deboli1790/`, catalogue 419 closed). Keys
   are filed in the same fonds (ZbPop 444 "Cyfra polska" sent to Deboli 1783, 451 French cipher 1780, 453-454) but
   are not online. Zielińska & Danilczyk printed only 1780-1782. Importance 4, solvability 4.
2. **Deboli 1783-1787** (ZbPop 9, 10, 11, 2, 3): the same series with about 420 pieces. No scans were found
   outside szukajwarchiwach.
3. **Zabłocki → the King from Berlin, 1780-1794** (ZbPop 20, 19, 13, 423, 14, 21): about 800 pieces in cipher.
   The clear Zabłocki files are ZbPop 372/373, and the keys are ZbPop 445/452 "Chiffre ... Kwilecki allant a
   Berlin" 1772.
4. **Letters to Ignacy Potocki "nierozszyfrowane"** (APP 335, 279a/480a, 1782). The archive itself labels them
   undeciphered. The 279a gallery is scanned, but 480a is only 2 pages.
5. **Wąsowicz → Aleksander Lubomirski 1662-69** (AN Kraków AKPot 3227, DECODE R7502-R7511). There are nine
   letters, and key record R7501 is in the same file (class A). Also **Morsztyn → Jerzy Lubomirski** (ASang 247/13,
   R7517-R7519) and **M. K. Radziwiłł → A. Lubomirski 1669** (R7512, same file as R7501).

Other rows: Hennig at Gdańsk 1788-92, Middleton at The Hague 1791-94, Jabłonowski at Berlin 1791-92, Woyna and
Pokubiatto/Corticelli at Vienna 1788-92, the Polish minister at Dresden 1791, Ogrodzki's St Petersburg
correspondence 1765/1769-70 (the 1765 volume has its key bound in), Garnysz ↔ Dresden 1789 (Nabytki I 125),
Charles VI → Kinner 1728 (Zb. dok. pap. 3001), Kórnik BK 401 "List nominata Inflant" (1697-1708), and the
Sanguszko-archive ciphers in DECODE.

## Key leads (bare keys, not rows)

- AGAD Zbiór Popielów 444 (Polish cipher for Deboli, 8 III 1783); 445/452 (French cipher for Kwilecki, Berlin, 1772);
  446/447 (old cipher for Gdańsk and London, enchiffrement/déchiffrement, copied 1780); 450 (French cipher for
  Constantinople, 1780); 451 (French cipher for Deboli, 1780); 453 and 454 (the Cabinet's numbered keys for the
  envoys, 1772-1795, 12+ sheets). These are the keys to all the Popiel rows. Scans were not found online.
- AGAD Zbiór Popielów 317 and 320: registers of already-deciphered letters, for Ogiński at Vienna 1772-74 and Deboli
  at St Petersburg 1774-77. They are decipherments that can be paired with any surviving cipher originals.
- PAN Biblioteka Kórnicka BK 1560-3, "Szyfry do listów politycznych" (Szembek archive, 18th c., WBC edition 346026,
  DjVu online). Test it on BK 401 and against target szembek1689.
- DECODE R7501 (key, AKPot 3227 pp. 81-268, item 1) for the Wąsowicz letters. R7460/R7461 (ASang 85/3) for R7463-R7465.

## Dead ends and exclusions

- Deboli 1780-1782 (ZbPop 32 and 8 cover 1781 and 1782) are printed in the IH PAN edition, so they were left out.
- Kórnik BK 243 (Krzycki → Tomicki 1521): cover names resolved in the margin and printed in Acta Tomiciana, not a cipher.
- Polona Rps 6537 I (1864 priest's diary): its decipherment is attached.
- The Rákóczi → Elżbieta Sieniawska letters (Czartoryski 2761 IV, French, scanned on Polona) and the Sobieski →
  M. H. Sieniawski letters (2756 IV) may contain cipher passages, but nothing in the description says so. They were
  not viewed and not rowed. Worth a look, because the Rákóczi-Sieniawska correspondence is known to use code names.
- Teki Naruszewicza (Czartoryski) have contents lists as PDFs on `sowa-cdn.mnk.pl`. Three were checked with no
  hits, and a full list of the PDFs was not found.

## Not reached

szukajwarchiwach.gov.pl, the whole portal. That covers AGAD Archiwum Radziwiłłów (dz. IV/V letters), Archiwum
Koronne Warszawskie, Archiwum Zamoyskich, Zbiór Branickich z Suchej, AP Gdańsk (Danzig envoy letters, fonds 300),
AP Kraków and AP Toruń. A person can pass the Imperva check in the built-in browser and then rerun the term list
through the portal's search. The Popiel scan lists also show that many units exist only there. The Kopal &
Waldispühl prior-art check was not needed, because none of the rows overlap their published Polish/Swedish letters
(Chodkiewicz 1575 is already closed in the repo).
