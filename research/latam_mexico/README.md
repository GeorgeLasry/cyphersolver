# Mexico sweep (28 Oct 2026): CEHM-Carso, AGN México and the Narváez literature

A first sweep of Mexican repositories (new region: Americas / Mexico) for ciphertexts not yet in the catalogue.
**25 candidates** in `candidates.json` (built by `make_candidates.py`), 21 from CEHM-Carso and 4 from the AGN. All
are scored from catalogue descriptions; none was viewed on the image. Every row passed `known.py` with no hit
outside this folder.

## Method

- **CEHM-Carso** (Centro de Estudios de Historia de México, Fundación Carlos Slim; ex-Condumex), `cehm.org.mx/Buscador`.
  The search posts a form to `/Buscador/Resultado` (fields `f_buscar`, `f_Pagina`, `f_NumReg`=100, `f_Orden`,
  `lfor`=F and D, `lcol`=A for the archive); each hit is loaded from `/Buscador/FichaBasica/<n>?Tipo=A`, a stable
  plain-HTML record (used as the row link; it opens with curl). The POST is refused from curl, so the harvest ran as
  `fetch` calls inside the built-in browser and the results were saved to `cehm_hits.json` (1,063 records) and
  `cehm_sintraduccion.json` (208 records); `cehm_show.py` prints them.
  Terms: cifrada (36), cifradas (6), cifrados (74), "claves no descifradas" (9), "clave no descifrada" (4),
  descifrada (12), descifrar (26), alfabeto (6), claves (70), "en cifra" (74), "en clave" (801), "sin descifrar"
  (26). Zero hits: criptografía, criptograma, jeroglíficos, tinta simpática. "cifrado" (2,118) is almost all Reyes
  telegrams of type "telegrama cifrado" with summaries, so instead the id lists of "sin traducción" (2,907) and
  "cifrado"/"cifrada" were intersected: 208 records, of which 52 are cipher telegrams/letters with no translation
  (47 in the Reyes fondo, 4 Limantour).
- **AGN México, Guía General** (`guiageneral.agn.gob.mx`). The search box calls
  `ajax/arbol2.php?id=%23&buscar=<term>` (flat JSON list, not capped) and `ajax/contenido.php?idref=<id>` (the unit's
  description; used as the row link). `agn_guia.py` runs single words (the engine ORs the words of a phrase: "carta
  cifrada" = 71,574 hits) and stores each description in `agn_hits.json`; `agn_show.py` prints them, hiding the
  20th-century DGIPS boilerplate. Hits: cifra 19, cifrada 2, cifradas 2, cifrado 81, cifrados about 1,030, clave
  117, claves 42, cifras 236, descifr* 7, jeroglífico 7, simpática 2; criptografía/contraseña/criptograma/cifrador 0.
  About 750 unit descriptions read in full (`agn_hits.json`); the remaining "cifrados" hits were classified by
  id only: 1,030 of 1,031 are DGIPS files of 1924-1950 with "telegrama(s) cifrado(s)" (one group row), so the
  harvest was stopped there.
  The Guía describes colonial series (Inquisición, Operaciones de Guerra, Infidencias, Historia) mostly at volume
  level, so a cipher inside an insurgent or viceregal file is invisible to this search.
- **Prior art**: Roberto Narváez is the specialist (book *Criptografía diplomática, política y militar en México
  1813-1926*, SRE/AHD 2019, 495 pp., not online; articles in Documenta & Instrumenta 6 (2008), 9 (2011), 13 (2015);
  Historia Mexicana 71:3 (2022), 75:2 (2025)); Ángel & Morales-Luna, "Breve descripción de la criptografía en la
  Revolución Mexicana" (Revista Digital Universitaria 9:3, 2008). The open-access ones were read in full (shelfmarks,
  what is said to be unread). Narváez works mainly from the SRE archive (AHGE/AHDSREM); the CEHM files below are
  cited by him only for the felicista letters of 1921-22.

## Best leads (ranked)

1. **Maderista junta, El Paso, 1911** (CEHM CMXV, González Garza): about 15 coded telegrams left "texto en clave"
   among about 70 "texto en clave y descifrado", plus 21 key sheets (CMXV.16.1557.1) and a typed transcription of 66
   decipherments (CMXV.18.1795.1). Class A, importance 4, solvability 5.
