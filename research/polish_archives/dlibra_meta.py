"""Print the metadata block of dLibra edition pages.

    python research/polish_archives/dlibra_meta.py <edition-url> [...]
"""
import html, re, sys, urllib.request


def meta(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research sweep)'})
    s = urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')
    out = []
    for m in re.finditer(r'<h3[^>]*class="[^"]*dlteround[^"]*"[^>]*>(.*?)</h3>\s*(.*?)</(?:div|ul)>', s, re.S):
        pass
    # dLibra 6 renders metadata as <div class="dlibra-tabs__content ..."> with <h3>label</h3> <p>value</p>
    for lab, val in re.findall(r'<h3 class="[^"]*">\s*(.*?)\s*</h3>(.*?)(?=<h3 class=|<div class="tab-content__footer|$)', s, re.S):
        v = re.sub(r'<[^>]+>', ' ', val)
        v = re.sub(r'\s+', ' ', html.unescape(v)).strip()
        lab = re.sub(r'<[^>]+>', '', lab).strip()
        if v and len(v) < 1500 and lab:
            out.append(f'{lab}: {v}')
    return out


if __name__ == '__main__':
    for u in sys.argv[1:]:
        print('==', u)
        for line in meta(u):
            print('  ', line)
