# Rennes 1563 — Catherine de Médicis / Court → Bernardin Bochetel, bishop of Rennes

Catalogue item 11 (class B). Goal: read the undeciphered letters
- BnF fr. 3181 f. 55 (Catherine, 31 July 1563) — ark btv1b9059845t, view 36 (folio = view + 19)
- 500 Colbert 390 p. 139 (ark btv1b10033942k, view 70; "Deschiffrez vous mesmes" note) and p. 357 (view 180)
- 500 Colbert 392 p. 231 (ark btv1b100339594, view 112; Bourdin, ~30 lines all cipher)

## Prior art
Tomokiyo, "French Ciphers during the Reigns of Charles IX and Henry III"
(https://cryptiana.web.fc2.com/code/henryiii.htm): reconstructed the Bishop of Rennes'
cipher 1561-1564 (`images/CharlesIX_Rennes.png`) from the deciphered letters in Colbert 390
and fr. 3158 f. 1 (Francis II, 3 Sept 1560, read with the key). fr. 3181 f. 52 (28 Feb 1563)
and f. 57 (10 Aug 1563) use the same cipher and carry marginal decipher glosses (views 33, 38);
f. 55 (31 July 1563) undeciphered. A second cipher (Cardinal de Lorraine → Rennes 1563,
Colbert 392 p. 27) = `images/CharlesIX_Rennes2.png`.
Short function words (est, plus, pour, que) double as NULLS in this key.

## Key (Tomokiyo reconstruction, images/CharlesIX_Rennes.png)
Letters (homophones separated by spaces; descriptions of glyphs):
- a: z / eta / long-s / ff-lig
- b: h / y-loop (8-like with tail)
- c: 3 / m-like / * / E
- d: La-lig / gamma-loop / x / script-v-dot
- e: d / xy / xi / backslash
- f: 4 / phi
- g: a / a-tilde / beta (circled)
- h: pi / pi-macron / c-hook
- i/j: 10 / 10-macron / m-hook / k / lz
- l: 6 / sigma / beta2
- m: 9-left / J-hook / N / d3
- n: 9 (circled) / u-hook / u-flourish / ff-tall / tt (circled)
- o: curl-C / 3-like / u-4 / lf
- p: b / Z / N-cap / my
- q: ss-double
- r: 2-like / s-swash / ee / U-cup
- s: 3-swash / phi-cross / V
- t: G-spiral(circled x2) / e-curl / c-tilde / T-bar / 6 / f-cross
- u/v: lambda / mu / w-flourish / w-3 / uv / gl-lig
- x: star4 / star6
- y: 7-hook / T / r-small
- z: theta / theta-slash
Nulls: // , double-dagger, =, r-hook, do, fo, eps3, g3, G-swash(circled), L-swash(circled); plus, pour, que, est, xix, vre (word-lookalikes as nulls)
Word signs: bien=pl, com=delta, con=croc, dit=delta-circ, ent=G-circ, est=#, et=g-tail/tp, faict=tu, faire=ca, la=mn-bar, le=vp, lettre=sc, luy=8
mais=A, nous=>, ont=delta2, par=at, plus=quote2, puis=tz, quant=Omega, que=qq-bar, qui=V-bar, si=z-swash, vous=<, vostre=+
l'Empereur=e-grave-like, Roy de Boheme=V-dot

## State

Status: not read (verify v8, 23 Oct 2026: all four letters decoded, not read; Tomokiyo's key applied).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**. f. 55,
Colbert 390 pp. 357-358 and Colbert 392 p. 231 build French sentences with scattered holes (`aligned/*.txt`; reviewed
B in `profile.json`). **Colbert 390 p. 139 is decoded, not read**: its first seven lines read, lines 8-14 are mostly
unread runs and code words. Reading figure 65.8% (sense tokens in the three letters that read, 1,520 of 2,311); the
79% below (sense over all four) is withdrawn as a reading figure.

23 Oct 2026, re-reading (REREAD_BRIEF, batch b33), p. 139: still **decoded, not read** (partial reading
`c390_p139_reading.md`, 0.25 clean sentences, b17 fr; log `c390_p139_reread_log.md`). All 184 views of Colbert 390
contact-sheeted: no clear copy or decipherment of the note. Found an unused key source in the same volume: Catherine's
**15 Dec 1562** letter (pp. 115-127), whose ciphered paragraphs (p. 118 lower, pp. 119-121, 125, 127) La Ferrière I
449-451 prints from the decipherment joined to it; p. 118 top is already written out in clear. Not aligned yet: it is
the next step for p. 139's open signs.

23 Oct 2026, second re-read (batch r2j), p. 139 against the 15 Dec 1562 letter: still **decoded, not read** (0.25,
hole rate 0.265). The 15 Dec letter's cipher is on pp. 117 (5 lines), 118 (22), 125 (about 35) and 126 (8); pp. 119-121
are the cursive decipherment La Ferriere printed. pp. 117-118 transcribed sign by sign (`c390_1562-12-15_cipher.txt`,
949 signs) and aligned with La Ferriere I 449-450 (`c390_1562-12-15_plain.txt`; hard EM,
`research/reading_audit/r2j_rennes_em.py`, table `c390_1562-12-15_em.txt`): ∂ = m 26/31, ẟ = r 12/13, ā = g 7/7,
♯ = y/et/est, + = f/s/x, ꞓ = o/h, ℒ = *dict*, ꝩ = *(le) roy des Romains*, ∂a = *Allemaigne*. pp. 125-126 inspected:
same inventory. **None of p. 139's open signs (ẟao, aʓ, ℛ, ℞, ẟ + superscript) occurs in the letter**, so the blocker
is now no-key-material. p. 139 retried (`research/reading_audit/r2j_p139_lattice.py`): *fils* carried (+ = s), l. 8
*passeront en ce [?voyaige] de mon cousin* proposed (the Cardinal of Lorraine's journey; ß = g needed); nothing else
closes. Log: `c390_p139_reread_log.md` "r2j".

Four letters in the same cipher, each read from its own image with values calibrated on
contemporary glossed letters in the same hand (21 Sept 2026). Share of cipher signs in
secure + probable French:

| Item | Date | Reading file | Read |
|---|---|---|---|
| fr. 3181 f. 55, Catherine | 31 July 1563 | `f55_v2_reading.md` | ~91% (80 secure, 11 probable) |
| 500 Colbert 390 pp. 357-358 | late summer 1564 | `c390_p357_reading.md` | ~99% (88 secure, 11 probable) |
| 500 Colbert 392 p. 231, Bourdin | Dec 1562 | `c392_p231_reading.md` | ~85% |
| 500 Colbert 390 p. 139, "Deschiffrez vous mesmes" | 1562-63 | `c390_p139_v3_reading.md` | ~65% (37 secure, 28 probable) |

Token-weighted, about 87% of the 2,310 transcribed signs (estimate, secure + probable). **Measured strictly on 5 Oct 2026 (`measure.py`, see "Push to 95%" below): 79% of 2,308 tokens read as sense, 15% probable, 6% unread.**

- **f. 55**: Council of Trent and the Habsburg marriage; "avancer le concile", "pour le bien
  de la Chrestienté", "ce qui se promect des sessions de Decembre, desquelz vous avez oy
  parler, vous estant dernierement à … Trante".
- **p. 357**: the precedence dispute at the imperial court (1564, after Ferdinand I's
  death): "il fauldra prandre autre pretexte que celuy porté par la depesche du s[ieu]r
  Charon… laisser là quelque secretaire ou aucun des vostres, advisés soubz couleur d'aucuns
  voz affaires particuliers".
- **Colbert 392 p. 231**: Bourdin encloses Catherine's letter of 15 Dec 1562 (La Ferrière I
  448-451) on the secret marriage overture; its leak to Spain ("sçavoit incontinant en
  Espaigne"), "[s]a femme … triumphe de la premiere ouverture que vous luy feistes de ce
  mariage", closing "d'amitié et alliance… à l'honneur de Dieu et au repos de la
  chrestienté". Clear end with date on p. 232.
- **p. 139**: a secret note, "decipher it yourself, trust no clerk, burn it": "que je vous
  tienne pour trop advisé et affectionné et loyal serviteur du roy mon fils… les yeux ouverts
  pour observer… mon cousin… ses actions… beau frère".

Method: `lattice.py` (beam decoder, fr-1530-despatches model) over per-glyph candidate sets;
per-hand values from the glossed siblings in `fr3181_glossed.md` (f. 57-58) and
`colbert390_glossed.md` (p. 138, pp. 189/199, 221-231). Crib material from La Ferrière in
`cribs.md`. Crops are git-ignored and rebuilt from Gallica.

## Setup (earlier session)
This is setup and key calibration, not a completed decipherment. No continuous reading of any of the four target letters has been established.

- Images fetched locally (img/): fr3181 v33-v42 (ff. 52-61), c390 v70-73 + v179-181, c392 v112-115.
- c390 v70 = pp. 138-139 spread: p.139 is the "Deschiffrez vous mesmes" note, ~20 lines cipher,
  plus a cipher paragraph on p. 138 with interlinear gloss visible (left page, partly deciphered).
- c390 v180 = p. 357: Catherine (?) letter, lower two thirds in cipher, ~25 lines, no gloss.
- c392 v112 = p. 231: Bourdin letter, ~30 lines cipher, no gloss.
- f. 55 = fr3181 v36: 17 lines of cipher then clear text (Havre de Grace / Queen of England passage in clear).

## Verification v8, 23 Oct 2026

The translation wave could not translate f. 55, Colbert 390 pp. 357-358 and Colbert 392 p. 231 because they do not read.
Its partial readings (`f55_reading.md`, `c390_p357_p358_reading.md`, `c392_p231_bourdin_reading.md`: the `aligned/`
files put into sentences, `~` probable words and `{n}` runs as holes) score **0.50, 0.27 and 0.17** clean sentences on
explicit holes (`research/reading_audit/v2_score.py`; plain 0.375, 0.133, 0.167; hole rates 0.17-0.23). Holes in most
sentences, and every key source is already tried (Escalation). **All three back to decoded, not read**; with p. 139 no
letter reads: class **not read**, method not solved (Tomokiyo's key applied, kept as an `outcome.parts` item),
`fraction_read` 0.658 -> 0. The partial readings are kept.

## Remaining gaps
- 500 Colbert 390 p. 139 as a whole decoded, not read (ll. 8-14 mostly unread runs and code words; reading audit 22 Oct 2026; re-read 23 Oct, 0.25) - blocker: no-key-material; the 15 Dec 1562 cipher (pp. 117-118, 949 signs) aligned with La Ferriere I 449-450 on 23 Oct (r2j) and pp. 125-126 inspected: the open signs ẟao, aʓ, ℛ, ℞ and the ẟ + superscript code words do not occur in it, and the common-sign values it measures do not close the runs (`c390_p139_reread_log.md`)
Measured 5 Oct 2026 with `measure.py` (strict: only words the signs give at attested values count; 2308 tokens): sense 0.79, probable 0.15, unread 0.06.
- fr. 3181 f. 55 decoded, not read (v8 23 Oct 2026: 0.50 clean sentences; 0.80 sense): l.2 ꝥ, ɼ ᑲ; l.4 "10 ᑲ ɗ xy ee z r"; l.8 "ß La ᑲ ᑲ z 10 9 z"; l.9 "‡ G̃ ꜧ ᑲ ᑲ ɗ ᑲ ᑲ"; l.12 "h Ə"; slips (ayt tenu, deliberay, monstrrer, sessions) - blocker: no-key-material; the signs occur in no glossed passage in this hand (f.57-58 aligned in full); re-viewed on native crops 5 Oct, no new value
- 500 Colbert 390 pp. 357-358 decoded, not read (v8 23 Oct 2026: 0.27 clean sentences; 0.82 / 0.76 sense): p.357 l.3-4 "6 d 9 ∿ io ꭓ | d λ ʒ ‡ ϑ d Z ℒ d ¢ ⊤̸ d", l.5 head, l.8 avoir / l'effect, l.13 afairres; p.358 s'offrira, esperer, [ajour/gouver]nement, lumiere, remects - blocker: no-key-material; each needs a value no gloss gives (∿ = n, sh = r)
- 500 Colbert 392 p. 231 decoded, not read (v8 23 Oct 2026: 0.17 clean sentences; 0.83 sense): maue, ſ λ ², ‡‡ ~, πꝫ (twice), "ꞁꞁ ℌ z 9 ‡‡", "La ƀ ſſ z", fc 7, conseil, comme en, leurs - blocker: no-key-material; these shapes occur once or twice and in no glossed passage of Colbert 390 pp.189-231
- 500 Colbert 390 p. 139 (0.70 sense): l.2 ā; l.4 "ſ mJ z ʓ G k ẓ ƀ"; l.5 "io ƀ η"; l.8 "ſ λ ſſ ♯ z k ß" and end; l.10-11 "de me donner" (ℊ, ‡‡ unsupported); l.12 ẟao + "ſ σ aʓ 9 ẓ La ſ ƀ"; l.13-14 ẟao + "ʓ k 9 ẓ m io ʓ η ſ ß x1"; code words ẟ, ẟao - blocker: no-key-material; ẟ+superscript are code words and ẟao, aʓ occur in no gloss, key or the 15 Dec 1562 letter (aligned 23 Oct 2026, r2j: there ā = g, ẟ = r)

## Escalation
- [x] siblings: sister volumes Colbert 391, 394, 395 surveyed (sister_volumes.md): no deciphered passage in this cipher; fr. 3181 f. 52, f. 57, f. 58 and Colbert 390 pp. 138, 189/199, 221-231, 241 opened; f. 57-58 and p. 138 give the hands' values; Colbert 392 p. 232 is the clear end of the Bourdin letter
- [x] clear-pages: clear parts of all four letters used for context; Colbert 392 p. 232 dates the Bourdin letter
- [x] known-keys: Tomokiyo's Bishop of Rennes key; the Rennes2 (Lorraine) key checked, not this cipher
- [x] print: La Ferrière I-II (cribs.md): none of the four passages printed; Bourdin's enclosure is Catherine 15 Dec 1562; Tomokiyo lists all four as undeciphered
- [x] key-rebuild: per-hand values from glossed siblings, LM lattice decoding
- [x] retry: every letter re-run after each new value set; p. 139 control re-run withdrew four readings
- [x] retry (5 Oct 2026): every letter re-transcribed against fresh native IIIF crops (hi2/) and re-measured strictly with measure.py; corrections in the token files' headers (c390_p139_v4.txt, c390_p357.txt, c392_p231n.txt). Strict sense 0.72 -> 0.79. 95% not reached.
- [x] siblings (5 Oct 2026, second survey): every view of Colbert 393, 396 and fr. 3180, 3182 contact-sheeted: no cipher, gloss, decipherment or key sheet (sister_volumes.md). With 391/394/395 the whole Bochetel series is negative; re-measured, unchanged at 0.79. Remaining outside leads: Tomokiyo's source for the key table, other Bochetel/Rennes correspondence outside Colbert 390-396 (e.g. Vienna HHStA), Lasry.
- [x] clear-pages (23 Oct 2026): all 184 views of Colbert 390 contact-sheeted (research/reading_audit/b33_rn_sheet.py): no clear copy or decipherment of p. 139; the 15 Dec 1562 letter (pp. 115-127) has printed decipherment (La Ferrière I 449-451) and is the next key source, not yet aligned
- [x] known-keys / key-rebuild (23 Oct 2026, r2j): the 15 Dec 1562 cipher (pp. 117-118, 949 signs) aligned with La Ferriere I 449-450 by hard EM; values confirmed (∂ = m, ẟ = r, ā = g, ♯ = y/et/est) and widened (+ = s, ꞓ = h, ʒ = c); pp. 125-126 inspected, same inventory; p. 139 retried: one word carried (fils), one proposed ([?voyaige]); p. 139's code signs are not in the letter
- [x] retry (23 Oct 2026, v8): the three letters' partial readings scored on explicit holes (0.50, 0.27, 0.17); no new value or source; all decoded, not read

## Push to 95% (5 Oct 2026)
**The old 0.87 did not measure sense.** It was a hand estimate of secure + probable per letter, and "probable"
included words that need a sign value nothing attests, or that were filled from context. `measure.py` now
counts: each letter has a word-by-word reading in `aligned/` (`{n}` unread, `~{n}word` probable); every cipher
token must align to the reading through its own candidate values (glyphs.G, the token's `=a|b`, the per-letter
EXTRA table with the evidence for each value), so a reading the signs do not give fails. Sense words are
checked against a 16th-c. French vocabulary. Run `PYTHONUTF8=1 python measure.py`.

| letter | tokens | before (strict) | after | probable | unread |
|---|---|---|---|---|---|
| fr. 3181 f. 55 | 401 | 0.80 | 0.80 | 0.13 | 0.07 |
| Colbert 390 p. 357 | 475 | 0.79 | 0.82 | 0.16 | 0.02 |
| Colbert 390 p. 358 | 275 | 0.76 | 0.76 | 0.22 | 0.03 |
| Colbert 392 p. 231 | 719 | 0.73 | 0.83 | 0.12 | 0.05 |
| Colbert 390 p. 139 | 438 | 0.53 | 0.70 | 0.16 | 0.14 |
| **all** | 2308 | **0.72** | **0.79** | 0.15 | 0.06 |

What moved it (all from re-looking at the signs, not from context):
- **p.139**: "ẟar" in l.9 is a struck-out word; ÿ = d (Tomokiyo's script-v-dot) gives *pour vous en dormir bien*
  (l.3) and *de me* (l.10, still probable); ᵐ C Ꝫ x1 = *come* (ᵐ = the m-like c, Ꝫ = d3 = m) and *totes … passeront
  en ce* (ƀ = p, the key value); the "€" before *cousin* is ℒ (null) + the m-like c, so *mon cousin* is secure;
  *encores que je n'en visse aucunement a doubter*; *beau frère … de vostre [ẟao]*.
- **p.357**: l.14 and l.15 had signs doubled where two half-line crops overlapped; with the doubles removed
  *de deniers … envoyé querir* aligns (ɥ = gamma-loop d).
- **Colbert 392**: *Je vous envoye* (l.1 opens with two nulls); *ne l'asseurer qu'elle la toute tel[l]e* (l.5);
  *propre* (6-shaped b = p); *difficulté* (ẽ = ff); *je vous advis* (ıō, not w); raised small z = a in *s[a]ns*,
  *y [a]voit*, *[a]u repos*; dʒ = mm in *femme* and *commun*; ff-ligature a in *aliance*.
Tried and failed: the p.139 runs listed above, "choses" (needs € = h against the € of afin), f.55 l.1-2 openings.

