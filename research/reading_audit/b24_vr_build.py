"""b24 (vanreede1787): corrected group transcriptions of R1026/R1027 (DECODE transcription, J+ = 1, the label
corrections read on the images) and a group-by-group decode with key R1024 (b24_vr_key: slips fixed, nulls marked).
Writes targets/vanreede1787/R10xx_transcription_corrected.tsv, R10xx_corrections.tsv, R10xx_decode_b24.txt."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from b24_vr_decode import groups, word
from b24_vr_key import load
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vanreede1787'
# (DECODE label after J+ -> 1) -> corrected label(s), with the evidence
CORR = {
 'R1026': [('1?00', ['100'], 'image l.5 "J00": hooked 1 + 00 = 100 me ("elle me paroit bonne")'),
           ('21423068', ['2142', '3068'], 'image l.5: two groups "2142. 3068." run together by the transcriber'),
           ('4', ['4433'], 'image l.10: 4438 corrected by the writer to 4433 written above (dotted underneath); DECODE split it into four digits'),
           ('4', None, 'part of 4438/4433'), ('3', None, 'part of 4438/4433'), ('8', None, 'part of 4438/4433'),
           ('51?', ['513'], 'image l.15 "51B": the writer\'s flat-backed 3 (as in "B090"=3090 ceci on p.2); 513 ce qui'),
           ('308?9', ['3089'], 'p.2 l.1 "3089" (the ? is a stray mark); 3089 ce ("la conference de ce matin")')],
 'R1027': [('3?089', ['3089'], 'image l.1 "B089": flat-backed 3; 3089 ce ("ce matin")'),
           ('1?1021', ['1021'], 'image l.6 "J021": hooked 1; 1021 ou ("resolu ou non")'),
           ('0969', ['1969'], 'image l.8 "J969": hooked 1; 1969 Imperatrice (as at l.3 and l.4)')],
}
k, _ = load()
for rec in ['R1026', 'R1027']:
    rows, corr = [], []
    todo = list(CORR[rec])
    for it in groups(rec):
        if it[0] == 'c': rows.append(('C', it[1], '')); continue
        g, marks, orig = it[1], it[2], it[3]
        if todo and g == todo[0][0]:
            _, new, why = todo.pop(0)
            corr.append((orig.replace('J', 'J+'), ' '.join(new) if new else '(merged)', why))
            for n in (new or []): rows.append(('G', n, marks))
            continue
        rows.append(('G', g, marks))
    assert not todo, (rec, todo)
    with open(T / f'{rec}_transcription_corrected.tsv', 'w', encoding='utf8') as f:
        f.write('# %s groups, DECODE transcription with J+ read as 1 (the writer\'s hooked 1) and the corrections in %s_corrections.tsv; '
                'col 3 = the transcriber\'s bar marks (^_ bar above, __ bar below); C rows = clear text as DECODE has it\n' % (rec, rec))
        n = 0
        for kind, g, m in rows:
            if kind == 'G': n += 1; f.write(f'{n}\t{g}\t{m}\n')
            else: f.write(f'C\t\t{g}\n')
    with open(T / f'{rec}_corrections.tsv', 'w', encoding='utf8') as f:
        f.write('decode_label\tcorrected\tevidence\n')
        f.write('J+ (all)\t1\tthe hooked 1 of this hand; J=1 gives a key word that fits at every one of the %s occurrences (b24_vr_jcheck in the log)\n' % ('77' if rec == 'R1026' else '24'))
        for a, b, c in corr: f.write(f'{a}\t{b}\t{c}\n')
    with open(T / f'{rec}_decode_b24.txt', 'w', encoding='utf8') as f:
        n = 0
        for kind, g, m in rows:
            if kind == 'C': f.write(f'[clear: {g}]\n'); continue
            n += 1; f.write('%3d %-5s %-12s %s\n' % (n, g, m, word(k, g)))
    print(rec, sum(1 for r in rows if r[0] == 'G'), 'groups')
