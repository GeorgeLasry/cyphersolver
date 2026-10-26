# Three-hundred-and-sixty-first registered predictions: goal loop 7, two context features

## CX1 a skip-bigram
- fixed test S 4.5956 -> 4.5956 (gain 0.0000, weight 0.00).
- A -> B 5.0891 -> 5.0891 (gain 0.0000, weight 0.00).
- **CX1 fails.**

## CX2 previous sign x distance from the end
- fixed test S 4.5956 -> 4.4428 (gain 0.1528, weight 0.40).
- A -> B 5.0891 -> 5.0319 (gain 0.0572, weight 0.50).
- **CX2 holds.**

## P progress rule: either hypothesis holds
- CX1 False, CX2 True.
- **P holds.**

## Summary

Held: CX2, P. Failed: CX1.
