"""r2b: parse chomentowski1713/R7476.txt into per-line token streams (code, gloss G, key value K, clear words)."""
import re, pathlib, json, sys
T = pathlib.Path(__file__).resolve().parents[2] / 'targets/chomentowski1713/R7476.txt'

def items_C(s):
    return re.findall(r'"[^"]*"|\S+', s)

def parse():
    lines, page, cur = [], None, None
    for raw in T.read_text(encoding='utf8').splitlines():
        m = re.match(r'== p\. (\d+) ==', raw)
        if m: page = int(m.group(1)); continue
        if raw.startswith('== Counts'): break
        m = re.match(r'L(\d+) C: (.*)', raw)
        if m and page:
            cur = dict(page=page, line=int(m.group(1)), C=items_C(m.group(2)), G=[], K=[], P5=[]); lines.append(cur); continue
        m = re.match(r'\s+([GK]): (.*)', raw)
        if m and cur: cur[m.group(1)] = m.group(2).split(); continue
        m = re.match(r'\s+P5: (.*)', raw)
        if m and cur: cur['P5'].append(m.group(1))
    return lines

if __name__ == '__main__':
    for l in parse():
        codes = [c for c in l['C'] if not c.startswith('"')]
        flag = '' if len(codes) == len(l['G']) == len(l['K']) else f'  MISMATCH C{len(codes)} G{len(l["G"])} K{len(l["K"])}'
        if flag: print(l['page'], l['line'], flag, codes)
    print(len(parse()))
