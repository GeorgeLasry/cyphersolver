# Colombia, Venezuela, Ecuador, Caribbean and Central America sweep (28 Oct 2026)

Scope: region "Americas": Colombia, Venezuela, Ecuador, Cuba, the Dominican Republic, Puerto Rico and Central
America. **10 candidates** in `candidates.json` (built by `make_candidates.py`). All are `seen: catalogue`. Only
image 1 of the López Méndez unit was glimpsed, and the cipher page was not reached. Almost all the yield comes
from one source: AGN Colombia's new DataViva platform. Gran Colombia records (Venezuela and Ecuador 1819-30) are
in it too.

## Method

### AGN Colombia, DataViva (the main route)

- The AGN's old "Archivo Digital" host no longer exists (`consulta.archivogeneral.gov.co` gives NXDOMAIN). Its
  successor is **DataViva**, `https://dataviva.archivogeneral.gov.co` (Next.js app, about 25 million images,
  launched Oct 2025). The AGN home page links it only through a video.
- The public JSON API was found from the app's own requests and needs no login:
  - search: `POST /api/search/public` with the body in `dataviva.py`: every `post_type`,
    `status: published`, `keyword`, root `66acc915a58c7bfd59b83353`; up to 100 results a page;
  - record: `GET /api/resources/public/details/<id>` gives the full ISAD fields (scope and content, folios, parents)
    and `filesObj`, the list of images;
  - viewer: `https://dataviva.archivogeneral.gov.co/explore/agn/detail/<id>` (record page) and
    `/gallery/<id>?index=<n>` (images).
- Search behaviour: the keyword is stemmed and fuzzy ("cifra" = "cifras" = "cifrado" = "cifradas": all 33 hits),
  and a multi-word keyword is ANDed. The words of descriptions are searched, not the images.
- Scripts in this folder:
  - `dataviva.py` runs the searches and writes `dataviva_hits.json`;
  - `show.py` lists the hits;
  - `ctx.py` / `details.py` print a record's scope text around a regex;
  - `triage.py` fetches the details of every hit of the given searches and keeps those whose scope text matches a
    cipher regex. It caches the details in `details_cache.json`, which is git-ignored with `dataviva_hits.json`.
    Its output is `triage_out.txt` / `triage_out2.txt`.
- Terms searched:
  - cipher terms: cifra / cifrada / cifrado / en cifra (33 hits, one stem), descifrar, clave (106), criptografía,
    tinta simpática (0), jeroglífico, signos convencionales, telegrama cifrado (9), clave telegráfica (10),
    lenguaje convenido, criptograma (0), cifrario (0), contraseña, código secreto, código telegráfico (39),
    caracteres, signos, nombres supuestos, guarismos (0), letras convenidas, abecedario;
  - secrecy and interception: reservada (1,095), secreto, telegrama reservado, carta reservada, reservadísima,
    interceptada (39), correspondencia interceptada;
  - name and place searches combined with "cifr", "clave" and "secreta": Revenga, López Méndez, Fernández Madrid,
    Gual, Zea, Hurtado, Morillo, Sámano, Montalvo, Nariño, Miranda, Bolívar, Santander, Sucre, Urdaneta, Páez,
    Montilla, Salazar, Restrepo, Mosquera, Obando, Flores, Ecuador, Venezuela, Panamá, Cuba, Guatemala, Londres,
    París, Madrid, Jamaica, Estados Unidos, correspondencia, carta, oficio.
- About 1,330 records were triaged by their full scope text. Most "cifra" hits are numbers ("cifras"), and most
  "clave" hits are "clavos" or "punto clave". About 15 real cipher mentions remain, and they gave the 7 DataViva
  rows.

### Other sources

- **PARES (Spanish state archives).** Region items were taken from `research/pares_ags/hits.jsonl` (title-level).
  The pares sweep ranked them but did not take them as candidates. Each new description fetch got **429** (PARES
  blocks the shared IP), so these rows rest on the titles plus Galende 2000.
