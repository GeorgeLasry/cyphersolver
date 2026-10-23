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

# r2j (23 Oct 2026, Claude Opus 5.5): the 15 Dec 1562 letter as a key source

1. **Where the cipher is.** Colbert 390 views 58-64 at full size (IIIF `full/max`, 6336 x 4736 spreads): the 15 Dec
   1562 letter has cipher on p. 117 (last five lines, after the clear "Et pource Monsr de Renes que"), p. 118 (22 lines
   after the clear "... sur ce propos qu'il y"), p. 125 (a full page, about 35 lines) and p. 126 (eight lines, then the
   clear end "Quant au memoire que Federich Spel ..." and the signatures Caterine / Bourdin). pp. 119-121 are a cursive
   clear text in another hand (the decipherment joined to the letter, which La Ferriere printed); pp. 122-124 blank.
2. **Transcribed and aligned**: pp. 117-118 in full, 27 lines, 949 signs (`c390_1562-12-15_cipher.txt`, token names
   as in `c390_p139_v4.txt` where the shape is the same), against La Ferriere I 449-450 (`c390_1562-12-15_plain.txt`,
   public domain, archive.org OCR checked). Hard-EM alignment (`research/reading_audit/r2j_rennes_em.py`, adapted from
   matignon1586c3's align_em.py): 852 signs align to letters, 81 to code words or doubled letters, 16 nulls; 101 printed
   letters have no sign (signs missed at the half-line crop edges). Table: `c390_1562-12-15_em.txt`.
3. **Values in this hand, measured** (count of aligned places): ∂ (p.139's *th*) = m 26/31; ẟ (5-shape with a top
   loop, *ds*) = r 12/13; ā (*at*) = g 7/7; ƀ (*xi*, the b-like e) = e 17/20 and plain b = p 3/3; ♯ (*sh*) = y 13,
   et 6, est 6; + (*plus*) = f 16, s 3, x 2; ꞓ (*C*) = o 44, h 3; €/ɛ (*E*) = h 3, ff 2; ʒ (*zs*) = s 21, c 3; ſ
   (*S*) = a 8; ɱ (*mJ*) = i 10/10; ⅄ = p 6/7; δ with a tick = b 6/6; θ = z/s; ℒ = *dict* 7/8; ꝩ = *(le) roy des
   Romains* 3/3; ∂a = *Allemaigne* (once); qq = que, 8 = luy, A = mais, ca = faire, tu = faict, ϯL = bien, > / 7 =
   nous, V̄ = qui, ⊥⊥ = pour, ꝑ = et, N = ll, ƀƀ = ss. These confirm the P139 table of `measure.py` (th = m, at = g,
   R = r, sh = y|et, mJ = i) and add ẟ = r, + = s, ꞓ = h, ʒ = c, ♯ = est.
4. **pp. 125-126 inspected, not transcribed** (bands at 2000 px): the same sign inventory as pp. 117-118. **None of
   p. 139's open signs occurs** in the 15 Dec cipher: no ẟao, aʓ, ℛ, ℞ and no ẟ with a superscript; ā is g, not
   *par* or *et*. The letter therefore supplies values for the common signs but not for p. 139's code signs.
5. **p. 139 retried** with the widened table (`research/reading_audit/r2j_p139_lattice.py`, a word lattice over
   `c390_p139_v4.txt`, Henri IV + 1520s despatch vocabulary): *fils* is now carried (+ = s); l. 8 *[?voyaige]* proposed
   for ſ λ ſſ ♯ z k ß … x1 (ß = g as in Tomokiyo's beta, but ß = l in *loyal* l. 2 and on p. 138; the sign after
   the null // is unread): "pour obseruer come totes [?choses] passeront en ce [?voyaige] de mon cousin", the Cardinal
   of Lorraine's journey that the 15 Dec letter calls "leur voyaige". No other run closes: l. 2 ā before *loyal*
   gives g, not *et*; l. 4 "ſ ɱ z ʓ G k ẓ" (a i a r t i -), l. 8-9 "♯ qq N d ʒ ¢ La ʓ ẟ ẓ" (et que lles s d r r),
   l. 12-14 runs with ẟao and aʓ.
6. **Score**: `v2_score.py` fr 0.25 (2/8), explicit holes 0.25, hole rate 0.276 -> 0.265. Stays decoded, not read.

## Still open (r2j)

- p. 139 ll. 2, 4-5, 8, 10-14 - blocker: **no-key-material**. The 15 Dec 1562 letter, the only deciphered text in the
  volume in this cipher besides the glossed p. 138 and pp. 189-231, has been aligned (pp. 117-118, 949 signs) and inspected
  (pp. 125-126): it has none of the signs these runs need (ẟao, aʓ, ℛ, ℞, ẟ + superscript), and the common-sign
  values it measures do not close them.
