# South Cone and Andes archives sweep (28 Oct 2026)

Region "Americas": Argentina, Chile, Uruguay, Paraguay, Bolivia, Peru. A sweep of the online catalogues of the
national archives and libraries for ciphertexts not yet in the catalogue. **23 candidate rows** in `candidates.json`
(built by `make_candidates.py`; edit that file, not the JSON). One was viewed on the scan; the rest are scored from
item-level catalogue notes.

This builds on the unfinished probe in `research/canada_latam/` (Biblioteca Nacional Digital de Chile, Memoria
Chilena, World Digital Library). Its hit lists were re-read first: the BND Chile and WDL hits are all noise (Borges's
*La cifra*, census figures, printed books, nothing for the region in WDL), and Memoria Chilena returned nothing.
Those portals were not searched again.

## Method

| Source | Route | Terms | Result |
|---|---|---|---|
| Archivo Nacional de Chile, Aleph catalogue on bncatalogo.cl (bases ARNES "Archivo especial", ARCHIVO_NACIONAL general, ARNHI, ARNIT, ARNGB, ARNNT, ARNCV, ARNFO, AFL, ASM) | `aleph_cl.py`, `aleph_cl2.py` (plain HTTP; permalinks `?func=direct&local_base=ARNES&doc_number=`) | cifra, cifrada, cifrado, cifr?, clave, clav?, claves, descifr?, criptogr?, jeroglifico, reservado, codigo, numeros, signos, simpatic?, convencional? | **Productive.** ARNES has item-level records for the Archivo Santa María (President Domingo Santa María, War of the Pacific) and the Archivo Fernández Larraín. `clave` = 195 records (`arnes_clave.json`, filtered in `arnes_clave_open.txt`): 142 cipher telegrams 1879-1886 with transcription attached, about 20 without, 2 key sheets. `cifra` and its forms are almost absent: Chilean cataloguers write "en clave". The general base adds volume-level "criptogramas" (Antofagasta 1926-40). |
| Biblioteca Nacional de Chile, Aleph base BNC01 (manuscripts: Sala Medina, Balmaceda and Carrera papers) | `bnc.py` (full records + any BND link) | "texto en clave", "escrito en clave", "clave manuscrito", "cifra manuscrito", "en cifra manuscrito", "cifrado manuscrito", "claves manuscrito", "codigo manuscrito", descifrar, criptograma, "telegrama cifrado", "tinta simpatica" | **Productive.** About 140 distinct records (`bnc_all.txt`), most noise (music "clave", "cifra" = figure, textbooks). Real: 1891 civil-war telegrams to Balmaceda in cipher, Balmaceda's own cipher note, Congressist "Marco" telegrams, Orbegoso → Santa Cruz 1837, a cover-name letter with its key, Huneeus 1921, and key sheets (1816 Carrera, 1891 both sides). No digital objects, and BND search finds no scans of them. |
| Archivo Nacional de Asunción (Paraguay), AtoM portals historia.archivonacional.gov.py and riobranco.archivonacional.gov.py (Colección Rio Branco, returned by Brazil 1981, PDFs online) | `atom.py` (generic AtoM scraper; `TERMS` and `SUF` env vars) | cifra/cifrado/cifrada/..., "en cifra", criptograma, descifr*, código, clave, "en números", "carta cifrada" | 1 real hit, Varela → Moreira de Castro 1850, **viewed** (images 41-42 of the file PDF). "Código" otherwise = legal codes. Nine sibling diplomatic files (Gelly in Rio 1849-52, Decoud in Buenos Aires 1853, F. S. López in Europe 1853, Varela → Derqui 1852) were skimmed at thumbnail size: no obvious number runs, but that is not conclusive. |
| Archivo General de la Nación del Perú, AtoM fondosdocumentales.agn.gob.pe | `atom.py` | as above plus espía, seudónimo, interceptadas, "Washington del Sur" | Nothing usable (see "Seen and left out"). Its search is shallow; the portal describes only part of the holdings. |
| AGN Uruguay, inventory PDFs on gub.uy (42 PDFs: Pivel Devoto, Batlle Berres, Assunção, ex-Archivo y Museo Histórico, Archivo Judicial ...) | downloaded to scratch, text-grepped (`uy_pdfs.txt` lists them) | cifr, criptogr, en clave, clave tele, jerogl, tinta simp | Aparicio Saravia folder (1897-1904): one cipher telegram plus the party's keys. |
| Printed archives on archive.org: *Documentos del Archivo de San Martín* (12 vols, 1910-11), *Documentos del archivo de Pueyrredón* (4), *Documentos del archivo de Belgrano* (7), *Archivo Artigas* general indexes (2 vols), *Cartas de Bolívar para Sucre* (1924) | OCR text grep | cifra, clave, descifr | Cipher passages in these editions are printed in clear; nothing flagged undeciphered. Key leads only (below). |
| Wikimedia Commons (Academia Nacional de la Historia Argentina uploads, AR-ANH) | Commons search API | cifr*, clave, "en clave", números | Noise only. |
| Web search (prior art and routes) | WebSearch | San Martín/Pueyrredón/O'Higgins cifra, Bolívar-Sucre, Solano López, War of the Pacific, Piérola, 1891 civil war, Carrera-Didier, Belgrano/Güemes | No published decipherment found for any candidate; also no study of these ciphers at all. |

