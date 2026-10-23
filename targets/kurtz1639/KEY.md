# Kurz von Senftenau cipher, 1638-39: the rebuilt key

Rebuilt 19 Sept 2026 from the contemporary interlinear decipherment on R3811 p.1 and the structure it shows, then
extended with a German n-gram model and read-through. `key.json` is the machine form (H41 = consonant of 41-45, etc.).

## Consonant+vowel signs 41-100

Each ten is split into two halves with one consonant each, in reverse alphabetical order from 41 (r p n m l k h g d c b).
Units 1-4 of a half run o i e a with that half's consonant. The fifth place of every half is a separate series of
consonant+u signs in its own order (pu lu mu hu ku du gu bu cu . us ru), found from context, not from the table pattern.

| | +1 o | +2 i | +3 e | +4 a | +5 |
|---|---|---|---|---|---|
| 41-45 | ro (68) | ri (173) | re (433) | ra (185) | pu (21) |
| 46-50 | po (57) | pi (24) | pe (74) | pa (47) | lu (55) |
| 51-55 | no (59) | ni (258) | ne (229) | na (51) | mu (33) |
| 56-60 | mo (26) | mi (120) | me (132) | ma (154) | hu (31) |
| 61-65 | lo (78) | li (207) | le (168) | la (109) | ku (7) |
| 66-70 | ko (60) | ki (10) | ke (33) | ka (29) | du (29) |
| 71-75 | ho (59) | hi (72) | he (203) | ha (126) | gu (27) |
| 76-80 | go (13) | gi (48) | ge (329) | ga (37) | bu (51) |
| 81-85 | do (21) | di (213) | de (517) | da (135) | cu (28) |
| 86-90 | co (114) | ci (65) | ce (17) | ca (35) | cu (1) |
| 91-95 | bo (15) | bi (20) | be (301) | ba (34) | us (17) |
| 96-100 | ? (0) | is (24) | es (24) | e (17) | ru (68) |

Irregular: 97 = is, 98 = es, 99 = e (uncertain), 100 = ru; 96 not seen.

## Single signs (numbers 1-40, letters, graphic signs)

| sign | value | count |
|---|---|---|
| `28` | r | 1421 |
| `31` | n | 1392 |
| `27` | s | 1265 |
| `26` | t | 1145 |
| `39` | c | 856 |
| `35` | h | 670 |
| `18` | e | 608 |
| `19` | e | 514 |
| `17` | i | 511 |
| `33` | l | 499 |
| `#z-tail` | n | 497 |
| `w` | n | 470 |
| `9` | te | 456 |
| `37` | f | 428 |
| `36` | g | 342 |
| `15` | i | 341 |
| `25` | u | 309 |
| `22` | a | 302 |
| `π` | m | 298 |
| `ψ` | z | 258 |
| `38` | g | 244 |
| `#s-long` | t | 240 |
| `40` | b | 225 |
| `21` | a | 223 |
| `10` | u | 222 |
| `x` | i | 212 |
| `6` | se | 204 |
| `20` | e | 200 |
| `13` | o | 195 |
| `11` | u | 189 |
| `23` | a | 186 |
| `16` | i | 183 |
| `c` | si | 183 |
| `#4-hook` | w | 173 |
| `24` | w | 165 |
| `34` | k | 160 |
| `α` | m | 151 |
| `p` | null / unread | 134 |
| `30` | p | 131 |
| `d` | so | 123 |
| `n` | ve | 119 |
| `12` | o | 98 |
| `14` | o | 97 |
| `32` | m | 95 |
| `#l-loop` | tu | 68 |
| `#s-loop` | null / unread | 60 |
| `29` | qu | 53 |
| `φ` | z | 45 |
| `Δ` | e | 44 |
| `#dot` | null / unread | 42 |
| `1` | i | 29 |
| `3` | null / unread | 27 |
| `m` | null / unread | 23 |
| `4` | null / unread | 22 |
| `#sect` | w | 18 |
| `7` | s | 17 |
| `k` | ti | 15 |
| `λ` | null / unread | 13 |
| `5` | sch | 11 |
| `v` | s | 8 |
| `2` | null / unread | 8 |
| `0` | ti | 8 |
| `#s-cross` | t | 7 |
| `e` | null / unread | 7 |
| `2?` | ? | 6 |
| `8` | s | 4 |
| `3?` | ? | 4 |
| `4?` | ? | 4 |
| `#hash` | s | 4 |
| `r` | i | 3 |
| `?` | ? | 3 |
| `#z-bar` | e | 3 |

