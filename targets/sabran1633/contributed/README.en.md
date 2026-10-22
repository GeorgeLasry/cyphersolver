# A reading of the cipher passages in Sabran's letters to Bouthillier (1633)

[日本語 README](README.md)

Melchior de Sabran, French diplomat resident in Genoa, wrote short passages in cipher in his 1633 letters to Bouthillier. This repository reads those passages as copied in Sabran's letter-book BnF fr. 4134, using the key reconstructed by George Lasry ("BNF Francais 4134", 2022).

- **Status: partial reading.** (updated 20 October 2026, see "Changes") The cipher passages of nine leaves (ff. 46v, 50v, 54r, 57r, 57v, 66r, 66v, 69v, 73v), 891 signs, were transcribed. Figures per leaf are in the table below; on all nine leaves the control is 0/1000, the independent second reading is at least 89% and at least 96% of signs have values. The calibration (accuracy of the same procedure on another letter in the same key) is 92.0%. Still, some AI-agreed corrections read worse and ff. 50v, 54r and 57r have long stretches that form no words, so we do not call it a full reading ([docs/OPEN.en.md](docs/OPEN.en.md)).
- **Prior work:** S. Tomokiyo's Cryptiana lists ff. 46, 50, 51, 54, 57, 66, 69, 73 of this volume as "undeciphered" and reports that George Lasry found his key applies to them ([louisxiii.htm](https://cryptiana.web.fc2.com/code/louisxiii.htm), [GL.htm](https://cryptiana.web.fc2.com/code/GL.htm)). The key is Lasry's work; this repository applies it. No published reading was found ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md), category "not found"). Lasry may have unpublished readings, and the originals received by Bouthillier (probably in the French diplomatic archives) were not checked, so we do not claim a first reading.
- **No human has checked the transcription.** It was made by an AI (Claude). Disagreements were judged from the images by two other AI models (OpenAI Codex and Claude Sonnet). Agreement between AIs is no substitute for a human check.
- **AI use:**
  - Transcription, checking procedure, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5).
  - Independent second transcription: OpenAI Codex (codex-cli 0.163.0-alpha.10.2, default model).
  - Judging disagreements: Codex and Claude Sonnet.
  - First transcription of the calibration leaf: Claude Opus (a separate instance that had not seen the decipherment).
  - Choice of target, instructions and the decision to publish: a human.

## Figures (per leaf)
| Leaf (Gallica image) | Signs | Valued | Control (shuffled keys ≥ real, of 1000) | Independent second reading (lowest of 3 Codex runs) | Sample |
|---|---|---|---|---|---|
| f. 46v (f100) | 87 | 98.9% | 0 | 92.0% | les citadins la desirent … fier les armes … le senat … avec moy |
| f. 50v (f108) | 269 | 98.5% | 0 | 91.8% | … de raid(en) les places … il … estoit dispose … secret … faire … surprise (many broken stretches) |
| f. 54r (f115) | 38 | 97.4% | 0 | 89.5% | l'argent … Parme |
| f. 57r (f121) | 127 | 100% | 0 | 90.6% | du munitionnaire de Sa[vone] … en munitionnaire … le commis (some broken) |
| f. 57v (f122) | 64 | 100% | 0 | 89.1% | Savone … du chateau … assurer ses compagnons |
| f. 66r (f139) | 149 | 96.6% | 0 | 92.6% | la ⟨3i⟩ de Savone … descouverte … l'on a mis prisonniers le munitionnaire et [d]eux avec luy amenes … ceux qui sont pris … donner la place … le gouvernement |
| f. 66v (f140) | 59 | 98.3% | 0 | 96.6% | du soupçon … descouvert … de l'intelligence dans cet estat |
| f. 69v (f146) | 71 | 100% | 0 | 93.0% | le munitionnaire de Savone … amenes ici … le discours … n'est long |
| f. 73v (f154) | 27 | 100% | 0 | 100% | le general des postes … conseil |
| **Total** | 891 | 98.7% (879) | — | 92.4–92.7% | |

