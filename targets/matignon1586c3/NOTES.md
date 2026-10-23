# Matignon's Cipher-3, 1586: BnF fr. 15572 f. 276, fr. 15571 f. 179 and fr. 15573 ff. 379-381 — NOTES

Status: in progress. f. 276 and f. 179 read; fr. 15573 ff. 379-381 decoded, not read (0.59 after the r2j re-read, under the 0.60 bar; see the coordinator's decision of 23 Oct at the end).

**23 Oct 2026, second re-read (batch r2j)**: fr. 15573 ff. 379-381 brought to 0.59 (the batch proposed read (B) at the edge of the bar; **kept decoded, not read** by the coordinator, see the end of these NOTES). No clear copy
or decipherment in the neighbouring folios (views 724-757 contact-sheeted; ff. 377-378 are town petitions, ff. 385-386
another cipher). Every break re-read on the full-size views 740-745: f. 379v l. 3's "p" is bleed-through (*la dite
riuiere*); five second values that recur across the despatch (C = h, p+ = b, b = y, g = o, Lr = n) and look-alike
alternates, 28 letters of about 2,300 (1.2%, `f379_381/ff379-381_corrections.tsv`); a word-by-word carry check
(`research/reading_audit/r2j_matignon_carry.py`) corrected words b30 had left unbracketed without support
(*commissions*, *ataquer*, *supplie* ...). New: *Sainte Baselle*, *le semblable a Caumont et au Mas de Verdun*, *si
vostre maieste l'avoit agreable, il seroit besoing*, *Bergera[c], Saincte Foy et Castillon*, *Cleruant*, *meschancete*,
*de Gourgues*, *d'Andos, seneschal de Foys*, *ils f[…]nt coure le bruict*. v2_score fr: explicit holes 0.344 -> **0.590**
(36/61), plain 0.279 -> 0.426, hole rate 0.133. fraction_read 0.305 -> 1.0 (documents that read, by signs). Log:
`f379_381/ff379-381_reread_log.md` "r2j". The brief named the Cipher-1 key: this despatch is Cipher-3.

**23 Oct 2026, re-reading (REREAD_BRIEF, batch b30)**: fr. 15573 ff. 379-381 still decoded, not read. No contemporary
decipherment, print or DECODE record; views 740-745 fetched at full size (IIIF), f. 379r ll. 1-3 compared with
Burford's sign names (no change). His decode divided, punctuated and translated as a partial reading
(`f379_381/ff379-381_reading.md`, `ff379-381_en.md`, log `ff379-381_reread_log.md`), every departure from the key's
letters bracketed (54 [?word]s): "... il n'y a rien qui incomode tant c[e] pays que [?les] places qui sont sur la
[?riuiere] de Garone entre Tolouse [?et] [?Bourdeaulx]"; new: "veu la saison qui est proche de l'iuer", "president
[?Brulart]", "baillant trois cents escus a vostre seur". Score 0.299 (20/67), holes-only 0.433: f. 379r and the end
build sentences, ff. 379v-380v mostly do not.

