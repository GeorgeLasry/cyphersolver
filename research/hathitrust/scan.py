"""Scan archive.org djvu text of printed calendars (copies of Hathi volumes) for 'undeciphered cipher' notes.
usage: python scan.py "<archive.org query>" [rows]   or   python scan.py id:<identifier> id:<identifier> ...   (<=1 req/s)"""
import sys, re, json, time, urllib.request, urllib.parse
UA = {'User-Agent': 'Mozilla/5.0 (cipher-catalogue research; dnbourdeau@gmail.com)'}
PAT = re.compile(r"(ndeci?y?phered|not (?:been )?deci?y?phered|cipher[^.\n]{0,25}(?:unread|unsolved|not (?:been )?(?:read|solved))"
                 r"|chiffre non|non d[eé]chiffr|nicht entziffert|ungel[oö]st|non decifrat|sin descifrar|no descifrad|undecyphered|not decyphered"
                 r"|cipher[^.\n]{0,30}no (?:key|decipher)|\(in cipher\)[^.\n]{0,40}(?:not|un))", re.I)


def get(u):
    time.sleep(1.1)
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read()


def main(args):
    ids = [x[3:] for x in args if x.startswith('id:')]
    if not ids:
        rows = int(args[1]) if len(args) > 1 else 10
        q = urllib.parse.quote(args[0] + ' AND mediatype:texts')
        j = json.loads(get(f'https://archive.org/advancedsearch.php?q={q}&fl[]=identifier&fl[]=title&fl[]=year&rows={rows}&output=json'))
        for d in j['response']['docs']:
            print('VOL', d['identifier'], d.get('year'), d.get('title', '')[:80]); ids.append(d['identifier'])
    for i in ids:
        try: t = get(f'https://archive.org/download/{i}/{i}_djvu.txt').decode('utf-8', 'replace')
        except Exception as e: print('ERR', i, e); continue
        n = 0
        for m in PAT.finditer(t):
            s = max(0, m.start() - 350)
            print(f'--- {i} @{m.start()} leaf~{t.count(chr(12), 0, m.start()) + 1}\n' + re.sub(r'\s+', ' ', t[s:m.end() + 200])); n += 1
            if n > 25: break
        print('DONE', i, len(t), n, flush=True)


main(sys.argv[1:])
