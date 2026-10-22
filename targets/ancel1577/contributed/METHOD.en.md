# Method, numbers, AI use and limits

Japanese: METHOD.md

## Material
- BnF, Cinq Cents de Colbert 398 (Gallica ark:/12148/btv1b525218133): original letters to Charles IX, Henry III and Catherine de Médicis on the affairs of Germany, including dispatches of Jean de Vulcob (1575–76) and Guillaume Ancel (1576–78, 1584), French residents at the Imperial court. Page numbers are the manuscript pagination; "f" numbers are Gallica views (page→view table in SOURCES.md).
- Key: S. Tomokiyo's reconstruction "Vulcob and Ancel's Cipher (1575–1584)" (Cryptiana, `code/frencheastern.htm`, image `easternVulcob.png`; page Last-Modified 15 Mar 2026). Tomokiyo lists the letters and writes that the key "will allow reading undeciphered letters"; he publishes no readings of them.
- Images: BnF IIIF Image API, 2400 px wide. No image is included here.

## Which passages were undeciphered
All cipher pages listed by Tomokiyo were viewed. Most carry a contemporary decipherment in the left margin. The cipher on p.525–526, p.539, p.561–563 and p.565 has none (the single line on p.570, at first counted with them, has a contemporary decipherment in the last margin line of p.569); these are the undeciphered passages (124 cipher lines, 4,383 symbols in the final transcription, plus a short cipher fragment at the end of p.524); the reading is given for p.525–565 (123 lines, 4,357 symbols).

## Steps
1. **Key table** (`data/key.tsv`, `src/vk.py` `TOKENS`): Tomokiyo's symbols with names; additions are marked in `TOKENS` (source `C`), the rest is his table (`T`). Symbols not in his table: OPEN.en.md section 1.
2. **First transcription** (`data/transcription/<page>_first.txt`): p.33 and p.539 by Claude Opus 5.5, the other pages by Claude Sonnet 5.5, from enlarged tiles, in symbol names, one row per manuscript line.
3. **Cross-check transcription** (`second/<page>_pass1.txt`): OpenAI Codex CLI (codex-cli 0.163.0-alpha.10.2, default model; the run log does not name the model), one run per page, `codex exec --ephemeral -s read-only` from an empty folder, given only the line images (cut by `src/lines.py`, one `-i` per image) and `second/PROMPT.md` (symbol names and shape descriptions; no values, no key, no first reading). The prompt was sent on standard input. The run logs contain one reply and no command execution. (`second/p525_pass1_misaligned.txt` is a first run of p.525 whose line images were shifted by two lines; it was rerun and is kept only for the record.)
4. **Image adjudication, first round** (`xcheck/adjudication_img_<page>.tsv`, prompt `xcheck/ADJUDICATE_PROMPT.md`): Claude Sonnet 5.5 looked at each disagreement between 2 and 3 in enlarged crops and changed the first reading only when the image clearly showed the other; otherwise it kept the first reading and marked it "?". Result: `data/transcription/intermediate/<page>.txt`.
   - In three places an image-based change made non-words in a systematic way (p→φ "mait, maire"; 3→ʒ "serblable, directerent"; qa→al "auon"). Claude Opus 5.5 put the first reading back and marked it "?" (p.525: 11 symbols; p.526: 3; p.561: 1). These 15 are decided by context, not by the image, and are counted as undecided.
   - Rows in the tables (a row may span several symbols; kept first / took second / undecided): p.33 38 (18/2/18); p.525 115 (46/59, of which 11 reverted by context/10); p.526 89, 9 formatting only (25/16, +5 mixed/34); p.539 36, 5 formatting only (12/1, +2 mixed/16); p.561 96 (54/16/26); p.562 43 (35/5/3); p.563 93 (49/5/39); p.565 103 (63/12/28); p.570 5 (1/0/4).
