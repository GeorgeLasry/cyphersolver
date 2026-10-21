"""Reproduce the limited key screen and source-duplication checks, without network."""
import ast
import hashlib
import json
import pathlib
import runpy

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
RUNS = [[71,55,45,62,47,8], [61,50,57,62,72,66,54,61,68,60], [45,58,44,50,72]]

def key_screen():
    # Extract only definitions and key assignments; do not run the old script's
    # file-loading, language model, reporting or output-writing code.
    source = ROOT/'targets/thurloe/apply_keys.py'
    prefix = source.read_text(encoding='utf-8').split('# English LM')[0]
    namespace = {'__file__': str(source)}
    exec(compile(ast.parse(prefix), str(source), 'exec'), namespace)
    keys = namespace['KEYS']
    keys['Barwick 1721 plate (targets/hyde/barwick_key.py)'] = runpy.run_path(str(ROOT/'targets/hyde/barwick_key.py'))['KEY']
    keys['Ormond-Rupert 1644-45 (K118)'] = runpy.run_path(str(ROOT/'targets/rupert/keys.py'))['K118_LET']
    keys['Add MS 72438 K125'] = runpy.run_path(str(ROOT/'targets/rupert/test_letters.py'))['K125']
    raw = (ROOT/'targets/rupert/k166.txt').read_text().strip()
    keys['Add MS 72438 K166'] = {int(n): p for n,p in (s.strip().split() for s in raw.split(','))}
    results = []
    for name, key in keys.items():
        results.append({'key': name,
                        'covered_tokens': sum(n in key for run in RUNS for n in run),
                        'total_tokens': sum(map(len,RUNS)),
                        'output': [''.join(key.get(n, f'[{n}]') for n in run) for run in RUNS]})
    (HERE/'brussels_key_screen.json').write_text(json.dumps(results,indent=1,ensure_ascii=False)+'\n',encoding='utf-8')
    return results

def manifest():
    cache = HERE/'decode'
    files = []
    for path in sorted(cache.glob('IMG_*')):
        data = path.read_bytes()
        files.append({'file': path.name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    (HERE/'evidence_manifest.json').write_text(json.dumps({'date':'2026-10-20','files':files},indent=1)+'\n',encoding='utf-8')
    def hashes(record):
        return [f['sha256'] for f in files if f['file'].startswith('IMG_R'+str(record)+'_')]
    a,b = hashes(1163),hashes(1164)
    assert len(a)==len(b)==4, 'Download all four photographs on each record first'
    assert a==b, 'R1163 and R1164 photographs are not all identical'
    assert sum(map(len,RUNS))==21
    return len(files)

if __name__=='__main__':
    results=key_screen()
    print(f'Brussels: {len(results)} existing key tables applied to 21 tokens; outputs saved, no solution asserted.')
    print(f'Manifest: {manifest()} source images hashed; all four R1163/R1164 pairs identical.')
