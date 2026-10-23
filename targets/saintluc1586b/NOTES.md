# Saint-Luc to Henri III, Brouage, June 1586 (BnF fr. 15572 f. 260r-v)

Status: in progress

Outcome (24 Oct 2026): **decoded, not read.** Tomokiyo's St. Luc table, corrected by Michael Brackx on the contemporary
margin decipherments of f. 245r-v, decodes f. 260r-v into French that mostly builds sentences, but too many letters
fall on labels that carry several values for the text to count as read. Brackx's reading and English are kept as
partial readings. Contributed by Michael Brackx (@brackxm), issue #90. Write-up: docs/saintluc1586b.html.

A different cipher from **`saintluc1586`** (f. 43, 30 January 1586, George Lasry's key): that letter's table is not
this one, so the two are separate targets with their own pages.

## The documents

BnF Français 15572 (despatches to Henri III and Villeroy, 1586), Gallica ark `btv1b9061879d`, full-size IIIF images.

- **f. 260r-v** (canvas 268 right, 269 left; foliated 260, older 274 struck through): St. Luc (François d'Espinay de
  Saint-Luc, governor of Brouage) to Henri III, 26 lines of cipher on the recto, 29 on the verso; the close in clear,
  *De Brouage, ce … de Juing 1586*, signed St. Luc. New item: not in the catalogue, the README or DECODE as far as found.
- **f. 245r-v** (canvas 253 right, 254 left): another St. Luc letter in the same table. f. 245v has a clear letter, then a
  12-line cipher block with a contemporary decipherment in the margin and letter glosses over part of it (crib 1);
  f. 245r has two cipher passages with margin decipherments (crib 2). `texts/f245_cribs.md`.

## Files

- `brackx2026/f260_cipher.txt`, `brackx2026/f245_cipher.txt`: Brackx's sign-by-sign transcriptions (labels).
- `brackx2026/key_r3.json`: his round-3 key (label = values; `+` = null).
- `brackx2026/label_legend.md`: label, sign shape, values, count on f. 260.
- `brackx2026/f260_decryption_lines.md`: each line's transcription, raw decryption and reading.
- `texts/reading_f260r.md`, `texts/reading_f260v.md` and `_en.md`: his reading in the writer's spelling, every unread
  run sized (`[?]` one word or group), and English with the same holes.
- `texts/f245_cribs.md`: the margin decipherments.

## The key

Tomokiyo, cryptiana henryiii page, "St. Luc's Cipher", gives the table and reads only the opening line of f. 260.
Brackx's corrections, each from a crib or at least two contexts with a shape check: Δo = *Monsieur du Mayne*,
ʞ = *pour* (crib 1); ⊔ = *la Rochelle* (listed as a null before; three contexts); a small hooked ɣ = *ss* (19 contexts,
crib 2 *asseurer*); ɑ with a raised stroke = *la*; Ↄ = *rr*; ʒ with a crossed tail = *h*; plain 3 = *m*; ♀/♁ = *n*/*p*;
a ♀-like sign = *x* (crib 2 *extrême*); ŧ̶ also *r*; π/ϖ also *s*; `q` = *e*.

What keeps it from reading: many labels still carry two to four values (z = u/v/h/m, 9 and 9q = n/m/g, S = m/s/g/mm,
f = c/s, p = i/r, 6 = s/y, y = n/d, d = l/c/p, t and tb = p/t/v/r, pi = f/s), and the decoder chooses among them with a
French model. Letters on such labels are **40.5% of f. 260r and 34.5% of f. 260v**. The f. 245 decipherment confirms
the values as part of the key, not each choice on f. 260. They are most likely look-alike shapes merged in
transcription; the README's look-alike limit is 3%.

## Measured (24 Oct 2026)

`research/reading_audit/v10_relabel.measure` on the readings (`[?]`, `[?word]` and supplied `[word]` count as holes):

| page | words | read share | multi-valued letters | state |
|---|---|---|---|---|
| f. 260r | 197 | 0.761 | 40.5% | decoded, not read |
| f. 260v | 275 | 0.851 | 34.5% | decoded, not read |

Brackx's own figures (#90): 75.4% / 85.3% read as sense; crib agreement 89.3% (f. 245v) and 83.2% (f. 245r); corpus-word
coverage 79.2% / 80.7% against shuffled-key controls of 27-46% / 31-49% (label value sets reassigned, sizes kept). Where
his reading departs from the decoder it always takes another value of the same label: 12 of 970 letters on f. 260r,
10 of 1,292 on f. 260v. The posted control ranges of the original issue (18-37%, 20-35%) could not be reproduced by him
and are withdrawn; his first model mixed Montaigne with an Italian and a Middle English text and was rebuilt.

## What it says (Brackx's reading, partial)

Brouage under the Rochelais fleet, June 1586. A Rochelais commander *arriua [?hier] en Olleron* and watched his galliots
attack the Brouage shallops, answered by the fort's guns. St. Luc has sent to Monsieur du Mayne to ask whether help can
be given. The Rochelais try to block the harbour with ships loaded with stone, one of *six uingts [?toneaux]*; the
defenders work by the tide and took one of the ships. The garrison is unpaid and murmurs; no word of the King's
commands since his letters of April. La Rochelle means to keep the sea and sell passports to its captains. And a thing
*de tres grande importance*: the council has let the farmers *du grand parti* take salt at La Rochelle, which feeds the
town's passport duty; he asks that French merchants be forbidden to take salt there *a peine de confiscation de corps
et de biens*.

## Remaining gaps

- multi-valued labels on f. 260r-v (40.5% / 34.5% of letters) - blocker: not-attempted for S, f, y, d, t/tb, pi; the four largest (ϙ `9`, ʒ `z`, б `6`, ρ `p`) were split-tested by shape on the full-size images and do not split (issue #95, below), so for those the blocker is no-key-material: a contemporary decipherment of f. 260 or another letter in this key
- open runs: f. 260r r. 1-2 (the places after *en son*), r. 5-11, r. 13-14, r. 17, r. 19-24; f. 260v v. 3 (the day in April), v. 4, v. 8-9, v. 12-18, v. 23, v. 27 - blocker: not-attempted; retry after the label split
- Π (`P`) taken as a null where *affaire(s)* needs *ff* (v. 25, v. 27); two signs after *n'oze* in crib 2 - blocker: not-attempted; image check

## Escalation

- [x] siblings: f. 245r-v (same table, margin decipherments) used as cribs; f. 43 is another table (saintluc1586)
- [x] clear-pages: f. 245v's clear letter and margins are the only clear material found; no clear copy of f. 260 looked for beyond Brackx's search
- [x] known-keys: Tomokiyo's St. Luc table is the key; Lasry's f. 43 key does not apply
- [x] print: Tomokiyo reads the opening line only; no other reading found by Brackx (web search) or here
- [ ] key-rebuild: label split by shape not yet done (see gaps)
- [ ] retry: after the split

## Shape test of the four largest multi-valued labels (Brackx, issue #95, 23 Oct 2026)

Every token re-located on the full-size images (canvases 268, 269) by template matching and cut into contact sheets
grouped by decoded value:

| label | tokens (decoded value) | shape | split? |
|---|---|---|---|
| ϙ `9` | 126 n, 12 m, 12 g | a ring on a straight stem in all three groups; one g token (r. 10) has a short stroke at the foot | no |
| ʒ `z` | 117 u, 15 m, 5 h | a flat-topped 3 over a descender ending in a q-like loop; m and h look like u | no |
| б `6` | 161 s, 32 y | a b-shape with a flag at the top, the same for s and y | no |
| ρ `p` | 125 i, 17 r | a small bowl on a straight stem; a short bar across the stem occurs with both values | no |

Only part of each minority value could be located cleanly (4 m and 1 h of ʒ, 4 g and 3 m of ϙ, 6 y of б, 7 r of ρ),
so a rare variant could still be missed. The look-alike share stays 40.5% / 34.5%; both pages stay decoded, not read.

## Log

- 22-23 Oct 2026: Brackx, issue #90 (solution post and reply of 23 Oct with the reading, English, line-by-line decode and
  label legend).
- 24 Oct 2026: taken in as a new target; measured; graded decoded, not read on the look-alike limit; profile, page,
  ledgers and DECODE note (no DECODE record known).
- 23 Oct 2026: Brackx's shape test of ϙ, ʒ, б, ρ (issue #95): none splits; recorded above.