- Control: French-likeness of the letter runs (table signs only) compared with keys whose letter values are shuffled ([controls/results.txt](controls/results.txt), `src/control.py --strict`).
- Independent second reading: after the last correction, Codex was given only the line images, reference sheets (the key's signs and up to eight examples per sign from this scribe) and the list of sign names, and transcribed three times in fresh contexts; no values, no reading, no key. The figure is the share of our signs matched by the same name ([second/](second/)). Three runs on the same transcription with the earlier sheet (up to four examples) gave 86.5–92.3% (lowest per leaf 72.1–100%; one run wrote r for every pl on f. 50v); they are also in second/.
- Calibration: no contemporary decipherment was found on the leaves examined in this volume. Instead we used BnF Baluze 155 f. 79 (Louis XIII to Sabran, 28 March 1631), deciphered by Lasry with the same key, read with the same procedure as this volume: the first transcription was made blind by a Claude Opus instance that had not seen Lasry's decipherment, then put through the same seven judging rounds. With the key it agrees with Lasry's decipherment at **92.0%** of letters (551 of 599; 90.2% for the first transcription alone). Codex-only transcriptions give 83.5–87.3% ([calib/](calib/), [docs/METHOD.en.md](docs/METHOD.en.md), "Calibration").

## Changes
- 20 October 2026 (after publication): the 60 corrections were re-judged by Codex and Sonnet as a two-way choice (before / after); 13 where they disagreed and 3 where both chose "before" were reverted (`corrections/r7_two_choice.tsv`), restoring e.g. assurer ses compagnons and deux avec. The reference sheet was extended to up to eight examples per sign and the independent second reading was redone (overall 88.1–92.6% → 92.2–92.5%; lowest per leaf 76.2–100% → 86.4–100%). The calibration was re-measured with the same stage added (86.1% → 84.6%). Controls stay at 0/1000 on all nine leaves.

- 20 October 2026 (same day, second update):
  - Calibration redone with the same procedure as this volume: first transcription by a Claude Opus instance that had not seen the decipherment, then the same seven judging rounds. 84.6% → 92.0%. The earlier figure came from a route whose first transcriber was Claude Sonnet (`calib/sonnet_route_*`).
  - Key transcription error fixed: si is 64, not 69 (misread of the key image; it does not occur in this volume's transcription, so the reading is unchanged).
  - On f. 54r, isolated number codes written between dots in the plain text (.12., .33.) and an interlinear insertion struck out by the writer were removed from the transcription. On the other leaves isolated codes in the plain text (. H. etc.) and struck-out text were never transcribed, so the definition is now the same. f. 54r: 44 → 38 signs, valued 90.9% → 97.4%.

## Content (summary, partly conjectural)
A report of 1633 on an affair at Savona:
- the citizens (citadins) want it; the senate (le senat); arms (les armes);
- a plot within this state (de l'intelligence dans cet estat) and suspicion (du soupçon) have been discovered (descouvert);
- the munitions officer (munitionnaire) and two others were arrested and brought here;
- those taken refer to handing over the place (donner la place).

Codes not in the key (35, 3i, 12, 20, 33), probably names, are listed with conjectures in [docs/OPEN.en.md](docs/OPEN.en.md).

## Usage
```
python3 src/decode.py data/key.tsv data/transcription.tsv                     # reading (= data/decoded.txt)
python3 src/control.py data/key.tsv data/transcription.tsv c139 1000 --strict  # control (needs wordfreq)
python3 src/compare.py data/key.tsv data/transcription.tsv second/codex_pass*.txt   # independent second reading
python3 src/calib.py data/key.tsv calib/lasry_plain.tsv calib/transcription_f79.tsv calib/codex_pass*.txt  # calibration
python3 -m unittest discover -s tests
```

## Files
| Path | Content |
|---|---|
| data/key.tsv | Lasry's key with sign names |
| data/transcription.tsv | transcription of the nine leaves (final) |
| data/transcription_first.tsv | first transcription (before any comparison) |
| data/decoded.txt | output of `src/decode.py` |
| corrections/ | judgements of disagreements and the corrections made (six rounds) |
| second/ | independent second reading (3 Codex runs) and the prompt |
| calib/ | calibration (Baluze 155 f. 79) |
| controls/results.txt | control results |
| docs/ | METHOD, READING, OPEN, PRIOR_CHECK |

Images are not included; sources are cited by image number ([SOURCES.en.md](SOURCES.en.md)).

## Licence
Code MIT; own documents and data CC BY 4.0. The key and the calibration answer are Lasry's work ([LICENSE](LICENSE)).