2. **Carranza's 1915 telegrams "en clave numérica"** to Obregón (Estación Trinidad), Pablo González, Sáenz, and
   "en clave de letras" to Arredondo in Washington (CEHM CDLXXX). Class B, importance 4.
3. **Díaz → Bernardo Reyes, about 45 cipher telegrams "sin traducción", 1885-1909** (CEHM DLI), among hundreds of
   summarised siblings; plus Reyes → Díaz untranslated letters of the 1885 Coahuila crisis and López Portillo y
   Rojas → Reyes, July 1909. Class A.
4. **Federal (Huertista) army telegrams "en clave", 1913-14** (CEHM DLXXIII, Rubio Navarrete), with the War
   Ministry's Clave núm. 109 and alphabet/syllable keys filed alongside. Class A, solvability 5.
5. **1825 carta cifrada on a Mexican-Colombian expedition to free Cuba** (AGN Gobernación vol. 85 exp. 2) and
   **Montenegro (New Orleans) → Gómez Pedraza, 1828**, with an undeciphered duplicate (CEHM CCXVIII). The early-republic
   Cuba project in cipher; the 1828 pair can give a key.
6. Others: magonista intercepted letters 1907 (AGN Gobernación vols. 802-803, with a file of their keys); felicista
   code-name letters 1921-22 (CEHM DCXXI, Narváez read three); León de la Barra 1911-13; Pablo González 1913-14;
   Heriberto Jara 1916-17; Second-Empire envoys' clave 1864 (sibling of catalogue 518); Cristero Liga 1927-33;
   José María Calderón's "oficios en clave" c. 1810-23 (AGN fondo Iglesias Calderón); Puente Nacional 1832 parte en
   clave; Oaxaca 1914 telegrams; Limantour 1899-1908; DGIPS telegrams 1924-49.

## Siblings of items already in the catalogue

- Catalogue 518 (HHStA, Almonte and Arrangoiz Geheimschrift 1863): the Arrangoiz/Hidalgo/Aguilar "clave" letters of
  1864 in CEHM IX-1 are the Mexican side of the same imperial legation network (row "Mexican imperial envoys").
- Catalogue 633 (Bazaine cable 1866): no AGN or CEHM original found; Maximilian → Aguilar, Aug 1866 (CEHM
  IX-1.7-8.819.1, 8.832.1) orders news by "telegramas cifrados" over the new Atlantic cable, so imperial cipher
  cables to Rome of late 1866 should exist in the Aguilar papers.
- Catalogue 692 (Obregón ↔ consul Ruiz code telegrams 1921, NARA) and 758 (Coahuila 1906): Mexican state/federal codes
  of the same family as the DGIPS and Reyes telegrams here.
- research/canada_latam already lists the SRE items Michelena 1824, Obregón 1825 and Torrens 1826 (not repeated).

## Key leads (keys without ciphertext; for reading other items)

- AGN Gobernación (127-128), vol. 3, exps. 53-80 (c. 1903-1912): about 25 typed and manuscript keys for political and
  military correspondence: Gen. Mariano Ruiz (1903), Manuel Loya, Corral-Carvajal, Corral-Valle, Gen. Juan A.
  Hernández, Ismael G. Zúñiga, Governor of Morelos-Gobernación, J. Y. Lugo-Gustavo Madero, Pascual Orozco, Madero with
  Cosío Robelo/Vicario/Figueroa/Hay, Sommerfeld, Lindoro Castellanos (Chiapas), Rafael Múzquiz, Emeterio Flores,
  Fidencio Hernández, Manuel Calero, the Rurales inspectorate; exp. 54 (ff. 1-62): keys of army generals and
  Gobernación. Vol. 730 exp. 4 (1898): Rurales cipher keys. Vol. 803 exp. 3 (1907): magonista keys.
- AGN Indiferente Virreinal caja 2610 exp. 026 (1817, Operaciones de Guerra): War Ministry to the viceroy on a
  cipher for Spain-America with the printed "Syllabical and Steganographical Table" (Narváez 2022 studied it; no
  ciphertext found by him). AGN Provincias Internas vol. 244-2 ff. 108-111 (Laffite plans) and the Onís-Cuba
  "contracifras" table (Narváez 2022).
