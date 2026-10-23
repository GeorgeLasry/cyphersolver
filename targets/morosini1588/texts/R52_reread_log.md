# Re-reading log, R52 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R52_decryption.txt` (DECODE D1716 under Meister no. 40) gave the topics
(Angers, Brittany, Mercœur, Mayenne, Épernon, Navarre) with garbles in most lines; `_check_reading.py` 0.517.

## 1. Is there a text already?

- Clear heading on 473r as transcribed by DECODE: "Tours a dì 6 Aprile 1589".
- DECODE "cleartext" images D1079, D1093, D1098, D1104 (contact sheet): a clear copy of Navarre's letter to the legate
  ("Copia de la lettera del Navarro al Leg.to Apostolico in Francia", ff. 470–471), the covering letter in clear from the
  abbey of Marmoutier (f. 472, April 1589) and its address leaf with the docket. None is a decipherment of the cipher.
  No interlinear glosses.
- Rome's decipherments (Francia 27) are not imaged; Tempesti (1754) has the Angers affair and the King's Holy Week only
  in outline. Not used for words.

## 2. Hand re-parsing (R52_corrections.tsv)

About one word in eight re-parsed, nearly all carried by the transcribed figures. The decoder's vocabulary lacked most
of the proper names, which the figures carry exactly: Brisac, Bodafino (Bois-Dauphin), d'Umone (Aumont), Monpensiero,
Mercurio, Sci[a]rtres, Abeuile, Amiens, Balagni, Longauila, Sciampagna, Tenteuile (Dinteville), Alfonso Corso, Auernia,
Bogiansi (Beaugency), San Polo, Gian (Gien), Fontanableo, Sansera, Montegni, Saumur, La Uardino, l'abate dal Bene,
Molano, "thesoriero del Esparmi", Lenoncourt, San Francesco di Paula, San Martino. Also: "con l'improuisa entrata",
"i borghesi restorno … sbigotiti et opresi", "fa mercantie de trauagli d'altri", "profondisimo sono", "segnate le
scrofole", "richisimam. adobato", "io poso dire" (DECODE decode "ristrinse con dire").
- Numbers in plain figures between null 8s: 100, 1200 ("mile 200"), 200 milia, 400, 60, 150, 4000, 300, 600, 3000, 4,
  300 milia, 60 milia.
- Spurious or misplaced dots: 816 (8 + 16), 265 (= 165, "come quello che"); 216 auiso written without its dot.
- Image check (one crop, 474v l. 2): the uncertain figures read 7 0 5 0 0 2 5 8, then Monlione (Mauléon?).

## 3. Alignment (reread_b00_align.py)

`TOTAL R52: 1331 words, 4 supplied, 8 partly` (after respelling double consonants as the figures give them). The four
"supplied" are code forms the aligner does not expand (guerre 143, catolica 226, "sue" before the code 137 abbatie);
"nobiltà" runs over the page turn 473v/474r.

## Result

Before: 0.517 clean-sentence share (`R52_decryption.txt`). After: 0.645 on the "## Reading" body (1,358 words). By hand:
9 unread stretches ([…]), 3 partly carried words and 15 supplied letters in about 1,330 words; every sentence carried.
Grade A-/B: the sentences hold throughout with few holes; a handful of figure+context corrections.

## Still open, and why

- 473r l. 3 (opening "5 4 2 7 9"), the two number words before "tanta milia scudi" (473r ll. 12, 28), 473r ll. 13, 15,
  34; 473v l. 2; 474v ll. 2 ("70 5 00 25" before Monlione), 9, 14, 33 (closing).
  Not re-checked on the image beyond 474v l. 2. No outside blocker otherwise.
- Rome's decipherment in Francia 27 would settle them (physical access).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`; the pages are clean), cancellation strokes looked for (none), the figures parsed
(`r2p_parseall.py`). Nothing could be filled: every remaining hole is as DECODE transcribes it.
Left, with blockers:
- 473r l. 3 "[…] quali esendosi": "5 4 2 7 9" (best parse "slto"). Blocker: no-key-material.
- 473r l. 8 "scrise al mar[e]sciale d Umone": "2 0 2 1 1 3 3 6 1 7 2 1 5 0 5" (best parse "amxuutiale"). Blocker: no-key-material.
- 473r l. 12 "fata di […] tanta milia": "9". Blocker: too-short.
- 473r l. 13 "quella carica […] che [t]": "6". Blocker: too-short.
- 473r l. 13 "[…] che [t] enese a": "(none)". Blocker: nothing written there; no-key-material.
- 473r l. 15 "Onde il mar[e]sciale che si": "2 0 2 1 0 0 3 4 1 7 2 1 5 0 5" (best parse "marsciarel"). Blocker: no-key-material.
- 473r l. 15 "si trouaua […] di [?Mans]": "0 3 5 1 7 1 1 9 1 5 9 1 0 0 1 0 7" (best parse "neicontorni"). Blocker: no-key-material.
- 473r l. 15 "[…] di [?Mans] al auiso": "8 3 7 2 0 2 1 0 1 4 5 8" (best parse "imans"). Blocker: no-key-material.
- 473r l. 18 "che i borgh[es]i cominciauano a": "8 4 2 9 1 0 0 4 0 1 4 1 7 8" (best parse "borghi"). Blocker: no-key-material.
- 473r l. 21-22 "entrata del mar[e]sciale i borghesi": "8 2 0 2 1 0 0 3 4 1 7 2 1 | 5 0 5" (best parse "mnfsiale"). Blocker: no-key-material.
- 473r l. 28 "colpi di […] tanta milia": "9 0 3 5 7 9" (best parse "ofsfo"). Blocker: no-key-material.
- 473r l. 34 "l armi […] non posino": "7 2 8". Blocker: too-short.
- 473v l. 2 "in Bretagna [?] unito col": "8 7". Blocker: no-key-material.
- 473v l. 4 "di nobili [che] posa combatere": "8". Blocker: too-short.
- 473v l. 11 "uicino a Sci[a]rtres da una": "8 4 5 2 5 1 7 0 0 1 5 0 0 3 5 4 5 8" (best parse "ctpntres"). Blocker: no-key-material.
- 474r l. 16 "aiuti forestieri s[i]a uicini per": "4 2 1 2" (best parse "sa"). Blocker: no-key-material.
- 474v l. 2 "è uoltato […] Monlione che": "8 7 6 2 5 0 0 2 5 8 9" (best parse "tcrc"). Blocker: no-key-material.
- 474v l. 9 "stato permeso […] tuti questi": "(none)". Blocker: nothing written there; no-key-material.
- 474v l. 14 "et già [?otuagenario] ma prelato": "9 1 5 9 1 4 0 3 5 0 1 2 1 0 0 1 7 9 1 8" (best parse "otogenario"). Blocker: no-key-material.
- 474v l. 28 "di Paula [et] a San": "8". Blocker: too-short.
- 474v l. 33 "di questa […]": "8 5 5 4 7 2 7 9 6 173^. 0 0 9 2 1 2 0 0 5 111^. 4 7 5 2 1 7 1" (best parse "siaiot[inghilterra]roare[il"). Blocker: no-key-material.
Result: 0 holes filled; 21 left, each with its blocker.
