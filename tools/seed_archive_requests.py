"""Seed and refresh archive_requests.json from the "blocker: needs-physical-access" gaps in targets/*/NOTES.md.

archive_requests.json is the ledger of what a volunteer could fetch from an archive or a library: a leaf to
photograph, a reproduction to order, a book or database the project cannot reach. docs/archives.html is built from it.

Re-running is safe. A request already in the ledger keeps every hand edit (archive, kind, status, history, volunteer);
only gaps that are new in NOTES are appended. A request whose gap has gone from NOTES is reported, not removed:
close it by hand (status "closed", with a history line saying what closed it).

    python tools/seed_archive_requests.py          # merge new gaps, report gone ones
    python tools/seed_archive_requests.py --dry    # report only
"""
import datetime, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'docs'))
import _further_page as F          # gaps_of(): the "## Remaining gaps" bullets with their blocker

LEDGER = ROOT / 'archive_requests.json'
TODAY = datetime.date.today().isoformat()

# (pattern, archive, city), tried on the gap text first, then on the target's profile shelfmarks
ARCHIVES = [
    (r'Heraklion|HM 22|autopsy of the tablets', 'Heraklion Archaeological Museum', 'Heraklion'),
    (r'\bMHS\b|Massachusetts Historical', 'Massachusetts Historical Society', 'Boston'),
    (r'\bNLI\b|National Library of Ireland', 'National Library of Ireland', 'Dublin'),
    (r'Bodleian', 'Bodleian Library', 'Oxford'),
    (r'\bASNa\b', 'Archivio di Stato di Napoli', 'Naples'),
    (r'Archives diplomatiques|AE CP|La Courneuve', 'Archives diplomatiques', 'La Courneuve'),
    (r'\bRAH\b|BRAH|Salazar', 'Real Academia de la Historia', 'Madrid'),
    (r'\bAGS\b|Simancas', 'Archivo General de Simancas', 'Simancas'),
    (r'\bAHN\b', 'Archivo Histórico Nacional', 'Madrid'),
    (r'\bBNE\b', 'Biblioteca Nacional de España', 'Madrid'),
    (r'Arxiu Capitular|\bACB\b', 'Arxiu Capitular de Barcelona', 'Barcelona'),
    (r'\bTNA\b|\bSP \d+|Kew', 'The National Archives', 'Kew, London'),
    (r'\bBL\b|British Library|Harley|Cotton|Add MS', 'British Library', 'London'),
    (r'outre-mer|\bANOM\b|\bCOL [BC]', 'Archives nationales d’outre-mer', 'Aix-en-Provence'),
    (r'Meurthe-et-Moselle', 'Archives départementales de Meurthe-et-Moselle', 'Nancy'),
    (r'\bBnF\b|Gallica|\bfr\. \d|Français \d|Colbert|Clairambault|Baluze', 'Bibliothèque nationale de France', 'Paris'),
    (r'\bASV\b|\bAAV\b|Segr\. Stato|Segreteria di Stato|Segretario di Stato|Nunziatura', 'Archivio Apostolico Vaticano', 'Vatican City'),
    (r'\bAPUG\b|Gregoriana', 'Archivio della Pontificia Università Gregoriana', 'Rome'),
    (r'\bASMo\b', 'Archivio di Stato di Modena', 'Modena'),
    (r'\bASVe\b', 'Archivio di Stato di Venezia', 'Venice'),
    (r'Siena|Concistoro', 'Archivio di Stato di Siena', 'Siena'),
    (r'\bKHA\b', 'Koninklijk Huisarchief', 'The Hague'),
    (r'Nationaal Archief|\bNA \d', 'Nationaal Archief', 'The Hague'),
    (r'\bAGR\b', 'Archives générales du Royaume', 'Brussels'),
    (r'Riksarkivet', 'Riksarkivet', 'Stockholm'),
    (r'\bHHStA\b|ÖStA', 'Haus-, Hof- und Staatsarchiv', 'Vienna'),
    (r'BayHStA', 'Bayerisches Hauptstaatsarchiv', 'Munich'),
    (r'\bHStAM\b|Staatsarchiv Marburg', 'Hessisches Staatsarchiv Marburg', 'Marburg'),
    (r'\bGWLB\b', 'Gottfried Wilhelm Leibniz Bibliothek', 'Hanover'),
    (r'SOA Plzeň', 'Státní oblastní archiv v Plzni', 'Klášter u Nepomuka'),
    (r'Slovenský národný archív', 'Slovenský národný archív', 'Bratislava'),
    (r'Ráday', 'Ráday Archives', 'Budapest'),
    (r'MNL OL|\bG15\b', 'Hungarian National Archives (MNL OL)', 'Budapest'),
    (r'NARA|\bRG \d+|\bM\d+ roll', 'U.S. National Archives (NARA)', 'College Park / Washington'),
    (r'JACAR|NIDS', 'National Institute for Defense Studies (via JACAR)', 'Tokyo'),
]
# a printed book or a database behind a login or bot check: closed from a library or a browser, not a reading room
LIBRARY = (r'HathiTrust|Google Books|archive\.org|Cambridge Element|paywall|Szaktárs|Rubinstein|Serrano|Benda|'
           r'Puig.s printed|Doussinague|Carande|Carmona|Scheurer|State Papers Online|Gale SPO|British Newspaper Archive|'
           r'bot check|not online here|library copy|re-reading of the JACAR scans')
