# Malicorne to Henri III, Niort, 21 April 1586 (BnF fr. 15572 ff. 162–164): aligned decode, other pages

The raw decode aligned with the transcription for the four cipher pages not included in the #92 comment
(f. 162r and f. 163r are there), and the label → shape legend.

| file | page | canvas | lines |
|---|---|---|---|
| `f162v_aligned.md` | f. 162v | 170 left | 31 |
| `c171_aligned.md` | canvas 171, left block and right block | 171 | 4 + 16 |
| `c172l_aligned.md` | canvas 172 left | 172 left | 31 |
| `c172r_aligned.md` | canvas 172 right | 172 right | 24 |
| `legend.md` | every label: count, value(s), sign shape, basis | | |

**Format.** For each cipher line: `T` the transcription, one label per sign (`|` is the word divider on
f. 162 and f. 172 right); `V` the raw decode sign by sign as `label=value`; `D` the decoded line.

**Notation in `V` and `D`.** `[|]` the divider; `[x]` a sign with no value in the key (unread); for a label with two
values the decoder's choice is shown, picked by the language model. Nothing is edited by hand: the readings that
depart from this decode are listed in the #92 comment.

**Decoder.** Beam search over each label's allowed values (key of round 2) under a French character 5-gram built from
Montaigne's *Essais* I–III (Project Gutenberg 48529, 49168, 58801).

Images: Gallica / BnF IIIF, ark `btv1b9061879d`, canvases 169–172.