Values of signs seen fewer than 3 times are in key.json and are uncertain. Two-letter values for single signs (9 te, 6 se,
c si, n ve, d so, k ti, #l-loop tu) were fixed from context and the glosses.


## Revisions, 21 Sept 2026 (second pass)

- α (small upright a) = **sa**, not m; the larger looped ℒ-form is a separate sign, `#a-loop` = **m**.
- `#f-cross` (crossed ƒ-like sign, R3813) = **ta**; pass 1 had merged it with `x` (i).

## Corrections, 22 Oct 2026 (re-read batch b06)

Made after kwic checks over all nine letters (read/<rec>_reread_log.md, research/reading_audit/b06_*.py):

| sign | was | now | evidence |
|---|---|---|---|
| `38` | g | d | feindt, und, landt, wurdt, standt, Teutschlandt, bald (all ~250 uses; 36 stays g) |
| `Δ` | e | nu | warnung, hoffnung, nun, nuzen, Nuncio, gefangnus, continuieren, eigennutz |
| `#dot` | null | su | sufficient, subsidia, disunirter, verfassung, suspiciones, succurs, summum periculum |
| `#s-long` | t | ti | militaria, resolution, obligation, negotiirt, particular, fertig (glossed ti on R3811 p. 1); in R3815's hand it also stands as a flourish, and a few words need a plain t (tausendt in R3812) |
| `m` | null | a | after 29: quartier, quam, quando, aliquam, quae |
| `pv` | (new) | vi | the crossed long-s `p` (otherwise a null or, after 27, #f-cross = ta) read vi: Salvius, resolviren, proviant, privilegia; tokens relabelled pv only where vi makes the word |
| `9v` | (new) | vo | a polyphonic 9, the same shape as 9 = te: Volck, von, vor, voluimus, darvon, vormaur; tokens relabelled 9v in tr/ only where te gives no word |

Open: the crossed long-s `p` (null) reads vi in Salvius, resolviren, proviant (and ta after 27, relabelled #f-cross); `x`
also reads to / su / vi in a few words; `#sect` reads z in R4645 and R4736 (w in R3811's glosses); `#hash` = x
(ex, rex). Printed with brackets in the readings.

## Corrections, 23 Oct 2026 (r2c), checked against Jakub Mírka's key

DECODE R3813 and R3814 carry two attachments not seen before: Mírka's key reconstruction as an Excel sheet (2022-11-30)
and a handwritten table (one page). His table agrees with this key in its structure (41-100 consonant+vowel signs, 97-99
is/es/as, 100 ru) and gives the letter signs as a series sa a, se b, si c, so d, su e, ta f, te g, ti h, to k, tu l,
va m, ve n, vi p, vo q, vu r; y = x; nulls φ λ ∂ β ν. Our labels map onto it: α = his a (sa), 6 = b (se), #dot = e (su),
#f-cross = f (ta), 9 = g (te), #s-long = h (ti), #l-loop = l (tu), pv = p (vi), 9v = q (vo), Δ = his NU sign.
Two values here disagreed with his and were checked at every occurrence:

| sign | was | now | evidence |
|---|---|---|---|
| `k` | ti | to | all 17 uses: protectorium, electores, multorum, a proposito, bis dato, in puncto, super puncto, tradimento, contento, (mal) sadisfatto, nondum reconciliatos, regi non acceptos; none needs ti |
| `m` | a | va | non-29 uses: negativam, vanitet, riserva, avantagiosen, enervatis, valedi(c)it; after 29 (= qu) the v is not written twice: decode.py now gives 29 + m = qua, 29 + 9v = quo (quod) |

`4`: the x-reading places (ex concluso, extremam, perrexit, ex defectu, rex, Oxensternio, extremitates) are a crossed 4 on the images (Mírka's X sign; glossed x on R3811 p. 1, where the transcription already had `4+=x`); parse.py strips `+`, so the crossed form had been merged with the plain 4. New label `#4-cross` = **x** (7 tokens); the plain 4 (R3814 P1 "denomina-d-4-e", R3813 P15 "um 4 so", the numeral "4." on R3814 P2) stays unvalued; `x` = i (Mírka y),
same reading in this German. `9v` = vo (22 Oct) holds at all 48 uses in the nine letters (volck, von, vor-, voluerit,
voluimus, bevor, vom) and is Mírka's q. Labels corrected on the images in R3813 (crossed sign → pv 20, p → pv 3, d → k 8,
α → k 1) and R3814 (9 → 9v 2, 9 → #sect 1), with crossed sign/p → pv in R3812 (5) and R3815 (1), x → k in R3811 (3), 4 → #4-cross in R3811-R3813 (7): read/<rec>_corrections.tsv.
