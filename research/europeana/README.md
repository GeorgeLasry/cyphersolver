# Europeana sweep (28 Oct 2026)

A metadata sweep of the Europeana Record API (public demo key `api2demo`) for ciphertexts that are not yet in the
catalogue. Six candidates went into `catalogue.json` (ids from `research/archive_sweep_2026-10/merged.json`).

## Method

- `harvest.py` pages (cursor) through phrase queries in English, French, Spanish, Italian, German, Dutch, Czech,
  Polish and Latin cipher vocabulary (cipher, chiffre, cifra, cijfer, Geheimschrift, steganographia ...), limited to
  items dated 1300-1950: 8,903 distinct records in `hits.jsonl` (first run) and `hits2.jsonl` (new in the second).
  `h3.py` re-ran boolean queries ("cifrad* AND carta", "chiffre* AND lettre") and wrote `hits3.json`.
- **The hit lists are almost all noise.** BNE sheet music ("bajo cifrado", "música en cifras"), Rijksmuseum, Swedish
  Army Museum and Portable Antiquities Scheme objects ("royal cipher" monograms), Nijmegen coins (cijfer = numeral),
  and printed cryptography books (Trithemius, Schott, Kircher, Porta, Breithaupt ...). `nomenclator` is a dictionary
  word. Europeana carries only the provider's metadata, so a manuscript shows up only when the provider's description
  names the cipher.
- The few real leads were deduplicated with `research/archive_sweep_2026-10/known.py` and written by hand into
  `make_candidates.py` / `candidates.json`. None was viewed on the image.

## Added to the catalogue (6)

| Item | Provider record |
|---|---|
| Ferdinand II → John II, Hostalric, 5 Jun 1473, cipher with interlinear notes (class A) | BNE bdh0000186643 |
| Ramón de Cardona, viceroy of Naples → Charles I, 4 letters partly ciphered, 1517-20 | BNE bdh0000173169 |
| Cardinal of Sigüenza → Granvelle, 6 letters, Naples 1554, partly ciphered | BNE bdh0000172763 |
| Antonio Maria di Savoia (Ferrara), London 11 Jan 1555, Mss/7913/107-109 | BNE bdh0000172729 |
| Frederick V → Rusdorf, 18 Oct 1630, names enciphered | Heidelberg Urkunde Lehmann 5918 |
| Landgrave Moritz of Hessen-Kassel, alchemical Geheimschrift | Kassel 2° Ms. theol. 181; Ms. chem. 19 |

## Seen and left out

- **BNE bdh0000172697, Ferrante Gonzaga → Granvelle, 30 Jun 1548:** partly ciphered, and the record says a
  deciphered text is on a separate sheet. Probably read at the time; a possible key lead for the other
  Granvelle items above.
- **BNE bdh0000186675, Lachaulx → Charles V, May 1522:** the repo's `poupet1522` (DECODE R1187).
- **RAH (Real Academia de la Historia) Morillo papers, 1817-20** (Enrile 15 Jul 1817, Eguía 28 Oct 1818, Herrera
  7 Nov 1820, all cipher): the records cite Rodríguez Villa's edition, which prints them. Cipher letters of the
  Morillo family are worth a look for the `revenga1822` and `crawford1813` key searches.
- **Archives nationales de France:** AE/B/III Pontchartrain → Louis XIV (1706) only mentions a ciphered letter of
  Amelot; the cipher itself is not in the item. The 1792 Provence/Artois questionnaire has a pencil numeral, no cipher.
- Printed books (Mazarinade "lettre déchiffrée" 1649, Sirmond 1628, Gerbert 1887 ...) and cryptography treatises:
  not ciphertexts.

## Limits and next steps

- Europeana aggregates providers' catalogue records. The big manuscript holders here (BNE Mss., RAH, Gallica
  fonds, Manuscriptorium) are already covered by their own sweeps, so a title search finds few new items.
- Spanish BNE records tag ciphered manuscripts as "(parcialmente) cifrada" in the physical-description field; the API
  matched only 2 such phrases in full, so the BNE manuscript series (Mss/7913, Gayangos volumes) is worth a direct
  BDH search (`bdh.bne.es`) for "cifrada".
- The Czech, Polish and Scandinavian providers returned no cipher manuscripts under the terms used.
