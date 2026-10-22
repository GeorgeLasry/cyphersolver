# Reading audit rubric (22 Oct 2026)

George Lasry, on matignon1586: *"The decryptions are not useful. They seem to have many errors, making it impossible to
assemble coherent … sentences. … The requirement should be that the LLM can build coherent sentences - that can later
be translated to English … It is OK to have a few holes, but not holes in almost every sentence."*

This audit asks, for every target that publishes a reading: **can a reader build coherent sentences from what we
publish, and translate them into English?** It is language-neutral: the text may be French, Italian, Spanish, Latin,
German, Dutch, Hungarian, English, Catalan, Portuguese, Polish, Swedish, Chinese, Japanese ...

## For each folder in your batch

Work in `C:\Users\dbour\cypher\.worktrees\reading-gate` (read only, except your output file).

1. Read `targets/<folder>/profile.json`: `outcome.method`, `outcome.class`, `outcome.fraction_read`, `outcome.texts`.
2. Open the `decryption` file(s) of `outcome.texts` (paths relative to the target folder). For a target with many
   documents, look at up to three: the first, a middle one and the one that looks weakest. Read about 40 lines of each;
   skip header comments and lines of cipher figures. If a `translation` file is listed, glance at it. If the listed
   decryption is a raw machine decode but the folder holds a prose reading (`READING.md`, `reading*.md`,
   `*_reading.md`, `read/`, `NOTES.md` sections quoting the text), look at that too and say so in `reading_file`.
3. Try to make sense of it as continuous text in its language. Then grade:

| grade | meaning |
|---|---|
| **A** | coherent sentences; holes are scattered (a few codes or words per page). Translatable as it stands. |
| **B** | the content is coherent, but the published form is raw: unspaced, all capitals, no punctuation, per-line decoder output, nomenclator tags. A reader can still build the sentences; it needs normalising and a translation, not more cryptanalysis. |
| **C** | mixed: some documents or long stretches read as sentences, others have holes in most sentences. |
| **D** | holes or nonsense in most sentences; a reader cannot build coherent sentences. **This is the matignon1586 case.** |
| **N** | not prose by nature: a key table, a code list, a worksheet, numbers, single words or names; or the file is missing/empty. Say which. |

4. Translate one or two of the best sentences into English (`sample_en`) — this is the test that it can be translated.
   For D, give the sentence you tried and why it fails.
5. Note mismatches: the profile says `read` / complete (or `fraction_read` ≥ 0.9) but you grade C or D.

## Output

Append **one JSON object per line** to `research/reading_audit/llm/out_<batch>.jsonl` **as soon as each folder is
done** (do not hold results to the end):

```json
{"folder": "...", "grade": "A|B|C|D|N", "language": "fr", "docs_checked": ["..."], "reading_file": "path or null",
 "translation_exists": true, "claimed": "<method> / <class> / <fraction_read>", "mismatch": false,
 "sample_original": "...", "sample_en": "...", "why": "one or two sentences: what makes it this grade",
 "fix": "none | normalise + translate | re-read (transcription/key) | relabel as decoded-not-read | check file list"}
```

Keep `why` concrete ("holes in 9 of 12 sentences on R805; R741 reads cleanly"). Do not edit any other file.
At the end, reply with a count per grade and the folders graded C or D.
