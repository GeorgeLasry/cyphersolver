# The "Devil's Handwriting": Ludovico Spoletano's conjuration, Teseo Ambrogio, *Introductio in Chaldaicam linguam* (Pavia 1539), f. 212v

Status: in progress. Not read. Second session (16 Oct 2026): a calibrated homophonic solver that solves 12/12 matched
153-letter, 31-sign controls in Latin and Italian finds nothing in the Devil's text. Schmeh's Top 25 no. 12.

## Target

- Teseo Ambrogio degli Albonesi, *Introductio in Chaldaicam linguam, Syriacam, atque Armenicam, & decem alias
  linguas* (Pavia: Giovanni Maria Simonetta, 1539), f. 212v (p. 426/427 in the Cipher Mysteries scans). A woodcut
  of seven lines of signs printed over the page's Latin text, presented as the Devil's written answer to
  Ludovico Spoletano's conjuration.
- The question (Italian, printed with the conjuration): "sel Cavaliero Marchantonio figliolo de ricca donna da
  Piacenza ha ritrovati tutti li dinari che laso Antonio Maria, & se no in qual loco sono." Ambrogio says the pen
  rose and wrote by itself, and that he "did not care to know" what the characters meant.
- Image: `margin.png`, supplied by the user on 16 Oct 2026 (first identified here as an unprovenanced marginal
  note). The identification and the background came from a PDF by David Scheers sent to the user the same day
  ("Remarks devil's handwriting": Wood 1663, Yeowell, Götze 1743, Cipher Mysteries 2013, Schmeh 2013, and
  Agostino Amadi's *Letere diaboliche*, a 31-sign "diabolic alphabet" named after demons that resembles these
  signs).
- Prior work: no published decipherment (Cipher Mysteries, Schmeh, search of 16 Oct 2026). Scheers tried
  Latin/Italian cribs (Amon, dinari, Antonio Maria, Marchantonio, tesoro) without a reading. Popular sources compare
  the signs to Amharic.

## Transcriptions

- `transcription.txt`: this project's, 174 signs in about 40 classes (dots and loops included), made from the
  image before the target was identified. Class codes are listed in the profile history (E = Ǝ, A = ꭗ, Y = U on a
  stem, H/M/S = arch variants, Q = barred sign ...).
- `transcription_scheers.txt`: David Scheers's transcript (the first of his versions in the PDF), 153 signs,
  31 symbols (measured). He notes that the woodcut drops and adds strokes, so sign identity is uncertain.

## Script identification (16 Oct 2026)

Reference charts were rendered from Noto fonts and compared sign by sign: Samaritan, Phoenician, Ethiopic,
Glagolitic, Tibetan, Old Italic, Old Hungarian, Georgian, Armenian, Hangul, Japanese kana (the image rotated
90°), Old Permic, Brahmi, Batak, Rejang, Hanunó'o, Canadian syllabics, Tifinagh. Partial look-alikes exist in
several (Ethiopic ሰ ሐ ተ ገ ለ አ and numeral bars; Tifinagh ⴺ ⵄ ⵖ ⵉ ⵎ ⵜ; Brahmi ka, ga, la, ya, e), none consistent.
The rotated reading (90°, 180°) and the mirror reading were checked and give no script. Ambrogio's book prints
about forty alphabets, including Ethiopic and Armenian; the woodcut may be built from such shapes.

## Solver runs and controls

Quadgram annealing, simple substitution (`work/anneal.py`), homophonic with a letter-frequency penalty
(`work/homophonic.py`), and Ethiopic consonant values with free vowels (`work/ethiopic_syllables.py`).
Corpora: CLTK Latin Library (Caesar, Cicero, Sallust), Latin and Italian Bibles, Hebrew Bible (WLC), Amharic,
Croatian and Russian Bibles (GitHub raw).

| test | real | control | verdict |
|---|---|---|---|
| own transcription, simple substitution, Latin / Hebrew / Croatian / Russian / Amharic rows, both directions | −12.1 to −13.5 | shuffles within ±0.3 | no signal |
| Ethiopic visual values + free vowels, Italian / Latin | z = 0.27 / 0.33 vs permuted values | | no signal |
| Scheers transcription, Latin, LTR | −11.59 | 15 shuffles −11.87 to −12.23 (z ≈ 4.5) | beats shuffles |
| same, Italian, LTR | −11.60 | 15 shuffles −11.74 to −12.27 (z ≈ 2.8) | beats shuffles |
| same, against bigram (Markov-1) surrogates of the ciphertext | −11.59 / −11.60 | Latin −11.03 to −11.70; Italian −10.93 to −11.67 | the excess is explained by sign-pair habits |
| calibration: 153 letters of Caesar, plain one-to-one | | solved, −9.0 to −9.7 | method works for monoalphabetic text |
| calibration: same with 6 homophones (25 signs) | | not solved, even at 6 × 200k iterations | method has no power for a homophonic system of this length |

