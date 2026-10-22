# ff. 196 / 201: reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`. Leaf name f196_201, one reading for both encipherments. Scratch scripts (alignment, joint
decode, forced alignment, image crops) were kept outside the repository; what they established is recorded here.

## Before

`python docs/_check_reading.py --file` on the mechanical decodes with the merged key:

| file | sentences clean | share | hole rate |
|---|---|---|---|
| `texts/f196.txt` | 3 / 22 | 0.136 | 0.205 |
| `texts/f201.txt` | 10 / 23 | 0.435 | 0.157 |

## Pass 1: align the two copies, decode jointly (worked)

Brackx's `f196_cipher.txt` (975 tokens) and `f201_cipher.txt` (972) aligned token by token (Needleman-Wunsch; same
label +3, label sets that share a letter +1, else -2; gap -2). The two copies use the same figure in most places, as
`f196_f201.md` had suspected: they are two fair copies of one enciphered draft, not an encipherment in depth. They
agree from the opening of f. 201's cipher to *pour le regard dudict siège* (f. 196 l. 29, f. 201 l. 26); there f. 201
switches to clear for one clause, and from then on the copies run in parallel only loosely.

Each aligned column was given the intersection of its two letter sets (the union where they were disjoint) and the
whole was decoded with this project's beam and 6-gram. Result, without any correction: lines 1–28 of f. 196 read as
continuous French with breaks of one or two letters (*il a depuis qu il a est ariue … qui lui a cause la fieure la
que le comme ie cro … cependant uoulu failardeusenaduertir ig de peur que cest aduis uous uenant de quelque autre
part …*). This was the decisive step: a figure that one copy misreads is usually read right in the other.

## Pass 2: hypothesise the plaintext, force-align, list the conflicts (worked)

The plaintext was written out from the joint decode and forced back onto f. 196's figures (each figure must emit a
letter of its set; substitution, null and missing figure cost 1–1.2). 63 conflicts on 975 figures with the merged
key. Each conflict was looked at on the image (openapi.bnf.fr IIIF, canvas 203 / 208, full resolution, 3–4 line
bands, single figures enlarged).

What the images showed (details in `brackx2026/corrections/f196_201.tsv`, 49 rows, 46 label changes):
- **Split and merged labels.** `dd e` is one figure *de* (t); Brackx's `he` is twice an *h* followed by *e*
  (*mercy*); `om` is three times *o m* (= *it*: *partiroit*, *avoit*, *estoit*), not the *om* ligature (q) of
  *quasi*; `76` is twice the figures 7 and 6 (*on*: *Matignon*, *Montberault*, *mondict*), not code 76; `47` before
  *-nsieur* is the 4-shaped m figure plus 7 (*Mon-*), not code 47; `6 8` is code 68 (*V. M.*); `y c` on f. 201 l. 26
  is one figure.
- **Figures under a shared label.** Brackx's `pl` covers a 4-shaped figure (m, s, i: *reume*, *mauvais*,
  *sitost*, *ja*) and a large plain cross, which is c (*accès*, *accident*) and e (*espère*, f. 201 *besongne*). New
  labels in `key_cipher1_f196_201.json`: `cr` (cross), `8e` (an open 8-shaped e, distinct from the numeral 8), `ps`
  (p with a curl, s: *accès*, *près*, *soulagés*), `ca` (c with a stroke, a), `tp` (t with a lower loop, p); `u` = q
  (*quand*, both copies), L also p (*supplier*, both copies).
- **Omissions.** Three superscript insertions Brackx left out: *t* (e) in *adve[r]tir* (f. 196 l. 8), *26* (vous) in
  *advis vous venant* (l. 9), and an *o* (a) in *partiroit* (l. 16).
- **Codes read as letters.** `s` = 51 (*pas*, l. 15) and `s` = 35 (*parce que*, l. 30).
- **Writer's slips seen on the image:** a figure struck through at the end of f. 196 l. 3 (f. 201 gives *o*), a
  struck *X* corrected above the line on l. 31, two figures struck before the clear clause on f. 201 l. 26, an extra
  *o* in f. 201's *se reglera*.
- **Image defects (not transcription):** two ink blots on f. 201 ll. 4–5 and a paper stain on f. 201 l. 28; the
  other copy supplies each letter.
- **Different wording, not misreading:** *je suis seur* (f. 196) / *certain* (f. 201); *faillir de [vous] en
  advertir* / *faillir d'en advertir*; *la Barge et Montberault* / *et de Montberault*; *le sieur* / *le S.r*; code 36
  (*toutesfois*) / *x 6* before *l'armée*.

After the corrections, 12 conflicts remain on f. 196, all in the open points below or spelling (*fauldra*).

## Pass 3: what failed or stays open

- Reading the opening *c v Ze w* (f. 196) and *c v Ħ me* (f. 201) as plaintext: no letters fit; f. 201 also has
  *c v* just before the clear *[Je] croy*. Treated as the marks of entry into and exit from cipher, not read.
  `f196_f201.md`'s question (nulls or *i/l* strokes before code 12) is settled: they are this marker, and the head
  crib then aligns exactly (*il a depuis qu'il y est arrivé*).
- `f196_f201.md`'s claim that the tail of f. 201 is not a crib for f. 196 is confirmed and explained: f. 196r stops
  at *il a fallu faire des* and continues on f. 196v (a full page of cipher, ~45 lines, signed in clear *Du camp
  devant Monségur ce … de May 1586*), which nobody has transcribed. That verso, not a divergence of the copies, is
  where f. 201's clear tail belongs.
- Open in the reading, each with the figures of both copies tried against the key: code 37; *[?récité]* (third
  figure c in both); *[?…tement]* (*c 6 tement* in both, superscript 2 over the c on f. 196); the subject and
  adjective of *[…] estant tousjours si […]* (*n e Ħ e t* / *n t H e t e*; *c 6 δ t* / *c 6 pl 8*); the vowel of
  *B?nault*; *[?l'armée]* (*l a r [+|ꝭ] ß*); *[?plus longue]* (two ε where l is needed); *[?vous]* (f. 196 l. 8).
  The same shapes appear in both copies, so these are either values the key lacks or words not found; no outside
  blocker.
- Not checked on the image: f. 196 l. 10 *c* (r in *autre*) and l. 31 *c* (r in *assiéger*), corrected from f. 201
  and marked `?` in the TSV.

## Check results

| pass | file | clean sentences | share | hole rate |
|---|---|---|---|---|
| before | `texts/f196.txt` / `texts/f201.txt` | 3/22, 10/23 | 0.136 / 0.435 | 0.205 / 0.157 |
| final | `texts/reading_f196_201.md`, whole file | 36/51 | **0.706** | 0.114 |
| final | the same, reading only (from "The fever") | 27/34 | 0.794 | 0.067 |

The whole-file figure includes the English header, which the checker scores as French.
