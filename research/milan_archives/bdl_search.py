"""BDL (Biblioteca Digitale Lombarda) VuFind search via curl; prints hit count and titles per term.
    PYTHONUTF8=1 python -I research/milan_archives/bdl_search.py term ...
"""
import re, html, subprocess, sys, urllib.parse
for term in sys.argv[1:]:
    u = 'https://www.bdl.servizirl.it/vufind/Search/Results?' + urllib.parse.urlencode({'lookfor': term, 'type': 'AllFields', 'limit': 100})
    s = subprocess.run(['curl', '-s', '-L', '-m', '60', u], capture_output=True).stdout.decode('utf-8', 'replace')
    n = re.search(r'Risultati trovati:\s*([\d.]+)', re.sub('<[^>]+>', ' ', s).replace('\n', ' ').replace('  ', ' '))
    print('==', term, n.group(1) if n else '0?')
    for rid, title in re.findall(r'href="/vufind/Record/([^"]+)">\s*(.*?)</a>', s, re.S):
        print('  ', rid, re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', title))).strip()[:150])
