# Venice / Milan sweep: printed finding aids and holdings outside Italy (28 Oct 2026)

Brief: `research/archive_sweep_2026-10/BRIEF.md`. **Result: 20 candidates** in `candidates.json` (built by
`make_candidates.py` from `rows_sforza.py` and `rows_outside.py`). Nothing committed; downloads in `dl/` (git-ignored).

## Method

1. **Cryptiana** (Tomokiyo): `crypto.htm` index, then the Italian pages (`italian`, `venetian`, `unsolved`, `mantua`,
   `variable`, `null`, `polyphonic`, `influence`, `isabella`, `worcester`, `castiglione`, `GL`, `valle` and 20 related
   pages) fetched to `dl/cr_*.htm` and grepped (`crgrep.py`, `totext.py`). Nearly every Venetian/Milanese item he
   names is already in the repo or solved: Ottobon 1589 (`targets/ottobon`), Ranzo/Garbino 1528 (`targets/ranzo1528`),
   Sirtori (catalogue), Mocenigo 1558 R1873, Surian 1558 R1867, Soranzo R1851, Mantua 1590 (read by Tomokiyo),
   Worcester 1526-29 (solved). The one open lead was his note on **BnF italien 1584** (Sforza papers, key DECODE R1857),
   which led to part 2.
2. **Mazzatinti, *Inventario dei manoscritti italiani della Biblioteca nazionale di Parigi*** (archive.org OCR,
   t. I 1886 `inventariodeima00mazzgoog`, t. II 1887 `InventarioDeiManoscrittiItalianiT2`). t. II pp. 285-509 is the
   item-level inventory of the **Archivio Sforzesco codices, BnF italien 1583-1596** (Sforza papers taken to France in
   1499-1500). `parse_mazzatinti.py` lists every item with codex, year and folio: 2,887 items, **114 marked "In
   cifre"**, of which 31 have a "Traduzione della lettera precedente" (contemporary decipherment) filed beside them
   (`sforza_cifre_all.json`, `sforza_list.txt`). t. I gave three non-Sforza leads (italien 258, 314, 1636).
3. **Gallica images**: `gallica.bnf.fr` (SRU, IIIF, viewer) returns a Cloudflare block to scripts, but the same
   images come through **`openapi.bnf.fr/iiif/presentation/v3/ark:/12148/<ark>/manifest.json`** and
   `openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<n>/full/<w>,/0/default.jpg`. italien 1584-1596 are digitised
   (microfilm, black and white; arks in `rows_sforza.py`); italien 1583 is not on Gallica (DECODE has ff. 68-158).
   A dozen canvases of ital. 1584 were viewed (scratchpad only, nothing kept in the repo): one opening per sheet,
   canvas = folio + 2..4 at the start of the volume.
4. **CSP Venice** (47 archive.org OCR volumes, vols 1-9, 24-26): grepped for "undeciphered", "not deciphered",
   "cipher illegible", "no decipher" etc. Pasini deciphered the cipher for the editors, so only two "Cipher illegible" /
   "Illegible cipher" footnotes turned up (vol. VI, Venetian ambassador in France, 1557; ASVe originals, physically
   illegible). Not kept. CSP Milan is not on archive.org.
5. **TNA Discovery API** within SP 99 (Venice), SP 85, SP 98, SP 79, SP 92, SP 93, SP 104 (`tna_series.py`,
   `tna_italy_hits.jsonl`): 10 hits, all already in `research/tna_discovery/` (SP 99/24/251, PRO 30/25/6) or keys.
   SP 99 is digitised only in State Papers Online (paywalled).
6. **British Library** Archives and Manuscripts catalogue, HTML result lists scraped (`bl_harvest.py`, 24 queries:
   cipher/cypher x Venice, Venetian, Milan, Mantua, Sforza, Doge, Gonzaga, Italian ...; cifra, cifre, zifra, "in cifra",
   decifrata): 720 records, 379 mention cipher, 61 mention Venice/Milan/Mantua (`bl_clean.json`). Records whose
   description says "with decipherings" were dropped. 6 kept.
7. Dedup: every kept shelfmark and name through `research/archive_sweep_2026-10/known.py`. ital. 1583 is already the
   repo target `it1583` (DECODE R7898-R7915), so its letters are only cited, not listed.

## Best leads, ranked

1. **Filippo Maria Visconti → Francesco Sforza, 1446-47, ~14 parchment slips wholly in cipher** (ital. 1584, plus
   ital. 1583 ff. 110, 136, 162). The Visconti chancery and its ciphers were destroyed in 1447; three slips have the
   decipherment filed after them (1584 ff. 5/6, 8/9; 1583 f. 130/131), so the key is recoverable (class A). Image check:
   f. 15 is followed by an unlisted clear f. 16 of the same date, so several "undeciphered" slips will turn out to be
   paired. A reading of any unpaired slip would be pre-1449, older than anything in `research/oldest/CANDIDATES.md`.
2. **Marcolino Barbavara → Sforza, Rome Feb-May 1447** (6 letters; the 1447 conclave). Key on DECODE (R1857), sibling
   f. 49/50 deciphered.
3. **Pietro Pusterla → Sforza, Jan-Mar 1447** (8 letters; key from f. 42/43).
4. **BL Add MS 18662, 'Il Solito' 1629**: leaks from the Venetian Inquisitors' secretariat to Cardinal de la Cueva's
   agent, partly in cipher, with the keys prefixed. Digitisation not confirmed.
