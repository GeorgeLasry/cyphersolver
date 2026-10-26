# Four-hundred-and-twenty-second registered predictions: goal loop 68, WORD with a subtype prior

- fixed (232 names): without prior 0 / 11; with subtype prior 1 / 11 (top-1 / top-10).
- C (211 names): without prior 0 / 1; with subtype prior 0 / 1 (top-1 / top-10).

## WK1 the subtype prior raises WORD top-10 on both splits
- 11 -> 11, 1 -> 1.
- **WK1 fails.**

## WK2 the subtype prior raises WORD top-1 on both splits
- 0 -> 1, 0 -> 0.
- **WK2 fails.**

## P progress rule: WK1
- WK1 False.
- **P fails.**

## Summary

Held: none. Failed: WK1, WK2, P.
