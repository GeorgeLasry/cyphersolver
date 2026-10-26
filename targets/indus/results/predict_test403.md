# Four-hundred-and-third registered predictions: goal loop 49, jointly fitted and per-group weights

- fixed: sequential base 4.5590; joint weights 0.5 0.1 0.0 0.2 0.2 -> 4.5577.
- fixed: plain + subtype (global weights) 4.5915; with per-group weights 4.5887.
- C: sequential base 4.5360; joint weights 0.5 0.0 0.0 0.3 0.2 -> 4.5401.
- C: plain + subtype (global weights) 4.5600; with per-group weights 4.5597.

## JW1 jointly fitted weights lower S (0.005 fixed, any on C)
- 4.5590 -> 4.5577; 4.5360 -> 4.5401.
- **JW1 fails.**

## JW2 per-group component weights lower S for the subtype model
- 4.5915 -> 4.5887; 4.5600 -> 4.5597.
- **JW2 fails.**

## P progress rule: either holds
- JW1 False, JW2 False.
- **P fails.**

## Summary

Held: none. Failed: JW1, JW2, P.
