# Re-reading log, R929 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b36)

## Starting point

Reading audit (22 Oct): "decoded, not read": George Lasry's plaintext (DECODE, 23 Oct 2020) was on the record only and
no copy was in any checkout. No reading file: before = 0.00.

## 1. Is there a text already?

- `research/reading_audit/b36_fetch.py` (project cookie, valid) fetched the R929 record page and all five files into the
  session scratchpad (not the repository: DECODE's and Lasry's work): Pettersson's transcription D1821, Lasry's key
  D3085, his interlinear cipher/plaintext D3084 (ff. 245-246 and 247), his plaintext with dating notes D3083, and the
  one image (1817 x 2300 px). The record has no comment block, margin gloss or clear copy.
- Neighbours: R928 (ff. 245-246, Goffe at The Hague, same key, a different letter), R927 (ff. 241-243, a simple
  substitution, non-decrypted), R930 (f. 249, graphic signs, non-decrypted). No decipherment or clear copy of f. 247.
- Lasry's plaintext is the existing decipherment. It is not copied into the repository (his work); the reading below
  is built from the figures and his key, and his plaintext was compared row by row.

## 2. Image check and transcription

The image was rotated (the cipher is written sideways on the lower half of the leaf, the last three lines in the
margin) and read line by line at full size (scratchpad crops). Ten corrections to Pettersson's transcription
(`R929_corrections.tsv`), corrected transcription `R929_signs.txt`:

- `810` (twice) is **o2** on the image, a letter-digit group like the key's o0 = WE; o2 = WE gives *weke* and *wekly*,
  both occurrences. Adopted (holds at every occurrence; Lasry read the same words from context).
- `993` is **g3** (key: MAY), "releif may be brovght"; `e5 106` is **c5 p6** (FOR WHICH); `e5` before "his" is **c5**
  (FOR). These are the writer's groups read correctly; all are already key values.
- `105` is written **p5** (same value WITH).
- `26`, `26`, `4` are the dates in clear figures (Ian 26; 26 of Decemb; the 4 of Ianuary).

## 3. Decode and alignment

`python research/reading_audit/b36_sp106.py <scratchpad R929>` decodes the corrected rows and prints Lasry's row under
each. Result: every letter group agrees with his plaintext; the corrections give values where he had open codes
(<810> WE, <993> MAY, <106> WHICH) and one change ("for his", where he has "in his"). The figures 81-90 (30 tokens)
fall only between words: word dividers.

Word-by-word alignment of `R929_reading.md` with the decode: every unbracketed word is spelled out by the figures (or
is a key word group), in the figures' spelling (U and V apart in the key: *withovt*, *brovght*, *hvmble*; a2 *are*
used for *ar*: *farether*, *mareriage*). Code values are marked: {word} two or more contexts (425 your x3, 429 you x2,
e3 her x2, 241 King x2), [?word] one context or sense only (334 Queen, 199 give/send, 208 Majesty, 319 Port in
*[?Port]ugall*, 259 letter). Supplied words: none. Look-alike letters: none (0 of the reading's letters).

## 4. Score

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=en) | no reading (0.00) | 0.273 (3/11) |
| reading body, b17 HOLES=1 (English 1646) | - | **0.727 (8/11)** |

The plain figure counts the period spellings (weke, wekly, thankes, affaires, releif, embassage, Decemb, Sr) and the
short sentence fragments the splitter makes at "Sr," as holes. The three unclean sentences on the explicit-hole count
are the [566] clause, the [554] [620] close with the signature codes, and the [?Port]ugall/[?letter]s sentence.
Reader's judgement: every sentence holds and translates (`R929_en.md`).

## Result

Read (grade B: the alphabet is Lasry's key throughout and agrees with his plaintext; nine code values are read here
from context, five of them from one context only).

## Open

- 566, 554, 620 and the signature 316 440 236: no-key-material (one context each, not in Lasry's key, no clear copy).
- 199 give or send: both fit both contexts.
