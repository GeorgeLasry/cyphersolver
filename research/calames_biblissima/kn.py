import subprocess,sys,re
for t in sys.argv[1:]:
    o=subprocess.run([sys.executable,'-X','utf8','research/archive_sweep_2026-10/known.py',t],capture_output=True,text=True,encoding='utf-8').stdout
    files=sorted(set(re.findall(r'^  ([^:]+):',o,re.M)))
    print(t,'->',files[:6])
