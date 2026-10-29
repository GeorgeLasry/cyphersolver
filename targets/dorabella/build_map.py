"""Build hypothesis-map.html from map_template.html and the project's own records.

Reads ct.txt, ct_measured.txt, disputes.json, disputes_merged.json, runs/ledger.tsv and runs/loop.md; adds the
question structure, coverage matrix and recheck notes below; writes the data into the template.

python targets/dorabella/build_map.py
"""
import os, re, csv, json

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)

ct_lines = [l.split() for l in open(P('ct.txt')).read().strip().splitlines()]
ct = sum(ct_lines, [])
me = open(P('ct_measured.txt')).read().split()
O = 'ABCDEFGH'
flips = sorted({j for i in range(1, 87) if (O.index(ct[i][0]) - O.index(ct[i - 1][0])) % 8 == 4 for j in (i - 1, i)})
sets = {
    'flips': flips,
    'doubles': sorted({j for i in range(86) if ct[i] == ct[i + 1] for j in (i, i + 1)}),
    'disputes': sorted(int(k) for k in json.load(open(P('disputes.json')))),
    'merged': sorted(int(k) for k in json.load(open(P('disputes_merged.json')))),
    'measured': [i for i, (a, b) in enumerate(zip(ct, me)) if a != b],
    'jager': [9, 22, 23, 24, 31, 33, 66, 77, 84, 85],
    'last2': [85, 86], 'first4': [0, 1, 2, 3], 'mother': list(range(47, 53)), 'all': list(range(87)),
}

# ---------------------------------------------------------------- ledger
FIX = {
    'arcs as ternary triplets, phase 0': 'Rechecked with 15 shuffles: negative.',
    'semaphore-like unordered pairs, phase 0': 'Rechecked: beats 40 pair-keeping shuffles (P < 0.025), but one test of about eight in the round, controls 16–98%, gibberish. Not significant.',
    'semaphore-like unordered pairs, phase 1': 'Rechecked with pair-keeping shuffles: no power (controls 2–14%).',
    'unordered orientation pairs ph0 (15 nulls)': 'Then 40 pair-keeping shuffles: P < 0.025, not significant across the round; gibberish.',
    'unordered orientation pairs ph1 (15 nulls)': 'No power: controls recovered 2–14%.',
    'unordered pairs ph0, doublet nulls': 'Then 40 pair-keeping shuffles: P < 0.025, not significant across the round; gibberish.',
    'polygraphic units: nomenclator (32 units)': 'Rechecked: no power, controls only 16–28% similar to the truth.',
}
ledger = []
with open(P('runs', 'ledger.tsv'), encoding='utf-8') as f:
    rd = csv.reader(f, delimiter='\t'); next(rd)
    for x in rd:
        if len(x) < 6:
            continue
        def rng(s):
            m = re.match(r'(-?[\d.]+)\.\.(-?[\d.]+)', s or '')
            return [float(m.group(1)), float(m.group(2))] if m else None
        try:
            D = float(x[2])
        except ValueError:
            D = None
        note = x[7] if len(x) > 7 else ''
        rnd, name, verdict = x[0], x[1], x[5]
        diag = rnd in ('11', '17', '25', '26', '29', '30', '31', '32', '35') or 'trigram' in name or 'Playfair' in name or verdict == 'excluded'
        fix = FIX.get(name)
        if rnd == '5' and verdict == 'no power':
            fix = 'Control encoder bug in this first pass; Dorabella and shuffle scores are valid. The two best were rechecked with valid controls (same round).'
        ledger.append(dict(round=rnd, name=name, D=D, nulls=rng(x[3]), ctl=rng(x[4]), verdict=verdict,
                           text=x[6][:80], note=note[:100], kind='diag' if diag else 'solver', fix=fix))

# ---------------------------------------------------------------- rounds
rounds = [dict(n='S', family='Steps 1–25: the first campaign',
               outcome="Simple substitution in six languages, Elgar's own table, rotations, transpositions, cribs, misread-tolerant solvers, the 1937 plate measured, the Pall Mall systems, Elgar's register, the opposite-flip signal found.",
               status='NEG')]
for line in open(P('runs', 'loop.md'), encoding='utf-8'):
    m = re.match(r'\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*(.+)\|\s*$', line)
    if not m:
        continue
    n, fam, hyps, out = m.groups()
    out_c = re.sub(r'\*\*', '', out).strip()
    low = out_c.lower()
    st = 'NP' if 'no power' in low or 'cannot discriminate' in low else 'DIAG' if 'diagnostic' in low or 'typical' in low else 'NEG'
    rounds.append(dict(n=n, family=fam.strip(), hyps=hyps.strip(), outcome=out_c, status=st))

