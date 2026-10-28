"""Apply manuscript key219 to the cipher left unread on Schück I,p259.
No statistical key reconstruction; literal outputs precede editorial expansion.
"""
from pathlib import Path
import csv,json
r=Path(__file__).resolve().parent
key=dict(ln.split(maxsplit=1) for ln in (r/'key219.txt').read_text().splitlines() if ln and not ln.startswith('#'))
rows=[];parts={}
for ln in (r/'schuck1771_cipher.txt').read_text().splitlines():
 if ln and not ln.startswith('#'):
  label,txt=ln.split(':',1);codes=txt.split();vals=[]
  for i,code in enumerate(codes,1):
   val=key.get(code,'['+code+']');vals.append(val)
   rows.append({'passage':label,'position':i,'code':code,'key_value':val,'source':'A0073297_00219','note':'Key variants retained; not automatically expanded into full French spelling.'})
  parts[label]={'codes':codes,'literal_values':vals}
assert key['626']=='Fersen_le_Cte' and key['665']=='breteuil'
assert parts['143.C']['literal_values'][:7]==['bo','ne','in','te','li','ge','nce,nci']
with (r/'schuck1771_reading.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
(r/'schuck1771_results.json').write_text(json.dumps({'key':'image219','method':'known key applied to a separately printed letter','tokens':len(rows),'editor_identified_name_tokens':2,'previously_unresolved_tokens':len(rows)-2,'parts':parts,'scope':'Side finding: no decryption of image107 is claimed.','reading_status':'Partial normalized reading; Court abbreviations and cre remain editorially unresolved.'},indent=2)+'\n')
for label,p in parts.items():print(label,' | '.join(p['literal_values']))