5. **Nicolò Guarna / Vincenzo Amidani → Sforza, Milan 1447-48** (about 26 letters): reports from Milan at the
   Duke's death and under the Ambrosian Republic; Amidani's cipher is the one read in part in `targets/it1583`.
   Canvases 226-235 show that some "In cifre" letters are short cipher passages with interlinear glosses.

Then: Tranchedini Florence 1447-49 (B), BnF italien 258 (Giusti → Groslot de l'Isle, Sarpi's circle, 1608-10),
BnF italien 314 (Mayenne's agents at Rome, cipher letter with its table), the minor 1447 envoys, Egerton MS 2050
(Fuente → governor of Milan 1665-66), Torcy → Pomponne at Venice 1706-10, Azzurini Conti → Gualterio.

**Caveat for all Sforza rows**: Mazzatinti notes a filed "Traduzione" only sometimes; interlinear decipherments are
never noted. Each leaf has to be viewed before it counts as unread. The rows are therefore grouped by correspondent
(the folio list is in `shelfmark`), not one row per letter.

## Key leads (keys without ciphertext, or keys for letters elsewhere)

- **DECODE R1857** "Marcolinus de Barbavara ..." (Tomokiyo): reads Barbavara's 1447 letters in ital. 1584.
- **BnF italien 1591 ff. 131-133**: "Spiegazioni delle cifre per le lettere 'cum quodam amico'" (1465), and
  **ff. 134-135**: cipher explanations for letters to Cristoforo Sagramoro and Nicolò de Statis, regio segretario
  (1465). Could read Sagramoro's ciphered despatches (Milanese ambassador, 1460s) wherever they are.
- **BnF italien 1592 f. 27**: "Alfabeto per leggere le lettere in cifre" (1470).
- **BnF italien 1593 ff. 6-7, 10, 93-115, 139-140, 153-157, 190-301**: filed decipherments ("Traduzione") of Alberico
  Maletta's (1463-64) and Giovan Pietro Panigarola's (1465-66) cipher despatches from the French court, about 20 pairs.
  Not listed as candidates (all read at the time, and Mandrot's *Dépêches des ambassadeurs milanais* prints the
  series), but they rebuild the Milanese France keys of 1463-66, e.g. for Louis XI → Maletta 1465 (`research/oldest`
  B6) or Giovanni Bianco, Lyon 1466 (row in candidates).
- **BnF italien 1589-1590 'Traduzioni'** of Antonio da Trezzo's Naples despatches 1463-64 (ff. 194, 246, 289; 8, 194,
  223, 281-282): the Naples key of 1463-64.
- **TNA SP 99/48/233** "Dodington's cypher": key for BL Add MS 4716-4718 (row in candidates).
- **BL Add MS 20582**: tables of Cardinal Gualterio's ciphers with Acquaviva, Amelot, du Luc, Benigni, Bentivoglio,
  Berwick and others (early 18th c.); may hold the Azzurini Conti key (BL Add MS 20504, row in candidates).
- **BL Add MS 8693, 8696**: registers of ciphered despatches of the nuncio in Spain (Sacchetti) 1624-26, "Registro di
  cifre": clear registers, i.e. plaintext for any original Sacchetti cipher letters (ASV Spagna).
- **BL Add MS 25486**: "Ristretto delle cifre di Münster" of Fabio Chigi 1644-51 (abstracts of his cipher letters):
  cribs for Chigi's Münster ciphers (Nunziatura di Germania / Paci).
- Meister 1906 (*Die Geheimschrift im Dienste der päpstlichen Kurie*, archive.org `diegeheimschrift00meis`):
  grepped for "nicht entziffert", "Schlüssel fehlt" etc.; prints papal keys only, no Venetian or Milanese ciphertext
  flagged as unread.
- ASVe Consiglio dei Dieci, "Cifre, chiavi e scontri di cifra", buste 1-8 (Bonavoglia 2019/2021; Tomokiyo
  `venetian.htm`): the Venetian key books; for the venice_archives / DECODE agents.

## Dead ends and not reached

- **Lamansky 1884, *Secrets d'État de Venise***: not on archive.org (searched by title and author); Gallica and
  HathiTrust block scripts (Cloudflare). Not read.
- **Cerioni 1970, Preto 1994, Perret 1890, Dispacci sforzeschi da Napoli, Carteggi Milano-Borgogna/Francia, CSP Milan**:
  none on archive.org; Google Books not tried. Their content overlaps the Sforza codices above (Cerioni prints the
  ASMi key ledgers, which are also on DECODE as Carteggio Sforzesco scat. 1597/1598).
- **Gallica search** (SRU, viewer): Cloudflare block; only the openapi.bnf.fr IIIF route works, so a volume can be
  viewed only once its ark is known (from BnF Archives et manuscrits pages, which do load). The arks of italien 258,
  314, 1636 were not found (the BnF cote search returned an empty result page).
- **BL digitisation**: the catalogue's "Digitised" facet appears on records with no viewer link; none of the six BL
  rows could be confirmed online.
- **PARES / Simancas Estado Venecia and Milán**: left to `research/pares_ags/` (PARES rate-limits this IP).
- **Vienna HHStA, Vatican intercepts**: not reached (no public item-level search found in the time).
- CSP Venice gave nothing new (Pasini deciphered everything; see Method 4).
- BL Add MS 28356 (Philip II ↔ 3rd Duke of Sessa and Don John, 1572-78, partly in cipher) turned up in the Milan query
  but is Spanish, not Milanese; not kept here (for the Spanish sweeps; known.py no hit).
