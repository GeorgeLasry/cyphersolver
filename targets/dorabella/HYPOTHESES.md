# Dorabella hypothesis map

The space of explanations, layer by layer. A reading needs one choice at every layer. Each branch carries a status and
its evidence (NOTES.md steps "S n", loop rounds "R n" in runs/loop.md, numbers in runs/ledger.tsv).

Status: **NEG** tested with power and negative · **NP** tested, no power at 87 signs (cannot be decided by
calculation) · **X** excluded by logic · **OPEN** not yet tested · **DIAG** a diagnostic, not a reading.

Calibration for every test: Dorabella vs shuffles (or doublet-preserving shuffles) vs English put through the same
system. A reading must reach the recovered-control range; beating shuffles alone is the known sequential structure.

## L0 Is there a message?

| branch | status | evidence |
|---|---|---|
| random scribble | X | repeated pairs 19 vs 11.2 (P 0.004), S 7 |
| hand doodle (gradual turning) | X | turns larger than chance, no sweeps, S 16 |
| deliberate pseudo-text (made to look like a cipher) | NEG for a two-habit writer (P 0.008); richer human generators untestable here | R 25 |
| English-like letter source | DIAG, supports | key-invariant statistics typical of English letters (P 0.84) and Elgar's letters (0.89), R 11 |
| opposite-orientation flips (27 vs 12.6) | DIAG, explained by the key layout | English under a flip-heavy layout reproduces all six key-invariant statistics (P 0.711; flips ≥ 27 in 32%), R 26; not V/C alternation R 17, not word breaks S 22 |

## L1 Transcription

| branch | status | evidence |
|---|---|---|
| Hauer 2025 five-reader consensus | NEG under every L3–L5 branch below | S 2–8 |
| attested reader disputes (11 positions, 2^11) | NEG | S 9 |
| measured from the 1937 plate (17 changes, 23 positions joint) | NEG | S 11 |
| free misreads (≤ 10 orientation slips) | NP at ≥ 10; ~6 slips unlikely (partial power, R 21) | S 5, 6, R 21 |
| all plausible readings jointly (48 positions) | NP | R 27 |
| better image (greyscale 1946/1949 plate) | OPEN, needs outside access | — |

## L2 Plaintext

