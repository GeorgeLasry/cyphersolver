# The block table of R1871 (catalogue 264), rebuilt by Brice Dudout

Built on 27 Oct 2026 from this folder's transcription (`../tx.txt`, `../groups.txt`) and Paolo Bonavoglia's
decipherment (`../r1871_bonavoglia.txt`). Bonavoglia publishes the text, not the table, and the contemporary
decipherment (ASVe Senato, Dispacci Francia, filza 166) gives the plain text only, so the table may be new.

## Structure (`table_blocks.json`)

- A syllabary in **blocks of five consecutive codes** Ca Ce Ci Co Cu, one block per consonant or cluster:
  b 115, n 142, r 151, ch 164, f 224, p 242, s 251, t 260, c 315, tr 360, l 433, pr 442, sp 451, gn 453, d 515,
  m 533, st 551, z 560 (so 115 ba, 116 be, 117 bi, 118 bo, 119 bu ...).
- **Vowels on X56**: a 156, e 256, i 356, o 456, u 556.
- A few words and fragments: 167 con, 368 non, 366 nel, 540 spagn-, 200 = new paragraph (¶).

## Validation

Learnt on L01-L15 only, then applied to L16-L23 held out: 94.9 % of the decoded letters agree with Bonavoglia
(shuffled controls 0.16-0.48). Whole text: 68 % of the 612 groups covered, 94.8 % agreement.
A blind EM search without the plain text fails, as does its control: the table rests on the plain text.

`decoding_on_your_transcription.txt`: the table applied to your transcription, ‹n› = code without value.

## Where it may correct the transcription

- **L18-L19, code 114**: no value fits; the surrounding codes decode well, so we suspect the transcription (a
  misread digit) rather than the table.
- **L22**: the middle of the line is the weakest part; 3/5 and 2/0 are the likely confusions in this hand.
- **269**: Bonavoglia's "[Francesi?]", a single occurrence, unresolved (a dictionary word).
