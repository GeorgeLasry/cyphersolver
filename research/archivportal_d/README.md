# Archivportal-D sweep (26 Oct 2026)

Full sweep of Archivportal-D (the archives sector of the Deutsche Digitale Bibliothek) for cipher terms, following
`research/archive_sweep_2026-10/BRIEF.md`. It finishes the work that `research/central_archives/` began: that sweep read
only the first 200 hits for "chiffriert".

`candidates.json` holds **60 rows**. Runs of one correspondence are grouped into one row. Every row was scored from the
finding-aid description alone (`seen: "catalogue"`); no scan was viewed. 13 rows are digitised in the Archivportal-D/DDB
viewer. `build_candidates.py` writes the file and is the place to edit rows.

## Method

- **Endpoint.** The DDB Solr index is public and needs **no API key**:
  `https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select?q=<term>&rows=500&start=N&wt=json`.
  (The old `api.deutsche-digitale-bibliothek.de/search` route returns 403 without a key.) `q` searches title,
  description and context; stemming merges Chiffre/Chiffren/chiffre/chiffré. `sector_fct:sec_01` is the archives
  sector (= Archivportal-D). Item pages: `https://www.archivportal-d.de/item/<id>`.
- **Script.** `ddb_harvest.py OUT.jsonl` harvests every term (all sectors), dedups by id and records the hitting terms.
  The raw harvest (3,627 unique records) stayed in the session scratchpad.
- **Terms and hit counts** (all sectors; Solr stems, so several share counts):

  | Term | Hits | Term | Hits |
  |---|---|---|---|
  | chiffriert | 183 | Geheimschrift | 539 |
  | chiffrierte | 174 | "in Ziffern" | 92 |
  | chiffrierten | 99 | verschlüsselt | 152 |
  | chiffrierter | 56 | verschlüsselte | 251 |
  | Chiffre / Chiffren / chiffre / chiffré | 832 | Chiffrierschlüssel | 27 |
  | Chiffern | 73 | Chiffrenschlüssel | 12 |
  | dechiffriert | 28 | "mit Chiffren" | 46 |
  | dechiffrierte | 16 | "in Chiffren" | 18 |
  | Dechiffrierung | 115 | "in Chiffern" | 51 |
  | entziffert | 109 | cifra | 305 (mostly music/library) |
  | Entzifferung | 410 | chiffrée / chiffrées / chiffrés | 41 / 14 / 190 |
  | Geheimzeichen | 45 | Kryptogramm | 18 |
  | Geheimtinte | 19 | Ziffernschrift / Chiffreschrift | 5 / 9 |
  | Zifferschrift, Ziffernbrief, Dechiffrat, cifrato | 0 | Chiffrebrief(e), Zifra, Ziffernschlüssel | 2 / 1 / 1 |

- **Filter.** Archives and library manuscripts, dated 1400-1950 or undated, with a cipher word in title, description
  or abstract: 1,460 records, all read as one-line listings; about 250 full descriptions read. Noise: Bundesarchiv
  20th-century administration (233), forestry/finance "Entzifferung" (= breakdown of figures), music "basse chiffrée",
  newspaper "Chiffre-Anzeigen", royal monogram "Namenschiffre", GLA 69 Sammlung 1995 D addresses, WWI army
  Geheimschrift manuals and prisoner-of-war secret-ink files.
- **Dedup.** Every row checked with `known.py` and against `research/central_archives/candidates.json` by shelfmark.
  Dropped as already held: LASH Abt. 8.1 Gottorp files (catalogue #530; the extra numbers are a separate row marked
  "extends #530"), Pechlin → Dumont (LASH 399.89 Nr. 18), Charles X Gustav → Müller (GStA IV. HA Rep. 15 B 274),
  Ernst Ludwig's diaries (D 4 Nr. 343/1), Knorre sheets of Loc. 4356/01, Nathan von Dortmund (L 74), Reichenau 1653
  (GLA 96 Nr. 1179), Kurbayern Äußeres Archiv 4591 (targets/kaa4591). None of the kept rows is on DECODE.
- **Prior art.** Quick web searches for the top rows (Teutonic Order 1519, Heinrich of Brunswick, Nassau, Ehingen,
  Grumbach) found no published decipherment; each row says what was checked and which edition to try next.

