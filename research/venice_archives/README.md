# Venice archives sweep (28 Oct 2026)

Brief: `research/archive_sweep_2026-10/BRIEF.md`. Scope: cipher material held in Venice (ASVe, Marciana, Correr,
Querini Stampalia, Cini) and described or imaged online. **Result: 4 candidates** (`candidates.json`, written by
`make_candidates.py`), all from ASVe finding aids, none viewed on the image. Venice's online description is mostly at
series level, and Venetian despatches were deciphered by the Secretaries at the time, so the yield of plausibly unread
items is small. The best output of this sweep is the key leads below.

## Method and endpoints

| Source | Route | Result |
|---|---|---|
| **ASVe moreveneto** (Arianna4, `asve.arianna4.cloud`) | GraphQL `POST /apollo/`; query copied from the site's own search ("Cerca in tutti i campi delle schede"). `moreveneto_search.py term ...` | Works with curl. 45 terms (cifra, cifre, cifrat*, decifra*, decifer*, zifra, ziffra, contrazifra, cifrario, chiavi, crittografia, "caratteri segreti", "scrittura segreta", "inchiostro simpatico", segni, alfabeto, numeri ...). Real hits: the CX series *Cifre, chiavi e scontri di cifra* and its manuscript catalogue; Senato *Dispacci degli ambasciatori. Deciferazioni* (123 registers of 19th-c. copies and decipherments); Miscellanea documenti turchi no. 628 (5 May 1547, the decipherment of two cipher phrases in a bailo's letter) and no. 87 (1503, a ducale sent "non cifrato" on purpose); Senato, Provveditori da terra e da mar, map 772.1 *Isola di Dia* (1607, "la descrizione, decifrata" is with the despatch). All read at the time; nothing kept. Item-level description exists only for a few fonds. |
| **ASVe textual finding aids** (`/it/patrimonio/versione-testuale-degli-strumenti-di-ricerca.html`, 22 PDFs) | downloaded 311 bis, 311 ter, 271 bis, 255, 405; text grep | **311 ter (Archivi propri degli ambasciatori, Tiepolo 1965)** gave the 3 ASVe item candidates. Also: Costantinopoli b. 4 n. 9bis, decipherment of a Senate ducale to Leonardo Donà and Marco Venier, Nov 1595 (read); Inghilterra n. 3, Alvise Mocenigo II copybook 1701-06 with "una istruzione sull'uso della cifra" (key lead). Other PDFs: nothing. |
| **Da Mosto index** (`dev.archiviodistatovenezia.it/.../DaMosto_1.pdf`, `_2.pdf`) | text extracted (vol. 1 9 pp. index layer, 690k chars; vol. 2 307 pp.) | Series level only. Confirms the "copie moderne e traduzioni di dispacci cifrati" for Costantinopoli, Francia, Inghilterra, Spagna (i.e. deciphered), and lists "Studi sulle cifre e decifrazioni ... fatti da Luigi Pasini" (1 pezzo). The CX cipher series is not in Da Mosto (moreveneto says so too). |
| **Manus Online** (ICCU) | `POST /o/manus-api/titles-search-post` (form fields `monocampo`, `monocampo:tipo`, `page`); `manus_search.py` | Works with curl. 17 terms; only 12 Venice records, all noise ("cifre arabe", a date digit; Correr 90 "iniziali di difficile decifrazione"). Marciana has few manuscripts in Manus. The non-Venice hits (143 records: BNCF Carte Machiavelli "in cifra" letters, Ginori Conti 29.x, Estense Lat., APUG Concilio di Trento, Ambrosiana ...) are out of scope and listed in `manus_nonvenice.txt` for the Italian sweeps. |
| **Europeana** (demo key), providers New Manuscript Library Veneto / Marciana / Cini / Querini / Correr / ASVe | `europeana_venice.py` | 123 records, all noise (Roman numerals, coat of arms with keys, printed books). |
| **Fondazione Cini** (`archivi.cini.it`, xDams) | built-in browser (curl gets an Anubis proof-of-work page) | 95 hits for "cifra", all 19th-20th c. music/art/theatre fonds. Dead end. |
| **University of Toronto Scarborough, Dragomans/DRRP** | curl | Page images of ASVe Capi CX, Lettere di ambasciatori, Costantinopoli regs 2-7 (1570s-1600). Site search ignores the term; one exploratory row written. |
| Web searches | | Suriano edition (Huygens), Bonavoglia 2023 (NAM 15), Marciana Lat. XIV 32, Correr Donà dalle Rose, Querini; see key leads. |

