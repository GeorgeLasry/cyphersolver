# Gattinara cipher key (partial rebuild from his glossed words)

Status: PARTIAL. Built 2026-10-27 by an agent session from native-resolution autocontrast crops
(`img/small/gt_*`). Only alignments where gloss and signs could be matched letter by letter are used.
Coordinates are native x pixels of the full-resolution JPG. Sign names are ASCII labels for shapes;
several shapes may still be merged or split wrongly (see "Doubtful").

## Words used to build the key

| # | item / image / place | gloss (contemporary; pencil = modern) | signs (x) | letters |
|---|---|---|---|---|
| W1 | 23-5-4_04 l.3, x550-1000 | "Bastardi" (ink gloss + modern pencil letter-by-letter b a s t a r d i) | cross 7 x div 3 delta bbar pcross | b a s t a r d i |
| W2 | 23-5-4_04 l.3, x1080-1300 | "filij" | vroot qstem lo hash pcross | f i l i j |
| W3 | 23-5-4_04 l.3, x1350-1600 | "Archiepiscopi" (pencil h over `9`, i over `Drev`) | 7 ring lo 9 Drev ... | a . . h i ... (only a, h, i taken) |
| W4 | 23-5-47_04 main text, row y~830, x1660-2320 | "matrimonium" | Odot 7 div ofo rho vl T Phi qhook venusdot vl | m a t r i m o n i u m (11/11) |
| W5 | 23-5-47_04 postscript l.2, x180-400 | "fugat" | pdbl Phi? 8 7 div | f u g a t |

## Letter signs

| sign | shape | value | proof |
|---|---|---|---|
| 7 | digit 7 | a | W1, W3, W4, W5 |
| 3 | digit 3 (z-like) | a | W1 (2nd a) - one instance |
| cross | upright cross with hooked foot | b | W1 - one instance |
| x | x-cross with loops (looks like `x`/`ꝶ`) | s | W1 - one instance |
| div | short horizontal bar(s) with dot(s) (`÷`-like) | t | W1, W4, W5 (and see control) |
| delta | δ / open loop with stem | r | W1 |
| ofo | two small loops joined by a bar (`ofo`) | r | W4 |
| bbar | b with crossbar on the stem | d | W1 - one instance |
| pcross | p with crossbar on the descender | i / j | W1 (i), W2 (j) |
| qstem | q / loop on a tall stem | i | W2 |
| hash | double-cross `#`-like (two uprights, two bars) | i | W2 |
| rho | rho / p-loop with descender | i | W4 |
| qhook | q-like loop with hook | i | W4 |
| Drev | reversed D with descender | i | W3 (pencil) |
| lo | `L` joined to small `o` (`Lo`) | l | W2, W3 |
| vroot | radical/√ stroke (`v` with long right arm) | f | W2 |
| pdbl | p / b with double crossbar on the descender | f | W5 |
| 9 | digit 9 | h | W3 (pencil h) - one instance |
| Odot | circle with dot inside (⊙) | m | W4 |
| vl | `vl` / `W` ligature (zigzag) | m | W4 (twice) |
| T | small `T` | o | W4 |
| Phi | Φ / circle crossed by vertical stroke | n (W4); u? (W5) | conflicting - see Doubtful |
| venusdot | circle on a cross, dot (`♀`-like) | u | W4 |
| 8 | digit 8 | g | W5 - one instance |
| H | capital `H` | u/v | postscript l.1 "vult" (H venus lo div), used as control below, not for building |

Homophones are evident: a = 7, 3; i = pcross, qstem, hash, rho, qhook, Drev; r = delta, ofo; m = Odot, vl.

## Name signs (whole words)

| sign | shape | value | proof |
|---|---|---|---|
| STRUCK | group `x c + o` (or `Z c + o`) drawn through with a long horizontal stroke | Maiestas (Ma.) | 23-5-47_04 main text row y~960: `HT` + STRUCK (x2000-2290) under gloss "Ma" with tilde; postscript l.1: `?` + STRUCK (x240-430) under gloss "S. Ma" ("S. Mat. vult"). Also 23-5-4_11 (x2420-2520, gloss "Ma..."?) |
| HT | `H` followed by `T` | appears with STRUCK (before it in the main text, after it in postscript l.5); gloss covers the pair only as "Ma"; separate value not proven | |
| S°p° | `S` with superscript o, `p` with superscript o | a name sign; glossed on 23-5-4_07 row y~1450 (x2130-2250) but the gloss above it is not legible to me (looks like `duzza`/`dueza`?, next to "principis") | not resolved |

