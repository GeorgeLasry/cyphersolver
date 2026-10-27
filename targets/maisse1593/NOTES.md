# Henri IV to Maisse (Venice), 8 February and 27 April 1593, in Maisse's Cipher (1592-1593) — BnF fr. 16093 ff. 406, 410

Status: in progress. The Brienne 13 clear copies are not transcribed; both letters decoded, not read (reading audit, 22 Oct 2026).

**22 Oct 2026, reading audit** (George Lasry's test): no text of f. 406 or f. 410 is in the repository, only links to the cipher leaves and to the Brienne 13 copies. Both are *decoded, not read*; class read -> not read, method read from existing decipherment -> not solved until the copies are transcribed; fraction_read 1.0 -> 0.

Earlier status (before the 22 Oct 2026 reading audit): read from the contemporary clear copies (Brienne 13); the cipher itself not deciphered on these leaves. Written up as docs/maisse1593.html.

Split on 14 Oct 2026 from `maisse1592` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old
entry (catalogue 17) joined four leaves of fr. 16093 that Tomokiyo assigns to two different ciphers. ff. 370 and 373
(November 1592) are in Maisse's Cipher (1592), a numerical cipher, which is a different cipher, with its own page
([`targets/maisse1592/`](../maisse1592/), docs/maisse1592.html). This folder keeps **ff. 406 and 410** in
**Maisse's Cipher (1592-1593)**, with their twins f. 404 (partial interlinear decipherment) and f. 412. The full
working record of the catalogue item (folio and canvas maps, the pièce-number route, the scripts) stays in
`../maisse1592/NOTES.md`; the fetch scripts (`fetch.py`, `fetchr.py`, `fetchb.py`) and the git-ignored images are there.
Tomokiyo's key image for this cipher is `src/henryiv_Maisse2.png` (moved here).

This entry was contributed (Arya Sanketbhai Patel, PR #7) as part of maisse1592.

## The leaves

| target | date on the original | pièce | Brienne 13 (NAF 6984) | canvas / page | confirmed by |
|---|---|---|---|---|---|
| **f. 406** (canvas 457) | Chartres, 8 Feb 1593 | 247 | fol. **171r** | 176 right | heading *"Coppie de lettre du Roy audict sieur de Maisse de Chartres le huictiesme febvrier 1593, receue le viii.e d'Avril"*; preamble identical |
| **f. 410** (canvas 461) | Mantes, 27 Apr 1593 | 251 | fol. **193v** | 199 left | heading *"Mante le vingt huictiesme Avril 1593, receue le vingt douxiesme May"* |

Twins: **f. 404** (canvas 455) is the same despatch of 8 Feb 1593 as f. 406, sent by the other route ("double voye"),
with a partial interlinear decipherment; Brienne 13 copies the letter once, at fol. 171r, under pièce 247. **f. 412**
is the duplicate of f. 410 (Tomokiyo). The four leaves of catalogue 17 are four despatches in two ciphers; f. 404 is
not one of the four (corrected 22 Sept 2026 in the maisse1592 notes).

## The cipher

Observed on f. 404 at native resolution: letter-shaped symbols (w, d, l, p, b, y, g, z, long-s and others) carry the
letters, two-digit figures carry the nomenclator; 27, 10, 26, 23, 19, 21, 22, 24 and 8 are the commonest figures on
f. 404. Tomokiyo's key, *"Maisse' Cipher 2 (BnF fr.16093, f.344 etc.)"* (`src/henryiv_Maisse2.png`), is homophonic and
carries word codes (*vous, ceulx, est, faict, de, des, fort, par, pour, que, qui, advis, ces, comme, bon, avec, et,
jay, les, luy, moy*). This is the key Henri IV calls "le double du chiffre que j'ay envoyé aud. de Brèves" in the clear
text of f. 404 itself, which is why Tomokiyo finds the same cipher in the Savary de Brèves correspondence of
1593-1596 and again between Brèves and Beaumont in 1602.

## What the letters say

- **f. 406 / f. 404** (8 Feb 1593, Chartres). The King has answered every despatch and docketed the dates so Maisse can
  tell what is lost; the Spanish insolence and the Pope; Pisany and Cardinal Gondi should not leave Rome; their going
  would be of importance, and their entry among those of the League could breed division.
- **f. 410** (27/28 Apr 1593, Mantes). Acknowledges Maisse's letters of 20 Feb, 7 and 23 Mar; the duc de Nevers held
  one courier in Champagne; warm assurance that Maisse's absence will cost him nothing in the King's favour; and that
  experience has proved Maisse's long-standing judgement of "les affaires de Rome" right.

## What is not done

The key is in hand but not applied: neither leaf is transcribed group by group, so nothing here verifies the cipher
on ff. 406/410. The text comes from the Brienne copies (and, for f. 406, the interlinear decipherment on f. 404).

## Log

- 2026-09-19: Brienne copies located through the pièce numbers (PR #7, as part of maisse1592); f. 406 = f. 404.
- 2026-10-14: split from `maisse1592`.

## Assumptions for George's review

- The outcome is "read from existing decipherment", class read, with `fraction_read` 1.0 carried from the parent entry
  as the share of content obtained from the clear copies; no token of the cipher was deciphered with Tomokiyo's key
  here. If the read bar should require a sign-level decipherment, this entry is "read in part" or "not applicable".

## Remaining gaps

- ff. 406 and 410: the Brienne 13 clear copies, not transcribed - blocker: not-attempted; Gallica btv1b100904592 canvases 176 and 199 through the IIIF at openapi.bnf.fr; then check them against the cipher leaves and f. 404's interlinear decipherment

## Escalation

- [x] siblings: f. 404 (twin of f. 406, partial interlinear) and f. 412 (twin of f. 410) identified
- [x] clear-pages: Brienne 13 fol. 171r and 193v located
- [ ] known-keys: Tomokiyo's key for this cipher (src/henryiv_Maisse2.png) not applied
- [x] print: Berger de Xivrey used to locate the copies
- [n/a] key-rebuild: the key exists (Tomokiyo)
- [ ] retry: none yet

## Contribution by WAINUT (27 Oct 2026)

Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company. The work was done with AI language-model
agents, and the readings were checked against the Gallica images twice, the second time independently. The target
and the Brienne 13 copies were found by Arya Sanketbhai Patel (PR #7); this section builds on that. The text above
is unchanged. The new files are in `wainut/`, and `profile.json` gains two `outcome.texts` entries, credits and dated
solution steps (existing entries untouched).

**Outcome: read in part.** The two clear copies in Brienne 13 are transcribed through the enciphered passages, and
the start of each cipher block is decrypted with Tomokiyo's key against them. The cipher itself is not transcribed
in full: only six stretches (128 signs) of ff. 404, 406 and 410.

### Files

- `wainut/f406_brienne_copy.txt`, `wainut/f410_brienne_copy.txt`: the contemporary clear copies, line by line
  (Brienne 13 = NAF 6984 fol. 171r lower part to 172v; fol. 193v, 194r and the first lines of 194v).
- `wainut/cipher_lines.txt`: the cipher stretches, sign by sign, with the sign names.
- `wainut/f406_decryption.md`, `wainut/f410_decryption.md`: line-by-line decryption against the copies.
- `wainut/f406_reading.md`, `wainut/f410_reading.md`: the letters as running French text (from the copies), with
  the clear and the enciphered parts marked. `wainut/f406_translation.md`, `wainut/f410_translation.md`: English.
- `wainut/decode_check.py` (standard library) and `wainut/decode_check_output.txt`: decryption and controls.

### Findings

1. **The summary of f. 406 above describes the wrong letter.** "The Spanish insolence and the Pope; Pisany and
   Cardinal Gondi should not leave Rome ...; their entry among those of the League could breed division" is the top
   of Brienne 13 fol. 171r. That text is the end of **Maisse's own letter "Au Roy du dixiesme Avril 1593"**, whose
   heading is on fol. 170v ("Sire, J'escrivay d'aujourd'huy en huict iours ..."). Fol. 170v ends "il pourroit bien
   advenir que cette" and fol. 171r goes on "insollence des Espagnolz fist resoudre Sa Saincteté ...". The King's
   letter of 8 Feb begins lower on fol. 171r, under "Coppie de lettre du Roy audict sieur de Maisse de Chartres le
   huictiesme febvrier 1593 receue le viii.e Avril", with "Monsieur de Maisse j'ay tousiours faict responce a voz
   depesches ...".
2. **Where the cipher is.** f. 406 is mostly in clear. Its cipher block starts on the line after "faire des bons
   advis que vous y pouvez apporter", with "Le surplus de voz lettres est sur le subiect des affaires de Rome du
   voiage ..." (copy fol. 172r); this was checked on f. 406 itself and on its twin f. 404. A short run of cipher
   groups also stands on an earlier line of f. 406, inside the clear part; it is not decrypted. The enciphered
   matter of 8 Feb: Rome; Pisany's journey and his arrival in Italy; the war in Piedmont and the new means Maisse
   found to help it; a letter sent through Lesdiguières' men and a further charge for Lesdiguières; Gondi at Nancy
   with the King's passport; the King going down to Saumur, where his sister is. On f. 410 the cipher starts right
   after "de ma bonne grace et faveur", with "L'experience a faict cognoistre ..." (fol. 193v). It covers the affairs
   of Rome; the advice not yet to let Cardinal de Gondi and the marquis de Pisany come back, so as to keep the Pope
   from extremes; leaving their moves to the Grand Duke's advice; Gondi's promises; and probably more (see below).
   The repository's summary of f. 410 covers only the part in clear.
3. **Tomokiyo's key reads these leaves.** Applied unchanged, it gives the copy's text on every stretch: f. 410 cipher
   ll. 1-2 (ratio 0.94 and 0.93 against the copy), f. 404 l. 3 (1.00), f. 406 cipher l. 1 (0.91) and two pieces of
   l. 2 (1.00 and 0.79). With 2000 random permutations of the key values no stretch gets above 0.67, and none of the
   four long ones above 0.53. Values confirmed include 27/e, 29/x, 14/p, to/r, 19/i, 23/c, 24/g, 26/n, 10/s, 8/r,
   7/l, 16/m, 25/d, 5/u, 6/u, 1/o, y/o, the x-like sign = p, the omega-like sign = s, the d-shaped sign = t, the
   crossed 2 = i, the T-like sign = f, the z-like sign = a, and the word signs **15 = faict, 17 = vous, 18 = est**,
   *que* (a 9 with a straight tail), *des* (p with a stroke) and *de* (looped sign). The hooked q-like sign that
   opens both blocks is Tomokiyo's l (l column, row 2), not a new homophone.
4. **Variants between cipher and copy.** The cipher spells *cougnoistre* and has *que vous en avez* and the
   abbreviation *l[ett]res*; the copy has *cognoistre*, *que vous avez*, *lettres*, and repeats *estes* ("vous ne
   vous estes estes en rien trompé").

### Corrections made on the second look

The first sign-level alignment had errors, corrected before writing: on f. 404 the sign first read "9" is the uy
sign (u) and the "+" the theta-like d; on f. 410 "9t" is c (not n), what looked like one long-s sign is two signs
(e, n), and the z-like sign is a; the middle of *cognoistre* reads with the uy sign and the crossed 2. The short
cipher run in the clear part of f. 406 was first placed near "pour le regard du pape" and on the second look near
"... & puissance ..."; its place in the copy text is open.

### Still open

- In f. 410 l. 1, the three signs where the copy has *vous ne* decode as r u e: misread, or a word sign missing from
  the key. In f. 406 l. 2 the pi-like sign in *Rome* is r by the key (*rrme*), and the `+` in *voiage* is a by the
  key but i by the copy. All marked as holes.
- The rest of both cipher blocks (about 18 lines on f. 406, and the verso, canvas 458, if it carries cipher; about
  23 lines on f. 410) is not transcribed, so the decryption covers the first lines only.
- The copies: fol. 173r (end of the 8 Feb letter) and fol. 194v after its first lines are not transcribed; on
  fol. 194v the right edge was cut off in the view used. Where each cipher block ends is not fixed. Only the
  headings and the first cipher lines of the copies were checked a second time.

### Prior art

The contemporary clear copies in Brienne 13 are in effect the decipherment of the time; they were located by Arya
Sanketbhai Patel through Berger de Xivrey's citations (PR #7). Berger de Xivrey, t. III (1846), was not re-checked
here. We know of no printed decipherment of ff. 406 and 410; Tomokiyo published the key, not readings of these leaves.
