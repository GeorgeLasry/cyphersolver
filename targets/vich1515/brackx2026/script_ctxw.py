import sys
exec(open('dec.py').read().split("T=[t for l in L for t in l]")[0])
T=[t for l in L for t in l]
for g in sys.argv[1:]:
    print('====',g,T.count(g))
    for i,t in enumerate(T):
        if t==g: print('  ',line(T[max(0,i-12):i]),'  ##',g,'##  ',line(T[i+1:i+12]))