## Best leads (ranked)

1. **Teutonic Order, Grand Master Albrecht's cipher, 1514-1524** (GStA PK XX. HA OBA; four rows). Dietrich von
   Schönberg, Joachim I of Brandenburg, Heydeck/Isenburg/Schönburg in the 1520 war, and Schönberg → Gundelfinger at
   Lyon 1524. Many letters "in Chiffern; dabei Auflösung" next to ones with none, and OBA 26859 holds the alphabet
   itself: class A. Check Erich Joachim, *Die Politik des letzten Hochmeisters* (1892-95) for printed resolutions.
2. **Willem Lodewijk of Nassau ↔ his brothers, 1605-1620, "zumeist verschlüsselt"** (HHStA Wiesbaden 171 S 995),
   digitised, with three digitised Nassau key files in the same Bestand. Highest solvability.
3. **Saxon 15th-century pieces** (Wittenberger Archiv): Bl. 252 of the Knorre volume, Brussels embassy news 1463,
   Delniczer → Schlick 1471, Hungarian-Polish war insert. Very early; siblings of the Knorre row.
4. **Heinrich the Middle of Brunswick-Lüneburg, 1518-22, in Geheimschrift** (NLA HA L 1 Nr. 548, 562), digitised;
   the Hildesheim Stiftsfehde and the 1519 election.
5. **Grumbach letters and ciphers, 1551-66** (GStA GR Rep. 39; HStA Dresden Loc. 4414/04, digitised), and the Peasants'
   War letters "in Chiffren" of Rudolf von Ehingen, April-May 1525 (HStA Stuttgart H 54).

Next: Zápolya/Łaski ↔ Philip of Hesse with key (Marburg PA 2985, test the kaa4591b key); Ferdinand III → Hatzfeldt
1633-57 (Neuenstein Ni 10; test the ferdinand3 alphabets); Gyllenstierna and Charles XII with key (NLA Stade Rep. 5a,
digitised); Hanoverian Mecklenburg-commission ciphers 1729-61 (Hann. 9g, digitised); Mörmann's Vienna reports with
cipher table (BayHStA, digitised); Stein at Mainz and Lucchesini 1786-91 with keys; French intercepts of 1703 (GLA 46
Nr. 3886).

## Key leads (bare keys, not rowed)

- GStA PK III. HA MdA ZB Nr. 73/1-7, 76, 76/1, 102, 109, 110 and MdA I Nr. 1856-8808: Prussian legation and mission
  ciphers 1806-1846, incl. "Chiffren der französischen Kundschafter unter Napoleon" (I Nr. 8808) and an 1858 offer of
  the French legation's key (I Nr. 8881). I. HA Rep. 81 legation files: Mainz Nr. 5, 20; Rastatt Nr. 18 (Sandoz-Rollin
  1796-97); Köln Nr. 1 (Rohd 1736-46); Florenz/T Nr. 4; Kassel Nr. 7; Konstantinopel IX Nr. 20, 22; Madrid Nr. 100;
  Vatikan Nr. 2. I. HA GR Rep. 41 Nr. 145 (Klinggräffen 1746-47). I. HA Rep. 7 C Nr. 3145 (Polish insurgents' keys
  1797-98). I. HA Rep. 77 Tit. 437 Nr. 6 (+ Adh.): decipherment of French ciphers 1809-33.
- Landesarchiv BW, GLA 48 Nr. 65-84 (Baden ciphers 1599-1893, incl. Hermann of Baden-Baden 1599, Edelsheim 1759-61),
  GLA 46 Nr. 3242 (Ferdinand Maximilian), GLA 77 Nr. 1131 (1745), GLA 52 Hennenhofer Nr. 49; HStA Stuttgart E 59 Bd.
  232-242 (Württemberg code books 1846-70), L 6 Bü 407, J 2 Nr. 10 (copies of Munich and Marburg keys 1530-34),
  A 2 Bü 9-11 (1534 letters "in Geheimschrift, mit Transkription": a ready sibling key), HZA Neuenstein Oe 1 Bü 18778,
  Sf 35 Bü 226; Staatsarchiv Wertheim F-Rep. 90N Nr. 106; Staatsarchiv Ludwigsburg B 137 Bü 588 (Schmalkaldic League).
