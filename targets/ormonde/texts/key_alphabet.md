# Alphabet copied verbatim from NOTES.md, section 3 'Structure' (22 Oct 2026).
## 3. Structure (from [analyze.py](analyze.py), output in [analyze_out.txt](analyze_out.txt))

* **91–111 are nulls.** Nine distinct values (93 95 97 98 99 100 103 108 111), each used 1–4 times, and 17 of 18
  occurrences sit at the edge of a cipher run or immediately beside a ≥112 code (`93 185 95`, `99 149`, `95 186 98`,
  `98 218 97`, `100 174 103`, `111 95 221`, `186 99`). Tomokiyo's guess is confirmed.
* **≥112 are nomenclator codes** (113 143 149 174 185 186 218 221 270): each stands alone between nulls or clear
  text, and 270 is explicitly *introduced* ("for whom 270 thus hereafter").
* **< 91 are letters**, and the letters are the key to the whole thing: the four spelled runs contain doubled letters
  written with *consecutive* figures — `49 50`, `69 70`, `28 29`, `11 12` — i.e. each letter owns a block of
  consecutive figures. Cribs:

  | figures | reading | context |
  |---|---|---|
  | 28 69 49 50 70 44 (89) | l e t t e r (s) | "brought no letters from [the Lord Deputy]" |
  | 11 79 85 35 12 69 28 29 79 44 | c o u n c e l l o r | "upon his motion [Ormonde] is to be a councellor" (Ormonde sworn PC Jan 1635) |
  | 10 44 79 47 8 59 | C r o s b y | Sir Piers Crosby, who fell out with Wentworth in the 1634 Parliament and was put out of the Irish Council early in 1635 ("like to go worser with him") |
  | 64 | a | "is to be **a** [null] councellor" |
  | 65 35 21 26 59 | a n g [k] y | "he was angry [with] the Lord Deputy" — see §5 |

  All of these are consistent with **one regular key**: the 19 consonants of the 24-letter alphabet
  (b c d f g h k l m n p q r s t w x y z; i=j, u=v) in alphabetical order, **three figures each, starting at 7**,
  followed by the vowels from 64:

  ```
  b 7-9   c 10-12  d 13-15  f 16-18  g 19-21  h 22-24  k 25-27  l 28-30  m 31-33  n 34-36
  p 37-39 q 40-42  r 43-45  s 46-48  t 49-51  w 52-54  x 55-57  y 58-60  z 61-63
  a 64-..  e ..69,70..  i ..  o 79-..  u 85-..      (vowel block sizes not fixable: 5 each = 64-88, or a=3/others 6 = 64-90)
  91-111 nulls        112+ nomenclator (names/words)      1-6 unknown (nulls or "&"/"the"?)
  ```
  Every letter-figure in the text falls where this grid predicts (b8 c10-12 g21 l28-29 m31 n35 r44 s47 t49-50 y59
  a64-65 e69-70 o79 u85); the only misfit is 26 (see §5). An exhaustive scan of regular grids (start 1–11, block
  2–4, uniform vowel blocks 2–6; 42 grids) ranks start=7/size=3 first by English quadgram score.
* Tomokiyo's "44 79" / "79 44" are simply **r-o** (C**ro**sby) and **o-r** (councell**or**).

