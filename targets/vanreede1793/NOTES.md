# Van Reede (Berlin) to the Secret Committee of the States General, 24 March 1793 (DECODE R1893)

Attempted, not solved: closed unread on 21 Sept 2026 (a marked three-digit code with no key and no crib).
Write-up docs/vanreede1793.html.

Status 21 Oct 2026: attempted, partial (a contributed proposal, not "read in part"). PR #66 (WAINUT) rebuilt the code
from 44 cipher/clear pairs of Van Reede's 1792-93 secret despatches in NA 1.01.02 inv. 6695 and applied it to R1893
(section "Contribution by WAINUT" at the end): 601 of 696 groups (0.864) have a value, 459 with support, 142 tentative,
95 unknown. Blind leave-one-letter-out on the 44 training letters gives only 0.599 of groups exactly right (0.701
character similarity), so the R1893 decode is recorded as a proposal with a hedged gist (Polish affairs before the
Grodno Diet, the "Maarschalk Potocki" crib), not as a reading; outcome stays "not solved" until a deciphered copy or
a better-validated code confirms it.

Shelfmark: DECODE files R1893 under NA 1.01.02 inv. 6695 (kept above as the record's metadata), but WAINUT found it is
not among that inventory's online scans (no letter between the P.S. of 16 March and the despatch of 6 May 1793), so
the original is either outside the digitised run or misfiled; where DECODE's photographs were taken is not
established.

Fagel key bundle: of R2842-R2852, only R2846, R2848, R2850 and R2851 were examined against R1893 (21 Sept 2026);
R2842-R2845 and R2847 were seen only as thumbnail montages, R2849 as a thumbnail, and R2852 was never fetched
(`fetch_key_thumbnails.py` loops 2842-2851). The bundle is not fully checked; testing its keys against WAINUT's
rebuilt values (e.g. 444B van, 973B en) is the obvious next step.

Split on 14 Oct 2026 from `vanreede1787` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old
entry (catalogue 231) joined Arend Willem van Reede's despatches of 1787–88, which are in William V's 1782 Grand
Chiffre (DECODE key R1024), with this despatch of 1793, which is not. The Grand Chiffre letters are a different cipher,
with their own page ([`targets/vanreede1787/`](../vanreede1787/), docs/vanreede1787.html). Catalogue entry 231 was
restored on 14 Oct 2026, narrowed to R1893, as "attempted, open". The DECODE downloads (`decode/`, git-ignored, main
checkout `targets/vanreede1787/decode/`) and `fetch_decode.py` stay in `../vanreede1787/`; the scripts here read
the scans from there.

## The document

DECODE R1893 = Nationaal Archief, Staten-Generaal 1.01.02, inv. 6695: van Reede to the Secret Committee, Berlin,
24 March 1793, in Dutch (DECODE tags the language as HU, wrongly). Four pages; DECODE transcription D3608
(`ciphertext_R1893.txt`).

## The code

Three-digit groups with per-digit overmarks (~ v = ¨ +): 696 tokens, 513 distinct marked forms (`analyze_1893.py`),
so several thousand possible values. The marks are absent from the 1787–88 despatches, which is why the system was
separated from the Grand Chiffre on the first day.

## What was tried

- Keys: the 1793 Fagel key bundle on DECODE (R2842–R2852; thumbnails `fetch_key_thumbnails.py`,
  `make_thumb_montages.py`; selected pages `fetch_selected_key_pages.py`); R2846, R2848, R2850 and R2851 examined
  (numeric cells indexed with `index_key_digits.py`, `index_key_digits_generic.py`, `index_r2851_digits.py`,
  `crop_key_matches.py`, `crop_index_matches.py`; the R2851 cells addressed by R1893's groups extracted with
  `extract_r2851_cells.py`), and the interlinearly decrypted control R2243. None reads R1893.
- Ciphertext-only: with 513 distinct forms in 696 tokens, most forms occur once or twice; a code of this size cannot
  be rebuilt from this much text without a crib.

Closed until a key or a deciphered copy turns up (Staten-Generaal secret files, NA 1.01.02).

## Log

- 2026-09-20: records and transcription fetched; R1893 separated as a different system (per-digit marks).
- 2026-09-21: the Fagel key bundle and R2243 tried; ciphertext-only attack judged not feasible; closed unread.
- 2026-10-14: split from `vanreede1787`; the R1893 files moved here.
- 2026-10-21: PR #66 (WAINUT) merged: code rebuilt from 44 pairs in inv. 6695, R1893 decoded in part (proposal);
  reviewed, status lines, shelfmark and Fagel-bundle coverage reconciled above.

## Remaining gaps

- R1893 (24 Mar 1793, 696 tokens) - blocker: no-key-material; different three-digit overmarked code, 513 distinct forms; keys R2846, R2848, R2850, R2851, R2243 tried; WAINUT's code rebuilt from inv. 6695 (PR #66) gives a partial proposal (0.599 leave-one-out exact), not a reading; R2842-R2845, R2847, R2849, R2852 not examined in detail

## Escalation

- [x] siblings: van Reede's other DECODE records (R1026-R1029, R1057) are Grand Chiffre; the 1793 Fagel key bundle R2842-R2852 opened
- [n/a] clear-pages: no clear copy or gloss on the R1893 images in DECODE's transcription; not re-checked against the images after the split
- [x] known-keys: R1024 (Grand Chiffre), R2846, R2848, R2850, R2851, R2243 tried; no fit
- [n/a] print: no printed edition of the Secret Committee's 1793 despatches was searched; recorded as not done in the old notes
- [n/a] key-rebuild: 513 distinct forms in 696 tokens leave nothing to rebuild from without a crib
- [n/a] retry: nothing reads, so there is no extended key to retry with

## Contribution by WAINUT (21 Oct 2026)

WAINUT (a Dutch AI company, https://github.com/WAINUTAI) followed the pointer above to NA 1.01.02 and rebuilt Van
Reede's code from the secret despatches that survive there with their clear copies, then applied it to R1893. Nothing
above has been changed, and `ciphertext_R1893.txt` is used as it is. Number groups and clear copies were transcribed
with Google Gemini (two independent passes for the cipher pages); the alignment, code rebuild, controls and analysis
were done with AI language-model agents; samples of the training transcription and of R1893 were checked by eye on
the scans (below). Files are in `wainut/`; `python3 targets/vanreede1793/wainut/check.py` reproduces every number in
this section (standard library and numpy, paths relative to the folder, about one minute).

**1. Training pairs.** NA 1.01.02 inv. 6695 ("Ingekomen secrete brieven ... Brandenburg en Pruisen", 1792-1793,
http://hdl.handle.net/10648/9195a4cc-61aa-4ff2-87fb-a35992926dde) files each of Van Reede's secret despatches as the
cipher original next to the clerks' registered clear copy ("Ontcijferd Post Scriptum ...", marked "Registr.").
`wainut/letters.json` lists 44 such letters (17 Jan 1792 to 24 Dec 1793) with the scan and half-page of each
cipher original and each copy; two of them (Sept 1793) were written by the legation secretary Bourdeaux in the same
code. The volume runs backwards in time (Dec 1793 near scan 6, Jan 1792 near scan 384). The clear words that Van
Reede left uncoded anchor each cipher run to its copy: 116 runs, 10,250 groups, 8,286 words (`wainut/runs.json`).

**2. The code.** A homophonic nomenclator of three-digit groups with marks over the digits (DECODE's ~ v ¨ = +). Each
group stands for a word, a syllable, a few letters or a phrase, and common words have several homophones. The mark is
part of the value: 773m, 319v, 442B and 751B are different groups from 773, 319, 442 and 751. `wainut/em.py`
segments each copy span into as many pieces as its run has groups (hard EM, each run re-segmented with the counts of
all the others) and counts piece per group. `wainut/code_marks.json` holds the result: 2,385 group forms, 1,416 seen
at least twice (for example 444B van, 973B en, 742B het, 958d Poolen, 848d den Koning).

**3. Blind validation (leave one letter out).** For each of the 44 letters the code was rebuilt without it, its
groups decoded with the majority piece of each group, and the decode scored against its own contemporary copy
(`wainut/loo_marks.tsv`; `check.py --loo` re-runs it in about 12 minutes).

| | groups | coverage | groups exactly right | character similarity to the copy |
|---|---|---|---|---|
| rebuilt code (letter held out) | 10,250 | 0.897 | 0.599 | 0.701 |
| shuffled code | | | 0.003 | 0.203 |
| rotated code (entry of the next number, same mark) | | | 0.013 | 0.210 |

All 44 letters beat both controls. The weakest is 1793-06-13 (0.210), whose copy spans two pages that the alignment
pairs badly. "Exactly right" is scored against a segmentation of the copy; character similarity does not depend on
it. The 44 letters have contemporary decipherments in the volume, so they are validation material, not new readings.
Transcription checks by eye: scan 116R lines 1-3 (30 groups, the start of the held-out PS of 29 Jan 1793) and the
first 40 groups of scan 13R (PS of 7 Dec 1793) agree with the transcription in digits and mark type, with one
doubtful digit on 116R (237 or 287).

**4. R1893.** DECODE's marks map onto the training marks one to one (~ m, v v, ¨ d, = B, + p). With the code from all
44 letters, 601 of R1893's 696 groups (0.864) are in the code: 459 read with support of 2 or more and a majority of
at least 50%, 142 tentative, 95 unknown (`wainut/r1893_reading.tsv`). A character 5-gram model trained on the clear
copies (R1893 is not in its training data) scores the decode:

- *Order permutation* (same code, R1893's groups permuted, 200 times): true order -2.161 per character, permuted
  mean -2.385 (sd 0.022), best -2.319, z 10.0, rank 0/200. Three held-out training letters, with code and model built
  without them, give z 11.6 (1793-03-12 PS), 9.0 (1792-01-21 PS) and 7.8 (1793-06-29). On this test R1893 sits in
  the range of the held-out letters.
- *Shuffled codes* (200): mean -2.305, best -2.154, z 2.7, rank 1/200. This control is weaker, because shuffling
  also breaks the match between frequent groups and frequent words.

**Crib.** R1893 groups 356-359 are `77~3 319v 44=2 75=1` (773m 319v 442B 751B). The same four groups spell
"Maarschalk Potocki" in Van Reede's PS of 16 June 1792 (scan 215R; copy 216R-217L): "de Maarschalk Potocki is
onverrigter zaake na huis gekeerd". That fits Ignacy Potocki's Berlin mission of 1792. Which Potocki is meant in
March 1793 is open; the decode does not support a Targowica (Szczęsny Potocki) identification.

**Gist (hedged).** The letter deals with Polish affairs around a Diet (*landdag*) to be held, which fits the run-up
to the Grodno Diet of 1793: a deputation and foreign affairs, the expedition and money, a proposal of the King to be
laid before the Diet, difficulties and prejudices, the Russian party, the party of the marshal Potocki, the
(Prussian) headquarters, advantages to be proposed there, a cession (*afstand*) to be deliberated and guaranteed,
Danzig, the minister of Austria. The partial edition, with tentative pieces marked, is in `wainut/r1893_edition.md`.
About a third of the groups are tentative or unknown, so no continuous translation is offered.

**5. DECODE's transcription against the image.** `docs/vanreede1793_r1893.jpg` (head of page 1, six rows) was
checked by eye against `ciphertext_R1893.txt`, about 88 groups. Rows 1-4 agree in numbers and mark types, except that
the transcription splits `960` into `9 60`. Row 5 on the image has `19" 69¨` after `112v`, which the transcription
omits; row 6 has `713= 896=` after `901~`, also omitted. So about 5 of 88 groups are dropped or split. The per-group
decode survives this, but some `[?]` in the edition may be transcription errors, and a fresh transcription of the
four DECODE images would probably raise the coverage. These corrections are not applied to `ciphertext_R1893.txt`
or to the numbers above.

**6. Prior decipherment.** None located. R1893 is not among the online scans of inv. 6695: between the P.S. of
16 March 1793 (scans 110-113) and the despatch of 6 May 1793 (scans 96-105) the volume holds no other letter, and a
3-gram search of R1893 against the transcribed pages found nothing beyond the Potocki groups and a few short
formulaic sequences. A quick web search found no edition of the letter. **Not searched:** the Fagel archive (NA
1.10.29, source of the 1793 key bundle R2842-R2852), which may hold a deciphered copy, and Colenbrander's
*Gedenkstukken*. "New" here means: not read in this repository, and no decipherment in the digitised inv. 6695.

Files: `wainut/check.py`, `em.py`, `letters.json` (pair list with scans), `runs.json` (aligned runs; the clear text
is model transcription, not checked word by word), `code_marks.json`, `loo_marks.tsv`, `r1893_reading.tsv`,
`r1893_edition.md`.

## Brice Dudout's report (email of 27 Oct 2026)

- The letter is not among the public scans of NA 1.01.02 inv. 6695.
- The Fagel key books (NA 1.10.29 inv. 1257-1267) are online. None is Van Reede's, but **1261, 1263 and 1265 are of the
  same family**: they describe null groups and "Begin des Briefs" / "Einde des Briefs" markers. That may explain some
  unknown groups at the start and end of R1893. Next: check the opening and closing groups of R1893 (and of WAINUT's
  decode) against the marker groups in those three books.
