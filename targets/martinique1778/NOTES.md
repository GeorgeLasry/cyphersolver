# Bouillé to the minister, Martinique, 17 September 1778 (ANOM C8 A 77 f. 88, no. 238) - catalogue 1202, with the 1203 letters surveyed

Status: in progress (read in part: key for Bouillé's code recovered from interlinear decipherments of 1779 letters; f. 88 is a monthly troop return, 68.0% of tokens valued, 58.0% inside dictionary words by a strict proxy, far below the 95% bar; 28 Oct 2026)

Catalogue 1202 (this letter; f. 101 of 5 Dec 1778 surveyed, not transcribed) and 1203 (C8 A 78-81; surveyed, three interlinear letters partly paired).
Written in the checkout cyph-merge, not committed.

## Document

- ANOM COL C8 A 77 f. 88 (image FRANOM23_C8A_077_0141, FranceArchives component 1bd8971212209a5c804b009c94910f186d12a09f,
  ark:/61561/zn401ysswzzd), Bouillé (governor general of the Windward Islands) to the Navy minister, no. 238, "à la
  Martinique le 17 7bre 1778", "Dup.ta". One page: clear "J'ai l'honneur de vous envoier", 12 lines of numeric
  groups, "Je suis avec respect, Monseigneur, Votre très humble et très obéissant serviteur, Bouillé". No interlinear
  decipherment; calendar: "Lettre chiffrée non décryptée".
- **Transcribed digit by digit from the image** (`transcription.txt`, 640x360 crops): **181 groups, 109 distinct,
  values 1-845** (`_check_profile.py --measure`), full-stop separators; a "+" above 451 and an "x" after 37 (line 4) are
  marks, not digits. In the hand a 4 looks like "h", a 5 like "S".
- Same day, no. 237 (f. 87, image 0140): clear, asks the inspection of the Dominica hospitals for a physician at Saint-Pierre.

## What f. 88 is (from the extended key)

A monthly **return of the troops** ("état de la situation des troupes ... au 1er de ce mois"): with the key, line 1 reads
"l'ét[at] de la situation des troupes", line 2 "au 1er de ce mois ...", later "garnison" (268, three times), "la Martinique"
(267), "hommes", "cents", "hôpital" (ho pi ta + [103]), "la Guadeloupe", "troupes", "hommes ef-fe-c-ti-f-s" (effectifs).
The same monthly return exists in the volume: f. 101 (5 Dec 1778, no. 259) opens `208 250 837 361 57 147 1 250 287 361 694
381 303 361 267 636 104 361 270 309 815` = "[J'ai] l'honneur de vous envoyer l'état de la situation des troupes de la Martinique au 1er de ce mois",
and C8 A 78 f. 31 (8 March 1779, no. 281) is the same kind of return with interlinear decipherment.

## System

- Numeric nomenclator, groups 1-845 (the 1761 code C8 A 64 f. 1 stops at 696, the 1765 d'Ennery form at 800). Letters, syllables,
  and whole words, with articles inside place names (428 = la Guadeloupe, 267 = la Martinique). Homophones exist (s = 817/635,
  fe = 658/538?, es/ez = 185, se/sé = 305); numerals are spelled in syllables and letters (si-x, qua-tre, cent-s, vi-n-g-t).
  A semicolon and a comma are written in the cipher line.
- Tests of the sibling keys (`test_keys.py`): the **mercier1761 key does not fit** (28 groups exceed 696; 39 of 181 tokens valued, salad)
  and neither does the **1765 d'Ennery form** (17 groups exceed 800; nonsense). The Bouillé code is a third code.

## Key sources: interlinear decipherments in the same series

Survey of the letters on the catalogue list (first images viewed 28 Oct 2026; image numbers from the manifests):

| letter | images | what is there |
|---|---|---|
| C8 A 78 f. 123 (no. 363, 11 Oct 1779) | 0197 | **interlinear**, fully paired (104 groups, `pairs1779_f123.txt`) |
| C8 A 78 f. 31 (no. 281, 8 Mar 1779) | 0046-0047 | **interlinear** (troop return; heavy ink bleed-through); about 60 groups paired |
| C8 A 78 f. 3 (no. 173, 6 May 1779) | 0004-0006 | **interlinear**, clean hand; lines 1-2 paired |
| C8 A 78 f. 5 (no. 175, 8 Jun 1779) | 0007 | **interlinear** (opens "Nous avons l'honneur de vous envoyer les états de ..."); not transcribed |
| C8 A 78 f. 144 (no. 372, 23 Nov 1779) | 0233-0246 | **interlinear** on image 0233 (opens "de la compagnie de M. d'Est..."); not transcribed |
| C8 A 78 f. 1 (Grasse du Bar) | 0001-0003 | cipher only, no interlinear on 0001-0002; a note says the original was deciphered. (Image 0075, dated 24 mars 1779, is another long cipher letter, no interlinear) |
| C8 A 79 f. 19 (no. 23, 14 Nov 1780) | 0029-0030 | cipher only, opens "Nous avons l'honneur de vous adresser" `250 287 381 744 ...` (état des ...), no interlinear |
| C8 A 79 f. 70 (no. 415, 24 May 1780) | 0107 | cipher only, "J'ai l'honneur de vous envoyer" `250 287 163 586 361 ...` (état des garnisons) |
| C8 A 77 f. 101 (no. 259, 5 Dec 1778) | 0162-0164 | cipher only on 0162 (troop return, parallels f. 88); image 0163 is a **table** of cipher groups in two columns (enclosure) |
| C8 A 79 f. 4, f. 24; C8 A 81 f. 97, f. 104 | first images | clear letters (cipher, if any, later in the letter; not read) |
| C8 A 81 f. 114 (no. 12, 24 Nov 1782) | 0195-0203 | clear opening; cipher lines begin below on 0195; not read |

- `pairs1779_f123.txt` (all of f. 123: "J'ai reçu la lettre ... fortifications de la Guadeloupe ... la moitié des troupes ... à découvert") and
  `pairs1779_f3_f31.txt` (f. 3 lines 1-2: "nous avons l'honneur de vous rendre compte de l'état de la colonie dont la situation est des plus critiques"; f. 31:
  "l'état de la situation des troupes au 1er mars, par lequel vous jugerez que la garnison de la Martinique n'est composée que de quatre ... Des six cents
  quarante cinq hommes de recrue ... trois cent vingt cinq à l'hôpital ... ce qui provient de la marine ..."). Alignment is by label position and by sense (labels sit up-left of their group).
- `apply_key.py` merges them into **`key_bouille.tsv`: 123 groups with provenance per value** and prints conflicts:
  67 qua/vous, 185 es/ez, 305 se/sé/e, 503 è/par (f. 123 vs f. 31; probably a misalignment in one of them), 718 a/à.
  New values include 694 situation, 267 la Martinique, 636 au, 104 1er, 116 ma + 325 rs (mars), 78 ho + 508 pi + 417 ta (hôpital), 453 cents, 91 x, 709 si, 37 hommes,
  558 recrue, 268 garnison, 682 dont, 815 is, 250 l', 287 état, 837 honneur, 810 compte, 488 nous, 448 plus, 353 colonie.
- **Same code, shown statistically** (`shared_ngrams.py`, session 1): 10 shared adjacent pairs and 2 triples against 1.55 and 0.01 expected (p < 0.001). Session 2 adds the identical openings
  of f. 3/f. 31 (250 287 361 587 694 = l'état de la situation) and f. 101/f. 88.
- Access: curl gets 403 from the ANOM image server; the browser pane loads the IIP URL (the manifest gives the path). Drawing a crop of the loaded image into a canvas in an 800x450 viewport gives legible 1:1 or 0.8-scale crops.
  The canvas only has to be displayed, so images can be drawn from any origin. The pane is shared: use your own tab and pass its tabId.

## Reading of f. 88 with the extended key (`apply_key.py`, `measure_sense.py`)

- **Valued: 123 of 181 tokens (68.0%), 61 of 109 distinct groups. Strict sense proxy: 105 of 181 tokens (58.0%)** (`measure_sense.py`: valued stretches are cut at unvalued groups and must
  segment into fr-gutenberg words plus a declared list; it accepts any word-shaped string, so it overstates). Not the 95% read bar.
- Decoded lines (`[n]` = open): 1 "l' ét [5=at] de la situation des troupes"; 2 "au 1er de ce mo-is [191 5 398 339 110 817] aux d' [531] plus d'"; 5 "... dre [403 143 160] isle [494] es"; 6 "... met tre un garnison [481] de [845] r [195]";
  7 "r la Martinique [507] il né re s te en de [412] is [210] le s ho"; 8 "pi ta [103] x ét la garnison de [138] que [516] is [454] [516] is cents"; 9 "hommes ef [538=fe] c ti [614=f] s [88] vous en ver [509] [260] l' état de la";
  10 "situation de la garnison d' é Ce t te [739] [195] er [505] isle [286] est [645]"; 12 "la Guadeloupe [819] en troupes re [26] es ...". The text reads as a garrison return; the numbers of men are mostly open.
- **Tentative values** (`tentative.tsv`, applied only with `--tentative`, not in the key): 5 = at, 538 = fe, 614 = f ("hommes ef-fe-c-ti-f-s" = effectifs; f. 123 has 594 658 345 754 for the same syllables, so 538 may be a misread of 658 in f. 88: check the image). With them 128 of 181 (70.7%) are valued.
- Not claimed: "j'attends" for line 2 (191 = J', 5 = at, 398 = te, 339 = n, 110 = d, 817 = s fits the letters but not the context); "il ne reste en de..." on line 7; 103 = ux.

## Ciphertext-only attack: not run

The mercier1761 control (same shape, ~800 entries, 818 tokens: 5-9% correct, the truth outscored) shows the objective cannot separate the true text at this size; with 181 tokens it is worse. The interlinear
keys make it unnecessary.

## Remaining gaps

- 48 of 109 distinct groups (58 of 181 tokens) of f. 88 are unvalued (among them 667, 665, 495, 710, 491, 279, 126, 568, 479, 545, 402, 240, 809, 321, 146, 350, 403, 143, 160, 494, 619, 443, 481, 845, 507, 412, 210, 138, 516, 454, 531, 739, 505, 286, 645, 26, 819, 320, 285, 622) - blocker: not-attempted; interlinear decipherments of C8 A 78 f. 3 (3 images), f. 5, f. 31 (second image and most of the first) and f. 144 are not yet paired and carry the same code
- Conflicting values 67, 185, 305, 503, 718 and the uncertain 538/658 - blocker: not-attempted; re-check the f. 31 and f. 88 images
- f. 101 (5 Dec 1778) and its table enclosure (image 0163), cipher-only letters C8 A 78 f. 1 and C8 A 79 f. 19, f. 70 and the ciphered passages of C8 A 81 f. 114 not transcribed - blocker: not-attempted; same code, to be read once the key is extended
- The minister's ciphered minutes (C8 A 77 ff. 31, 43) and MAR/G/178 (colonial Navy keys 1741-1776) - blocker: needs-physical-access (MAR/G/178); minutes not opened

## Escalation

- [x] siblings: f. 87 (clear), f. 112 and the C8 A 78-81 letters surveyed; interlinear decipherments found on f. 123, f. 31, f. 3, f. 5, f. 144; f. 101 is the same kind of return
- [x] clear-pages: f. 87 clear, unrelated; the clear letters of C8 A 79 f. 4, f. 24 and C8 A 81 are different dispatches
- [x] known-keys: mercier1761 key and 1765 d'Ennery form tested, both ruled out
- [ ] print: not searched (the 28 Oct catalogue sweep found nothing printed)
- [x] key-rebuild: key_bouille.tsv (123 values, provenance per value) from the interlinear letters; no annealing (control fails at this size)
- [ ] retry: the extended key is applied once; f. 3, f. 31 (rest), f. 5, f. 144 still to pair, then re-measure

## Next steps

1. Pair f. 3 (images 0004-0006, clean hand), the rest of f. 31 (0046-0047), f. 5 (0007) and f. 144 (0233-): each adds 100-300 pairs of the same code; many open groups of f. 88 (numbers of men, "présents", "morts", regiment names) will appear.
2. Re-run `apply_key.py` and `measure_sense.py`; fill short gaps by context with `lang/` French models only with a crib, marked tentative.
3. Then read f. 101 and its table enclosure and the cipher-only letters (C8 A 78 f. 1; C8 A 79 f. 19, f. 70). The catalogue 1202/1203 entries should note that C8 A 78 f. 3, f. 5, f. 31, f. 123, f. 144 carry interlinear decipherments.

## Prior art

Catalogue sweep 28 Oct 2026: nothing published, not on DECODE. Not re-searched here.