## Separators / nulls

| sign | shape | status |
|---|---|---|
| .1. | the digit 1 between two dots | frequent between groups; behaves like a word separator but appears inside the gloss span of single words (e.g. main text after "matrimonium": `delta six .1. 8 pcross Z .1.` under "Neapoli"), so it is not proven to be a null |
| dots | single dots after groups | separators |

## Doubtful / unresolved
- Phi = n in W4, but stands where u should be in W5 ("fugat"); the two shapes may differ (open Φ vs φ with tail) - not settled.
- bbar = d in W1, but the postscript l.3 repeat of "matrim[onium]" has `Odot bbar div ofo rho vl` where bbar stands for a - either two distinct b-shapes or a homophone; not settled.
- Unvalued signs met in the targets: vtick, aloop, orho, dcross, theta, Zcross, phicross, W, deltabar, Z, six, ring, four.
- Alignment of the "Neapoli" segment (main text row y~830 x2400-2640) and of "uxorem", "Francia", "alium" in the postscript could not be made letter by letter.

## Raw working notes
The step-by-step working alignments (including superseded ones) are kept in the session scratchpad only; everything that held up is in the tables above.

---------------------------------------------------------------------------------------------------
# SECOND PASS (2026-10-27): full alignment

## Name sign S°p° resolved
- 23-5-4_11 row y~1110, x470-560: `S°p°` at line start, contemporary gloss in the LEFT MARGIN "principis / Caroli" (a struck-out gloss above it).
- 23-5-4_11 row y~1950 (clear Latin line): "& S°p° habeat M^tas v^ra omnino illius memoriam"; interlinear gloss over S°p°: "principis Karoli".
- => S°p° = principis Caroli (Prince Charles, the future Charles V). 2 glossed instances.

## Row transcriptions and alignments (x = native px)

### 23-5-4_11 row y~905
signs: 8(620) T(670) Odot(720) pcross(770) plus(820) hp(850) lo(890) | div(1040) 9(1090) hp(1140) pcross(1200) 7(1250) H(1300) delta(1350) 6(1390) 7(1430) ofo(1530) pcross(1590) 8(1640) 8b(1680) vl(1750) orho(1830) H(1920) T(1960) Z(2020) bcross(2090) 3(2140) Odot(2190) ofo(2350) .1.(2420) 8(2500) pcross(2540) x(2570)
glosses: "Gomil"(680-770), "Thesaurari.."? (1050-1340, read `Tsosaurariu`), "quod"/"quenot"? (1850-1950), "Regi[s]"(2280-2400)
- "Regis" = ofo .1. 8 pcross x = r e g i s  -> .1. = e (!), 8 = g, x = s, pcross = i, ofo = r. SOLID (5/5).
- "Gomi..l" = 8 T Odot pcross plus hp lo = g o m i ? ? l (gloss has 5 letters for 7 signs; plus/hp unresolved, possibly "Gomiel" with one extra sign)

### 23-5-4_11 row y~1005
signs: Qloop(640) qdot(690) venusarm(760) 9(840) brev(900) qstem(950) hash(1000) x(1050) .1.(1110) delta(1180) six(1230) Hp(1280-1310) div(1380) T(1430) delta(1500) six(1540) Hl(1590) Odot(1650) vroot(1700) hp(1730) bbar(1790) .1.(1830) lo(1880) Qstem(1940) venuscross(2000) dagger3(2060) hp(2120) vl(2190) venusdotblack(2240) Odot-small(2300) STRUCK(2350-2490) vhook(2560)
glosses: "Philippo"(620-760), "servitor"(950-1100), "fidelissimus"/"fidelissi.."(1680-1900), "Ma.."(2130-2250), tilde(2400-2450)
- "servitor" = x .1. delta six Hp div T delta = s e r v i t o r (8/8, taking Hp as one sign = i) -> six = v.
- "fidelissimus" (start) = vroot hp bbar .1. lo ... = f i d e l ... -> bbar = d (2nd instance), hp = i.
- "Ma.. ~" over [vl venusdot Odot-small] + STRUCK: Maiestati V(estre) - pair again.

