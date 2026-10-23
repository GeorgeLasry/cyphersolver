# V2831 fourth pass (r2l, 23 Oct 2026, Claude Opus 5.5): language-model segmentation and p. 3 re-crop

Task: the letter groups of V2831 that decode letter for letter with R5411 but had not been split into words (NOTES
Remaining gaps: p. 1 L04, L11, L12, L22, L24; p. 2 L09, L15, L16 and ll. 18-31; p. 3; p. 4 L02).

## 1. Segmenter (shared lang/ model)

- `research/reading_audit/r2l_signs.py` turns a sign string (notation of `trans/*_r2e.md`, `*_b25.md`) into a lattice: each
  sign gets the key value first, then the other values it has carried on this letter (o-form b/t, d l/s, s c/u, 8 g/n,
  6 u/v, x̄ ma/et, ρ n/ff, L to/h ...) and its look-alike readings marked (g read x or h, 3 read r, ε read b, 6 read o).
- `research/reading_audit/r2l_seg.py` enumerates the lattice (beam 4,000 by the no-space model), segments every string
  into words (k-best dynamic programme on word frequencies of the it-cinquecento corpora it-renaissance + it-nunziature,
  plus the words of the letter's own read parts), and ranks the candidates by the lang/ model **it-cinquecento**
  (character 5-gram, spaces, early norm) over left context + candidate + right context, with costs for a second value
  (1.5), a null (2.5), a look-alike (3.0) and an out-of-vocabulary word (9.0). Nothing is inserted: every candidate
  letter comes from a sign. No target-local model was written.
- 79 groups (`research/reading_audit/r2l_buda_raw.txt`); output in the session scratchpad (`reread/r2l/seg1.txt`).
- Adopted only where the top candidate reads as sense in its sentence and every letter is carried:

| page/line | signs | adopted | values used |
|---|---|---|---|
| p. 1 L09 | o 4 8 | ben (disposto) | o = b (key), 8 = n |
| p. 1 L13 | n g // d | in el (tractare) | key values |
| p. 1 L18 | // c d r | epsa (liberamente) | d = s |
| p. 1 L24 | c ε b r x̄ b^o | poco amano (da Regina) | x̄ = ma (key) |
| p. 2 L09 | d s o n 6 v d 4 | subiunse | d = s, s = u, o = b |
| p. 2 L23 | b ρ | con (inconveniente) | ρ = n (p. 2 value) |
| p. 2 L29 | xo d n x n | ma[…] li di passati | xo = ma, the rest key values |
| p. 2 L31 | 9 r n n# n 8 v r o n | ha assignati | first n taken as the dotted 1 = a (look-alike, counted) |
| p. 3 L11 | d // g r o // g | le [?ha] ben (veduto) | g for h (look-alike, counted; as hanno, honore on p. 2) |
| p. 3 L11 | d // g o-bar n q^o | sentire (fructo) | d = s, q^o = re |
| p. 3 L13 | d // b^e b^e | (excusar) se ne, ne | d = s |
| p. 3 L14 | d 4 z r d E b^e | le rasone | d = l, then s |
| p. 3 L25 | b̶ d 6 a v ñ // | calumnie | key values, ñ = i |
| p. 3 L27 | n 8 r 8 L: | inante | 8 = n |
| p. 3 L30 | o r d o-bar n | basti (l'animo) | o = b, d = s |

- Not adopted (top candidates are not sense): p. 1 L03 (lauo), L04 (mintimariteglione; enti et pio ne; uon an erire),
  L08 (ncercassuno), L11 (na con epse siia e re), L12 (coti bei eo im), L14 (single 6), L17 (in en), L19 (ait in io a),
  L20 (fi p la), L22 (di m p enrico a; capit duol), L25-L29; p. 2 L09 (care), L15 (vimmobile, uico, ui sane), L16
  (d nome ne touit), L19, L21, L25, L28, L30 (cauti); p. 3 L02, L03 head, L05 (corsi core tante; care glie), L06
  (sgano), L08 (a la ii), L09 heads, L15, L18 (sig ma), L19 (mise a s su), L21 (prome amplis si), L22 (lio in), L28
  (te e), L29 (ir), L31 (les non e); p. 4 L02 (u manda caiuno nicolo iuncho: "manda" and "Nicolo" are tempting, the
  rest is not, kept unread).

## 2. Page 3 re-cropped at full resolution

The Vestigia plate `img/v2831_p3r.jpg` (3240x4320, the original; DECODE serves the same negative) re-cut row by row
(`research/reading_audit/r2l_crop3.py`, copy of b25_buda_rows3.py, and `r2l_zoom.py` for 2.2-3.2x zooms of single
groups; the left ends of the rows sit about 60 px above the block-3 row centres, which is why some b25 crops mixed
lines). Lines looked at: L02, L03, L05, L08, L09, L19, L20, L23-L31. Findings (all in `trans/v2831_r2l_corrections.tsv`):

- **L03** "con li ochi [?aperti]": ε s 9 n = o-c-h-i, r c // ʒ o-bar n = a-p-e-r-t-i, with one n̶-like sign between
  them not accounted for (so [?aperti]). "**L'invito facto** ad [mes]sere Francesco ... e proceduto da la Regina": the
  b of b25's "b s o-bar 3" is crossed at the top, the key's Fa: fa-c-t-o; d n g 6 n p̸ ε = l-i-n-v-i-t-o.
- **L05** "ad fine **per quanto** si po cognoscere": the sign b25 read c (p) has a dot inside: the key's q (reversed
  c with a dot).
- **L08-L09** "volerli **persuadere** che": L08 ends c // ʒ (per) and a null, L09 opens with m with a ꝑ-tail (the key's
  su) + r x // q^e (a-de-re); b25 had "a" (m).
