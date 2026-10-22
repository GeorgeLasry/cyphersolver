# BnF Espagnol 318 no. 95: an unaddressed Spanish cipher letter, 8 Jan 1497 — George Lasry's alphabet

Split on 14 Oct 2026 from `esp318` (the whole volume, catalogue no. 9) under the one-key rule (George Lasry,
14 Oct 2026). This letter is the only one in the volume in Lasry's 2022 alphabet; the other ciphered letters of
Espagnol 318 are different ciphers, each with its own entry and page: [`targets/esp318/`](../esp318/NOTES.md)
(no. 92, the *Cifra general*), [`targets/federico1497/`](../federico1497/NOTES.md) (no. 5, Escrivà's cipher),
[`targets/esp318no93/`](../esp318no93/NOTES.md) (no. 93, key not identified), [`targets/esp318no94/`](../esp318no94/NOTES.md)
(no. 94, alphabet recovered by Michael Brackx).

**Outcome (22 Oct 2026): key recovered from ciphertext-only by George Lasry; recto deciphered in full** (PR 75).
George's CTTS key (2021-22, revised 2026 with Claude Opus 5.5) gives every one of the 1,245 recto symbols a value;
five name code groups are unidentified and three readings tentative. The verso's four cipher lines are Michael
Brackx's reading ([issue #63](https://github.com/dbourdeau/cyphersolver/issues/63)) with the same alphabet. Before
PR 75: Lasry's approximate ll. 1-13 (2022), Brackx's ll. 14-33 and verso, and the project's machine reading of about
two thirds of the recto (Sept 2026), all kept below as history; `f122_reading.md` is the pre-PR-75 combined text.
Sessions of 17 and 21 Sept and 21 Oct 2026.

The segmentation pipeline built for this letter, its outputs and its git-ignored intermediates stay in
`targets/esp318/`, run from there (shared with no. 93, whose glyphs it also segmented): `seg.py`, `glyphs.py`,
`cluster.py`, `montage.py`, `assign95.py`, `localseg*.py`, `viterbi95.py`, `hybrid95.py`, `linedp95.py`, `band95.py`,
`reseg.py`, `solve95*.py`, `lm.py`, `f122r_*.txt`, `f122r_*.pkl`, `f122v_reseg.pkl`, the strips in `ov/` and the scans
`full/f122r.jpg`, `full/f122v.jpg`. The line-by-line reading `f122r_reading.md` moved here.

## The letter and the key

F. 122 is a single leaf of 31 dense lines by the segmentation (33 line bands as Brackx cuts them) and four cipher lines
on the verso above a clear date line and signature (canvases 458–459 of ark `btv1b52503046q`); no address, no
salutation, dated 8 January 1497, three days before Federico's no. 5 at the other end of the volume.

Solved "approximately" by George Lasry in May 2022. Tomokiyo's page of Lasry's solutions (saved as
`targets/esp318/lit/crypt/GL.htm`) carries **two** images, both now kept beside it in `targets/esp318/lit/crypt/GL/`:
the alphabet (`BnF_es318_f122.png`) and **his decipherment of ll. 1–13** as a red overlay on the scan
(`BnF_es318_f122_decipher.png`, "provided by George Lasry"). Until 21 Oct 2026 these notes said no plaintext had been
published: that was wrong, the second image was missed (Brackx pointed it out). The alphabet is homophonic, one to
three signs per letter, plus unassigned signs and the code groups `bac bnh bon dah daf dae oht bed dal boo del`.

## George Lasry's complete recto (PR 75, 22 Oct 2026)

`lasry2021/` holds his CTTS project (transcription of the three overlapping photographs f122a-c, key, decryption and
edited readings), `CONTRIBUTION.md` (Spanish edition, English translation, notes, context) and two images. Key: 21
letters with 43 invented signs (one to four each), 11 code groups written in letters, three special signs
(`lasry2021/ctts/key.txt`). In 2026 he corrected two values (small solid circle = Z, not B; the l-shaped sign = R, not
S), read the code groups from context (bac ciudad, bon gente, bnh rey, dae papa, bcd cardenal; dif rey de romanos?)
and left five names unidentified (dcl, dah, dal, dnl, boo). CTTS writes some groups as bcd, dcl, dif, dnl where
Brackx read bed, del, def, dhl. The full reading is `reading.txt`.

His recto agrees with Brackx's ll. 14-33 (and adopts his *avemos traido aca*), except *rogaria a los que le ruegan*
(Brackx *logaria ... llegan*), *para que* (Brackx *parece que*) and *Claver avra* (Brackx *Claue haura*). It agrees
with every correction Brackx proposed to Lasry's 2022 ll. 1-13 (*no ay que dezir*, *remitiendome*, *hazen*, *diz*,
*con palabras*, *haga*, *no buen estado*), which therefore stand.

Checked here (22 Oct 2026):
- `decode.py` re-applies the key: 1,323 transcribed symbols, of which 78 are the last two lines of f122a photographed
  again at the top of f122b (the two transcriptions of those lines differ in a few signs: *toca/tocad*, *no uen/no
  buen*, *amicer/amier*); 1,245 counted once = 1,224 letters + 2 nulls + 19 code and special signs, none unassigned.
  George's count is 1,245.
