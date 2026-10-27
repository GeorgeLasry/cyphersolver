# f. 406 (twin f. 404), Henri IV to Maisse, Chartres, 8 Feb 1593: cipher decrypted line by line (first lines only)

WAINUT, 27 Oct 2026. Tokens from `cipher_lines.txt`; values from Tomokiyo's "Maisse' Cipher 2"
(`../src/henryiv_Maisse2.png`); `python decode_check.py` reproduces the letter strings and the controls.
Word signs in capitals. `[?]` = a sign whose value does not fit the copy, or an uncertain transcription.
Only the start of the cipher block is decrypted. About 18 further cipher lines of f. 406 (and the verso, canvas 458,
if it carries cipher) are not transcribed. The text of the whole block is known from the contemporary clear copy
(`f406_brienne_copy.txt`, fol. 172r-172v).

| leaf, line | tokens | decryption | clear copy (Brienne 13 fol. 172r) | English |
|---|---|---|---|---|
| f. 404, l. 3 | q~ 27 10 uy 8 14 7 6 w D~ 27 | l e s u r p l u s d e | Le surplus de | The rest of |
| f. 406, cipher l. 1 | 7 E~ 10 uy 8 x q~ 5 w 25 27 6 y my 7 8 E~ 10 18 10 uy to 7 E~ 10 | l e s u r p l u s d e v o z l r e s EST s u r l e s | Le surplus de voz lettres est sur le s[ubiect] | The rest of your letters concerns the [subject] |
| f. 406, cipher l. 2, start | 2+ 0 23 d desp z T | i e c t DES a f | (sub)iect des af(faires) | (sub)ject of the af(fairs) |
| f. 406, cipher l. 2, later | de~ to pi 16 27 25 6 uy 1 + 2 24 E~ | DE r r[?] m e d u v o a[?] a g e | de Rome du voiage | of Rome, the journey |

Notes on the lines:

- f. 404 l. 3 is the same despatch sent by the other route. Its first eleven signs give *Le surplus de* exactly.
- f. 406 cipher l. 1: the cipher writes the abbreviation *l[ett]res* (l r e s), where the copy has *lettres*.
- f. 406 l. 2, *Rome*: the pi-like sign is r in our reading of Tomokiyo's key, which gives *rrme*. The value o for it
  is not supported by the key, so the sign is left as a hole.
- f. 406 l. 2, *voiage*: the `+` sign is a by the key, but the copy and the sense need i. Left as a hole.
- f. 406 itself was checked, not only its twin f. 404: the cipher begins on the line after "faire des bons advis que
  vous y pouvez apporter", as on f. 404.
- A short run of cipher groups stands on an earlier line of f. 406, inside the clear part of the letter. It was
  seen but not decrypted.

Controls (`decode_check_output.txt`, difflib ratio between the decryption and the copy): f. 404 l. 3 1.00;
f. 406 cipher l. 1 0.91; l. 2 start 1.00; l. 2 later 0.79. With 2000 random permutations of the key values the best
ratio on any of these lines is 0.67, and 0.56 or lower on the two longer ones. The short stretches (7 and 11 signs)
prove little alone, but they agree with the long ones and with f. 410.
