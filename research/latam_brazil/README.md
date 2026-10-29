# Brazil sweep (28 Oct 2026)

**Result: 30 candidates (`candidates.json`, built by `make_candidates.py`), all region "Americas", 1893-1946.** Two were
checked on the image (the 1914 army telegrams at CPDOC); the rest are scored from catalogue descriptions. Nothing
before 1893 turned up: the colonial and imperial holders (Arquivo Nacional, Biblioteca Nacional, Museu Imperial,
Itamaraty, IHGB) were blocked, down, or have no item-level online catalogue.

## Routes and counts

| Source | Route | Result |
|---|---|---|
| CPDOC/FGV Accessus (Rio) | www18.fgv.br/cpdoc/acervo/arquivo, ASP.NET postback scripted with fetch() in the built-in browser; detail pages fetched for each hit | cifrado 130 hits (stemmed: cifrada/cifrados give the same), cifra 144, codificado 17, decifrado 7, criptografia 4, tinta invisível 40 (noise). 104 cipher-relevant records with detail, `cpdoc_hits.tsv`; 18 rows. |
| CPDOC DocReader (docvirt.com) | `docvirt.com/asp/fgv.asp?pesq=<code>` resolves to the viewer; the viewer search is full text (OCR) per collection | Only the digitised fonds (GV, FSC, and some others) have images. FSC_PACEARA and FSC_CONTEST searched for "cifrado". |
| NUPERGS/UFRGS (Porto Alegre) | `acervos/acervo-documental?assunto=<term>&buscar=Buscar` (`nupergs.py`, `nup_rec.py`) | cifrado 22, cifrada 61, cifra 86 ids (`nupergs_hits_1.json`); decifrado 1, decifrar 2, código 35, chave 3 (`nupergs_hits_2.json`). Many 1893-94 records are indexed twice (an 'arquivo 0' microfilm pass and an 'arquivo 1' pass); rows give both record numbers. 11 rows. |
| APESP (São Paulo) AtoM | atom.arquivoestado.sp.gov.br informationobject/browse (`atom_search.py`) | cifr*/codific*/decifrado hit mostly newspaper issues (Correio Paulistano); criptografia/codificada gave the 13 Távora letters of the IHGSP 'Revolução de 1924' collection. 1 row. |
| Arquivo Público Mineiro (SIAAPM) | every module's search.php (`apm.py`, `apm_hits*.json`) | cifra/cifrado/cifrada/decifrado/criptografia: only 'cifras' = sums of money (SG Cx.115 doc 35, CMOP Cx.34 doc 5), a DOPS folder of 1971-73 and a 1974 clipping. No row. |
| Arquivo Nacional de Asunción (Colección Rio Branco, the Paraguayan papers taken to the BN Rio in 1870, returned 1981) | AtoM (`atom_search.py`) | One hit, Varela → Moreira de Castro, ANA-AHRP-PY-558-1-31 item 13 (1849): already in the parallel South Cone sweep (`research/latam_southcone`), so not repeated. |
| FUNAG/CHDD AHI inventory (Itamaraty, 1582-1822) | PDF catalogue, grep (`dl_funag/`, git-ignore it) | No cipher entries; the inventory is at bundle level. |
| UNICAMP REDISAP AtoM | `atom_search.py` | 0 hits (the search path may differ; not pursued). |

`known.py` was run for every name and shelfmark used (Assis Brasil, Rio Branco, Floriano, Zeballos, Flores da Cunha,
Aranha, Klinger, Raul Soares, Collor, Borges de Medeiros, Setembrino, Ceará, Pedro Ernesto, Juazeiro, Távora, Simas,
REVO1924, Moreira de Castro, 558-1-31, Dutch Brazil, Pernambuco, Bahia, Itamaraty, Bonifácio, Paraguay, Abwehr, Vargas):
no hits except Moreira de Castro (South Cone sweep) and the Dutch Brazil ciphers (Nationaal Archief sweep, already
published by Dinnissen & Araújo, HistoCrypt 2023). None of the rows is on DECODE.

## Best leads

1. **CPDOC FSC pce 1914.03.10/4**, 12 cipher telegrams to Setembrino de Carvalho in Ceará, Mar-May 1914 (Juazeiro
   sedition). Digitised. Image seen: letter groups of 4-11 letters, no decipherment. **Crib in the same fonds:**
   FSC cont 1914.10.07/2 (War Minister Vespasiano, 7 Oct 1914), where the groups `CFIIOIZUPDYBSUDX SBHBCUDJ` carry the
   pencil gloss *restabelecimento harmonia* (16 + 8 letters, letter for letter; *e* has four different equivalents,
   so it is polyalphabetic). Also FSC pce 1914.02.19/2: typed clear copies of Vespasiano's telegrams. The best
   ciphertext-plus-crib set found, and online.
2. **CPDOC OA cp 1930.04.27/2**, 354 cipher telegrams 'sem tradução' of the 1930 revolution (580 ff.), with
   OA cp 1929.10.30/3 (16 more) and the keys in OA cp 1926/1929.00.00. Not digitised: scans must be ordered.
3. **NUPERGS, Assis Brasil papers, 1893-94**: Floriano Peixoto, the foreign and war ministers and agents in Montevideo
   to the minister in Buenos Aires during the Federalist war and naval revolt; about 30 telegrams, one with
   'palavras decifradoras' written on it (doc 55).
