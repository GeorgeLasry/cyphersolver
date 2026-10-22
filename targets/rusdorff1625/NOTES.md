# Johann Joachim von Rusdorff to Axel Oxenstierna, London, February 1625 (Riksarkivet E 701, DECODE R4336-R4337)

Outcome (21 Oct 2026): **key recovered from ciphertext-only by George Lasry** (PR 72). Three Latin letters, all
cipher tokens carry a value except two codes; 24 code readings are tentative. Write-up: docs/rusdorff1625.html.

Split on 21 Oct 2026 from [`targets/rusdorff1628/`](../rusdorff1628/NOTES.md) under the one-key rule. The other three
Rusdorff records in the volume (R4333-R4335) are a different cipher, with their own entry: R4333 is German and uses
numbers 8-13 and 100-107, which this table does not have, and DECODE lists R4334 and R4335 as "Alphabet".

## The documents

Riksarkivet, Oxenstiernska samlingen, Oxenstierna af Södermöre Ser. B, E 701 (letters of Rusdorff to Axel
Oxenstierna). DECODE R4336 "Riksarkivet_Rusdorff_Oxenstierna_1628-4" (2 images) and R4337 "-1628-5" (3 images); both
catalogued "1628", The Hague, Non-decrypted. The letters themselves are dated in London:

- R4336, images 1-2: London, 15/25 February 1625. The subscription runs past the photographed page.
- R4337, images 1-2: London, 26 February 1625 old style, signed Rusdorff (code 760). The first page is not
  photographed.
- R4337, image 3: the beginning of a further, undated letter (on Bellin and the French offer of 500,000 livres).

Rusdorff was the Palatine envoy in London 1622-1627; DECODE's "The Hague 1628" is the volume's later date.

## The key (George Lasry)

Homophonic letter table plus a one-part nomenclator (`lasry2026/ctts/key.txt`, picture
`lasry2026/cryptiana/images/rusdorff1625_key.png`).

- Letters: 24 letters, three two-digit homophones each, 24 apart (A = 16, 40, 64). Consecutive letters 4 apart in
  runs of six: A-F 16-36, G-M 17-37, N-S 18-38, T-Z 19-39. 23 = U/V; W 27, Y 35, Z 39 unused here; X = 31.
- Codes: three-digit, 187-760, alphabetical by meaning (187 Britannicus? ... 418 Gallia, 428 Germania, 517 Legatus,
  526 Londini, 620 Palatinatus, 631 Parlamentum, 678 Propositio, 738 Rex Galliae, 740 Rex Magnae Britanniae,
  744 Rex, 745 Rex Daniae, 746 Rex Sueciae, 760 Rusdorff). Latin endings are written in clear beside a code
  (`678 bus` = propositionibus).
- Only key words are enciphered; most of the Latin is clear.

## How it was obtained

George Lasry transcribed the five images in CTTS (CrypTool Transcriber and Solver), took the initial letter table
from CTTS's built-in cryptanalysis and completed it with the 24-step rule; the codes were recovered with Claude Opus
5.5 from context and the clear endings, checked against the alphabetical order of the nomenclator. He edited and
translated the Latin (`lasry2026/CONTRIBUTION.md`, Cryptiana-style entry in `lasry2026/cryptiana/`).

Checked here (21 Oct 2026):
- `decode.py` re-applies `key.txt` to the CTTS transcription and reproduces the counts: 438 cipher tokens, 376 letter
  signs (all assigned), 62 codes (36 confident, 24 tentative, 2 unknown). R4336 183 tokens, R4337 255.
- `docs/_validate.py` (model `la`, letter signs only, codes left out): reading -1.997 per letter, random keys
  -5.200 (z 7.4), key fitted to shuffled text -2.724 (z 28.5), annealer on the real text -2.545. Verdict: pass.

## Prior solution (checked 21 Oct 2026)

No earlier decipherment found:
- DECODE R4336/R4337: Non-decrypted, images only, no documents attached.
- Nothing on Cryptoole (XX1628-11), Cryptiana, or in Waldispühl & Kopal (their Oxenstierna paper is Heusner 1637).
- Kröger, *Johann von Rusdorf, kurpfälzischer Gesandter und Staatsmann* (1876; archive.org bub_gb_3NwPAAAAYAAJ,
  pp. 9-10): Rusdorf's papers, four folio volumes, are at the Landesbibliothek Kassel (now UB Kassel); vol. 3
  "exclusively" holds his correspondence with Oxenstierna 1624-1628 and was unprinted in 1876. It probably carries
  the clear text of these letters. **Not consulted; not found digitised.** It would confirm or correct the 24
  tentative codes and fill 628 and 701.
- Loen, *Consilia et negotia politica* (1725) and Cuhn, *Mémoires et négociations secrètes* (1789) come from the
  Munich Camerarius papers and the reports to Frederick V; no sign they print the Oxenstierna letters.
- Riksarkivet's Oxenstierna letter database sits behind a CAPTCHA; not searched.

## Remaining gaps
- codes 628 and 701 (one occurrence each) - blocker: open-codes; alphabetical ranges Palatinatus-Papista and Propositio-Regnum, no second occurrence; the Kassel copybook would settle them
- first page of the 26 February letter, subscription of the 15/25 February letter, rest of the third letter - blocker: needs-physical-access; not among the DECODE photographs of E 701

## Escalation
- [x] siblings: R4333-R4335 in the same volume opened; another cipher (R4333 German, numbers 8-13 and 100-107 outside this table)
- [x] clear-pages: none on the five images; no interlinear decipherment
- [x] known-keys: no other Rusdorff or Palatine key on DECODE fits the 16-87 table; the 70 Chifferklaver låda II keys are Swedish chancery keys of other correspondents
- [x] print: Kröger 1876 read; Loen 1725 and Cuhn 1789 are other correspondence; the Kassel copybook (vol. 3) is unprinted and not digitised
- [x] key-rebuild: the nomenclator's alphabetical order brackets every code; 628 and 701 stay open with one occurrence each
- [n/a] retry: no extended key beyond George's; nothing new to rerun

## Files
- `lasry2026/` — George Lasry's contribution (PR 72): CONTRIBUTION.md, CTTS project files, Cryptiana entry and images.
- `decode.py` — mechanical decipherment and counts from the CTTS transcription and key.
- `validation.tsv` — letter-sign pairs for `docs/_validate.py`.
- `profile.json`
