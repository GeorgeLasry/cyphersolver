# Coverage: NARA Chicago sweep (28 Oct 2026)

Filter: `record.physicalOccurrences.referenceUnits.city:Chicago AND <term>` on the NARA catalog proxy
(`catalog.archives.gov/proxy/records/search`), 4 s spacing, no 403 or 429 met (a few 502s, retried).
3,607 distinct records harvested over 70 term queries; 510 survive the noise/date filter
(`triage.py`: drops naturalization, dockets, newsletters, scrapbooks, post-1950). All 510 were read by title and scope
note, grouped by case (~220 cases/files); the espionage, secret-ink and cipher cases were opened through the OCR text
(`ocr.py`, `/proxy/extractedText/<naId>`).

| term | total hits |
|---|---|
| cipher | 11 |
| ciphers | 3 |
| cipher | 11 |
| ciphers | 3 |
| ciphered | 0 |
| cypher | 9 |
| cryptogram | 2 |
| cryptograms | 0 |
| cryptographic | 1 |
| cryptography | 1 |
| decipher | 8 |
| deciphered | 5 |
| decode | 3 |
| decoded | 3 |
| coded | 310 |
| codebook | 0 |
| encoded | 0 |
| enciphered | 0 |
| espionage | 57 |
| spy | 124 |
| spies | 73 |
| sabotage | 28494 |
| Hindu | 24 |
| Ghadr | 1 |
| Gadar | 7 |
| Gupta | 16 |
| conspiracy AND German | 55 |
| invisible AND ink | 12 |
| secret AND ink | 75 |
| secret AND writing | 235 |
| code AND message | 136 |
| code AND messages | 56 |
| code AND telegram | 109 |
| code AND telegrams | 81 |
| code AND letter | 990 |
| code AND letters | 744 |
| code AND book | 523 |
| rum AND code | 115 |
| liquor AND code | 273 |
| radio AND code | 159 |
| smuggling AND code | 31 |
| Trading AND Enemy | 17 |
| German AND agent | 716 |
| Bund AND espionage | 11 |
| Nazi | 35 |
| Japanese AND espionage | 4 |
| intercepted | 14 |
| secret AND code | 183 |
| cablegram | 17 |
| enemy AND alien AND letters | 44 |
| censor | 26 |
| Bolshevik | 11 |
| IWW AND code | 3 |
| counterfeit AND code | 94 |
| Duquesne | 80 |
| Haupt | 61 |
| saboteurs | 0 |
| Pastorius | 1 |
| Lusitania | 644 |
| Jahnke | 59 |
| Witzke | 22 |
| Rintelen | 3 |
| Bopp | 28 |
| Ram Chandra | 16 |
| Sekunna | 0 |
| Boehm | 141 |
| Jacobsen | 133 |
| Ras Bihari | 1 |
| Hindu AND German | 15 |
| treason | 65 |

"sabotage" (28,494) is not a real hit count (the proxy stems it to a stopword-like match); only the first 1,000 were taken.
Terms with broad counts (code AND letter, German AND agent, Lusitania, Boehm, Jacobsen) are mostly civil/railroad "code" noise.

## Checked in OCR (digitised Chicago court files)
- Hindu-German conspiracy, Chicago (RG 21, US v. Jacobsen, von Reiswitz, Wehde, Boehm, Gupta et al., Crim. 6082):
  naId 540798683 (Bill of Exceptions), 540798684/-85 (Case Documents Part 1/2), fileunits 540798681, 540240450. All digitised.
  The coded exhibit is Government's Exhibit "Code" (Gupta to "Albourge"/Chatterjee, 16 Nov 1916): seven sheets of
  three-digit groups; Friedman decipherment and the full plaintext are printed in the Bill of Exceptions. Solved,
  so not a candidate. No other coded exhibit found in the 693 OCR pages (greps: cipher, code book, numerals, Collier).
- US v. Max Stephan (Detroit 1942, naId 496508051): only a secret-writing document (Ex. 11) read in court. Not a cipher.
- US v. Behrens, Buchanan-Dineen et al. (Detroit 1943, 350862571 ff.): secret-ink recipes and codes in the indictment
  and 6th Cir. appeal; no ciphertext in the digitised folders.
- US v. Wilfong and McGuire (417267109 ff.): "cipher" hit is telegram-company boilerplate.
- US v. Munio Knoll et al. (1950, 580005686): immigration fraud, no cipher.
- Medina/Crowder (1983), Konovsky (post-1950), Debs, Haywood, Remus, Colbeck, Eastland: no cipher content.

## Not digitised (catalogue description only, nothing says cipher)
USA v. Hans Max Haupt (661876551, "an espionage case"), Chicago criminal dockets vols. 10-11 (1915-19; digitised but
docket entries only), RG 118 legal-precedent series (N.D. Ill. 6423676: Capone, Annenberg, Druggan only).