- **Galende Díaz, "Sistemas criptográficos empleados en Hispanoamérica"** (Revista Complutense de Historia de
  América 26, 2000, pp. 57-71) was read for leads. It gave the AGI Estado 12 N.14 system and the key leads below.

## Candidates (ranked)

1. **Luis López Méndez (London) → Bolívar, 1819**, AGN Bogotá HISTORIA.SAA-I.17,25,D.24, ff. 222-233. The
   description says part is "bajo el código de una clave secreta". 24 images are online. Imp 4. It may be a
   forerunner of the Revenga 1822 London-Madrid key (`targets/revenga1822`); compare on sight.
2. **Leticia 1932, Gen. Amadeo Rodríguez Vergara fonds** (AGN Archivos Privados GARV). Five imaged units carry
   cipher telegrams; two say "con traducción"; GARV..1.1.4 (1931) holds "la criptografía y descripción de claves".
   Class A, solvability 4.
3. **AGI Estado 12 N.14, Havana 25 May 1819**, Cienfuegos → Casa-Irujo. The vowel-to-digit cipher is described by
   Galende, so a quick full reading is likely. Images are on PARES.
4. **AGI Estado 64 N.46, 1820**, "Expedición a favor de insurgentes de Venezuela y Colombia". PARES says
   "no descifrada". Images are on PARES; the description has not been read.
5. **Ministerio de Gobierno, orden público 1911-12** (SAA-II.23.4.16.3.2). Most telegrams are in cipher, a few
   with translations. Not imaged.
6. PARES 1747718 "Orden Público. Gobierno de Cuba" 1868-78 ("sin descifrar"; signatura unknown).
7. Cúcuta cipher telegrams on Gen. Régulo Olivares (SAA-II.23.4.16.3.1).
8. Ministerio de Gobierno 1932, cipher telegrams on communists and forged notes, with translations
   (SAA-II.23.1.2.28.1.2).
9. Embassy in Lima → Zuleta Ángel 1948, cipher cables on APRA and Haya de la Torre (MRE Transf. 14, VRHT..1.5).
10. Telegraph copies 1907-08 in letter code (probably commercial codes; importance 1).

## Key leads (no ciphertext, or the key is in print)

- **Colombia 1829 monarchy project, cipher notes and their key.** AGN CO.AGN.AO.100.MRE[16]-1.1..43.1 is the
  contract of 11 Jul 1917 between Foreign Minister Marco Fidel Suárez and Roberto Padilla. It pays for four copies
  of "la traducción de las notas cifradas y su clave" in **tomo 490 of the Archivo Diplomático y Consular**: the
  Fernández Madrid (London) and Leandro Palacios notes on the 1829 monarchy plan. A Colombian legation key of 1829
  exists, deciphered in 1917. It is the best lead for the **revenga1822** key (same service, London, seven years
  later). The tomo itself is not in DataViva; it is in the Cancillería's historical archive or the AGN MRE
  "Diplomática y Consular" series.
- **Bákula 1949**, *Apuntes de historia, criptografía y diplomacia de la emancipación* (Lima), prints, after
  Galende, these keys:
  - Bolívar's key (after O'Leary);
  - Sucre's key (substitution with nulls, numbers and word breaks);
  - **Santander's key** (two interleaved half-alphabets);
  - the García del Río-Paroissien mission code of 1822 (409 words as symbols);
  - the first Chilean legation key (1822).

  Any Santander or Bolívar cipher found in Colombia or Venezuela should be tried against them first.
- **Rebeca Rosell, *Las claves de Martí y el plan de alzamiento para Cuba*** (La Habana, 1948) prints Martí's
  keys. The 1895 insurgent ciphers are probably read; check Rosell before cataloguing any Martí or PRC item.
- **Cuba 1872 new cipher key:** AHN ULTRAMAR,4731,Exp.109, 26 Jul 1872, "Remisión a Cuba de la nueva clave y
  cifra reservada" (PARES 6067649). It is the Ultramar ministry key for the Ten Years' War and fits row 6.
