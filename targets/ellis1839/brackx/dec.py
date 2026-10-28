"""Decode an image transcription with the jqa table plus the values found here; unknown groups shown as <n>."""
import sys
tab = {}
for l in open('code_table.tsv'):
    p = l.rstrip('\n').split('\t')
    if len(p) >= 2 and p[0].isdigit(): tab[int(p[0])] = p[1]
tab.update({1261: ',', 1264: '.', 647: 'mil', 116: 'congress', 1152: 'por', 261: 'son', 311: 'fam', 886: 'lin', 850: 'disposed', 750: 'resolved',
            516: 'notwithstanding', 1262: ';', 363: 'nou', 768: 'tur', 1268: '()',
            1488: 'upon', 309: 'faith', 1511: 'action', 803: 'dai', 832: 'dev', 1263: ':', 79: 'nevertheless', 741: 'rel', 306: 'faction', 1337: 'bit', 410: 'nat', 28: 'opportunity', 1267: '—', 292: 'even', 604: 'mad', 427: 'neighbors', 944: 'joy', 566: 'tir', 320: 'fear', 1530: 'al', 1023: 'ch', 785: 'bur', 985: 'forth', 196: 'hor', 470: 'vil', 344: 'firm', 795: 'dom', 912: 'restore'})
for l in open('ellis_values.tsv'):
    if l.startswith('#') or not l.strip(): continue
    g, v = l.split('\t')[:2]
    tab[int(g)] = '' if v == '0' else v   # values from the 1836 despatches override the table
for f in sys.argv[1:]:
    out = []
    for l in open(f):
        if l.startswith('#'): continue
        out.append(' '.join(tab.get(int(x), f'<{x}>') for x in l.split() if x.isdigit()))
    print(f'== {f}'); print('\n'.join(out))

