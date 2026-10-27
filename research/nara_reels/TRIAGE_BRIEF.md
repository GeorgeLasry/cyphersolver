# NARA bulk-scan triage: shared brief

Read `research/archive_sweep_2026-10/BRIEF.md` first: output format, dedup with `known.py` (run from
`C:\Users\dbour\cypher-sweep`), prior-art checks, incremental writes, no commits, no edits to catalogue.json or docs/.

## What you are given

`research/nara_reels/bulk_scan.py` streamed NARA's open-data catalogue export (AWS) and kept, per record group,
`out/rg_<n>.jsonl` hits:

- `frame`: a digitised frame whose OCR looks like numeric code (`nums` 2-4 digit non-year groups, `run` the longest
  unbroken run, `words` ordinary words; `snippet` = first 400 chars of the OCR);
- `phrase`: a frame whose OCR has "undeciphered", "not deciphered", "in cipher", "key lost" and the like;
- `desc`: a description that names cipher or code.

`out/agg_rg_<n>.tsv` groups frames by item (reel/volume): `flagged`, `solid` (frames with fewer words than numbers:
no clear text or interlinear decipherment), frame numbers. Full OCR of any item: `python research/nara_reels/reels.py
fetch <item naId>` caches it (one request per item, spaced 4 s; never loop faster, never retry on 403/challenge pages,
never send browser-imitating headers). Frame images: the `objectUrl` in the cached record
(`catalog.archives.gov/medialz/...jpg`); view only the few frames you need, at most one image every few seconds.

## What to decide, per correspondence run (not per frame)

1. Is it cipher or code at all? Statistical tables, accounts, ship lists, telegram tariff sheets, page numbers and
   OCR noise are not. Code looks like runs of mixed 1-4 digit groups inside or instead of prose.
2. Was it decoded? Signs that it was: interlinear words over the numbers (OCR mixes words among numbers; view one
   frame to be sure), a "translation"/"decypher"/"decode" copy on the next frames, the passage printed in clear in
   FRUS, ASP, Manning, Moore, the Founders/Jefferson/Madison editions. Coded despatches with a clear copy filed
   beside them are not candidates.
3. Is a key held? The repo has rebuilt State Department codes: `targets/jqa/code_table.tsv` (Madrid/St Petersburg
   1810s-20s; the = 1385, of = 1576, that = 1384, and = 668), `targets/armstrong` (972 code, 1800s Paris),
   `targets/erving1807` (Pinckney code), `targets/jefferson1787/key.tsv` (Code No. 11). Test the groups you can read
   from the OCR against them; a high hit rate makes the entry class A/B and high solvability.

Write one candidate per legation/correspondent and code period, with every flagged frame or volume in
`folio_note`, the item naIds and catalog links (`https://catalog.archives.gov/id/<naId>`) in `links`, and what you
checked in `status` and `prior_art`. Prefer fewer, well-grounded rows over many vague ones, but list every real
undecoded run you find. Put dead ends (tables, decoded runs) in your README with counts so the coverage is recorded.
