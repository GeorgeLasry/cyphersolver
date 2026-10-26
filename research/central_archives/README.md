# Central archives sweep (Oct 2026): Vienna, German union catalogues, Paris

The archive sweep of 26 Oct 2026 (brief: `research/archive_sweep_2026-10/BRIEF.md`) looked for ciphertexts that may still be
unsolved and that the repo does not hold yet. It covered the Austrian State Archives, Kalliope and Archivportal-D, and
FranceArchives with the Archives nationales.

`candidates.json` holds **69 rows**. Runs of one correspondence are grouped into one row. Every row was scored from
the catalogue description alone (`seen: "catalogue"`), so no scan was looked at. `build_candidates.py` generates the
file and is the place to edit rows.

## Method and counts

### 1. Austrian State Archives: HHStA, FHKA, AVA, KA ([archivinformationssystem.at](https://www.archivinformationssystem.at))

- **Search route.** The scopeArchiv full-text search is an ASP.NET postback. `ais_search.py` posts the form, and
  `ais_harvest.py` pages through the result list using the "next page" postback. `ais_details.py` fetches each
  `detail.aspx?ID=` page and pulls out Titel, Darin, Inhalt, Ort, Sprache, Umfang, the reproduction field and whether a
  thumbnail (Ansichtsbild) is shown. A thumbnail means the images can be viewed online.
- **Terms and hit counts.**

  | Term | Hits |
  |---|---|
  | Chiffre | 1,500 (capped; 70% are AVA Verkehr railway files) |
  | chiffriert | 243 |
  | Chiffrenschlüssel | 244 |
  | dechiffriert | 134 |
  | Chiffrierte | 84 |
  | Ziffer | 71 |
  | Chiffern | 53 |
  | Klarschrift | 55 |
  | in Ziffern | 43 |
  | Chiffren | 40 |
  | Dechiffrierung | 29 |
  | Geheimschrift | 22 |
  | verschlüsselt | 94 |
  | Entzifferung | 6 |
  | entziffert | 5 |
  | Zifra | 5 |
  | chiffrés | 5 |
  | cifra | 3 |
  | cifre | 1 |
  | Dechiffrat, Zifferbrief, cifrato, cifrada | 0 |

  The searches returned 2,090 unique items. After dropping AVA Verkehr and AdR files, about 760 detail pages were
  fetched.
- **What was kept.** Items marked "chiffriert", "in Chiffern", "ohne Klarschrift", "nicht entziffert",
  "keine Dechiffrierung", or "teilweise verschlüsselt" with no decipherment noted. Items marked "interlinear
  dechiffriert", "mit Klarschrift" or "Dechiffrierung liegt bei" were dropped, and kept only as sibling keys.
- **Rows.** 32.
- **Images.** The AIS viewer has images for RK Maximiliana and StAbt Türkei I (1530-1557). Kriegsakten, Spanien Varia
  and FHKA have none.
- **Limits.** The Familienkorrespondenz and Große Korrespondenz returned only Habsburg family letters that were already
  deciphered: Marie Karoline 1800 "mit Dechiffrierung", Maria Theresa-era copies. Reichskanzlei Diplomatische Akten
  returned nothing usable under these terms.

### 2. Bavaria, Kalliope, Archivportal-D

- **Kalliope SRU.** Kalliope has an SRU interface (`https://kalliope-verbund.info/sru`, MODS records); `kalliope_sru.py`
  harvests it. Terms: Geheimschrift (114), Chiffre/Chiffren/chiffré (224, mostly review sigla and music), chiffriert
  (17), verschlüsselt (61), Kryptogramm (7), cifra (3). That gave 424 unique records and **8 rows** (the Sieyès row also uses AN 284AP/12).
- **Kalliope records dropped:**
  - Jablonski → Ráday 1704-07 (SBB, Nachl. Francke). Already rejected in `research/oldest/scan_2026-09-23/hard_targets.md`
    because the Latin plaintext sits under the cipher.
  - Jung-Stilling diaries (rejected there too; transcripts survive).
  - Rubens → Olivares 1629, Basel (Rubens struck out the cipher himself and wrote the clear text).
  - Musculus → Blarer 1554 (printed by Schiess).
  - Ilten 1741-46. Already done: `targets/ilten1697`, plus the 1743 letters noted in CATALOGUE.md.
- **Archivportal-D.** Archivportal-D (archivportal-d.de, read with the built-in browser) indexes the Bayerisches
  Hauptstaatsarchiv and the other state archives. "chiffriert" returned 171 records; the first 200 slots were read and
  produced **6 rows**. The strongest is the Saxon Knorre ciphers of 1462-63.