Conclusion so far: the Devil's Handwriting is not a monoalphabetic Latin text under either transcription (a
monoalphabetic Latin text of this length scores near −9.5 and is solved). A homophonic Latin or Italian text of
31 signs cannot be excluded: the solvers used here fail on a matched control. The bigram-surrogate result means
that nothing in the text is yet distinguishable from habitual pseudo-writing.

## Calibrated homophonic solver (second pass, 16 Oct 2026)

`work/hs/hs.c` (and `hsg.c` for any alphabet): simulated annealing over a free sign → letter key, scored with
interpolated 5-gram conditional log-probabilities plus a letter-frequency chi-square penalty (λ 0.5), 24 restarts ×
3 M moves. Models: Latin (Vulgate + CLTK), Italian (Bible + Pallotto 1629 nunciature letters), and Hebrew (WLC), Spanish
(Quijote), French (Guizot), German, Greek, Arabic, Amharic consonant rows; also Italian and Latin with vowels dropped
or merged (Judeo-Italian style).

Controls (`work/hs/mkctl.py`): 153 letters of held-out text, 31 signs, homophones given to the commonest letters.

| controls, 24 restarts | solved | score of solved key |
|---|---|---|
| Latin (Caesar, Sallust), 6 | 6/6 at 99–100% of letters | −1.62 to −1.86 |
| Italian (held-out Bible), 6 | 6/6 at 88–100% | −1.64 to −2.12 |
| Italian (archival lists, asl1883), 6 | 2–3/6 (model mismatch: the true key scores lower than the false one) | |

Devil's text, best of 24 restarts: Latin −2.37 (LTR) / −2.50 (RTL); Italian −2.44 / −2.45 (Scheers transcription);
own transcription −2.42 to −2.80. Shuffled copies score −2.42 to −2.52. Hebrew, Spanish, French, German, Greek,
Arabic, Amharic rows and the vowel-dropped/merged variants: all within the shuffle range (`work/hs` results in the
profile steps). **The text is not a simple or homophonic substitution of Latin or Italian under either
transcription**; the other languages are excluded with less calibration.

Structural note: both transcriptions independently read a run of three identical signs in line 2 (Scheers ZZZ, here
the arch run H M H / S S S), which a letter substitution of Latin or Italian would turn into a tripled letter.

