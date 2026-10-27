"""Group the bulk scan's code-like frames by item (a microfilm reel or volume) for triage.

    python research/nara_reels/aggregate.py <rg> [--min 3] > out/agg_rg_<rg>.tsv

One row per item with at least --min flagged frames: publication, item title, series/file-unit titles, flagged
frame count, how many are "solid" (few words, so no clear text or interlinear decipherment on the frame), the frame
files, and the item's naId.
"""
import collections, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(rg, mn):
    items = collections.OrderedDict()
    for line in open(os.path.join(HERE, 'out', f'rg_{rg}.jsonl'), encoding='utf-8'):
        h = json.loads(line)
        if h['kind'] != 'frame':
            continue
        it = items.setdefault(h['naId'], {'h': h, 'frames': [], 'solid': 0})
        it['frames'].append(h['file'] or '')
        if h['words'] < h['nums']:
            it['solid'] += 1
    print('\t'.join(['naId', 'pub', 'flagged', 'solid', 'item', 'parent', 'frames']))
    for naid, it in items.items():
        if len(it['frames']) < mn:
            continue
        h = it['h']
        fr = sorted(f.rsplit('-', 1)[-1].split('.')[0] for f in it['frames'])
        print('\t'.join([str(naid), ','.join(h['microform']) or '-', str(len(fr)), str(it['solid']),
                         (h['title'] or '')[:90], ' > '.join(a[:50] for a in h['ancestors'][1:]),
                         ' '.join(fr)[:400]]))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    mn = int(a[a.index('--min') + 1]) if '--min' in a else 3
    main(a[0], mn)
