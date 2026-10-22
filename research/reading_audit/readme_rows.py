"""Move README Results rows to their new method section after the reading audit (22 Oct 2026), and say why.

For every target whose outcome method or class the audit changed (against origin/main), its row in the old method's
section gets the new extent and a lead note, and moves to the section of the new method. matignon1586 was done by hand.
    python research/reading_audit/readme_rows.py
"""
import json, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
EXTENT = {'read': 'complete', 'read in part': 'partial', 'not read': 'none', 'already solved': None}
SKIP = {'matignon1586'}


def old_outcome(folder):
    r = subprocess.run(['git', 'show', f'origin/main:targets/{folder}/profile.json'], capture_output=True, cwd=ROOT)
    try: return json.loads(r.stdout.decode('utf-8')).get('outcome') or {}
    except ValueError: return {}


def main():
    folders = set()
    for f in (ROOT / 'research' / 'reading_audit').glob('relabel_[0-9].txt'):
        folders |= set(f.read_text().split())
    lines = (ROOT / 'README.md').read_text(encoding='utf-8').split('\n')
    heads = {l[4:].strip().lower(): i for i, l in enumerate(lines) if l.startswith('### ')}
    moves = []
    for folder in sorted(folders - SKIP):
        p = ROOT / 'targets' / folder / 'profile.json'
        if not p.exists(): continue
        new, old = json.loads(p.read_text(encoding='utf-8'))['outcome'], old_outcome(folder)
        if (new.get('method'), new.get('class')) == (old.get('method'), old.get('class')): continue
        idx = [i for i, l in enumerate(lines) if l.startswith('| ') and f'(targets/{folder}/)' in l]
        if not idx: continue
        # the row in the old method's section (a split entry has one row per part)
        def section(i): return max((h for h in heads.values() if h < i), default=-1)
        old_h = heads.get((old.get('method') or '').lower())
        pick = [i for i in idx if section(i) == old_h] or idx[:1]
        i = pick[0]
        decoded = [t.get('label') or '/'.join(map(str, t['doc'] if isinstance(t.get('doc'), list) else [t.get('doc')]))
                   for t in new.get('texts') or [] if t.get('state') == 'decoded, not read']
        note = (f"**Reading audit, 22 Oct 2026** (George Lasry: a reading must build coherent sentences): "
                f"{new.get('class')}, {new.get('method')} (was {old.get('class')}, {old.get('method')})"
                + (f"; decoded, not read: {', '.join(map(str, decoded[:8]))}{' …' if len(decoded) > 8 else ''}" if decoded else '')
                + '. ')
        cells = lines[i].split(' | ')
        if len(cells) >= 6:
            ext = EXTENT.get(new.get('class'))
            if ext: cells[3] = ext
            cells[4] = note + cells[4]
            row = ' | '.join(cells)
        else:
            row = lines[i]
        moves.append((i, row, (new.get('method') or '').lower(), folder))
    # remove from the old place (bottom up), then insert at the end of the new section's table
    for i, _, _, _ in sorted(moves, reverse=True): del lines[i]
    for _, row, meth, folder in moves:
        heads = {l[4:].strip().lower(): k for k, l in enumerate(lines) if l.startswith('### ')}
        h = heads[meth]
        nxt = min([k for k in heads.values() if k > h] + [len(lines)])
        last = max(k for k in range(h, nxt) if lines[k].startswith('| '))
        lines.insert(last + 1, row)
        print(f'{folder}: -> {meth}')
    (ROOT / 'README.md').write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    main()