5. **Further Codex readings and second image adjudication**: Codex read the same line images again, without seeing our transcription — once with `second/PROMPT.md` (pass 2) and three times with `second/PROMPT2.md` (pass 3a–c), which describes more precisely the look-alike shapes (9/q, ∂/δ, the cross signs, the large-arc S, qa/al, L/g). Claude Sonnet 5.5 then adjudicated by image the disagreements between the intermediate transcription and the value-level majority of pass 3a–c (`src/vote.py`; `xcheck/adjudication2_img_<page>.tsv`, prompt `xcheck/ADJUDICATE_PROMPT2.md`). Changes taken: p.33 2, p.525 6, p.526 7, p.539 3, p.561 5, p.562 1, p.563 10, p.565 6, p.570 1; the rest kept or marked "?". Two cross-over-box signs written "gn" were renamed dq (the key's mm sign; context "comme"), marked "?". Result: the final transcription `data/transcription/<page>.txt`. Because passes 2 and 3 were used for corrections, they are not reported as independent.
   - We also found that the line images used so far stopped at 94% of the page width and cut 1–3 symbols at the end of some lines (notably p.526). The line images were re-cut at the same line positions up to 99% of the width (`src/recut.py`).
6. **Independent second transcription** (`second/<page>_pass4[abc].txt`): after the final transcription was fixed, Codex read the re-cut line images three times, each in a new context, without seeing it, with `second/PROMPT3.md` (PROMPT2 plus descriptions of 8 vs 4, the cross-over-box sign and line-end symbols; no values, key or reading). The run logs contain one reply each and no command execution. The lowest of the three runs is the one that counts.
7. **Reading**: `src/vk.py decode` (→ `data/decoded/`), word division by Claude Opus 5.5 (`docs/READING*.md`).
8. **Control**: the letter values of the key shuffled among the letter symbols 1,000 times; each shuffled key and the real key scored on runs of single-letter symbols by a character-trigram model of French (wordfreq, top 50,000 words; j→i, v→u). `src/vk.py control`.
9. **Calibration**: two pages with a contemporary decipherment in the margin, chosen before any result was seen — p.258 and p.285 (Vulcob, 1576) — were processed exactly like the undeciphered pages without the margin being seen: line images without the margin; first transcription by Claude Sonnet 5.5 (`calib/p258_first.txt`, `calib/p285_first.txt`); disagreements with the majority of three Codex runs adjudicated by image (`calib/p258.txt`, `calib/p285.txt`, `xcheck/adjudication_img_p258.tsv`, `..._p285.tsv`); key applied (`calib/p258_decode.tsv`, `calib/p285_decode.tsv`). Each margin was transcribed separately by Claude Sonnet 5.5 and by Codex, and the differences adjudicated by image (`calib/p258_margin_adj.txt`, `calib/p285_margin_adj.txt`, with logs). The decodes were compared letter by letter with the adjudicated margins (`src/calib.py`); the two pages together decide.

## Numbers
**Independent second transcription** (final transcription vs each of the three independent runs; symbols mapped to values, aligned per line, `src/xcompare.py`). The lowest run counts.

| run | p.525 | p.526 | p.539 | p.561 | p.562 | p.563 | p.565 | 7 pages | p.570 | p.33 (calibration page) |
|---|---|---|---|---|---|---|---|---|---|---|
| pass 4a | 98.2% | 96.1% | 97.4% | 98.0% | 95.8% | 95.7% | 88.8% | 4,176/4,357 = 95.8% | 76.9% | 87.3% |
| pass 4b | 97.9% | 96.3% | 97.4% | 97.7% | 95.1% | 96.1% | 91.8% | 4,186/4,357 = 96.1% | 84.6% | 87.7% |
| pass 4c | 97.7% | 91.9% | 96.9% | 98.2% | 90.5% | 95.7% | 96.4% | 4,149/4,357 = 95.2% | 80.8% | 83.8% |
| **lowest** | 97.7% | 91.9% | 96.9% | 97.7% | 90.5% | 95.7% | **88.8%** | 95.2% | **76.9%** | 83.8% |

By symbol name instead of value (`src/namecompare.py`), all nine pages: pass 4a 92.6%, 4b 92.9%, 4c 92.0%; on the seven read pages the lowest page is p.565 87.0% (pass 4a). For the record (these readings were used for corrections and are not independent): pass 2 86.6% and pass 3a–c 94.5–94.9% against the intermediate transcription.

**Control** (`xcheck/control.tsv`, 1,000 shuffles each; "table only" = only symbols in Tomokiyo's table):

| page | symbols scored | real key | best shuffled | shuffled ≥ real | table only: shuffled ≥ real |
|---|---|---|---|---|---|
| p.33 | 242 | −1.859 | −3.444 | 0 | 0 |
| p.525 | 879 | −2.810 | −4.524 | 0 | 0 |
| p.526 | 514 | −2.924 | −4.420 | 0 | 0 |
| p.539 | 174 | −2.045 | −3.843 | 0 | 0 |
| p.561 | 706 | −3.151 | −4.395 | 0 | 0 |
| p.562 | 810 | −2.914 | −4.311 | 0 | 0 |
| p.563 | 529 | −3.000 | −4.398 | 0 | 0 |
| p.565 | 533 | −2.933 | −4.349 | 0 | 0 |
| p.570 | 22 | −3.770 | −3.580 | **4** | **8** |

p.570 (one line) does not reach 0/1,000; it has a contemporary decipherment in the margin of p.569, which the key output matches (READING).

**Calibration** (letters only; long gaps of ≥4 letters — code-word positions and text outside the margin's span — are not scored):

| page | letters scored | agree |
|---|---|---|
| p.258 | 412 | 333 (80.8%) |
| p.285 | 148 | 125 (84.5%) |
| **both** | 560 | **458 (81.8%)** |

With the reference margin replaced by the word-level majority of five independent readings (Codex 3 runs — one of them the reading used in the adjudication above — and two Claude Sonnet 5.5 readers; none saw the cipher, the decode or the other readings; `calib/readers/`, `src/mvote.py`, `calib/p258_margin_vote.txt`, `calib/p285_margin_vote.txt`). The method and tie rule were fixed before the result was seen; decode and scoring unchanged:

| page | letters scored | agree |
|---|---|---|
| p.258 | 398 | 341 (85.7%) |
| p.285 | 148 | 128 (86.5%) |
| **both** | 546 | **469 (85.9%)** |

Against the other margin readings the p.258 decode gives 82.1% (Sonnet) and 85.8% (Codex); the reference itself is uncertain, and the p.285 margin is faint (13 of 18 lines keep uncertain words). Many letters are not scored, mostly where the margin spells out what the cipher gives as a plain-letter code word. For the record: Codex pass 1 alone, decoded, against the margin of p.33 (read by Claude Opus 5.5): 85.5% (234 letters).

**Share of symbols with a value** (final transcription, nine pages): of 4,672 symbols and plain-letter groups, 4,552 (97.4%) have a value, 18 (0.4%) are unreadable, 102 (2.2%) are plain-letter groups (code words or nulls), most without a known meaning.

**Status: full reading.** On the seven read pages (p.525–526, 539, 561–565): control 0/1,000 on every page; lowest independent agreement 88.8% (p.565), 95.2% over the seven pages; 97.4% of symbols have a value; calibration 85.9% on two pages (against the five-reader majority margin; 81.8% against a single adjudicated margin reading). Most code words are unexplained (OPEN section 3). The single line on p.570 turned out to have a contemporary decipherment in the last margin line of p.569 ("… quil ny reussiroit(?) peu ou point de proffit"), so it was not undeciphered; the key output ("…[ss]iroit peu ou point de profit") agrees with it.

## AI use (COPE disclosure)
- Claude Opus 5.5 (Anthropic): prior-work search, key table, first transcription of p.33 and p.539, coordination, decoding, word division, the 15 context reversions and 2 sign renamings, documents.
- Claude Sonnet 5.5 (Anthropic): first transcription of p.525–526, 561–565, 570 and of the calibration pages p.258 and p.285; image adjudication of all disagreements (two rounds); transcription and adjudication of the p.258 and p.285 margins; search for code-word meanings in the deciphered letters (mostly unsuccessful).
- OpenAI Codex CLI 0.163.0-alpha.10.2 (default model): cross-check transcription (pass 1), further transcriptions used for correction (pass 2, pass 3a–c), the independent transcriptions (pass 4a–c), transcriptions of the p.258 and p.285 margins.
- A separate Claude reader that took no part in the decipherment searched for prior work (docs/PRIOR_CHECK.en.md).
- **No human has checked the transcriptions, the adjudication or the readings against the manuscript.** Agreement between AI systems is not a substitute for a human check.

## Limits
- Look-alike symbol pairs (OPEN.en.md section 2) are decided partly by context; uppercase letters in the key output mark the uncertain ones.
- Code words are mostly unexplained (OPEN.en.md section 3); the readings put them in [brackets].
- Calibration rests on two pages and on AI readings of their margins.
- p.570 has one line (22 symbols scored), 4/1,000 in the control; it agrees with the contemporary decipherment in the margin of p.569.
