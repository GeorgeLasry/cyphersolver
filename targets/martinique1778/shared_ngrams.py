"""Is the 1778 letter in the same code as the 1779 f.123 key? Count adjacent group pairs/triples shared with the 1779 interlinear
stream, against 2000 shuffles of the 1778 token order (same tokens, same frequencies, order destroyed)."""
import re, os, random
H = os.path.dirname(os.path.abspath(__file__))
def stream79():
    out = []
    for l in open(os.path.join(H, 'pairs1779_f123.txt'), encoding='utf8'):
        if l.startswith('l') and ':' in l[:4]:
            out.append([g for g, v in re.findall(r'(\d+)=(\S+)', l)])
    return out
a79 = [g for l in stream79() for g in l]
lines78 = [l.split() for l in open(os.path.join(H, 'transcription.txt'), encoding='utf8') if l[0] != '#']
a78 = [g for l in lines78 for g in l]
def ngr(seq, n): return {tuple(seq[i:i+n]) for i in range(len(seq)-n+1)}
def shared(seq, n): return len(ngr(seq, n) & ngr(a79, n))
res = {n: shared(a78, n) for n in (2, 3)}
print('tokens 1778', len(a78), 'tokens 1779', len(a79), 'shared groups', len(set(a78) & set(a79)), 'of', len(set(a78)))
print('observed shared bigrams', res[2], 'trigrams', res[3])
print('shared bigrams:', sorted(ngr(a78, 2) & ngr(a79, 2)))
print('shared trigrams:', sorted(ngr(a78, 3) & ngr(a79, 3)))
random.seed(1); c2 = []; c3 = []
for _ in range(2000):
    s = a78[:]; random.shuffle(s); c2.append(shared(s, 2)); c3.append(shared(s, 3))
print('shuffled bigram mean %.2f max %d; p(>=obs) %.4f' % (sum(c2)/2000, max(c2), sum(x >= res[2] for x in c2)/2000))
print('shuffled trigram mean %.2f max %d; p(>=obs) %.4f' % (sum(c3)/2000, max(c3), sum(x >= res[3] for x in c3)/2000))
