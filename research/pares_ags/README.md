# PARES (AGS / AHN) cipher sweep, Oct 2026

Part of the October 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Archive: PARES, the
Spanish state archives portal, mainly Archivo General de Simancas (AGS) Estado, Guerra y Marina, Secretaría de
Estado, and the Archivo Histórico Nacional (AHN) Estado.

## Method

- Search flow (server-rendered; see `targets/toledo1565/NOTES.md`), per term in its own session (cookie jar):
  `GET catalogo/find?nm=&texto=<term>[&anio1=<y>&anio2=<y>]` (always 25 rows), then
  `POST catalogo/SearchController.do?nm=.` with the `formBusqueda` fields `tambloque=100&orderBy=8` (100 rows a
  page), then the displaytag links `SearchController.do;jsessionid=<s>?...&d-2677838-p=<n>` for pages 2..n.
  `sweep.py` in this folder runs one term (optionally one year range), slowly, and appends hits to `hits.jsonl`;
  `run_batch.py` runs a list of term / year-range jobs under one hard request cap (usage in its docstring).
- Terms: cifra, cifrada, "en cifra", "parte en cifra", "sin descifrar", "no descifrada", descifrado,
  "carta cifrada", contracifra, cifras.
- Each hit kept as a candidate was checked with `research/archive_sweep_2026-10/known.py` on legajo and folio.

## Access log

- 26 Oct 2026, 21:00 UTC: PARES answered **429 Too Many Requests** to every request from this machine from the
  first query on (also in the built-in browser, so it is the IP, not the client). Several sweep agents share the
  IP. Probed at intervals of several minutes after that.
- 27 Oct 2026, 19:03-19:17 UTC: PARES answered again. `sweep.py` (now: 20 s delay plus 0-10 s jitter, stop at the
  first 429, request cap, `hits_progress.json`) ran three narrow terms: "sin descifrar" (1 page), "no descifrada"
  (14 pages), "parte en cifra" (15 pages). 30 requests in all, about one every 30 s, no 429. Nothing was fetched after
  that; the screening below is from the hit lists only (no description pages were opened).