4. **NUPERGS, Rio Branco → Assis Brasil 1905-08**, 'Texto cifrado', Zeballos crisis. Key lead: the 1908 'telegrama
   nº 9' affair, when Rio Branco published a cipher telegram with its decipherment (not checked whether the code was
   printed).
5. **APESP, Távora letters 1924-26**, 13 letters 'com escrita codificada' from Juarez and Fernando Távora (tenentes);
   APESP holds PDFs.

Also with keys in the same archive: Lindolfo Collor 1932 (LC c 1930/1932.00.00/11 code lists), Raul Soares 1919-23
(RS c 1918.00.00/1, RS sp 1919.01.00/4), Pedro Ernesto 1930 (PEB 'Relação de cifras', 18 ff.), Klinger 1932
(34 telegrams 'cifrados e traduzidos', BK ger 1932.08.27/1), Flores da Cunha (NUPERGS docs 993-994).

Rows marked "probably read at the time" (Daudt d'Oliveira, single Aranha telegrams, most Pedro Ernesto and Klinger
items) are kept because the summaries give content without saying whether the decipherment is on the sheet; they are
cribs at worst.

## Key leads (no ciphertext)

- CPDOC OA cp 1926/1929.00.00 (keys attached to an Aranha telegram; it is also a row), LC c 1930/1932.00.00/11 (codes,
  pseudonyms, 22 ff.), RS c 1918.00.00/1 and RS sp 1919.01.00/4 (Minas codes), PEB c 1930/1932.00.00/3 ('Relação de
  cifras', 18 ff.), VMF c 1932.00.00/1 (key words), GV c 1938.03.25/2 (private cipher Vargas–Batista Luzardo, 7 ff.,
  digitised), GV c 1946/1950.00.00/5 and GV c 1950.02.00/1 (Vargas codes 1946-50, digitised), JF c 1907.10.14 (letter
  on the ciphers to use with João Francisco).
- NUPERGS Flores da Cunha docs 993-994 ('Códigos para cifrar e decifrar documentos'), doc 133 (9 Dec 1923, sends 'uma
  chave telegráfica do arquivo de Honório Lemos'), Assis Brasil doc 196 (Tibúrcio de Azevedo, 5 Apr 1923, sets up a
  code and false names).
- ML rj 1956.02/03.00/2 (codes of the 1956 Jacareacanga revolt telegrams): after 1950, out of scope.

## Dead ends

- Mentions of cipher, not ciphertext (left out): GV c 1930.02.19/1, GV c 1930.03.05/1, GV c 1929.08.27/3,
  GV c 1928.04.07, GV c 1937.03.27 (letter forwarding cipher telegrams, 1 f., the telegrams not in the item),
  OA cp 1931.05.26/1, OA cp 1932.01.06/2, RS sp 1919.02.18/2, RS sp 1921.06.15/3, LV c 1935.04.10, PEB c 1932.08.30,
  PEB c 1934.12.20, LC c 1932.03.10, LC c 1933.07.23/2, PEB c 1930.08.22. 'Cifras' as figures (JSP Mercúrio 1951,
  EUG 1971, EL 1979) and post-1950 items.
- Web searches for Pedro I / José Bonifácio / Leopoldina cipher letters, the Paraguayan war (Caxias, Paranhos),
  the 1817 and Inconfidência movements and the Farroupilha (Coleção Varela, AHRS Anais) found no cipher material.
  The 1935 Comintern traffic (Prestes, Ewert) is known through Moscow archives, not Brazilian originals; not pursued.
- WWII German traffic in Brazil: not searched separately; the Brazilian originals sit in the Arquivo Nacional (blocked).

## Blocked or not reached

- **SIAN (Arquivo Nacional):** F5 bot challenge for scripts; in the browser the search needs a login (e-mail/CPF,
  password, reCAPTCHA). No account was created. This is the main holder of the colonial, imperial (Pedro I/II,
  Casa Real) and Vargas-era police records.
- **Biblioteca Nacional** (acervo.bn.gov.br, bndigital, bdlb): Cloudflare block page in curl and in the browser.
- **Museu Imperial DAMI:** 504 Gateway Time-out (curl: no answer). Arquivo da Casa Imperial not searched.
- **Arquivo Histórico do Itamaraty:** no item-level online catalogue; FUNAG only publishes bundle-level inventories
  and the Cadernos do CHDD (printed transcriptions, not searched here).
- **IHGB** (arquivo.ihgb.org.br: no answer), **IEB-USP** (no answer), **Casa de Rui Barbosa** (DocReader library name
  not found), **Fundação Pedro Calmon / APEB** (no catalogue search found).
- CPDOC fonds not digitised (OA, LC, RS, FC, BK, PEB, JD, JF, VMF): images must be ordered from CPDOC. NUPERGS
  documents: no images online; ask NUPERGS.

## Files

`make_candidates.py` (rows), `candidates.json`, `cpdoc_hits.tsv` (104 CPDOC records), `cpdoc_extra.txt`,
`nupergs.py`, `nup_rec.py`, `nupergs_hits_1.json`, `nupergs_hits_2.json`, `nupergs*.log`, `atom_search.py`,
`atom_hits_*.json`, `apm.py`, `apm_hits*.json`. Scratch HTML and the FUNAG PDF were deleted.

`needs_archive_scan` and `access_note` were added to each row at the merge (28 Oct 2026), from the row's own description; re-running the build script drops them.