- Hessen: HHStA Wiesbaden 150 Nr. 787, 151 Nr. 902, 171 C 667, K 569, Z 1807, A 615; HStAD D 4 Nr. 141/2, 239/1,
  301/6, 588/5, 778/3 (Grand Duchess Mathilde); HStAM 3 Nr. 1491, 1495.
- Sachsen: HStA Dresden 10024 Loc. 08233/05, 08236/05-15, 08285/18 (Hesse-Darmstadt alphabet 1639-40), 08485/04;
  10026 Loc. 03233/01-07, 03234/01-07 (Flemming and cabinet ciphers), 00663/01 and 02684/08 (Instructions et
  Chiffres, Debrose 1720, Brühl 1769), 00694/10 (Krauske's 1893 decipherments of Manteuffel → Flemming 1712-13),
  30004/01, 30347/02; Rötha 2423.
- Sachsen-Anhalt: Z 18 A 9a Nr. 1/0 and A 19 Nr. 5 (Christian I of Anhalt-Bernburg's ciphers 1608-27); Z 44 A 9b Ib
  Nr. 13 (1745 tables); A 1 Nr. 530 (key used by the Osnabrück peace envoys, 1643-47, digitised).
- Elsewhere: LAV NRW AA 0031 Nr. 1938, 2041, 242 (Jülich-Berg 1539, 1594-1605), AA 0606a Nr. 311, W 005 Nr. 475, 499 a
  (Münster, digitised), L 77 A Nr. 7520 (Lippe Bundestag key 1825-26, digitised), RW 1167 II 44 (18 Virmond keys);
  NLA HA Rep. 241 E 16-17 (East Frisian ivory cipher table 1727), Hann. 92 Nr. 1983 (Guydickens 1738-39); NLA OL
  Best. 20-10 Nr. 69; Staatsarchiv Nürnberg Ansbacher Historica 279 (Chiffres de Vienne et de Berlin); Staatsarchiv
  Hamburg 132-5/10 A 6 (1819-20); Stadtarchiv Worms 159 Nr. 0778 (Duc de Dalberg); Archiv der Hansestadt Lübeck
  01.1-03.05 Nr. 134, 155; Bundesarchiv N 1007/1589 (1890).

## Dead ends and cautions

- "(De)chiffriert", "mit Auflösung", "mit Transkription" items were dropped as targets and kept only as sibling keys
  (Frederick II → Klinggräffen/Voss/Maltzahn 1743-56 "mit Auflösung", GStA Rep. 81 Dresden Nr. 781-791; Degenfeld 1844-46
  "mit Aufl."; Busbecq 1581/1588 "chiffrierte und dechiffrierte"; Alix of Hesse's Geheimschrift album, with key).
- Name codes only, not rowed: Lippe Pauline ↔ Treitlinger 1806-10 (person-cipher list), Schaumburg-Lippe 1761, Frederick V
  of Bohemia → Rusdorf (Heidelberg), Nuremberg "L und L" spy 1514, Hogguer "Marie" letters.
- Secret ink / WWI: BayHStA Stv. GK I. AK 1411-1420, GLA 456 F 9, BArch RM 86 copies, all transcribed or chemical.
- DSHI 110 Liphart II 4-2 "Ferdinand 1533 (Text noch nicht entziffert)" probably means unread handwriting; unchecked.
- Most hits carry no item-level date or folio for the cipher; ciphered amount is unknown for nearly every row.

## Not reached

- The DDB item/IIIF endpoints for page images were not used; no scan was looked at.
- Archive-own portals with deeper indexing than Archivportal-D (Landesarchiv BW OLF, Arcinsys Hessen/Niedersachsen,
  GStA's own database, HStA Dresden) were not queried separately; their item descriptions are mostly mirrored here.
- Prior-art checks beyond quick web searches (Joachim 1892-95, Ortloff 1868-70, Groen van Prinsterer, Politische
  Correspondenz, Baumann 1877).

## Scripts

- `ddb_harvest.py`: DDB Solr harvest of all terms.
- `build_candidates.py`: writes `candidates.json`.
