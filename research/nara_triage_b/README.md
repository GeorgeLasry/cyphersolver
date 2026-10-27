# NARA bulk-scan triage, slice B: RG 59 1906-1950, RG 84, RG 76

Brief: `research/nara_reels/TRIAGE_BRIEF.md` and `research/archive_sweep_2026-10/BRIEF.md`. Input:
`research/nara_reels/out/{rg_59,rg_84,rg_76}.jsonl` and `agg_rg_*.tsv`. Work done 27 Oct 2026.

## Method

1. `triage.py score` keeps the slice (RG 59 publications M862, M367, M973, M1442, T1249, M1751, M1284, M1286,
   M1889 and the unpublished "-" series dated 1906+, all of RG 84 and RG 76) and scores every flagged frame
   (`scored.tsv`, one row per item). Lincoln-condolence volumes (1865), Marshals' returns (1812), Alexandria aqueduct
   drawings, pre-1906 diplomatic instructions, and the 1960s Subject-Numeric/Mongoose files were set aside as out of
   slice (they are not 1906-1950 or are post-1950).
2. `strict.py` keeps frames with 12+ bare 3-5 digit non-year groups, not a running sequence, no table vocabulary,
   few decimals (`strict.tsv`, 1,403 frames); `telegrams.py` keeps frames with telegram/cipher vocabulary and 6+
   four/five-digit groups (`telegrams.tsv`, 14 frames). Every item with strict or telegram hits was looked at by
   its snippets; the leads were fetched in full with `reels.py fetch` (10 items, 4 s apart) and read with `ocr.py`.
3. `triage.py phrases` lists every rare-phrase hit ("undeciphered", "could not decipher", "key lost" ...) and
   every desc hit in the slice (`phrases.txt`, 169 lines; the 10,000+ "in cipher" headers of State Department
   telegram forms were dropped as non-informative). All 169 were read. A further vocabulary search
   (Gesandtschaft, intercept, "German cipher", "code message" ...) gave 174 frames, all read.
4. Groups were not tested against `targets/jqa`, `armstrong`, `erving1807`, `jefferson1787`: those are 1790s-1820s
   US codes; nothing in this slice is in them. 1906+ US traffic used the Department's Red/Blue/Green/Gray codes and
   was decoded on receipt (true readings filed).

Candidates written: 5 (`candidates.json`). Not viewed as images; all read from NARA's OCR of the frames.

## Best leads

1. **German FO → German Legation Stockholm, July 1918, numeric code** (M367 rolls 108, 114, 122, 141). The US
   Legation Stockholm obtained ~19 "authentic" German telegrams of 22-27 July 1918 and sent them in three batches
   (despatches 1421, 1426, 1475, plus re-cabling from Christiania as tels. 1214-1237). The telegraph-form copies with
   full German headers are filed; no decode is in the four rolls. Indicators 017/010/693 + 3-5 digit groups.
2. **Bernstorff → Berlin, 11 Jan 1917**, cipher telegram passed through the State Department cable (roll 166
   frames 0785-0786), filed beside the German armed-merchantmen memorandum in clear: a likely crib.
3. **OHL (Ludendorff) → military attaché Stockholm, and Berlin → Legation/Consulate-General, 5-digit groups,
   July 1918** (same batches).
4. **Abt. II five-letter code-word telegrams to Stockholm, July 1918** (same batches).
5. **German Legation Lima ↔ South American legations 1917-18** (862.20223): ~70 batches of German cipher
   telegrams copied by the US Legation Lima; Room 40 sent back "substance" for most; file not in the scan.

## Per publication: items examined and conclusion