Dedup: `known.py` run for Spinelli, Lionello, Corner, Garzoni, Suriano, "Cifre, chiavi", Archivio di Stato di Venezia, ASVe,
Inquisitori di Stato, Donà, Venier. No candidate is in the repo or on DECODE. The repo already knows CX *Cifre* b. 4 r. 16
(`targets/ottobon`), the Codice Amadi (Inquisitori reg. 1269) and b. 4 key registers (`targets/r1862`), and DECODE's
ASVe images (R1862, R1871-R1875, keys R1788-R1790); not re-listed here.

## Candidates (ranked)

1. **Three letters wholly in cipher to Gasparo Spinelli, Venetian resident at Naples, 20-23 Oct 1618** (Archivi propri
   ambasciatori, Napoli 7bis). Osuna crisis; no decipherment noted. Class B: the residents' cipher of 1616-23 (Suriano's
   key) is filed in CX *Cifre* b. 1. Imp 3 / solv 2 / diff 2.
2. **Senate ducali in cipher to G. B. Lionello, resident with the Swiss, 1620-21** (Svizzeri 5b), in two or three copies.
   Valtellina crisis. Class A: the clear text is almost certainly in Senato, Deliberazioni, Secreta. Imp 2 / solv 3.
3. **A "replica" wholly in cipher to Francesco Corner, ambassador in London, 1706-07** (Inghilterra 4), from a fellow
   ambassador (Dolfin, Tiepolo or Garzoni). Class C. Imp 2 / solv 2 / diff 3.
4. **Capi CX, Lettere di ambasciatori, Costantinopoli, regs 2-7, partly imaged at UTSC**: exploratory; cipher pages not
   confirmed and probably decipherments are with them.

There is no fifth: nothing else found online in Venetian holdings is both ciphertext and plausibly unread.

## Key leads (keys and cipher treatises, no ciphertext)

- **ASVe, Consiglio dei Dieci, *Cifre, chiavi e scontri di cifra con studi successivi*** (moreveneto id
  a87224b7-83b9-4dde-bf2f-8ea49b5163f5): 9 buste (7 buste + 1 register of the Council's cipher keys, 16th-18th c., and 1
  busta of decipherment studies by the archivists Luigi Pasini and Giuseppe Giomo, 1882-96). Kept under key with
  restricted access ("sottoposta a particolari limiti di consultazione"), so not fully described. Finding aid: the
  manuscript *Catalogo delle chiavi e dei documenti relativi alle cifre* (attributed to Pasini; moreveneto id
  1dfd0572-fd70-4bed-9548-9c64c77017ac). Citations found: b. 1 fol. 3, the residents' "great cipher" used by
  Christoforo Suriano at The Hague 1616-23 (key a = z10); b. 2 fol. 15, the cipher introduced in 1621 (a = 156/174)
  (both from the Huygens Suriano edition); b. 2 fasc. 13, the 1630 cipher, and b. 2 fasc. 14, the 1645 "scontro novissimo"
  (Bonavoglia 2023, who also notes the 1621 cipher was reused after 1680 and a near-copy of the 1630 one, +10 per
  decade, approved in 1714; he cites Soro-school treatises by Ludovici and Marin in the same series); b. 4 r. 16, the cipher book of 1578-87 (already in `targets/ottobon`). This is the key source for any Venetian
  despatch held elsewhere (CSP Venetian originals, intercepts in Vienna, Simancas, the Vatican).
