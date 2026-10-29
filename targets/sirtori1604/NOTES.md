# Sirtori cipher, BNE Mss/994 ff. 83-90 (catalogue 358, Cryptoole ITXXXX-1)

Status: in progress. Attempted 28 Oct 2026 (claude-opus-5-5): system narrowed, nothing read. Waiting on the
high-resolution BNE scans Brice Dudout has ordered; the BDH copy is behind a browser check this session could not pass.

## The document
Madrid, Biblioteca Nacional, Mss/994 (Luis Valle de la Cerda's memorial of services, with cipher papers),
ff. 83-90; BDH bdh0000174344. The 1890s inventory entry (quoted by Pelling 2012): "La cifra que Geronio Sertori milanes
ofrecio a S. M. por suya, y el Consejo de Estado la cometio para que la viese Luis Valle de la Zerda, el cual mostro al
dicho Sertori un papel en que estaba la misma declarada por el al Rey Don Phelippe Segundo" (ff. 83-91?).

- **Date.** 1604, Valladolid (f. 90 dated 7 Oct 1604, Tomokiyo; Dudout 2026). Not 1599.
- **What the ciphertext is.** Two letters (Dudout, 27 Oct 2026, email): f. 85r with the marginal name "Andres de
  Prada" (endorsed f. 88v "Andres de Prada secretario de estado de su Mag.d"), and ff. 86r-86v with the marginal name
  "Juan Baptista de Tassis" (endorsed f. 87v, with a clear note "..mporta al seru[ici]o de su Mag.d que se de luego ... a
  buen recaudo"). Valle does not say he broke them: he says he already had "la misma" cipher, shown to Philip II
  fifteen years earlier. Language therefore Spanish (or Italian), not Latin.
- **Layout.** Words separated by spaces, almost every word followed by a dot or comma (sometimes preceded), tall
  looped strokes standing over some words, chains of 2-5 small loops, a signature block bottom right, and a two-word
  line bottom left. **The bottom-left line is the same on both letters** (f. 85r and f. 86v: the same five signs,
  read "3 l l-o 7 l" in the working shapes), so it is a formula common to both (place/date line or a fixed
  subscription), a crib for later.

## Files
- `transcription/gomez2012_stream.txt`: Sara Gomez Hernandez's 27-symbol transcription of ff. 85-86v (747 signs),
  copied from Pelling 2012. No word divisions, and the dots, commas, arcs and loop counts dropped.
- `transcription/caballero2012_f85.txt`: Eloy Caballero's word-divided transcription of f. 85 with marks (his letters
  are his substitution, not sign names). Used only for counts; his Latin reading is not used.
- `solve_stream.py`, `results/stream_runs.json`: the substitution runs below, with controls.
- Images (not committed): Pelling's copies of ff. 85, 86r, 86v (about 950 x 1480 px), at
  `https://ciphermysteries.com/wp-content/uploads/sites/6/2012/06/Sirtori-page-85.jpg` (-86, -87).

## Prior work
- Gomez Hernandez (final-year project, before June 2012): transcription, concluded "monoalphabetic"; no reading.
- Caballero 2012 (Cipher Mysteries comments, ideasexcel.com): Latin reading of f. 85, signature "Sirtori Girolamo",
  with abbreviation expansions chosen word by word. He himself grants the excess freedom. Not accepted (catalogue
  review 20 Oct 2026). Dudout's identification of the two letters as addressed to Prada and Tassis makes a Latin
  petition signed by Sirtori unlikely.
- Tomokiyo, cryptiana valle.htm: episode, folios, date of f. 90; no reading.
- Dudout 2026: identification of the letters; has asked the BNE for high-resolution scans.

## Findings, 28 Oct 2026

**Signs per word.** f. 85 has 94 words in the body (counted on the image here, and the same 94 in Caballero's
word-divided copy), carrying 206 signs: **2.19 signs per word**. Letters per word in the shared corpora (`lang/`):
Spanish (es-golden-age) 4.27, Italian (it-cinquecento) 4.69, Latin 5.68. *Consonants* per word: Spanish **2.22**,
Italian 2.40, Latin 3.03. A letter-for-letter substitution of any of the three is excluded: the words are half as long
as they should be. Latin is too long even as a consonant skeleton (3.03), which is a second argument against
Caballero's reading.

**Group-length distribution.** f. 85 groups of 1/2/3/4 signs: 13/59/26/3%, none longer. That is too narrow for words
in any form: Spanish *consonants* per word run 1/2/3/4+ = 38/23/16/19%, so "consonant signs, vowels in the marks"
fits the mean (2.22) but not the shape, and is ruled out. It matches Spanish **syllables** spelled out (8/56/29/6%;
Italian 7/55/31/5%; `syll.py`).

**No vowel set.** If each group were a syllable spelled letter by letter, four to six signs (the vowels) would occur
exactly once in nearly every group. `vowel_set_test.py` searches every set: the best covers 64% of groups, the same
as groups with their signs shuffled (60-63%), against 89% for real Spanish syllables of the same count. So the
groups are not letter-spelled syllables either.

**Signs have places.** `position_test.py`: some signs lean to the start of a group (Caballero's I, E, S, V), others
to the end (O, Q, G). Skew 0.41 against 0.24 for shuffles (99th percentile 0.33). The groups are structured units.

**What is left.** Groups of 1-4 signs with the length profile of syllables, no vowel signs, positional structure,
and a dot or comma on almost every group: a syllabic or code system in which a group (perhaps with its mark) stands
for a syllable or a word, or signs whose value depends on the mark beside them. Loop chains of different lengths
(Gomez's O = three loops, 8 = four) may be one more variable. None of these can be tested on a transcription that
drops the marks and the loop counts.

**Vowel-only words.** Isolated marks with no sign stand between words in several places (f. 85 l. 7 end ",,";
l. 12 ", -"), as Spanish *y*, *a*, *e*, *o* would be under a consonant-sign system.

**F3 and B3.** Gomez's "3" (the tall stroke) follows F or B 76 of 85 times, so F3 and B3 are better taken as two
signs (or the stroke as a mark on F and B), not as a separate letter.

**Statistics of the Gomez stream.** 747 signs, IC 1.84 (normalised to 26): language-like. N 102, 3 85, B 77, P 67,
F 52.

**Substitution solver on the Gomez stream** (`solve_stream.py`, `results/stream_runs.json`). Many-to-one
substitution anneal, letters-only order-4 models built from the shared `lang/` corpora (numeral tokens dropped),
10 restarts x 40k moves. Control = a passage of the same corpus, same length, enciphered with the same number of signs
(homophones on the commonest letters). Per-character log-prob:

| model | stream | control recovered | control score | real score |
|---|---|---|---|---|
| es full | raw (29 signs) | 99% | -1.81 | -2.78 |
| es full | F3/B3 merged | 48% | -2.32 | -2.81 |
| it full | raw | 100% | -1.78 | -2.70 |
| it full | merged | 0% (search trap) | -2.42 | -2.65 |
| la full | raw | 99% | -2.15 | -2.65 |
| la full | merged | 99% | -2.16 | -2.61 |
| es/it/la skeleton (vowels deleted) | both | 3-24% | | |

Letter-for-letter substitution of Spanish, Italian or Latin is ruled out on the raw stream, where every control is
recovered and the real stream stays 0.5-1.0 below. The consonant-skeleton runs are underpowered (controls not
recovered) and say nothing. All of this is on a transcription that drops the marks.

## Remaining gaps
All of ff. 85r, 86r, 86v is unread. Blockers: **illegible** at the resolution available (the dots, commas, arcs and
the length of the loop chains cannot be read reliably from the 2012 web copies, and the BDH copy is the same 140 ppi);
no key material (Valle's own description of the scheme, ff. 83-84 and 88-90, has not been read here, because BDH
is behind a browser check).

## Escalation
- Siblings: none known. Valle's "papel" with the same cipher shown to Philip II (c. 1589) would be the key; look for
  it in Mss/994 ff. 88-91 and in the rest of the volume.
- Clear pages: ff. 83-84, 88-90 (Valle's record and the endorsements) not yet read; first thing to do when the
  images are in hand.
- Known keys: none published. Sirtori's printed works (*Telescopium*, 1618; *Compendium politicum*) checked by
  Pelling/Caballero only for abbreviation habits.
- Print: no edition of the episode found beyond Navarro Bonilla et al. 2015 and Carnicer and Marcos 2005 (episode
  only).
- Key rebuild: substitution runs on the mark-stripped stream (above). The next attack needs a transcription that keeps
  every mark and loop count, then a consonant-sign + vowel-mark model.
- Retry: when Dudout's high-resolution scans arrive.
