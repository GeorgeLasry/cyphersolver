# Keys copied verbatim from NOTES.md, section 'The three keys (as he states them)' (22 Oct 2026): Brice Dudout's keys; the same keys are coded in decode.py.
## The three keys (as he states them)

P is the number in the Chinese telegraph code (CTC); none of the keys has been found in a historical code book.

- **共密** (9 telegrams, 555 groups): replace the tens digit t by φ(t), φ = 9 7 6 1 4 0 5 2 8 3; P = (9000 − C′) mod
  10000. Example: 1188, tens 8 → 8, 9000 − 1188 = 7812 黎; 7528, tens 2 → 6, 7568, 9000 − 7568 = 1432 就.
- **容密** (14 telegrams, 1306 groups): per-place digit substitution, thousands 0123456790, hundreds identity,
  tens 0198276543, units 9801723456; P = σ(C) + 0901 mod 10000 with ordinary carries. No group starts 00; the
  encipherer writes 90 instead (thousands 9 → 0). Example: 2081 → 2048, + 0901 = 2949 款; 9084 → 0047, + 0901 =
  0948 國.
- **辰密** (4 telegrams, 239 groups): the CTC reordered. The first two digits give the page, numbered backwards over
  the numbers without a zero (99 = page 00, 91 = 08, 89 = 09 ..., 11 = 80); tens T = 3987102645, units
  U = 1 9 5 4 3 2 6 7 8 10 (units 9 stands for 10 and carries). Example: 9950 4220 6219 → 0001 5281 3500 = 一興灰
  (6219: page 62 → 34, tens 1 → 9, units 9 → 10: 3400 + 90 + 10 = 3500 灰, the day code for the 10th).

