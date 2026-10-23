# Re-reading log, Colbert 390 p. 139 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b33)

## Starting point

Reading audit (22 Oct): *decoded, not read*: ll. 1-7 build French sentences, ll. 8-14 are mostly unread runs and code
words. Seven earlier passes (Sept - 5 Oct 2026) are in `c390_p139_v3_reading.md`; blocker recorded then:
no-key-material (the open signs ẟao, aʓ, ā, ℛ, ℞ and the ẟ + superscript code words occur in no glossed passage).

## What was done

1. **Not a DECODE record**: p. 139 is on Gallica only (500 Colbert 390, btv1b10033942k, view 70); no attachment to
   open. Not printed (La Ferrière I-II checked in Sept, `cribs.md`); Tomokiyo lists it as not deciphered.
2. **Whole volume contact-sheeted** (`research/reading_audit/b33_rn_sheet.py`: all 184 views at 600 px through
   openapi.bnf.fr IIIF, 16 sheets; images only in the scratchpad). The September survey (`colbert390_glossed.md`)
   covered views 40-163 for glossed passages; this pass looked for a clear copy or a decipherment of the p. 139 note
   anywhere in the volume. None found: view 70 holds p. 138 (cipher with margin gloss, used for calibration) and the
   inserted slip p. 139; view 71 is the slip's blank verso and p. 141 (a clear letter of Catherine). No other slip, and
   no clear text with *beau frère* / *mon cousin* / *les yeux ouverts* near it.
3. **A key source not yet used** (found while surveying): Catherine's letter of **15 December 1562** to Rennes
   (pp. 115-127, views 58-64, signed Caterine / Bourdin) is in the same cipher hand. Its first ciphered paragraphs are
   written out in clear on p. 118 (*je desire que vous le merciez tant de la part du Roy monsr ... Et fault que je vous
   dye sur ce propos qu'il*), and from there p. 118 lower, pp. 119-121, p. 125 (a full page) and p. 127 (top) are cipher.
   La Ferrière I 449-451 prints these paragraphs "d'après le déchiffrement qui est joint à la lettre" (`cribs.md`
   §1), and Tomokiyo locates a decipherment on p. 120. About four pages of cipher therefore have a full printed
   plaintext. The calibration so far used only p. 138, pp. 189/199 and pp. 221-231 (`colbert390_glossed.md` lists
   pp. 125-126 with "?"). This letter was **not aligned in this session**: it needs a glyph transcription of about four
   pages in the project's token scheme before its sign values can be harvested for p. 139's open signs.
4. **p. 139 looked at again** on native-resolution crops of ll. 6-14 (view 70, x 3500-6320, y 1700-2750): faint ink,
   the same shapes as in `c390_p139_v4.txt`; no new value settles with the current key. Not re-transcribed.
5. **Partial reading written out** (`c390_p139_reading.md`) from `aligned/p139.txt` for the bar measure.

## Measures (reading body, `research/reading_audit/b17_score.py`, LANG_=fr)

- plain 0.25 (2/8 sentences, hole rate 0.212); HOLES=1 0.25 (hole rate 0.195). Below the bar: *decoded, not read*
  kept.
- `_check_reading.py --file aligned/p139.txt` gives 0.90 because it reads each `{n}` run as a code word and each
  manuscript line as a sentence; it is not a reading measure here.

## Still open

- p. 139 ll. 2, 4-5, 8, 10-14 - blocker: not-attempted. The 15 Dec 1562 cipher (Colbert 390 pp. 118-127) with La
  Ferrière's printed decipherment is the next key source: transcribe its cipher, align it with La Ferrière I 449-451,
  and look for ẟao, aʓ, ā, ℛ, ℞ and the ẟ + superscript code words among its signs. What it does not supply stays
  no-key-material.