Dedup: every candidate was run through `research/archive_sweep_2026-10/known.py` (shelfmarks, names: Moreira de
Castro, Varela, Santa María, Piérola, Lynch, Novoa, Rodríguez Aldea, Fernández Larraín, Balmaceda, Carrera,
Orbegoso, Huneeus, Claudio Matte). None is in the repo or on DECODE. The repo's Poinsett (Chile/Buenos Aires
1811-14) and NARA German Lima/Buenos Aires items were not touched.

## Candidates, ranked

1. **Benito Varela (Paraguayan foreign minister) → Manuel Moreira de Castro, Rio, 13 Feb 1850**, ANA-AHRP-PY-558-1-31
   item 13 (ex BN Rio I-29,25,23). Viewed: a clear letter with about 12 runs of dot-separated numbers (1-116), 60-80
   tokens, on Brazil, Rio Grande and Buenos Aires. The ANA cataloguer could not read it. Scans online. The only
   lead here that can be worked today.
2. **Piérola's letter-book, Lima, 8 Apr - 31 Dec 1880, 62 pp., "Texto en clave"**, Archivo Santa María A6000. The
   largest item: a Peruvian wartime cipher in Chilean hands. Not online.
3. **Archivo Santa María cipher telegrams with no transcription** (8 rows): Lynch → Santa María 1882-84, Novoa 1883
   and 1884, Pinto → Santa María 1879, Huneeus 1879, anonymous Lima → Balmaceda 1883. Class A on paper: the fonds
   has 142 transcribed siblings and two key sheets (below). Not online.
4. **1891 civil war, Biblioteca Nacional de Chile**: Villegas (Antofagasta), Vicuña Guerrero (Valparaíso), Viel,
   Morán/Jarpa telegrams to Balmaceda; Balmaceda's own cipher note; "Marco" → Claudio Matte, Berlin (22 ff.). The
   Villegas openings quoted by the cataloguer ("Y j h _ t v t b...") show a letter cipher in clear text. Congressist
   key sheets are in the same library; the government key is not catalogued, except Viel's "código Oscar"
   explanation of 9 Jun 1891.
5. **Orbegoso → Andrés de Santa Cruz, Lima, 18 Oct 1837** (Peru-Bolivian Confederation, contemporary copy, part in
   cipher), and **Rodríguez Aldea → O'Higgins** (Archivo Fernández Larraín vol. 39 p. 15, partly in cipher).
6. Lower: the cover-name letter "La Estrella de la Banda Oriental..." with its key (BN Chile sys. 000103674); the
   Aparicio Saravia cipher telegram (AGN Uruguay, with the party key); Antofagasta "criptogramas" 1926-40; Huneeus,
   Paris, 23 Mar 1921.

Most rows have solvability 1-2 only because nothing is online: they need a scan request to the Archivo Nacional or
the Biblioteca Nacional in Santiago. With scans, the Santa María and 1891 telegrams are probably quick reads
(codebooks or short letter ciphers, with sibling transcriptions and key sheets in the same fonds).

## Key leads (bare keys, no ciphertext)

- Archivo Santa María A3039 (sys. 000003039), "Código para escribir en clave" (ca. 1880, 1 p., subject CIFRAS Y
  CLAVES), and B4931 (sys. 000014931), "Claves telegráficas a utilizar con Lynch, Altamirano, Novoa y todas las
  legaciones chilenas en el extranjero" (ca. 1883, 10 p. + envelope, with drafts). These should read the
  untranscribed telegrams and any Chilean legation traffic of 1883-86 found elsewhere (NARA, FO intercepts).
- Archivo Santa María sys. 000017188: Manuel José Soffia, Jefatura Política de Tacna y Arica → Santa María,
  23 Mar 1884, "Adjunta clave telegráfica".
- BN Chile, 1891: "[Códigos y claves antibalmacedistas]" (3 ff., sys. 001156140); "[Códigos y claves de grupo
  congresista]" (sys. 001156145); Legation list "de las palabras de las claves enviadas a París", 15 Jun 1891
  (sys. 001083798); Oscar Viel → Julio Haase, 9 Jun 1891, details of the "código Oscar" and how to decipher it
  (sys. 001081115); Ricardo Escobar's 14 Apr 1891 copy of a telegram in the "darhan" key (sys. 001060882); Pedro
  Montt, 9 May 1893, mentions "el diccionario en clave" (sys. 000857678).
- BN Chile, José Miguel Carrera: "[Claves] 1816 marzo 31, New York" (A B C D ..., Hoja 29614, sys. 001176896) and
  Carrera → Henry Didier, Baltimore 25 Nov 1816, revealing a key and a cover name (Hoja 29598, sys. 001176840); an
  undated "[Clave]" A B C D ... (Hoja 29674, sys. 001177066). Carrera's 1816-18 letters from the US and Buenos Aires
  (some at BN Chile and on microfilm) may contain cipher in this key; none was flagged as unread.
