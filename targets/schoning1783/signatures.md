# Numeric signatures and the s029 address panel (26 Oct 2026)

ASCII only. Digits are written as the digits they look like; the few non-digit signs get labels:
SQ = small square (closed box, sometimes with a short tail), TR = small triangle, H = capital-H-like sign,
DOT = filled round blot, + = plus sign. `.::` is the closing dot cluster.

## 1. The signatures

Every letter Schoning signs "en chiffre" closes with the clear formula "Votre tres humble et tres obeissant
serviteur", then two or three rows in a mixed digit-and-sign script, then the date in clear. Crops checked at 3-5x on
five letters:

| scan | date | transcription (rows joined with /) |
|---|---|---|
| s001 | 28 July 1783 (No. 1) | 8 SQ TR 9 7 H 3 0 9 6 0 5 3 4 + 5 9 6 3 8 7 9 9 SQ .:: (one row) |
| s025 | 16 Aug 1783 (No. 6) | 8 SQ TR 9 1 + 3 TR 3 9 TR 9 4 H 3 DOT 4 6 0 / 5 3 7 + 5 9 6 3 8 7 9 9 SQ .:: |
| s142 | 9 Jan 1784 | 8 SQ TR 9 1 + 3 TR 3 9 TR 9 7 / H 3 0 4 6 0 5 3 9 + 5 9 6 3 / 8 7 9 9 SQ .:: |
| s205 | 10 July 1784 | 8 SQ TR 9 1 + 3 TR 3 9 TR 9 7 / H 3 0 9 6 0 5 3 9 + 5 9 6 / 3 8 7 9 9 SQ .:: |
| s154/155 | 15 Jan 1784 | (dec_154.tsv: third row "8799" + dots; same form) |

Canonical form (s142, s205; s025 differs only in single strokes, 4 for 7/9 and a blot for 0):

    8 SQ TR 9 1 + 3 TR 3 9 TR 9 7 H 3 0 9 6 0 5 3 9 + 5 9 6 3 8 7 9 9 SQ .::

s001 (the first letter) is the short form: it lacks the stretch `1 + 3 TR 3 9 TR 9` and has one `+` only.

### What they are

- A fixed signature formula, not numbering: the same 30-31 signs recur from July 1783 to July 1784 with only
  pen-slip variation (4/7/9 and 0/blot in two places). It is not a date (the date stands beside it in clear) and
  not one of the letter-body code numbers (862 = Schoning in the code does not occur in it).
- It is not a letter-for-letter substitution of Schoning's name in any form: sign 9 stands 8 times in 30 signs
  (27%), and 3 five times. No form of "Gotthard (Baron) von/de Schoning", "G. B. de Schoning", "G. de Schoning"
  has one letter 8 times, and the last group `5 9 6 3 8 7 9 9 SQ` cannot be "Schoning" or "Schoening" under one
  sign per letter (the repeated n's would fall on different signs, and 9 would have to be c, i and n at once). So 9 (and perhaps 3) are either nulls/fillers or the
  script is syllabic or a flourish.
- Nor is it the letter-body symbol alphabet (G01-G24): the signs are ordinary-looking digits plus three box/triangle
  marks, and reading the digit look-alikes through the G table (3 as G07 e, 7 as G18 s, 0 as G02 n, + as G23 h)
  gives no French or German.
- No clear equivalent survives: the decipherer's copies and Larrey's dossier never write the signature out, and
  no signature in the file carries a gloss. With one fixed 30-sign string and no crib, the mapping cannot be
  recovered. It is plainly Schoning's own name or paraphe in a private form (it stands where the name goes, and in
  s001 the short form is used before he took to the full one), but it is **transcribed, not read**.

## 2. The s029 address panel

s029 is the outer leaf of the Nordhausen letter of October 1783 (s027). The address is written across the fold,
turned 90 degrees (read it with the page rotated a quarter turn counter-clockwise), with a large "8" in a
hatched (double-ruled #) box to its left: probably the letter's running number or a carrier/postage mark; it is
in the same ink.

The address itself is **not** in the digit script of the signatures and **not** in the letter-body G alphabet. It is
a third, cursive sign set: horizontal waves, arch-and-cup waves, slanted strokes, a T-shaped stroke with a curled
foot, an S-curve and a crossed stroke, with dots above or below and one bar above serving as diacritics. Labels
(A01-A10) and the sequence, left to right:

- A01 arch with a dot below; A02 plain horizontal wave; A03 slanted stroke; A04 T with curled foot; A05 slanted
  stroke with a crossbar; A06 arch-and-cup wave (two humps); A07 S-curve (upright); A08 crossed stroke (long
  slanted stroke crossed by a short wave). Diacritics: `'` = dot above, `,` = dot below, `^` = bar above.

```
line 1: A01, A02 | A03' A04 A03 A04' A05 A03:(two dots) A03' | A02 A04 A02', A06 A04'
line 2: A02 A02, A06 A06, A07 A06, A06' A08 A06 A06'
line 3: A03 A02^ A02, .::
```

About 33 signs. It ends with the same `.::` as the signatures. Tested: no repeat matching "Monsieur / Monsieur"
(which would give a 7-8 sign repeat on lines 1-2), and the G table gives nothing. The clear addresses elsewhere in
the file (s103: Mr G. C. van der Hoop, advocate-fiscal, Amsterdam) do not fit the sign pattern letter for letter
(line 3 has three signs, too short for "Amsterdam"), so the panel may carry a cover name or address. With 33 signs, a
new sign set and no crib, it is **transcribed, not read** (blocker: too short, no key).

## Result

- Signatures: a constant signature formula in a private digit-and-sign script, 5 instances transcribed; not a
  simple substitution of the name; unread (no crib, too short).
- s029 address: a third sign set, transcribed with labels A01-A08; unread (too short, no crib).
- Neither affects the letter texts: both stand outside the cipher passages and are left out of measure.py.
