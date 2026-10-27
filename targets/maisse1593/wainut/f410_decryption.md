# f. 410, Henri IV to Maisse, Mantes, 27/28 Apr 1593: cipher decrypted line by line (first two lines only)

WAINUT, 27 Oct 2026. Tokens from `cipher_lines.txt`; values from Tomokiyo's "Maisse' Cipher 2"
(`../src/henryiv_Maisse2.png`); `python decode_check.py` reproduces the letter strings and the controls.
Word signs in capitals. `[?]` = a sign whose value does not fit the copy, or an uncertain transcription.
Only the first two cipher lines (lines 10-11 of the leaf) are decrypted. About 23 further cipher lines are not
transcribed. The text of the whole block is known from the contemporary clear copy (`f410_brienne_copy.txt`,
fol. 193v-194v).

| leaf, line | tokens | decryption | clear copy (Brienne 13 fol. 193v) | English |
|---|---|---|---|---|
| f. 410, l. 10 | q~ 27 29 14 E~ to 19 f_ rho 9t E~ z 15 / 23 y uy 24 26 y 2+ 10 d 8 E~ / que 8 6 f_ 17 18 27 10 E~ 26 8 phi 27 26 d | l e x p e r i e n c e a FAICT c o u g n o i s t r e QUE r[?] u[?] e[?] VOUS EST e s e n r i e n t | L'experience a faict cognoistre que vous ne vous estes [estes] en rien t[rompé] | Experience has shown that you were in no way mis[taken] |
| f. 410, l. 11 | 16 x E~ D~ uy 2+ uy 24 E~ 16 0 26 d que 17 E~ 26 z uy 0 my de~ 7 y 26 24 d E~ UNK x 10 15 desp | m p e d u i u g e m e n t QUE VOUS e n a v e z DE l o n g t e [?] p s FAICT DES | (trom)pé du iugement que vous avez de long temps faict des [affaires de Rome] | in the judgement that you formed long ago of [the affairs of Rome] |

Notes on the lines:

- The cipher starts immediately after the clear words "de ma bonne grace et faveur".
- *cougnoistre*: the sign after *co* is the uy sign (u), so the cipher spells *cougnoistre* (a spelling variant or
  a clerk's slip) where the copy has *cognoistre*.
- *rience a*: `9t` (the crossed g-like sign) is c in the key, `f_ rho` are two signs (e, n) and `z` is a.
- *que vous ne*: the three signs `8 6 f_` that stand where the copy has *vous ne* decode as r u e. Either they are
  misread or they are a word sign missing from the key. Left as holes.
- *que vous en avez*: the cipher has *en*, the copy does not. The copy repeats *estes* ("vous estes estes"); the
  cipher does not.
- The hooked q-like sign that opens both blocks is in Tomokiyo's l column (row 2); it is not a new homophone. The
  *que* sign is a 9 with a straight tail; the two signs look alike.

Values confirmed on these two lines: 27/e, 29/x, 14/p, to/r, 19/i, 23/c, 24/g, 26/n, 10/s, 8/r, 7/l, 16/m, 1/o, y/o,
the x-like sign = p, the d-shaped sign = t, the crossed 2 = i, the z-like sign = a; word signs 15 = *faict*,
17 = *vous*, 18 = *est*, *que*, *des* (p with a stroke) and *de* (looped sign).

Controls (`decode_check_output.txt`): ratio 0.94 (l. 10) and 0.93 (l. 11) against the copy; 2000 random
permutations of the key values give at most 0.53 and 0.49, and 2000 shuffles of the group order at most 0.65 and
0.61.
