"""The 1916 three-kana code, decoded with S. Tomokiyo's formula (Cryptiana, chinesecrypto_e2.htm, added 23 Sept 2026).

A Chinese character's standard telegraph code c (1..9199) is written as three kana:
  k1 = S1[c // 200]               S1 = the 46 kana of the gojuon, column by column (a ka sa ... wa / i ki shi ... wi / ...)
  k2 = S2[(c - 1) % 10]           S2 = a i u e o ka ki ku ke ko
  k3 = S3[((c - 1) // 10) % 20]   S3 = ho he fu hi ha no ne nu ni na to te tsu chi ta so se su shi sa
so c = 200*i1 + 10*i3 + i2 + 1.  Romanised YE is the old kana we in first place and e elsewhere.
Code -> character from ../sunyatsen/tw.csv (the repository's standard telegraph code table).

This decoder was written here from the formula alone (21 Oct 2026), to check two things independently:

  python threekana.py reply     Huang Xing's reply of 25 May 1916 (JACAR B03050731500 frame 0246), from the
                                transcription made here on 15 Sept 2026 (huang.py), before the formula was known.
                                One correction, Tomokiyo's: the O HI of KONUOHIKE is a CHI.
  python threekana.py stream    the two telegrams of 20 May 1916 (B03050089100 frames 0076-0078) as contributed by
                                Harumi-Matsuba (sankana/groups.csv, CC BY 4.0): every final kana triple is run
                                through this decoder and this repository's code table, and the categories counted.
  python threekana.py reveal    writes ../../docs/reveal/huangxing.json from the reply.
"""
import csv, json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
TW = {}
for r in csv.DictReader(open(os.path.join(HERE, '..', 'sunyatsen', 'tw.csv'), encoding='utf8')):
    for c in r['code'].split():
        TW.setdefault(int(c), r['character'])

S1 = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa',
      'i', 'ki', 'shi', 'chi', 'ni', 'hi', 'mi', 'ri', 'wi',
      'u', 'ku', 'su', 'tsu', 'nu', 'fu', 'mu', 'yu', 'ru',
      'e', 'ke', 'se', 'te', 'ne', 'he', 'me', 're', 'we',
      'o', 'ko', 'so', 'to', 'no', 'ho', 'mo', 'yo', 'ro']
S2 = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko']
S3 = ['ho', 'he', 'fu', 'hi', 'ha', 'no', 'ne', 'nu', 'ni', 'na', 'to', 'te', 'tsu', 'chi', 'ta', 'so', 'se', 'su', 'shi', 'sa']
SYL = sorted(set(S1 + S2 + S3 + ['ye', 'yo']), key=len, reverse=True)
KATA = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰヱヲ'
ROM = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi', 'tsu', 'te', 'to',
       'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo',
       'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wi', 'we', 'wo']
K2R = dict(zip(KATA, ROM))

# Huang Xing's reply as transcribed here on 15 Sept 2026 (huang.py CT), unchanged
REPLY = ("REKUTATA UHOYAKATE SEKANAOKU SAKEKINISE OSUKAKUCHI REUHONIUSU MAKASUSAKU "
         "FUREOHIHE YENIKIYEHI TAKASUREU SASHIKIHE WAONIAAHO SAYEHITE UHINAKUTA "
         "NEATEMUYE SUHEUHAKA YESOMIKANU TEASUUKU TSUHAKOSE KEKININAKI TEAKETASHI "
         "KONUOHIKE HIMIKANO SHIKUSAHE UHATAKASA KEKINIKA ATAREUSASU OSO YUA NIRA KISU")
REPLY_FIX = [('konuohike', 'konuchike')]     # Tomokiyo, 23 Sept 2026: O HI is CHI


def kana(s):
    s, out, i = s.lower(), [], 0
    while i < len(s):
        for k in SYL:
            if s.startswith(k, i):
                out.append(k); i += len(k); break
        else:
            out.append('?' + s[i]); i += 1
    return out


def code(t):
    a, b, c = t
    a = 'we' if a == 'ye' else a
    b = 'e' if b == 'ye' else b
    c = 'e' if c == 'ye' else c
    try:
        return 200 * S1.index(a) + 10 * S3.index(c) + S2.index(b) + 1
    except ValueError:
        return None


def encode(c):
    return S1[c // 200] + S2[(c - 1) % 10] + S3[((c - 1) // 10) % 20]


def reply(fix=True):
    s = REPLY.replace(' ', '').lower()
    if fix:
        for a, b in REPLY_FIX: s = s.replace(a, b, 1)
    k = kana(s)
    out = []
    for i in range(0, len(k) - len(k) % 3, 3):
        g = k[i:i + 3]
        c = code(g)
        out.append(('-'.join(g), c, TW.get(c, '?') if c else '?'))
    return out, k[len(k) - len(k) % 3:]


def stream():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'sankana', 'groups.csv'), encoding='utf8')))
    agree = disagree = 0
    for r in rows:
        if not r['電碼']:
            continue
        c = code([K2R[ch] for ch in r['仮名']])
        if c == int(r['電碼']) and TW.get(c) == r['字']:
            agree += 1
        else:
            disagree += 1
            print('disagrees:', r)
    cat = collections.Counter((1 if int(r['組']) < 108 else 2, r['区分']) for r in rows)
    return rows, agree, disagree, cat


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    what = sys.argv[1] if len(sys.argv) > 1 else 'reply'
    if what == 'reply':
        for fix in (False, True):
            out, rest = reply(fix)
            print('with Tomokiyo correction' if fix else 'as transcribed', '| groups', len(out), '| left over', rest)
            print(''.join(ch for _, _, ch in out))
        out, _ = reply(True)
        for i, (g, c, ch) in enumerate(out):
            print(f'{i:2d} {g:12s} {c:5d} {ch}')
    elif what == 'stream':
        rows, a, d, cat = stream()
        print('groups', len(rows), '| groups with a code', a + d, '| formula + tw.csv agree', a, '| disagree', d)
        for k in sorted(cat): print('telegram', k[0], k[1], cat[k])
        print('T1', ''.join(r['字'] for r in rows[:108]))
        print('T2', ''.join(r['字'] for r in rows[108:]))
    elif what == 'reveal':
        out, _ = reply(True)
        toks = [{'g': g.upper(), 'p': ch, 'cls': ('unc' if i == 35 else '')} for i, (g, c, ch) in enumerate(out)]
        doc = {'slug': 'huangxing', 'anchor': 'reply', 'title': 'Huang Xing’s reply, 25 May 1916',
               'caption': 'The 46 kana triples of frame 0246 as transcribed here on 15 September 2026, run through Tomokiyo’s formula and the standard telegraph code. The one marked doubtful is CHI-KE-HI, where the telegram as filed has O-HI-KE (Tomokiyo’s correction).',
               'unit': 'kana triple', 'key_note': 'Tomokiyo’s three-kana formula over the standard Chinese telegraph code',
               'tokens': toks}
        p = os.path.join(HERE, '..', '..', 'docs', 'reveal', 'huangxing.json')
        open(p, 'w', encoding='utf8', newline='\n').write(json.dumps(doc, ensure_ascii=False, indent=1) + '\n')
        print('wrote', os.path.normpath(p), len(toks), 'tokens')
