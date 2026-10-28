# Huntington Library sweep (Oct 2026)

Sweep of The Huntington Library, San Marino, for unsolved or possibly unsolved ciphertexts dated 1350-1950 that are not
yet in the repo. The brief is `research/archive_sweep_2026-10/BRIEF.md`. The full query log with hit counts is in
`coverage.md`. The 15 rows are in `candidates.json`.

Already in the repo before this sweep: the Eckert Papers telegram ledgers (catalogue 648, `targets/eckert1862/`).

## Method

| endpoint | how | queries | result |
|---|---|---|---|
| OAC finding aids (oac.cdlib.org), facet "Huntington Library, Manuscript Collections" | built-in browser, same-origin fetch (curl gets an AWS WAF challenge) | 18 terms, 25 page requests | 173 + ~420 component hits, read; WAF CAPTCHA twice, so stopped |
| Huntington Digital Library (hdl.huntington.org), all 26 collections | CONTENTdm dmwebservices API (`hdl_sweep.py`) | 22 terms | 832 distinct non-Eckert objects (683 Marston photos matched on 'code'); all 149 others read |
| Huntington catalog (catalog.huntington.org) | III WebPAC keyword search (`catalog_sweep.py`) | 26 terms | 100 manuscript records, read |
| HMC Hastings IV (archive.org/DLI full text) | grep | cipher/cypher/decipher | 3 hits, none a Huntington item |

The pace was one request every 3-5 s per host (10 s on OAC). Images were viewed only to check leads (5 Blathwayt pages,
kept in the session scratchpad, not in the repo). Dedup used `known.py`: none of the 15 rows is in the repo, Cryptoole
or the DECODE list.

## Best leads (ranked)

1. **Port Sainte-Marie intelligence report, 1729** (mssBLA 191, Blathwayt papers addenda). About 140 code groups, not
   decoded. The same code is deciphered on the sibling mssBLA 187 (checked on the image), and on mssBLA 188 and the
   14 Jul and 4 Aug 1729 letters, all in HDL. Class A; a code table rebuilt from the siblings should read it.
2. **Kerlerec, governor of Louisiana, to Machault, 28 Jan 1757**, and **Kerlerec, 12 Dec 1756** (Loudoun papers
   Box 151 F17 and Box 145 F14). These are intercepted French nomenclator despatches. They are not digitised.
3. **Bothmer and Hanoverian agents to Robethon, 1713** (HM 44710, 393 leaves). Some dispatches are ciphered. Check
   Schnath 1984 and Macpherson 1775 for prior decipherments.
4. **East India Company Committee of Secrecy, Philippine expedition, 1769-80** (HM 80328-80338). Some items are in cipher.
5. **Francis Drake (Munich) to Charles Stuart, 20 Sep 1803** (Hamond collection F34). The cipher has no reading noted.
   Stuart's own readings on F36 and F37 should give the key.

Lower priority rows:
- Madrid 13 Sep 1728 (BLA 186, 11 groups) and the Rottembourg statement (BLA 184, a few name codes). Both are probably
  the same code as lead 1.
- J. Q. Adams to Madison, 7 Jan 1811. Probably printed decoded in Papers of James Madison, Presidential Series 3.
- Hooker telegrams of 1862.
- HM 64 cipher words (late 15th century) and HM 744 owner's cipher notes (1648/51). Both are digitised on HDL.
- Cleary journal line (the key is on the facing page).
- Fuller code letter.
- H. E. and C. P. Huntington coded business correspondence (the code books are in the same papers).

## Key leads (keys or decipherments, no open ciphertext)

- **La Luzerne to Destouches, Jan-Mar 1781** (mssDE 37, 55, 68, 108B, digitised on HDL). These are numerical-code
  letters decoded by Destouches or interlined in another hand. They are crib and key material for La Luzerne's 1781 code
  (see `targets/destaing/NOTES.md`, which mentions "the Luzerne 1781 code").
- Blathwayt addenda decipherments: Pareti 7 Jun 1725; To [-----] Jan 1728; Port Sainte-Marie 23 Jun, 14 Jul and
  4 Aug 1729; To [-----] c. 1729; mssBLA 188. These hold the code of lead 1.
- Townshend family papers Box 13: Ferdinando Warner, "An Explanation of the Cyphers in Mr. Selwyn's Letters" (c. 1765).
- Parker of Browsholme newsletters (HM 66704-66716): the key to an alphabetic code sent to Sir Gilbert Hoghton.
- Southern Pacific Company code book 1892-97 (H. E. Huntington papers Box 307 F35). Also the executive cipher books and
  Union Pacific/Southern Pacific code books (21, in the uncatalogued Union Pacific collection).
- Eckert Papers cipher books (mssEC 36-67): already used by catalogue 648.
- Welbeck extracts 1687-88 (MSS MFilm 00361, microfilm of a BL original): a list of numerical ciphers and pseudonyms.
- Beaufort "Cryptography, a System of Secret Writing" (Beaufort papers; the solution was found in 1974).

## Dead ends

These hits are not open ciphers:
- Chang Hong Yen 1910 cable: the meaning is given in the record.
- SP de México telegrams of 1910 and 1929: their content is quoted in the finding aid.
- HU 1051: the cataloguer gives the reading.
- Lady Pecunia "in cipher": a phonetic transcript.
- Book of Hours "cipher": a price code.
- Bristow ledger: the binder's cypher.
- Grant correspondence: plaintext drafts.
- Grant to Stanton 1866: printed in Papers of U. S. Grant.
- Salvetti: printed by the HMC.
- Arensberg, Bendikson and the Bacon Foundation: Baconian material.
- Duryea, Stevens and Lossing "cyphering books": arithmetic.
- Coulette: poems.

## Not reached

- **OAC.** The WAF CAPTCHA stopped the search before the Rare Book facet, "telegraphic code" and cifra, and before any
  container-list browsing of Stowe, Hastings, Ellesmere, Battle Abbey, Pulteney and Loudoun. None of these collections
  gave a hit for cipher, cypher or decipher in the OAC full-text index. Their item-level lists are largely in PDF or
  printed guides.
- **The printed guides.** The Huntington's printed Guides (British 1982, American 1979, medieval 1989) are archive.org
  lending scans, and search-inside was refused.
- **HMC Hastings.** Volumes I-III were not found online.
- **The Huntington site.** huntington.org (Verso blog) was not searched.

## Files

- `candidates.json`: the 15 rows.
- `coverage.md`: every query, with hit counts.
- `hdl_sweep.py`, `hdl_hits.json`, `hdl_items.json`: the HDL sweep.
- `catalog_sweep.py`, `catalog_hits.json`, `catalog_records.json`: the catalog sweep.
- `ia_inside.py`: archive.org search-inside helper. It was refused for the lending scans.

## Dropped at merge (28 Oct 2026)

- JQA → Madison, 7 Jan 1811 (Shapiro collection): printed in the Papers of James Madison, Presidential Series 3, with
  the coded passages decoded and italicised (founders.archives.gov/documents/Madison/03-03-02-0121).
