"""v5 (b): nunzio1718 - join Lasry's decode rows of lasry/364D-<n>.txt (the line under each figure line) into one
stream per page: values joined, nulls '_' dropped, u/v -> u, a value 'a/b' -> a, '?' and 'N?' -> '[?]'; the
nomenclator groups of key_extra.txt and the adopted b22 changes (key_b22.tsv: 78 dal, 4029 pero, 4009 essendo,
4160 esercit) applied on the figures; codes still open -> '[4238]'. Prints it (for word division by hand) and the
plain score of the stream (_check_reading, Viterbi split of unspaced text).

    python research/reading_audit/v5b_nunzio_rows.py <n> [--show] [--lines]     --lines: one output line per figure line
"""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
T = ROOT / 'targets' / 'nunzio1718'
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b\nunzio1718')
SCR.mkdir(parents=True, exist_ok=True)
OV = {}
for l in (T / 'key_extra.txt').read_text(encoding='utf8').splitlines():
    m = re.match(r'^(\d+)\s*=\s*(.+?)\s*$', l)
    if m: OV[m.group(1)] = m.group(2)
OV.update({'78': 'dal', '4029': 'però', '4009': 'essendo', '4160': 'esercit'})


def stream(n, per_line=False):
    ls = (T / 'lasry' / f'364D-{n}.txt').read_text(encoding='utf8', errors='replace').splitlines()
    out = []
    for i, l in enumerate(ls):
        if l.startswith('#IMAGE') and re.search(r'\d+[rv]\.jpg', l):
            out.append('\n\n[' + l.split(':', 1)[1].strip().replace('.jpg', '') + ']\n'); continue
        if l.startswith('<CLEARTEXT'):
            out.append('\n{' + l[11:].rstrip('>').strip() + '}\n'); continue
        if not re.match(r'^[\d ?\-]+\|\s*$', l) or i + 1 >= len(ls): continue
        figs = l.split('|')[0].split()
        vals = ls[i + 1].split('|')[0].split()
        s = ''
        for k, v in enumerate(vals):
            f = figs[k] if k < len(figs) else ''
            if v == '_' or f == '3': continue
            if f in OV: v = OV[f]
            if re.fullmatch(r'\d+\?|\?', v) or v == '-': s += ' [?] ' if v != '-' else ''; continue
            m = re.fullmatch(r'<(\d+)>', v)
            if m: s += f' [{m.group(1)}] '; continue
            v = v.replace('u/v', 'u').split('/')[0]
            s += (' ' + v + ' ') if (v[:1].isupper() or '.' in v) else v
        out.append(s + ('\n' if per_line else ''))
    return re.sub(r'[ \t]+', ' ', ''.join(out))


if __name__ == '__main__':
    n = sys.argv[1]
    txt = stream(n, '--lines' in sys.argv)
    o = SCR / f'364D-{n}_rows.md'
    o.write_text('## Reading\n' + re.sub(r'^\[.*\]$|^\{.*\}$', '', txt, flags=re.M) + '\n', encoding='utf8')
    if '--show' in sys.argv: print(txt)
    sys.path.insert(0, str(HERE)); import v2_score as v
    v.cr.lexicon('it')
    r = v.cr.score_text(v.holes(v.body_of(o.read_text(encoding='utf8'))), 'it')
    print(n, 'R%d' % (153 + int(n)), 'plain', r['clean_share'], f"({r['clean']}/{r['sentences']})", r['words'], 'words')