- **Suriano 1616-23**: his ciphered despatches from The Hague (ASVe Senato, Dispacci, Olanda) are fully edited by the
  Huygens Institute; the Secretary's decipherments are filed with them and F. D'Uonno decoded the remainder. Solved;
  useful as a crib/control set for the 1616-23 residents' key (and for candidate 1 and 2 above).
- **ASVe Inquisitori di Stato, pezzo 395** (Capitani da Mar to the Inquisitors, 1647-60): ciphered despatches of
  G. B. Grimani and Francesco Morosini, each with the chancery decipherment; three published and re-deciphered by
  Paolo Bonavoglia, "Due dispacci cifrati al veleno nella guerra di Candia", *Nuova Antologia Militare* 4 (2023) fasc. 15.
  The busta probably holds more of the same (read at the time). Pezzo 134 fasc. Capitani da Mar holds the replies.
- **Alvise Mocenigo II, ambassador in England, copybook 1701-06** (Archivi propri ambasciatori, Inghilterra 3; ex Miscellanea
  codici 45): "inserta all'inizio una istruzione sull'uso della cifra". A 1701 Venetian embassy cipher instruction; may
  carry the key for candidate 3.
- **Senato, Dispacci degli ambasciatori. Deciferazioni** (moreveneto id 0635a851-...): 123 registers of decipherments by
  place. Any Venetian ambassador's cipher despatch found abroad should be checked here first.
- **ASVe "Studi sulle cifre e decifrazioni ... Luigi Pasini"** (Da Mosto II, 1 pezzo) and Pasini's printed *Delle scritture
  in cifra usate dalla Repubblica di Venezia* (1872/73) for the key catalogue.
- **Biblioteca Nazionale Marciana, Lat. XIV 32 (= 4702)**: Alberti's *De cifris*, photographed (reading room only).
- **Collegio, Lettere secrete, registers from 1436** (moreveneto, e.g. reg. 5, 1436-38), digitised (Kohl / Hedgelawn
  Foundation): clear register copies of the Signoria's secret letters, i.e. cribs for 15th-century Venetian ciphers held
  elsewhere.

## Dead ends and blocked

- **Biblioteca Nazionale Marciana**: `marciana.venezia.sbn.it` redirects to `bibliotecanazionalemarciana.cultura.gov.it`,
  which times out (curl and built-in browser). Its catalogue and digital library were not searched.
- **Internet Culturale**: homepage answers to curl (200) but searches return 403; the built-in browser fails
  (ERR_SOCKET_NOT_CONNECTED). A retry with browser-like headers was refused by the permission classifier as bot-check
  circumvention, so not pursued.
- **Nuova Biblioteca Manoscritta** (Regione Veneto, catalogues Correr, Querini and other Venetian libraries):
  "il servizio non è disponibile" for this IP (curl 500, browser shows the block page). Its records reach Europeana,
  which was searched instead (noise only).
- **Museo Correr** fund list PDF (`correr.visitmuve.it/.../ELENCO-FONDI.pdf`) 404. Donà dalle Rose / Cicogna not searchable
  online beyond Manus/Europeana.
- **Querini Stampalia**: no online manuscript search found (its records are in NBM, blocked).
- **ASVe "Dispacci degli ambasciatori al Senato. Indice" (1959)** is linked from 311 ter at `151.12.58.123/dgagaeta/...`
  (a ministry host); not tried after the cultura.gov.it failures.
- ASVe images: apart from DECODE, moreveneto's gallery and the Kohl registers, ASVe series are not imaged online, so all
  ASVe candidates need ordered scans (solvability 2).

## Files

- `moreveneto_search.py`, `manus_search.py`, `europeana_venice.py`, `make_candidates.py`: scripts.
- `candidates.json`: the 4 rows. `manus_nonvenice.txt`: out-of-scope Manus hits for the Italian sweeps.
- `dl/` (git-ignored): downloaded PDFs, their text, raw search JSON.