### 23-5-4_11 row y~1150 (signs y~1130-1170; glosses y~1070-1100)
signs: S°p°(620-700) orho(780-880, circle joined to p) H(920) p(950) bp(1000-1100, b-loop joined to p) T(1130) Phi(1180) div(1260) venuscross(1350) Z(1420) bulb(1500, black bulb on bar) Hp(1550-1590) Odot(1640) .1.(1690-1740) | qstem(1810) boxcross(1870) Odotbox(1930) pcross(1970) div(2020) 3(2080) venusring(2130) H(2190) delta(2250) six(2290) | x(2370) H(2420) plus(2480)
glosses: margin "principis Caroli" (for S°p°); "qui"(1000-1060); "continu[o]"(1150-1390); "?ivi?"(1600-1700, illegible); "consili.."(1840-1990); "sub"(2350-2420)
- "sub" = x H plus = s u b  (x=s 2nd instance, H=u 2nd instance, plus/cross=b 2nd instance). SOLID 3/3.
- "qui" = orho H p = q u i (assuming the gloss sits slightly right of its signs) - PROBABLE.
- "continuo" = bp T Phi div venuscross Z bulb Hp? = c o n t i n u o -> T=o, Phi=n (2nd n), div=t, venuscross=i, Z=n, bulb=u; Hp would be o here (conflicts with Hp=i in "servitor"); PROBABLE for first 7 signs.
- "consili.." over qstem boxcross Odotbox pcross div 3 ...: does not fit (div=t) - NOT ALIGNED.

### 23-5-4_11 row y~905, extra
- "quod"(gloss 1850-1950) over orho(1830) H(1920) T(1960) Z(2020) = q u o d -> orho = q (2nd), Z = d?? (Z = n in "continuo") - PROBABLE, Z polyphonic or misaligned.

### 23-5-4_11 row y~1240 (transcribed, not aligned)
signs: aloop+p(650-690) plus-bar(720) lo(800) theta?(870, circle with cross inside) ofo(940-990) .1.(1050-1080) x(1110) T(1160) 9(1200) pcross(1240) rho(1350-1390) venuscross(1410) div(1480) 3(1550) Phi(1620) six(1710) venuscross(1740) x(1810) T(1880) lo(1930) H(1990) div(2060) pcross(2120) Phi(2280) plusdot(2340) orho(2380) vl(2440-2480) div(2560)
glosses above it (y~1185): "col.."(830-930), "sollicitandi"?(1300-1450), "solicito.."(1990-2100), "premiare"?(2350-2480). I could not make a letter-by-letter alignment.
- Partial: "x T 9 pcross" then ... ; ".1. x" = e s ; no target sign proven here.

### 23-5-4_07 row y~1450: the gloss over S°p°
- 3.5x crops at two contrast settings (gt_sg4.png, gt_sg4p.png): the gloss runs "duza" (x2050-2170; perhaps Spanish "duquesa"/"duqsa"), then a gap over S°p° (x2150-2250), then "principis" (x2340-2500) over the FOLLOWING cipher letters `v p Lo`. So this S°p° has no gloss of its own.
- Other instances: 23-5-4_11 row y~1150 (margin gloss "principis / Caroli", a struck gloss above it), and 23-5-4_11 y~1950 in a clear Latin line "& S°p° habeat M^tas v^ra omnino illius memoriam" with the interlinear gloss "principis Karoli". => S°p° = principis Caroli (2 instances).

### 23-5-47_04 postscript l.4: the end gloss
- The gloss written past the end of l.4 ("iuniore" in the survey) has the same number of minim strokes as "minore" (i-u-n-i = 6 minims = m-i-n). The last six signs of l.4, `Odot hash Z T ofo 3`, give m i n o r + (3), so the gloss is most likely "minore" (3 = e here). This is a second value for 3 (a in "Bastardi" on the strength of the pencil gloss; e here).

## TALLY (both passes; n = glossed instances)

