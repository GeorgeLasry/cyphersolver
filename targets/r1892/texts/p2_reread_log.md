# Re-reading log, R1892 page 2 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b31)

## Starting point

Reading audit (22 Oct): page 2 (Dutch postscript) "decoded, not read": `decrypt_p2.txt` unspaced, an open word sign or a
bracketed conjecture in almost every line. WAINUT's proposals of 12 Oct (NOTES) were recorded but not adopted, pending an
image check of their shape splits.

## 1. Is there a text already? No

- **DECODE R1892** fetched logged in 23 Oct 2026 (`research/reading_audit/b31_fetch.py`): two images only
  (`IMG_R1892_I9358_P1.png`, `..._I9359_P2.png`, the same files as `img/`), no document, no transcription, no key;
  "Additional information" names R2242 as related. **R2242** fetched too: four images, no document. No key sheet on
  DECODE under another name (R2233, R2240 checked 2 Oct; R2236-R2239 use a different word list). Print: Colenbrander,
  Gedenkstukken, searched 2 Oct, not printed.

## 2. Image check of WAINUT's shape splits (rot_IMG_R1892_I9359_P2.jpg, band crops in scratchpad `reread/r1892/`)

- The `<H>` label covers two shapes: a **long horizontal stroke run into a double-barred H** (ll. 4, 5, 7, 8, always
  before *willen*) and the **I-beam** (short bar, stroke, short bar: ll. 15, 20, 21, and the `<hook>` of l. 4), which is
  the shape of l. 9's bar-H (*zoo*). Split confirmed.
- l. 13 *mynnader*: the bottom digit of the fourth pair is 3, not 2: **myn vader** (pair 33).
- l. 15: the sign before *antwoord te laten* is the same crossed Y as at ll. 17, 18, 22 (checked).
- G (C with an inner loop) and the flat-legged hook: one shape each across their occurrences (labels of
  `transcription_p2.txt`, not split).

## 3. Values: adopted only where they hold at every occurrence

| sign | value | occurrences | decision |
|---|---|---|---|
| I-beam (incl. l. 9 bar-H) | zo / zoo | 4, 9, 15, 20 (zoude), 21 (zo kun; zoude) | **adopted** (shape = l. 9 *zoo* and R2242's zo) |
| G | UE | 8, 12, 13, 16, 17, 21, 24 | **adopted, sense-only, flagged**: l. 24 *waaraan UE ... bloodgesteld is geweest* (3rd person) and l. 17 *dat ik UE myn eerste brief* exclude *ik* |
| flat-legged hook | dat | 8, 16, 17, 20, 21, 22 | **adopted, sense-only, flagged** (a second sign for *dat* beside Λ) |
| c-symbol | zal | 4, 6, 9, 12, 13 | **adopted, sense-only, flagged**; the old *te* fails at 4 (*zo te W.*) and 12 (*te UE*) |
| looped stem (phi, psi l. 20) | uit | 9, 13, 20, heading *uit Hampton Court* | **adopted** |
| crossed Y | ik | 13, 17, 18, 22 fit; **15 does not** (*gedaan [cf] [Y-cross] antwoord te laten*) | not adopted: `[?ik]` |
| gamma (curl) | zulks | 6, 20 fit; 10 (*alleen [γ]e te zyn*) does not | not adopted: `[?zulks]` |
| cf | zyn | 15, 16, 19, 21; l. 19 awkward | not adopted: `[?zyn]` |
| slash (dotted stroke) | aan | 11, 24 fit; 16 unclear | `aan` at 11, 24 (same shape as f = aan); `[?aan]` at 16 |
| 8 (∞ shape) + trident, delta, cross, I, check | daar, over, kan, mogelyk, Engeland, van | one context each | not adopted |

## 4. Reading and scores

`p2_reading.md` (word-divided, Dutch spelling as the pairs give it), `p2_en.md`, corrections in `p2_corrections.tsv`.

| | clean-sentence share |
|---|---|
| before | no word-divided text |
| b17 plain (`LANG_=nl`) | 0.10 (3/30) |
| b17 `HOLES=1` | 0.60 (18/30), hole rate 0.14 |

Look-alike letters: 0. Reader's judgement: from *Al het gene wat UE in [...] cyffer zal vinden* to the end the
sentences build (a few `[?…]`); the first half (ll. 2-12: who is to be named, employed, given fixed days) has two to five
open signs per sentence and does not build. **Kept decoded, not read**, at the bar on the score but not on the reading.

## Open

- long-dash H (4), S (3), 7 (2), Y (3), bar, slash l. 6, x, delta, A, 3, 9, Z, circle-cross, 8 of l. 19, the sign
  before *dert*: blocker no-key-material (no key sheet; R2242 lacks them; single or few contexts).
- crossed Y, gamma, cf: values fit all but one occurrence; blocker no-key-material (a contradicting context, no sheet).
