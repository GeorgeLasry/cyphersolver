# Many routes to one reading

Status: in progress (protocol written 23 Oct 2026; no runs yet)

Tao (Nature 658, 1103, 22 Oct 2026) suggests that a result reached by many independent routes shows which ideas
are essential to it and which belong to one particular proof. For us: read the same letter several independent
ways, and see what evidence actually breaks a historical cipher. That is a paper section for the work with George
Lasry, and an answer to "proof indigestion", because each route is a separate, checkable account of the same reading.

## Targets

Five, chosen because each was read by one route and has the material for the others, and each has a valid profile
and a published page. Lengths come from the profiles; re-measure with `docs/_check_profile.py --measure` before a run.

| target | how it was read | routes to add |
|---|---|---|
| gramont1529 | Lasry's GL.htm key applied (read with known key) | ciphertext-only anneal on the 4,002 signs; crib from the docket |
| bay1706 | G15 key R609 picked by `bay1706/score_keys.py` (read after matching) | ciphertext-only; key rebuilt from sibling R581 |
| harley1582r8500 | key rebuilt from the f. 72r crib (adjacent plaintext) | ciphertext-only; key match against the Harley 1582 sibling R8504 |
| buda1489 | Somogyi's numeric key re-anchored to signs | ciphertext-only; crib from the printed lines 1-2 only |
| rechteren1785 | the "cleartext" pages were the decipherment (existing decipherment) | key from R1038 (Croiset); ciphertext-only |

## Protocol

1. **Blind the route.** Each run starts from a fresh session given only that route's inputs: the transcription, plus
   the crib or sibling key or nothing. It is not given the reading, the key file or the NOTES. Record the inputs
   in the run log.
2. **One route, one log.** `research/routes/<target>/<route>.md`: inputs, tools, every step with its result
   (failures too), the key reached, the text reached, wall time, model.
3. **Score against the reference reading** with the same measure for every route: share of tokens matching the
   reference, `docs/_validate.py` z-scores, and which signs and code groups each route got wrong or left open.
4. **Say what decided it.** For each route, name the single step after which the reading was no longer in doubt
   (the crib position, the annealer restart that locked, the key match score). Compare across routes: what was
   essential, what was incidental.
5. **Record in the profile.** Append each run to `targets/<target>/profile.json` `solution` as `kind: "control"`
   steps, `technique` filled in, and mention the route comparison in `outcome.notes`. Never change `outcome.method`:
   the first route remains how the target was read.
6. **A human check last.** A person compares one passage from each route with the image, without AI
   (`outcome.human_check`).

## Output

`research/routes/RESULTS.md` holds a table of target × route giving success, accuracy, decisive step and cost, and a
paragraph per target on what was essential. The paper table is generated from the profile steps, not copied by hand.

## Open questions

- Whether a route that fails on one target but works on another tells us about the cipher or about the tooling.
- Whether ciphertext-only runs should be capped at the same compute budget across targets (proposed: yes, and
  record the budget).