- `docs/_validate.py` (model `es-golden-age`, codes left unread): reading -1.960 per letter; random keys -6.156 (z
  8.5); key fitted to shuffled text -3.514 (z 36.7); annealer on the real text -2.095. Verdict: pass.
- The f122c overlay compared by eye with the decode: the code groups `dal` and `bnh` and the letters around them fall
  where the decoder puts them.

## Lasry's ll. 1–13 and Brackx's reading (21 Oct 2026)

Lasry's decipherment of ll. 1–13, transcribed from his image, is the reference reading of those lines. Brackx read
the rest by eye with Lasry's alphabet on 1.5–3× crops, each doubtful word re-cut and re-read (about seventeen
passes), adopting a new sign value only when it made sense of two or more independent words. No solver and no
language model; the project's machine segmentation was not used. Both are in `f122_reading.md`.

In outline: grain is getting dear; the French bring victuals and offer the silk-makers, "a third of" `[bac]`, licence
to trade in France, to win `[bon]` over; `[bnh]` provides "very late and very little"; the Señoría leans to the
French. Juan Luys has been brought over; `[def]` treats daily with "those who govern"; they hide from `[bnh]` and
bear him ill will, and the writer hinders the harm to `[bnh]` as he can. `[dae]` wants the `[bed]` of Santa Cruz to
go to France to seek peace; the League should do its duty; `[dal]` should order `[boo]` to come and defend "this",
for if it were lost "no auia cosa segura en Ytalia". The verso: `[def]` has gone to Germany (*Alemanna*) without
anyone knowing, with no hope of his return. Brackx's suggestions for the groups (contextual, not read): `def`
Maximilian I, whose withdrawal from Italy in December 1496 fits; `bed` cardinal (Carvajal, of Santa Croce); `dae`
the Pope?

**Proposed corrections to Lasry's ll. 1–13** (Brackx; pending George Lasry, who has not yet seen them; his reading
stays the reference on the site). Compared here with the image itself, letters only:

| l. | Lasry 2022 | Brackx proposes | checked here on the scan |
|---|---|---|---|
| 1 | first sign *i* | null (large ꝺ-shaped sign) | no |
| 1 | *no a lo ve debir* | *no ay que dezir* | no |
| 1 | *[r]emitiendo e* | *remitiendome* | no |
| 5 | *haben* | *hazen* (*la seda*) | yes |
| 8 | *dib* | *diz* | yes |
| 10 | *con la ladras* | *con palabras* | yes |
| 12 | *hama* | *haga* | yes |
| 13 | *no ven estado* | *no buen estado* | no |
| 13 | *i a ices* | *y* + null + one unread word | no |

The issue's table also lists ll. 7, 8, 9, 10 as corrections where Lasry's overlay only leaves a blank over the code
groups `bon` and `bnh` (written in clear letters on the leaf) or has the same text (*provee como suele mui tarde*);
those are not differences. Brackx confirms ll. 2, 3, 4, 6 as Lasry has them, and Lasry's two 7-forms (crossed 7 = S,
plain 7 = D).

**Sign values proposed for Lasry's "Unknown" signs** (Brackx; for Lasry's review): ∝-like alpha = l; b-bowl with two
crossbars = z; 8-shape = a; hooked lightning variant = d; `9.` = *con* or null; ꝑ = h in *haura*; and, not in
Lasry's table, the small solid circle = z, a two-crossbar stroke that doubles the preceding consonant, and a π/o sign
with two crossbars = o. `dah` (l. 23) and `dal` (ll. 29, 31) are different groups; `oht` was not found.

**Checks here (21 Oct 2026).** Recto ll. 5, 8, 9, 10, 12, 25–26 and verso l. 2 were deciphered sign by sign from
the scan with Lasry's table: *los que ha[z]en la seda*, *con la mas [bon] que pueden*, *provee como suele muy tarde*,
*con palabras y la*, *a que el [bnh] haga*, *dificultad. Y el [dae] di[z]…*, *-ta Cru[z]*, *y del [def] no se que
siga, sino que esta en Alemanna* — all as Brackx has them. Where his lines overlap the project's September machine
reading they agree (ll. 15, 16, 17, 18, 19–20, 22, 23, 25), except that our l. 12 *me toca* is *le toca* (Lasry and
Brackx agree). Not checked: the remaining lines of 14–33 sign by sign.

## Lasry's key applied by machine and checked by eye (Sept 2026)

