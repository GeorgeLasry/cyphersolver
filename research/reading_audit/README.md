# Reading audit, 22 October 2026

## Why

George Lasry, 22 Oct 2026, on [matignon1586](https://dbourdeau.github.io/cyphersolver/matignon1586.html):

> The decryptions are not useful. They seem to have many errors, making it impossible to assemble coherent French
> sentences. This is likely due to transcription errors. The requirement should be that the LLM can build coherent
> sentences - that can later be translated to English, and iteratively improve the transcription and the key until
> this is the case. Before you accept a PR with readings, the acceptance process should validate that the submission
> includes not only a mechanical decryption but also readable coherent text + translations. … It is OK to have a few
> holes, but not holes in almost every sentence.

He was right about that page: its 63.7% "tokens in runs of French" counted runs of short corpus words ("la que le
estoit"), and the leaves without a clear copy had holes in nearly every sentence. This audit asks his question of
every published reading, in any language.

## What was done

1. **Automatic triage** (`docs/_check_reading.py --audit` → `auto_scores.csv`). Each decryption file is cut into
   sentences; a sentence is clean with at most one hole in ten words (explicit gaps, or words the period word list of
   its language does not know; word lists built from `lang/` corpora, committed in `lang/lexicons/`).
2. **A reader for every target** (327, in twelve batches; rubric `llm/RUBRIC.md`; results `llm/out_*.jsonl`): open the
   decryptions, try to build them into sentences, translate one or two, grade A–D or N.
3. **Join** (`aggregate.py` → `audit.csv`): grade, automatic score, the profile's claim, mismatch flag, action.
4. **Relabel** the C and D targets (`RELABEL_BRIEF.md`, four batches): each document checked again; those that do not
   read marked `state: "decoded, not read"` in `profile.json`, the claim and figure cut back, NOTES and page corrected,
   README rows moved (`readme_rows.py`).

## Results

| grade | meaning | targets |
|---|---|---|
| A | coherent sentences, scattered holes | 171 |
| B | coherent but published raw (unspaced, capitals, decoder lines) | 56 |
| C | mixed: some documents read, others do not | 53 |
| D | holes in most sentences (the matignon case) | 29 |
| N | not prose (key sheets, code lists, single words) or only an excerpt | 18 |

* 36 targets claimed `read` or ≥ 90% while graded C or D.
* On the closer per-document reading of the relabel step, about one C/D grade in five was overturned or refined
  (mostly B: coherent but raw); 27 targets are no longer readings at all, 54 keep a reading for some documents only.
  After the relabel the profiles hold 680 documents marked read and 300 decoded, not read.
* Only 27 of 327 targets had any English translation.
* 46 targets publish only an excerpt (usually from Lasry's own report) rather than the full decryption.

### The automatic score is a pointer, not a verdict

| automatic clean share | A | B | C | D | N |
|---|---|---|---|---|---|
| < 0.45 | 37 | 31 | 20 | 13 | 10 |
| 0.45–0.70 | 82 | 13 | 21 | 11 | 6 |
| ≥ 0.70 | 52 | 12 | 12 | 5 | 2 |

The D grades fall in every band: mixed files (headers, tables, clear text and cipher interleaved), period spellings
the word lists lack, and decodes made of short real words all defeat it. So the gate (`docs/_texts.py
reading_problems`) requires a **recorded reader's review** on every document counted as read (`reading_review`
{grade A|B, by, date, note}), and an English translation; the score is printed to point the reviewer at weak
sentences. `reviews.json` (`seed_reviews.py`) carries this audit's grades, which stand in for documents with no
review of their own.

## What is left

* **Translations**: 731 documents across the targets still marked read have no English translation; the gate
  refuses each target when it is next written up. `_check_writeup.py --audit` section J counts them.
* **Re-reading** the decoded-not-read documents (George's iterative method: build sentences, check each break on the
  image, correct transcription and key). Done on 22 Oct 2026 for matignon1586 ff. 173 and 196/201 (14% → 79% clean
  sentences on 196/201, 16% → 71% on 173); f. 110 needs a full re-transcription (labels of that hand inconsistent).
  The rest are listed as `not-attempted` gaps in each target's NOTES.
* **Full texts** for the 46 excerpt-only targets.
