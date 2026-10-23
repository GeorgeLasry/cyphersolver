"""b28: align harley1582r8505 cipher decodes with R8505_reading.md, page by page.
For every run, the beam decode (b28_r8505_beam.py: f. 263r from R8505_transcription_f1_b28.txt, the other sides from
final/f2-f4) is segmented into words; a run counts as carried when its dictionary words (3+ letters) are found in order
in the reading section of its page. Prints runs carried / not, and the share of decoded letters that reach the reading.
    python research/reading_audit/b28_r8505_align.py"""
import os, re, sys, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]; T = ROOT / 'targets' / 'harley1582r8505'
rd = (T / 'R8505_reading.md').read_text(encoding='utf-8')
body = re.search(r'^## Reading\n(.*?)^## ', rd, re.S | re.M).group(1)
secs = dict(re.findall(r'^### f\. (\S+)\n(.*?)(?=^### |\Z)', body, re.S | re.M))
def norm(s): return re.sub(r'[^a-z ]', ' ', s.lower().replace("'", ' ').replace('j', 'i').replace('v', 'u').replace('ç', 'c').replace('é', 'e').replace('è', 'e').replace('ü', 'u'))
files = {'263r': T / 'R8505_transcription_f1_b28.txt', '264r': T / 'R8505_transcription_f2_b28.txt', '264v': T / 'R8505_transcription_f3_b28.txt', '263v': T / 'final' / 'f4.txt'}   # versos: f3 = 264v, f4 = 263v
tot_w = tot_f = 0
for page, fn in files.items():
    out = subprocess.run([sys.executable, str(ROOT / 'research' / 'reading_audit' / 'b28_r8505_beam.py'), str(fn)], capture_output=True, text=True, encoding='utf-8', env=dict(os.environ, PYTHONUTF8='1', NULLPEN='99')).stdout
    text = norm(secs.get(page, '')).replace(' ', '')
    pos = 0; f = w = 0
    for line in out.splitlines():
        parts = line.split('\t')
        if len(parts) < 4: continue
        ws = [x for x in parts[3].split() if not (x.startswith('[') or x.isupper() or len(x) < 3)]
        # anchor each run: the earliest place after the previous run where two of its words occur within 80 chars
        best = None; bi = 0
        for i in range(min(len(ws), 4)):                # the earliest anchor among the run's first words
            k = text.find(ws[i], pos)
            while k >= 0:
                nxt = [text.find(x, k + len(ws[i])) for x in ws[i + 1:i + 3]]
                if any(0 <= n - k < 80 for n in nxt) or len(ws) == 1:
                    break
                k = text.find(ws[i], k + 1)
            if k >= 0 and (best is None or k < best): best, bi = k, i
        q = best if best is not None else pos
        w += bi                                       # words before the anchor count as not found
        for word in ws[bi:]:
            w += 1
            k = text.find(word, q)
            if k >= 0 and k - q < 120: f += 1; q = k + len(word)
            elif os.environ.get('V'): print('   not found:', page, parts[0], word)
        if best is not None: pos = q
    tot_w += w; tot_f += f
    print(page, 'decoded words (3+ letters) found in order in the reading:', f, '/', w)
print('all', tot_f, '/', tot_w)
