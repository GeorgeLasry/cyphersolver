# Beinecke (Yale) and Folger sweep, 28 Oct 2026

Part of the Oct 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Output: `candidates.json`
(38 rows, built by `build_candidates.py`), query log in `coverage.md`.

## Method

- **Yale.** Archives at Yale (archives.yale.edu) answered 403 on the first request and was not retried. Its
  finding-aid components are also indexed in Quicksearch's "Archives or Manuscripts" source
  (`search.library.yale.edu/archives`), so every cipher-family query was run there (162 hits for
  cipher/ciphers/ciphered/"in cipher", 26 for "partly in cipher", 32 cypher, 39 cryptogram ...) and all 270
  cipher-family records were read by title, date, call number and "Found in" path. Catalogue (Orbis) records
  were opened for notes. Yale Digital Collections (`collections.library.yale.edu/catalog.json`) was searched
  with the same terms (54 hits for cipher) and used to check which call numbers are digitised. Both Yale hosts sit
  behind an AWS WAF JavaScript challenge, so all requests went through the built-in browser, about one every
  3 s.
- **Folger.** catalog.folger.edu (TIND) harvested as MARCXML (`/search?p=...&of=xm&rg=200`) for 33 terms; the 46
  manuscript records (leader/06 = t) among the cipher-family hits were read in full. Most "cipher" hits at the
  Folger are Baconian-cipher literature (Donnelly, Gallup, Owen, Platt), not ciphertext.
- **Dedup.** `known.py` on every shelfmark and name; DECODE list (R2854-R2877 are the Beinecke records) checked
  against the repo.

## Rows kept (38): the best leads

1. **Utah War cipher letter, Salt Lake City, 21 Jul 1858** (WA MSS S-4203 Un21). Two pages, catalogued
   "Undecoded"; Schmeh posted images in 2020 and it is still unsolved. Readable now from the blog images.
2. **Barras → Rochambeau, Newport, 3 Aug 1781** (GEN MSS 146 box 4 f. 216), "partly in code (not decoded)".
   Class A: the 11 and 17 Aug Barras letters in the same series carry interlinear decodes (R2856; the 17 Aug one is
   digitised) and the army code tables are in box 5 ff. 294-298.
3. **Jersey → Manchester, 15 Apr 1700** and **Vernon → Manchester, 23 Dec 1700** (OSB MSS fc37 box 3 f. 34, box
   6 f. 52): cipher parts left out of Cole's *Memoirs* and not on DECODE; the THE=454 key already used in
   `targets/yard1699` should read them. Also R2868 (8 Jan 1700), digitised, DECODE Non-decrypted, printed "not
   quite correctly".
4. **Copies of Charles I's 66 secret letters to Hopkins, 1648** (Osborn c650): names in numerical cipher; may
   share a table with `targets/charlesi` (22 May 1648 to Worsley, unread).
5. **Digby → Rupert, 27 Apr 1645** (Folger X.c.125), tagged "Cryptograms"; royalist keys in `targets/rupert*`.
   Warburton 1849 may print it; not compared.

Others: Titley (Copenhagen 1764-66, "several letters in cipher"), Richard Hill (Savoy 1705), Emo and Grimani to
Ruzzini (Utrecht congress 1712-13, "some letters in code"), the Chlingensperg encrypted diaries (1805, 1825,
1830), Blathwayt → Stepney 1701-02 (could hold the key `targets/stepney` lacks), Osborn-file letters (Charles II to
Proger 1658, Forbin-Janson from Cracow 1676, Duchess of Marlborough and Mainwaring to Coningsby), the Pforzheimer
"Codes and Ciphers" items (Philip II 1597, Charles V 1548, Richelieu 1623), small private ciphers (Fossey
notebook, seen: vowel-to-digit, trivial; Shield diary 1838; Osborn b216, b253, b77; German charm book GEN MSS
FILE 413; colour-cipher letter 1863; Latham & King telegram 1878), and Folger V.b.333, V.a.682, X.d.542.

Nine rows say "cipher matched" (Sandwich, Orrery, Essex, Charles II, Forbin-Janson, Mainwaring, Marlborough,
Blathwayt ×2): Quicksearch matched the cipher queries on a note that only archives.yale.edu shows, so the cipher is
probable but not confirmed.

## Key leads (keys or tables, no ciphertext)

- OSB MSS 148, George Aust Secret Service papers 1794-1800, "a detailed cryptographic key" (DECODE R2857, N/A).
- GEN MSS 146 box 5 ff. 294-298: Rochambeau army codes ("Chiffre de Robt. Morris" No. 1, "Dechiffrement No. 2"
  with Greene and Morris, "chiffre du major Talmadge", "Tableau pour chiffrer / déchiffrer", a numbered code with a
  substitution cipher). Reads Barras 3 Aug 1781 and perhaps Washington-Rochambeau items.
- GEN MSS VOL 1120, Jacques Picques (French resident in Sweden): seven ciphers c. 1641-51 (with Brasset, Brégy,
  the Elector Palatine Karl Ludwig) plus letter extracts 1651-53.
