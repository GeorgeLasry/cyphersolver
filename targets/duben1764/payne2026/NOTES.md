# Catalogue 450: additional research, 28 October 2026

Status: in progress

Contribution by Bryan Payne (@bdpayne), using OpenAI Codex. **The May 1764 cipher remains unread.** A separate printed 1771 passage positively matches key 219; it is a fragment decode, not a whole-letter reading. No newly recovered May key or invented plaintext is submitted.

This folder preserves research performed before reading the latest upstream target notes. Upstream already independently identified the interlinear 1765 material and multiple cipher families. Those findings are not claimed here as first discoveries. The existing parent notes, transcriptions and experiments are retained unchanged apart from an addendum and profile integration. Our provisional 126 alignment is separate from upstream's fuller positioned-gloss transcription; its failures do not overturn that work.

## Main results

1. The apparent 15 May 1764 letter begins on image 105 right, continues on 106 left and 107 right, and ends on 108 left. Its identified numeric portions total **870 groups, 33 uncertain occurrences**. The complete clear portions and physical sequence need checking. The viewer date and upstream's 15/4 May notation should be reconciled rather than silently normalized. Image 107 alone is a continuation, not a whole letter.
2. The key inventory extends beyond sheets 218–220: images **162–168** contain a substantial French vocabulary key, following cover 161, with labels extending to about 2950. The cover names C.W. von Düben and A.H. v. Borcke; exact identity/date remain unestablished. It has only sample transcription here.
3. Complete-table transcription attempts cover **218: 353 rows / 352 labels; 219: 504 rows; 220: 459 rows**. All are preliminary. Key 218 preserves duplicate 951 rather than silently selecting a value. Key 219 retains 22 explicit doubt marks after corrections. These are archival tables, not recovered keys for the May letter.
4. The handwritten reference on key 219 resolves to Henrik Schück's edition, part I, p. 259, letter 143, in the later-series SAH volume 29 appendix (1917 volume, published 1918; separate edition 1919). The editor dates the undated letter to mid-February 1771 and leaves two numeric runs unresolved. Key 219 matches editor-known **626 Fersen / 665 Breteuil**, and the longer run begins **“bonne intelligence entre la…”** after doubled-consonant normalization. Final court abbreviations and the proposed “créé[?]” remain uncertain. All 19 printed groups, literal mappings, cautious French/English and sources are in [KEY219_PROVENANCE.md](KEY219_PROVENANCE.md). This is application of an existing key, with no claim that later prior art is exhausted.
5. The entire **38-page Uppsala F474 portfolio** is publicly available through Alvin 164482. All pages were surveyed and principal tables enlarged; 27 sampled entries from four families are recorded. No May-letter match was accepted. [KEY_SEARCH.md](KEY_SEARCH.md) supplies a page map and public PDF link, plus contemporary archive leads: Chifferklaver 202/8–10, Düben's Diplomatica Muscovitica 71 (1763–66), and Gyldenstolpe's Sjöholm collection. Their metadata does not identify a private-channel key; no scan links were found for those holdings.
6. Related Alvin 490037 / F414 is a six-page clear French draft dated 15 November 1768, marked Chiffrée, with no numeric counterpart in the scan. The parent record's 1758 date conflicts with the detailed record/manuscript. It is a lead, not a key match.

## Sources and manuscript observations

