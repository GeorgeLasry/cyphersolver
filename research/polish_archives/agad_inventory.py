"""Grep AGAD's online inventories (https://www.agad.gov.pl/inwentarze/<name>.xml, HTML despite the extension)
for cipher terms, printing each archival unit that matches.

    python research/polish_archives/agad_inventory.py <dir-with-downloaded-xml> [name ...]

The list of inventory files comes from https://agad.gov.pl/pomoce/eagpln.xml and inwentarze/testy.html.
Units are the <hr>-separated blocks; tags are stripped.
"""
import html, os, re, sys

RX = re.compile(r'szyfr|chiffr|ziffer|cyfrą|cyframi|cyfrach|kryptogra|tajnopis|cifr|zifra', re.I)


def units(path):
    s = open(path, encoding='utf-8', errors='replace').read()
    title = re.search(r'<title>(.*?)</title>', s, re.S)
    for blk in re.split(r'<hr[^>]*>', s):
        t = html.unescape(re.sub(r'<[^>]+>', ' ', blk))
        t = re.sub(r'\s+', ' ', t).strip()
        if t:
            yield (title.group(1).strip() if title else ''), t


def main(d, names):
    names = names or sorted(n[:-4] for n in os.listdir(d) if n.endswith('.xml'))
    for n in names:
        for title, t in units(os.path.join(d, n + '.xml')):
            if RX.search(t) and len(t) < 4000:
                print(f'[{n}] {t}\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
