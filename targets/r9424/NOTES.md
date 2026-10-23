# A letter to Duke Wilhelm V of Bavaria, 12 June 1583, in a Latin-letter cipher (BayHStA KAA 4591 ff.274–277, DECODE R9424)

Split on 15 Oct 2026 from `targets/kaa4591/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 161
grouped fourteen ciphertexts of the Munich key volume KAA 4591 in at least six systems; this letter is in a cipher of
its own. **Key recovered from ciphertext-only by Ryan Xu (ry-xu, issue #89, 23 Oct 2026); read in part (92.8% of words) after a re-reading on the images, 23 Oct 2026** (block below). The other letters are different ciphers, each with its own page: System A′
([`targets/kaa4591/`](../kaa4591/NOTES.md)), Łaski's cipher ([`targets/kaa4591b/`](../kaa4591b/NOTES.md)), the Fulda note
([`targets/fulda1576/`](../fulda1576/NOTES.md)), R9367 ([`targets/r9367/`](../r9367/NOTES.md)), R9416
([`targets/r9416/`](../r9416/NOTES.md)) and R9319 ([`targets/r9319/`](../r9319/NOTES.md)). Work 21 Sept 2026 (Claude
Opus 5) as part of kaa4591; `r9424/` moved here unchanged; `signstream.py` added 15 Oct 2026. Catalogue entry 161 stays
open in `catalogue.json` for this record and R9319.

Images: DECODE, login; not public domain, kept untracked; the page shows none.

## The letter

German letter to Duke Wilhelm V, dated 12 June 1583 (the Cologne war). P1 (f.274r) opens in clear; the cipher runs
from line 8, in Latin minuscules with a few invented signs (ε, ∆, ʒ, a 2-like z, '/', a cross-mark), word-separated,
inside clear words ("Zwisch Ho. Fe.", "und Ni. sein"). Contemporary glosses stand over a few single groups on f.275r
(Hildesheim, Würzburg, Eichstätt, Freising). A nomenclator fragment shows on the facing leaf f.273v at the edge of the
photo: names with signs (Cöln = δ?, Wirtemberg = δδ?, Landgraf = φ). P2 (f.274v) is clear German only.
Transcription: `r9424/transcription.txt` (glyph by glyph); 913 cipher signs (`signstream.py` → `r9424/signs.txt`,
29 distinct).

## What was tried

- R9422 (the volume's 1582–83 key; its alphabet is cut off at a/b) does not read as transcribed; R9420 (1531 keys,
  a shift alphabet) and R9421 (tabula recta) checked.
- IoC 0.068, flat over periods 1–8: monoalphabetic, or a code.
- Constrained annealing with de-modern, then de-1500s, with and without '/' and nulls, and in Latin and Italian: no
  text. The glosses sit over single groups, so the cipher is probably partly code groups; with transcription noise and
  too few gloss cribs it does not open.

## 23 Oct 2026: key recovered ciphertext-only by Ryan Xu; re-read on the images (Claude Opus 5.5)

**Credit.** Ryan Xu ([ry-xu](https://github.com/ry-xu)), with Claude Opus 5.5, recovered the key from
`r9424/transcription.txt` alone and posted it as issue #89 ("Solution: r9424"), 23 Oct 2026; write-up, scripts and
controls at https://github.com/ry-xu/slightlysupervised/tree/main/wilhelm-1583-cipher (no licence stated, so cited
and linked, not copied; our English is our own). He is the breaker; this session checked his key and reading on the
images and built the reading below.

**The key** (`r9424/key.md`): a simple substitution on Latin letters (r=a, w=b, d=c, z=d/r, k=e, i=f/u/v, 3=g, D=h,
o=i, s=l, n=m/n/u, a=n, 4=o, t=p, c=t, m=z, q=y), '/' doubles the previous letter, nulls g, y, b, p (and some d, m, n)
at word edges; one nomenclator sign (barred o-o, written # in the transcription). The values form chains
(p→t→c→d→z→m→n→a→r, l→s→e→k, u→i→o→4), so each sign should carry one value: the dual values are look-alike glyphs
under one label. His method: `-ka` = -en, `-kz` = -er, short words, then long words exact (dissimulationes,
indignationen, beschaidenhait). His controls: 65% of words of 4+ signs in a 16th-century DTA lexicon vs median 8%
(max 24%) for 40 shuffled keys; from-scratch annealing (DTA 1500-1599 4-grams, no cribs) recovers 11 signs, 70% of
tokens (seed 2). Why our 21 Sept annealing failed: the unconstrained homophonic search collapses to e/n/r text, and
the merged z labels and nulls hide the single-valued key.

**Image check** (DECODE IMG_R9424_I44564_P1, P3 at full resolution, scratchpad only; `r9424/R9424_corrections.tsv`):
- of his 15 one-sign emendations, 9 are settled by the image: looped d (c) misread as s/o in auch (l. 8), confusion
  (l. 9), nachgeben (l. 11), durch (l. 28), fructus (f.275r); geistlichen (dD = ch); s-form (l) read as e in
  muglich (l. 27); r-form read as z in allain (f.275r); the first sign of befinde (l. 9) is w, not c; the sign
  before belaitten (l. 22) is the cross mark, not 4. suspi[c]tion is withdrawn: the image gives *suspition*. Kept
  as supplied or uncertain: gr[o]ss (image shows o), sti[f]t (image shows z), cöl[ni]sche (p with superscript),
  [?magna], [?weihb.], [?wünschen].
- 'Sl' on f.275r is the clear sigil "Si." (as in l. 14), not a cipher sign.
- writer's spelling restored: regirt, ghen, gefurt, gefuhrt, muglich, seim, phillip.
- **look-alikes:** in the 146 directly aligned words, z = d 37, z = r 37; n = m 22, n 4 (+ u/v); r = a 45, r 2.
  Letters resting on the other member of a merged label: 43 of 631 (6.8%) on the transcription labels. On the image
  the z for d has a hooked or tailed top, the z for r is a flat-footed 2 (zizoD = durch shows both; droakz/zka;
  drok3ei/keka); about a dozen spot-checked, consistent, but the 92 z's were not all re-labelled. With the two z
  forms kept apart the share is about 1%. The contemporary glosses (der, thumbrobst, Wirtzburg, Hildesheim) agree.

**Reading:** `r9424/R9424_reading.md` (writer's spelling, holes marked), `r9424/R9424_en.md` (our English).
read_share 0.928 (v10_relabel.share: 218 words, 17 holes): coherent sentences, under 95%, so **read in part**;
reading_review grade A; clean sentences 0.21 on the shape score (modern word list), 0.905
(19/21) counting explicit holes only (b17_score HOLES=1). _validate.py: not applicable (polyphony 0.147 from the merged
labels; validation.tsv from the 126 directly read words). fraction_read about 0.97 of 913 signs (about 28 signs unvalued).

## Remaining gaps

- the # sign (barred o-o), 3 times (ll. 23, 27; f.275r) - blocker: no-key-material; a nomenclator sign, the volume key R9422 is cut at a/b and the f.273v table is half outside the photo
- l. 21 izriafzia/kz, a name or title (F-r-a-u-n-?-d/r-u-nn-e-r) - blocker: no-key-material; one sign (f) has no value and no name in context fits
- l. 22 'eo' after ghen, l. 8 dʒ and np - blocker: too-short; two-sign groups the key does not value
- f.275r zodDcw3, glossed Aichstet - blocker: no-key-material; does not decode with the key, a code word or a miscopy

## Escalation

- [x] siblings: R9419-R9423 key records of the volume opened; the f.273v nomenclator fragment noted (half visible)
- [x] clear-pages: the f.275r glosses checked against the key (der, thumbrobst, Wirtzburg, Hildesheim agree; Aichstet does not decode)
- [x] known-keys: R9420, R9421, R9422 tried (21 Sept); Ryan Xu's key fits
- [x] print: no edition found (Ryan Xu: Cryptiana, GitHub, Leighton 1974); Immler 1999 not online
- [x] key-rebuild: key recovered ciphertext-only by Ryan Xu; checked sign by sign on the images 23 Oct 2026
- [x] retry: every emendation and unread group re-read on the full-resolution images 23 Oct 2026; 9 settled, 1 withdrawn
## Next

Re-label the 92 z's as two signs on the images; ask the BayHStA for the full f.273v (the nomenclator for the # sign);
look for the escort's name of l. 21 among the Freising chapter of 1583.
