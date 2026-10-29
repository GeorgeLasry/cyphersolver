import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8',errors='replace')
S='C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt/inventairedesarc00cauc.txt'
t=re.sub(r'\s+',' ',open(S,encoding='utf8',errors='ignore').read())
for pos in map(int,sys.argv[1:]):
    f=[m for m in re.finditer(r'Fascio (\d+)',t[:pos]) ]
    # nearest heading style "Fascio 123." occurrence
    print(pos,[m.group(0) for m in f[-3:]], t[pos-20:pos+5])