- OSB MSS 1 (Poley papers) box 5 f. 205, private cipher Poley/Secretary of State, 2 Nov 1702 (photocopy); box 6
  f. 220 "Cypher" (oversize). OSB MSS 2 (Blathwayt) box 8 f. 179 and box 6 f. 142, memoranda of the ciphers used
  by Alexander Stanhope (c. 1700) and Poley (1692). OSB MSS FILE 1409, Perwich's code with Blathwayt (c. 1668-72).
- OSB MSS fc37 box 18 f. 47, "Diplomatic cipher, contemporary copy", July 1701 (= THE=454, R2858, already used).
- Lewis Walpole Library, LWL MSS 7 box 48 f. 7, "Key for cypher" in the Thomas Coningsby papers (1584-1717);
  may read the Coningsby letters above.
- Folger MS 272890, "Table of cypher substitutes issued by Sir Charles Hedges", 2 Nov 1703.
- Osborn c70, Broadbent commonplace book 1757: "A New Method of Wrighting Secrets" (a cipher explained).

## Shorthand (not rows)

Beinecke GEN MSS VOL 575 ("Cryptography, or a compleat system of short hand"); Osborn b216 (shorthand beside
the cipher pages). Folger V.a.387 (Katherine Packer 1639, "shorthand based cipher"), V.a.8 (L. Cromwell cookbook,
same shorthand), V.a.308 (epigrams partly in shorthand).

## Left out (deciphered, famous, known, or not ciphertext)

- Voynich (MS 408, 408A), Mellon MS 29 and 136 (in repo); Mellon MS 27 (DECODE R2874 "Decrypted").
- Spinelli archive GEN MSS 109 (Piero Spinelli, 30 letters 1514-26 partly in cipher; Tommaso 7 Sep 1519): already
  catalogue 306, Spinelli brothers' key rebuilt by Domnina.
- Manchester papers OSB MSS fc37: the letters "partly in cipher, deciphered" or "printed as deciphered" in Cole
  (Jersey 11 Jan, 5 Feb, 15 Feb, 14 Mar, 1 Apr, 18 Apr, 25 Apr, 28 Oct 1700; Prior 2 May 1700; Vernon 25 Jul,
  18 Nov, 12 Dec, 30 Dec 1700; Yard 28 Sep and 5 Oct 1699; the Italian partition paper of 7 Mar 1700; the n.d.
  Portugal sheet, box 6 f. 35); Yard 12 and 16 Oct 1699 (read here, `targets/yard1699`); Stepney 23 Mar 1702
  (`targets/stepney`).
- Rochambeau, Barras 11 Aug 1781 (interlinear decipher, R2856).
- Folger X.c.58 (Nottingham 5 Jul 1692, numerical code "deciphered by the recipient"); V.b.264 before p. 435
  (Walsingham 26 May 1574, "deciphered"); M.a.244 (1843 copy of Madox's diary, BL Add MS 5008, cipher read in
  Donno's 1976 edition).
- Strang diary ciphers (WA MSS 447; Weiskopf's 1937 translation in the same collection; published).
- Franklin → Dumas 16 Aug 1781 (GEN MSS 1457; in the Franklin Papers); Benjamin Church 1775 (Pforzheimer; the
  famous letter, deciphered 1775).
- LWL Mss Vol. 87 (Conway's drafts 1765-67 "marked for translation into cipher": plaintext drafts).
- Manuscripts and Archives MS 1670 (Unshlikht → Voroshilov "cipher telegram" 1928, a decoded copy from Russian
  archives); RU 58 Phi Beta Kappa cipher letter 1782 ("not in collection"); Yale Divinity RG 275 (Andover
  student society constitution and cipher, 1808).
- Carlingford papers, Charles II → Taaffe 1655-60 (digitised; two viewed, clear).
- All Baconian-cipher material at both libraries; monogram "ciphers" (Tennyson, Kerrich, bookplates); "ciphering"
  arithmetic books.

## Not reached

- **archives.yale.edu**: 403 Forbidden on first contact (28 Oct 2026); folder-level notes therefore unread. The
  nine "cipher matched" rows need a check there.
- **Folger digital collections** (luna.folger.edu → digitalcollections.folger.edu): a Cloudflare Turnstile
  "verify you are human" page; not bypassed. No Folger image was viewed.
- **Folger finding aids** for uncatalogued collections were not searched separately (the catalogue carries
  item-level records for the large manuscript groups).
- Printed checks still to do: Doniol t. V (Barras), Blackley 1845 (Hill), Essex Papers 1890, Warburton 1849
  (Digby 27 Apr 1645), Poynting (Charles I to Hopkins).

## Dropped at merge (28 Oct 2026)

- The four Pforzheimer "Codes and Ciphers" rows (GEN MSS 817; Philip II 1597, Charles V 1548, Richelieu 1623, 18th-c.
  substitution): filed by subject heading only, nothing shows they hold ciphertext rather than keys or printed
  examples. Kept here as leads.