Task: [catalogue 450](https://dbourdeau.github.io/cyphersolver/solve/450.html). Archive: Riksarkivet, SE/RA/710003/02/008/b/K 259. [IIIF manifest](https://lbiiif.riksarkivet.se/arkis!A0073297/manifest), 223 canvases. Image numbers throughout are scan numbers, not folios. Use the [viewer](https://sok.riksarkivet.se/bildvisning/A0073297_00107), replacing the five-digit image suffix as needed. Full image template: `https://lbiiif.riksarkivet.se/v2/arkis!A0073297_NNNNN/full/max/0/default.jpg`.

All 223 thumbnails were visually surveyed; `inventory.csv` is a screening inventory, not a full-resolution audit. Selected cipher pages, all four K259 key families, and later adjacent pages were enlarged. The initial thumbnail pass missed interlinear French on 125–126; this was corrected on reinspection. `image126_french.md` transcribes and translates the visible French on 126; it is manuscript clear text, not a new decryption. `image126_audit.md` records disputed numeric glyphs. Do not treat `image126_pair.json` as a validated token alignment.

Image 97 right explicitly refers to the opening `15.73.100.347.503.401.107.536` on 96. This identifies related material without proving duplication rather than continuation. Images 85–86 have Swedish “Nyheter från Finland”; linkage to 87–93 is unproved here. Image 118 begins the 5 October 1764 “Chiffre no 2” material; clear draft 120 is a candidate, not an assumed exact plaintext. The letter beginning on 124 right is dated 15 November 1765.

Sheet 217 is the “Chiffernycklar” folder title; 221 is unrelated German material. Key 218's added 952 reads “Felt Mar: Fersen.” [SBL](https://sok.riksarkivet.se/Sbl/Mobil/Artikel/15288) dates Fredrik Axel von Fersen's field-marshal appointment to 12 January 1770. **If** that is the person meant, this annotated table is later than May 1764; identity and an older base key remain possible. Key 220's seven meaningless initial “chiffres” may mean individual digits: `66.74.100` and `15.73.100` each contain seven. This framing clue does not establish a key match and must not be reapplied on every continuation page.

## Experiments and limits

| Experiment / files | Observation | What it establishes |
|---|---|---|
| `analyze.py`, `statistics.json`, `key_diagnostics.md` | Image 107: 311 groups, 14 uncertain, 175 distinct certain labels; sample substitutions | Lookup mechanics only; diagnostic strings are not decipherments |
| `compare_tables.py`, `table_comparison.json` | Literal and zero-stripped, three-phase substitutions of 105–108 against 218–220; no accepted French | 48 bounded diagnostics, not exclusion of changed/transformed keys |
| `test_regroup.py`, `test_arithmetic.py` and JSON | Six regroupings; invertible affine maps mod 1000; best 218 coverage 187/297 certain 107 groups | Coverage is not language evidence |
| `digit_permutation.cpp`, `permutation*`; `screen_radix.py`, `screen_resegmented.py` | Digit permutations / position orders for 220; base-9 and affine membership screens; no accepted text | Coverage screens only; not a general cryptanalytic rejection |
| `digit_control.py`, `digit_control_results.json` | Exhaustive fixed 1/2-digit letter-code model recovers matched synthetic control; no exact real-126 match, zeros kept/deleted, end padding ≤12 digits | Only this exact model on provisional text/glyph readings |
| `align_candidate.py`, `align_interlinear.py` | Z3 word-equation hypotheses timed out | Unknown, not UNSAT or a recovered key |
| `beam_align.py`, `beam_control.py`, `em_alignment.py` | Beam and EM failed matched synthetic controls | Historical outputs have no evidential weight |
| `cp_align.py`, `alignment_experiments.py`, `cp_experiments.json` | Unrestricted control 42.96% token-value accuracy; lexical control 80%; unrestricted real formal fit; seed-450 shuffled order INFEASIBLE; eight restricted lexical framing cases INFEASIBLE | Neither control reaches 95%; formal fits are not historical keys; exact-spelling restrictions cannot reject other conventions |
| `read_schuck1771.py`, `schuck1771_reading.tsv` | All 19 literal mappings; two editor-known names match; connected French opening | Positive key-219 / 1771 passage connection, with uncertain expansions retained |
| `screen_f474_samples.py`, `f474_fingerprints.json` | 27 samples from four families | No accepted match, not exhaustive rejection |

No general French-language solver was run in this contribution. Upstream has separate annealing/EM experiments, preserved in the parent folder. Frozen synthetic inputs are included; guesses in experimental JSON are **not accepted historical key values**. Solver-dependent outputs can vary with versions/time limits.

## File guide and reproduction

- `image105_cipher.txt` through `image108_cipher.txt`, combined in `may1764_cipher.txt`: preliminary numeric transcription only, line labels followed by groups; `?` marks doubt. No clear portions supplied as ciphertext.
- `image096_cipher.txt`: eight opening lines, not the whole letter.
- `key218.txt`, `key219.txt`, `key220.txt`: preliminary manuscript tables; `key_samples.tsv` includes the larger 162–168 key samples. H = primary-source reading, M = doubtful reading. `transcribe219.py` regenerates 219 and corrected sample values.
- `KEY219_PROVENANCE.md` and `KEY_SEARCH.md`: detailed citations and limits. `key_search_archive_metadata.json`: five public archival metadata graphs.
- `WORKLOG.md`: chronological record, including superseded early assumptions. `letter_statistics.json`: extended transcription counts. `REPORT.md`: concise PR summary.
- Large scans, thumbnails, redundant manifest download and caches are omitted. Fetch from source URLs; do not mistake missing binary images for missing transcriptions.

From the repository root:

```sh
python3 targets/duben1764/payne2026/analyze.py
python3 targets/duben1764/payne2026/compare_tables.py
python3 targets/duben1764/payne2026/read_schuck1771.py
python3 targets/duben1764/payne2026/screen_f474_samples.py
python3 docs/_check_profile.py --measure targets/duben1764/payne2026/may1764_cipher.txt --drop-first
python3 docs/_check_profile.py --measure targets/duben1764/payne2026/schuck1771_cipher.txt --drop-first
python3 docs/_check_profile.py duben1764
python3 docs/_check_reading.py duben1764
```

The profile checker measures 870 tokens / 327 distinct literal spellings including uncertainty marks; 296 is the distinct count of **certain-only** labels, not a conflicting measurement. Printed fragment: 19 tokens / 18 distinct groups. Dependency-free reproduction covers the principal transcriptions/lookups; exploratory scripts additionally use NumPy, Z3 or OR-Tools (9.15.6755 for the recorded CP run). C++ permutation search is optional and expensive. No network access is needed for the saved-input checks.

## Prior art and credit

Exact-target searches did not locate a May decipherment; that is not proof of novelty. Schück's edition was inspected directly via public KB scans 594–596. Later 1771 scholarship remains unchecked. SBL bibliographies identify Jägerskiöld (1938, 1943, 1945) and Metcalf (1977); those books have not been searched page by page. Behre's *Postspionaget under 1700-talet*, Scandia 29:2 (1963; online 2008), supplied context only, with no target-specific hit. Its examples of French clear / Swedish cipher correspondence do not prove the language of this cipher. No logged-in DECODE inspection took place. The publicly available F474 PDF supersedes the earlier access obstacle for that portfolio.

Bryan Payne supplied the task URL, directed continuation and requested submission. OpenAI Codex performed source search, visual transcription, scripts and write-up; exact model variant was not recorded. Tools: web search, curl, git, Python, Pillow, PDF text/render tools, Z3, OR-Tools, C++; OCR attempts with Tesseract/macOS Vision were unusable. No subagents. No independent human reading review is claimed. The archival key's contemporary author is unidentified; Schück's edition supplies the printed passage and earlier name readings. Existing upstream work and Brice Dudout's pointer remain separately credited in the parent profile.

## Remaining gaps

The May letter has no validated key or coherent cipher reading. Independently audit all 33 uncertain tokens and the leaf sequence/date; transcribe the clear portions. Validate 126's numeric/clear alignment against the fuller upstream gloss, spelling conventions and an independent passage before accepting any key values. Independently check all three table transcriptions and complete 162–168 where warranted. Resolve the final 1771 expansions and later prior art; the whole 1771 letter is not supplied or claimed read.

## Escalation

Adjacent pages, four K259 key families, printed provenance and public F474 material were investigated. The next archival priorities are detailed inventories/images of Chifferklaver 202/8–10, Düben's contemporary file 71, and recipient/KB royal papers. These are leads requiring access or further catalogue work, not proven absent keys. Preserve upstream's multiple-system distinction. Any new solver needs a recovered matched positive control before a historical failure carries weight. No archive inquiry or email was sent.