- AGN Gobernación s. XIX, Segundo Imperio (136), caja 38 exp. 99 (Jan-Feb 1866): a clave for the prefects' reserved communications.
- AGN Luis Castillo Ledón exp. 1063 (1930): presidential "cuadro de claves" for Nayarit.
- CEHM CMXV.16.1557.1 (21 maderista/constitutionalist keys incl. "clave de los reyistas"), CMXV.23.2223.1,
  CMXV.34.3409.1 (number-column key, Kraft y Madero 1914); X-1.5.466.1 (Presidential Secretariat "abecedario y su
  clave", 1911); XXI.76.8362 ("Clave con el General en Jefe, Serie A"); LXVIII-1.23.3148.1 ("clave alpha-32");
  DLXXIII.1.28.8-23, 1.28.14-23, 1.29.15-30 (federal army 1913); CLXXXVI.7.632 (Cristero claves 1928); XXI.139.16091
  ("The Nameless" → Carranza, read by Narváez 2015); CDLIV.2a.1910.29.17 (Schwabach number code), 1910.14.199-223
  (name lists with translation, 1914); VII-1.1-4.28 (Antonio Corona → Gen. Adrián Woll, a clave, 1860).
- SRE (from Narváez 2008): AHDSREM exp. 40-2-146 (Tornel nomenclator, Baltimore 1830); leg. 1-1-44 ff. 78-82
  (Alamán-Michelena tables 1824); AHDSREM exp. 11-4-198 f. 11 and L-E-954 II f. 316 (magonista tables, Narváez 2015).

## Seen and left out

- AGN Benito Juárez (242) caja 2 exp. 15 (12 Mar 1872): "comunicación cifrada" to Gen. Ramón Corona whose content the
  record quotes (read). Ángel & Morales-Luna 2008 note Juárez-Vallarta simple-substitution traffic and a press
  article mentions Juárez → José María Mata (Washington, 1858-60) coded letters: not located in AGN/CEHM records.
- CEHM: hundreds of "texto en clave y descifrado" telegrams (González Garza 1911), Reyes and Limantour cipher
  telegrams with summaries, Charles A. Douglas 1915 notes "en clave" with translations (XXI.152.17415), Limantour
  commercial code telegrams with translations; "en cifra" hits that mean a figure or a monogram.
- AGN: "cifra" as number/monogram (Pesas y Medidas punches, "medias con la cifra del Jesús" 1819, poems "de cifra y
  laberinto" 1805), clavichord makers ("hace claves", Inquisición 1789-95), DGIPS "Circulares 104 cifradas sin
  traducción" (1970, after 1950), Colosio access codes.
- No cipher of Hidalgo, Allende, Morelos, Rayón or the Guadalupes turned up in AGN or CEHM records; the Guadalupes
  used pseudonyms ("Número 12", "El Serpentón") and press code (Guedea 1992), and a 2017 Crónica piece reports that no
  insurgent coded messages are known. The Hernández y Dávalos catalogue (PIM-UNAM) searches showed none.

## Not reached / blocked

- **SRE Acervo Histórico Diplomático (AHGE)**: no item-level online catalogue; only PDF guías documentales
  (portales.sre.gob.mx/acervo). This is where most of Narváez's material sits (consular and legation ciphers
  1820s-1926), and his book says what is still unread there.
- **UT Austin Benson** (`collections.lib.utexas.edu`): Anubis bot wall for curl; in the browser its `/api/search` is
  fuzzy and returned no cipher manuscripts (Alamán papers, Comonfort, broadsides; `ut_collections_hits.txt`). The
  Genaro García and Hernández y Dávalos manuscripts are not item-described there.
- **Historia Mexicana** PDFs (Colmex) sit behind Cloudflare: Narváez 2025 (Constitutionalist cryptography 1914-15,
  AHGE) and his 1860-79 military article were not read.
- Universidad Iberoamericana, Colección Porfirio Díaz (Díaz's own keys and cipher telegrams, used by Ángel &
  Morales-Luna); Archivo Histórico de la SEDENA; INAH/BNAH; BNM Fondo Reservado:
  not searched (no item-level online catalogue found in the time available).
- CEHM images ("Formato Digital") need a reader account; nothing was viewed. The CEHM search is a word/phrase index of
  the catalogue summaries, so cipher items described only as "telegrama" are invisible.

`needs_archive_scan` and `access_note` were added to each row at the merge (28 Oct 2026), from the row's own description; re-running the build script drops them.
