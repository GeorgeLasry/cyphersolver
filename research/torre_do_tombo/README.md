# Torre do Tombo (ANTT, Lisbon) sweep, Oct 2026

Sweep of the Arquivo Nacional Torre do Tombo catalogue through DigitArq for cipher letters that are not known to be
read. Output: `candidates_ungrouped.json` (71 rows, built by `build_candidates.py` from the saved DigitArq records), grouped by `group.py` into `candidates.json` (33 rows: per-letter rows of one writer in one volume merged, the catalogue convention). Brief:
`research/archive_sweep_2026-10/BRIEF.md`.

## Method

DigitArq (digitarq.arquivos.pt) is a Next.js app over an open JSON API. It needs no login for the public
catalogue and images:

| purpose | request |
|---|---|
| search (fuzzy, title + description) | `GET /api/docs/search?query=<q>&archiveCode=ANTT&fromIndex=<n>&max=100` -> `{results, total}` |
| full record (description, quota, languages, hasImages, parent) | `GET /api/docs/details/<id>` |
| children of a level | `GET /api/docs/details/<id>?down=1&childrens=<id>&fromIndex=<n>&max=200` (`childrens` must repeat the record's own id, or paging is ignored and only 30 come back) |
| scans of a digitised record | `GET /api/rdigital/<id>?fromIndex=0&max=2000` -> file ids; image `GET /rdigital/dissemination?fileId=<fileId>` |
| item page (stable link) | `https://digitarq.arquivos.pt/documentDetails/<id>`; viewer `/fileViewer/<id>` |

`archiveCode=ANTT` limits to Torre do Tombo (the same portal also holds the district archives and AHU). The search
is fuzzy: `cifra` also returns Cufra, Citra, `cifa` (pitch, hundreds of Corpo Cronológico Ormuz requisitions) and
the summaries of Corpo Cronológico *maços* that give "a cifra do total original de documentos". Every hit was
therefore fetched in full and filtered on the description (`filter.py`).

Scripts (all in this folder): `harvest.py` (search terms -> `hits.jsonl`), `details.py` (full records ->
`details.jsonl`), `crawl.py` (walk a whole fonds -> `crawl_<fonds>.jsonl`), `filter.py` (cipher mentions),
`build_candidates.py` (rows). The `.jsonl` files are the raw catalogue records the rows were built from.

Search terms (archiveCode=ANTT; total hits in brackets): cifra (1394), cifras (228), cifrada (35), cifradas (31),
cifrado (51), cifrados (46), em cifra (306), cifra de (1366), carta em cifra (109), parte em cifra (65), partes em
cifra (69), escrita em cifra (32), em cifras (180), documentos cifrados (38), cifrados telegramas (34), carta(s)
cifrada(s) (11, 15), cifrar (223), cyfra (215), zifra (214), decifrada/decifrado/decifrar/decifra (2-6 each), chave
da cifra (10), chaves de cifra (12), registo de cifra (12), contracifra (6), caracteres (180), letra secreta (26),
criptografia (2), algarismos (22), chiffre(s) (6, 18), segredo cifra (159), ofício cifrado (3). Together **1,677
unique records**, all fetched in full. Of these about 90 really concern cipher before 1951 (the rest are noise
above, plus 600 "Processo CIFRE" files of the 1976 retornados commission).

Four fonds turned out to hold cipher letters described one by one and were crawled completely, since the fuzzy
index does not surface every "Parte da carta está em cifra": Miscelâneas Manuscritas do Convento da Graça (MMCG,
2,243 records), Condes da Ponte (CPN, 2,713), Manuscritos da Livraria 1016 and 1017 (183 + 285) and 1104 (105).

Dedup: `known.py` on every name and fonds (Teles de Faro, conde de Miranda, Nisa/Niza, Vidigueira, Sande, Melo e
Torres, Álvares Ribeiro, João IV, Assumar, Tarouca, Saldanha da Gama, Palmela, Burnay, Pindela, Couceiro, Miranda
Pereira, Francisco Botelho, Orsini, "Torre do Tombo", ANTT, PT/TT): no hit in the repo, DECODE or Cryptoole.
DECODE holds no Torre do Tombo record at all, so none of these rows carries a `decode_ids`. The only earlier
pass over ANTT was the oldest-cipher scan (`research/oldest/scan_2026-09-23/iberia.md`), which looked only for
pre-1500 items.

## Results

71 rows: 38 for 1651-1700, 10 for 1611-1650, 3 for 1701-1800, 6 for 1801-1900, 14 for 1901-1950. Class A 37,
B 2, C 32. Rows are per letter where DigitArq describes letters one by one (MMCG, MSLIV 1017), per volume where it
only says a volume contains cipher letters.

### Best leads

1. **João IV → marquês de Nisa, ambassador in Paris, 1642-45** (MSLIV 1017, letter-book "Tomo II", 284 letters,
   289 scans online; 7 letters described as mostly in cipher, plus the forwarded cipher of the agent "Francisco
   Taquet"). Scan m0019 was viewed: cipher written as pseudo-words in Latin letters ("alloinc fux fxotnc zcx
   ...") inside clear text, no interlinear decipherment. That looks like a monoalphabetic or small homophonic
   substitution, readable ciphertext-only once transcribed. The flagged 7 are certainly not all: m0019 is not
   one of them. Sibling Tomo I (MSLIV 1016, 260 scans) has no item flagged but is the same correspondence.
   Caveat: printed as *Cartas de El-Rei D. João IV ao Conde da Vidigueira (Marquês de Niza)*, ed. P. M. Laranjo
   Coelho, Academia Portuguesa da História, 1940-42, from Torre do Tombo manuscripts; whether the cipher runs are
   deciphered in print has not been checked (not found online).
2. **Royal letters to the governors of arms in the Alentejo and Beira, 1660-63** (Luís de Miranda Pereira, liv. 2,
   864 scans online, "cartas cifradas"). A 12-scan sample showed clear royal letters; the cipher ones still have
   to be found.
3. **Marquês de Sande papers on the Catherine of Braganza marriage, 1657-67** (Luís de Miranda Pereira, liv. 1,
   592 scans online, "cartas cifradas", incl. Diogo Lopes de Ulhoa at The Hague to Rui Teles de Meneses in Paris).
4. **The Hague embassy letters to Francisco de Melo, 1658-60** (MMCG tomes 1E, 2L, 3L: 9 letters of Fernando Teles
   de Faro "em cifra", 9 of the secretary Luís Álvares Ribeiro plus a draft to the States General, 13 of the conde
   de Miranda and one unidentified), each tome with its **own key bound in** (1E f. 4; 2L f. 22; 3L ff. 3 and 30). Class A and
   difficulty 1, but not digitised: images must be ordered. Teles de Faro's letters run up to his defection to
   Spain in 1659. CPN mç. 19 n.º 1 (copy-book of Miranda/Orsini letters to Sande, 1660-61) continues the series.
5. **Carlos I and Manuel II to Queen Amélia, 1903-13** (CAM macetes 9, 12-15, digitised, "alguns documentos estão
   escritos em cifra"): private royal ciphers of the last years of the monarchy, scans online, probably short.

Also notable: Cardinal Orsini's and secretary Vieira da Silva's cipher letters to Melo (CPN mç. 17 n.º 1,
1657-60); Assumar's Barcelona copy-books (Fronteira e Alorna n.º 82, 83, 1708-11) and Tarouca's letters from The
Hague (n.º 114, 1720-21), all with cipher passages; marquês de Aguiar's despatch wholly in cipher to Saldanha da
Gama (1816), with a deciphered ministry despatch of 1817 in the same fonds as crib.

### Key leads (bare keys, not rows)

| key | reference | note |
|---|---|---|
| Teles de Faro letters key | [MMCG/1E/000003](https://digitarq.arquivos.pt/documentDetails/f9340fb8440844d8a015c66e698d3c2e), tomo 1E f. 4 | "Cifra por que se podem entender as cartas que estão neste livro" |
| Álvares Ribeiro letters key | [MMCG/2L/000013](https://digitarq.arquivos.pt/documentDetails/86452686d88a49099678553edd8e366a), tomo 2L f. 22 | same formula |
| Miranda letters keys (two) | [MMCG/3L/000003](https://digitarq.arquivos.pt/documentDetails/0d9cd8ba172a40429ec05490f889405a) f. 3; [MMCG/3L/000020](https://digitarq.arquivos.pt/documentDetails/db2865b81ea04e389a21762d810d1198) f. 30 | first letters / the rest |
| "cifra de França" of Luís da Cunha and Sebastião José de Carvalho (Pombal), to be sent to António Freire de Andrade | [MMIP liv. 23](https://digitarq.arquivos.pt/documentDetails/ef093132ffe1406d870ce2c61c4485fd) | 18th-c. Portuguese diplomatic key, c. 1738-45; would read London/Vienna despatches of Cunha and Carvalho held elsewhere |
| Cipher for Manuel Barreto (marquês de Sande's papers, c. 1662) | [CPN/002285](https://digitarq.arquivos.pt/documentDetails/04e0d2c15ba1462e941d4f33482d53d5), cx. 80 doc. 65 | in a folder with Sande's letter on Queen Catherine |
| Assumar–Garelli cipher register, 1707-13 | [Fronteira e Alorna n.º 104 doc. 30](https://digitarq.arquivos.pt/documentDetails/a8eb5956e0ab46aabfd1f4946edca96c) | may key the Assumar copy-books n.º 82/83 |
| MNE "Cifra antiga", cifrante-decifrante, 1788-1806 | [MNE-ASC/R/4](https://digitarq.arquivos.pt/documentDetails/f391303c93634b9cb5f066b283c62302), cx. 214-215 | Foreign Ministry code books |
| Cryptographic tables, 1796 | [MRM/M027.001](https://digitarq.arquivos.pt/documentDetails/4c0821e5ef844b8faa796efa4eea0cd2) | Rio Maior papers, "tabelas criptográficas para encriptar e decifrar" |
| "Cifras ou códigos utilizados pelo Rei de França", 1595 | [APC/0002/00323](https://digitarq.arquivos.pt/documentDetails/88480c6bb07245288b15ce4ab6386b07) | papers of D. António, Prior of Crato; Henri IV-era French keys? |
| "A B C por cifra" sent by Duarte da Paz from Rome, 1532 | [CC/1/49/20](https://digitarq.arquivos.pt/documentDetails/4dea3bf8d36946f6bba680a47711b9d8) (scans online) | whether the alphabet is enclosed is unknown |
| "traslado das cifras" sent by the infante D. Henrique, 1542 | [CC/1/72/154](https://digitarq.arquivos.pt/documentDetails/0552dfed51324809b646fd1617024525) (scans online) | |
| Cipher + clear draft, Paiva Couceiro, 1921 | [HPC/0024/000135](https://digitarq.arquivos.pt/documentDetails/1cf360ccdf174ea1a55d7aad9d0fdd65) | crib for HPC mç. 24 n.º 97, 130-132 |
| Numeric syllabary fragment, 1865 | [FCC/001/0021/00026](https://digitarq.arquivos.pt/documentDetails/b482fac086d54e2bae791264bb78b79f) (scans) | "pa-pa (419-419), di-ga-mo (926-923-1212)" |
| Cipher proposed for India telegrams, 1897 | [JLC/006/00003](https://digitarq.arquivos.pt/documentDetails/a98d032f707b457b8859a2fac88e08ca) | |
| "Mitografia", notes on cryptography, 1830-80 | [AVSM/0008/00181](https://digitarq.arquivos.pt/documentDetails/68500b1c122d4c1cbbacee05dd750dc6) | |

Other leads: MMS vol. 2 n.º 61-62 (1736, António Baptista to Marco António de Azevedo Coutinho, refers to cipher
use and "a nova chave da cifra"); CLNH liv. 50 p. 56 (1761, Oeiras on the Jesuits' cipher); Ministério do Interior
1930s circulars on the civil-governor telegraph cipher (MI-GM/004-20/40, 004-14/327 and others).

### Excluded on purpose

- Items with decipherment attached: ASG/B/003/00002 (1817, "decifração da parte cifrada"), MI-GM/004-45/175 (1936
  telegrams "e respectiva descodificação"), JSC/A/025/0001 (1858 telegram translation), HB/1-5/24 (telegram with
  decipherment).
- CFTR/001/0003/000191 and 000193: trasladas of the intercepted 1540s Rome cipher letters of the bishop of Viseu's
  household, made from the deciphered text; CM 6/6, 6/8, 9/7 (Francisco Botelho's 1542 mission) are about those
  letters, not ciphertext.
- Mentions only: CC/1/66/25 (1539, will write in cipher), CC/1/88/126 (1552, cipher letters found on António
  Grifson), MNEJ letters on Garampi "secretário da Cifra", MSLIV 1706 (printed freemason exposé).
- After 1950 (EMA, AMC, PIDE, SGPCM cipher telegrams), and the AHU "CIFRA" series (another archive).
- The Ministério do Interior 1930-37 civil-governor telegrams "cifrados" (MI-GM/004-…): about 15 single
  telegrams, routine administration; listed by reference in `details.jsonl`, left out of the rows.

## Blockers and what was not reached

- Most cipher items are **not digitised** (all MMCG, CPN, Fronteira e Alorna, ASG, JLC, HPC). Only MSLIV 1016/1017,
  LMP 1-2, CAM macetes and a few Corpo Cronológico items have scans online. Ordering scans from ANTT is the next
  step for the keyed MMCG letters.
- Coverage is limited by the catalogue: Corpo Cronológico, Gavetas, Cartas Missivas and the Colecção de São
  Vicente are described in summaries that almost never say whether a letter is in cipher, so their cipher letters
  cannot be found by search. Of the high-yield fonds named in the brief, only MMCG and MSLIV describe cipher
  item by item. A real sweep of Corpo Cronológico (Rome/Castile embassy letters, 16th c.) would mean paging scans.
- The Ministério dos Negócios Estrangeiros embassy correspondence (17th-19th c.) is catalogued at box level only
  (no item descriptions); only its code books (MNE-ASC/R/4) surfaced.
- Prior art not checked in print: the Laranjo Coelho edition of João IV's letters to Nisa (1940-42), and Edgar
  Prestage's studies of Portuguese diplomacy 1640-68, which may quote deciphered passages from the Melo papers.