- **Pagination bug (fixed in the next entry).** PARES ignored `tambloque=100` and `pagina=<n>` on `catalogo/find`. Every
  page came back with 25 rows (the "Resultados por página" select shows 25 selected), and pages 2-15 list
  the same 25 rows as page 1. The site pages through the displaytag parameter `d-2677838-p=<n>` on
  `SearchController.do;jsessionid=<session>?texto=...&d-2677838-p=<n>` links in the `pagelinks` div of page 1, so it
  needs the session cookie and those links; 100 rows a page is set through the POST form `formBusqueda`. So only the
  first 25 rows of each term were collected: "sin descifrar" 24 of 24 (complete), "no descifrada" 25 of 488,
  "parte en cifra" 25 of 58. Page 14 of "no descifrada" was the PARES error page ("Problema encontrado al realizar la
  búsqueda"). The old `'raquo' not in h` stop test never fires because every page carries the pager. Two more parser
  bugs, fixed offline against the saved pages: `has_images` was read from the text after the title link, which
  belongs to the next row (the thumbnail link comes first in each row), and the signatura was cut at the first space
  ("SANTA" for "SANTA CRUZ,C.51,D.40-60"); pages were also decoded as Latin-1 although PARES sends UTF-8. `hits.jsonl`
  was rebuilt from the saved pages with the fixed parser (same 74 rows). `sweep.py` now also stops when a page repeats
  the previous one, and `hits_progress.json` is reset to page 1 for the two unfinished terms. The paging was
  then tested live and fixed the same evening (next entry).
- 27 Oct 2026, 19:39-19:46 UTC: pagination fixed and tested live (session + `formBusqueda` POST + displaytag
  links, see Method). 16 requests in all, one at a time, no 429:
  - 19:39:16 GET, 19:39:40 POST: "parte en cifra", all 58 rows on one 100-row page ("Resultados 58"). 58 of 58.
  - 19:40:14 GET, 19:40:42 POST, 19:41:08, 19:41:36, 19:42:05, 19:42:27 GET (pages 2-5): "no descifrada", banners
    1-100, 101-200, 201-300, 301-400, 401-488 of 488, so the rows really differ page to page; 475 unique ids,
    because the order is not stable between pages (page 3 repeated 12 rows of page 2, page 4 one row of page 3,
    and as many were skipped).
  - 19:43:07 GET, 19:43:34 POST: the same term with `orderBy=7` (signatura) gave the PARES error page.
  - 19:43:46 GET, 19:44:15 POST, 19:44:44, 19:45:10, 19:45:34, 19:45:58 GET: "no descifrada" in title order
    (`orderBy=0`, 481 unique, 7 repeats); it added the 13 missing rows: 488 of 488.
  - The 19:43:46 request came 12 s after the one before, because it was a new process and the delay was only kept
    inside one process. `sweep.py` now keeps the time of the last request in a stamp file (`PARES_STAMP`), so the
    20 s + jitter spacing holds across processes too. All other gaps were 22-40 s.
  - `hits.jsonl` now holds 570 rows: "sin descifrar" 24, "no descifrada" 488, "parte en cifra" 58 (dedup by id
    within a term). The 463 new "no descifrada" rows and 33 new "parte en cifra" rows are not screened yet; 399 of
    the 488 are AGS Estado (EST,LEG) letters, most of them 16th century.
- Not run, on purpose: the broad terms ("cifra", "cifrada", "en cifra", "descifrado", "carta cifrada", "contracifra",
  "cifras"). They return thousands of rows and should be run by decade with `run_batch.py` (e.g.
  `run_batch.py 120 "cifrada@1500-1599/10"`); the owner allowed batches for the evening of 27 Oct only.

## Screening of the 27 Oct 2026 hits (74 rows, hit-list titles only)

PARES full-text search seems to match words, not the phrase: a 1494 lawsuit ("cifra" as a sum of money), Falla's
letters (1927, 1939) and a map fonds also hit. So a hit is a pointer, and every row added says so in `status`.

- Added to `candidates.json` (22 rows, after the 16 earlier ones), best first: Philip II to the I marqués de Santa
  Cruz on the annexation of Portugal 1580-81 (AHNOB SANTA CRUZ,C.47,D.2); papers taken from a French cabinet courier
  near Irún 1809 (AHN ESTADO,20,B; "sin descifrar" hit); Philip IV to the II marqués de Santa Cruz 1630, 1632
  (Flanders) and 1634-35 (nine units, all "sin descifrar" hits); Philip IV to the duque del Infantado in Rome 1650, two
  identical letters partly in cipher (OSUNA,C.1981,D.113); cipher letters to Diego de Brizuela at the siege of Tortosa
  1648 (FUENRUBIA,C.7,D.56); Jardet to Marmont 1812 (DIVERSOS-COLECCIONES,133,N.29); intercepted correspondence 1811-12
  (ESTADO,3130,Exp.4); Philip IV to Caracena 1660 (FRIAS,C.81,D.105-137); Binasco in Genoa 1592 (AGS EST,LEG,1424,79);
  Lemaur 1823 (AGI ESTADO,35,N.76); the AGI file on Russian America 1761-75 (ESTADO,86B,N.100); and AGI Estado
  despatches of 1816-25, grouped by post (St Petersburg 5, London 3, Rio de Janeiro / Río de la Plata 4, Vienna 2,
  others 4), plus Philippine cipher letters of 1757 and 1780, Manila ransom 1766 and Santa Cruz 1624-25. Grouped rows
  should be split once the descriptions confirm which items hold undeciphered cipher.
- Prior art (27 Oct 2026, one web search each for the rows of importance 3 or more, plus the offline cryptiana copies
  in `targets/vasto1527/prior/` and `targets/esp318/lit/crypt/`): nothing found on any of them. The October 2026
  news about an AI reading of a 1809 letter to Marmont concerns the Beauharnais letter already in `targets/napoleon/`,
  not the 1812 Jardet letter.
- Dropped, deciphered: Osuna Philip IV to the Rome embassy 1642-45 with deciphered copies (OSUNA,CT.7,D.3, D.16,
  D.17; CT.2,D.6, D.8, D.13). These are crib material for the 1650 Infantado letter. OSUNA,CT.13,D.6 (Carretto and
  Grana to Infantado 1650) hit "descifrada" with no cipher in the title; check it with the Infantado row.
- Dropped, already here: AGS EST,LEG,12,233 "Carta cifrada de Diego López al cardenal de Tortosa" is DECODE R10024
  (Ayala, deciphered 1867; the key behind `targets/ayala1516/`). AGS PTR,LEG,2,36,8 (PARES 12988891) "Carta cifrada de
  Lope Hurtado de Mendoza al rey" is very likely the cipher letter of catalogue 626 (Paz, Catálogo V no. 189): map it
  there.
- Key leads (keys or tables, no ciphertext): PTR,LEG,52,191 "Cifra con su clave e instrucción para descifrar" (1502 /
  1564; already Tomokiyo's Cg.3, 1564); AHNOB LUQUE,C.307,D.113 "Tabla para descifrar determinados documentos"
  (undated); AHN DIVERSOS-COLECCIONES,142,N.29 (1811), report on the blockade of Ciudad Rodrigo "y clave para
  descifrar cartas interceptadas a los franceses", a Peninsular War key for French intercepts, worth pairing with the
  1809-12 rows; AHN telegraph keys 1869-81 (PARES 6051253) and 1882 (ULTRAMAR,5245,Exp.34).
- Dropped as out of scope or not cipher: fonds- and series-level rows without signatura (Orden Público Cuba, Mapas,
  Obras públicas, Esplá-Prieto notes); 1931 and 1937 telegram keys and files; the 1938-39 cipher-machine invoices; the
  Causa General; items after 1950 (AGA 1956, CDMH 1963); the 1948 AGA file on the Hungarian primate; Falla drafts;
  the 1494 lawsuit; a 1778 cannon plan; "Anexo al Dietario" 1929-36 (DIVERSOS-TITULOS_FAMILIAS,3782,N.3, a diary
  annex: worth one look at the description, nothing in the title says cipher).

## Prior art for AGS ciphers (to check candidates against)

- Tomokiyo, cryptiana `spanish2C_now.htm` (copy in `targets/vasto1527/prior/`): the DECODE AGS records R9952-R9969,
  R10024, R7966, all deciphered at the time or by him/Luo.
- Luo, Wanruo, doctoral thesis (Valencia, 2021): 126 letters from 48 AGS Estado legajos, Charles V / Isabella
  period; keys in AGS Estado leg. 1.1.1 (docs 112, 136, 151, 169, 197, 210, 214, 215).
- *Estudios Románicos* 34 (2025), monograph "La escritura secreta en Europa en el siglo XVI"
  (https://revistas.um.es/estudiosromanicos/issue/view/22781): Margaret of Parma 1559-66 (Benavent; Florio),
  Florence 1537-38 (Bertomeu Masià), Naples 1547 (Bucuré, AGS Estado leg. 1037?), Rome 1543 (Cascella Alcaraz),
  Rome conclave 1565-66, Requesens/Pacheco (Leone, AGS Estado leg. 899-902), Juana de Austria regency 1554-59
  (Luo), Fogliani 1747 cifra y contracifra (Pacheco), Emmanuel Philibert → Renard 1556 in French (Pich Ponce),
  Mary of Hungary (Reales Pérez). Items in these legajos should be flagged as possibly already read.
- Kolosova (Ferdinand the Catholic ciphers), Bergenroth / CSP Spain, Danvila (MHE), CODOIN: printed
  decipherments are possible for any Estado letter of 1485-1558.

## Printed-catalogue pass (26 Oct 2026, PARES still 429)

- Sources grepped (archive.org OCR): Paz, Catálogo IV (catlogo4secret01spai, 27 cipher hits) and Catálogo II
  (catalogo2secreta00spai, 6 hits). HathiTrust full-text search returned 403; the archive.org Guía (dli.ernet.535875)
  and the AGS Norteamérica catalogue have no public OCR. Catálogos of Roma, Nápoles, Sicilia, Milán, Venecia,
  Génova, Inglaterra, Flandes (Magdaleno, Plaza) were not found full-text on archive.org; not reached.
- Rows added: K 1498 Chantonay 1562; leg. 6446/6452 Viana 1729-30; leg. 6443 Rialp intercepts 1728. 9 rows total.
- Key leads (Catálogo IV, keys with no ciphertext listed): K 1492 (1559 key with the Archduchess's chaplain and
  Rodrigo Manrique); Jerónimo Brun key (1580s); agent David key (Avisos de Tours, 1590); Coedon Gormille key
  (Brittany/Mercœur); Mateo de Aguirre key (Guise); Baron d'Itre key (Bavarian agent, Paris, c. 1700).
  Catálogo II: cipher for the Aranjuez treaty correspondence and Carvajal's cipher (18th c.).
- Dead end: K 1539 = cipher originals of Diego de Zúñiga's letters whose descifrados are in K 1538 (read at the time);
  useful only as crib material.

## Printed-catalogue pass 2: Catálogo III (Flandes) and Catálogo V (Patronato Real), 26 Oct 2026

- Finding the volumes: the Google Books API (`googleapis.com/books/v1`) returned a 0-quota 429; the old Atom feed
  `https://www.google.com/books/feeds/volumes?q=...` still answers and gives viewability. Full view (pre-1927):
  Catálogo III, Flandes, Holanda y Bruselas 1506-1795 (1915; ids `GXdKAQAAMAAJ`, `98k6AQAAIAAJ`), Catálogo V,
  Patronato Real (1912; `V0hQAQAAMAAJ`), the 1920 Guía (`o4kwAQAAMAAJ`), Catálogo IV (`LRxmk7ffOgwC`, done).
  No view: XIV Roma (1936, `xDhmAAAAMAAJ`), XVI Nápoles (1942), XVII Inglaterra (1947, `u4p00QEACAAJ`), XIX Sicilia
  (1951), XXI Dos Sicilias (1956), XXIII Milán y Saboya (1961). Venecia, Génova and later Alemania volumes not found
  in full view anywhere tried.
- Reading them: books.google.com from curl gives a reCAPTCHA page; in the built-in browser, same-origin `fetch` of
  `/books?id=<id>&jscmd=SearchWithinVolume2&q=<term>` (snippets, capped at ~10 hits) and of
  `/books?id=<id>&pg=PA<n>&output=text` (OCR text of a window of pages; text in `class='flow'`) both work. Every
  page of Catálogo III (PA1-200) and V (PA1-540, PT1-30) was scanned for `cifr`: III 6 distinct passages, V 18.
- Rows added (7): Estado leg. 587 Parma cipher letters 1582-83; leg. 563 Requesens cipher letters; leg. 499/500
  'Mr. de San Vicente' cipher correspondence 1541-43; leg. 2126 spy Vannó letters + his cipher; Patronato Real
  no. 4715 cipher "con sobre inglés ... Ni descifrado"; no. 189 Lope Hurtado 1520 Comunidades letter in cipher;
  no. 1521 Charles V instruction to the Cardinal of Trent 1546, "Toda en cifra". Legajo numbers in Catálogo III are
  margin numbers mixed into the OCR flow: confirm on PARES. Patronato Real numbers are catalogue item numbers, not
  PTR legajo/doc signatures: map them on PARES before merging (no. 4715 may already be one of the PTR leg. 52
  Puebla rows in catalogue.json).
- Left out as read at the time (cipher with descifrado listed): Catálogo V nos. 285 (Alarcón 1521), 1274 (Puebla
  1498), 1545 (third instruction to San Valentín 1556), Garcilaso to Alba 1556 (fol. 106), 1594 (Pacheco 1556),
  1607, 1632 (Gaeta 1557), 1998, 3705, 3826 (Busca 1540), 3911 (Bivona); no. 1522 (Manrique de Lara 1551, cipher
  copy) has the clear copy as no. 1523 (crib pair).
- Key leads: Catálogo V, Garcilaso de la Vega 1556 key sent to Rome 10 June 1556 (Carafa war file, fol. 99);
  Catálogo III leg. 2101 (1658-62) and 1677 papers on "un francés que descifraba sin clave" (a codebreaker offering
  his services) and leg. ~2133 on the French reading Spanish despatches: background, not ciphertext.
- Not reached: Roma, Nápoles, Sicilia, Milán, Venecia, Génova, Inglaterra catalogues (in copyright, no view);
  HathiTrust full-text search (403), BVPB (429), BDH (403) from this machine.
