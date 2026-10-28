# Library of Congress sweep (27-28 Oct 2026)

Part of the October 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Output: `candidates.json`
(3 rows), `coverage.md` (every query and its hit count), `triage.tsv` (one line per hit), `hits.json` (harvested
records), `context.json` (transcription snippets around each cipher word), `collections_counts.json`,
`coll_hits.json`. Scripts: `locapi.py` (polite cached fetcher), `harvest.py`, `counts.py`, `ctx.py`,
`loc_collections.py`, `coll_hits.py`, `triage.py`; `fa_grep.py`/`fa_ids.py` were for finding-aid PDFs (not reachable,
see below). `raw/` and `img/` are git-ignored caches.

## Method

- loc.gov JSON API, one request per 3.2-6.5 s (two jobs never ran together above 1 per 3 s), User-Agent
  "cyphersolver research (catalogue sweep)". No 429 or 403 from www.loc.gov; several Cloudflare 5xx and truncated
  1 MB responses, retried after 20 s.
- `/manuscripts/?q=<term>` covers every item record of format manuscript/mixed material and the **full text of
  transcriptions** (By the People, Lincoln Studies Center, ADST oral histories). 41 terms probed for counts; 26
  harvested in full (1,948 distinct items). The engine stems and ignores quotes, so "ciphered", "ciphers",
  "in cipher" return the same 1,085 records as "cipher"; generic "code"/"in code" (7,129) and "encoded" (1,438) were
  not harvested.
- Full-text hits were opened (`ctx.py`, 212 items) to read the context. Lincoln telegrams were sampled (40) and then
  dropped as a class; Theodore Roosevelt folder hits were covered through the TR Center subject lists instead.
- 116 relevant digital collections queried one by one (cipher, cypher, decipher); see `coverage.md`.

## Counts and verdicts

| group | hits | verdict |
|---|---|---|
| Madison Papers "partly in cipher" (162 records) | 176 | Printed and decoded in Papers of James Madison / Founders; not rows. Founders "not decoded" cases already in `research/founders_emlo` and `targets/armstrong`, `erving1807`, `graham1806`. |
| Jefferson Papers cipher items (43 records) | 112 | Read in PTJ/Founders, or keys (1784 ciphers, printed numerical cipher, wheel notes, Patterson 1802 solved by Smithline 2009, Lewis 1803 key). |
| Washington Papers (15 records) | 50 | Rochambeau, Morris, Pinckney: "with translation"/"decoded copy"; Church 1775 read; Bezaleel Kerr 1779 invisible-ink letters are developed plaintext. |
| Lincoln Papers | 347 | Received telegrams marked "In Cipher" are deciphered copies; Western Union form text "errors in cipher" causes most hits. Hess 1861 and Slight 1861 are cipher proposals. |
| Theodore Roosevelt Papers | 182 | Mostly telegram-form boilerplate; TR Center lists: one undecoded coded telegram kept (row 2); the rest carry translations or are about codebooks. |
| Bell Family Papers | 53 | Telegram boilerplate, plus one Unicode code telegram (row 3) and an 1875 Bell-Mabel private cipher mentioned but not located. |
| McClellan telegram books 1862 | 2 | Volumes of deciphered telegrams (finding aid); not rows. |
| Andrew Jackson Papers | 7 | Butler → Jackson 1834 cipher paragraph decoded interlinear; Butler 1832 only mentions deciphering. |
| Holt, Goldsborough, Garfield, Dickinson, Douglass, Catt, Terrell, NAWSA, Blackwell | ~260 | Handwriting "decipher", arithmetic "cipher", telegraph tariffs; Garfield 1862 sends Lucretia a cipher key (key lead). |
| Oral histories, motion-picture descriptions, folk music, Whitman, post-1950 | ~550 | Out of scope. |
| World Digital Library, Rosenwald, France in America | 200+ | Printed books; WDL Greenhow letter already `targets/greenhow1861`. |

Kept: 3 rows. Rejected: about 1,945 hits (read, keys, mentions, boilerplate, out of scope).

## Best leads

1. **James Wilkinson ('Agent 13') cipher letters to the Spanish governors**, LoC reproductions of AGI Papeles de
   Cuba leg. 2374 (LoC pp. 1524-3072). Found through Chu, Valenti & Knight 2020, who read 75.1% of word tokens of
   one excerpt with a wordbank and a neural LM; the dictionary was never identified; about 73 pp have no
   decipherment and a second system ("1096") is untouched. Imp 5, solv 4. The decipherments of LoC 1614-1624 and
   1635-1637 (LoC 2975-2989, 3014-3018) are known pairs the project never had.
2. TR → Hay coded telegram, 27 May 1903 (TR Papers): short; decode probably in the Hay papers.
3. Bell → Mabel Bell, 27 Aug 1900, five Unicode code words: trivial with the codebook.

## Key leads (no ciphertext row)

- Isaac Briggs → Wilkinson, 10 Jan 1807 (Jefferson Papers, mtj1.037_0405_0406): image 0405 is the **plaintext**
  ("The President directs me to say to thee ... pilot-boat ... conspirators") and 0406 its cipher with Jefferson's note
  "this cypher is established between Genl Wilkinson and mr Briggs": a plain/cipher pair for the Wilkinson-Briggs
  system, useful for other Burr-period Wilkinson letters.
- Lafayette Papers (LoC, mm96083803): holograph of the secret code used by Lafayette and Washington.
- Lincoln Papers, War Department cipher key, 1 Jan 1863 (mal2088800): US Military Telegraph route-cipher word list.
- Garfield → Lucretia Garfield, Nov 1862 (mss219560007): encloses the key of the cipher he meant to use with her and
  Almeda Booth.
- John Callan O'Laughlin → Roosevelt, 8 Aug 1905 (TR Center o50622): cipher key for Portsmouth peace-talk despatches.
- Adee → Loeb, 16 Dec 1905 (TR Center o52051): modified cipher for Russian-American telegrams.
- Edmund C. Burnett Papers: "translation of a cipher used by the Lee family of Virginia".
- Confederate States of America Records (Pickett Papers): cipher tables for Mason, Slidell, Mann (1922 inventory;
  Gaddy, "Rochford's Cipher", solved).

## Not reached

- **Container lists in finding aids**: findingaids.loc.gov answers 403 to scripted requests (not retried); the
  browser route was refused in this session. Folder-level cipher material in un-transcribed collections (Grant,
  Sherman, Sheridan, Stanton, Pershing, Hamilton, Franklin, Monroe, Polk, Pickett Papers, Rochambeau, William Short,
  Gouverneur Morris, Nicholas Trist, the Foreign Copying reproductions) is therefore **not covered** by this sweep.
- Page images of un-transcribed collections are not searchable at all; zero hits there mean nothing.
- Founders Online (WAF) and the TR Center image server (S3 AccessDenied) refused scripted access; relied on the
  founders_emlo sweep and catalogue text.
- Lincoln telegrams (about 300) were not opened one by one; TR folder hits were not opened.
