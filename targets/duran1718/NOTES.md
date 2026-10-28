# Fernández Durán to the marqués de San Felipe, El Pardo 30 Nov 1718 (ACA, DECODE R10181; catalogue 355)

Status: no write-up (attempted, closed unread: one-part numerical code of about 770-880 entries, no key on DECODE or in print; the ciphertext-only attack failed its own control)

The despatch is still unread. It stays in the catalogue as "attempted, open".

## The document

- Barcelona, Archivo de la Corona de Aragón, Diversos, Legación en Génova y Turín, Cajón 1, leg. 22, doc. 67.
  DECODE R10181 ("ACA_Diversos_Cajón_1_leg.22_doc.67.", Cipher, Non-decrypted, public access, 4 images, dated 1718,
  no sender, receiver or language on the record; symbol sets "Graphic signs, Alphabet, Numerical"; it is numerical
  only). Images fetched 28 Oct 2026 into `decode/` (git-ignored).
- P1: cover, "... 30 de Nov.e 1718 / D.n Mig.l F.z Duran / en Zifra". P2 left leaf: 17 lines of dot-separated
  numbers and the address "S.r Marq.s de S.n Ph.e" at the foot. P3 right leaf: 10 lines of numbers, then in clear
  "Dios g.de a V.S. mu.os an.os como deseo. El Pardo 30 de Nov.e 1718", signed "D. Mig.l F.z Duran".
- Miguel Fernández Durán was Secretario del Despacho de Guerra; the marqués de San Felipe (Vicente Bacallar y Sanna)
  was Philip V's envoy at Genoa. The letter falls during the War of the Quadruple Alliance, three months after Cape
  Passaro. Its subject is not known.

## Transcription (`ciphertext.tsv`)

- Taken from NoAutopilot's (Turner's) reconciled transcription (NoAutopilot/cipher-lab, `aca-sanfelipe-duran-1718/harvest/
  ciphertext.tsv`, two blind passes, 309 tokens; copy in `turner/`). Checked here against the images on f2r ll. 2-4
  and the end of f2v: the digit shapes agree (7 written as ")", 9 as a tailed "ɔ", 4 as a triangle, 5 as an "S",
  0 as a small "o").
- **Correction: Turner's file stops one line short on f2v.** The last cipher line, which runs into "Dios g.de",
  is `433 163 369 216 424 378 309 524` (the last group 524 or 594, grade M). Added as f2v L11. Total 317 tokens,
  149 distinct, values 2-768 plus one 877 (Turner's R grade; probably 377 or 577, not checked further).
- The six groups `369 216 424 378 309 5?4` close the letter and also occur on f2r l. 14 (with 215 for 216 and 594
  for 524, probably the same phrase misread on one side). It is the letter's longest repeat and probably a closing
  formula.
- Counts (`key_ranges.txt`, `python mono.py`): 163 ×16, 32 ×11, 544 ×9, 216/551/222 ×8, 594/652 ×7. No values
  between 111 and 149 or between 274 and 307; nothing between 768 and 877.

## The keys of the same fonds (R10189-R10197)

Cajón 19, leg. 30 of the same legation archive holds the keys DECODE photographed (docs 1, 2, 3, 5, 6, 8, 15, 16,
19). All nine were downloaded and viewed on 28 Oct 2026. None fits:

| key | top value | letter tokens in range |
|---|---|---|
| R10189 (1715, Molina-Villamayor) | 231 | 39% |
| R10190 (1715) | 282 | 41% |
| R10191 (1717, military, San Felipe = 180) | 288 | 41% |
| R10192 (1715) | 243 | 39% |
| R10193 (1715, Acquaviva; one-part, descending) | about 442 | 56% |
| R10194 (1711, Monteleón-Villamayor, "Estado y ... Guerra") | 530 | 65% |
| R10195 (1716) | 210 | 29% |
| R10196 (1718, Cellamare-Monteleón) | 209 | 29% |
| R10197 (1715) | 182 | 27% |

A key reads all of a letter's groups; 112 of the 317 groups are above 530. Under R10194, the nearest family (it
names the war secretariat), the in-range groups give nonsense: 32 = G occurs eleven times, 163/164/165 = lle/che/lli.
R10182-R10188, next to them on DECODE, are other ACA fonds (1413-16th c.) and do not belong to this correspondence.
Brice Dudout (email, 27 Oct 2026) reached the same conclusion on the nine keys.

