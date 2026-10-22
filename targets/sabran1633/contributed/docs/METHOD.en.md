# Method

[日本語](METHOD.md)

## Sources and key
- Ciphertext: BnF fr. 4134 (copies, Sabran's letter-book for 1633), Gallica ark:/12148/btv1b9060193z, images f100, f108, f115, f121, f122, f139, f140, f146, f154, fetched at full size from the openapi.bnf.fr IIIF service.
- Key: George Lasry's reconstruction "BNF Francais 4134" (25/05/2022), published as an image on S. Tomokiyo's Cryptiana GL.htm, rewritten with sign names (shape-like labels) in `data/key.tsv`: 52 letter signs, 19 word numbers, 1 doubling sign. 0, 34 and 29 stand together in Lasry's table as "o- 34 29. ET"; we read all three as et (our interpretation).

## Transcription
1. Pages were cut into lines from the horizontal ink profile. Only f. 54r was tilted (about 2°); its first cut mixed lines and it was recut after deskewing.
2. Claude transcribed the enlarged line images with sign names (`data/transcription_first.tsv`).

## Correcting disagreements from the images (corrections/)
OpenAI Codex transcribed the same line images without seeing our reading. Signs where it disagreed one-to-one with us were judged from the images, separately and blind, by two other AI models (Codex and Claude Sonnet). We changed a sign **only where both chose the same other name**.

| Round | How the sign was judged | Changed |
|---|---|---|
| r1 | line image, with the sign hidden as [?n] in the sign sequence; reference sheet of signs cut from the key image (names only, no values) | 26 |
| r2 | as r1; Codex's transcriptions made with the reference sheet attached | 17 |
| r3, r4 | each sign cut out on its own, without context; positions given by Codex on line images with a pixel ruler | 16, 4 |
| r5, r6 | as r3; the reference sheet extended with up to four examples per name from this scribe, taken from signs that we and Codex named alike | 5, 2 |
| r7 | the 60 changes of r1–r6, each sign cut out again and judged as a two-way choice between 'before' and 'after' (which is which not shown); kept if both chose the same name, reverted to 'before' if they disagreed | 16 reverted (13 split, 3 both 'before') |

Some corrections improved the reading (intelligence, commis, l'argent) and some made it worse. r7 restored compagnons, deux and others, but where both models again chose 'after', worse readings remain, e.g. f. 46v ie les excite → ieleseecite ([OPEN.en.md](OPEN.en.md)). Agreement between two models does not remove all errors.

## Independent second reading (second/)
After the last correction, Codex transcribed the lines three times in fresh contexts, given only the 116 line images, three reference sheets (key signs and up to eight examples per sign from this scribe, spread over the pages) and the sign-name list (`second/PROMPT.md`); no values, no reading, no key, no judgements. Each run's log contains a single reply and no command execution or file reading.

Agreement = share of our signs inside matching blocks of the per-line sign sequences (`src/compare.py`): 92.2%, 92.3%, 92.5% overall. The README gives, per leaf, the lowest of the three runs.

The same final transcription read three times with the earlier sheet (up to four examples) gave 92.1%, 86.5%, 86.4% (`second/earlier_sheet_*`). In those runs Codex sometimes switched a name throughout a run (every pl on f. 50v written r, every S on other leaves written f); this is why the examples were increased. Taking the lowest over those runs too, the per-leaf minima are f. 50v 72.1%, f. 57v 81.2%, f. 54r 81.8%, f. 66r 84.6%.

The comparisons used to make corrections (the rounds above) are not called independent.

## Control (controls/)
1000 keys with the letter values shuffled among the letter signs; French-likeness = mean log-likelihood of letter trigrams built from wordfreq's top 50,000 French words. Runs are broken at word numbers, the doubling sign, unreadable and uncertain signs. On all nine leaves, 0 of 1000 shuffled keys scored as high as the real key.

## Calibration (calib/)
No contemporary decipherment was found on the leaves examined in this volume. We used BnF Baluze 155 f. 79 (Gallica btv1b9001401d f163), 17 cipher lines deciphered by Lasry with the same key. His decipherment (red overlay in the GL.htm images) was transcribed into `calib/lasry_plain.tsv` (599 letters; signs he left without a value are omitted).

The leaf was read with the same procedure as this volume:
1. First transcription: a Claude Opus instance that had not seen Lasry's decipherment was given only the key image, the list of sign names and the 51 line images (`calib/opus_first.tsv`, prompt `calib/opus_first_PROMPT.md`). Its log shows it opened no other files.
2. The same seven judging rounds as r1–r7 of this volume, with Codex and Claude Sonnet (`calib/opus_rounds/`). The Codex transcriptions used to find disagreements were made with the same kinds of prompt (no sheet, sheet, sheet with examples).

| Stage | Agreement |
|---|---|
| First transcription (Claude Opus, blind) | 90.2% |
| r1, r2 judging in context (36, 31 changed) | 91.0%, 91.5% |
| r3, r4 single-sign judging (7, 3 changed) | 92.2%, 91.7% |
| r5, r6 single-sign judging with scribe examples (4, 0 changed) | 92.0%, 92.0% |
| r7 two-way re-judging of changes (16 reverted) | **92.0%** (`calib/transcription_f79.tsv`) |
| For reference: Codex only (sheet with eight examples), 3 runs | 83.5%, 85.1%, 87.3% |

Remaining differences:
- The scribe examples on the reference sheet come from the fr. 4134 hand; Baluze 155 f. 79 is in another hand, so they were presented as "another scribe's examples".
- The Claude Opus that made the first transcription of this volume knew the key values while working; the calibration Opus was also given the key image with values.
- Neither was deskewed, apart from f. 54r.

**Earlier route (for reference):** with Claude Sonnet as first transcriber the figures were 78.6% (as transcribed) → 82.5% → 86.1% → 84.6% (after the two-way round) (`calib/sonnet_route_*`, `calib/r1_context.tsv` etc.). The first transcriber has a large effect on the final figure.

## Scope of the transcription
Runs of cipher signs were transcribed. Isolated codes written between dots in the plain text (. H., .12. etc.) and text struck out by the writer are not included.

## Valued share
`src/decode.py` counts the signs whose name is in the key (879 of 891, 98.7%). Stretches that have values but form no words are marked in READING and OPEN.

## Limits
- No human has checked the transcription.
- Sign names, shape descriptions and the reference crops were made by us. Errors shared by us and the other AI are not caught by comparison.
- fr. 4134 is a copy book; copying errors cannot be told apart.
- fr. 4135 (1635) has cipher in the same key, but the scribe's sign shapes differ and it is not read here ([OPEN.en.md](OPEN.en.md)).
