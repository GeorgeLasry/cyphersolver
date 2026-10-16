# The "Devil's Handwriting": Ludovico Spoletano's conjuration, Teseo Ambrogio, *Introductio in Chaldaicam linguam* (Pavia 1539), f. 212v

Status: in progress. Not read; no method tested here reaches a reading. Schmeh's Top 25 no. 12.

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

## Remaining gaps

- Reading: none. Blocker: illegible (the woodcut's sign identities are uncertain; two transcriptions disagree on
  the class inventory).
- A homophonic solver that solves a 150-letter, 31-sign Latin control: not available here.
- Amadi's *Letere diaboliche* table (sign → demon name) and Ambrogio's own alphabets in the same book: not seen
  (archive.org and Google Books blocked in this environment). Blocker: needs the scans.

## Escalation

- Get the Ambrogio scan (archive.org bub_gb_yUkKq_QnrnwC, n428) and his alphabet plates; compare each sign with the
  Ethiopic, Armenian and "magical" alphabets he prints; get Amadi's table from Scheers's book.
- Re-transcribe from the sharper scan, reconciling with Scheers; then a stronger homophonic solver (Lasry-style,
  with restarts and n-gram 5) calibrated on matched controls.
