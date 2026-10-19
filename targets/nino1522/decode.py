"""Reproduce literal decryption and measured counts from the submitted sign labels and key."""
from pathlib import Path
from collections import Counter
import json,re
p=Path(__file__).resolve().parent
k=json.loads((p/'key.json').read_text(encoding='utf-8'))
rows=[re.findall(r'\((\d+)\)',s) for s in (p/'transcription.txt').read_text(encoding='utf-8').splitlines() if s.strip()]
c=Counter(n for r in rows for n in r)
assert len(rows)==8 and sum(c.values())==260 and len(c)==49
for r in rows:print(''.join('?' if '?' in k[n] else '' if k[n]=='_' else k[n].lower() for n in r))
letters=Counter(v for v in k.values() if len(v)==1 and v.isalpha())
nulls=sum(c[n] for n in c if k[n]=='_')
unknown=sum(c[n] for n in c if '?' in k[n])
print(json.dumps({'cipher_elements':sum(c.values()),'key_entries':len(k),'line_counts':list(map(len,rows)),
 'null_types':sum(v=='_' for v in k.values()),'null_occurrences':nulls,'ambiguous_occurrences':unknown,
 'non_null_elements':sum(c.values())-nulls,'unambiguous_non_null_assignments':sum(c.values())-nulls-unknown,
 'max_per_vowel':max(letters[x] for x in 'AEIOU'),'max_per_consonant':max(v for x,v in letters.items() if x not in 'AEIOU'),
 'per_letter':dict(sorted(letters.items()))},ensure_ascii=False,indent=1))
