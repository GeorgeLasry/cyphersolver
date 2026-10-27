# Duplessis-Mornay circle: undeciphered figures printed in the 1824 *Mémoires et correspondance*

Status: in progress (1593 figures read with Brice Dudout's key, 27 Oct 2026; 1595-98 figures open)

Opened 25 Oct 2026. Found while checking whether Archives nationales 402AP/13 (catalogue 365, "lettres chiffrées"
of the Mornay family) was already in print. It is not, but the printed edition itself carries unread cipher.

## Source

*Mémoires et correspondance de Duplessis-Mornay* (Paris: Treuttel et Würtz, 1824-25), 12 vols. archive.org
`mmoiresetcorre01morn` … `mmoiresetcorre12morn` (vol. 7 text is short in that copy; use `mmoiresetcorresp07morn`).
Page images: `https://archive.org/download/<id>/page/n<leaf>_w1600.jpg`; leaf from `<id>_page_numbers.json`
(vol. 5: printed p. 471 = leaf 480, p. 487 = leaf 496).

Editors' note, vol. 6 p. 82 n. 1: they kept the figures they had a translation for (printed above them) "afin que le
lecteur puisse y recourir pour traduire les chiffres dont nous n'avons pas la clef". So passages printed as bare
figures were unread in 1824.

## Inventory of cipher in the edition

| Vol./letter | Writer → recipient, date | State |
|---|---|---|
| 5, CCI, pp. 471-475 | Du Maurier → Duplessis, "mardi .. juin 1593" (= Tuesday 20 July 1593, Dudout) | bare figures, 6 passages, 72 groups; **read 27 Oct 2026 (Dudout key)** |
| 5, pp. 487-488 | J. de Serviez → Duplessis, 6 Jul 1593 | bare figures, 2 passages, 21 groups, same system; **read 27 Oct 2026** |
| 6, LVI, pp. 82-85 | Catherine de Parthenay (Mme de Rohan) → Mme Duplessis, Paris 30 Jul 1594 | figures printed **with** decipherment above; a ready key (syllabic/homophonic, e.g. 158 = re, 162 = Sa, 49 = n) |
| 6, CVII, pp. 179-181 | Loménie → Duplessis, Paris 24 Feb 1595 | bare figures, different system (many groups x10: 610, 810, 910), plus small numbers as name codes (3, 11, 16, 25, 26, 98, 99) |
| 6, CIX | Duplessis → his wife, 1595 | short bare run |
| 7, LXVI-LXVII, CXLI and others | Duplessis, Jan-Oct 1597 | bare figures |
| 8, p. ~507 | Duplessis, 14 Apr 1598 | short run |
| 11, CXCVII | 2 Dec 1611 | name codes only |

Not yet transcribed: everything after vol. 5. The Rohan 1594 key should be tested on the 1595-98 figures first: same
household, and the editors expected readers to do exactly that.

## The 1593 system (vols. 5)

`ciphertext.txt` has all eight passages with their clear context. 93 groups, 62 distinct; repeats 149, 912, 129, 2210,
515 (x4). Groups split into two numbers of 2-24 (2210 = 22|10, 1020 = 10|20, 912 = 9|12), and both halves use the same
set of values (1 and 3 never occur in either half).

Context cribs:
- P5 "la maison de [10 groups]": the house of the vicomte de Pont-du-Château, younger brother of the marquis de
  Canilhac (family Beaufort-Montboissier-Canillac). P1 and P5 both open with 192.
- P1 follows "une particularité … que," and precedes "avec les cérémonies et circonstances": the July 1593 conversion
  of Henri IV is the topic of the letter.
- S2 "le roy est [1014 215 17]".

## Steps

1. Literature: no decipherment found (web search, 25 Oct 2026).
2. Hypothesis A, two letters per group: annealed number→letter onto `fr-1600-letters` with a frequency penalty
   (`anneal_pairs.py`). No French in 10 restarts. Failed.

3. Rohan 1594 key built from the printed decipherment (`rohan1594_key.tsv`, 78 values: letters 6-65, syllables
   88-175, words 660-919 with 810 = de and 910 = les, names 10 = le roi, 87 = Paris, 95 = Tours, 96 = Saumur).
4. Transcribed Loménie 24 Feb 1595 (`lomenie1595.txt`, 15 passages) and Duplessis 18-19 Jan 1597 to Cargroy and to
   his wife (`duplessis1597.txt`, 11 passages) from the page images.
5. Applied the Rohan key to both: no French; most groups unvalued, place names fall mid-word. **The key does not
   fit.** Partial sign in Loménie: "du sieur 810 62 110 4" = "du sieur de …", so the x10 word codes (810, 910, 410,
   610) may belong to a shared series even though the letters differ. In the 1597 letter to his wife the editors
   printed some letters among the figures ("e. 77. v. 36. 71. 5", "15. 102. 32. tr. 89 …").

6. **27 Oct 2026: read by Brice Dudout** (email to Daniel; published on Europe chiffrée,
   `bdudout.github.io/europe-chiffree/en/documents.html#mornay-1593`, crediting this folder and hypothesis A).
   Hypothesis A was right (two letters per group); the alphabet is folded: a = 2, c-m on rising odd numbers
   (c 5, d 7, e 9, f 11, g 13, h 15, i 17, l 19, m 21), n-u on falling even numbers (n 22, o 20, p 18, q 16, r 14,
   s 12, t 10, u/v 8), 44 = x/y (probable); 1 and 3 never occur, b unattested. He built it on P1-P5 and S1 and read
   P6 and S2 held out. Key in `key_dudout.tsv`; `apply_dudout.py` applies it to our transcription and writes
   `reading_dudout.txt`: 93/93 groups give letters, three groups split two ways (219 me/al, 213 an/na, 215 ah/mc),
   the sense decides each. Readings:
   - P1 "l'arrest estoit adressé contre le duc de Guise pour le tirer à quatre chevaux"
   - P2 "Touraine" (244 = a + x/y: "Tour{ay}ne"); P3 "Montrichart"; P4 "Vautorneuf" (unidentified)
   - P5 "la duchesse d'Angolesme"; P6 "[le] conte de Gramont ne soit de la partie"
   - S1 "le chancelier et Sourdis font l'entreprinse"; S2 "le roy est trahi"
   Differences from his text: our P1 gives "larest" and S1 "lenteprinse" (his "l'arrest", "l'entreprinse"):
   check the page images for a dropped group. He also dates Du Maurier's letter Tuesday 20 July 1593 (the
   edition prints "mardi .. juin"; the letter anticipates the abjuration of Sunday 25 July).

