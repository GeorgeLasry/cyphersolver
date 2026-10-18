# Michel de Seure (Lisbon) to de Fresne and Henri II, December 1558 (BnF fr. 3151 nos. 39-41, 43-44): catalogue no. 10

Status: read. Key recovered and the five letters deciphered by Angus Robinson (GitHub AngusRobinson, PR #40,
16 Oct 2026), from cribs on an adjacent deciphered leaf plus simulated annealing and manual correction; checked
here 18 Oct 2026. Outcome method: key recovered based on adjacent plaintext (contributed).

His files, kept verbatim and not edited here: `SOLUTION.txt` (summary), `KEY.svg` (the sign shapes) and
`KEY_AND_DECRYPTION.txt` (the key and every transcribed position with its output, by manuscript row). His
walkthrough, with continuous French readings and English translations:
https://angusrobinson.github.io/historical-decipherment/seure

Split on 14 Oct 2026 from `../guiche1551/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 10
had grouped these letters with La Guiche's Rome letter of 1551 (`../guiche1551/`) and Noailles's Venice letter of
1558 (`../noailles1558/`), each a different cipher with its own page. Surveyed 21 Sept 2026 (Claude Opus 5) as
part of the joint entry.

## The letters

Michel de Seure, commandeur (Knight of Malta), was Henri II's ambassador in Portugal. Five of his letters in the
volume carry cipher (Gallica btv1b9059865k):

| No. | To | Views | Cipher sections | Positions | Key values / signifying |
|---|---|---|---|---|---|
| 39 | Florimond Robertet, sieur de Fresne | 72-73 | one passage, 20 rows | 405 | 365 / 366 |
| 40 | Henri II | 74-75 | opening, continuation, postscript | 1,474 | 1,380 / 1,385 |
| 41 | Henri II | 77-78 | main, continuation, postscript | 1,921 | 1,792 / 1,799 |
| 43 | Henri II | 81-83 | opening, long continuation, postscript | 3,622 | 3,440 / 3,464 |
| 44 | Henri II | 85-87 | A, B, C | 1,983 | 1,842 / 1,843 |

Measured here from the sign rows of `KEY_AND_DECRYPTION.txt` (scratch script, counts include nulls and
cancellations): 9,405 positions in 397 rows, as Robinson states. "Signifying" = positions less nulls and cancelled
signs.

Correction to the survey of 21 Sept: no. 42 is not Seure's. View 79 is headed "Lettre du Mareschal de Brissac au
Roy Henry second", so the Seure letters are nos. 39-41 and 43-44; view 88 begins a letter of the duc de Guise. The duplicate
pairs were also misstated: measured on the decipherment, no. 41's three passages are the same text as no. 44's
A, B and C (1,295, 449 and 427 letters in common), and no. 43's long continuation and postscript carry that text
again (1,341 letters shared with 44A, 404 with 44C). No. 40 is different. Dates from Robinson's readings (closing
lines; some dockets disagree): no. 39 12 Dec, no. 40 27 Dec, nos. 41, 43, 44 12 Dec 1558 (no. 44 docketed
"Dupplicata"), so 41, 43 and 44 are three copies of one letter. No. 39's address panel names the duc de Guise, its
heading de Fresne. Not re-checked here against the scans.

## The cipher (Robinson's key)

118 sign types: 55 letter signs, up to three homophones each (a = H#, o, ss; e = 3bar, ff, q ...), 18 syllable
signs for 16 values (au, ce, co, con/com, de, est, et x3, il, le, luy, moy, on, par/per, que, qui, si), 22 word signs (argent,
arme, castille, dict, dire, escuz, espaigne, faict, faire, la royne marye, l'empereur, mais, nauires, nous, perou,
portugal, pour, roy de portugal, roy d'espaigne, sire, vostre, vous), one unassigned word sign (N10_4), 21 nulls (among them the numerals 7, 12, 13,
14, 23, 30, 40 and 100 that looked like codes in the survey) and a cancellation sign (`tri`) that voids the sign
before it. No word division. Several signs are secretary-hand Roman or Greek letters.

## How it was recovered (from Robinson's walkthrough and SOLUTION.txt)

- A leaf inserted mid-sentence in the volume holds three short deciphered paragraphs labelled A, B, C, which
  overlap no. 44's cipher sections A-C. These were the cribs.
- Best-effort transcription, then simulated annealing (four parallel runs). Look-alike signs first taken as one
  were split by repeated comparison with the scans: about 230 proposed characters reduced to 118.
- No. 43's postscript repeats no. 44 C; no. 40's enciphered passages have surviving clear copies.
- A held-out section was deciphered with the final key. He estimates at least 18 scribal errors in 9,405
  positions (for example a "p" sign written for g, five times).
- He reports that his AI collaborator ("Sol"), asked to transcribe one section, back-filled signs from a parallel
  plaintext rather than reading the scan (68 of 360 signs wrong, about 19%), and that this was corrected.

## Checks here (18 Oct 2026)

- Language: `lm.best_language` on each letter's decipherment puts fr-1600-letters first (-1.99 to -2.13 per
  letter, fr-modern next at -2.36 to -2.65).
- Statistical validation (`docs/_validate.py`, fr-1530-despatches, `validation.tsv` built from his rows): 9,367
  read tokens, 121 types; reading -2.269 per letter, random keys -5.406 (z 13.0), key annealed onto shuffled text
  best -3.653 (z 56.0); verdict pass.
- Images: rows 1-9 of no. 39 compared with Gallica view 72 (main checkout `research/gallica_sweep/hi/k72full.jpg`):
  the numerals 14, 13, 30, 12, 100 and the 55 sign fall where his rows put them; the clear text before the cipher
  ends "a estimer selon la facon".
- Content: Spanish treasure from Peru and the Indies fleet, the money held at the Medina fairs ("huict cens mille
  escuz"), Queen Mary's death and Philip II, the Portuguese court, and Seure's own debts and pleas for funds.

## Remaining gaps
- N10_4, one occurrence in no. 39 row 10 - blocker: open-codes; unassigned word sign, contributor proposes vostre from context
- 27 damaged or unidentified signs, mostly no. 43 views 82-83 - blocker: illegible; left [...] by the contributor, 10 more read only from context

## Escalation
- [x] siblings: the five Seure letters found in fr. 3151 (no. 42 is Brissac's); 41, 43 and 44 share one text
- [x] clear-pages: the deciphered A/B/C leaf supplied the cribs; no. 40's clear copies reported by the contributor
- [n/a] known-keys: the key was recovered in full by the contributor; no other Seure key is known
- [n/a] print: not needed for the reading; printed sources for Seure's embassy not searched
- [x] key-rebuild: done by the contributor (annealing from cribs, manual correction)
- [n/a] retry: the contributor's held-out section and the three witnesses of one text already cross-check the key; the remaining unread signs are damaged
