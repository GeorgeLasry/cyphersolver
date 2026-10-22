# Reading of Bilia's cipher letter to the Duke of Milan (Burgos, 22 November 1527, BnF fr. 3013 no. 43)

[日本語 README](README.md)

A reading of the cipher letter of Jo. Antonio Bilia to Francesco II Sforza, Duke of Milan, in BnF Français 3013 no. 43 (ff. 102r–v), made with a Sforza key sheet kept in the Archivio di Stato di Milano (DECODE R5258, "Cum equite Bilie").

## Status (2026-10-20)
- **f. 102r (30 cipher lines, 505 signs): complete reading.** Figures: key-shuffling control 0/1000 (also 0/1000 with key-sheet values only). Value agreement between the first transcription and an independent second transcription (OpenAI Codex, reading without seeing the first; three runs): 94.9, 94.9, 94.9% (by name 89.3–90.3%). Signs with a value: 99.8% (100% with inferences). No calibration (no contemporary decipherment or printed text was found; [docs/METHOD.en.md](docs/METHOD.en.md)). Reading: [docs/READING.en.md](docs/READING.en.md).
- **f. 102v (7 cipher lines): reading unconfirmed and not given.** Lowest agreement with the independent second transcription 82.2%; the control with key-sheet values only gives 24/1000, so the result is not clearly distinguished from chance ([docs/OPEN.en.md](docs/OPEN.en.md)). The clear close and postscript are given.
- **No. 42 (ff. 99r–v, to Zaberna, same date): not read.** A different cipher; no key found.
- **Relation to earlier work**: the key is earlier work (the Milan key sheet; its transcription in the Cyphersolver ledger; George Lasry's recovery of the same key). The Cyphersolver ledger listed this letter as readable with a key in hand (catalogue 291). The transcription and the reading were made in this repository. Prior-work check ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md), 2026-10-20): a reader that did not make the reading (Claude Sonnet) searched with the aim of showing that the letter had already been read; result "not found". The places searched (CSP Spain iii/2, Venice iv, L&P iv, Cyphersolver, Cryptiana, Cryptoole, GitHub …) and those that could not be checked (the text of Cerioni 1970, the full text of Giudici 2018, …) are listed there. Not finding a reading does not prove that none exists.
- **No human has checked the transcription.** It was read from the images by AI. Agreement between AI readers is not a substitute for a human check.
- **Use of AI**: transcription, key table, decipherment, scripts and documents by Anthropic Claude (Claude Code, Claude Opus 5.5); independent transcriptions and image-check judgements by OpenAI Codex; image-check judgements and the prior-work check by Claude Sonnet. A human chose the target and decided to publish ([docs/METHOD.en.md](docs/METHOD.en.md), "Use of AI").

## Source
- BnF Français 3013 (letters, 1501–1600), Gallica ark:/12148/btv1b9060138r. f. 102r = view 164 (all cipher), f. 102v = view 165 (7 cipher lines and clear text), address = view 167. No. 42: views 159, 160, 162. See [SOURCES.en.md](SOURCES.en.md).

## Content (summary, partly inferred; [docs/READING.en.md](docs/READING.en.md))
Bilia dined with a person (name code B.58, unidentified), who complained that, according to letters from his son-in-law, the Duke was troubling "conte Theophimo(?)" over earlier prohibitions. Bilia calmed him, saying the Duke had acted for his sake and had always loved him as a father, and advises the Duke to write a letter guaranteeing that, as master of the state, he would not take back what he once gave but would make him lord of something greater, so as not to drive the old man to despair.

## Earlier work used, and what this reading adds
**Used**
- Key: Archivio di Stato di Milano, Carteggio Sforzesco cart. 1591 no. 24 (DECODE R5258). Values from the transcription of the sheet in the Cyphersolver ledger (github.com/dbourdeau/cyphersolver, targets/gilino1527) and from George Lasry's independent recovery. The ledger reads "el Gilino"'s letter of 15 September 1527 with this key.
- The observation that this letter is readable with a key in hand: the Cyphersolver ledger (Daniel Bourdeau).

**Added here**
1. A line-by-line sign-name transcription of the cipher on ff. 102r–v (data/).
2. Values for five signs not in the key-sheet transcription, inferred from this letter (data/key.tsv).
3. A full reading of f. 102r, checked by a shuffling control, an independent second transcription and image checks (docs/METHOD.en.md).

## Files
| Path | Content |
|---|---|
| data/key.tsv | key (sign, value, source) |
| data/transcription_f102r.txt, decoded_f102r.txt | transcription of f. 102r and the key applied to it |
| data/transcription_f102v_unconfirmed.txt | transcription of f. 102v (reading unconfirmed) |
| second/ | the independent second transcription (three Codex runs), earlier Codex runs, the sign-name list given |
| check/ | questions, judgements and decisions of the image checks (two rounds) |
| src/, tests/ | scripts and tests (`python3 -m unittest discover -s tests`; src/control.py needs `wordfreq`) |
| docs/ | METHOD, READING, OPEN, PRIOR_CHECK (Japanese; English in *.en.md) |

## Licence
Code MIT; our own documents and data CC BY 4.0 ([LICENSE](LICENSE)). Sources of the key values as above.