# ---------------------------------------------------------------- questions
def B(name, status, desc, ev, rounds=(), signs=None, signsNote=None):
    return dict(name=name, status=status, desc=desc, ev=ev, rounds=list(rounds), signs=signs, signsNote=signsNote)


questions = [
    dict(id='q1', n='Q1', layers='L0', title='Is it a message?',
         answer="<b>Yes, almost certainly.</b> The signs are ordered like language, not scribbled or doodled, and they look like English letters under a key that flips common neighbours to opposite sides of the dial.",
         branches=[
             B('Random scribble', 'X', 'The signs repeat in pairs far more than chance: 19 repeated pairs against 11.2 expected (P = 0.004).', 'S7'),
             B('Hand doodle', 'X', 'A doodling hand turns gradually. Dorabella turns more than chance, with no gradual sweeps at all.', 'S16', signs='flips', signsNote='Highlighted: the signs in opposite flips.'),
             B('Simple pseudo-writer', 'NEG', 'A writer who flips often and sometimes repeats reproduces the flips but not the repeated pairs (9.4 against 19). P = 0.008.', 'R25', [25]),
             B('English letters', 'DIAG', "On the statistics no key can change, Dorabella is a typical sample of English letters (P 0.84) and of Elgar's own letters (P 0.89). Caveat from Jager 2026: shuffles that keep Dorabella's adjacent pairs do as well (p = 0.085), so a writer with strong pair habits fits these statistics too.", 'R11 · R20 · Jager 2026', [11]),
             B('The opposite flips', 'DIAG', 'Consecutive signs face opposite ways 27 times against 12.6 expected. English under a key that puts common neighbours on opposite sides reproduces this and the other five statistics at once (P 0.71).', 'R26 · R17 · S16 · S22', [26], 'flips', 'Highlighted: the 49 signs that take part in an opposite flip.'),
             B('Pair-habit writer', 'NP', "A writer choosing each sign from the last, with strong habits. Shuffles keeping Dorabella's adjacent pairs match it on every statistic tried, including repeats at gaps 2–4 and skip-pairs (R35), and on Jager's tests. With a fixed-table English message now strained (R31–R33), this is the leading alternative: a deliberate sequence with no message.", 'R35 · R20 · Jager 2026', [35], 'flips', 'Highlighted: the flips such a writer would produce by habit.'),
             B('Human fake-cipher data', 'OPEN', 'Needs recordings of people inventing cipher-like squiggles.', '—'),
         ]),
    dict(id='q2', n='Q2', layers='L1', title='Is the transcription right?',
         answer="<b>Probably close, not certainly.</b> Every disputed and measured reading fails. A handful of misreads is unlikely; ten or more can't be decided from 87 signs.",
         branches=[
             B('Five-reader consensus', 'NEG', 'The input to every test. Negative under every key and order tried.', 'S2–S8', signs='all', signsNote='Every sign is in play.'),
             B('Disputed readings', 'NEG', 'All 2,048 combinations of the 11 positions where Schmeh and the Elgar-key transcription disagree.', 'S9', signs='disputes', signsNote='Highlighted: the 11 disputed positions.'),
             B('Measured 1937 plate', 'NEG', "Each sign's angle measured on the first-edition scan; 17 reclassified; 23 positions solved jointly.", 'S11', signs='measured', signsNote='Highlighted: the 17 signs the measurement reclassifies.'),
             B('Up to six misreads', 'NEG', 'Large parallel search (230 runs per target): Elgar-letter controls with 6 misreads recovered 89–95%; Dorabella −2.548, no better than its shuffles (−2.586) and far below the controls. Excluded with power.', 'R33 · R21', [33, 21], 'merged', 'Highlighted: the 23 doubtful positions.'),
             B('Misreads of either kind', 'NEG', 'Up to six slips in orientation or arc count, at full power: controls recovered 4 of 4, the note at shuffle level (R54). Eight: controls readable but under 90%, a shuffle beats the note (R56). Ten or more: no power even at full compute (R55).', 'R54 · R55 · R56', [54, 56, 55], 'merged', 'Highlighted: the 23 doubtful positions.'),
             B('Arc-count misreads', 'NEG', 'Up to six signs with one arc too many or too few: three independent searches on the note give three unrelated texts, and a shuffle scores higher than all three.', 'R53', [53], 'merged', 'Highlighted: the 23 doubtful positions.'),
             B("Jager's 2026 transcription", 'NEG', 'Independent reading with 9 uncertain signs; differs from the consensus at signs 23, 32, 34, 85, 86. Same large search: −2.556, no reading.', 'R33 · Jager 2026', [33], 'jager', "Highlighted: Jager's doubtful signs."),
             B('The 1949 second dot', 'OPEN', "A second dot at line 2, sign 11 or 12, appears in the 1949 edition but not in the 1947 copy (Belanger, Pelling). Read as a sentence break after sign 40 or 41 it gives nothing (R36); what the dot is remains open until the plates are compared.", 'R36 · Cipher Mysteries thread', [36], [39, 40], 'Highlighted: line 2, signs 11 and 12.'),
             B('Ten or more misreads', 'NP', 'With 48 doubtful positions the solver recovers English only 0–83% of the time. Too much freedom for 87 signs.', 'R27 · S5–S6', [27], 'merged', 'Highlighted: the 23 doubtful positions.'),
             B('Cleaner image', 'OPEN', 'A greyscale plate from the 1946 or 1949 edition would settle the doubtful positions.', '—', signs='merged', signsNote='Highlighted: what a better image would settle.'),
         ]),
    dict(id='q3', n='Q3', layers='L2 · L6', title='What kind of text is it?',
         answer="<b>Most likely English letters, yet no form of English reads.</b> Standard, Elgar's own, phonetic, abbreviated and reversed English, eleven other languages, known quotations, melodies and cribs all fail.",
         branches=[
             B('Standard English', 'NEG', 'Controls recovered at 97–100%; Dorabella scores like its shuffles.', 'S2–S3', [5, 6, 14]),
             B("Elgar's own register", 'NEG', 'A model trained on his 23 letters to the Pennys ("warbling wigorously … wunce a week").', 'S14 · R27', [27]),
             B('Reversed and back-slang', 'NEG', 'The whole text reversed, and each word written backwards.', 'S3 · R7', [7]),
             B('Skeleton and abbreviations', 'NEG', 'English without vowels, and the first three letters of each word. At full power the skeleton came closest of any branch, but its decode splits into word skeletons no better than shuffles do (−3.24 per letter against −2.91 to −3.63; real controls −2.28 to −2.80).', 'R39 · R38 · R7', [39, 38, 7]),
             B('Phonetic English', 'NEG', 'Sounds grouped into 25 classes; rerun at full power with controls from Elgar’s letters: −2.853, far below the controls (−1.97 to −2.35). With all 39 sounds the test has no power.', 'R43 · S24', [43]),
             B('Syllables', 'NEG', 'Orientation as consonant class, arc count as vowel.', 'R20', [20]),
             B('Word initials', 'NP', 'A model of English word initials recovers its own controls only 1–48% of the time.', 'S18 · R22', [22]),
             B('Eleven other languages', 'NEG', 'Latin, French, German, Italian, Spanish, Dutch, Portuguese, Danish, Swedish, Welsh, Hungarian; all rerun at full power with own-language controls (R37, R45), Latin (R41) and French, German, Italian, Spanish (R57) also with misreads, and the main three with homophones (R42). Every decode segments into words like shuffles do.', 'R37 · R41 · R42 · R45 · R57 · S3 · R9', [37, 45, 41, 42, 57]),
             B('Polish', 'NEG', 'At full power (R45) its controls are recovered 3 of 4; Dorabella stays far below them.', 'R45 · R9', [45, 9]),
             B('A known quotation', 'NEG', "Every 87-letter window of the Bible, Shakespeare, a verse anthology, Longfellow, Tennyson, Browning, Elgar's letters and Powell. Best fit 37 of 87; shuffles 35; a real quotation 80.", 'R18 · R22', [18, 22]),
             B('Music: the Lullaby', 'NEG', 'The tune Elgar played that week as melody cribs, and its words (Alice Elgar’s lyric) as the plaintext and as cribs. No better than shuffles.', 'S20 · S25 · R40', [40]),
             B("Elgar's practice phrases", 'NEG', 'The test sentences in his cipher notebook ("a very old cypher", "do you go to london", "marco elgar") fit nowhere in Dorabella.', 'R40', [40]),
             B('Numbers or a date', 'NP', 'Digits carry no redundancy a test could use.', '—'),
             B('Floating cribs', 'NEG', '50 personal and situational words placed wherever they fit.', 'S7'),
             B('Openings', 'NEG', 'Only "dora" and "dear" fit the first signs, and nothing reads after them.', 'R10', [10], 'first4', 'Highlighted: the first four signs.'),
             B('Sign-offs', 'X', 'The last two signs differ, so "ee" is impossible, and every longer closing conflicts.', 'R10', [10], 'last2', 'Highlighted: the last two signs, H1 and A3.'),
             B('The July 1897 visit', 'NEG', '29 words from that week: kites, Boscobel, the oak, Caractacus, the lullaby. Best "mother" at sign 48; scraps only.', 'R24', [24], 'mother', 'Highlighted: where "mother" was placed.'),
             B('A second text', 'OPEN', 'The Courage cards. Needs museum access.', '—'),
             B('The Microcryptogram', 'OPEN', "A short text in the same symbols sold at Sotheby's (lot 92), mentioned by Pelling; not yet located or transcribed.", 'Cipher Mysteries thread'),
             B("Elgar's prose at 87 signs", 'DIAG', "Enciphered windows of Elgar's own letters are recovered at 90% or better only 42% of the time by the loop's solver (Gutenberg prose 58%). A failed solve is weaker evidence than it looks; round 31 asks whether failures are search or model failures.", 'R30 · R31'),
         ]),
    dict(id='q4', n='Q4', layers='L3 · L4 · L5', title='Which system made the signs?',
         answer="<b>None of the systems tested.</b> Substitution, Elgar's own table, keyed and running-key ciphers, Nihilist, Morse, fractionation and every transposition fail; Playfair and a scrambled version of his table are impossible.",
         branches=[
             B('One letter each', 'NEG', 'Simple substitution under one fixed table. At full power (3,680 long runs) the best is −2.71, below every real Elgar window (−1.80 to −2.56); a real solution would be found ~92% of the time.', 'R31 · R32 · S2–S3', [32, 31]),
             B('Homophones in a fixed table', 'NEG', 'Up to two signs per letter, 230 long runs per target: Elgar-letter controls with doubled common letters recovered 3 of 4 (83–99%); Dorabella −2.224, level with its shuffles, gibberish.', 'R34 · R42 · R46 · R7', [34, 42, 46, 7]),
             B("Elgar's own table", 'NEG', 'All 1,081,600 ordered layouts, with shifts and reversals.', 'S1 · R13', [13]),
             B('The turn between signs', 'NEG', 'The change in orientation from one sign to the next as the letter.', 'S21', signs='flips'),
             B('Note names and keyboard', 'NEG', 'Orientation as a–h (40,320 orders); a 3 × 8 keyboard (241,920).', 'R13', [13]),
             B('Bacon, ternary, Morse', 'NEG', 'Letters spread over several signs, and every Morse reading.', 'R1 · R2', [1, 2]),
             B('Sign pairs', 'NEG', 'Semaphore-like pairs beat 40 pair-keeping shuffles once; not significant across the round, and gibberish.', 'R1', [1]),
             B('Axis and arcs only', 'NP', 'Twelve signs for 24 letters makes English-like text from anything.', 'S17'),
             B('Digraphs and word signs', 'NP', 'Controls came back only 16–28% similar to the truth.', 'R15', [15]),
             B('Dial rotation', 'NEG', 'Periodic and progressive turns of the dial, whole text and per line.', 'S8 · R6', [6]),
             B('Roe grid with a keyword', 'NEG', 'All 5,040 group orders with keyword or dial keys; hidden English recovered 4 times out of 4.', 'S12'),
             B('Nihilist and COURAGE', 'NEG', 'Unknown keys, and the 27 keys from his world including COURAGE.', 'S12 · R23', [23]),
             B('Context keywords', 'NEG', 'Vigenère, Beaufort, autokey and the date 14.97 as keys.', 'R3', [3]),
             B('Running key', 'NEG', 'Every starting point in the Bible, Shakespeare, verse, prose and Powell.', 'R4', [4]),
             B('Mixed alphabets', 'NEG', "Keyword alphabets on Elgar's table, checked directly.", 'R19', [19]),
             B('His table, scrambled', 'X', 'His table does not even give English letter frequencies, so it cannot be his table with the order shuffled.', 'R18', [18]),
             B('Key change partway', 'NP', 'Two interleaved messages, or a new key per line: controls recovered 0–31%.', 'R16', [16]),
             B('Reversal, mirror, lines', 'NEG', 'Every line order, boustrophedon, mirror writing, upside-down lines, columns and diagonals; the main ones rerun at full power (R44, R48).', 'R44 · R48 · S3 · R5', [44, 48, 5]),
             B('Transposition', 'X', '5,913 columnar orders and rail fences. The written order already has the most repeated pairs, so nothing was scrambled.', 'R8', [8]),
             B('Misaligned streams', 'NEG', 'Arc counts shifted or reversed against the orientations.', 'R14', [14]),
             B('Null signs', 'NEG', 'Dropping each class, the rare signs, the five singletons (full power, R47), or every k-th sign.', 'R47 · S15 · R12', [47, 12]),
             B('Word spaces', 'NEG', 'No sign, and no flip, gives English word lengths.', 'R12 · S22', [12]),
             B('Block rearrangement', 'NEG', 'Arcs rotated or reversed inside blocks of 2 to 6.', 'R19', [19]),
             B('Playfair', 'X', 'Two identical signs would land inside one pair under every way of pairing.', 'R12', [], 'doubles', 'Highlighted: the four doubled pairs.'),
             B('Any table-changing key', 'X', 'Periodic dial, Vigenère, autokey, running key, Nihilist and progressive dial all wash the flips back to chance (7.7–11.5 against 27; P ≤ 0.001). Dorabella was written with one fixed table throughout.', 'R29', [], 'flips', 'Highlighted: the flips a changing key would have destroyed.'),
         ]),
]
for q in questions:
    for k, b in enumerate(q['branches'], 1):
        b['id'] = f"b-{q['id']}-{k}"

