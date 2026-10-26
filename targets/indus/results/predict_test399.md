# Three-hundred-and-ninety-ninth registered predictions: goal loop 45, WORD with a city prior

- fixed (232 names): without prior top-1 0.0% / top-10 4.7%; with city prior 0.9% / 4.3%.
- A -> B (299 names): without prior top-1 1.7% / top-10 5.0%; with city prior 1.0% / 4.7%.

## WL1 the city prior raises WORD top-10 on both splits
- 11 -> 10, 15 -> 14.
- **WL1 fails.**

## WL2 the city prior raises WORD top-1 on both splits
- 0 -> 2, 5 -> 3.
- **WL2 fails.**

## P progress rule: WL1
- WL1 False.
- **P fails.**

## Summary

Held: none. Failed: WL1, WL2, P.
