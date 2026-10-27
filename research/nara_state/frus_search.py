"""Harvest FRUS (history.state.gov) full-text search hits for cipher-trouble phrases.

    python frus_search.py            # writes frus_hits.json (doc id, title, date, snippet per phrase)

10 results per page; pages fetched with ?start=N. 1 s between requests.
"""
import html, json, os, re, sys, time, urllib.parse, urllib.request

PHRASES = [
    '"not deciphered"', '"undeciphered"', '"could not be deciphered"', '"cannot be deciphered"',
    '"not been deciphered"', '"not decoded"', '"undecoded"', '"could not be decoded"', '"not been decoded"',
    '"cipher text not"', '"code text not"', '"illegible in code"', '"unable to decipher"', '"unable to decode"',
    '"not decipherable"', '"indecipherable"', '"undecipherable"', '"key not found"', '"cipher not found"',
    '"no key"', '"partly in cipher"', '"partly in code"', '"in cipher" "not printed"', '"telegram in cipher"',
    '"unable to read" cipher', '"not yet deciphered"', '"not been able to decipher"', '"could not decipher"',
    '"undecyphered"', '"not decyphered"', '"cypher" "not"', '"mutilated" cipher', '"garbled" "not deciphered"',
    '"remainder of telegram garbled"', '"garbled in transmission"', '"garbled beyond"', '"hopelessly garbled"',
    '"entirely garbled"', '"badly garbled"', '"undecipherable"', '"key to the cipher"', '"lost cipher"',
    '"cipher key"', '"new cipher"', '"code book"', '"[cipher]"', '"in cipher"',
]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frus_hits.json')
MAXPAGES = int(os.environ.get('MAXPAGES', '30'))


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research; cyphersolver)'})
    for i in range(3):
        try:
            return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')
        except Exception as e:
            print('retry', e, file=sys.stderr); time.sleep(5)
    return ''


def parse(page):
    out = []
    parts = page.split('Resource ID')
    for k, blk in enumerate(parts[1:]):
        prev = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', parts[k])))
        m = re.search(r'([a-z0-9A-Z\-]+/(?:d|ch|comp|pg_)[A-Za-z0-9_\-]+)', blk)
        if not m:
            continue
        txt = html.unescape(re.sub(r'<[^>]+>', ' ', blk))
        snip = re.sub(r'\s+', ' ', txt.split('Keyword Relevance')[0])
        out.append({'id': m.group(1), 'head': prev[-300:], 'snippet': snip[:700]})
    # titles / dates precede each "Resource ID": capture from the previous block
    heads = re.findall(r'Recorded Date\s*</[^>]+>\s*<[^>]+>([^<]*)', page)
    return out


def main():
    hits = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    phrases = sys.argv[1:] or PHRASES
    for ph in phrases:
        if ph in hits and not os.environ.get('FORCE'):
            continue
        res, start = [], 1
        while True:
            q = urllib.parse.urlencode({'q': ph, 'within': 'documents', 'start': start})
            page = get('https://history.state.gov/search?' + q)
            m = re.search(r'of\s+(?:<[^>]+>\s*)?([\d,]+)\s*(?:</[^>]+>\s*)?results', page)
            total = int(m.group(1).replace(',', '')) if m else 0
            # title per hit
            items = parse(page)
            titles = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t))).strip()
                      for t in re.findall(r'<a[^>]+href="/historicaldocuments/[^"]+"[^>]*>(.*?)</a>', page, re.S)]
            res += items
            print(ph, start, total, len(items), file=sys.stderr)
            start += 10
            if not items or start > total or start > MAXPAGES * 10:
                break
            time.sleep(1)
        hits[ph] = {'total': total, 'hits': res}
        json.dump(hits, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
