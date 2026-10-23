"""Score every reading of the vieuville1587 runs that the Nevers informant key (nevers1588/key.md) allows."""
import itertools, sys
sys.path.insert(0, sys.argv[1])
from lang import lm
ALL='abcdefghilmnopqrstuxyz'
# informant key, sign -> plain options (key.md); transcription glyphs of vieuville mapped to the nearest key sign
OPT={'2':'ah','9':'ahr','8':'b','7':'c','6':'d','5':'e','4':'f','3':'gj','i':'i','1':'i','k':'o','n':'l','o':'l',
     'v':'d','D':'u','d':'u','t':'e','s':'e','f':'fs','g':'gr','e':'t','x':'c','c':'x','h':'q','m':'m','p':'i',
     'J':'p','y':'b','q':'y','l':'n','r':ALL,'Z':ALL,'8t':'b'}
RUNS={'A':'5i7fZrd65i8th6D725','B':'5i7D629v','C':'k7n6297'}
m=lm.load('fr-1530-despatches',spaces=False)
for k,run in RUNS.items():
    pools=[OPT.get(ch,ch) for ch in run]
    n=1
    for p in pools: n*=len(p)
    best=sorted(((m.score(''.join(c))/len(run),''.join(c)) for c in itertools.product(*pools)),reverse=True)[:5]
    print(k,run,n,'readings; best:',[(round(s,2),t) for s,t in best])
