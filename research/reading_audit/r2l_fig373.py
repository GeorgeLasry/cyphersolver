"""r2l: build texts/f373_figures.txt from the line-by-line reading of f. 373's figures (spec file: one line of the leaf
per row, the letters as the figures give them, {xx} = a double sign, [24] = a code group, [struck] = struck group,
'?' after a letter = the figure is doubtful on the image).
    python research/reading_audit/r2l_fig373.py <spec.txt> > targets/maisse1592/texts/f373_figures.txt"""
import re, sys
K = {'a':7,'b':8,'c':9,'d':10,'e':11,'f':1,'g':2,'h':3,'i':4,'l':5,'m':6,'n':12,'o':13,'p':14,'q':15,'r':16,'s':17,'t':18,'u':19,'x':20,'y':21,'z':22}
D = {'ff':66,'mm':67,'nn':68,'rr':71,'ss':72,'tt':73}
for line in open(sys.argv[1], encoding='utf8'):
    if ':' not in line: continue
    tag, txt = line.split(':', 1)
    out = []
    for m in re.finditer(r"\{(\w\w)\}(\?)?|\[(\w+)\]|([a-z])(\?)?", txt):
        if m.group(1): out.append(f'{D[m.group(1)]}' + ('?' if m.group(2) else ''))
        elif m.group(3): out.append('X?' if m.group(3) == 'struck' else m.group(3))
        else: out.append(f'{K[m.group(4)]}' + ('?' if m.group(5) else ''))
    print(f'{tag.strip()}: ' + ' '.join(out))
