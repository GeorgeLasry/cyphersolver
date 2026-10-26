"""Set 643 (lead 2): the Linear B control for set 552. Does the size of a count depend on what is counted, replicated
from Knossos to Pylos? DAMOS (C:/Users/dbour/indus_data/linb). Writes results/predict_test643.md."""
import json
import re
from collections import Counter

import rtools as R
from scipy.stats import binomtest, fisher_exact

LB = 'C:/Users/dbour/indus_data/linb/corpus_damos_documents.jsonl'
MEASURE = {'S', 'V', 'T', 'Z', 'M', 'N', 'P', 'Q', 'L', 'Q'}
ANIMAL = re.compile(r'^(OVIS|CAP|SUS|BOS|EQU|\*10[5-9])')
BULK = re.compile(r'^(GRA|HORD|OLIV|OLE|VIN|LANA|AROM|CYP|FAR|NI|TELA|AES|AUR|MEL|VIR\*|\*1[2-9][0-9])')


def counts(site):
    c = {'s': Counter(), 'l': Counter()}
    for ln in open(LB, encoding='utf-8'):
        d = json.loads(ln)
        if d.get('site') != site:
            continue
        for line in d.get('lines', []):
            tk = line['tokens']
            for i in range(len(tk) - 1):
                a, b = tk[i], tk[i + 1]
                if re.match(r'^[A-Z*][A-Z0-9*+]*$', a) and a not in MEASURE and b.isdigit():
                    c['s' if int(b) <= 3 else 'l'][a.split('+')[0]] += 1
    return c


def main():
    rd = R.Round('Set 643 registered predictions: the Linear B control for number size', 'predict_test643')
    ck, cp = counts('Knossos'), counts('Pylos')
    ns, nl = sum(ck['s'].values()), sum(ck['l'].values())
    sk = {}
    for g in set(ck['s']) | set(ck['l']):
        a, b = ck['s'][g], ck['l'][g]
        if a + b >= 6 and fisher_exact([[a, ns - a], [b, nl - b]])[1] < 0.05:
            sk[g] = a / ns > b / nl
    ms, ml = max(1, sum(cp['s'].values())), max(1, sum(cp['l'].values()))
    rep = [g for g in sk if cp['s'][g] + cp['l'][g] >= 3]
    same = sum((cp['s'][g] / ms > cp['l'][g] / ml) == sk[g] for g in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- Knossos: %d small counts, %d large; skewed small: %s; skewed large: %s.' % (ns, nl, ' '.join(sorted(g for g in sk if sk[g])), ' '.join(sorted(g for g in sk if not sk[g]))))
    ok1 = len(sk) >= 3 and bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec('LB1', 'ideograms skewed small / large at Knossos lean the same way at Pylos', '%d of %d, p = %.4f' % (same, len(rep), p), ok1)
    large = [g for g in sk if not sk[g]]
    ab = sum(bool(ANIMAL.match(g) or BULK.match(g)) for g in large)
    ok2 = bool(large) and ab / len(large) >= 0.7
    rd.rec('LB2', 'the large-count ideograms are livestock or bulk commodities (70%+)', '%d of %d' % (ab, len(large)), ok2)
    rd.rec('P', 'progress rule: none (a control; LB1 + LB2 would make set 552 ordinary bookkeeping)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