- Cienfuegos's 1817 vowel cipher (A=5 E=3 I=1 O=2 U=4; Galende n. 52) is the key for row 3.
- AGN SAA-II.28.14.18.1 (1891), "información de una clave telegráfica": a Colombian telegraph key, not seen.
- AGN HISTORIA.SAA-I.17,28,D.86 (1812, Quito insurgents): "documento sin fecha que contiene el abecedario
  español y algunos nombres masculinos", next to lists of insurgents. It could be a cipher alphabet; 24 images
  online, not viewed.
- Morillo's cipher letters are printed by Rodríguez Villa (already noted by research/europeana); see that README
  before searching Morillo again.

## Seen and left out

- "Cifras" (numbers), "clavos", "punto clave" and Masonic "jeroglíficos" on jewels (Quito 1825) are all noise.
- The Haya de la Torre folders after 1950 (VRHT..11.93, 1954, "traducción de cables cifrados") are past the
  1950 limit.
- AHN DIVERSOS,7,R.2,D.20B "Segunda campaña de Cuba" (1880): it matched "cifrada" in PARES, but there was no
  description to judge it by; it is probably a memoir with statistics ("cifras"). Not kept.
- About 40 AGN "interceptada" units (1809-41): the royalist and patriot interceptions name no cipher.
- Banco de la República digital library (`babel.banrepcultural.org`, CONTENTdm API): 46 collections, among them
  the T. C. de Mosquera correspondence (p17054coll39) and Fondo Acosta Samper. No cipher, clave or cifra in any
  metadata field. Full-text hits are economics reports.
- Biblioteca Nacional de Colombia digital (SirsiDynix `catalogoenlinea`, reached through a browser bot check):
  full-text hits are sheet music ("cifrada" = figured) and printed pamphlets of Fondo Pineda and Quijano. No
  manuscripts.

## Blocked or not reached

- **Venezuela:** AGN Caracas (agnve.gob.ve), the Archivo del Libertador (archivodellibertador.gob.ve) and the
  Biblioteca Nacional did not answer from here. anhvenezuela.org.ve loads but has no catalogue.
- **Ecuador:** the Archivo Nacional (ane.gob.ec, archivonacional.gob.ec) did not answer.
- **Cuba:** the Archivo Nacional (ancuba.cu), BNJM (bnjm.cu) and coleccionesdigitales.ohc.cu (Omeka) did not answer.
- **Dominican Republic:** agn.gob.do returns 403.
- **Puerto Rico:** archivogeneral.pr.gov does not answer; icp.pr.gov returns 406.
- **Central America:**
  - Guatemala: agca.gob.gt did not answer.
  - Honduras, El Salvador and Nicaragua archive sites did not answer.
  - Panama: the ANP site has no catalogue.
  - Costa Rica: the ANCR site loads, but its online database could not be found; only Joomla site search is
    exposed.
- **dLOC / UFDC** is a JS-only app with no API found; it was not searched.
- **PARES:** 429 on every request, 28 Oct 2026, so the AGI and AHN Ultramar descriptions could not be read. A
  region-targeted PARES run when it answers again is the best next step for Cuba, Puerto Rico and New Granada.
  Suggested searches: "cifra Habana", "clave insurrectos", "cifrado Ultramar" and "cifra Santa Fe", in AGI Estado
  and Cuba and AHN Ultramar.
- **Built-in browser:** the pane is shared with other sweep agents and was taken over mid-check, so the images of
  candidate 1 were not read. View its gallery (`/gallery/66b0cd4f151c9d47762a2382?index=0..23`) first.
- **Not done:** reading O'Leary's *Memorias* and Lecuna for the López Méndez cipher; obtaining Bákula 1949 and
  Rosell 1948; the AGN MRE tomo 490.

`needs_archive_scan` and `access_note` were added to each row at the merge (28 Oct 2026), from the row's own description; re-running the build script drops them.
