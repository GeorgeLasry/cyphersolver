"""v7 list 1: apply {folder: [[index, {fields}], ...]} from a json file with translate_v7_1.set_fields, then check.
    python research/reading_audit/t7_1_apply.py <actions.json>"""
import json, sys, pathlib, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import translate_v7_1 as t
R = pathlib.Path(__file__).resolve().parents[2]
a = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf8'))
for folder, items in a.items():
    for i, fields in items:
        t.set_fields(folder, f'#{i}', fields)
    r = subprocess.run([sys.executable, 'docs/_check_profile.py', folder], cwd=R, capture_output=True, text=True)
    print(folder, [l for l in r.stdout.splitlines() if 'result' in l])