## The system (measured, not proved)

A numerical code with no marks or separators beyond the dots. The value range and the number of distinct groups fit
a code of 770-880 entries. R10193 in the same fonds is a one-part (alphabetical) code mixing syllables and words, so
the type was in use at this legation. Brice Dudout suggested an ascending one-part word code with 'de' 163,
'del' 164 and 'que' 652. That is consistent with the counts (163 is the commonest group, 164 the next value) but is
not established: no passage reads under it.

## What was tried (28 Oct 2026)

1. **Prior decipherment.** Cryptoole XX1718-2 is still "open" (snapshot of 11 Oct 2026); DECODE has no document
   attached; Turner's searches of 28 Sept and 3 Oct 2026 (Cryptiana, Cipherbrain, the solver repositories) found
   nothing; a web search on 28 Oct 2026 found nothing either.
2. **Keys of the fonds.** All nine tested by range and, for R10194, by applying the in-range values. None fits.
3. **Ciphertext-only, one-part code (`mono.py`).** Each distinct number is given a Spanish word, constrained to
   alphabetical order (ascending, or descending), and the assignment is annealed under a word-bigram model built
   from `lang/corpora/es-vasto-memorias.txt` and `es-gutenberg.txt`, with a prior tying a word's alphabetical
   position to its number.
   - **Control.** A 317-word passage of the Vasto memoirs enciphered in a one-part code drawn from the 700 commonest
     corpus words (numbers 2-770, no syllables, no names): 49% and 60% of tokens right on two seeds (2M iterations),
     mostly function words. So even in this easy setting the method cannot produce a reading, only a skeleton.
   - **Letter.** Ascending best -1499.5, descending best -1557.9 (four restarts each, `run_asc.txt`,
     `run_desc.txt`). With Brice's anchors fixed (`run_anchored.txt`) the best is -1497.5. All three outputs are
     word salad with Quixote vocabulary. The free ascending run did put 163 = de by itself, but 'que' went
     elsewhere. Nothing here is a reading.
4. **Not tried:** a syllable-aware solver (the real code very probably spells names and rare words in syllables, as
   R10193 does), a corpus of Spanish war-office despatches of 1715-1720 (none in `lang/`).

## Remaining gaps

- R10181, all 317 groups - blocker: no-key-material; the 1718 war-office code is not among the nine keys on DECODE
  and is not in print; the one-part solver fails its control, so a ciphertext-only reading is not in reach

## Escalation

- [x] siblings: R10182-R10197 opened; R10189-R10197 are the legation's keys, none for this code
- [x] clear-pages: the only clear text is the closing formula and signature (P3) and the cover (P1)
- [x] known-keys: all nine keys of Cajón 19 leg. 30 tested; none covers the range or reads
- [x] print: web, Cryptiana, Cipherbrain, Cryptoole, Turner's search log: no edition or decipherment found
- [x] key-rebuild: one-part word-code anneal with a control; control 49-60%, letter word salad
- [n/a] retry: nothing reads, so there is nothing to retry with

## What would move it

- The rest of Cajón 19 leg. 30 (docs 4, 7, 9-14, 17, 18, not on DECODE): ACA reading room or PARES description.
- The war secretariat's cipher of 1718 in AGS (Guerra Moderna or Estado), or San Felipe's deciphered register at Genoa.
- A Spanish diplomatic/military corpus of c. 1700-1730 in `lang/` and a solver that mixes syllables and words.

## Credits

- NoAutopilot (Turner), cipher-lab: transcription, key ranges, search log.
- Brice Dudout: the nine keys checked, the one-part code suggestion with three anchors (email 27 Oct 2026).
