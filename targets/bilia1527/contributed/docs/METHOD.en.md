# Method and checks

[日本語](METHOD.md)

## Procedure
1. **Images**: BnF Français 3013 on Gallica (ark:/12148/btv1b9060138r, digitised from microfilm). Leaves identified by the ink foliation: f. 102r = view 164, f. 102v = view 165, address = view 167 (no. 42: f. 99r = view 159, f. 99v = view 160, address = view 162). The BnF catalogue's "Fol. 102" and "Fol. 105" are three higher than the ink foliation. No images are included in this repository.
2. **Key**: the key sheet Archivio di Stato di Milano, Carteggio Sforzesco cart. 1591 no. 24 (DECODE R5258, docketed "Cum equite Bilie / extracta ex cifris", i.e. extracted from the ciphers with the Cavaliere Bilia). Values were taken from the transcription of the sheet in the Cyphersolver ledger (targets/gilino1527) and from George Lasry's independent recovery of the same key from a letter (contributed to the same ledger) (data/key.tsv, source in the source columns). The ledger uses this key to read the letter of "el Gilino" to the Duke of Milan (BL Cotton Vespasian C IV ff. 214–218, 15 Sept 1527).
   - System: barred base letters (G, B, o〔D〕) with two-digit numbers, numbered in order through a syllabary (B.31 ba … B.50 gu, B.51 fa … B.55 fu, D.51 la … D.65 nu, G.56 pa … G.80 tu, o.33 va … o.47 zu); a letter alphabet of bare numbers and signs; a few word codes (H.27 che, H.28 come …); name codes; nulls.
   - Five signs with no matching form in the key-sheet transcription (ß, £, F, tt, qx) were given values from this letter (41 signs on f. 102r, 8.1%). The control was also run without them.
3. **Transcription**: Claude Opus 5.5 transcribed the full-size images line by line by sign name (data/transcription_f102r.txt): base letter and number (G.67, B.42, o.53, H.27 …) and bare signs (19, 25, ÷, x, ß …).
4. **Decipherment**: src/decode.py applies the key (data/decoded_f102r.txt). The reading ([READING.en.md](READING.en.md)) adds word division and punctuation.

## Cross-checking and image checks
- **Cross-check**: OpenAI Codex (codex-cli 0.163.0-alpha.10.2, default model; the run log does not name the model) was given only the 37 line images and a list of sign names (second/PROMPT.md: shape descriptions only, with no values, first transcription, key or reading), and run three times separately from an empty folder in read-only mode (`codex exec --ephemeral -s read-only`). Each run log holds a single reply, with no command executions or file reads.
- **Image check, round 1**: the 51 places where at least two of three Codex runs read the same value differing from the first transcription were judged separately by Codex and Claude Sonnet on the line images (check/round1/; the two candidates in random order, no values or readings given). 15 places where both chose the Codex reading were corrected; 14 where both chose the first reading were kept; 22 split places were left as first read.
- **Image check, round 2**: the 22 split places were judged again separately on enlarged thirds cut from the full-size images (check/round2/). 5 places were corrected (2 by deleting a sign), 5 kept, 12 still split (8 of them on f. 102r; [OPEN.en.md](OPEN.en.md)).
- On f. 102r alone, 9 of 31 places were corrected in round 1 and 3 of 14 in round 2 (12 in all).
- A place was corrected only when both models agreed. Nothing was corrected by majority vote or by fit to the context.

## Figures (f. 102r, 505 signs)
| Item | Result |
|---|---|
| **Independent second transcription**: three new Codex runs after the corrections (second/codex_pass1–3.txt), value agreement with the corrected transcription | 94.9, 94.9, 94.9% (by name 89.3, 90.1, 90.3%). The transcription was not corrected from this comparison |
| Record of the cross-check (not used for the assessment): uncorrected transcription vs the first three Codex runs (second/earlier_v1/), both pages | 89.3–91.2% (by name 85.0–86.7%) |
| Record: transcription after round 1 vs the second three Codex runs (second/earlier_v2/), f. 102r | 94.5, 94.1, 95.3% (by name 89.7, 89.1, 90.5%) |
| Key-shuffling control (1,000 shuffles), all signs | real −2.218, best shuffled −2.844, 0 at or above the real key |
| Same, key-sheet values only (the five inferred signs removed) | real −2.179, best −2.687, 0 |
| Same, the key applied unchanged to the three independent Codex transcriptions | real −2.256, −2.222, −2.228; best −2.765, −2.710, −2.648; 0 each |
| Signs with a value | 504/505 (99.8%); 505/505 with the inferred [ca]; key-sheet values only 463/505 (91.7%) |
| Calibration | none (below) |

- Agreement: within each line the two sign sequences are aligned by edit distance, and the share of the first transcription's signs that agree is counted (src/xcompare.py, src/perpage.py). "Value agreement" treats different names with the same key value (e.g. 25 and as) as agreeing.
- Control: the key values are shuffled among the signs that occur in the letter, and the Italian-likeness of the result is compared with the real key (src/control.py). Italian-likeness is the mean log-likelihood of letter trigrams, built from the top 50,000 Italian words of `wordfreq` weighted by frequency, with trigrams across word boundaries from the top 2,000 words added because the cipher has no word division. Name and word codes are not scored.

## Why there is no calibration
No contemporary decipherment or printed text of any cipher in this key was found, either for this letter or for the other letters in the volume (the BnF catalogue records no "déchiffrement", and the clear text on f. 102v is the close and a postscript, not a decipherment). So the accuracy of a blind reading could not be measured.

## Use of AI
- Anthropic Claude (Claude Code, Claude Opus 5.5): transcription, assembly of the key table, decipherment, reading, scripts, documents.
- OpenAI Codex: independent transcriptions (nine runs) and judgements in the image checks.
- Claude Sonnet: judgements in the image checks, and the prior-work check ([PRIOR_CHECK.en.md](PRIOR_CHECK.en.md), by a reader that did not make the transcription or the reading).
- Human: choice of target and decision to publish. **No human has checked the transcription.**

## Limits
- The list of sign names and the line images were prepared by the side that made the first transcription; the choice of names reflects that view.
- Errors shared by both AI readers are not caught by the cross-check.
- The key values rest on the transcription of the key sheet (Cyphersolver ledger); the key-sheet image itself was not examined here.
