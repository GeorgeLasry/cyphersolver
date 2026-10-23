"""b05: word-by-word check of the Schenck readings against what carries them.

For each reading (targets/schenck1706/reading/R74xx_reading.md, body only) every unbracketed word is looked up in
(a) the diplomatic transcription transcr/R74xx.txt, (b) the 'now' column of reading/R74xx_corrections.tsv (words read
on the images on 22 Oct 2026) and (c) the decodes of the letter-table runs (two-digit numbers 7-79 in the
transcription, decoded with key.py's table, any word division). Words found nowhere are printed for a hand check:
each must be either a supplied word put in brackets or a word read on the image and added to the corrections file.

    python research/reading_audit/b05_align.py R7486 [R7488 ...]
"""
import re, sys, pathlib, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'schenck1706'
ALPH = 'abcdefghiklmnopqrstuwxyz'


def let(n):
    n = int(n)
    if n == 70: return 'w'
    if n in (76, 77, 78): return 'y'
    if n == 79: return 'z'
    return ALPH[(n - 7) // 3] if 7 <= n <= 69 else ''


def norm(w):
    w = unicodedata.normalize('NFKD', w.lower())
    w = ''.join(c for c in w if not unicodedata.combining(c))
    return w.replace('ÿ', 'y').replace('j', 'i').replace('v', 'u').replace('w', 'u').replace('ß', 'ss')


def main(rec):
    body = (T / 'reading' / f'{rec}_reading.md').read_text(encoding='utf8')
    body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', body, re.S | re.M).group(1)
    tr = (T / 'transcr' / f'{rec}.txt').read_text(encoding='utf8')
    cor = T / 'reading' / f'{rec}_corrections.tsv'
    cortext = cor.read_text(encoding='utf8') if cor.exists() else ''
    runs = ''
    for line in tr.splitlines():
        line = re.sub(r'\([^)]*\)', ' ', line.split('     ')[0])
        nums = re.findall(r'(?<![\d<{])\b(\d{1,2})\b(?![\d>}])', line)
        runs += ''.join(let(n) for n in nums) + ' '
    joined = re.sub(r'\s*\([^)]*\)', ' ', tr)
    joined = re.sub(r'(?m)^\[[^\]]*\]\s*', '', joined)
    joined = re.sub(r'[-=]\s*\n\s*', '', joined)
    pool = norm(joined + ' ' + tr + ' ' + cortext.replace('/', ' ').replace('-', ''))
    pool = pool.replace('ae', 'a').replace('oe', 'o').replace('ue', 'u') + ' ' + pool
    runsn = norm(runs).replace(' ', '')
    # drop bracketed material, codes and signs
    plain = re.sub(r'\[[^\]]*\]|\{[^}]*\}|<[^>]*>', ' ', body)
    miss = []
    for w in re.findall(r"[^\W\d_]+", plain):
        n = norm(w).replace('ae', 'a').replace('oe', 'o')
        if len(n) < 2: continue
        if re.search(r'(?<![a-z])' + re.escape(n), pool) or (len(n) >= 3 and n in runsn):
            continue
        miss.append(w)
    print(rec, len(miss), 'words not found in transcription / corrections / run decodes:')
    print('   ', ' '.join(miss))


if __name__ == '__main__':
    for r in sys.argv[1:]:
        main(r)
