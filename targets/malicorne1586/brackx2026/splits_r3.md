# Malicorne r3: shape splits of `F`, `cr`, `Lb`/`Lm` and `y_`

Follow-up to the #92 reply of 23 Oct. The candidates were checked in the order asked: `F` (d / *la*), `cr` (h / s),
`Lb` / `Lm`, `y_`.

**Method.**
1. Cipher lines were found from the row ink profile of the full-size canvases (about 8550 × 6353):
   - canvas 172 left: 31 lines;
   - canvas 172 right: 24 lines;
   - canvas 170 left (f. 162v): 31 lines.
2. In each line band, a template of the sign was matched by normalised cross-correlation. The best peaks were kept,
   as many as the line has tokens of the label.
3. The tiles were laid out in contact sheets grouped by decoded value (`splits_r3/sheet_*.jpg`).
4. Verdicts rest only on clean tiles; tiles that caught a neighbouring sign were discarded.

## Verdicts

| label | values | verdict | evidence |
|---|---|---|---|
| `F` | d / *la* | **no split** | 172 left: 12 *d*, 5 *la*; 172 right: l. 2 *d*, l. 22 *la*. Every clean tile is the same cursive f with a crossbar at mid-stem. No barred and unbarred pair. l. 6 on 172 left is only heavier ink. |
| `cr` | h / s | **inconclusive** | Only *s* tokens were located (172 left ll. 3 ×2, 5, 7), all the dagger-like crossed stroke. No *h* token was located, so the crossed-p form cannot be tied to a value. |
| `Lb` | b / m | **split** | On canvas 172 the *m* tokens are the barred £: 11 of 12 clean tiles (172 left ll. 6, 7, 10, 13, 24, 26–30; 172 right ll. 4, 6). The exception is 172 left l. 31, a looped ℒ decoded *m*. The *b* tokens are the looped ℒ (172 left ll. 2, 23; 162v ll. 15, 30). `Lc` on 172 is the same £, always *m*. |
| `Lm` | m / n | **no split** | On f. 162v the *m* tokens (ll. 4, 12, 14, 15, 21, 25, 26) and the *n* tokens (ll. 12, 15, 21, 27) are the same barred £. The *n* value rests on the decoder alone. |
| `y_` | s | **no split** | The located tokens (172 right ll. 1, 3) are the plain hooked y (*s*). 172 left l. 19 may be the looped ꝩ (*p*); flagged, not relabelled. |

Not covered:
- f. 162v l. 11, an ℒ decoded *m*, stays `Lb` (only one token);
- `Lb` / `Lm` on f. 162r, f. 163 and canvas 171: canvas 169 right gives no reliable line rows, and f. 163 and canvas
  171 were not line-detected (done on 26 Oct; see "Second shape check" below);
- `a2`, `dc`/`dcL`, `zz` and `s` were not in this round's list.

## The `Lb` relabel (r3)

On canvas 172, every `Lb` token decoded *m* becomes `Lc` (barred £, *m*), except 172 left l. 31:
- 19 tokens: 13 on 172 left, 6 on 172 right (`logs/changes_r3.log`);
- the shape was seen on 11 of them; the other 8 follow the same rule unseen.

The new transcriptions are `transcriptions/*_groups_r3.txt`; only the two canvas 172 files change. Re-decoded with
the corrected French model, the text is unchanged letter for letter on all six pages. The relabel moves 19 letters
from a two-valued label to a single-valued one; it does not change a reading.

## Share of letters on two-valued labels

Two-valued share = decoded letters resting on labels with more than one value ÷ all decoded letters.

| page | r2 | r3 |
|---|---|---|
| f. 162r | 15.5% | 15.5% |
| f. 162v | 14.0% | 14.0% |
| f. 163r | 17.0% | 17.0% |
| canvas 171 | 9.8% | 9.8% |
| canvas 172 left | 13.3% | **11.9%** |
| canvas 172 right | 11.1% | **10.3%** |

The readings of f. 162v and canvases 171–172 built on r3 are in `reading_r3.md`.

## `cr` (h / s): second look, f. 163r