ORDER = r'\border\b|scan-on-request|higher-resolution|high-resolution|400-dpi|must be scanned|imaging|reproduction|raking-light'


def split_gap(text):
    """(what is needed, why it is blocked) from one Remaining-gaps bullet."""
    m = re.search(r'\s*[-–—:]?\s*blocker:\s*needs-physical-access[.;:]?\s*', text, re.I)
    if not m: return text.strip(), ''
    need, why = text[:m.start()].strip(' -–—;'), text[m.end():].strip()
    why = re.sub(r'^\(|\)$', '', why) if why.startswith('(') and why.endswith(')') else why
    return need or why, why if need else ''


def shelfmarks(folder):
    p = ROOT / 'targets' / folder / 'profile.json'
    if not p.is_file(): return []
    try: docs = json.loads(p.read_text(encoding='utf-8')).get('documents', [])
    except ValueError: return []
    out = []
    for d in docs:
        s = re.sub(r'\s*[(;].*$', '', d.get('shelfmark') or '').strip()
        if s and s != 'unknown' and s not in out: out.append(s)
    return out


def archive_of(text, marks):
    for src in (text, ' ; '.join(marks)):
        for pat, name, city in ARCHIVES:
            if re.search(pat, src): return name, city
    return 'unknown', ''


def kind_of(text):
    if re.search(LIBRARY, text, re.I): return 'library'
    if re.search(ORDER, text, re.I): return 'order'
    return 'visit'


def key(target, need):
    return target + '|' + re.sub(r'\W+', ' ', need.lower()).strip()[:90]


def gaps():
    for d in sorted((ROOT / 'targets').iterdir()):
        if not (d / 'NOTES.md').is_file(): continue
        for t, b in F.gaps_of(d.name):
            if b == 'needs-physical-access': yield d.name, t


def main(dry=False, quiet=False):
    led = json.loads(LEDGER.read_text(encoding='utf-8')) if LEDGER.is_file() else {'_about': __doc__.split('\n\n')[1], 'requests': []}
    reqs = led['requests']
    have = {key(r['target'], r['need']): r for r in reqs if r.get('target')}
    seen, added = set(), []
    n = max((int(r['id'][3:]) for r in reqs), default=0)
    for folder, text in gaps():
        need, why = split_gap(text)
        k = key(folder, need); seen.add(k)
        if k in have: continue
        marks = shelfmarks(folder)
        kind = kind_of(text)
        archive, city = archive_of(text, marks)
        if kind == 'library' and not re.search(r'\bTNA\b|RAH|JACAR', text): archive, city = 'A library or database', ''
        n += 1
        r = dict(id=f'ar-{n:03d}', target=folder, kind=kind, archive=archive, city=city, shelfmark=marks[0] if marks else '',
                 need=need, why=why, status='open', volunteer=None, issue=None,
                 history=[dict(date=TODAY, status='open', note='from the NOTES.md Remaining gaps')])
        reqs.append(r); have[k] = r; added.append(r)
    gone = [r for r in reqs if r.get('target') and r['status'] not in ('closed',) and key(r['target'], r['need']) not in seen]
    for r in ([] if quiet else added): print(f"+ {r['id']} {r['target']:18} {r['kind']:7} {r['archive']}")
    for r in ([] if quiet else gone): print(f"? {r['id']} {r['target']}: gap no longer in NOTES.md (close it by hand)")
    if not quiet: print(f'{len(added)} added, {len(gone)} gone, {len(reqs)} in the ledger')
    if not dry and added:
        LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return len(added), len(gone)


if __name__ == '__main__':
    main('--dry' in sys.argv)