- AGN Uruguay, Pivel Devoto: Partido Nacional keys of 1897 and 1904 (Saravia folder docs. 13, 45, 48; section 33.7
  "Claves utilizadas en 1897 y 1904"; section 16.4 "Claves utilizadas durante la revolución"; Luis Mongrell 1904
  doc. 17 "Claves: Para cifrar - Para descifrar"; "Clave de frases con el Departamento de Colonia"); "Juego de claves
  telegráficas para uso del Cuerpo Consular" in the ex-Archivo y Museo Histórico inventory.
- Printed San Martín archive: vol. 3 (a captured royalist "clave", copy sent to the Director; the instruction to use
  sympathetic ink instead of the "clave"), vol. 5 (royalist spies' cipher A=1, B=2 with commas and null dots), vol. 7
  (1821 Peru instructions: commissioners write "con la cifra del librito" or with a cut-out grille; commanders of
  the Sierra and Huanta given keys nos. 1 and 2), vol. 6 (a letter of "J. M." with cipher lines ordering San
  Martín's assassination, read with a "cartilla"). *Archivo Artigas* prints "en clave" items of Sandabuny 1812 and
  Curado 1819 (Spanish and Portuguese originals, outside this region).

## Seen and left out

- 142 Archivo Santa María telegrams with "adjunta transcripción" (read at the time); Gana, Rio/Petrópolis 1885, and
  Novoa, Lima 6 Aug 1884, which have the clear text with the cipher copy; Aldunate Carrera, Lima 1 Oct 1883
  (transcribed).
- AGN Peru PE AGN 06.2-G4-CO-SM-11-717: a spy report to Sucre ("Washington del Sur") on Viceroy Pezuela, signed with
  the sorted-letter anagram "aaacdeeeijmnoorrs". Only the names are coded; the body is described in clear. Worth a
  line in a cover-name study, not a ciphertext row.
- BN Chile: Lynch → del Canto 1883 (asks to send messages *without* cipher); Carvallo Orrego 1891 (says he lacks the
  key of the president's message: no ciphertext in the item); Havas → E. Matte 1891 and an unsigned telegram of
  10 Apr 1891 (cipher with translation included); Ross → Montt 1892 London (translation of a cipher telegram);
  1962 cables "para ser transmitido en clave" (clear drafts, after 1950).
- AGN Uruguay, Assunção inventory: Carralón 1885 notes "con información sobre telegramas en clave" (about, not in,
  cipher).
- Printed editions (San Martín, Pueyrredón, Belgrano, Artigas): passages printed in clear.

## Blocked or not reached

- **Bolivia, ABNB** (archivo-abnb.org.bo): Cloudflare challenge in both curl and the built-in browser; not passed.
  digital.biblioteca-abnb.org.bo not tried.
- **British Library EAP** (eap.bl.uk; EAP1495 is a Peruvian project): human-verification wall; web search with
  `site:` returns nothing.
- **Peru, Biblioteca Nacional** (bibliotecadigital.bnp.gob.pe, catalogo.bnp.gob.pe): no DNS / refused from here and
  in the browser. **AGN Peru** main site 406/500; only the AtoM portal works.
- **Argentina**: no item-level online catalogue found for the AGN (Sala VII, Sala X); Museo Mitre and the Academia
  Nacional de la Historia sites return 403; Trapalanda (BN Mariano Moreno) unreachable; the BN Aleph catalogue
  (catalogo.bn.gov.ar) answered but its result counts were not usable; the Cancillería archive has no online
  catalogue. Argentina is the largest gap of this sweep.
- **Chile, Archivo Nacional "documentos" portal** (documentos.archivonacional.cl) requires a ClaveÚnica sign-in;
  not used. Ministerio de RREE archive (minrel.gob.cl) 403.
- **Uruguay**: AGN and Museo Histórico Nacional sites unreachable; only the gub.uy inventory PDFs were used.
- Not done: War of the Pacific Peruvian and Bolivian archives (no catalogue online), Paraguayan-war intercepts
  beyond the ANA portal, a full look at the López-era Rio Branco files' PDFs (about 100 diplomatic files could
  hide more numeric cipher like the Varela letter), the *Colección Documental de la Independencia del Perú* and
  the printed *Archivo de don Bernardo O'Higgins* (not found on archive.org).

## Files

`aleph_cl.py`, `aleph_cl2.py` (Archivo Nacional de Chile Aleph), `bnc.py` (BN Chile manuscripts), `atom.py` (any
AtoM portal), `make_candidates.py` (writes `candidates.json`); raw hits in `arnes_*.json`, `arn_*.json`,
`bnc_*.json`, `atom_hits_*.json`; `arnes_clave_open.txt` and `bnc_all.txt` are the filtered reading lists;
`uy_pdfs.txt` lists the AGN Uruguay inventory PDFs. Page images and PDFs were kept in the session scratch directory,
not in the repo.

`needs_archive_scan` and `access_note` were added to each row at the merge (28 Oct 2026), from the row's own description; re-running the build script drops them.
