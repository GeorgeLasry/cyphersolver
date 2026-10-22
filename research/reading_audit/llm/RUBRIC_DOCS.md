# Per-document reading review (second wave, 22 Oct 2026)

Same question as `RUBRIC.md` (George Lasry: can a reader build coherent sentences from what we publish and translate
them?), but now **for every document**, not a sample per target. Grades as in `RUBRIC.md`: A, B, C (part of the
document reads), D (holes in most sentences), N (not prose, or no text in the repository).

Work in `C:\Users\dbour\cypher\.worktrees\reading-gate`, read only except your output file.

## Your list

Each line of your batch file is a target folder. For each, open `targets/<folder>/profile.json` and take every
`outcome.texts` entry whose `state` is `read` (or absent) and that has no `reading_review` of its own. For each such
entry, open its `reading` file if listed, else its `decryption` file(s), and read the whole document (if it is very
long, read at least the first, a middle and the last 40 lines).

**Texts that are not local files.** If the decryption is a URL, fetch it (WebFetch). If it is a PDF in the folder,
read it (the Read tool takes PDFs, `pages` for long ones). If the file is missing, say so and grade N with
`"missing": true`. If the reading exists only in print and only an excerpt is in the repository, grade what is there and
set `"excerpt": true`.

## Output

Append one JSON line per **entry** to `research/reading_audit/llm/docs_<batch>.jsonl`, as soon as it is done:

```json
{"folder": "...", "doc": "<the entry's doc value, as in the profile>", "label": "<entry label or ''>",
 "file": "<what you read>", "grade": "A|B|C|D|N", "language": "fr", "excerpt": false, "missing": false,
 "sample_original": "...", "sample_en": "...", "why": "one or two concrete sentences"}
```

Helper scripts, if any, end in `_<batch>` and stay in `research/reading_audit/llm/`. Do not edit anything else.
End with a count per grade and the list of entries graded C, D or N, each with its reason.
