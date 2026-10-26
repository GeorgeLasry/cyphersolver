# PARES (AGS / AHN) cipher sweep, Oct 2026

Part of the October 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Archive: PARES, the
Spanish state archives portal, mainly Archivo General de Simancas (AGS) Estado, Guerra y Marina, Secretaría de
Estado, and the Archivo Histórico Nacional (AHN) Estado.

## Method

- Endpoint: `https://pares.cultura.gob.es/ParesBusquedas20/catalogo/find?nm=&texto=<term>&tambloque=100&pagina=<n>`
  (server-rendered; see the memory note `pares-access-and-search.md` and `targets/toledo1565/NOTES.md`).
  `sweep.py` in this folder runs one term, slowly, and appends hits to `hits.jsonl`.
- Terms: cifra, cifrada, "en cifra", "parte en cifra", "sin descifrar", "no descifrada", descifrado,
  "carta cifrada", contracifra, cifras.
- Each hit kept as a candidate was checked with `research/archive_sweep_2026-10/known.py` on legajo and folio.

## Access log

- 26 Oct 2026, 21:00 UTC: PARES answered **429 Too Many Requests** to every request from this machine from the
  first query on (also in the built-in browser, so it is the IP, not the client). Several sweep agents share the
  IP. Probed at intervals of several minutes after that.

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
