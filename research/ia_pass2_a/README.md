# Internet Archive pass 2 (series A), 28 Oct 2026

Output: `candidates.json` (14 rows, all class C except the Najera letter, all `seen: catalogue`). Scripts here: `find*.py`/`probe*.py`
(identifier discovery via advancedsearch and metadata), `dl2.py` (djvu.txt downloader, to the session scratchpad), `grepneg.py`,
`extract3.py`, `fuzzy.py`, `miss.py`, `tgt.py`, `hmc.py`, `dom.py` (regex passes), `show.py`/`eh.py`/`occ.py` (readers), `build.py` (rows).

## Method
Found about 230 candidate identifiers; about 200 OCR texts downloaded (the `dli.ministry.*` Indian-library copies and a few others return 404/401).
Regexes: cipher word near undeciphered/not deciphered/no key/key wanting/"decipher missing"; "partly in cipher" without a decipher in the window
(Salisbury, Domestic); index entries ("Ciphers, undeciphered"). About 1,400 windows, about 600 read by hand. Rows dropped when the same entry or a
sibling prints the decipher (e.g. CSP Dom. Sept 1663 no. 17/18, CSP Foreign 1559 nos. 362/363, Charles I Jan 1646 Tavistock letter, whose
decipher is in the Supplement to the Preface of the 1645-47 volume), when the sender is not named (Salisbury III no. 436, IV p. 484 "Cipher letter 28 Feb 1594
undeciphered", II no. 1291), or when the note concerns a single cipher group.

## Volumes covered (OCR scanned)
CSP Venetian I-VI, X, XXIV-XXVI; CSP Spanish (Henry VIII) I-VI, Elizabeth I-IV (Hume), Further/Supplement not found; HMC Salisbury I-VII, IX-XIV, XV-XVII, XIX-XXI, XXIII, XXIV
(XVIII, XXII not found on IA); CSP Foreign Edward VI, Mary, Elizabeth 1558-59, 1559-65, 1564-65, 1569-71, 1572-74 (as available); CSP Domestic Elizabeth,
James I (1603-25), Charles I (about 23 volumes 1625-49), Charles II 1660-85 (about 30 volumes, partly "sim_" scans), James II vol. III; LP Henry VIII (45 more volumes, mostly already clear).
Not on IA in full text: CSP Milan, CSP Rome, Foreign Elizabeth 1575-90, Spanish Further Supplement, Henry VIII Spanish Supplement, James II vol. I-II.

## Findings
The hoped-for "undeciphered" notes are rare in these series: Venetian, Spanish and Salisbury print the decipher or editor's reading with each cipher passage
("Original partly in cipher, deciphering appended" or "deciphered by the editor"). The usable notes sit in the Green/Lemon Elizabethan Domestic calendars and in
Charles II Domestic. Many of the best ones (Saint Main, Bristowe, Barnes, Wicham, Allen, Mak) were already in pass 1.

## Best leads
1. Andrada's advertisement to Mendoza, 5 Mar 1591 (CSP Dom. 1591-94 no. 68): ties to targets/mendoza1589.
2. Giles van Harwick to "Peter Artson" (Cecil), Lisbon 1598 (CSP Dom. 1598-1601 no. 109, number inferred).
3. "Aug. Mott" to Jo. Bar, Nov 1666, intercepted insurrection letter (CSP Dom. Car. II 1666-67 no. 107).
4. Charles V to the Abbot of Najera, 16 Nov 1526 (Spanish calendar III no. 609), half-legible cipher.
5. Paget to Throgmorton, Brussels June 1595 (no. 60 III), next to Phelippes deciphers.

## Key leads (not rows)
* CSP Dom. James I 1611-18, nos. 121-122: key and decipher of the cipher letter to Somerset (Overbury affair).
* Salisbury XIV: "French cipher key" (140.54), about 50 proper-name signs; XIII: cipher keys pp. 32, 328, "Ciphers for Italy, England" p. 505; IV p. 559 "cipher used by Mr Edmunds".
* Salisbury III preface, p. 34: Elizabeth's cipher (1585) text; III no. 436 and IV p. 484 are anonymous cipher letters (no sender printed), possible keys for each other.

## Dead ends / blockers
CSP Venetian notes "cipher illegible" (vol. VI, 1557 Michiel despatches) refer to gaps in Pasini's decipher, not usable. The Spanish Henry VIII calendar's "No deciphering appended" entries
(vol. III, many) are read by Gayangos/Bergenroth and printed with "(Cipher:)", so they are not open. Charles I 1644-46 intercepts are deciphered in the Supplement to the Preface.
Class A/B ranking only a rough guess. No entry was checked against DECODE R-numbers (only known.py by name). Entry numbers marked "inferred" or "not captured" in `shelfmark`
need confirming in the printed volume. Web checks done only for Andrada and the Najera letter.
