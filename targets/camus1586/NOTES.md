# Camus de Pontcarré to Villeroy, March–June 1586: cipher passages in BnF fr. 15572 ff. 111v–272v (Camus's cipher)

**Read in part, 24 Oct 2026.** Contributed by Michael Brackx (@brackxm, issue #91, 22–23 Oct 2026), with Claude Code
(Claude Opus 5.5). Method: **read from existing decipherment**: the blocks that read rest on the contemporary
decipherments on the leaves; Tomokiyo's key table, corrected and extended by Brackx, was applied to the figures as a
check and decides where figures and margin differ. Three blocks reach the read bar (f. 111v 0.961, f. 112r 0.974,
f. 151r middle block 0.963); f. 134v B (0.781) and C (0.812) are read in part; ff. 132v, 134v A, the f. 151r margin and
foot blocks and ff. 272r–v are *decoded, not read*.

Same volume as Matignon's and Mayenne/Forget's ciphers ([`targets/matignon1586/`](../matignon1586/NOTES.md)), a
different cipher, with its own page. Malicorne's letter in the same volume, ff. 162–164, is another cipher again:
[`targets/malicorne1586/`](../malicorne1586/NOTES.md).

## The documents

Letters of Claude Camus de Pontcarré to Villeroy during Matignon's Guyenne campaign of 1586, mostly clear text with
cipher blocks. Ark `btv1b9061879d`, full-size IIIF images.

| leaf | canvas | letter | cipher | contemporary decipherment |
|---|---|---|---|---|
| f. 111v | 118 left | Castets, 21 March 1586 | 7 lines at the foot | interlinear glosses and a full margin text |
| f. 112r | 118 right | (same letter) | 8 lines at the head | interlinear glosses and a full margin text |
| f. 132v | 140 left | Castets, 1 April 1586 | one block | none |
| f. 134v | 142 left | Bordeaux, 3(?) April 1586 | blocks A (5 lines), B (5), C (3) | a margin note beside each (A, B paraphrases) |
| f. 151r | 158 right | Bordeaux, 12 April 1586 | middle block, a vertical margin block, a foot block | margin note (mid); clear postscript (margin) |
| ff. 272r–v | 281 right, 282 left | La Rochelle, June 1586 | 11 + 21 lines | none |

Tomokiyo (Cryptiana, henryiii page, "Camus's Cipher") lists these leaves and gives the key table and one opening
phrase; he gives no reading of the blocks. Nothing on them was in this repository before issue #91.

## Files

- `brackx2026/transcription_r2.txt`: all leaves, one label per sign (`/` = divider); 2,452 labels, 127 distinct.
- `brackx2026/key_r2.txt`: the round-2 key (label = values; `+` null). `brackx2026/legend.md`: each label with its sign shape.
- `brackx2026/blocks_r2.md`: per block, transcription and raw decryption line by line and the contemporary decipherment (issue #91 comment).
- `texts/<block>_transcription.txt`, `texts/<block>_decryption.txt` (raw decode lines, then the margin text);
  `texts/reading_<block>.md` in the writer's spelling and `texts/reading_<block>_en.md` for the five cribbed blocks.
  The decoded-not-read leaves have their phrase decode in `texts/<leaf>_decryption.txt`.

## The reading

Notation: no accents added; `[?]` one unread word; `[?word]` doubtful; `[word]` supplied. Every word is carried by
the figures or by the contemporary decipherment.

| block | words | holes | read_share (v10_relabel.measure) | state |
|---|---|---|---|---|
| f. 111v | 73 | 3 | 0.961 | read |
| f. 112r | 76 | 2 | 0.974 | read |
| f. 134v B | 25 | 7 | 0.781 | read in part |
| f. 134v C | 13 | 3 | 0.812 | read in part |
| f. 151r middle | 26 | 1 | 0.963 | read |

The measure counts in-word bracket expansions as holes (Brackx counted 74/74/32/15/24 words; his percentages were
95.9, 97.3, 78.1, 80.0, 95.8). Reviewed as sentences, grade B, Claude Opus 5.5, 24 Oct 2026.

- **f. 111v**: Ie escriuis au porteur par home expres, et en attendant responce; mais puis que le parent n'est plus en ce
  pays, ie me trouue fort empesche comme i'ay a me gouuerner … car ie uous [?] [?] [?]
- **f. 112r**: … s'il uous plaist que ce soit enchiffre selon le memoire que uous laisse, auquel il uous plaira
  adiouster, pour le nom de celluy qui porte la lettre au parent, ces deux mots: le beau frere ou le porteur; et pour
  moy: le seruiteur ou l'oblige.
- **f. 151r middle**: C'est mon excuse pour auoir la commodite de uoir le porteur et dresser la partie que scauez, que
  i'espere s'effectuera lundy et sans [?subson].

Where figures and margin differ, the figures are followed (*Comont*, *s'effectuera*, *lundy et sans*, *subson* for the
margin's *soupcon*).

*serment* on f. 112r (issue #95, 23 Oct 2026): cipher l. 2 ends `… / m o / ʃ ρ r a q ⱶ θ ʃ t /`; the contemporary
decipherer glossed **ent** over `q ⱶ θ` and **ne** over `ʃ t`, so *-ment ne* rests on the figures (`a` = m, `θ` = t,
`q` = e) and the gloss. `ʃ ρ r` carry no gloss and the key does not give *s-e-r* for them (`ʃ` = m, `ρ` = i/s, `r` =
a/e); *ser-* rests on the margin alone, so the doubt now sits on that syllable only: *[?ser]ment*. The sign there is
drawn `ⱶ` and glossed *n*, possibly a different sign from the key's `f` = e.

## Key

Tomokiyo's table with Brackx's corrections (issue #91): `6` = c (also g); plain round e = r; looped e = s; circled G =
g; ŋ = o (also l, u); long-tailed ŋ = u/v/l; φ = ff/f/mm; Ⱡ = *et*; ‡ = b; ɱ = l; x₀ = *pour*/*par*; ʒo = *vous*; 9 =
e/n/o. Each change rests on cribs or on two contexts and a contact sheet.

## Controls

- Crib agreement: 84.3% (111v), 90.5% (112r), 84.8/70.2% (134v A l. 1/all), 73.6% (134v B), 93.4% (134v C), 90.1%
  (151r mid), 67.2% (151r margin); shuffled medians 31.1–41.8%.
- Language-model coverage: posted 79.3% over all blocks; **corrected by Brackx on 23 Oct 2026 to 74.6%** after the
  French model was rebuilt from Montaigne's *Essais* I–III (Gutenberg 48529, 49168, 58801; the first model had mixed
  in an Italian and a Middle English text); five shuffled keys 36–50%. Crib agreements do not use the model.
- Blind re-transcription of the cribbed blocks: 76–95% token agreement; 22 changes accepted on the image.

## Remaining gaps

- f. 111v: the three groups after 'car ie uous' - blocker: no-key-material; they run past the margin decipherment, no second context
- f. 134v B: the name after 'sauue' (margin C?main, cipher 7 z fa qn es) and doubtful sur, Frenac, peult, on - blocker: no-key-material; the margin paraphrases and does not match the figures
- f. 134v C: the last group and doubtful et, le - blocker: too-short; single signs at the end of the block, one context each
- ff. 132v, 134v A, 151r margin and foot blocks, 272r-v: decoded, not read - blocker: no-key-material; no contemporary decipherment (or a paraphrase only), and the plain 9 and y still carry three values each with no further split on the contact sheets
- 57 unvalued labels (108 tokens), among them the group for 'cy faict' on 134v A - blocker: no-key-material; mostly single tokens with no crib context, not in Tomokiyo's table

## Escalation

- [x] siblings: the other Camus letters in fr. 15572 (ff. 111-272) all transcribed and decoded on one shared label set; the Matignon and Forget ciphers of the same volume are different keys
- [x] clear-pages: the f. 151r clear postscript is a free version of the margin block (crib 67.2%); the f. 132v margin note is not a decipherment
- [x] known-keys: Tomokiyo's Camus table applied and corrected; the matignon1586 Cipher-1 key is a different system
- [x] print: Tomokiyo gives the key and one opening phrase only; no edition found by Brackx's web search
- [x] key-rebuild: values adopted from two or more contexts and contact sheets over all leaves (passes J1-J8); a blind re-transcription of the cribbed blocks
- [x] retry: every block re-decoded with the round-2 key and re-read; holes regraded in the issue #91 comment of 23 Oct 2026

## Next

A crib for ff. 272r–v or 132v (a copy in Villeroy's or the King's papers), and a split of the plain 9 and ŋ at higher
resolution, are what would move the decoded leaves to a reading.