- **Other Archivportal-D hits, listed and not rowed:**
  - Gemingen → Lucchesini 1787 (deciphered).
  - Boehmer → Lucchesini 1787, "weitgehend chiffriert" (LAV NRW W V 061, 126).
  - Hohenlohe agent Melchior in Vienna 1679-80 and 1689 (HZA Neuenstein Sf 35 Bü 161, 165).
  - Baden-Durlach Reichstag reports 1758 (GLA 50 Nr. 924).
  - Intercepta 1704 of Markgraf Ludwig Wilhelm (GLA 46 Nr. 3885-3886, Chamillart and Marsin items "chiffriert").
  - Freitag 1687-88 (NLA HA Dep. 1 Nr. 137/4).
  - Degenfeld-Schomburg in Munich 1845-46 (HStA Stuttgart E 50/05).
  - Lepsius 1916-18: name codes only.

  A dedicated Archivportal-D sweep, with all 171 "chiffriert" hits plus "Chiffre", "Geheimschrift" and "Ziffern", would
  likely give 30 more rows.
- **digitale-sammlungen.de** (BSB/MDZ). The JSON API is `/api/search?handler=simple-metadata`. "Geheimschrift"
  returned 19 metadata hits and "Chiffre" 22, almost all printed books. The handwritten hits were Fontana's
  Bellicorum instrumentorum (already solved), a 9th-century Bamberg codex (out of scope) and music. Dead end: the BSB
  Cgm/Clm descriptions are not indexed for cipher terms.
- **gda.bayern.de and bavarikon.** Not reached as separate portals. BayHStA finding aids are in Archivportal-D, where
  the only BayHStA hit was a 1915 telegram file. Kurbayern Äußeres Archiv 4591 is already in the repo (kaa4591).

### 3. Paris: FranceArchives and the Archives nationales

- **Access.** FranceArchives blocks plain HTTP clients: curl gets a 262-byte bot-check page. It was read through the
  built-in browser with in-page `fetch` of `/fr/search?...&page=N` and of each `/fr/facomponent/<hash>` notice.
- **Terms and hit counts.**

  | Term | Hits |
  |---|---|
  | "lettre chiffrée" | 290 |
  | "partiellement chiffrée" | 80 |
  | "partie chiffrée" | 78 |
  | "non transcrite" | 23 |
  | "non déchiffrée" | 20 |
  | "lettres chiffrées" | 20 |
  | "non déchiffrées" | 18 |
  | "non déchiffré" | 15 |
  | "dépêche chiffrée" | 14 |
  | "dépêches chiffrées" | 13 |
  | "chiffre non" | 12 |
  | "non déchiffrés" | 5 |
  | "pas déchiffré" | 4 |
  | "passages chiffrés" | 4 |
  | "sans le déchiffrement" | 1 |
  | "déchiffrement manque" | 2 |

  Full notices were fetched for about 140 items. **23 rows.**
- **Archives nationales coverage.** FranceArchives covers the AN item-level inventories (AE/B/I consular
  correspondence, AF/III, AF/IV, the AP private archives, AB/XIX, MAR), ANOM, SHD, CADN and the departmental archives.
  The AN's own SIV was not queried separately, because FranceArchives carries the same item-level notices.
- **How the AE/B/I inventories read.** They analyse almost every "lettre chiffrée", which means a decipherment was
  bound in. Only the letters explicitly flagged "non déchiffrée", "non transcrite" or "le déchiffrement manque" were
  kept. Their deciphered siblings in the same volumes give class A.
- **Already covered elsewhere:** BnF (huge repo coverage), Nièvre du Croc, the Villeneuve 1737 target
  (`targets/villeneuve1737`), La Fin (SOLVED_CATALOGUE) and Bossuet (`targets/bossuet`). Rows that share a writer with
  a repo target say so.

## Best leads (ranked)

1. **Caulaincourt → Napoleon, Châtillon congress, Feb-Mar 1814** (AN AF/IV plaquettes 4/III and 4/IV), class A.
   - Three letters are ciphered "sans le déchiffrement".
   - Four cipher + déchiffrement pairs sit in the same plaquettes.
   - The weak point: Fain or Houssaye may print the clear texts.
2. **Maximilian I's envoys, 1510-1516** (HHStA RK Maximiliana: de Burgo, Veit von Fürst, Paulus de Laude, Gattinara,
   Colla), class A.
   - About 25 partly ciphered reports, with images online in AIS.
   - De Burgo's glossed 1511 letters give the key.
   - The 42-1-9 "Chiffrierte Schreiben" file is the fully ciphered follow-up (separate row).
3. **Knorre and Schenk → Duke Wilhelm III of Saxony, 1462-63** (SächsHStA Dresden, Loc. 4356/01), class A.
   - About 12 sheets "vollständig" or "größtenteils chiffriert"; one is partly deciphered.
   - Very early German diplomatic cipher, no edition found.
   - Not on DECODE. Of interest to `research/oldest/` (post-1435, so not an oldest-cipher candidate).
