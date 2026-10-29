# Image126 reinspection and alignment limits

Reinspected the middle paragraph at full resolution on28October2026. The French text remains a preliminary reading. The numerical text in `image126_pair.json` must not be treated as exact.

Potential transcription disagreements that require another reading:

- Row1, group1: `100` has an adjacent pen stroke; do not infer1100 from it without checking other occurrences.
- Row2, group6: provisional247 may be257.
- Row3, group1: provisional583 may be653; writing overlaps the fold and the French.
- Row3, group7: provisional215 looks like218 on enlargement.
- Row5, group1: provisional609 may be602.

No candidate variant was selected because it improves a desired alignment. The earlier experimental JSON remains unchanged so its existing results stay reproducible. These disagreements further limit any negative result on that pair.

`cp_align.py` adds an exact finite-domain alignment model (OR-Tools9.15.6755). It can find a formal alignment on the synthetic135-group/301-letter control, but an arbitrary solution recovers too few true values. The lexical version recovers80% of control token values, below the95% key-recovery standard used here. Thus it is not a validated key-recovery method.

The unrestricted real-text model also fits, but assigns implausible chunks that run across several words. This is overfitting, not a decipherment. Restricting pieces to short attested table values and French words gives INFEASIBLE on eight specific prefix choices with three trailing groups excluded. Those verdicts apply only to that restricted model, that provisional transcription, and exact written spelling. They do not exclude alternate values, variants, nulls, phonetic conventions, errors, or an indirect relation between the two texts.

The independently matched1771 example in `KEY219_PROVENANCE.md` shows that a literal key output can require doubled-consonant normalization. This is a concrete reason to avoid treating exact spelling as an established property of the1765 passage.

One deterministic shuffled-order control, preserving group frequencies, was INFEASIBLE under the unrestricted model (seed450). The actual provisional order fitted. This limited comparison does not establish historical equivalence, statistical significance, or a recovered key; the unrestricted synthetic-control key accuracy was only42.96%.
