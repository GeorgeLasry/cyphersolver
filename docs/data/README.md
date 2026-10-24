# cyphersolver profiles dataset

430 historical cipher targets, 957 documents. Exported 2026-10-23 by
`docs/_export_dataset.py` from `targets/<folder>/profile.json` (schema: `profile.schema.json`).

- `profiles.jsonl`: one profile per line, as recorded: the cipher system, the documents, what the model was given,
  every solution step (failed ones included), and the outcome with George Lasry's method categories.
- `targets.csv`: the same flattened to one row per document; `codebook.md` explains every column.

Only targets with a published write-up are included, and none whose texts are withheld. `"unknown"` means the field
could not be established; it is never a guess. `outcome.provenance` says whether the result is the project's own or
was contributed. `conditions.prior_solution` records whether a reading existed before the attempt. Readings are
claims to check against the images linked from each page, not settled facts.

Patterns mined from these profiles: `research/patterns/REPORT.md` in the repository.
