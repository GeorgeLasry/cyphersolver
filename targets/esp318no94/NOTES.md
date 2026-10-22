# BnF Espagnol 318 no. 94: the viceroy of Sicily to Ferdinand, Messina, 27 April 1503 — alphabet recovered ciphertext-only and code partly read by Michael Brackx

Status: in progress (contributed reading, about 90 code groups open; the decrypt needs a line-by-line check against the scans)

Split on 21 Oct 2026 from [`targets/esp318no93/`](../esp318no93/NOTES.md), which held nos. 93 and 94 together as
"keys not identified, no shared key claimed". Michael Brackx (GitHub [issue #62](https://github.com/dbourdeau/cyphersolver/issues/62),
21 Oct 2026, worked with Claude Opus 5.5) recovered the alphabet of no. 94, read part of its code, and showed that
no. 93 is in a different key; the check below agrees, so under the one-key rule no. 94 is its own entry. The other
ciphered letters of Espagnol 318 have their own entries: [`esp318`](../esp318/NOTES.md) (no. 92, *Cifra general*),
[`federico1497`](../federico1497/NOTES.md) (no. 5, Escrivà's cipher), [`esp318no93`](../esp318no93/NOTES.md) (no. 93,
Lorenzo Suárez, key not identified), [`esp318no95`](../esp318no95/NOTES.md) (no. 95, Lasry's alphabet).

**Outcome: key recovered from ciphertext-only (contributed), read in part.** The letter alphabet is complete; about 20
code groups are firm and 14 tentative out of 113; the content is readable in outline.

Files: `ct94_brackx.txt` (Brackx's sign transcription, the C: lines of the issue, his ASCII labels), `check94.py` (the
review checks below), `validation.tsv` (pairs for `docs/_validate.py`). The scans stay in `targets/esp318/full/`
(`f120r.jpg`, `f120v.jpg`, `f121r.jpg`, `f121v.jpg`; Gallica ark `btv1b52503046q`, canvases 452–455).

## The letter

Four pages, ff. 120r–121v. Spanish, clear and cipher mixed: the clear islands carry the narrative joins ("y no poder
passar estava la galea de allá del Faro, donde llegó don Fernando de Andrada…", "en lo de la hazienda luego…",
"Puerto Carrero, Dios le aya el ánima"). Dated at Messina, 27 April 1503, the day before Cerignola and six days after
Andrada's victory at Seminara (21 April). F. 121v carries the superscription, the seal and the endorsement "Del
virrey de Siçilia en çifra". There is no decipherment in the volume.

## The key (Brackx, adopted with credit)

Homophonic: 39 sign classes for 21 letters (40 labels: `f`, unresolved, reads s). His ASCII labels for the glyphs are defined in the issue and in the
header of `ct94_brackx.txt`.

| value | signs |
|---|---|
| a | 3, O, o, p, q |
| c | F1 (single crossed f), W (otto ligature) |
| d | 2 (n with tail), T (crossed descender) |
| e | 4, b (t over b) |
| g | G (tall Ꞩ) |
| h | 8 |
| i | : (dots), P (curly thorn) |
| l | H, K |
| m | E (C with stroke) |
| n | 5 (small ƽ), S (long ss) |
| o | A (alpha), X, e (q with tail) |
| p | D (B with bowl), d (delta) |
| q | V |
| r | = (dash), I (triple minim), M |
| s | 7, 9, F2 (ff-stroke), L, Q, Z5, f |
| t | 6, t |
| u | B (ß), a |

The suspect classes were cropped from the scans and split by Brackx (254 n/g, s/c, s/y, p/b occurrences and 149
ß/thorn); the split classes, re-solved from scratch, came back to the same values. Sign `K` is unstable (l in the
final key, s in earlier runs).

**Code groups, firm** (several independent contexts each): `qa` que ×65, `rah` y ×61, `mny` de ×47, `qag` se ×32,
`mys` en ×23, `pif` no ×21, `nyb` lo ×20, `mnb` la ×17, `lux` como ×14, `malg`/`malh` the digraph *ll* ×14/×6,
`nae` los ×11, `pat` por ×10, `nyl` havía ×8, `qaz` V. Al. ×6, `gik` su ×6, `reg` yo, `mnh` gente, `qe` quando ×4,
`pns` Puerto- (in *Portocarrero*) ×2. **Tentative**: `mog` a?, `lik` buena, `pnb` antes/después, `pad` bien, `re`
esto, `mok` dar, `mas` el, `pit` contra/sobre, `leg` ellos, `nag` más, `neb` hazer, `per` para, `nob` dicho,
`mos` ellos. The firm readings break alphabetical order (`gik` su and `nyl` havía sort before `mny` de), so the code
is two-part and neighbours give no bracket.

`mny` = de matches Bergenroth's `muy` = de in his reconstruction of the Gran Capitán's *Gran cifra* (1501–04): *n* and
*u* are the same two minims in this hand. Most of the initials (m-, q-, n-, r-, p-, l-) also sit in the *Gran
cifra*'s band (h-, l-, m-, p-, q-, r-, s-, u-). No. 94 is in that key or a close relative.

## What it says (summary)

Brackx's normalized reading is in the issue; it is provisional word by word, firmer passage by passage. In outline:
the galley could not cross the Faro; Fernando de Andrada arrived and turned back; a night entry, the infantry
looting, stabbings among them, men surrendering *a merced*; Cardona named; a *pesquisa* under oath into those who
profited from the spoil; the captains told to guard the *ropa* and the prisoners; the camp at Rocca d'Angitola and a
shortage holding up the fleet; three principal prisoners well kept in the castle until the king orders; the dispute
over the post Portocarrero had given, after his death; Hugo de Cardona's following and its "presunción"; 800
*peones* sent; and an *elección* proposed among "tantos principales capitanes". Spelled out in cipher:
*puertocarero* (three times, once directly before the clear "Dios le aya el ánima"), *cardona*, *semenaoa*
(Seminara), *tienedonugo* (tiene don Hugo), *pesquisa*, *iuramento*, *presoneros principales*, *punsaladas*.

## Review (21 Oct 2026)

What the issue raised, and what was checked here (`check94.py`):

1. **Transcription.** f. 120r ll. 1–3 and f. 121r ll. 1–2 compared sign for sign with the scans: the sequence, the
   code groups (`rag re lux mog nyl pat mas qar qag lik pns`) and the class assignments as Brackx has them.
2. **The score.** Brackx's −2.61 nats/char against −1.91 for clean Spanish compares a noisy decrypt with a clean
   corpus. On the shared `es-golden-age` model (order 5, no spaces) his key gives **−2.59** on the letter-sign runs;
   the letter's **own clear islands** score **−2.23**; 200 keys with the same values shuffled score at best −4.48.
3. **Overfitting.** An independent anneal here (40 sign labels, letter-frequency penalty) from four random starts reaches
   his key in two (35 of the 40 sign labels agree, −2.58). The same annealer on the same signs in shuffled order reaches only
   −3.63 to −3.77. `docs/_validate.py`: **pass** (reading −2.35 with the firm code groups, random keys −4.58,
   shuffled refit −3.15, annealer power −2.37).
4. **Words.** Spanish words of four letters or more cover 0.63 of the decoded letter runs, against 0.77 for the clear
   islands and 0.10–0.13 under shuffled keys.
5. **Different key from no. 93.** Our earlier note listed no. 94's initials as g/l/m/n/p/r/v/z from a sample: the g-
   groups are Brackx's q- groups (`qag`, `qa`; the same 9-shaped letter), and his full count is m 184, q 139, n 82,
   r 76, p 73, l 47, g 11. Comparing inventories: no. 93's commonest groups (`gto` ×21, `pie` ×19, `heg` ×13,
   `zoe`, `zoc`, `hug`) never occur in no. 94, and no. 94's (`qa`, `rah`, `mny`, `qag`) are absent from no. 93's
   stream except `pif` twice. `muy` does occur in no. 93, three times in 1,016 signs, where no. 94 uses `mny` 47 times
   in 612 groups: if it is the same group, it is the one overlap, not a shared code. Brackx also found that no. 94's
   alphabet makes no. 93 worse. Split.

## Remaining gaps

- about 90 code groups, 143 tokens, mostly once or twice - blocker: open-codes; two-part code, no alphabetical bracket; nouns, names and verbs that context does not fix; the Gran cifra list (BNE MSS 20.211/52) and the 'Cifra del visorrey' (BRAH 9/15 ff. 1-6) are not online
- 14 tentative code readings (93 tokens) - blocker: open-codes; one or two contexts each
- spelled-out stretches that do not parse (about a fifth of the letter-sign text) - blocker: open-codes; single misread glyphs in a transcription by eye; a third of the ß/thorn/B glyphs not cropped and checked; sign K unstable

## Escalation

- [x] siblings: all thirteen cipher folios of Espagnol 318 opened; no decipherment of no. 94; no. 93 is a different code (see Review 5)
- [x] clear-pages: the clear islands of no. 94 itself are the context Brackx read the code from; no clear copy
- [x] known-keys: Escrivà no. 1 and the Cifra general excluded by code initials; Bergenroth's Gran cifra agrees on mny/muy = de, his full list not obtainable (BNE bot-check)
- [x] print: Parisi 2004 and 2020, Galende Díaz 1994, Tomokiyo, Quirantes 2018: nothing on no. 94
- [x] key-rebuild: Brackx's ciphertext-only anneal and class splitting; reproduced here from random starts (Review 3)
- [x] retry: Brackx ran three rounds over the code groups with the improving key (round 3 moved `mys` from la to en and `mnb` to la, revised `nyb` from assí to lo, withdrew `mos` = fueron) and cropped the suspect sign classes from the scans (254 + 149 occurrences, a third of the ß/thorn/B missed) and re-solved the split classes from scratch; the open groups were retried in each round. Still to do, not blocked: re-transcribe the non-parsing stretches against the scans with the final key

## Assumptions for George's review

- The result is Brackx's (provenance contributed); the project's part is the review and the split. It stays out of
  the paper data.
- The split rests on code inventories, not on a reading of no. 93.