4. **Hieronymus Łaski → Ferdinand I from Constantinople, 1540-41** (HHStA Türkei I 5-1/5-2), class B.
   - About 10 ciphered letters, digitised.
   - The repo has Łaski's 1531 key (kaa4591) as a first test.
5. **Habsburg resident ciphers at the Porte, 1530-1555**, class A, all digitised.
   - Malvezzi's circle 1547-50: "Inhalt nicht dechiffriert", plus Veltwyck and the "vollständig chiffrierte Briefe".
   - The Ragusa network 1530-32 and Ferducci 1542-43.
   - The Amasya letter of 1555 "keine Dechiffrierung vorhanden!".
   - Glossed siblings exist in each run, and the repo's malvezzi1548 key applies.

Next in line:
- Ferdinand III → Holzapfel and Traun 1647-48, "ohne Klarschrift", with glossed siblings.
- Sieyès's Berlin mission 1798-99: Konstanz plus AN 284AP/12.
- Donzelot → Andréossy 1813, which the Vienna cabinet failed on.
- St Petersburg and Constantinople consular letters "non déchiffrés", including Villeneuve 1737 with the repo key.
- Martinique 1761, digitised on ANOM.

## Key leads (bare keys or tables, not rowed)

- **HHStA Ungarische Akten 425-24.** 1528 cipher alphabet of King John I and Hieronymus Łaski
  ([AIS 3383443](https://www.archivinformationssystem.at/detail.aspx?ID=3383443)).
- **HHStA StK Interiora Kt. 13-14, "Chiffrenschlüssel".** Keys from 1530 to 1775: Zifra Johannis 1530, Nogarola 1533
  "Zifra antiqua/nova", a French key of 1761. Most are listed in Cryptoole (`research/cryptoole/snapshot.json`).
- **HHStA Ungarische Akten 327-4.** "Schlüssel zu verschiedenen Chiffres" 1664-68.
- **Other HHStA keys:** RHR Kriegsakten 109-24 and 109-89 (1642, letter with a key enclosed); Nachlass Hallwich 12-10
  (copy of Schwarzenberg's key to Aldringen); KA Nachlass Kolbielski 4-19 (assorted keys, Bardaxi notebook); RK
  Ministerialkorrespondenz 2-1-2 (Cobenzl 1741, letters with an "Entschlüsselungscode").
- **Vienna police keys (AVA Inneres PHSt), 1807-1819.** Keys for confidants: Kerpen 1809, Beckers, Buck, Stephing,
  Fernau.
- **Archives nationales, Fersen papers 4410AP/1.** Marie-Antoinette → Fersen copies "avec la clé dans l'interligne".
  Already studied: Lasry et al.
- **Kalliope.** Bernoulli's "Clé du chiffre de J. R. v. Patkul" (UB Basel, Bernoulli papers).

## Dead ends and cautions

- **AVA Verkehr.** "Chiffre" there means file numbers or telegraph codes of the railway administration (about 1,100
  hits).
- **HHStA Coburg and Braun telegrams, 1887-1901.** Chiffre-Telegramme are copies already in clear (Nl Braun 19-1-48
  to 118).
- **Türkei I, 1553-57.** Dozens of "chiffriert und interlinear dechiffriert" items (Vrančić, Zay, Busbecq, Cernovich).
  They are kept only as sibling keys.
- **"Nathan von Dortmund (chiffriert)" (LAV NRW OWL L 74).** May be name-codes only; scored low.
- **FranceArchives "non déchiffré".** Most hits are photographs and signatures. Only the AE/B/I, AF/IV, ANOM and CADN
  ones are ciphers.

## Not reached

- AN SIV queried directly. FranceArchives was used instead.
- bavarikon and gda.bayern.de as separate portals.
- Archivportal-D beyond the first 200 "chiffriert" slots, and no other Archivportal-D terms.
- HHStA Staatenabteilungen beyond the term searches: Spanien Diplomatische Korrespondenz, Rom, Venedig. No AIS item
  records turned up for Große Korrespondenz with cipher terms.
- Prior-art checks were quick web searches for the top items only (Caulaincourt, Knorre, Łaski, Bouillé). Every row
  says what was checked.

## Scripts

- `ais_search.py`, `ais_harvest.py`, `ais_details.py`: AIS full-text search, paging and detail extraction.
- `kalliope_sru.py`: Kalliope SRU harvest (MODS).
- `build_candidates.py`: writes `candidates.json`.

Raw harvests (jsonl) were kept in the session scratchpad and not committed.
