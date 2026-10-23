# Re-reading log, R9635 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b23)

## Starting point

Reading audit (22 Oct): "decoded, not read". `read_r9635.md` was a table of resolved code-group phrases and
`edition/r9635_f20r.md` / `r9635_f21.md` line-by-line fragments of f. 20r and the opening of f. 21; no reading body
(nothing to score with b17; `_check_reading.py` on `read_r9635.md` gives 0.638 on table fragments, not sentences).

## 1. Is there a text already? Yes: the 1522 decipherment, f. 22r

- **DECODE record**, fetched logged in on 23 Oct 2026 (`research/reading_audit/b23_fetch.py`): 3 images
  (`IMG_R9635_I45364_P1..P3`, two-page openings, 3368x2410), no attachment, no transcription, no comment block. Every
  page opened (scratchpad `reread/R9635/`):
  - P1: left page, the end of the previous record's matter / blank side; right page **f. 20r**, cipher, with the
    interlinear glosses (*obligados*, *fuessen restituydas sus …*).
  - P2: left page **f. 20v**, cipher (*tambien … embaxador que esta en Francia … el rey de Francia …*); right page
    **f. 21r**, cipher with the glosses *obligados / fuessen restituydas sus tierras* and the clear Pace paragraph
    (`edition/r9635_f21.md`).
  - P3: left page **f. 21v**, address leaf, docket written upside down (*… Venecia a xvi de setiembre …*); right page
    **f. 22r: a full clear decipherment of the cipher, in a court hand, 29 lines**, beginning *Visto que [?y]. tanto
    tardavan cartas de v. mad.* and ending *Por dos vias me han certificado esto*. Earlier sessions opened P3 only as
    "f. 22, not examined" (`edition/r9635_f21.md`, "Open").
- Transcribed line by line: `R9635_decifrado_f22r.txt`. A tear across ll. 9-10 takes about ten words; three words are
  uncertain in the hand (*[?dema] [?bastar]* l. 12, *[?tenido]* l. 21, *[?lureina]* l. 22).
- Print: CSP Spain 2 no. 476 (Bergenroth's abstract) agrees topic by topic (the 20,000 due under the truce, the
  18,000 left unpaid, the Venetians' demand that their towns be restored first); used only as a check.

## 2. The decipherment against the figures

Every passage of ff. 20r, 20v already read sign by sign (`edition/r9635_f20r.md`) or re-read in this pass on 2x crops
(`b23_sanchez_lines.py`) stands in the decipherment in the same order: listed in `R9635_reading.md`, Notes. Two
disagreements:
- f. 20r l. 22 *darian todos los* (edition) = *pagarian todos los* (decipherment): the edition's first sign `∞` d is
  wrong there.
- `hec` = *Inglaterra* (edition, f. 20r l. 13) has nothing corresponding in the decipherment (*en poder […] quien
  quiera [?que] los*); withdrawn, `hec` stays unassigned.
The cipher writes *ahora* (a-h-o-r-a) where the decipherer wrote *agora*; the reading keeps the decipherer's word.

## 3. Key values (proposed; key_codes.tsv not edited)

Adopted on the decipherment (each holds at its occurrences on ff. 20r-20v):
- `gim` = **suyos** (Tomokiyo "suquos?"): f. 20v *todos los suyos que … en Francia a la parte de*.
- `deg` = **visto** (d-block between `def` visorey and `dog` vimes; first word of the letter; once).
- `feb` = **tanto** (f-block between `fab` tene and `fib` tanta; once).
Sense-only, flagged for review: `tac` (f. 20v, before *los suyos*, in the slot of *tenian*), alphabetically odd.
Withdrawn: `hec` = Inglaterra (this folder's 20 Sept value); `cag` = xxx (edition, "probable") is not supported: the
decipherment has no xxx at that place (*todos los xx mil ducados*), so `cag` stays open.

## 4. Reading and scores

`R9635_reading.md`: the decipherment's text in its spelling, abbreviations expanded, tear and uncertain words marked.
Word alignment (`research/reading_audit/b23_sanchez_align.py`): 283 unbracketed reading words, 0 not carried by the
decipherment.

| | clean-sentence share |
|---|---|
| before | no reading body (fragment table only) |
| b17 plain (`LANG_=es`) | 0.417 (10/24), hole rate 0.148 |
| b17 `HOLES=1` (explicit holes only) | **0.833 (20/24)**, hole rate 0.037 |
| `_check_reading.py --file` | 0.44 |

The plain figure falls on period spelling the Spanish list does not know (tardavan, havian, deven, rogava,
assentada, pagavan, escrive, restituydas) and on the clitic forms (dixeles, respondieronme, replicaronme). The body is
all cipher text (the clear Pace paragraph of f. 21r is not part of it), so the cipher-only share is the same figure.
Sentences hold throughout except the torn passage (ll. 9-10).

**Look-alike letters: 0.** The reading rests on the decipherment's clear court hand, not on sign values; the four
uncertain words are marked `[?…]` rather than resolved.

## Open

- the tear on f. 22r ll. 9-10 (about ten words): blocker **not-attempted**: the same passage stands in cipher on
  f. 21r (P2 right, ll. under the gloss *fuessen restituydas sus tierras*), which was not read sign by sign in this pass.
- *[?…] [?bastar]* (l. 12), *[?tenido]*, *[?Menorami]*, *[?Lucerna]*: hand uncertain at DECODE's resolution
  (blocker illegible; the cipher of f. 20v could settle *tenido* and the name).
- The cipher of f. 21r beyond the glossed lines was not aligned word by word with the decipherment.
