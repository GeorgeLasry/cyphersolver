"""Validate both CTTS images and regenerate edited text after key changes.
Run python Codex_verify.py [--sync-edited]. Geometry changes require review.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, os, shutil, re

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def alignment(rectangles):
    lines=[]
    for p in sorted(rectangles,key=lambda r:r['x']):
        def overlap(q):
            a,b=sorted([p,q],key=lambda r:r['y'])
            return min(max(0,a['y']+a['h']-b['y']),b['h'])/min(a['h'],b['h'])
        scores=[max(overlap(q) for q in line[-2:]) for line in lines]
        if not scores or max(scores)<.4:lines.append([p])
        else:lines[scores.index(max(scores))].append(p)
    return sorted(lines,key=lambda line:sum(r['y']+r['h']/2 for r in line)/len(line))

def read_projects(root):
    colors=[line.split(';') for line in (root/'colors.txt').read_text().splitlines()]
    key={}
    for line in (root/'key.txt').read_text().splitlines():
        if ' - ' in line:
            symbols,value=line.split(' - ')
            for symbol in symbols.split('|'):
                assert symbol not in key,f'Duplicate key entry {symbol}'
                key[symbol]=value
    spec=json.loads((root/'Codex_edited_alignment.json').read_text(encoding='utf-8'))
    projects={};trs=[];dcs=[]
    for stem,doc in spec['documents'].items():
        rectangles=[]
        for line in (root/f'positions/{stem}_positions.txt').read_text().splitlines():
            if line.strip():
                x,y,w,h,c=line.split();rectangles.append(dict(x=float(x),y=float(y),w=float(w),h=float(h),c=int(c)))
        lines=alignment(rectangles)
        trp=root/f'transcription/{stem}.txt';dcp=root/f'decryption/{stem}.txt'
        tr=trp.read_text().splitlines();dc=dcp.read_text().splitlines()
        assert tr[0]==dc[0]=='# '+doc['image']
        assert len(tr)==len(dc)==len(lines)+2 and tr[-1]==dc[-1]==''
        for i,row in enumerate(lines,1):
            labs=tr[i].split(';');assert labs.pop()==''
            vals=dc[i].split();assert len(row)==len(labs)==len(vals),(stem,i,'token count')
            for b,lab,val in zip(row,labs,vals):
                assert colors[b['c']][1]==lab,(stem,i,'position label',lab)
                assert lab in key and val==key[lab].lower(),(stem,i,lab,'key mismatch')
                b.update(label=lab,value=val)
        assert (root/f'positions/{stem}_positions.txt').read_bytes()==(root/f'positions_SECOND_COPY/{stem}_positions.txt').read_bytes()
        projects[stem]=lines;trs.append(trp.read_bytes());dcs.append(dcp.read_bytes())
    assert (root/'transcription/all.txt').read_bytes()==b''.join(trs)
    assert (root/'decryption/all.txt').read_bytes()==b''.join(dcs)
    assert (root/'colors.txt').read_bytes()==(root/'colors_SECOND_COPY.txt').read_bytes()
    assert len(colors)==431 and sorted(int(c[2]) for c in colors)==list(range(431))
    base=[0,85,127,170,212,255]
    native=[f'0x{r:02x}{g:02x}{b:02x}ff' for bs in (base,[42],[51,102,153,204,243]) for r in base for g in base for b in bs if r or g or b]
    assert [c[0] for c in colors]==native
    return colors,key,projects,spec

def read_project(root):
    colors,key,projects,spec=read_projects(root)
    return colors,key,projects['1']

def render_edits(lines,spec):
    assert len(lines)==len(spec['rows']),'Physical rows changed; review alignment'
    rendered=[]
    for n,(row,rec) in enumerate(zip(lines,spec['rows']),1):
        assert [[b[k] for k in ('x','y','w','h')] for b in row]==rec['geometry'],f'Geometry changed on row {n}; review alignment'
        covered=[];parts=[]
        for seg in rec['segments']:
            if seg['kind']=='clear':parts.append(seg['text']);continue
            start,end=seg['tokens'];covered+=list(range(start,end+1));boxes=row[start-1:end]
            if seg['kind']=='clear_box':
                assert all(b['label']=='[Plaintext]' for b in boxes)
                parts.append(seg['text'])
            else:
                assert seg['kind']=='cipher' and all(b['label']!='[Plaintext]' for b in boxes)
                raw=seg.get('separator','').join(b['value'] for b in boxes)
                if 'reading' in seg:
                    assert seg['reading_basis']==raw,'Key changed under editorial supply; review reading'
                    assert re.sub(r'\[[^\]]*\]','',seg['reading'])==raw,'Editorial reading deletes or changes cipher text'
                    raw=seg['reading']
                parts.append(raw)
        assert covered==list(range(1,len(row)+1)),f'Every box must occur once: row {n}'
        joined=''
        for seg,part in zip(rec['segments'],parts):
            joined+=(seg.get('join_before',' ') if joined else '')+part
        rendered.append(f'{n}|'+joined+rec.get('suffix',''))
    return '\n'.join(rendered)+'\n'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--sync-edited',action='store_true');parser.add_argument('--source',type=Path);args=parser.parse_args()
    root=Path(__file__).resolve().parent;source=args.source or root
    colors,key,projects,spec=read_projects(root)
    from PIL import Image
    expected={};combined=[]
    for stem,lines in projects.items():
        doc=spec['documents'][stem];width,height=Image.open(source/doc['image']).size
        for row in lines:
            for b in row:
                assert 0<=b['x']<b['x']+b['w']<=width and 0<=b['y']<b['y']+b['h']<=height
                if b['label']!='[Plaintext]':
                    with Image.open(root/'icons'/(colors[b['c']][0]+'.png')) as icon:
                        assert icon.mode=='RGBA' and icon.getbbox(),b['label']
        edited=render_edits(lines,doc);expected[f'edited/{stem}_edits.txt']=edited;combined.append(stem+'\n'+edited)
    expected['edited/edits.txt']=''.join(combined)
    changed=[rel for rel,text in expected.items() if not (root/rel).exists() or (root/rel).read_text(encoding='utf-8')!=text]
    if changed and args.sync_edited:
        backup=root/'codex_backups'/('edited_sync_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));backup.mkdir(parents=True,exist_ok=False)
        for rel in changed:
            p=root/rel
            if p.exists():q=backup/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
            p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_suffix('.pending');assert not tmp.exists();tmp.write_text(expected[rel],encoding='utf-8',newline='\n');os.replace(tmp,p)
        print('Edited synchronization backup:',backup)
    for rel,text in expected.items():assert (root/rel).read_text(encoding='utf-8')==text,rel+' is stale'
    for rel,h in spec['protected_hashes'].items():assert sha(source/rel)==h,'Protected source changed: '+rel
    for stem,lines in projects.items():
        n=sum(map(len,lines));clear=sum(b['label']=='[Plaintext]' for row in lines for b in row);unknown=sum(b['value']=='?' for row in lines for b in row)
        print(f'PASS {stem}: {len(lines)} rows; {n} boxes = {n-clear} cipher + {clear} clear; {unknown} unresolved signs')
    print('PASS: key, positions, transcription, decryption, edited, icons, duplicate exports and protected sources agree.')
if __name__=='__main__':main()
