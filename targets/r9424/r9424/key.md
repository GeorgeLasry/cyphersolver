# R9424 key (Ryan Xu, 23 Oct 2026)

Recovered ciphertext-only by Ryan Xu ([ry-xu](https://github.com/ry-xu)) with Claude Opus 5.5, from this repository's
`r9424/transcription.txt`, and posted as issue #89 ("Solution: r9424"). His write-up, scripts and controls:
https://github.com/ry-xu/slightlysupervised/tree/main/wilhelm-1583-cipher (no licence stated; cited, not copied).
Checked on the DECODE images by Claude Opus 5.5 on 23 Oct 2026 (`R9424_corrections.tsv`).

Labels are those of `transcription.txt`.

| sign | value | note |
|---|---|---|
| a | n | |
| c | t | |
| d | c / k | dD = ch; at word edges often a null |
| D | h | |
| e | s | |
| i | u / v / f | i/ = w; ii = fu |
| k | e | also ö (gresten, bese) |
| m | z | m in Latin words; often a null at word edges |
| n | m | also n, u/v (one label for look-alike glyphs) |
| o | i | |
| q | y | |
| r | a | r in 2 words (drey, kriegswesen before re-labelling) |
| s | l | |
| t | p | |
| w | b | |
| z | d / r | two glyphs under one label: hooked/tailed z = d, flat-footed 2 = r (image, 23 Oct) |
| 3 | g | |
| 4 | o | |
| / | doubles the previous letter | s/ = ll, c/ = tt, e/ = ss, a/ = nn, n/ = mm, z/ = rr |
| g, y, p, b | nulls | at word edges |
| o-o barred (#) | unread nomenclator sign | 3 times |

Structure noted by Ryan Xu: the values form chains (plain → cipher) p→t→c→d→z→m→n→a→r, l→s→e→k, u→i→o→4, i.e. each
plain letter is written as the next letter of a scrambled sequence.

Controls (his): 65% of cipher words of 4+ signs decode to a word of a 135k-type 16th-century German lexicon (DTA) under
the key, against a median 8% (max 24%) for 40 shuffled keys of the same ambiguity; from-scratch annealing with a DTA
1500-1599 4-gram model, no cribs, recovers 11 signs covering 70% of sign tokens (seed 2).