Reading the signs by eye alone was not reliable (÷ against ≐, plain 7 against ᵒ7 and crossed 7), so f. 122r was
segmented and clustered: adaptive-threshold binarisation (`seg.py`), connected components grouped into glyphs by
x-overlap with diacritics attached (`glyphs.py`: 963 glyphs on 31 lines), Ward clustering of 28×28 bitmaps
(`cluster.py`, `montage.py`), the clusters labelled from the montages against Lasry's key (`assign95.py`). The clean
clusters carry 64 % of the glyphs and their frequencies are Spanish to the letter (E 9 %, A 7 %, O 5 %, N 5 %, S, C,
U, R, D, M, T, I, Q ≈ 1 %). The rest — two signs touching, or a sign cut by a descender from the line above — is
re-explained by FFT correlation against the cluster templates (`localseg2.py`, `viterbi95.py`), and a beam search
over a 5-gram Spanish model (`lm.py`, Don Quijote) fills those boxes while the verified glyphs stay fixed
(`hybrid95.py` → `f122r_hybrid.txt`, where `~` marks model-filled positions). Annotated strips with the machine
letter under each glyph (`ov/A95_NNa|b.png`) are the instrument for checking it.

Checked by eye on the strips, with Lasry's key, the following read cleanly (line numbers of f. 122r):
3 *…r. Despues…*; 4 *…emos franceses…* (the y-with-crossbar is F, as in his key); 6 *[bac] que puedan merc[ed]…
[de] Francia…* (the dotted x is his *p*); 8 *…con esto…*; 11 *Señoría … que esta … por*; 12 *que me toca… mucho…
será… que [bnh]… haga* (the group `bnh` written in clear letters mid-line); 13 *con esto… acorde… lo bueno…*;
16 *…que go[u]ierna[n]… pero*; 17 *…muy grandes cosas … no creo que…*; 19 *que se … encubre … que … quieren*;
22 *por obra creo que … amigo*; 23 *escreuir a…*; 25 *dificultad … en los…*. The letter is Spanish, in a court hand
of the 1490s, about the French — *franceses*, *Francia* — and about what a *Señoría* (Venice?) can or cannot be made to
do; `bac` and `bon` are nomenclator groups. Two of Lasry's signs were corrected on the way (the n-with-cross-tail is
M, not Y). His two 7-forms — plain 7 = D, 7 with a small o = S — are confirmed by *puedan* and *franceses*, and the
clusters separate them where the eye at this resolution does not.

A word-segmentation pass over the hybrid decode with a Spanish lexicon (`f122r_words.txt`, non-words bracketed) is the
honest measure of where it stands: only the eye-checked stretches segment into words. The line-by-line result is
`f122r_reading.md` (here): every line has verified stretches, the nomenclator groups are located (`bac`, `bon` ×2,
`bnh` ×4, `dal`, `bed`?), and lines 19–20 give *…quieren go|uernar…* across the line break. It is a reading of
perhaps two thirds of the signs, not a text.

Two further mechanical attempts did not help: clipping every glyph to its line band (`band95.py`) cut the tall signs
in half; a segmentation-free DP tiling (`linedp95.py`) reads the same lines the eye did and no more, and its language
model writes Don Quijote over the uncertain tiles (*don quiiote que el que*). Three independent readings (eye,
cluster-hybrid, tiling) agree on the same two thirds and disagree on the same third. The limit is the sign shapes at
this resolution, not the method.

## Remaining gaps

- five name code groups (dcl, dah, dal, dnl, boo; Name1-Name5 in Lasry's key), one occurrence each - blocker: open-codes; no other letter in this key is known, context suggests persons but does not name them
- tentative readings rey de romanos? (dif, x2), aunque? (oN), y? (9) - blocker: too-short; one or two occurrences each
- *en al* in l. 20 - blocker: illegible; a burn hole according to Brackx, one image only
- the clear date line and signature of f. 122v, read only as "… de enero …" - blocker: illegible; faded clear hand, not cipher

## Escalation

- [x] siblings: all thirteen cipher folios of the volume opened; no other letter in this alphabet, no decipherment of f. 122 anywhere in the volume
- [x] clear-pages: none; the cipher pages have no clear word
- [x] known-keys: Lasry's 2022 alphabet is the key; values proposed for his Unknown signs (Brackx) and two signs corrected here in Sept
- [x] print: cryptiana GL.htm: Lasry's alphabet and his decipherment of ll. 1-13 (the second image was missed until Brackx's issue #63); nothing else in print
- [x] key-rebuild: cluster labelling, FFT template re-explanation, beam search and DP tiling (Sept); Brackx's sign values for the Unknown row, each from two or more words (Oct)
- [x] retry: Lasry's revised key re-run over the whole recto (PR 75, every symbol assigned); Brackx re-read every doubtful word over about seventeen passes and withdrew conjectures that failed (Ingalaterra, a value for ŧ); seven passages re-deciphered here from the scan agree

## Next step

Answered by PR 75 (22 Oct 2026): George's complete recto replaces his 2022 overlay as the reference and agrees with
Brackx's corrections. Open for George: whether the verso (four cipher lines, Brackx's reading) should be added to his
CTTS project; whether *en al* (l. 20) is a burn hole.

## Assumptions for George's review

- Your 2026 recto (PR 75) is now the reference reading of the whole recto; the 2022 overlay and Brackx's proposals
  are kept as history. The outcome is recorded as your ciphertext-only key recovery (CTTS), not as a known key.
- The verso stays Brackx's reading with your alphabet (issue #63).
- None of the other letters of Espagnol 318 carries your credit.
