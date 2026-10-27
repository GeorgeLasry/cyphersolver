"""Independent check of Tomokiyo's 'Maisse' Cipher 2' on fr. 16093 ff. 404/406/410.
WAINUT, 27 Oct 2026. Tokens: cipher_lines.txt (same stretches), transcribed from full-resolution BnF images.
Sign names: q~ = hooked q-like sign; E~ = hooked s/3-like sign; D~ = theta-like d sign; d = d-shaped sign;
uy = 'uy' ligature sign; f_ = long s; rho = g/rho-like loop; 9t = g with cross; x = x-like sign;
w = omega-like sign; de~ = looped 'de' sign; desp = p with stroke; my = m with tail; phi = 9/phi sign;
que = 9 with straight tail; pi = pi-like sign; UNK = not identified.
Key values below are read off Tomokiyo's key image (../src/henryiv_Maisse2.png), with the sign
identifications marked in comments; nothing is learned from the copies.
Run: python decode_check.py   (standard library only; output in decode_check_output.txt)"""
import random, difflib, statistics
KEY = {
 '2':'a','+':'a','z':'a',            # a: 2, +, (z-like sign in row 4)
 '20':'b','23':'c','9t':'c','25':'d','D~':'d',
 '27':'e','0':'e','f_':'e','E~':'e',  # E~ identified with Tomokiyo's 3/z-like e homophone [?]
 '21':'f','T':'f','24':'g','22':'h','19':'i','2+':'i','phi':'i',
 '7':'l','q~':'l','16':'m','26':'n','rho':'n','1':'o','y':'o',
 '14':'p','x':'p','4':'q','8':'r','to':'r','pi':'r','10':'s','w':'s',
 '3':'t','d':'t','5':'u','uy':'u','6':'u','29':'x','my':'z',
 # word codes
 '15':'faict','17':'vous','18':'est','que':'que','desp':'des','de~':'de',
}
LINES = [ # (label, tokens, clear copy of the same stretch)
 ('f410 l.10', 'q~ 27 29 14 E~ to 19 f_ rho 9t E~ z 15 23 y uy 24 26 y 2+ 10 d 8 E~ que 8 6 f_ 17 18 27 10 E~ 26 8 phi 27 26 d',
  "lexperienceafaictcognoistrequevousnevousestesenrient"),
 ('f410 l.11', '16 x E~ D~ uy 2+ uy 24 E~ 16 0 26 d que 17 E~ 26 z uy 0 my de~ 7 y 26 24 d E~ UNK x 10 15 desp',
  "mpeduiugementquevousavezdelongtempsfaictdes"),
 ('f404 l.3', 'q~ 27 10 uy 8 14 7 6 w D~ 27', "lesurplusde"),
 ('f406 l.16', '7 E~ 10 uy 8 x q~ 5 w 25 27 6 y my 7 8 E~ 10 18 10 uy to 7 E~ 10',
  "lesurplusdevozlettresestsurles"),
 ('f406 l.17a', '2+ 0 23 d desp z T', "iectdesaf"),
 ('f406 l.17b', 'de~ to pi 16 27 25 6 uy 1 + 2 24 E~', "deromeduvoiage"),
]
def dec(toks, key): return ''.join(key.get(t,'?') for t in toks)
def score(a,b): return difflib.SequenceMatcher(None,a,b,autojunk=False).ratio()
random.seed(1593)
syms=list(KEY); vals=[KEY[s] for s in syms]
tot_true=[]; out=[]
for lab,ts,copy in LINES:
    toks=ts.split(); d=dec(toks,KEY); s=score(d,copy); tot_true.append(s)
    perm=[]
    for _ in range(2000):
        v=vals[:]; random.shuffle(v); perm.append(score(dec(toks,dict(zip(syms,v))),copy))
    shuf=[]
    for _ in range(2000):
        t=toks[:]; random.shuffle(t); shuf.append(score(dec(t,KEY),copy))
    out.append((lab,len(toks),d,copy,s,statistics.mean(perm),max(perm),statistics.mean(shuf),max(shuf)))
for o in out:
    print(f"{o[0]}: {o[1]} groups\n  decoded: {o[2]}\n  copy   : {o[3]}\n  true-key ratio {o[4]:.2f} | permuted-key mean {o[5]:.2f} max {o[6]:.2f} | shuffled-groups mean {o[7]:.2f} max {o[8]:.2f}")
print('mean true', round(statistics.mean(tot_true),2))