**22 Oct 2026, reading audit** (George Lasry's test): f. 276 and f. 179 read from SOLUTION.md. fr. 15573 ff. 379-381 (Burford v0.5) is an unpunctuated machine decode with a garbled word in nearly every sentence and no translation: *decoded, not read*. fraction_read 0.9118 -> 0.305 (signs in the two slips that read).

Split on 14 Oct 2026 from `matignon1586` under the one-key rule (George Lasry, 14 Oct 2026). That entry (catalogue
item 12) joined these two leaves in **Matignon's Cipher-3** with the Mayenne–Forget despatches in **Cipher-1**, a
different cipher with its own entry: [`targets/matignon1586/`](../matignon1586/NOTES.md) (in progress, no page yet).
`f276/` and `f179/` moved here unchanged except for path references; the scans stay in the main checkout's
`targets/matignon1586/scan15571/` (git-ignored), with Tomokiyo's annotated image `img/BnFfr15571f179.jpg`.

**Outcome: read with known key (f. 276; fr. 15573 ff. 379-381) and read from existing decipherment (f. 179), read in
part (91.2% of 4,079 signs, measured).** The two slips are **alejandrozarco's** work (PR #25, 6–7 Oct 2026), reviewed and
re-measured here; full accounts in [`f276/SOLUTION.md`](f276/SOLUTION.md) and [`f179/SOLUTION.md`](f179/SOLUTION.md).
The six-page despatch fr. 15573 ff. 379-381 is **Brett Burford's** (issue #44, 18-19 Oct 2026), added 21 Oct 2026; see
"fr. 15573 ff. 379-381" below.

## The leaves

| leaf | Gallica | lines | signs | read (measured) | method |
|---|---|---|---|---|---|
| fr. 15572 f. 276 | `btv1b9061879d` canvas 285 right | 22 | 734 | 706 (96.2%) | read with known key (Tomokiyo's table, checked and extended) |
| fr. 15571 f. 179 | `btv1b90618802` canvas 187 left, bound upside down | 21 | 509 | 473 (92.9%) | read from Tomokiyo's interlinear decipherment, checked with his key |
| fr. 15573 ff. 379r-381v | `btv1b90618780` views 740-745 | 127 | 2,836 | 2,540 (89.6%) | read with known key (Burford, issue #44) |
| **all** | | 170 | **4,079** | **3,719 (91.2%)** | |

Measured with `f276/scripts/measure.py <read_final.txt> 50` (the `targets/matignon1586/measure.py` rule: a sign counts
read only inside a run of at least three lexicon words totalling at least ten letters; lexicon of the shared `lang`
model `fr-1600-letters`, words ≥ 20 occurrences). Re-run 14 Oct 2026 after the move: 706/734 and 473/509, unchanged.
Shuffled-key controls (50): median 6.9% (max 29.3%) and 3.5% (max 23.8%).

The two leaves name the same people (Iehan Durant, La Rousière) and concern Poitou and Saintonge in 1586:

- **f. 276**: a Poitou intelligence note on the Catholic factions round La Roussière, Henri III's governor of
  Fontenay(-le-Comte): La Guiolle unsure of Le Puy, La Saussaie, the priory promised to Aubois, the sieurs de la
  Fontaine, la Chaie and Mirebeau; "Le Pui est ennuyé de la guerre". Its opening matches Tomokiyo's published line.
- **f. 179**: Frontin to come to terms with La Rousière's children; resolved to attack Pons, "il se poura prendre en
  ung mois"; sickness among the foot; "employer Lansac en … l'armée de mer". The siege and the sickness fit, not
  established, the plague in Mayenne's and Matignon's army round Castillon (Aug–Sept 1586).

Writer and recipient of both are not named on the leaves.

## fr. 15573 ff. 379-381 (Brett Burford, issue #44)

A six-page despatch of autumn 1586 wholly in cipher, addressed to the King and probably from Matignon (Tomokiyo:
"Undeciphered. Uses Matignon's Cipher-3"; he prints the opening line). Brett Burford published the first reading of the
whole despatch on 18 Oct 2026 and brought it to v0.5 the next day
([BravoBravoIX/matignon-1586-cipher-reading](https://github.com/BravoBravoIX/matignon-1586-cipher-reading),
Zenodo 10.5281/zenodo.23470959; data CC BY 4.0, code MIT). His per-page signs, keys with the recorded choice at
every two-valued sign, the French and English text and the unresolved list are copied to `f379_381/burford/` with
his licence.

- **Method (his).** Claude Opus 5.5 named every sign under a 50-sign reference sheet cut from the sibling f. 277r;
  five passes voted; corrections only where two blind asks agreed and the image supported them. The key is
  Tomokiyo's table, checked by aligning a reading of ff. 277r-278r with their decipherment (ff. 279-280), plus six
  values from another Cipher-3 letter deciphered at the time, fr. 15570 ff. 271-272 (decipherment f. 273, Sept 1585):
  long zigzag = ss, circled 9 = *par*, d = *vostre*, and three flagged doubtful. Calibration: 0.962 per sign (0.933
  strict) on f. 278r ll. 12-18 against its decipherment.
- **What it says (his gist).** A military report to the King on the Guyenne campaign: the river trade on the Garonne
  between Toulouse and Bordeaux, from which the Huguenots draw dues; Caumont and the Mas de Verdun; Castillon; the
  Isle and the Dordogne; the King of Navarre, "your sister" at Agen, the artillery from Navarrenx, Marmande, "fifteen
  to sixteen thousand crowns".
- **Re-measured here (21 Oct 2026).** `f379_381/to_read.py` turns his signs and recorded choices into this entry's
  line format; `f276/scripts/measure.py read_<page>.txt 20` gives 440/503, 447/490, 420/492, 493/532, 479/524,
  261/295 = **2,540 of 2,836 (89.6%)**; 20 shuffled keys median 5.8-9.8%, max 33%. His own measure (any dictionary
  word) gives 0.90-0.95 per page.
- **Checked here.** Gallica view 740 (f. 379r): 22 cipher lines, as in his `signs.txt`; the opening signs of l. 2
  (b, a, a hooked sign, 30) correspond to his names; his first line matches Tomokiyo's published opening. Not checked: the other
  five pages sign by sign. No person has checked his transcription.

## The key

S. Tomokiyo's partial Cipher-3 table (cryptiana, *Henry III's Cipher with Ambassadors*): homophonic letter
substitution with word signs (60 *faire*, a β-like sign *de*, 20 *la*, 18 *le*, p-with-stroke *pour*, C with n *que*,
∴ *qui*), v a null. Checked by a hard-EM alignment of a value-blind transcription of the deciphered sibling f. 277r
against its contemporary decipherment on ff. 279r–280r (`f276/crib/`, `f276/scripts/align_em.py`): 1,271 signs align to
letters and 55 word signs to their words, the table's value the top emission for every frequent column. Added on the
leaves: `###` = *et* (8 places), split columns (ζ = i, ɤ = o; ꝫ = u, ʒ = t), ∂ = f, hooked ϱ = i, dotted v = u,
two-stroke # = i, the C with ε inside = q.

## Remaining gaps

- fr. 15573 ff. 379-381: five rare code signs (circle on a cross, looped epsilon with a stroke, zigzag-tailed 3, m with a z-like tail, the barred double o where it is not *le roy de Navarre*) - blocker: no-key-material; one to three occurrences each, in none of the deciphered Cipher-3 letters Burford checked (ff. 189-190, 277-280, 282, fr. 15573 f. 373, fr. 15570 ff. 271-273)
- fr. 15573 ff. 379-381: about 300 signs outside sense runs, of which 5 short runs of clear signs not read - blocker: no-key-material; mostly names, period spellings and reader errors (0.93-0.96 per sign on known text); his list explains 110 of 115 items; no sign-by-sign human check yet

- f. 276 L18 'K' and L14 'C with o inside', one-sign code words not in Tomokiyo's table - blocker: no-key-material; each occurs once and neither recurs on these two leaves; the deciphered Cipher-3 siblings f. 189/190, f. 282 and fr. 15570 ff. 271-273 have not been searched for them
- f. 179 L13, the omega-with-overbar code sign (a person, Navarre?) - blocker: no-key-material; one occurrence, Tomokiyo's 680-px magenta does not settle it
- blots: f. 276 L04 after "de lui", f. 179 L18 after "en" - blocker: illegible; ink blots, checked on the Gallica natives
- f. 276 L22 closing and f. 179 L20 "de la D[…]use", a struck sign and a few short spans - blocker: illegible; faint or struck signs at the edge of the slip; the other unread signs are words the period lexicon holds fewer than 20 times (prieure, escriuent)
- fr. 15573 ff. 379-381: read 23 Oct 2026 (r2j, 0.59 explicit holes); about 45 doubtful words where the signs are clear but give no word under the key (Bourdeaulx, nouuelle, come, faict, reuenu, semble, propos, pourroit, seroit, Brulart, fortifications, recherche, consuls, supplie, consequence, Castelnau, Bearnais) - blocker: no-key-material; every break re-read on the full-size views 740-745 (r2j log); the values they need are in no deciphered Cipher-3 letter; Monaco J 41 (Matignon's minutes) not screened
- fr. 15573 ff. 379-381: blotted or bled-through spans (f. 380r ll. 2, 6-9, 18; f. 381r ll. 5, 8, 12, 19) - blocker: illegible; checked on the full-size views 740-745

## Escalation

- [x] siblings: ff. 277r-278r with their decipherment ff. 279-280 used to check and extend the key; fr. 15570 ff. 271-273 (1585, deciphered on f. 273) gave six more values, and ff. 189-190, 282 and fr. 15573 f. 373 were read for the unknown signs (Burford, #44); f. 189/190, f. 282 and fr. 15570 ff. 271-273 not yet searched for the three code signs (named in the gaps)
- [x] clear-pages: ff. 279-280 are the clear decipherment of ff. 277-278; Tomokiyo's magenta interlinear used for f. 179
- [x] known-keys: Tomokiyo's partial Cipher-3 table applied; the Mayenne-Forget Cipher-1 key is a different cipher
- [x] print: no printed decipherment of any leaf; Tomokiyo's openings of f. 276 and fr. 15573 f. 379r match; Burford searched GitHub, Tomokiyo's pages, Cryptoole and the web (PRIOR-ART.md); Monaco Palace archives J 41 (Matignon's minutes) not screened
- [x] key-rebuild: ### = et, the split columns, the C-family signs and the other additions found on the leaves (f276/SOLUTION.md)
- [x] retry: ff. 379-381 five voted passes and image rounds (Burford v0.2-v0.5); two independent reads of each slip, then a second (f. 276) and third (f. 179) image pass on every disagreeing span
- [x] retry (23 Oct 2026): ff. 379-381 decode divided, punctuated, translated with departures bracketed; f. 379r ll. 1-3 compared on the full-size image
- [x] clear-pages (23 Oct 2026, r2j): fr. 15573 views 724-757 searched for a clear copy, minute or decipherment of ff. 379-381: none
- [x] retry (23 Oct 2026, r2j): every break re-read on the full-size views 740-745; one label corrected; recurring second values and look-alike alternates (1.2% of letters); word-by-word carry check; 0.344 -> 0.590 explicit holes, read (B)

## Assumptions for George's review

- The two Cipher-3 leaves are one entry (one key). George Lasry's 2022 solution of fr. 15572 f. 43, which stood as a
  credit on the old matignon1586 entry, is credited on neither entry: f. 43 is not one of their documents and its
  cipher was not identified here.
- fr. 15573 ff. 379-381 is filed here because Tomokiyo assigns it to Cipher-3 and Burford's key (Tomokiyo's Cipher-3 table plus
  values from deciphered Cipher-3 letters) reads it; the leaf was not in the ledger before (credit: new cipher with solution).

## 23 Oct 2026: coordinator's decision on ff. 379-381
- The r2j pass lifted ff. 379-381 to 0.59 on explicit holes (0.43 plain). The bar is about 0.60, and r9367, ranzo1528 letter 4 and sp106r924 R924 were kept unread at 0.59-0.597, so this despatch is kept **decoded, not read** the same way. fraction_read back to 0.305.
- Remaining gap: about 45 words whose signs are clear but give no word under the Cipher-3 key, and the code signs - blocker: no-key-material; blotted spans - blocker: illegible. Monaco J 41 (Matignon's minutes) not screened - blocker: needs-physical-access.
