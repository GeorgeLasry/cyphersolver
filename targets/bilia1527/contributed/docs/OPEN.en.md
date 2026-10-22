# Open questions

[日本語](OPEN.md)

## 1. f. 102v (7 cipher lines): reading unconfirmed, not given
- Values can be assigned, but much of it does not read as sentences. Line ends run into the gutter and many digits are faint.
- Figures (transcription data/transcription_f102v_unconfirmed.txt, 118 signs):
  - Value agreement with the independent second transcription (Codex, 3 runs): 82.2, 83.1, 83.1% (by name 75.4, 79.7, 79.7%), below the 85% set for calling a reading complete.
  - Key-shuffling control (1,000 shuffles): with all signs, 0 shuffles at or above the real key (real −2.821, best −2.845); with key-sheet signs only, 24 (real −2.795, best −2.537). Before the second round of image checks: 5 and 17. Not clearly distinguished from chance.
  - Signs with a value: 110/118 (93.2%).
- Passages that seem to read (for reference only, not confirmed): "… a suo genero o a qual[che] (u)ino deli soi …", "… quale con [de]siderio si aspeta …", "… con le risposte di …".

## 2. No. 42 (ff. 99r–v, Bilia to Jo. Francesco Zaberna (Taverna, the Duke of Milan's ambassador), same date): not read
- A different cipher from no. 43 (base letters M, A, K, H, B, Π … with numbers 1–29). Neither R5258 nor Bilia's numerical alphabet R5237 fits.
- Its key is probably among the Milan key sheets (Carteggio Sforzesco cart. 1591, 1597, 1598). No letter in this volume (fr. 3013) carries a decipherment in the same key.

## 3. f. 102r: 8 places where the image checks disagree (first reading kept)
Two models (OpenAI Codex and Claude Sonnet) judged each place separately on enlarged images, twice; these places stayed split. Positions are the order within the line in check/round2/verdict.tsv (before the corrections).

| line | position | this reading | Codex transcription | Codex judgement | Sonnet judgement |
|---|---|---|---|---|---|
| 102r.02 | 4 | B.39 | B.33 | B.39 | B.33 |
| 102r.03 | 17 | 3p | np | np | 3p |
| 102r.07 | 6 | tt | a++ | a++ | tt |
| 102r.07 | 11 | np | mp | mp | np |
| 102r.08 | 13 | 31 | 39 | 39 | 31 |
| 102r.15 | 11 | r7 | np | np | r7 |
| 102r.17 | 15 | G.77 | G.27 | G.77 | G.27 |
| 102r.30 | 16 | B.51 | B.53 | B.51 | neither (B.57) |

## 4. f. 102r: unknown signs and name codes
- B.3? at the end of 102r.20: second digit unreadable; taken as B.36 (ca) from "certifi[ca]to" (inferred).
- B.58 (102r.02): a name code; the name is unknown (data/key.tsv gives the provisional value of D.58 = mi).
- "conte Theophimo" (102r.06): not identified.

## 5. Values not checked against the key sheet
These signs have no matching form in the transcription of the key sheet; their values were inferred from this letter (41 signs on f. 102r, 8.1%): ß = r (14), £ = l (12), F = c (6), tt = t (5), qx = ss (4) (source column of data/key.tsv). The key-sheet image itself was not seen (the values rest on the transcription of the sheet).

## 6. Doubtful readings
- 102r.13 "per pervitio": a slip for servitio, or a misread sign.
- 102r.18 "in e[a++]etto": a++ is a null on the key sheet; here it looks like ff.
- 102r.27 "vechilza", "tompi", 102r.14 "papre": these readings result from signs corrected after the image checks. Writer's slips or misreadings: undecided.
