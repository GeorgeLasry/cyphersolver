# Builds wide_words.txt, the group options: the 450 commonest 1-4 letter strings inside words of La Celestina
# (Gutenberg 1619, corp/g1619.txt), its 150 commonest words, and a chancery vocabulary.
import collections
from drv import norm_words
def body(p):
    t=open(p,encoding='utf-8',errors='ignore').read(); a=t.find('*** START'); return t[t.find('\n',a):t.find('*** END')]
W=norm_words(body('corp/g1619.txt')); wc=collections.Counter(W); sub=collections.Counter()
for w,c in wc.items():
    for L in (1,2,3,4):
        for i in range(len(w)-L+1): sub[w[i:i+L]]+=c
CH='''su santidad papa rey francia frances franceses emperador uenecianos uenecia napoles roma cardenal cardenales embaxador
dineros gente gentes armada tregua liga concierto capitulos capitulacion capitulado scriuir escreuir scriuo escriuo
carta cartas letras milan suyços suiços esguiçaros florencia mantua ferrara genoua ytalia lombardia exercito campo
cauallos infanteria artilleria dinero ducados nuestro nuestra nuestros nuestras uos uuestro uuestra sabiduria
paz guerra principe principes reyno reynos estado estados negocio negocios fecho fazer hazer dezir dicho dicha
tierra tierras lugar lugares tiempo assi porende otrosi mismo misma'''.split()
ws=[]
for x in [s for s,_ in sub.most_common(450)]+[w for w,_ in wc.most_common(150)]+CH:
    x=x.translate(str.maketrans('jvkwç','iucuc'))
    if x not in ws and all(c in 'abcdefghilmnopqrstuxyz' for c in x): ws.append(x)
open('wide_words.txt','w').write('\n'.join(ws)+'\n')