Two *h*-valued `cr` tokens were found on f. 163r stretch B (canvas 170 right, full-size IIIF crops): *aux
c[h]arbonnieres* (B l. 3, confirmed by the margin's *charbonnieres*) and *l[h]eur…* (B l. 5). Both are a crossed p
(ꝑ): a round bowl on a stem with a bar through the stem below the bowl. The *s*-valued token next to the second
(`br cr oo`, B l. 5) is a stem with a short bar near the top and no bowl, like the dagger form of the four *s* tokens
on canvas 172. So the two values look like two signs (ꝑ = *h*, dagger = *s*), on 2 *h* and 5 *s* tokens seen. Not
adopted: the *h* sample is too small, and the f. 162r tokens (no usable line rows) were not seen. Recorded as a
probable split.


## Second shape check (26 Oct): f. 162r, f. 163r and canvas 171

The open item of the #92 reply of 26 Oct: `Lb` and `Lm` on the three pages without positions, and more `cr` tokens.

**Method.**
1. **Line rows.** Canvas 169 right is skewed by about 3.5° (the lines rise to the right by about one line across the
   page), which is why its row profile failed. Each cipher block was cut from the full-size IIIF image and deskewed
   at the angle that maximises the variance of the row ink profile:
   - f. 162r: −3.5°;
   - f. 163r: −1.0°;
   - canvas 171 left: −2.25°;
   - canvas 171 right: −2.5°.

   The rows then fall out of the profile: all 27 lines of f. 162r, stretches A (2) and B (8) of f. 163r, and 4 + 16
   lines on canvas 171.
2. **Signs.** Each token of the four labels was found in its line by counting signs from the transcription. The
   transcription of f. 163r and canvas 171 has no dividers, but the page has them, so they were skipped in the count.
   The position was checked on a tile centred on it. All 45 tokens on the three pages were located (11 `Lb`, 3 `Lc`,
   21 `Lm`, 10 `cr`).
3. **Records.** Positions are in `transcriptions/shape_check_r3_positions.tsv`: centre on the original full-size
   image, ±40 px, with the shape seen. NCC was not needed once the lines were level; counting with a tile check was
   enough for every token.

Contact sheets, grouped by decoded value: `splits_r3/sheet_lb_r3b.jpg` (`Lb` and `Lc`), `sheet_lm_r3b.jpg`,
`sheet_cr_r3b.jpg`.

| label | values | tokens (b/m, m/n, h/s) | verdict | evidence |
|---|---|---|---|---|
| `Lb` | b / m | 162r 3/1; 163 3/0; 171 1/3 | **no further split**; one token relabelled | All 7 *b* tokens are the looped script L, except 163 B l. 5, where show-through covers the sign. Of the 4 *m* tokens, one is the barred £ (171 right l. 9): it becomes `Lc`, as on canvas 172. The other three are the same looped L as the *b* tokens (162r l. 7; 171 right ll. 10, 16). So the looped L carries *m* as well as *b*, as on 172 left l. 31 and 162v l. 11; the two values cannot be separated by shape. The tick after the L on 162r ll. 7 and 12 occurs with both values. |
| `Lc` | m | 162r 1; 171 2 | label is not one shape | The two canvas 171 tokens are the barred £. The 162r token (l. 19) is the looped script L, the same as `Lb`. Relabelling it `Lb` would let the decoder pick *b* in an unread word (*commanlt* → *combanlt*), so it is left as `Lc` and flagged. |
| `Lm` | m / n | 162r 8/3; 163 1/3; 171 3/3 | **no split** | All 21 tokens are the same barred £, as on f. 162v. The *n* value rests on the decoder alone. |
| `cr` | h / s | 162r 1/1; 163 2/4; 171 1/1 | **no split** (a dagger relabel was tried and reverted on review) | Wider crops (520 × 260 px) show three forms. Crossed p (ꝑ): 3 *h* (162r l. 27, 163 B ll. 3, 5) and 2 *s* (162r l. 7; 163 B l. 4, in *[tou]tes forces*). Crossed v (a v with a bar, on a stem or not): 1 *h* (171 left l. 3, sign 10) and 2 *s* (171 left l. 3, sign 4; 163 B l. 6, second token). Dagger: 1 *s* (163 B l. 5). The sixth *s* (163 B l. 6, first token) is struck through. Neither the crossed p nor the crossed v keeps to one value, so the shapes do not separate *h* from *s*. |

The four canvas 172 left tokens taken as daggers in the first round (ll. 3 ×2, 5, 7) are, on `sheet_cr_172l.jpg`, a cross with a bulb (l. 3 ×2), a cross like the `+` sign (l. 7) and an unclear form (l. 5), so they do not make the dagger a separate *s* sign either.

### Relabel (r3, updated 26 Oct)

One token changes (`logs/changes_r3.log`, second block): `Lb` → `Lc` on canvas 171 (right l. 9, the barred £). Seven `cr` → `cd` relabels (a dagger label) were made and then reverted on review; the log records both. The r3 transcriptions are updated in place, with a header line naming the change. No new label, so the key is still `keys/key_r2.json`.

Re-decoded with `tools/align.py`, `keys/key_r2.json` and the corrected French model (Montaigne, *Essais* I–III,
Gutenberg 48529, 49168, 58801, built with `tools/lm.py`), the text is unchanged letter for letter on all six pages.
The f. 163r crib agreement (A, B1–3, Bx) is therefore unchanged.

### Share of letters on two-valued labels, recomputed

The share is letters on labels with more than one value ÷ all decoded letters. Both columns come from the same
script. For f. 162r and f. 162v the r3 figures in the table above are 0.1 point lower than recomputed here.

| page | r3 (recomputed) | r3, 26 Oct |
|---|---|---|
| f. 162r | 15.6% | 15.6% |
| f. 162v | 14.1% | 14.1% |
| f. 163r | 17.0% | 17.0% |
| canvas 171 | 9.8% | **9.6%** |
| canvas 172 left | 11.9% | 11.9% |
| canvas 172 right | 10.3% | 10.3% |

