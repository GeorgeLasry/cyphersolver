<!-- Copied verbatim from NOTES.md ("The key"), 22 Oct 2026. The same key is coded in dec.py. -->

## The key

This is a syllabic nomenclator. Every token is separated by a point. There are four kinds of token:

1. **Plain numbers 9–30: single letters.**
   a 9, b 10, c 11, d 12, e 13, f 14, g 15, h 16, i 17, l 18, m 19, n 20, o 21, p 22, q 23, r 24, s 25, t 26, u 27,
   x 28, y 29, z 30.
   In practice these mostly spell closing consonants: n 20, r 24 and s 25 are the three commonest tokens.
2. **Plain numbers 31–60: consonant + vowel syllables, in rows of five (a e i o u).**
   m 31–35, n 36–40, p 41–45, r 46–50, s 51–55, t 56–60.
   Examples: 33 mi, 36 na (also ña), 39 no, 41 pa, 44 po, 48 ri, 51 sa, 52 se.
3. **Struck-through numbers: a second syllable table** (DECODE marks the stroke with "+").
   - t row 15–19 (ta te ti to tu)
   - f row 20–24 (fa … fu)
   - vowel + l 30–34 (al el il ol ul)
   - vowel + s 35–39 (as es is os us)
   - vowel + n 40–44 (an en in on un)
   - vowel + r 45–49
   - que 50, qua 51, qui 52
   - 14 is a word not yet fixed. It comes before -s/-sta, as in "[14]sta mente" and "[14]ticia", so possibly "ju".

   Struck N, R, g and 4 are nulls. They sit mainly at the start and end of each cipher block.
4. **Letter pairs: syllables with the consonant disguised, vowel kept.** Cipher → plain:
   b→c, c→b/v, g→d, l→g, m→l, d→m.
   So ge = de, gi = di, go = do, ma = la, mo = lo, me = le, bo = co, bi = ci, ca = va/ba, ci = vi, la = ga, lu = gu,
   lo = go.
   Special cases: ag = ha, eg = he, e (a separate sign) = lle.
   116 = V.S. (Vuestra Señoría). 8 is used for o.
5. **Three-letter words (code names), read from context:**

   | code | meaning |
   |---|---|
   | sen | el Rey |
   | gin / jin / jen | S.M. / el Rey |
   | gus / mus | Príncipe (de Orange) |
   | quol | Inglaterra |
   | ana | Nápoles |
   | ten / den | Francia |
   | pon | armada |
   | san | Bruselas |
   | tan | Flandes (?) |
   | gon | señor(es) |
   | ran / xan | gobernador |
   | xon | guerra |
   | cun iles | españoles (?) |
   | lun | cart(as) |
   | men / Jen (R1010) | Reino |

   R1010's "gus de s ra n ge s" is Príncipe de Orange, spelled out.

Scripts: `parse.py` reads DECODE's transcription files and `dec.py <record>` prints a reading. The raw machine
readings are in `read/R*.raw.txt`. They inherit DECODE's transcription slips: a few misread numbers show up as
`{..}` or as nonsense syllables.

