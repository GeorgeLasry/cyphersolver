"""r2l: the Brienne copy of f. 373 enciphered with key1.tsv, word by word, from a start word (a reading aid for checking
the figures line by line on the image; the transcription records what the image shows).
    python research/reading_audit/r2l_pred373.py [start_word_index] [n_words]"""
import pathlib, re, sys, unicodedata
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'maisse1592' / 'texts'
T = open(D / 'f373_brienne_copy.txt', encoding='utf8').read()
body = ' '.join(l for l in T.splitlines() if not l.startswith('#') and not l.startswith('[fol')).replace('= ', '').replace('=', '')
body = re.sub(r'\[\?([^\]]*)\]', r'\1', body)
K = {'a':7,'b':8,'c':9,'d':10,'e':11,'f':1,'g':2,'h':3,'i':4,'l':5,'m':6,'n':12,'o':13,'p':14,'q':15,'r':16,'s':17,'t':18,'u':19,'x':20,'y':21,'z':22}
def norm(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if c.isalpha() and ord(c) < 128)
    return w.replace('j', 'i').replace('v', 'u').replace('k', 'c')
words = [norm(w) for w in re.split(r"[\s'.,;:/]+", body) if norm(w)]
s = int(sys.argv[1]) if len(sys.argv) > 1 else words.index('autant') - 1
n = int(sys.argv[2]) if len(sys.argv) > 2 else 40
for i in range(s, min(s + n, len(words))):
    print(i, words[i], ' '.join(str(K[c]) for c in words[i]))
