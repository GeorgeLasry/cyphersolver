# The Louis XIII–Sabran cipher, 1631–1635: Baluze 155 f. 79, fr. 4134, fr. 4135 — NOTES

Status: in progress (22 Oct 2026). George Lasry's key reads all 43 imaged pages (PR 84); seven listed leaves in the
same key (fr. 4134 f. 51; fr. 4135 ff. 217, 226v, 227v, 231v, 239v, 243) and Baluze 156 f. 157 are not yet done.

**Outcome: key recovered from ciphertext-only by George Lasry, read in part (contributed, PR 84).** He recovered
the key with CTTS's built-in cryptanalysis in 2022 on the King's letter of 1631, and in October 2026, with Claude
Opus 5.5 and OpenAI Codex, completed the transcription of 43 images and the nomenclator, and edited and translated
18 letters (`lasry2022/READING.md`). Write-up: `docs/sabran1633.html`.

**One key, one entry (22 Oct 2026).** Two former entries are folded in here:
- `sabran1631` (Louis XIII to Sabran, Baluze 155 f. 79, DECODE R2748; "read from existing decipherment",
  Lasry 2022): its notes are `notes_former_sabran1631.md`; `docs/sabran1631.html` is now a "moved" page.
- the fr. 4134 entry built on Harumi-Matsuba's partial AI reading of nine leaves (issue #56, 20 Oct 2026): its
  notes are `notes_issue56_fr4134.md`, its data and code `contributed/`, the earlier checks `measure.py`,
  `measure.txt`, `spotcheck.md`.

## Documents (all three in one cipher)

| source | images | cipher signs | letters |
|---|---|---|---|
| BnF Baluze 155 f. 79r–v: Louis XIII to Sabran, Dijon, 28 Mar 1631 (DECODE R2748; Gallica btv1b9001401d) | a1, a2 | 528 | 1 |
| BnF fr. 4134 ff. 46v–73v, Sabran's "Troisième livre des negotiations … à Gennes" (1633), to Bouthillier (Gallica btv1b9060193z) | 14 | 1,061 | 8 |
| BnF fr. 4135 ff. 132–252, "Le quatrième livre …" (1634–35), to Bouthillier (Gallica btv1b9060194c) | 27 | 1,764 | 9 |

Melchior de Sabran was the French resident at Genoa from late 1629 to about 1638. The letter-books are his copies of
his despatches to Claude Bouthillier (or his son Léon, Chavigny, secretary of state from March 1632: which one
received each letter is open). Most images show only part of a letter; dates in brackets come from the leaf order
and the BnF catalogue (Lasry's READING.md, letter by letter).

## The key (Lasry, `lasry2022/ctts/key.txt`)

Homophonic substitution of 22 letters with 51 signs (up to four for S; digits 7 = A, 8 = E, 9 = I, 10 = O,
11 = V); 41 two-digit codes for words and syllables in first-letter order (17 bon, 24 ce, 26 de, 35 Genes,
47 monsieur, 59 que, 68 vous, 95 ou); ten name signs read from context ([France?], [Espagne?], [Republique?],
[Savoie?] …); three doubling signs. The clerks' hands differ from leaf to leaf, so one sign can look different
(the clerk of ff. 57 and 242v–245v writes H with a straight stem and F as a script L).

## Checks made here (22 Oct 2026)

- `decode.py` applies key.txt to the CTTS transcription and reproduces Lasry's counts exactly: 3,353 signs,
  2,853 letter signs, 287 firm and 212 tentative code readings ([Traicte] counted as tentative), one unknown
  (code 46). Per source 528 / 1,061 / 1,764; 108 distinct sign labels (hand variants included).
- `docs/_validate.py` (fr-1600-letters, letter signs only, codes and clear text as breaks): reading −2.125 per
  letter; random keys −5.728 (z 7.8); key fitted to shuffled text −3.255 (z 94.3); annealer on the real text
  −2.916. Verdict: pass.
- `coherence.py` → `coherence.txt` (word cover, fr-henri4 vocabulary, early spelling normalised): 83.7% of the
  deciphered text lies in French words of 3+ letters; Baluze 155, which Lasry deciphered in full in 2022, gives
  91.6%, the measure's ceiling on a clean letter; fr. 4134 84.5%, fr. 4135 80.8%; shuffled keys median 36.9%,
  max 44.9%.
- Against the independent reading of issue #56 (Harumi-Matsuba, nine fr. 4134 leaves): 761 of their 865 decoded
  letters align with Lasry's (88%; f. 73v 100%, f. 66v 98%, f. 46v 96%, f. 50v 77%, the leaf where theirs formed no
  words). Their unlisted codes 35, 12, 33 are Lasry's Genes, [Agent?], [Guerre?].
- Image: the second cipher line of Baluze 155 f. 79r (DECODE R2748 P1) matches the transcription sign for sign
  (26 of 26: *monacho, l'avtre vostre seiovr a Genes*). Gallica refused scripted IIIF requests on 22 Oct 2026, so
  no fr. 4135 leaf was checked on the image here.
- No edition of the fr. 4134/4135 cipher passages found (web, Tomokiyo louisxiii.htm and GL.htm, the
  contributor's sources). Sabran's despatches of 1636–37 printed in the *Correspondance de Sourdis* are later.

## Remaining gaps
- code 46 (fr. 4135 f. 219, once) - blocker: open-codes; "d'une [46] de l'armée navale", context does not fix it
- 212 tentative name-sign readings - blocker: open-codes; read from context only; o- and o-- may be confused in the ff. 215v–216 hand
- cipher runs that do not read (f. 50v "veraivre", "fevitga", "tmineli…"; f. 215b "parico"; f. 228v "duc de s / vop"; "Vbr[?]" on 54b, 57b) - blocker: illegible; reviewed against the images by the contributor, probably clerks' slips in the copies
- fr. 4134 f. 51; fr. 4135 ff. 217, 226v, 227v, 231v, 239v, 243; Baluze 156 f. 157 (1636) - blocker: not-attempted; listed by Tomokiyo, on Gallica, workable with the key
- the originals as received (Archives diplomatiques, Correspondance politique, Gênes) - blocker: needs-physical-access; not digitised

## Escalation
- [x] siblings: Baluze 155, fr. 4134 and fr. 4135 in one key; the issue #56 reading compared (88% agreement); Baluze 156 f. 157 and seven leaves still to do
- [x] clear-pages: no decipherment on the letter-book leaves; Baluze 155 f. 80 blank
- [x] known-keys: the key is Lasry's own, recovered ciphertext-only
- [x] print: no edition of these passages; Sourdis correspondence covers 1636–37 only
- [x] key-rebuild: nomenclator completed from context and first-letter order; code 46 stays open
- [ ] retry: not done — the uncovered leaves are the retry; open on Gallica with this key

## Files
- `lasry2022/` — George Lasry's contribution (PR 84): CONTRIBUTION.md, READING.md, CTTS project, key and overlay images.
- `decode.py`, `coherence.py` (+ `coherence.txt`), `validation.tsv` — the checks above.
- `notes_former_sabran1631.md`, `notes_issue56_fr4134.md`, `contributed/`, `measure.py`, `measure.txt`,
  `spotcheck.md`, `build_reveal.py` — the two former entries.
- `profile.json`
