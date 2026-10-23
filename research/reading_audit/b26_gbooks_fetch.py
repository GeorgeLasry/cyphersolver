"""b26: fetch Google Books page images through the jscmd=click3 endpoint (signed page-image URLs), into a scratch dir.

    python research/reading_audit/b26_gbooks_fetch.py <book id> <out dir> PA562 PA578 ...

Used for Puig y Puig 1920 (CuOlkxWnk-EC), comuel1415 and comuel1416, 23 Oct 2026. The click3 answer lists the asked
page and its neighbours; every listed page with a src is saved at w=1600 as <pid>.png. Images stay in the scratchpad.
"""
import json, pathlib, sys, urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read()


def main(book, out, *pages):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for pg in pages:
        j = json.loads(get(f'https://books.google.com/books?id={book}&pg={pg}&jscmd=click3'))
        for p in j['page']:
            if 'src' in p and not (out / f"{p['pid']}.png").exists():
                (out / f"{p['pid']}.png").write_bytes(get(p['src'] + '&w=1600'))
                print('saved', p['pid'])


if __name__ == '__main__':
    main(*sys.argv[1:])