| sign | value(s) with counts | status |
|---|---|---|
| 7 | a x4 (Bastardi, Archiepiscopi, matrimonium, fugat) | solid |
| 3 | a x1 (Bastardi), e x1 (minore, PS l.4) | polyphonic or one misalignment; unresolved |
| bbar | d x2 (Bastardi, fidelissimus), a x1 (PS l.3 "matrim") | d by count; the a case is probably a different shape or a slip |
| plus / cross | b x2 (Bastardi, sub) | solid |
| x | s x4 (Bastardi, Regis, servitor, sub) | solid |
| div | t x5 (Bastardi, matrimonium, fugat, servitor, continuo) | solid |
| delta | r x3 (Bastardi, servitor x2) | solid |
| ofo | r x3 (matrimonium x2, Regis) | solid |
| .1. | e x3 (Regis, servitor, fidelissimus) | solid. NOT a null/separator as assumed in pass 1 |
| 8 | g x2 (fugat, Regis) | solid |
| T | o x3 (matrimonium, servitor, continuo) | solid |
| Phi | n x2 (matrimonium, continuo), u x1 (fugat) | n by count; polyphonic n/u possible (shape of the fugat sign was at the torn edge) |
| Z | n x1 (continuo) | single |
| H | u x3 (vult, qui, sub) | solid |
| Hp / hp | i x2 (servitor, fidelissimus), o x1 (continuo, end) | i by count |
| orho | q x1 (qui) | single |
| six | v x1 (servitor) | single |
| venuscross | i x1 (continuo) | single |
| bulb | u x1 (continuo) | single |
| Odot | m x2 (matrimonium x2: main text, PS l.3) | solid |
| vl | m x3 (matrimonium x2, matrim PS) | solid |
| lo | l x4 (filij, Archiepiscopi, vult, fidelissimus) | solid |
| vroot | f x2 (filij, fidelissimus) | solid |
| pdbl | f x1 (fugat) | single |
| 9 | h x1 (Archiepiscopi, pencil) | single |
| pcross | i x3 (Bastardi, Regis, matrim PS), j x1 (filij) | solid |
| qstem, hash, rho, qhook, Drev, venusdot | i x1-2 each | homophones of i |
| STRUCK (`x c + o` crossed through, with a short group before it) | Maiestas x4 (47_04 main "Ma"; PS l.1 "S. Ma."; 23-5-4_11 y~1005 "Ma~"; 23-5-4_11 y~1790 "Ma.." ) | solid name sign; the case/possessive sits in the short group before it (`HT`, `vl venusdot Odot`, `venus H O`) |
| S°p° | principis Caroli x2 | solid name sign |

Signs in the target lines with NO glossed instance after pass 2: dcross, theta, Zcross, phicross, W, aloop, vtick, deltabar, oo, xhash, bb. Target that each gets 2 instances: NOT met.

---------------------------------------------------------------------------------------------------
# THIRD PASS (2026-10-27)

## New transcriptions
- 23-5-4_12 row y~1135: `O p? (480-520) D?(570) Qcross(620) | Z(760) T(800) Phi(850) 7(920) d(980) .1.(1020) p(1060) | delta six p 3(1160-1260) div(1320) H(1420) ofo(1480) | b?(1580) plus o p(1650-1760) bp+(1810) theta(1890, circle with + inside) Hp(1960) | p(2100) bb(2150) p+(2200) plus(2240) venus(2300) 6 .1. vl(2390-2510)`
  glosses: "mihi"(500-600), "?ie"(760-850), "aperiat id"(1240-1530), "quod"(1730-1800), "propter"(1950-2050), "suggest[ionem]"(2180-2320).
  - "aperiat" over delta six p 3 = H ofo ...: does not align (delta = r, six = v). NOT ALIGNED.
  - "propter" over theta Hp ... p bb: no letter-by-letter fit. NOT ALIGNED. theta is under or near "quod"/"propter", but its letter cannot be fixed.
- 23-5-4_12 row y~1240: `x(500) ap(560) ofo(620-690) venus(730) d(790) p(830) H(870) | venuscross(1030) T(1090) ofo(1140) 9(1170) 7(1210) div(1290) boxcross(1400-1450) 66(1500-1560) p(1580) | x(1680) H(1740) T(1770) 9(1830) lo(1890) 7(1950) 66(2050-2100) .1. | qH(2250) ofo(2310) ofo(2370) 9(2420) d(2470)`
  glosses: margin "habet"(300-400); "principi"(640-760); "Clare"(1950-2050); "regno"(2190-2260); "cum"(1300-1380 under the row?); "suo"(1630-1700).
  - "suo" over x H T = s u o (x = s, H = u, T = o: all known values). SOLID control (3/3).
  - "Clare" over lo 7 66 .1.? = l a ? e; the C is missing. PARTIAL.
