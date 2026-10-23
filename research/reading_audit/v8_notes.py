"""v8 (23 Oct 2026): NOTES.md blocks for the v8 decisions (v8_apply.py). Each edit asserts its anchor once.

    python research/reading_audit/v8_notes.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]


def edit(folder, block, status=None, repl=(), esc=None):
    p = ROOT / 'targets' / folder / 'NOTES.md'
    t = p.read_text(encoding='utf8')
    nl = '\r\n' if '\r\n' in t else '\n'
    t = t.replace('\r\n', '\n')
    if status:
        old, new = status
        assert t.count(old) == 1, (folder, old); t = t.replace(old, new)
    for old, new in repl:
        assert t.count(old) == 1, (folder, old); t = t.replace(old, new)
    block = block.strip() + '\n\n'
    if '\n## Remaining gaps' in t:
        i = t.index('\n## Remaining gaps') + 1
        t = t[:i] + block + t[i:]
    else:
        t = t.rstrip('\n') + '\n\n' + block
    if esc:
        m = re.search(r'^## Escalation\n', t, re.M)
        assert m, folder
        n = re.search(r'^## ', t[m.end():], re.M)
        j = m.end() + n.start() if n else len(t)
        seg = t[:j].rstrip('\n')
        t = seg + '\n' + esc + '\n' + ('\n' if n else '') + t[j:]
    p.write_text(t.replace('\n', nl), encoding='utf8')
    print('notes', folder)


H = '## Verification v8, 23 Oct 2026'

edit('rennes1563', H + """

