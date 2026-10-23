# Re-reading log, fr. 3071 no. 4 (macon1537), 23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b34

## Starting point

Reading audit (22 Oct): "decoded, not read": `fr3071_no4_macon.md` says 35-40% of the cipher is read confidently;
the f. 9v part fragments. That figure is the first pass's: the second pass (18 Sept, `macon_9r_26-34.md`,
`macon_9v.md`) had read f. 9r ll. 26-34 (~175 of ~190 signs) and f. 9v in full, but no single reading of the letter
existed, and the clear text (a third of the letter) was "read loosely" with long `...` gaps. No reading file to score:
before = 0.00.

## 1. Is there a text already?

- Not a DECODE record (Lasry decoded it in 2023 but never published a plaintext: NOTES, credits). Tomokiyo francis.htm,
  Lasry GL.htm: keys only.
- **The slip f. 9bis** (Gallica view 18) is a contemporary decipherment of the f. 9v cipher (identified 18 Sept, only
  partly transcribed then). Transcribed in full now: `macon1537_slip_f9bis.txt`. It covers f. 9v ll. 4-16; nothing
  covers the f. 9r cipher. Neighbouring items of fr. 3071 (the other item-6 letters) were reviewed in Sept for
  gramont1529; no clear copy of this letter found. Not in print.

## 2. Images

Gallica through openapi.bnf.fr IIIF, views 16 (f. 9r), 17 (f. 9v), 18 (slip), 19 (f. 10r), full size (4353 x 6079),
scratchpad only. The clear text was re-read band by band: f. 9r clear runs (ll. 1-3, 17-19, 21-22, 25-31), f. 9v
ll. 1-4 and 17-30, f. 10r ll. 1-11 and the subscription. New: the count on f. 9v l. 4 is *Gifuentes* = Cifuentes (the
imperial ambassador in Rome); the f. 9r l. 21-22 clear *Ce que je ne croy, mais est chose que je pense que*; the f. 9v
Mantua passage and f. 10r close transcribed in full (single doubtful words marked).

## 3. Alignment

- f. 9v ll. 4-16 decode vs the slip: word for word, except *ce que* (figures) / *car* (slip) l. 7 and *peur* (figures)
  / *peine* (slip) l. 8: the reading follows the figures; the slip's interlinear *ou myeulx* settles l. 11 *ou mieulx*;
  slip *les Vitelli* / figures *le dict Vitelli*: the figures.
- f. 9r: the decodes of the two Sept passes were taken as they stand (no key change); the reading uses their word
  division. Every cipher word of the reading is in the decode tables of `fr3071_no4_macon.md` / `macon_9r_26-34.md`;
  words the decode does not carry are bracketed: `[?de Cosme]` (l. 8, supported by the slip), `[?pape]` (l. 27 `{B♦}`),
  `[?sera]`, `[?suivissent]`, `[?grosse]`, the l. 10 hole.
- Supplied words: *[et estre]* (f. 9r l. 25-26, between *considerer* and *advise*).
- **Look-alike letters**: about 10 letters of the f. 9r cipher rest on the other member of a look-alike pair (short `4`
  as R in *declarant*, *craindre*, *declarer*; hooked `g` as T in *Venitiens*; `7` as N/B/R where the sense chooses)
  out of about 3,900 letters of the reading: 0.3%, under the 3% limit. The f. 9v cipher rests on the slip.

## 4. Score

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=fr) | no reading (0.00) | **0.676 (46/68)** |
| reading body, b17 HOLES=1 | — | **0.868 (59/68)** |

Unclean sentences: the marked holes (f. 9r ll. 3, 8, 10, 16-19, 27-31; the Mantua passage's doubtful words) and 1537
spellings (*nouarre*, *concille*, *pouure*, *escripuy*). Reader's judgement: the letter reads as connected French and
translates (`macon1537_en.md`); the f. 9r paragraph on the Venetians (ll. 27-31) is the weakest, carried by its
cipher frame (*a craindre que les Venitiens … actendu qu'il se dict que le Roy avoit promis au Turc …*).

## Result

Read: grade B (cipher from the key decode, f. 9v checked against the contemporary slip; clear text with single doubtful
words).

## Open

- Cipher: f. 9r l. 10 middle, l. 16-17 after *messire Latin*, l. 27-28 seven signs, l. 33 the word before *puissance*,
  l. 8 the name group (sense from the slip) - blocker: illegible (blot and odd sign forms on the Gallica scan; no
  decipherment covers f. 9r).
- Clear text: single doubtful words (f. 9r ll. 17-19, 29-31; f. 9v Mantua passage) - blocker: illegible (fast
  secretary hand on a bitonal microfilm scan).
