"""Reproduce the bounded CP alignment diagnostics; none establishes a historical key.
Install ortools==9.15.6755 before running. Existing synthetic input is preserved.
"""
from cp_align import solve,norm,r
import random,json,hashlib
real=json.loads((r/'image126_pair.json').read_text());control=json.loads((r/'beam_control_input.json').read_text())
ts=' '.join(real['cipher_lines']).split();p=norm(real['plaintext']);out=[]
for lexical in (False,True):
 o=solve(control['cipher'],norm(control['plaintext']),seconds=10,lexical=lexical)
 if 'key' in o:
  o['token_value_accuracy']=sum(o['key'][t]==control['true_key'][t] for t in control['cipher'])/len(control['cipher'])
  o['usable_for_key_recovery']=o['token_value_accuracy']>=.95
 o['case']='synthetic_control';out.append(o)
o=solve(ts,p,seconds=10);o['case']='real_unrestricted';out.append(o)
shuffled=ts.copy();random.Random(450).shuffle(shuffled)
o=solve(shuffled,p,seconds=10);o.update(case='shuffled_order_control',seed=450);out.append(o)
for skip in range(8):
 o=solve(ts,p,seconds=5,skip=skip,tail=3,lexical=True);o['case']='real_lexical_framing';out.append(o)
for o in out:
 print(o['case'],o['status'],'lexical',o['lexical'],'skip',o['skip_groups'],'accuracy',o.get('token_value_accuracy'),flush=True)
result={'input_sha256':{f:hashlib.sha256((r/f).read_bytes()).hexdigest() for f in ['image126_pair.json','beam_control_input.json','key218.txt','key219.txt','key220.txt']},'warning':'Formal alignment is not key recovery. Glyph and spelling assumptions remain unvalidated; see image126_audit.md.','results':out}
(r/'cp_experiments.json').write_text(json.dumps(result,indent=2)+'\n')