Left open: a syllabic system (Ethiopic-style signs with vowel marks, which neither transcription separates), a code or
nomenclator, or pseudo-writing with no linguistic content (the most economical reading of all the tests, and
consistent with Ambrogio's "I did not care to know").

## Crib attack (16 Oct 2026)

`work/hs/hscrib.c`, `cribrun.py`: each crib fixed at every offset (both transcriptions, both directions), placements
inconsistent with the sign classes rejected, the rest annealed with the calibrated solver (3 restarts × 400k). Cribs
from the question: antoniomaria, marchantonio, dinari, denari, danari, piacenza, caualiero, ritrouati, trouati,
qualloco, tesoro, figliolo; Latin pecunia, thesaurus, antoniusmaria, marcusantonius, placentia. 15,970 placements,
2,449 consistent. Best −2.50 (danari, Scheers, offset 54), below the uncribbed best and far from the solved-control
range (−1.6 to −2.1); top 25 in `work/hs/crib_results_top25.txt`. On a control the true crib placement recovers the
whole text and every wrong offset is rejected. None of these words is in the text under a letter substitution.

## Machine-assisted transcription (20 Oct 2026)

`work/machine/seg2.py` segments the image into 183 glyphs (detached dots kept as marks with their position);
`clus.py` clusters the base shapes (HOG features, Ward, k = 35; silhouette ≈ 0.07, weak). The clusters recover the
main families (Ǝ 17+4+2, arches, forks, ꭗ, barred signs, `work/machine/clusters.png`) but mix the round signs. Every
glyph was then labelled by eye against the clusters: `transcription_v3.txt`, 161 signs, 38 classes, which agrees
closely with `transcription.txt`. Calibrated homophonic solver on v3: Italian −2.31 vs shuffles −2.36/−2.37, Latin
−2.38 vs −2.34/−2.36. No signal; the earlier transcriptions are not hiding a misreading that the solver would catch.

## Syllabic (abugida) test (20 Oct 2026)

`work/syllabic/`: each sign = base family + mark class (`dv.txt`, `dv.fm`: 22 families, 7 mark classes: plain,
stub, dot, middle leg, flat top, crossbar, hook; dots from the automatic segmentation). Two models: `syl.c` (vowel
free per sign) overfits and fails on its controls even with the true families, so it has no power; `syl2.c`
(Ethiopic-style: one consonant per family, one vowel per mark class, ~29 parameters) solves 3/4 Italian syllabary
controls of 161 signs (the fourth is a search failure; the true key scores higher). On the Devil's text it gives
Italian −2.55 / −2.55 (LTR/RTL), Latin −2.54 / −2.51, against shuffles −2.49 to −2.54, and no words. This
decomposition is one hypothesis among several; others (marks mapped differently across families) remain untested.

## Amadi's diabolic alphabet (21 Oct 2026)

David Scheers's redrawing (sent privately, not to be distributed; not in the repository) of Agostino Amadi's *Letere diaboliche* (Venice, c. 1588), 31 signs,
each named after a demon (Astaroth, Minos, Belzebub, Lybicon, Sathan, Barion, Stix, Pluton, Zael, Charon, Cerber,
Acheron, Let, Demon, Cocito, Aletho, Eunce, Lucifer, Megera, Phlegeton, Raziel, Fython, Nayn, Uriel, Oziel, Gax,
Sachao, Radamastra, Xac, Dis, Thesiphon). The signs are the woodcut's own: Acheron = Ǝ, Lybicon / Zael / Lucifer =
the three arch variants (stub, stub + dot, stub + long middle), Aletho and Nayn = the two forks, Astaroth = the fork
on a cross, Minos = ⊏, Pluton = −6, Charon = ≻, Cerber = F over ᗰ, Megera = ξ, Phlegeton = the barred sign, Oziel =
≈, Sachao = e, Xac = the hooked cross ᆿ, Radamastra = the plain arch, **Demon = the loop with a tail**, Cocito =
the stacked sign. Amadi therefore read the woodcut as an alphabet of about 31 signs, the size of Scheers's
transcription.

The names as a key (`work/amadi_acrophonic.py`, first letter of each name; v3 transcription): `?agu??b?rrbaab?agssagggcgbaa
/ rzccaaccammamlmzlzpaabaculzbm / …`, no words; Italian −4.49 against 2,000 random reassignments −4.73 ± 0.18
(z = 1.35), Latin z = 0.63; second letters no better. The demon names are labels, not sound values.

Amadi's "Aetiopice" (f. 180r) and Armenian (ff. 178v–179r) tables, also sent privately by Scheers (21 Oct 2026, not
in the repository): the Ethiopian is a cursive Greek-style alphabet in Greek order (names Alfa, beda, gama, delda …
Zso … Theda), sharing only generic shapes (E, 3, 8, X, λ, Π, Ψ, +) with the woodcut; the Armenian is genuine
Armenian, a few arches like ո ռ տ մ. Neither has the woodcut's distinctive signs (Ǝ with long bar, the stubbed arch
variants, fork on a stem, Γ on a stem, barred signs, ≻, ξ). Only Amadi's diabolic table, itself a copy of the
woodcut, matches.

## Remaining gaps

- Reading: none. Blocker: illegible (the woodcut's sign identities are uncertain; two transcriptions disagree on
  the class inventory).
- A homophonic solver that solves a 150-letter, 31-sign Latin control: not available here.
- Amadi's table: received 21 Oct 2026 (Scheers), tested, no key. Ambrogio's own alphabets in the same book: not seen
  (archive.org and Google Books blocked in this environment). Blocker: needs the scans.

## Escalation

- Get the Ambrogio scan (archive.org bub_gb_yUkKq_QnrnwC, n428) and his alphabet plates; compare each sign with the
  Ethiopic, Armenian and "magical" alphabets he prints; get Amadi's table from Scheers's book.
- Re-transcribe from the sharper scan, reconciling with Scheers; then a stronger homophonic solver (Lasry-style,
  with restarts and n-gram 5) calibrated on matched controls.
