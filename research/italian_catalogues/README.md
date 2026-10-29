# Italian catalogues sweep (28 Oct 2026)

Brief: `research/archive_sweep_2026-10/BRIEF.md`. **Result: 3 candidates**, all from Lombardia Beni Culturali (LBC). Most of the
requested portals could not be reached from this machine.

## Method
- `lbc_harvest.py`: LBC "ricerca avanzata" (`/archivi/ricerca/?testo=<term>&where=comparch`, plain GET, scrapable). 20 terms
  (cifra, cifrato/a/e/i, in cifra, lettera cifrata, decifrazione, decifrato, cifrario/i, scrittura segreta, cifre, notae ...).
  Only "cifra" (59), "cifre" (22) and "cifrari" (4) return anything (exact-word search); 73 distinct fonds/series in
  `lbc_hits.json`. **Nearly all are noise** (cifra/cifre = figures in tax and estimo series, trade names). LBC describes
  fonds and series, not items. Six descriptions were read in full (`lbc_MIBA*.html`).
- `make_candidates.py` writes `candidates.json`. Dedup with `known.py` (Rizzardo, Marescalchi, Archinto, Inquisitori di Stato,
  Maletta, Campofregoso, Ricasoli ...).
- Web searches for Venice, Mantua, Modena, Milan cipher holdings.

## Kept (3)
Rizzardo London 1615 ciphered despatches with keys (ASMi, Marescalchi rosso b.1 fasc. D); Archinto nuncio volumes 1683-1720
(21 vols, cipher letters); Milan legates' letters 1516-1751 (partly ciphered). Scores low to middling; none viewed.

## Key leads (keys, not ciphertext)
- ASMi Carteggi consolari 1701-41 (Molinari/Guicciardi, imperial residents at Genoa), pezzo 1 and "Patenti, credenziali, istruzioni": cifrari. LBC MIBA0024D5 / MIBA0024D7.
- ASMi Visconteo-Sforzesco, Potenze sovrane / Cancelleria segreta "Chiavi e cifrari" scatt. 1591, 1597-98 (edited by Cerioni 1970). LBC MIBA002409. Meister 1902 also cites Pot. Est. Cifre fasc. 1, 2, 4.
- ASVe Consiglio dei Dieci, "Cifre, chiavi e scontri di cifra", busta 1 (web search; unverified).
- ASMo (Modena): 8 buste of surviving 15th-18th c. cipher systems (Casa e Stato b. 141, 1510 ...), per ASMo teaching material.
- Unverified web/forum leads without shelfmark: Maletta (Sforza ambassador) Naples 26 Jul 1455 "in cifre" (ASMi Potenze estere Napoli 1455); Milanese letters intercepted by Florence 1424 (ASF); Campofregoso to the Duke of Milan 1453 (ASMi carteggio); Albertoni cipher ledger 1444 (Cremona); Mantua Archivio Gonzaga b. 423 key. Several are probably solved or are keys.

## Blocked / not reached
- **Internet Culturale**: `www.internetculturale.it` fails TLS from curl (schannel error 35); the built-in browser refused it. Loosening TLS checks was refused by the permission classifier, so not attempted. OAI-PMH untried.
- **DigiVatLib** (`digi.vatlib.it`): 403 Forbidden to curl and to the built-in browser.
- **Everything on `*.cultura.gov.it`** (ASMo, ASMn, SAN `inventari-san`, ASF, beniculturali.it, SIUSA; Antenati 403): connection refused or timeout, same outage as in `research/medici_bia/README.md`. So the Mantua, Modena, Milan and Florence inventories were not searched.
- **ASVe** (`archiviodistatovenezia.it`) answers but no search endpoint was found; Da Mosto's index PDF (`dev.archiviodistatovenezia.it/wp-content/uploads/2025/05/DaMosto_1.pdf`) is a possible full-text route for the Dieci/Inquisitori series, not tried.
- **Manus Online** (ICCU): loads, but no GET search endpoint located; mostly codices anyway.
- LBC covers Lombardy only, with series-level text. Rerun when the cultura.gov.it hosts return; OCR of Da Mosto and the SAN PDF inventories for "cifr" is the best next step.
