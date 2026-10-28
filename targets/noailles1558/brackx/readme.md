# noailles1558: tools and counts

**Tools.** The transcription, the sign labels and positions, the key, the decodes and the readings were made with
Claude Code (Anthropic, model Claude Opus 5.5), directed by Michael Brackx, working on the BnF IIIF images of fr. 3151
(Gallica btv1b9059865k, views 61-62, full size 7930 x 5655). Signs were read on enlarged tiles of those images. The
scripts are Python 3: `decode.py` (plain decode), `tvd.py` (the T/V/D file and the key TSV here). Key recovery used
`crib_anneal.py` (alignment with the marginal gloss) and `lm_anneal.py` (a French 5-gram model trained on Montaigne's
*Essais*, Project Gutenberg, to fill values the gloss does not fix); both are in the local working folder and can be
added on request.

**Counts from these files** (`tvd.py`, key round 5): 272 sign tokens in blocks A, B and C, of which 12 are nulls;
244 of the 260 non-null tokens have a value (93.8%), 12 of them on tentative values (11 labels). The counts posted in
the issue (246 of 262, 16 tentative) were made at round 7 with a slightly different token count; these files are the
reference.

**Files.**
- `transcription_f60r_f60v.txt`: blocks A, B (f. 60r) and C (f. 60v), one line per cipher line, labels in reading order;
  the header gives the shape behind each label.
- `positions_f60r.txt`, `positions_f60v_C.txt`: x centre of each sign on the full-size image, same order; y from the
  line centre and slope.
- `legend.md`: label → shape → value.
- `key_r5.txt` (with the words that fix each value) and `key_r5.tsv` (label, value, firm/tentative, tokens, basis).
- `decode_tvd_r5.txt`: the raw decode, T (labels) / V (values, `{x}` tentative, `0` null, `?` none) / D (letters).
- `reading_original.md`: readings of A, B and C in the writer's spelling, holes sized, tentative values braced;
  `translation_en.md`: English.

