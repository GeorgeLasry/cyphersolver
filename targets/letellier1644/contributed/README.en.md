# A reading of Le Tellier's cipher letter to Marca (26 April 1644)

[日本語 README](README.md)

A reading of the cipher in BnF Baluze 103 f. 50, a letter from Michel Le Tellier, Secretary of State for War, to Pierre de Marca in Catalonia, using the table of the "Le Tellier-Marca Cipher (1644)" reconstructed by Satoshi Tomokiyo.

- Source: BnF Baluze 103 (Affaires de Catalogne — Correspondance de Marca), Gallica ark:/12148/btv1b9001389d, view 111 (f. 50r, dated in clear "Du 26e avril 1644", 20 cipher lines) and view 112 (f. 50v, 12 cipher lines).
- **State: full reading (controls 0/1000, independent second reading 90.7%, signs with a value 99.5%, calibration 91.3% of signs and 93.6% of letters).** All 32 cipher lines of f. 50r–v read through; nine signs or code groups have no value ([docs/OPEN.en.md](docs/OPEN.en.md)).
- **Relation to earlier work:** Tomokiyo lists f. 50 as the one "undeciphered" letter in this cipher ([Cryptiana](https://cryptiana.web.fc2.com/code/louisxiv0.htm)). NoAutopilot/cipher-lab has a partial draft of f. 50 with the same table (version of 13 Oct 2026, "Status: partial", 451 of 630 signs valued). Words already in that draft ("conseil", "que ledit", "descouvert", "surtou[t]", among others; reading.txt f50r L01, L09, f50v L09, L10) are **reproduced** here. What we add: the connected reading, key additions, the checks of the code groups, the content ([docs/METHOD.en.md](docs/METHOD.en.md)). In the check for earlier readings ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md), 20 Oct 2026: a search made in order to refute by a reader who had not seen the decipherment work, and our own search) no plaintext of this letter was found in print, papers or repositories (class "not found"); HathiTrust full text gives 0 hits for the letter's phrases. Gallica and Google Books full text, the DECODE documents and Spanish printed works such as Sanabre could not be searched. We do not call the reading the first.
- **No person has checked the transcription.** It was made by an AI (Claude) and corrected against five transcriptions made independently from the images by another AI (OpenAI Codex). Agreement between AIs is not a substitute for human checking.
- **Figures:**
  - Independent second transcription: after the last correction, Codex read the page once more in a fresh context: same name on 568 of 626 signs (90.7%), 590 (94.2%) counting names that carry the same key value as one ([second/INDEPENDENT.md](second/INDEPENDENT.md), Japanese). The transcription was not corrected from this comparison.
  - Cross-check record (comparisons used to correct the transcription): five Codex passes; first transcription vs passes 1–3: 565, 554, 559 of 633; final transcription vote: all five agree on 572, majority on 604 ([second/VOTE.md](second/VOTE.md)).
  - Controls: 0 of 1000 shuffled keys score as high as the real key; also with Tomokiyo's table signs only, without the values inferred from f. 50, on the last fifth alone, and on each of the five Codex transcriptions ([controls/results.txt](controls/results.txt)).
  - Signs with a value: of 620 cipher signs, 617 (99.5%) have a key value or a known code group, 613 (98.9%) without the values inferred from f. 50; without a value: 23̂ (r06), a sign cut at the gutter (r10), =18 (v05) (`src/valued.py`). Signs that have a value but cannot be read in context are in [docs/OPEN.en.md](docs/OPEN.en.md).
  - Calibration: 13 lines of f. 171r, which has a period decipherment, read blind with the same key: sign accuracy 0.913 (253/277; 0.874 with main values only; 0.924 with the key at the time the reading was frozen), letter agreement 93.6% (337/360) ([calib/RESULT.md](calib/RESULT.md)).
  - Where each number comes from: [NUMBERS.md](NUMBERS.md).
- **AI use:** transcription, key additions, decipherment, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5). Second transcription: OpenAI Codex. Choice of target, instructions and the decision to publish: a person.
- **Check by hand:** [docs/index.html](docs/index.html) shows each line's image (from the BnF IIIF server) with our sign names and values.

## Change log
- 20 Oct 2026: first version. In the pre-publication check of the same day:
  - Key: main value of y changed from n to g (as in Tomokiyo's table); mz split into mz with a barred tail (s) and mi without a bar (i) (11 places of f. 50 changed to mi); the barred curly x (xx = c) separated.
  - Sister letter f. 230r (lines 1–21) transcribed again with these signs kept apart (`data/f230r_tx.txt`) and aligned automatically with its period decipherment (`src/align_sister.py`): signs matching a key value 406/424 with the key before the changes, 412/424 after. Added ff = d, small o = z, ℓ = x, small ʒ = s, =83 = le Gouverneur.
  - 20 Oct 2026 (same day): every correction of the transcription re-checked on the image (`second/CORRECTIONS.md`); eight of ten changes to σ returned to 6; after the last correction, one more Codex pass as the independent second reading (`second/INDEPENDENT.md`).
  - Real control score −3.458 → −3.446 → −3.286 → −3.302 (0/1000 throughout). Sign accuracy of the calibration 0.924 → 0.913 (the f. 171r calibration transcription was frozen before mz and mi were split).

## Content (gist)
The Barcelona councillors chose, as Marca's lodgings, the house of a friend of Marshal de La Motte, who expected thereby to learn everything Marca does and writes; Marca is warned to be on his guard. Barcelona's agent at Court complains that packets sent to him by the Catalans are being opened; the Queen wishes Marca to watch this, report, and stop it.

## Usage
```
python3 src/decode.py data/key.tsv data/transcription_f50.txt
python3 src/control.py data/key.tsv data/transcription_f50.txt 1000   # needs wordfreq
python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt
python3 src/score_signs.py data/key.tsv calib/f171r_tx.txt calib/f172r_ref.txt
python3 src/align_sister.py data/key.tsv data/f230r_tx.txt data/f232r_ref_l1-21.txt
sh controls/run.sh
python3 -m unittest discover -s tests
```
