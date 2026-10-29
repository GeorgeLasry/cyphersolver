# Milan / Lombard archives sweep (28 Oct 2026)

Brief: `research/archive_sweep_2026-10/BRIEF.md`. Builds on `research/italian_catalogues/` (LBC only; its three
rows, Rizzardo 1615, Archinto nuncios and the Milan legates, are not repeated here) and `research/medici_bia/`.

**Result: 18 candidates** in `candidates.json`: 16 from the Biblioteca Ambrosiana, 2 from Manus Online. Images
were viewed for 6 of them. The Archivio di Stato di Milano itself was not reachable (see Blocked).

## Method

| Source | Route | Hits | Kept |
|---|---|---|---|
| **Biblioteca Ambrosiana OPAC** (`ambrosiana.comperio.it`, ClavisNG) | `opac/search/lst?q=<term>&page=N`, plain GET via curl (Python's TLS gets reset). Item-level records for the Carlo Borromeo correspondence (F/P inf.), the pergamene (Z 219 sup. Sforza letters) and manuscript units. `ambrosiana_harvest.py` → `ambrosiana_hits.json` (359 records); `ambrosiana_details.py` fetches the detail pages (Nota, folios, image ids) → `ambrosiana_details.json` (186 records) | 34 terms + wildcards: cifra 59, cifre 196, cifr* 297, cifrata 10, cifrate 11, cifrato 8, cifrati 8, decifr* 28, zifr* 4, chiffr* 8, "nomi cifrati" 5, occulte 15 ... | 16 |
| **Ambrosiana digital library** | list of 1,365 fully digitised manuscripts (`biblioteca-digitale/?start=N`, `ambrosiana_digital_list.py` → `ambrosiana_digital.json`), intersected with the cipher shelfmarks. Viewer `digitallibrary.unicatt.it/veneranda/<id>` (JS bot check: works in the built-in browser, not curl); IIIF manifest `/veneranda/data/public/manifests/<id split in pairs>/<id>.json`, images `/iiif/3/veneranda&SEP...jp2/full/1000,/0/default.jpg` | G 275 inf., Trotti 22, A 118 inf. digitised | (in the 16) |
| Borromeo correspondence images | each F/P inf. item record carries its own 750-px images (`clavisng/index.php?file=N`) | 22 imaged letters with cipher notes | (in the 16) |
| **Manus Online** (ICCU) | built-in browser; captured the XHR `POST /o/manus-api/titles-search-post` (form body with `item:1016:Keywords=<term>`), detail pages are JS-rendered (`/risultati-ricerca-manoscritti/-/manus-search/detail/<bid>`). Results capped at 80 per query; phrase search does not work | cifra 862 (348 of them Bergamo, noise), cifrata 14, cifrate 12, cifrato 25, cifrati 7, decifrata 52, decifrazione 27, zifra 2, cifrario 3. Lombard records checked: 11 | 2 |
| Europeana API (`api2demo` key, COUNTRY Italy) | `europeana_harvest.py` → `europeana_hits.json` (581 items, git-ignored) | 22 terms | 0 (all noise: music "basso cifrato", "firma non decifrata", Puccini postcards) |
| Biblioteca Digitale Lombarda | VuFind `bdl.servizirl.it/vufind/Search/Results?lookfor=` (`bdl_search.py`) | cifra 1 (Colorni's printed *Scotographia*), cifre 2, nothing archival | 0 |

Dedup: `known.py` on Ambrosiana, F 46 inf, Speciano/Spetiano, Bascapè, Gualtieri, Flavio Orsini, Crivelli, Castaldo,
G 275, Biglia, Trotti 22, Z 219, Carreto, Nicodemo, Tranchedini, Nardini, Maletta, Pontremoli, Q 123, Bichi, Archivio
Gonzaga. Only Tranchedini (repo target `tranchedini1452`, BnF ital. 2242; other agents' rows for BnF ital. 1583 and the
1447-49 Florence letters) and Maletta (other agents' France 1463-65 rows) had hits, for different documents. No
Ambrosiana item is in the repo or on DECODE. `make_candidates.py` writes `candidates.json`.

## Best leads (ranked)

1. **Ferdinand I → G. B. Castaldo, Oct 1552, Ambrosiana G 275 inf.** (4 Latin letters, ff. 9-48). Viewed: whole pages
   of symbol cipher; c. 10r has a contemporary marginal decipherment of part of the cipher, c. 35r has none.
   The volume (486 images) is open IIIF. Class A, imp 4, solv 4. Transylvania after the fall of Temesvár. Nobody has
   noticed the ciphers in print (Carpentieri 2012, Domokos 2025 describe the codex for other reasons).
2. **Carlo Bascapè → Carlo Borromeo, Badajoz/Madrid 1580** (F 58 inf. 247, 249; F 57 inf. 149) with the **cifrario in
   the same series** (F 57 inf. 275, sent with Borromeo's letter of 14 July 1580). Viewed: numeric code runs in clear
   letters. Class A, solv 5, difficulty 1: a key application.
3. **Unknown → Borromeo, 1560, F 100 inf. 49**: a full page of unbroken digits (4 pages imaged). Class C, the most
   "real" unknown cipher of the sweep.
4. **Melchiorre Biglia, nuncio at the imperial court, Oct 1565: two numeric cipher letters copied into his register**
   (Trotti 22, cc. 6v-7v, digitised). Nuntiaturberichte II/5 probably prints the Vatican copies (crib).
5. **Unknown → Borromeo, 1573, F 46 inf. 275**: symbol cipher mixed with clear Italian, one leaf. Viewed.

Then: the Speciano ↔ Borromeo letters 1574-78 (a cipher-with-translation sibling F 47 inf. 131 exists); the
**Sforza-period Ambrosiana pergamene (Z 219 sup.)**: Nicodemo Tranchedini 1452-53, Ottone del Carretto 1457-64,
archbishop Nardini 1464, a Sforza polizza to Maletta 1455. These have no images online, but many siblings carry their
contemporary "spiegazione della cifra", and Tranchedini's key is published.

## Key leads (keys, decipherments and treatises, not ciphertext)

- **Ambrosiana pergamene Z 219 sup., Sforza Rome despatches with "spiegazione della cifra"** (read at the time, so key
  sources for Cerioni-period Milanese ciphers): 9138-9 (Nicodemo, 18 Jan 1452), 9297-8, 9300-1, 9302-3, 9304-5,
  9306-7, 9308-9 (Carretto / della Torre, May-June 1458), 9464-5 (Sforza → Carretto, 2 Aug 1458), 9287, 9454
  (1457), 9373 (Aug 1458), 9404 (Oct 1464); 9631 "ex cifra Nicodemi" (decipherment, 1452); 9624 extracts "de zifre"
  of Guglielmo of Monferrato's letters to Venice 1451. OPAC search `q=cifra` lists them.
- **Ambrosiana F 57 inf. n. 275**: Borromeo's cifrario for Bascapè, 1580 (images online).
- **Ambrosiana F 47 inf. n. 131**: Speciano cipher letter with the translation on f. 270r (images online).
- **Ambrosiana Y 146 sup.**: Filippo Antonio Gualtieri (nuncio in France 1700-06), "Lettere degli anni 1702, 1703,
  1704, in cifra con le spiegazioni" (pp. 1-226) and "Lettere cifrate diverse di cardinali, e di altri, con le
  spiegazioni" (pp. 228-261): decipherments, so a key-rebuild source for the 1700s nunciature ciphers.
- **Ambrosiana R 101 sup., unit 4**: Cardinal Flavio Orsini's 1572 legation to France (after St Bartholomew), copies of
  "lettere appartate in cifra" in clear (EU 3 p. 45): plaintexts for any Orsini cipher originals in the Vatican.
- **Ambrosiana D 234 inf.**: Andrea Gritti 1521, copies "trascritte da un esemplare (parzialmente) cifrato" (clear).
- **Ambrosiana Q 123 sup. unit 19**: Alessandro Crivelli, "Cifra, 15 luglio 1563" (clear text of a cipher letter, Trent).
- **Ambrosiana S 219 inf.**: "Cifrario per corrispondenza (esempio di una cifra vecchia)" in a Council of Trent miscellany.
- **Treatises**: Z 296 sup. unit 18 "La zifra ritiene in sé le seguenti qualità" (ff. 286-292, 329); Federico Borromeo,
  "Delle zifre" (A 77 suss., cc. 33v-50v, 1594-1600) and "Schemi di scritture cifrate" (G 309 (32) inf., ff. 43v-52r).
- From the earlier sweep, still unreached: ASMi Visconteo-Sforzesco "Chiavi e cifrari" scatt. 1591, 1597-98 (Cerioni
  1970). The Ambrosiana pergamene above are the nearest digit-ready complement to those keys.

## Looked at and left out

- F 47 inf. 131 (Speciano, cipher with translation): read at the time (key lead above).
- R 101 sup. Orsini 1572, D 234 inf. Gritti 1521, Q 123 sup. 19 Crivelli: clear copies.
- Y 146 sup. Gualtieri: "con le spiegazioni".
- F 46 inf. 227 (Castelli 1573, "two names in cipher"): two names only.
- G 119 inf. 45 (letter to Ettore Ausonio 1555, "Alla cifra di ..."): incipit is clear; a letter about a cipher.
- Ambrosiana pergamene with "anno in cifre romane" (~100 hits on "cifre"): numerals, noise.
- Manus: Duomo M 33 (20th-c. shorthand/cipher, carbon copies), Brescia Queriniana A.VI.32, Mantova Teresiana 103/156/370,
  Sormani Stendhal MSS FSB 1705/2368, Pavia Ald. 159: "decifrata" = hard to read, or nothing cipher.
- Ambrosiana I 142 inf. "ricetta in scrittura parzialmente cifrata" (209v): a recipe, not added (could be).

## Blocked / not reached

- **Archivio di Stato di Milano**: `asmilano.cultura.gov.it` and `www.archiviodistatomilano.it` refuse curl (no
  connection) and the built-in browser ("navigation denied or failed"). Same for Mantua (`mantova.cultura.gov.it`,
  `archiviodistatomantova.it`) and Cremona (`cremona.cultura.gov.it`). So the Sforzesco carteggio, Potenze estere,
  "Chiavi e cifrari", the Spanish-period Carteggio and Dispacci reali, and the Archivio Gonzaga inventories were not searched.
- **Archivio Storico Civico / Trivulziana** (`archiviostoricocivico.comune.milano.it`): no connection; `milanocastello.it` 403.
- **Internet Culturale**: answers now, but every search hits a "Firewall Captcha Authentication" page (curl and
  browser). Not attempted (CAPTCHA). Daniel could solve it by hand in the built-in browser and a later agent could search.
- **Braidense** (`teca.braidense.it`), **Biblioteca Digitale Lombarda** public archive portal
  (`bibliotecadigitalelombarda.it`), **Archivio storico diocesano di Milano**, **lombardiarchivi.servizirl.it**: no connection.
- **Isabella d'Este Archive (IDEA, UNC)** and BEIC: answer, not searched for lack of time.
- The Borromeo correspondence (c. 20,000 item records, images online) was only reached through the catalogue's own
  notes. Letters whose cipher is not mentioned in the "Nota" field are missed; paging through F 100-F 104 inf. (1560-61)
  and the nunciature letters would likely turn up more.
- Ambrosiana images on the OPAC are 750 px; the IIIF digital library serves full size only for the 1,365 digitised codices.