- **L19, L20, L30, L31** the b̶ of b25's "care" is crossed at the top (ƀ = fa): "quello che havera **fare** ad Roma",
  "**fare** intendere **al Papa**" (the single sign after "al" is the Papa sign; Fa is its near shape, counted),
  "basti l'animo **fare** iuditio", "che vole **fare** questo Ser.mo Re con el Turco".
- **L23-L24** "con tale modestia che **non [?venga] a alienare l'animo del pontifice da se**": L23 ends 8 ε v 6 // 8 q̄ r |
  r d n // (n-o-n v-e-n-ga a a-l-i-e) and L24 opens b^a q^e (na-re) + d r g n a 3 (l-a-n-i-m-o; b25 had x 8 n r a 3).
  The q with a bar is the key's ga; doubtful on the crop, so [?venga].
- **L24** "**Tertio, in iustificare** lo Vescovo Varadino": o-bar // ʒ o-bar n ε = t-e-r-t-i-o (b25 counted the ʒ twice,
  as z and 3), n 8 = i-n, n 6 d o-bar n d: b̶ ʒ // = i-u-s-t-i-fi-ca-r-e.
- **L25** "de le **calumnie** che li sono date apresso **el Papa, offerendoli de mandarlo li**": the sign b25 read b̶
  is a b with a crossed stem and a dark bowl (Papa); ε n p̸ // ʒ 4 v x ε d n = o-ff-e-r-e-n-d-o-l-i; there is no gap
  after it (b25's "… | d n" was a mis-cut); x // a r g x 1 ʒ d 3 = de mandarlo (the dotted 1 = a, b25 had n).
- **L26** "per far li piu chiara de la **innocentia** sua": b25's string doubled the head of the group (7 … z 7 r z); the
  crop shows c // ʒ 7 r ʒ d n c n 6 (per far li piu); n g v ε s 4 v p̸ n r = i-n-n-o-c-e-n-t-i-a.
- **L27** "la quale **cosa** quando": plain b (co) + m^a, not b̶; the next group a ρ n# 4 | r n̶ 4 | c p̸ r o-bar r (m-?-ss-e
  a-tt-e p-t-a-t-a) is not read ("acceptata" would need n: = cc).
- **L29** "[…] non […] **sento d'avere** tante ingenio": d // 8 o-bar 3 = s-e-n-t-o, then a looped x (the key's second d)
  + r 6 // q^o = d'a-v-e-re; the lone x before "sento" is not read.
- **L30** opens with a dash null (∸) before "basti".

## 3. Score

`research/reading_audit/v2_score.py v2831_p2p3_r2l_reading.md it`: **explicit holes 0.636 (35/55)**, plain 0.491, hole
rate 0.121 (before: 0.466 / 0.293 / 0.164). By part: p. 2 ll. 18-31 0.611 (11/18), p. 3 0.649 (24/37).
The read part (`v2831_r2e_reading.md`, with the five r2l words): 0.698 (37/53), before 0.642.

**Look-alike letters.** b25 counted every shape choice on p. 3 (z/3, 8/9/g, s/6, q/q^e, b/d, dotted i ...), 59 letters,
including values that the original key R5411 later confirmed (dotted i = a, plain o = b) and values adopted across the
whole letter (plain q = e at every occurrence). Counted by the brief's definition (a letter that rests on the other
member of a look-alike pair rather than the figure's own value), from the b25 per-line notes and this pass: p. 2
ll. 18-31 17 (experientia 4, hanno/honore 2, the round 3 for r and Papa against Fe 5, [?quanto] and [?ha] 4, habia 1,
assignati 1); p. 3 16 (contrario 1, fa con arte 2, passira 2, excusar/excusatione 2, favore 2, Santita 1, venga 2, le
[?ha] 1, al Papa 2, Ra 1): **33 of about 1,800 decoded letters, 1.8%**; 15 of them sit inside [?word] holes. Separately,
the o-form is read t against the key's b about 40 times (the key's T column is torn; the value holds across the letter,
listed, not counted as a look-alike). The p. 3 per-line counts that b25 gave without reasons were not re-checked sign by
sign; their reasons, where given, are key-value choices.

**Decision: set read, grade B** (0.636 explicit-hole above the 0.60 bar; sentences hold in p. 2 ll. 18-27 and in p. 3
from L09 to L26; look-alikes 1.8%). Still fragmentary: p. 2 ll. 28-31 between the secure words, p. 3 L01-L03 (head),
L05-L08 middles, L27, L29 and L31 tail.

## 4. What stays open, and why

Every group listed under "Not adopted" has now been tried sign by sign (three passes) and through the segmenter with
every alternative value: they decode letter for letter but give no Italian word under any combination of the key's
values. What is missing is the value of the signs the torn columns of R5411 held (T, U/V, X, Y, Z, &, part of the
syllable rows) and of the signs not in the key (r̥, the n̶ in "ochi … aperti", the lone x on p. 3 L29): blocker
no-key-material. p. 3 L15 (blot) and the stained right ends of p. 1 ll. 21-29: illegible.