| RG / publication | items with flagged frames (frames) | conclusion |
|---|---|---|
| RG 59 M862 Numerical/Minor File 1906-10 | 700 (10,131); 1,122 strict frames | Statistical annexes (Berlin pt. annexes 17594, Swedish union tables, railway tariffs, census, Hawaiian immigration, meteorology) almost throughout; 142 frames with telegram vocabulary or no words read: all tables or ledgers. Two code runs found, both decoded: Panama 1907 Red-code cable with interlinear decode (9271, roll 673 f. 0058-0062); San Salvador 1907 "Merry" numeric cables with interlinear decode (5717, roll 467 f. 0502-0506). 17 rare-phrase hits: "word undeciphered" inside decoded telegrams (2540, 6369), a Navy-code cable decoded late (2126), cipher typewriter offer (3611), garbled-telegram reports. **No candidate.** |
| RG 59 M367 WWI decimal file 763.72 | 316 (1,805); 89 strict | Stockholm German intercepts (rolls 108, 114, 122, 141) and Bernstorff 1917 (roll 166): **4 candidates**. Ship-case enclosure-number lists (Cormoran, Kronprinz Wilhelm, Eitel Friedrich, Zealandia), Austrian tonnage annexes, Swedish/Russian statistics, mirrored year columns: dead ends. Appam 1916 "two wireless messages in cipher" (roll 178 f. 0379): plain texts only filed, no cipher. 15 rare phrases: garbled own-code telegrams, "signature not deciphered", locks/keys. |
| RG 59 M973 purport lists | 240 (771); 6 strict | Index cards; no ciphertext. 28 rare phrases all about US telegrams garbled in transmission. Pointer used for **1 candidate** (Peru 862.20223). Other pointers kept as leads below. |
| RG 59 M1442 France decimal 851 | 108 (1,084); 22 strict | Financial tables and mirrored OCR of balance sheets. None. |
| RG 59 T1249 USSR decimal 861 | 70 (354); 20 strict | Production and credit tables, mirrored year scales; "could not decipher" = illegible handwriting (861.41/1). None. |
| RG 59 M1751 Polish MFA records | 43 (145); 22 strict | Registry extracts and telegram-cost ledgers (D/V numbers, Polono-Presse tariffs). None. |
| RG 59 M1284 840.48 refugees | 18 (59); 2 strict | Medical/relief statistics. None. |
| RG 59 M1286, M1889 | 3 (5) | Card-index entries. None. |
| RG 59 unpublished 1906+ series ("-") | ~600 items (~1,400 frames) | Passport and consular-registration forms, civilian-internee casualty forms (WWII), Nazi War Crimes death-claim schedules, photographs. Desc hits: Zimmermann telegram items (famous, solved, excluded), Division of Cryptography admin files, codebook titles (ICA geographic code 1959, internee code book: post-1950 or no ciphertext). None. |
| RG 84 Foreign Service posts | 177 items (1,639 frames) + 73 desc hits | Yokohama correspondence (invoice-number lists, telegraph forms), Jerusalem/Jaffa/Haifa ledgers and import tables, Spandau prison logs (A3352). Desc hits are "true readings" (clear copies) of US code telegrams or 1960s CR-7 crypto-admin files. None. |
| RG 76 boundary/claims commissions | 158 items (1,037 frames) | Cattle Claims Memorial (Texas-Mexico, 1870s documents) and Rio Grande boundary hydrology tables; "telegram in cipher" mentions are decoded army telegrams printed in clear. None. |

## Leads not written as rows (need the file, not in the scan)

- 861.00/8312 (M973 roll 204 f. 0886): Berlin tel. 268, 11 Mar 1921, "intercepted messages in cipher to Kopp" (Soviet
  representative in Berlin), full report sent by mail; the decoded content is summarised, ciphers not seen.
- 800.20216/1361 (M973 roll 534 f. 0153): Office of Censorship, Sept 1942, photostat of a "message in cipher" from
  Mrs. Henry Wood, Santiago, Chile, to Asheville NC. Private, minor.
- 862.20212 series: other German cipher telegrams relayed through the Department in 1916-18 ("FOR BELL FROM HARRISON");
  the Zimmermann items are famous and excluded.
- [Mozambique - Beira - Consulate] "Codes and Cipher Other Than State Department" (RG 84 naId 1355076): a possible
  key lead (non-State codes held at a consulate); not digitised in the scan.

## Out of slice, noticed

- M899 (named in the assignment) is *Despatches from US Consuls in Havana 1783-1906*: pre-1906, left to slice A.
- "Seized Correspondence of Rose O'Neal Greenhow" and the Greenhow cipher-letter desc hits (1861-62) are pre-1906.

## Not reached / blockers

- No frame images were viewed; everything is from NARA's OCR. Transcriptions for the Stockholm and Bernstorff
  telegrams need the images (rolls 108, 114, 122, 141, 166).
- The bulk scan only flags numeric frames; five-letter code-word telegrams (the normal State Department form) and
  letter ciphers are invisible to it unless a phrase hit catches them. The Abt. II letter-code telegrams were found
  only because they sat next to numeric ones.
- M862 was triaged by heuristics plus reading of the 142 telegram/no-word frames and per-item samples, not frame by
  frame; it is overwhelmingly printed statistics.
- Decodes by MI-8 (RG 165/RG 457) and Room 40 (TNA HW 7) were not checked.

Scripts: `triage.py`, `strict.py`, `telegrams.py`, `ocr.py`. Outputs: `scored.tsv`, `strict.tsv`, `telegrams.tsv`,
`phrases.txt`.