| branch | status | evidence |
|---|---|---|
| English, standard spelling | NEG | S 2–3, 9, 11 |
| Elgar's register (his letters) | NEG | S 14 |
| English reversed / back-slang | NEG | S 3, R 7 |
| consonant skeleton / abbreviations | NEG | R 7 |
| phonetic English (25 sound classes) | NEG; 39 classes NP | S 24 |
| word initials (model) | NP | S 18a |
| Latin, French, German, Italian, Spanish | NEG | S 3 |
| Dutch, Portuguese, Danish, Swedish, Welsh, Hungarian | NEG | R 9 |
| Polish | NP | R 9 |
| music (pitch × duration) | NEG for the Lullaby cribs; general music model NP | S 20, 25; Hauer 2025 |
| a known quotation enciphered letter by letter | NEG (KJV, Shakespeare, verse, prose, Elgar's letters, Powell; Longfellow incl. King Olaf, Tennyson, Browning) | R 18, R 22 |
| numbers / a date / an address | NP (digits carry no redundancy to test against) | — |

## L3 What a sign stands for

| branch | status | evidence |
|---|---|---|
| one letter (simple substitution) | NEG | S 2–3 |
| homophonic (≤ 2, ≤ 3 per letter) | NEG | S 3, R 7 |
| polyphonic: axis × arcs = 12 | NP | S 17 |
| the turn between signs | NEG | S 21 |
| fractionated: Bacon, ternary arcs, orientation pairs, semaphore pairs | NEG (pairs marginal, not significant) | R 1 |
| Morse (element, letter, run-length) | NEG | R 2 |
| polygraphic: digraphs, letters + words, nomenclator | NEG / NP | R 15 |
| syllables (consonant × vowel abugida) | NEG | R 20 |
| German note names a–h; 3 × 8 keyboard | NEG | R 13 |
| Elgar's own table, all 1.08 M ordered layouts | NEG | S 1 |

## L4 Key layer

**Excluded as a whole by the flips (R 29):** every table-changing layer (periodic dial, Vigenère, autokey, running key,
Nihilist, progressive dial) drops English-under-a-fixed-flip-table from 24.5 flips to 7.7–11.5, P(≥ 27) ≤ 0.001. Dorabella
has 27, so it was written with one fixed table throughout. The rows below stay as the direct tests.

| branch | status | evidence |
|---|---|---|
| none | NEG (= L3 one letter) | S 2 |
| dial rotation, periodic / progressive | NEG | S 8 |
| Nihilist on both coordinates | NEG | S 12B |
| Roe grid + keyword or dial key, any group order | NEG | S 12A, 12C |
| Nihilist with known keys (COURAGE …) | NEG | R 23 |
| context keywords, autokey, date digits | NEG | R 3 |
| running key from KJV, Shakespeare, verse, prose, Powell | NEG | R 4 |
| per-line keys, per-line progressive | NEG | R 6 |
| key change partway (interleaved, by line, by half) | NP | R 16 |
| keyword-mixed alphabets laid on Elgar's table (direct, no solver) | NEG | R 19 |
| Elgar's own table + transposition (letters right, order scrambled) | X (his table gives no English letter frequencies) | R 18 |

## L5 Order layer

| branch | status | evidence |
|---|---|---|
| reversal, boustrophedon, line orders, mirror, upside-down lines | NEG (full power: every per-line reversal mix, columns, spiral, diagonals, with and without misreads) | S 3, R 5, R 44, R 48, R 65, R 66 |
| columnar w ≤ 7, rail fence, snake, decimation | NEG / X (written order already has the most repeated pairs) | S 3, R 8 |
| misaligned orientation / arc streams | NEG | R 14 |
| nulls (by class, rare signs, every k-th) | NEG | S 15, R 12 |
| one sign is a word space | NEG | R 12 |
| flips are word breaks | NEG | S 22 |
| block-wise rearrangement of coordinates (bifid-like) | NEG | R 19 |

## L6 Context

| branch | status | evidence |
|---|---|---|
| floating cribs (50 words) | NEG | S 7 |
| fixed openings / sign-offs | X for sign-offs; NEG for openings | R 10 |
| Lullaby melodies | NEG | S 20, 25 |
| Playfair (cipher pairs never identical) | X | R 12 |
| cribs from the July 1897 visit (29 words) | NEG | R 24 |

## Frontier: where to attach next (ranked)

Ranked by how much each could change the verdict, given that the flips force a fixed table (R 29) and that the
loop's solver recovers real English at 87 signs only ~58% of the time, Elgar's own letters ~42% (R 30).

1. **Search failure or model failure?** On failed Elgar-letter controls, does the true text outscore the solver's
   answer? (R 31, running.) If search fails, a far larger search could still find a reading.
2. **A much larger search on Dorabella** — 920 restarts × 60k steps × {en-modern, en-elgar} × {consensus,
   measured} on 23 cores (R 32, running). Compare the best score with real Elgar text's scores.
3. **Fixed flip-heavy table as a prior, with misreads** (R 28, running).
4. **Fixed-table plaintext models not yet tried:** short-note register (greetings, names, dates), word-boundary-free
   English with Elgar's nicknames (Dorabella, Penny, Alice, Carice …) boosted.
5. **Untested coverage cells that keep a fixed table:** other languages × misreads; Elgar register × transpositions.
6. Outside material: Courage cards, greyscale plate.

## Where the map stands (after 27 rounds)

- Every branch decidable on this machine is now NEG, X or NP. No branch is still OPEN except those that need outside
  material (a better image, a second text, human pseudo-text data).
- The best-supported generator is **English letters under a substitution key that puts common neighbours on opposite
  orientations** (R 26: all six key-invariant statistics typical, P 0.71). Under such a key a correct transcription
  would be solved ~98% of the time; it is not, so either the transcription is wrong in more places than 87 signs
  can absorb (R 21, R 27), or the English is unusual in a way none of the models covers.
- The one result that would change this: a second text in the same system (Courage cards), or a cleaner image
  that resolves the 48 doubtful positions.