The translation wave could not translate f. 55, Colbert 390 pp. 357-358 and Colbert 392 p. 231 because they do not read.
Its partial readings (`f55_reading.md`, `c390_p357_p358_reading.md`, `c392_p231_bourdin_reading.md`: the `aligned/`
files put into sentences, `~` probable words and `{n}` runs as holes) score **0.50, 0.27 and 0.17** clean sentences on
explicit holes (`research/reading_audit/v2_score.py`; plain 0.375, 0.133, 0.167; hole rates 0.17-0.23). Holes in most
sentences, and every key source is already tried (Escalation). **All three back to decoded, not read**; with p. 139 no
letter reads: class **not read**, method not solved (Tomokiyo's key applied, kept as an `outcome.parts` item),
`fraction_read` 0.658 -> 0. The partial readings are kept.""",
     status=('Status: read in part.', 'Status: not read (verify v8, 23 Oct 2026: all four letters decoded, not read; Tomokiyo\'s key applied).'),
     repl=[('- fr. 3181 f. 55 (0.80 sense):', '- fr. 3181 f. 55 decoded, not read (v8 23 Oct 2026: 0.50 clean sentences; 0.80 sense):'),
           ('- 500 Colbert 390 pp. 357-358 (0.82 / 0.76 sense):', '- 500 Colbert 390 pp. 357-358 decoded, not read (v8 23 Oct 2026: 0.27 clean sentences; 0.82 / 0.76 sense):'),
           ('- 500 Colbert 392 p. 231 (0.83 sense):', '- 500 Colbert 392 p. 231 decoded, not read (v8 23 Oct 2026: 0.17 clean sentences; 0.83 sense):')],
     esc='- [x] retry (23 Oct 2026, v8): the three letters\' partial readings scored on explicit holes (0.50, 0.27, 0.17); no new value or source; all decoded, not read')

edit('selve1535', H + """

The sweep's 0.57 for R3697 scored `READING_R3697.md` whole, where the clear text, the decipherer's glosses and the
struck runs sit in lower-case brackets and count as holes. The unstruck cipher written out as running text
(**`R3697_reading.md`**, holes and doubtful words marked) scores **0.733** on explicit holes (11/15), 0.667 plain, hole rate
0.089; with the clear-text leads kept, 0.688 / 0.562. The sentences hold (the Swiss road; the Imperial ambassador's watch
and his urging the merchant to go to the French court; the informants reporting to the Turk). **Keeps read**; `reading`
points at the new file.""",
     esc='- [x] retry (23 Oct 2026, v8): R3697 unstruck cipher written out as running text and rescored (0.733 explicit holes); keeps read')

edit('sessa1593', H + """

The translation wave could not translate no. 45. Its running text (`no45_reading.md`, from `sense.tsv`'s reading column)
scores **0.50** on explicit holes (7/14), 0.357 plain, hole rate 0.158: the opening (*con este achaque ... a costa de la
bolsa*), the residence passage and the close carry unresolved groups and nomenclature groups not on the f. 97 sheet
(ʃo, 9̈4, ʒe, Val, ral, ʃep, pir). No decipherment of no. 45 exists. **Back to decoded, not read**; nos. 79 and 47 stay
read; `fraction_read` 0.925 -> 0.750 (982 of 1,310 groups). The gap blocker `open-codes` (the doubtful syllables) is
renamed no-key-material.""",
     repl=[('(slips, ambiguous hooks), listed per line in sense.tsv - blocker: open-codes',
            '(slips, ambiguous hooks), listed per line in sense.tsv - blocker: no-key-material; no gloss or second copy settles them'),
           ('## Escalation', '- no. 45 decoded, not read (v8 23 Oct 2026: 0.50 clean sentences on explicit holes) - blocker: no-key-material; open groups not on the f. 97 sheet, no decipherment of no. 45\n\n## Escalation')],
     esc='- [x] retry (23 Oct 2026, v8): no. 45 running text scored on explicit holes (0.50); decoded, not read')

edit('siena14', H + """

The translation wave could not translate L01-L06. Their running text (`transcripts/no14_L01-L06_reading.md`, the second
pass with its tags as holes) scores **0.0** on explicit holes (0/7), hole rate 0.289: the gist holds, but every sentence
carries doubtful words resting on look-alike sign classes the DECODE image does not separate. **Back to decoded, not
read**; no line of the letter reads: class **not read**, method not solved (the ciphertext-only key kept as an
`outcome.parts` item), `fraction_read` 0.28 -> 0. L08-L26 still not re-compared sign by sign (not-attempted), so the
target is in progress.""",
     status=('Status: read in part — key recovered from the ciphertext alone;',
             'Status: in progress (not read: L01-L26 decoded, not read, verify v8 23 Oct 2026). Earlier: key recovered from the ciphertext alone;'),
     repl=[('- L08-L26 not re-compared sign by sign',
            '- L01-L06 decoded, not read (v8 23 Oct 2026: 0.0 clean sentences, hole rate 0.289) - blocker: illegible; doubtful words rest on look-alike sign classes Q/Q4, 8/TH, P/PHI\n- L08-L26 not re-compared sign by sign')],
     esc='- [x] retry (23 Oct 2026, v8): L01-L06 running text scored on explicit holes (0.0); decoded, not read')

edit('sperantio1534', H + """

The translation wave could not translate R9411 and R9412 from `reading_r9411.txt` / `reading_r9412.txt` (line numbers
and line-end breaks scored as holes: 0.455, 0.40). Rescored as running text (`research/reading_audit/v3b_lines.py`),
now written as **`r9411/R9411_reading.md`** and **`r9411/R9412_reading.md`** with `reading` pointed at them: R9411
**0.71** on explicit holes, hole rate 0.078, sentences hold (grade A); R9412 **0.648** (0.642 with the clear Latin cut),
hole rate 0.106-0.114, **marginal**: the opening, QUARTO, the Schmalz passage and the close build sentences, TERTIO
(ll. 12-17) and ll. 31-41 do not (grade B). Both keep read.""",
     esc='- [x] retry (23 Oct 2026, v8): R9411/R9412 rescored as running text (0.71, 0.648); both keep read, R9412 marginal')

edit('visconti1529', H + """

The sweep's 0.59 scored `fr3045_f28_reading.md`, the line-by-line first pass. The running text rewritten with the
push-pass readings of `fr3045_f28_final.md` (**`fr3045_f28_v2_reading.md`**) scores **0.778** on explicit holes (14/18),
0.278 plain (1528 Lombard spelling), hole rate 0.111. **Keeps read, marginal**: ll. 8-9 (*et pur al tuto ... cum
Urbino*), the *quanto ci è* clause and ll. 14-15 (*Designati ... as[?]sedio*) do not build; the rest does. `reading`
points at the new file.""",
     esc='- [x] retry (23 Oct 2026, v8): f. 28 running text rewritten with the push-pass readings and rescored (0.778); keeps read')

edit('soria1523', H + """

The translation wave could not translate R9494-96. `R9494_reading.md` (from `measure/kb_r9494.txt`) scores **0.583** on
explicit holes (7/12), 0.333 plain, hole rate 0.118: the courier sentence and the money sentence carry three code-group
holes each, and the R9496 paragraph breaks off. The groups are spelled the same in all three copies and are not in the
R9844 crib. **Back to decoded, not read**; class read -> **read in part**, `fraction_read` 0.966 -> 0.873. R9498 beyond
block 1 is still not collated (not-attempted), so the target is in progress.""",
     status=('Status: read (5 Oct 2026:', 'Status: in progress (read in part since verify v8, 23 Oct 2026: R9494-96 decoded, not read). Earlier: read (5 Oct 2026:'),
     repl=[('- R9494-96 te, per, tep, zu, tol, the day count before \'dias\', and two phrases of R9496\'s extra paragraph - blocker: open-codes;',
            '- R9494-96 decoded, not read (v8 23 Oct 2026: 0.583 clean sentences): te, per, tep, zu, tol, the day count before \'dias\', and two phrases of R9496\'s extra paragraph - blocker: no-key-material;')],
     esc='- [x] retry (23 Oct 2026, v8): R9494 reading scored on explicit holes (0.583); decoded, not read')

edit('siena8', H + """

The translation wave flagged `texts/no08_reading.md` at 0.50: the two resolved name signs were written lower-case
(`[duca di Milano]`, counted as holes) and the run-edge `…` marks (clear text, not unread cipher) were counted too. With
the name signs capitalised and the marks dropped: **1.0** on explicit holes (4/4), 0.25 plain (1440 Sienese spelling),
hole rate 0. **A reading of fragments; keeps read** (grade A): each cipher run is a clause that holds, and every word is
confirmed letter for letter by the contemporary memorandum. Not 'not prose' (the runs are running sentences) and not
decoded-only (no hole).""",
     esc='- [x] retry (23 Oct 2026, v8): reading rescored with the name signs capitalised (1.0 explicit holes); keeps read')

edit('salviati1525', H + """

The excerpt of f54r held here (`lasry_entry.md`) does not read on its own: `v2_score.py` 0.0 on explicit holes and plain
(0/2 sentences, a `[?]` in each, hole rate 0.152). The reading is George Lasry's (3/8 pages deciphered in part, not in
the repository); the entry's state is left as his pointer, with a note saying so.""")