## Remaining gaps

- 1593 sign 44 (x/y, end of P1 and P2) and the two possible dropped groups in P1 ("larest") and S1 ("lenteprinse") - blocker: too-short; 44 occurs twice, b never; the dropped groups need the page images rechecked
- Loménie 1595 (95 groups) and Duplessis Jan 1597 (90 groups): transcribed, a different system; the Rohan key does not fit - blocker: not-attempted; the folded 1593 key and its variants not yet tried
- Later 1597 letters in vol. 7 (pp. ~169, 305, 335, 347) and vol. 8 (1598) - blocker: not-attempted; not yet transcribed

## Escalation

- [ ] siblings: transcribe every bare-figure passage in vols. 5-8 and pool by system (vols. 5-6 and Jan 1597 done).
- [n/a] clear-pages: printed edition; the editors printed decipherments only where they had them (vol. 6 Rohan 1594).
- [x] known-keys: Rohan 1594 key tried on 1595-97, no fit (step 5); Dudout's 1593 key reads 1593 (step 6). Still to try on 1595-97.
- [ ] print: originals possibly AN 402AP/13 (requested 25 Oct 2026) and the Mornay papers at the Institut / BnF.
- [ ] key-rebuild: 1595-97 system not yet attacked beyond the Rohan key.
- [ ] retry: after the 1595-97 attack.
