# Siena no. 11 — Donato Acciaiuoli to Lorenzo de' Medici, Rome, 13 June 1478 (DECODE R4800)

Status: read in part; key recovered from ciphertext-only by George Lasry with CTTS and Claude (about 90% certain; 357 of 381 plaintext letters in words without a query, 93.7%). Contributed result, filed here 18 Oct 2026.

Archivio di Stato di Siena, Concistoro 2308, fasc. 2 ("Lettere in cifra"), no. 11; DECODE
[R4800](https://de-crypt.org/decrypt-web/RecordsView/4800) (Concistoro_2308_54), catalogued "1500-1599", status N/A.
A Florentine letter held in the Sienese file; a key of its own (report section E, "A Florentine cipher of 1478").

## Source

George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (17 Oct 2026), consolidated report sent by email to
Daniel Bourdeau, pp. 18-19, section E. His section is quoted whole in [`lasry_report.md`](lasry_report.md); his key
figure (signs cut from the manuscript) is `docs/siena11_key.png`. His reading, translation and dating are not
re-edited here.

## What the report gives

- **Status (Lasry):** "Solved: about 90 % certain; a few signs and one damaged word open. 15–17 October 2026, by
  George Lasry with CTTS and Claude: transcription by Claude and key recovered by Claude (crib analysis)."
- **Ciphertext:** 393 symbols in 10 lines on P2 (block A 206 symbols in 5 lines, block B 187 in 5 lines), mostly
  homophones for single letters, plus nulls and two literal dotted numerals (80, 7).
- **Key:** 57 distinct signs; homophonic substitution, three to five signs for each vowel, one to three for the
  consonants, a few nulls, no nomenclator.
- **Reading:** block A, after the clear "e veduti brevi e quali scriviamo a dto S.re di Furli:": the lord of Faenza
  likewise to stay in his lands and send two squadrons of men-at-arms into the field; Acciaiuoli marvels at Faenza.
  Block B, after the clear "et della legha": Signor Giovan Francesco Gonzaga will gladly come into Lorenzo's service with
  at least 80 men-at-arms, asks 7,000 ducats for the troops and 1,000 for himself; Baccio(?) will explain by word of
  mouth. Two probable encipherer's slips marked.
- **Context (Lasry):** seven weeks after the Pazzi conspiracy; Gianfrancesco Gonzaga (1446-1496), whose father
  Ludovico III died on 12 June 1478; Pino III Ordelaffi of Forlì and Galeotto Manfredi of Faenza; how the letter came to
  Siena is unexplained (interception is the obvious hypothesis).

## Measure

George Lasry gives "about 90 %". Counted here on his reading text (cipher passages only, the clear words around
them excluded): 381 plaintext letters and numerals; the words carrying his query marks (di?, ? ?v m, non?, da?,
s?ervigi, no?, Bacio?) hold 24 of them. **357 of 381 (93.7%) are in words read without a query.** This is a count on
his plaintext, not on the 393 cipher signs (nulls and the sign lost in the hole are not in the plaintext).

## Project's earlier attempt (siena1421 survey, 24 Sept 2026)

Agent B transcribed no. 11 from the DECODE photographs (`transcripts/no11.txt`, `no11.tok`: 409 tokens, 44 sign
names, moved here from `targets/siena1421/transcripts/` on 18 Oct 2026). Homophonic annealing failed; the Sienese key
R4752 ("Cifra de m. Antonio Bichi 1478 Rom.") did not fit; Gabbrielli's index of Florentine keys (Ilardi reel 58) has
no key for Donato Acciaiuoli. The piece was closed "no key in reach". Nothing of that attempt is claimed in the
reading, which is George Lasry's from his own transcription. His 57 signs against our 44 names: our transcription
merged look-alikes, the obstacle George names for the whole fascicle (accurate transcription).

## 20 Oct 2026: his key checked on this project's transcription

`research/siena2308/verify_lasry.py no11` (moved from `targets/siena1421/` with the split): his key table matched by
shape and count to agent B's sign names (`transcripts/no11.txt`, 24 Sept, made before his work); our tokens
deciphered with his key, without fitting, and aligned with his reading. **357 of 378 sign units agree (94.4%)**; 66.7%
with eight signs unidentified, before his two-stroke signs '+o' (e) and 'o+' (d) were read as our token pairs
PLUS O / O PLUS and ODAG = h, D = a, RHO = o were set. His nulls 'g#', '31', '87', mⁿ, /// are our G HASH, 3 1,
8^dot 7, M^n, SL3. Our two cipher blocks are his two runs line for line. Independent verification of his reading.

## Disagreements with the repository

- None on the facts: sender, recipient, place and date (13 June 1478, dated in the clear) agree with the siena1421
  inventory. The repository's "no key in reach" is superseded by George's ciphertext-only recovery.
- DECODE has "1500-1599" and no sender or receiver.

## Remaining gaps

- one sign lost in a hole in block A ("? ?v m") - blocker: illegible; the paper is holed, no other image
- six doubtful words (di?, non?, da?, s?ervigi, no?, Bacio?), 24 of 381 letters - blocker: too-short; single-occurrence signs and two probable encipherer's slips in a 393-sign text; nothing else in this key is known
- whether the Gonzaga condotta was concluded - blocker: needs-physical-access; George Lasry: unchecked in Rubinstein, Lettere di Lorenzo de' Medici III (1977), not online here

## Escalation

- [x] siblings: every piece of fasc. 2 and the 43 keys of fasc. 1 opened (siena1421 survey); no other piece in this key, which is Florentine.
- [x] clear-pages: the clear text frames the two blocks; no decipherment on the sheet (P1 is the address).
- [x] known-keys: R4752 (Bichi, Rome 1478) tried 24 Sept; Gabbrielli's Florentine key index (Ilardi reel 58) has no Acciaiuoli key for 1478.
- [x] print: Meister 1902, the 1952 inventory; Rubinstein's Lettere di Lorenzo III named by George Lasry, not available online here.
- [n/a] key-rebuild: the key is George Lasry's; extending it needs his sign-level CTTS transcription, which is not in the repository (a question for George).
- [x] retry: 20 Oct 2026, his key run unchanged on the project's own 24 Sept transcription (`research/siena2308/verify_lasry.py no11`): 94.4% agreement; no key extension was made here.
