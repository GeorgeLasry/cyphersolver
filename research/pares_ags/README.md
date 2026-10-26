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