# ---------------------------------------------------------------- coverage
cols = ['Simple substitution', 'Homophonic', "Elgar's table", 'Dial rotation', 'Roe + keyword', 'Nihilist',
        'Keyword, autokey', 'Running key', 'Per-line keys', 'Transposition', 'Nulls, spaces', 'Misreads',
        'Fractionation, Morse', 'Known text, cribs']
E = ''
cov_rows = [
    ['English', ['NEG', 'NEG', 'NEG', 'NEG', 'NEG', 'NEG', 'NEG', 'NEG', 'NEG', 'X', 'NEG', 'NEG', 'NEG', 'NEG']],
    ["Elgar's register", ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, 'NEG', E, 'NEG']],
    ['Reversed, back-slang', ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Skeleton, abbreviations', ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Phonetic (25 classes)', ['NEG', E, E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Syllables', ['NEG', E, E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Word initials', ['NP', E, E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, 'NEG']],
    ['Latin', ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, 'NEG', E, E]],
    ['French', ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['German', ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Italian', ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Spanish', ['NEG', 'NEG', E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Six other European', ['NEG', E, E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Polish', ['NEG', E, E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, E]],
    ['Music', ['NP', E, E, 'X', 'X', 'X', 'X', 'X', 'X', E, E, E, E, 'NEG']],
]

frontier = [
    dict(rank=1, title='Saturation: the fixed-table branches are exhausted here', why='Every fixed-table branch that 87 signs can decide has been run at full power and is negative: English and Elgar (R32), misreads (R33), homophones (R34), five languages (R37), four plaintext forms (R38), the consonant skeleton settled on two criteria (R39), the Lullaby lyric and his practice phrases (R40).', status='done', ev='R31–R40'),
    dict(rank=2, title='Undecidable at 87 signs', why='Pair habit vs language (R35), a key that changes partway (R16), ten or more misreads (R27), homophones with misreads. No calculation on this text can separate these from noise.', status='blocked', ev='R16 · R27 · R35'),
    dict(rank=3, title='A second text in the same system', why="The Courage cards and the Sotheby's Microcryptogram. Any surviving key could be checked on two documents; this is the single most valuable item.", status='blocked', ev='outside'),
    dict(rank=4, title='Better images of the plate', why='Greyscale plates from 1946 and 1949 (the 1949 second dot) and the Elgar Museum photo, to settle the 23 doubtful signs.', status='blocked', ev='outside'),
    dict(rank=5, title='How people fake ciphers', why='Recordings of people inventing cipher-like squiggles, to test the leading alternative directly.', status='blocked', ev='outside'),
]
data = dict(frontier=frontier, ct=ct_lines, sets=sets, ledger=ledger, rounds=rounds, questions=questions,
            coverage=dict(cols=cols, rows=cov_rows))
tpl = open(P('map_template.html'), encoding='utf-8').read()
out = tpl.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
open(P('hypothesis-map.html'), 'w', encoding='utf-8').write(out)
print(f"hypothesis-map.html: {len(out):,} bytes; {len(ledger)} ledger rows "
      f"({sum(r['kind'] == 'solver' for r in ledger)} solver), {len(rounds)} timeline entries, "
      f"{sum(len(q['branches']) for q in questions)} branches")
