"""Build reading.tsv for the three letters and print the measure.
Grades: T = TJ's interlinear over the group (Short); H = value attested by a decoding in another letter of the same code
(Pinckney); E = the PTJ editors' reading, not attested elsewhere; C = editors' or context conjecture; O = open."""
import csv, collections
OPEN_SHORT = {'401', '1083', '359', '199', '34', '724'}
out = []
for r in csv.DictReader(open('transcription/short_17920726_full.tsv', encoding='utf-8'), delimiter='\t'):
    if (r.get('note') or '').strip() == 'struck':  # Short's own struck group
        continue
    g = r['group'].strip()
    il = (r.get('interlinear') or '').strip()
    grade = 'O' if g in OPEN_SHORT else ('T' if il else 'E')
    out.append(('short_17920726', r['frame'], r['line'], r['pos'], g, il, grade))
for r in csv.reader(l for l in open('reading_pinckney_17930828.tsv', encoding='utf-8') if not l.startswith('#')):
    pass
rows = [l.rstrip('\n').split('\t') for l in open('reading_pinckney_17930828.tsv', encoding='utf-8') if not l.startswith('#')][1:]
for line, pos, g, reading, grade, *_ in rows:
    out.append(('pinckney_17930828', 'M30-002-0140', line, pos, g, reading, grade))
carm = [('009_0224', '108', 'Maryland', 'C'), ('009_0230', '108', 'Maryland', 'C'), ('009_0230', '223', 'Massachusetts', 'C'),
        ('009_0230', '273', 'majority', 'C'), ('009_0230', '597', '—', 'O')]
for i, (f, g, w, gr) in enumerate(carm, 1):
    out.append(('carmichael_17880414', f, '', str(i), g, w, gr))
with open('reading.tsv', 'w', encoding='utf-8', newline='') as fh:
    fh.write('letter\tframe\tline\tpos\tgroup\treading\tgrade\n')
    for o in out:
        fh.write('\t'.join(o) + '\n')
by = collections.defaultdict(collections.Counter)
for o in out:
    by[o[0]][o[6]] += 1
tot = collections.Counter()
for k, c in by.items():
    n = sum(c.values()); tot += c
    print(k, n, dict(c), 'read incl. C %.1f%%' % (100 * (n - c['O']) / n), 'excl. C %.1f%%' % (100 * (n - c['O'] - c['C']) / n))
n = sum(tot.values())
print('ALL', n, dict(tot), 'read incl. C %.2f%%' % (100 * (n - tot['O']) / n), 'excl. C %.2f%%' % (100 * (n - tot['O'] - tot['C']) / n))
