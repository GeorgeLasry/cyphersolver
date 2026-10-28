# Dorabella hypothesis loop (28 Oct 2026)

Harness: `hyp.py` (calibration, ledger), `rounds.py` (hypotheses), `run_round.py`. Every hypothesis is scored on
Dorabella, on shuffles of its signs (or doublet-preserving shuffles, which keep every adjacent pair) and on English
put through the hypothesised system. Full numbers: `ledger.tsv`. "Above nulls" alone is the known sequential
structure (repeated bigrams, opposite flips), not a reading; a reading must reach the control range.

| round | family | hypotheses | outcome |
|---|---|---|---|
| 1 | fractionation | Bacon biliteral (80 readings); arcs as ternary triplets (3 phases); orientation pairs as 64 values (2); unordered pairs, semaphore-like (2) | negative; unordered pairs phase 0 beats 40 doublet nulls (P < 0.025, one test of ~8, gibberish, controls 16–98%): not significant |
| 2 | Morse | sign = dot/dash, unsegmented (16 readings, DP decoder); sign = whole letter, arcs = length (768 labelings); run-length (arcs = repeats) | negative |
| 3 | context keys | Vigenère/Beaufort/variant × 27 keywords (courage, dorabella, prudentia …) × 32 grids; autokey; Gronsfeld from the date 14.97 | negative (−5.7 to −6.2 vs controls −1.8 to −2.4) |
| 4 | running key | every offset of KJV, Shakespeare, verse anthology, Gutenberg prose, Powell 1937; 4 Elgar grids × 3 rules | negative (−5.16; controls recovered −2.0 to −2.4) |
| 5 | writing order | 4 line orders; boustrophedon mirrored line 2; lines 1+3 mirrored; line 2 mirrored; each line upside down | negative (best two re-run with 15 nulls: above shuffles, no better than the plain order, gibberish) |
| 6 | per-line keys | per-line dial + arc shift; arc shift only; per-line progressive rotation a = 1–4 | negative |
| 7 | plaintext form | consonant skeleton; back-slang; first-3-letter abbreviations; homophones ≤ 3 | negative (skeleton re-run 20 restarts/12 nulls/6 ctl: −2.500 below all controls) |
| 8 | transposition | all columnar w = 2–7 (5,913 orders), rail fences, snake columns, screened by repeated pairs (key-free); top 3 solved | negative: no order beats the written one (19 pairs; best 20; shuffles reach 19–23) |
| 9 | languages | Dutch, Portuguese, Danish, Swedish, Welsh, Polish, Hungarian (own-language controls) | negative (all below recovered controls; Polish test without power) |
| 10 | fixed cribs | 14 openings at the start; 9 sign-offs at the end; both together | negative: no sign-off is possible (last two signs differ, longer closings conflict); only "dora"/"dear" fit the start, gibberish after |
| 11 | source type | key-invariant statistics (distinct, IoC, repeated pairs, doubles, singletons) vs English, Latin, German, French, Elgar's letters, word initials, phonemes, music | **diagnostic**: typical of English letters (P 0.84) and Elgar's letters (0.89); atypical of phonemes (0.002), music (0.03), Latin (0.04) |
| 12 | Playfair; space sign; regular nulls | Playfair on 3×8/8×3 grid; each of the 8 commonest signs as word space; drop every k-th sign (k = 2–6, all phases) | negative; Playfair excluded by logic (identical signs inside a digraph under every pairing) |
| 13 | musical alphabets | orientation = German note name a–h (40,320); 3 rows × 8 "keyboard" with any column/row order (241,920) | negative |
| 14 | misaligned streams | arcs shifted ±1–3; arcs reversed; orientations reversed; arcs reversed per line | negative (controls 0.94–1.00) |
| 15 | polygraphic units | signs = letters + top digraphs + short words (66 units); all digraphs (60); nomenclator (letters + 6 words) | negative / no power: nomenclator beats 15 shuffles but its controls come back only 16–28% similar to the truth; word salad |
| 16 | key changes partway | two interleaved messages; new key from line 2; new key at halfway; key per line | **no power** (controls 0–31%): untestable at 87 signs, not negative |
| 17 | vowels and flips | Sukhotin vowels; V/C alternation vs English; vowel signs by orientation; flips vs V/C switches | alternation English-like (0.709 vs 0.733, P 0.34); vowel signs spread over 6 orientations, not one side; flips switch V/C only slightly more (0.74 vs 0.69): **the flips are not vowel/consonant alternation** |
| 18 | known quotation; Elgar table + transposition | 87-letter windows of KJV, Shakespeare, verse, Gutenberg prose, Elgar's letters, Powell 1937 (misread-tolerant one-to-one fit); Elgar's table (832 variants) letter frequencies | negative: best quotation fit 37/87 (shuffles 35–36, real quotation with 6 misreads 79–81); Elgar's table gives no English frequencies (−3.205, random tables to −3.18), so "his table + scrambled order" is out |
| 19 | mixed alphabets; block rearrangement | keyword-mixed alphabets × 32 grids × 24 shifts (41,472, direct); arcs rotated/reversed within blocks p = 2–6 | negative |
| 20 | syllabic script; longer structure | sign = consonant class × vowel class (24 units, English converted); repeated 3- and 4-grams vs English and pair-keeping shuffles | syllabic negative; trigram/4-gram counts (2, 0) fit both English (P 0.26, 0.45) and a pair-by-pair generator: **cannot discriminate at 87** |
| 21 | misreads, more compute | alternating key/slip search, ≤ 8 orientation slips, 30 restarts | partial power now (controls with 6 seeded slips 45–89%, median 0.57); Dorabella −2.739 below every control (−2.65..−2.12), gibberish: **a substitution behind ~6 misreads is unlikely** |
| 22 | quotations from Elgar's reading | Longfellow complete (incl. King Olaf), Evangeline, Idylls of the King, Tennyson early poems, The Princess, Browning shorter poems: letter by letter and word initials, misread-tolerant | negative: best 34/87 both ways (shuffles 32–35; real quotation with 6 misreads 80–82) |
| 23 | Nihilist with known keys | coordinate addition/subtraction with 27 keys (COURAGE …) × 32 grids; key restarting per line | negative (−5.9..−6.0 vs controls −1.8..−2.1) |
| 24 | July 1897 visit cribs | 29 words from Powell p. 9 (kites, Boscobel, oak, Caractacus, lullaby, mother …) at every fitting offset, key annealed around them | negative: best "mother"@47, −2.889 (shuffles −3.03..−3.37, recovered English −1.7..−2.0); scraps around the crib, gibberish elsewhere |
| 25 | pseudo-text | a writer with two habits (flip often, sometimes repeat) at Dorabella's own sign rates, vs English under a random key, on 6 key-invariant statistics (incl. flips) | **neither explains it**: pseudo-writer P 0.008 (flips yes, repeated pairs 9.4 vs 19 no); English under random key P 0.013 (pairs yes, flips 10.8 vs 27 no) |
| 26 | English under a flip-heavy key | the letter layout that maximises opposite steps for English (a/e/t opposite h/r/s …) | **all six statistics typical (P 0.711)**; flips ≥ 27 in 32% of samples. Best-supported generator: English letters under a key with common neighbours on opposite orientations |
| 27 | every plausible reading at once | 48 positions with alternatives (consensus, attested, measured, both neighbours near a boundary), joint key + reading search, en-modern and en-elgar | **no power**: controls 0–83% / 8–29%; Dorabella among its shuffles. The transcription doubts are too many to decide at 87 signs; round 21 (~6 slips) is the limit of what this length allows |
