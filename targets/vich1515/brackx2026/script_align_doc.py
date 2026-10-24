# Writes decode_aligned.md: each line of the repo transcription, the split labels used (sin/sim, X -> Xr/Xs/Xz),
# each token's value, and the decoded line. Firm groups in capitals, tentative groups in {braces}, unread groups in
# [brackets], signs with no value in <angle brackets>.
import json,re
S=dict(kv.split('=') for kv in open('keys/signs.txt').read().split())
G=json.load(open('keys/groups.json'))
orig=[l.split() for l in open('transcriptions/n73_tokens.txt')]
split=[l.split() for l in open('work/v15x.txt')]
isg=lambda t: t.islower() and t.isalpha()
out=["# vich1515: the decode aligned with the transcription","",
"AHN Estado 8715 N.73. For each line: `T` the repository's transcription (`n73_tokens.txt`, `?` removed); `S` the",
"labels as split for decoding where they differ (`sin`/`sim`, and `X` as `Xr`/`Xs`/`Xz`, both chosen token by token",
"from context: look-alike readings, see `reading_original.md`); `V` each token's value; `D` the decoded line.",
"In `V` and `D`: signs in lower case; firm code groups in CAPITALS; tentative groups in {braces}; unread groups as",
"[group]; a sign with no value as <SIGN>. Values: `keys/signs.txt`, `keys/groups.json`. Nothing here is edited by",
"hand beyond those two token splits.","","```"]
decs=[]
for n,(o,s) in enumerate(zip(orig,split),1):
    vals=[];dec=[]
    for t in s:
        if isg(t):
            g=G.get(t)
            if g and g['status']=='firm': v=g['value'].upper()
            elif g: v='{'+g['value'].upper()+'}'
            else: v='['+t+']'
        else:
            v=S.get(t,'<'+t+'>')
        vals.append(f'{t}={v}'); dec.append(v)
    d=''.join(dec); decs.append(d)
    out+=[f'{n:3} T: {" ".join(o)}']
    if o!=s: out+=[f'    S: {" ".join(s)}']
    out+=[f'    V: {" ".join(vals)}',f'    D: {d}','']
out[-1:]=['```']
open('decode_aligned.md','w').write('\n'.join(out)+'\n')
open('work/decoded_lines.txt','w').write('\n'.join(f'{i+1:3} {d}' for i,d in enumerate(decs))+'\n')