- 23-5-4_12 row y~1340: `H P b T(470-560) Odot(620) .1.(660) ;(690) gamma-8(790) T(860) Z(980) plus-bar(1050) div-bar(1120) Hp(1200) 8(1280) ofo-like(1350) 7(1430) div(1480) phi(1640) vl(1700) | bb(1820) ap(1900) H(1970) O(2030) Z(2160) pcross(2200) W(2270-2300) bulb(2330) x(2400) 7d(2460-2500)`
  glosses: "magno"(630-720), "salutem"?(1180-1260, read "J S?ir"), "?ra"(1400-1480), "cum"(2000-2050), "aperuit"?(2200-2320).
  - W occurs here at x2270-2300 under the gloss "...uit" area, but the gloss could not be aligned letter by letter.
- 23-5-4_10 row y~2950: `phi .1. ap(1380-1480) div(1560) 7(1600) O(1650) Hp(1700) Z(1760) | x(1830) a p(1880-1920) | ofo p plus 3(2080-2230) vtick W? (2250-2320) qstem .1. 66 (2360-2470)`; glosses "?er"(1400), "tanti"(1700), "Sudbam"(1950), "per"(2300).
  - "tanti" over div 7 O Hp Z = t a ? ? ? : div = t, 7 = a. Then O, Hp, Z should be n, t, i, which does not agree with Hp = i and Z = n. PARTIAL (2/5).
- 23-5-4_10 row y~3040: `p x div T p q H ofo x box66 .1. p | vtick H lo dcross Z a | p H .1. x q ofo p plus Hp 66 .1.`; glosses "cursore"(margin), "multi"(1150-1300), "qui"(1880-1920).
  - The signs `vtick H lo dcross Z` (x1480-1720) give ? u l ? ?, which fits "multi" (m u l t i) with vtick = m, dcross = t, Z = i. But the gloss "multi" stands about 300 px to the LEFT of these signs, over `x box66`. CANDIDATE ONLY: the gloss is not above the signs. The Latin model ranks l first for "mu?ti" (-3.0 vs -7.3 for the next), which supports reading the known lo = l, not the unknown signs.

## 23-5-47_04 postscript l.4 end, CORRECTED
Re-read non-deskewed at 1.5x (gt_e4.png). The last signs are `Odot(1000) Zcross(1060-1100) pcross(1170) T(1240) ofo(1300) 3(1380) xhash(1450)`, and the gloss "iuniore"/"minore" is written above x1420-1600.
The pass-2 reading `Odot hash Z T ofo 3` = "minore" is WITHDRAWN: the 3rd sign is pcross (i x3), not Z.
Values: m [Zcross] i o r e. The Latin model ranks a first for "m?iore" (maiore -3.2; next b -5.4).
So the word is "maiore" with Zcross = a, which is a CANDIDATE: it rests on the model, not on a gloss. The contemporary gloss, whatever its exact letters, ends in "-iore", which confirms i o r e (pcross, T, ofo, 3 = e).

## TALLY changes (pass 3)
| sign | change |
|---|---|
| 3 | e x1 (PS l.4 -iore, confirmed by the gloss ending), a x1 (Bastardi, pencil). Still split 1:1, so polyphonic a/e or one misreading |
| x | s x5 (+ suo) |
| H | u x4 (+ suo) |
| T | o x4 (+ suo) |
| pcross | i x4 (+ PS l.4 -iore) |
| Zcross | a? candidate x1 (PS l.4 m?iore, model only). No glossed instance |
| vtick, dcross | m?, t? candidates x1 each (23-5-4_10 "multi", gloss displaced). No glossed instance above the sign |
| W, theta | occur on glossed rows (23-5-4_12 y~1135 and y~1340; 23-5-4_10 y~2950) but the glosses there could not be aligned letter by letter. No value |
| Z | n x1 (continuo), d x1 (quod), i? x1 (multi candidate). Unresolved, probably polyphonic or misread |
| pdbl (f from "fugat") | no second instance found under a gloss |

## Stopping statement
- In the rows checked (23-5-4_04 l.3; 23-5-4_07 rows y~1250-1500; 23-5-4_10 rows y~2950-3040; 23-5-4_11 rows y~905-1240; 23-5-4_12 rows y~1135-1340; 23-5-47_04 main rows y~830-960 and postscript), these signs have NO instance that can be aligned under a gloss: phicross, aloop, deltabar, oo, xhash, bb.
- W and theta occur under glosses that I could not align.
- Zcross, vtick and dcross have only candidate values.
- NOT checked: 23-5-4_07 rows y~850-1000; 23-5-4_11 rows y~1320-1840; 23-5-4_12 rows y~1445-1550; 23-5-47_04 main rows y~1040-2600. So the stopping condition ("the sign never occurs under a gloss in either letter") is NOT established. It holds only for the rows listed.
