# R4284 / R4325 — evidence for Cyphersolver issue 98

Prepared 25 October 2026 by Dolly Moulekhi for review by Daniel Bourdeau.
Candidate external-key match; decoded, not fully read. No verified accuracy
or full translation is claimed.

## Start here

1. `strip_number_to_letter.txt`: each number → letter and the precise image region.
2. `reviewed_number_to_letter.txt`: all 41 numerical-letter lines, original
   tokens, numbered token mappings, uncertainty labels, and literal output.
3. `original_number_to_letter.txt`: the same export for the earlier input,
   before the project's image-review corrections.
4. `validate.py` and `validation_results.json`: executable decoding and both
   retrospective controls, including all raw trial scores.

## Sources, permission, and credit

- Cipher: https://de-crypt.org/decrypt-web/RecordsView/4284
  Riksarkivet, Chifferklaver låda II:114.
  I25750 right page; I25751 upper-left continuation.
- Key: https://de-crypt.org/decrypt-web/RecordsView/4325
  Chifferklaver låda II:152. I25940, left page: separate horizontal alphabet
  strip below the first square grid, **not the square grid**.
- Earlier transcription and investigation: Daniel Bourdeau / Cyphersolver.
  https://dbourdeau.github.io/cyphersolver/riksarkivet4284.html
- Transcription reuse with credit was explicitly permitted by Daniel:
  https://github.com/dbourdeau/cyphersolver/issues/98#issuecomment-6403275918
- Dolly Moulekhi: candidate archival-key match and AI-assisted decoding,
  working transcription review, and validation. https://github.com/dollymoulekhi
- Riksarkivet holds the manuscripts; DECODE/DECRYPT provides record access.
  No scans or crops are included. Permission to reproduce the project's
  transcription is not represented as permission to redistribute archive images.

The public article and code repository are now available:
https://dollymoulekhi.github.io/r4284-decipherment/
https://github.com/dollymoulekhi/r4284-decipherment
The article's English reading aid is provisional, not a reference plaintext
for testing the match. Use the literal material here for review.

## Reproduce offline

Download all gist files into one folder, preserving their names. Python 3.9+
and its standard library suffice; no network, AI service, or language model
is needed. Run:

```text
python -B -X utf8 validate.py --check --summary
python -B -m unittest test_validate.py test_decoder.py
python -B -X utf8 export_alignment.py --check
python -B -X utf8 decoder.py --transcription reviewed_transcription.txt --key key.json
```

`validate.py --check` (without `--summary`) also prints all literal lines and
raw control scores. The check verifies this submission's exact file set and
fingerprints, then compares regenerated results to the frozen results.
Do not add other files to this folder before running the integrity check.
`export_alignment.py --check` independently regenerates the human-readable
exports in memory and compares them without modifying the files.

## What the package contains

- `key.json`: 104 working assignments, Y/Z ambiguity preserved.
- `original_transcription.txt` and `reviewed_transcription.txt`: unchanged
  snapshots from the local 24 October review package. "Original" means the
  earlier project input, not a newly independent or certified transcription.
  Source attribution belongs to Bourdeau/Cyphersolver; reviewed corrections
  belong to this project and remain open to independent image checking.
- `line_review.json`: both token streams, changed positions, and literal lines;
  independent-review fields are still pending. Do not confuse this with
  an independent transcription.
- `original_literal.txt`, `reviewed_literal.txt`: all literal lines.
- Both `*_number_to_letter.txt` files: per-token alignments with clear script,
  ambiguous letters, unknown groups, and uncertain tokens distinguished.
- `group_decisions.json`, `uncertain_numeric.json`, `anomalies.json`:
  unresolved groups and explicitly unaccepted hypotheses.
- `validate.py`, `test_validate.py`, `validation_results.json`: the exact
  24 October computational protocol, tests, and stored results.
- `decoder.py`, `test_decoder.py`: standalone literal decoder and synthetic tests.
- `export_alignment.py`: new presentation-only exporter; no changed readings.
- `HISTORY.md`: dated retrospective search history and withdrawn claims.
- `manifest.json`: submission fingerprints and original snapshot hashes for
  the unchanged files. These establish consistency, not independently certified priority.

The source review snapshot is preserved locally without modification.
Its private-handling README, old manifest, and ignore file are not reused as
current submission metadata. The new README and manifest describe this release.
Historical references to private status in `HISTORY.md` describe that earlier
snapshot. Earlier exploratory solver runs are summarized there; this package
does not claim to rerun the entire candidate-key search.

## Results and limitations

Reviewed input: 754 numeric occurrences, 729 assigned (96.68% coverage),
23 unresolved unmarked groups above 108, and two uncertain numeric tokens.
There are also 25 clear-script spans. Doubtful clear-script words are retained;
the two uncertain numeric tokens are not all uncertainties in the manuscript.
Line 16 is retained; without it the result is 707/732. The continuation is
previously inspected, not held out. No number splits or dictionary guesses
are applied to the baseline.

Controls: 1,000 label-shuffle trials (seed 428424) and 1,000 within-line
mapped-position shuffles (seed 428425). Both exclude repeated line 16 and
preserve coverage. Scoring is exact agreement at 115 positions in four
post-selected excerpts. Observed agreement is 115/115; means are 4.506 and
13.747; both maxima are 24.

**These are retrospective sanity checks, not confirmatory significance tests.**
The expected strings came from the proposed key's output. No independent
language score, prospective selection control, or correction for the
candidate-key search is supplied. This is NOT Cyphersolver's
`docs/_validate.py` test against keys fitted to shuffled ciphertext.
That independent test and an image check are requested, not claimed complete.

AI assisted analysis, code, and drafting in Cursor. The decoder and controls
are deterministic Python computations; they do not generate text with an AI.
No claim of peer review, complete reading, proven priority, or endorsement
is made. Please credit any accepted match to Dolly Moulekhi and the inherited
transcription and groundwork to Daniel Bourdeau / Cyphersolver.
