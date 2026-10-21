"""Build docs/catalogue.html and the tables in ../CATALOGUE.md from ../catalogue.json.

Run from docs/:  python _catalogue_page.py   (it runs _build_site.py afterwards for the nav, footer and contents
strip; a catalogue.html left with the bare <!-- site:nav --> marker has no navigation bar).

catalogue.json is the single source: entries with 1-5 scores for importance, solvability and difficulty.
The page embeds the JSON and computes a priority score client-side from adjustable weights; it also renders a
static table for readers without JavaScript. CATALOGUE.md gets its table (counted entries, default weights) and
its "Also noted" list rewritten between <!-- table:start --> / <!-- table:end --> and <!-- also:start --> /
<!-- also:end --> markers; the prose around them is hand-written and left alone.
"""
import json, html, pathlib, re, datetime

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
DATA = json.loads((ROOT / 'catalogue.json').read_text(encoding='utf-8'))
W = DATA['weights_default']
GALLICA = 'https://gallica.bnf.fr/ark:/12148/'
CONTRIB = {c['id']: c for c in json.loads((ROOT / 'contributors.json').read_text(encoding='utf-8'))['contributors']}


def priority(e, w=W):
    """0-10: weighted mean of importance, solvability and ease (6 - difficulty), each 1-5, rescaled."""
    tot = w['importance'] + w['solvability'] + w['ease']
    v = (w['importance'] * e['importance'] + w['solvability'] * e['solvability'] + w['ease'] * (6 - e['difficulty'])) / tot
    return round((v - 1) / 4 * 10, 1)


def is_open(e):
    """Still in the open ranking: no outcome, or attempted but not read."""
    return not e.get('outcome') or e['outcome'].startswith('attempted')


def esc(t):
    return html.escape(str(t), quote=False)


def is_ark(a):
    return bool(re.match(r'^(btv1b|bpt6k)\w+$', a or ''))


AS_OF = DATA.get('status_as_of', '')            # the day every entry's known/open split was last checked


def fmt_day(iso):
    if not iso: return ''
    y, m, d = iso.split('-')
    return f"{int(d)} {['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'][int(m)-1]} {y}"


# ---------- what has left the catalogue ----------
# The README result tables are the ledger of finished targets; a row that cites "catalogue N" says that catalogue
# number (or part of it) has an outcome. Read them so a reader holding an old catalogue number can see where it went.
CAT_RE = re.compile(r'catalogue(?: items?| nos?\.)? (\d+(?:\s*(?:\+|,|and|&)\s*\d+)*)')
OPEN_SECTIONS = {'Not solved', 'Not applicable', 'In progress', 'Surveys'}


def solved_map():
    """{catalogue id: [(target, method, landed, slug or None, part)]} from README.md's Results tables."""
    out, sec = {}, None
    for line in (ROOT / 'README.md').read_text(encoding='utf-8').splitlines():
        if line.startswith('## '): sec = None
        if line.startswith('### '): sec = line[4:].strip()
        if not sec or sec in OPEN_SECTIONS or not line.startswith('| ') or line.startswith('| Target') or line.startswith('|---'): continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 5: continue
        m = CAT_RE.search(cells[0])
        if not m: continue
        ids = [int(x) for x in re.findall(r'\d+', m.group(1))]
        name = re.sub(r'\*\*|\[|\]\([^)]*\)', '', cells[0])
        name = re.sub(r'\s*\((?:[^()]|\([^()]*\))*(?:catalogue|DECODE)(?:[^()]|\([^()]*\))*\)\s*$', '', name).strip()
        slug = re.search(r'dbourdeau\.github\.io/cyphersolver/([\w-]+)\.html', line)
        part = bool(re.search(r'catalogue(?: item)? \d+[^)]*?part|split \d|from catalogue', cells[0]))
        for i in ids:
            out.setdefault(i, []).append((name, sec, cells[2], slug.group(1) if slug else None, part))
    return out


def open_prs():
    """Open pull requests, refreshed with gh when it is available, else the copy cached at the last build."""
    cache = HERE / '_open_prs.json'
    try:
        import subprocess
        r = subprocess.run(['gh', 'pr', 'list', '--state', 'open', '--json', 'number,title,url,author,updatedAt'],
                           capture_output=True, text=True, encoding='utf-8', timeout=30, cwd=ROOT)
        if r.returncode == 0:
            prs = json.loads(r.stdout)
            cache.write_text(json.dumps(prs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
            return prs
    except Exception:
        pass
    return json.loads(cache.read_text(encoding='utf-8')) if cache.exists() else []


def link_pairs(e):
    """(label, href) for each Gallica ark and each extra link (e['links'], e.g. DECODE records); href None = text only."""
    out = []
    for k in ('ark', 'ark2'):
        a = e.get(k)
        if a: out.append((a, GALLICA + a if is_ark(a) else None))
    for l in e.get('links') or []:
        out.append((l['label'], l['href']))
    return out


def ark_links(e):
    return ' · '.join(f'<a href="{h}" rel="noopener">{esc(t)}</a>' if h else esc(t) for t, h in link_pairs(e))


def md_links(e, sep):
    return sep.join((f'[{t}]({h})' if h else t) if not is_ark(t) else f'ark {t}' for t, h in link_pairs(e))


# ---------- Markdown ----------
def md_table(entries, outcome=False):
    first = 'Outcome' if outcome else 'Prio.'
    rows = [f'| {first} | # | Date | Item | Shelfmark / access | Status & prior art | Why it matters | Imp. | Solv. | Diff. | Cls | Seen |',
            '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for e in entries:
        arks = md_links(e, '; ')
        shelf = e['shelfmark'] + (f' ({arks})' if arks else '') + (f'; {e["folio_note"]}' if e.get('folio_note') else '')
        seen = '●' if e['seen'] == 'image' else '◇'
        lead = f"**{e['outcome']}**" if outcome else f"**{priority(e)}**"
        st = f"**Known ({e.get('as_of') or AS_OF}):** {e['known']} **Open:** {e['open']}" if e.get('known') else e['status']
        rows.append(f"| {lead} | {e['id']} | {e['date']} | {e['title']}: {e['correspondents']} | {shelf} | {st} | {e['why']} | {e['importance']} | {e['solvability']} | {e['difficulty']} | {e['cls']} | {seen} |")
    return '\n'.join(rows)


def md_also(entries):
    out = []
    for e in entries:
        arks = md_links(e, ', ')
        out.append(f"- **{e['title']}**, {e['date']}, {e['shelfmark']}{(', ' + arks) if arks else ''}. {e['status']} {e['why']} "
                   f"Imp. {e['importance']}, solv. {e['solvability']}, diff. {e['difficulty']}, class {e['cls']}, priority {priority(e)}.")
    return '\n'.join(out)


def update_md():
    p = ROOT / 'CATALOGUE.md'
    s = p.read_text(encoding='utf-8')
    counted = sorted([e for e in DATA['entries'] if e['counted'] and is_open(e)], key=lambda e: (-priority(e), e['id']))
    also = sorted([e for e in DATA['entries'] if not e['counted']], key=lambda e: (-priority(e), e['id']))
    s = re.sub(r'## The \d+ open targets, by priority', f'## The {len(counted)} open targets, by priority', s)
    s = re.sub(r'<!-- table:start -->.*?<!-- table:end -->', lambda m: '<!-- table:start -->\n' + md_table(counted) + '\n<!-- table:end -->', s, flags=re.S)
    s = re.sub(r'<!-- also:start -->.*?<!-- also:end -->', lambda m: '<!-- also:start -->\n' + md_also(also) + '\n<!-- also:end -->', s, flags=re.S)
    p.write_text(s, encoding='utf-8')


# ---------- HTML ----------
# Correspondents with a public-domain portrait on the site (_portraits.json), matched by hand-checked patterns
# on the "correspondents" field; a wrong face is worse than none, so ambiguous names carry a date test.
PORTRAITS = {}
for _v in json.loads((HERE / '_portraits.json').read_text(encoding='utf-8')).values():
    for _p in _v:
        if _p.get('img'): PORTRAITS.setdefault(_p['name'], _p['img'])
FACES = [
    (r'Frederick II', 'Frederick II', lambda e: 1740 <= e['year'] <= 1786),
    (r'Henry Percy', 'Henry Percy', None),
    (r"Catherine de' Medici|Catherine de M[ée]dicis", "Catherine de' Medici", None),
    (r'Charles I\b', 'Charles I', lambda e: 1625 <= e['year'] <= 1649),
    (r'Charles I\b|Charles V\b', 'Charles V', lambda e: 1516 <= e['year'] <= 1558),
    (r'Francis I(?:st)?\b|Franis I\b', 'Francis I', lambda e: 1515 <= e['year'] <= 1547),
    (r'Montmorency', 'Anne de Montmorency', lambda e: 1520 <= e['year'] <= 1567),
    (r'duke of Nevers|duc de Nevers|Duke of Nivernois', 'Duke of Nevers', lambda e: 1565 <= e['year'] <= 1595),
    (r'Merc(?:œ|oe)ur', 'Duc de Mercœur', None),
    (r'Henri II\b', 'Henry II', lambda e: 1547 <= e['year'] <= 1559),
    (r'R[áa]k[óo]czi', 'Francis II Rákóczi', lambda e: 1700 <= e['year'] <= 1735),
    (r'Oxenstierna', 'Axel Oxenstierna', None),
    (r'Secretary Cecil|Burghley|Burleigh|Baurleigh', 'William Cecil', lambda e: 1550 <= e['year'] <= 1598),
    (r'Walsingham', 'Francis Walsingham', lambda e: 1568 <= e['year'] <= 1590),
    (r'Elizabeth R\b', 'Elizabeth I', lambda e: 1558 <= e['year'] <= 1603),
    (r'William V\b', 'William V', lambda e: 1766 <= e['year'] <= 1806),
    (r'Maarten van der Goes', 'Maarten van der Goes', None),
    (r'Dirk van Hogendorp', 'Dirk van Hogendorp', None),
    (r'Starhemberg|Staremberg', 'Gundaker Starhemberg', lambda e: 1700 <= e['year'] <= 1745),
]

def faces(e):
    """(name, image) for each correspondent of e with a portrait, in the order they appear (sender first)."""
    c, out = e['correspondents'], []
    for pat, name, ok in FACES:
        m = re.search(pat, c)
        if m and re.match(r'\w*\s?\?', c[m.end():]): m = None      # a name the catalogue itself queries
        if m and name in PORTRAITS and (ok is None or ok(e)) and name not in [n for _, n, _ in out]:
            out.append((m.start(), name, PORTRAITS[name]))
    return [(n, i) for _, n, i in sorted(out)]

def people_html(e):
    f = faces(e)
    if not f: return ''
    tip = esc(' → '.join(n for n, _ in f)).replace('"', '&quot;')
    return f'<span class="avs" title="{tip}">' + ''.join(f'<img src="{i}" alt="" loading="lazy">' for _, i in f) + '</span>'

def blank_html(e):
    """No portrait: a small wax roundel with the entry's language initial."""
    return f'<span class="avs none" aria-hidden="true"><i>{esc((e.get("language") or "?")[:2])}</i></span>'



# ---------- HTML ----------
def dots(v, cls=''):
    return f'<span class="dots {cls}" title="{v} of 5">' + ''.join(f'<i class="{"on" if i < v else ""}"></i>' for i in range(5)) + '</span>'


SOLVED = solved_map()


def parts_html(e):
    """Links to the write-ups of pieces of an open entry that already have an outcome (README rows citing its number)."""
    L, seen = [], set()
    for n, _, _, sl, _ in SOLVED.get(e['id'], []):
        if sl and sl not in seen: seen.add(sl); L.append((n, sl))
    if not L: return ''
    return ('<span class="ko"><i class="k">written up</i> '
            + ' · '.join(f'<a href="{sl}.html" title="{esc(n).replace(chr(34), "&quot;")}">{sl}</a>' for n, sl in L) + '</span>')


def row(e):
    arks = ark_links(e)
    seen = '<span class="seen img" title="viewed on the image">●</span>' if e['seen'] == 'image' else '<span class="seen cat" title="catalogue description only">◇</span>'
    noted = '' if e['counted'] else ' <span class="noted">noted</span>'
    if e.get('outcome'): noted += f' <span class="noted out">{esc(e["outcome"])}</span>'
    if e.get('scored') == 'rule': noted += ' <span class="noted" title="scored by script from DECODE metadata, not reviewed">rule-scored</span>'
    if e.get('scored') == 'sweep': noted += ' <span class="noted" title="added by the new-solves sweep of 22 Sept 2026, scored by hand from descriptions">new 22 Sept</span>'
    if e.get('contributed_by'):          # a cipher brought in by an outside contributor (contributors.json id)
        who = CONTRIB.get(e['contributed_by'], {}).get('name', e['contributed_by'])
        noted += f' <a class="noted by" href="contributors.html#{esc(e["contributed_by"])}" title="brought into the catalogue by {esc(who)}">via {esc(who)}</a>'
    if e.get('on_list'): noted += f' <span class="noted" title="also on this list">{esc(e["on_list"])} list</span>'
    detail = (f'<div class="det"><div><b>Correspondents.</b> {esc(e["correspondents"])} · {esc(e["place"])} · {esc(e["language"])}</div>'
              f'<div><b>Shelfmark.</b> {esc(e["shelfmark"])}{(" · " + arks) if arks else ""}{(" · " + esc(e["folio_note"])) if e.get("folio_note") else ""}</div>'
              + (f'<div class="kn"><b>Known so far</b> <span class="asof">checked {fmt_day(e.get("as_of") or AS_OF)}</span> {esc(e["known"])}</div>'
                 f'<div class="op"><b>Still open.</b> {esc(e["open"])}</div>' if e.get('known') else '')
              + f'<div><b>{"History and prior art" if e.get("known") else "Status and prior art"}.</b> {esc(e["status"])}</div>'
              f'<div><b>Why it matters.</b> {esc(e["why"])}</div>'
              f'<div><b>Scores.</b> {esc(e["score_note"])}</div>'
              f'<div><b>Verify first.</b> {esc(e["verify"])}</div>'
              + (f'<div><a href="{e["writeup"]}">Write-up &rarr;</a></div>' if e.get('writeup') else '') + '</div>')
    return (f'<tr class="e" data-id="{e["id"]}" tabindex="0" aria-expanded="false">'
            f'<td class="prio"><b>{priority(e):.1f}</b></td>'
            f'<td class="date">{esc(e["date"])}<span class="num">no. {e["id"]}</span></td>'
            f'<td class="item">{people_html(e)}<b>{seen} {esc(e["title"])}</b>{noted}<span class="sub">{esc(e["why"])}</span>'
            + (f'<span class="ko"><i class="k">known</i> {esc(e["known"])}</span><span class="ko"><i class="o">open</i> {esc(e["open"])}</span>' if e.get('known') else '')
            + parts_html(e) + '</td>'
            f'<td class="shelf">{esc(e["shelfmark"])}{("<br>" + arks) if arks else ""}</td>'
            f'<td class="sc">{dots(e["importance"])}</td><td class="sc">{dots(e["solvability"])}</td><td class="sc">{dots(e["difficulty"], "diff")}</td>'
            f'<td class="cls"><span class="badge {e["cls"]}">{e["cls"]}</span></td></tr>'
            f'<tr class="d" data-for="{e["id"]}" hidden><td colspan="8">{detail}</td></tr>')


def facet(name, label, values):
    opts = ''.join(f'<button type="button" class="chip" data-facet="{name}" data-val="{esc(v)}" aria-pressed="false">{esc(v)}</button>' for v in values)
    return f'<div class="facet"><span class="flabel">{label}</span>{opts}</div>'


def is_blocked(e):
    o = e.get('outcome') or ''
    return 'blocked' in o or o.startswith('attempted, skipped')


def status_html(E):
    """The two lists a reader needs before starting work: what is known and what is still open, both dated."""
    day = fmt_day(AS_OF) or fmt_day(datetime.date.today().isoformat())
    ids = {e['id'] for e in E}
    gone = sorted(set(SOLVED) - ids)
    part = sorted([e for e in E if (e.get('known') and not e['known'].startswith('Nothing')) or e['id'] in SOLVED], key=lambda e: e['id'])
    opn = sorted(E, key=lambda e: (-priority(e), e['id']))
    n_blk = sum(1 for e in E if is_blocked(e))
    n_att = sum(1 for e in E if (e.get('outcome') or '').startswith('attempted') and not is_blocked(e))
    prs = open_prs()

    def one(e, field):
        t = e.get(field) or e['status']
        return f'<li><a href="#e{e["id"]}">no. {e["id"]}</a> <b>{esc(e["title"])}</b> <span class="d">{esc(e["date"])}</span> &mdash; {esc(t)}</li>'

    gone_rows = ''.join(
        f'<tr id="e{i}g"><td>{i}</td><td>' + '<br>'.join(
            (f'<a href="{sl}.html">{esc(n)}</a>' if sl else esc(n)) + (' <span class="d">(part)</span>' if pt else '')
            for n, _, _, sl, pt in SOLVED[i]) + '</td><td>' + '<br>'.join(esc(m) for _, m, _, _, _ in SOLVED[i])
        + '</td><td>' + '<br>'.join(esc(l) for _, _, l, _, _ in SOLVED[i]) + '</td></tr>' for i in gone)
    pr_li = ''.join(f'<li><a href="{esc(r["url"])}" rel="noopener">#{r["number"]}</a> {esc(r["title"])} '
                    f'<span class="d">{esc((r.get("author") or {}).get("login", ""))}, updated {fmt_day(r["updatedAt"][:10])}</span></li>' for r in prs)
    html_ = f"""<section class="state" id="status">
<h2>Where things stand, {day}</h2>
<p>Before starting on an entry, read its <b>known</b> and <b>open</b> lines in the table and the open pull requests below. Work that has landed is folded into both lists at each rebuild; work still in a pull request is not. If a number you were given is not in the table, it has left the catalogue: <a href="#gone">look it up</a>.</p>
<div class="cols">
<div class="card"><h3>What is solved or known so far</h3>
<p><b>{len(gone)}</b> catalogue numbers have been deciphered, explained or found in print and have left the open list (<a href="#gone">the list</a>; every write-up is on the <a href="writeups.html">write-ups</a> page). <b>{len(part)}</b> of the entries still open have pieces already deciphered or identified.</p>
<details><summary>the {len(part)} open entries with known pieces</summary><ul class="sl">{"".join(one(e, "known") for e in part)}</ul></details>
</div>
<div class="card"><h3>What is still unsolved</h3>
<p><b>{len(E)}</b> entries are open ({sum(1 for e in E if e['counted'])} counted targets, the rest also noted): <b>{n_blk}</b> blocked from outside (no images online, an archive order needed, or no key known to exist), <b>{n_att}</b> attempted here without a decipherment, <b>{len(E) - n_blk - n_att}</b> not yet attempted.</p>
<details><summary>the {len(E)} open entries, by priority, with what is still open</summary><ul class="sl">{"".join(one(e, "open") for e in opn)}</ul></details>
</div>
</div>
<div class="card wide"><h3>Work in progress: {len(prs)} open pull request{"s" if len(prs) != 1 else ""}</h3>
{f'<ul class="sl">{pr_li}</ul>' if prs else '<p>None.</p>'}</div>
</section>"""
    return html_, gone_rows, len(gone)


def build_html():
    E = DATA['entries']
    state, gone_rows, n_gone = status_html(E)
    gone_js = json.dumps({i: [[n, sl] for n, _, _, sl, _ in SOLVED[i]] for i in sorted(set(SOLVED) - {e['id'] for e in E})}, ensure_ascii=False).replace('</', '<\\/')
    ordered = sorted(E, key=lambda e: (not is_open(e), not e['counted'], -priority(e), e['id']))
    counted = [e for e in E if e['counted'] and is_open(e)]
    periods = sorted({e['period'] for e in E}); regions = sorted({e['region'] for e in E}); sources = sorted({e['source'] for e in E})
    data_js = json.dumps({'weights': W, 'entries': E}, ensure_ascii=False).replace('</', '<\\/')
    n_all, n_img = len(E), sum(1 for e in E if e['seen'] == 'image')
    n_dec = sum(1 for e in E if e.get('source') == 'DECODE')
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Unsolved Catalogue — {len(counted)} open targets, scored</title>
<meta name="description" content="Undeciphered historical cipher letters, 1482–1841, not on the standard unsolved lists, harvested from the BnF catalogue on Gallica, the fine print of the cryptiana articles and the DECODE database. Each scored for historical importance, solvability and difficulty; filter, sort and reweight the priority score.">
<link rel="stylesheet" href="style.css">
<style>
.ctl{{background:var(--panel);border:1px solid var(--rule);border-radius:var(--radius);padding:.9rem 1.1rem .5rem;margin:1.2rem 0 .8rem}}
.ctl .row{{display:flex;flex-wrap:wrap;gap:.6rem 1.4rem;align-items:center;margin-bottom:.5rem}}
.ctl label{{font-family:var(--mono);font-size:.74rem;letter-spacing:.04em;color:var(--muted);display:inline-flex;align-items:center;gap:.4rem}}
.ctl input[type=range]{{width:120px;accent-color:var(--gold)}}
.ctl input[type=search]{{background:var(--bg);color:var(--ink);border:1px solid var(--rule);border-radius:6px;padding:.35rem .6rem;font:inherit;font-size:.9rem;min-width:220px}}
.ctl .wv{{min-width:2.4em;color:var(--ink2)}}
.facet{{display:flex;flex-wrap:wrap;gap:.3rem;align-items:center;margin:.3rem 0}}
.flabel{{font-family:var(--mono);font-size:.7rem;letter-spacing:.06em;color:var(--muted);min-width:5rem}}
.chip{{padding:.2rem .65rem;border-radius:999px;border:1px solid var(--rule);background:var(--bg);color:var(--ink2);font-family:var(--mono);font-size:.72rem;cursor:pointer}}
.chip[aria-pressed=true]{{background:var(--gold);color:var(--gold-ink);border-color:var(--gold)}}
.chip:hover{{border-color:var(--gold)}}
.count{{font-family:var(--mono);font-size:.74rem;color:var(--muted);margin:.5rem 0 0}}
.tw{{overflow-x:auto;margin:0 0 1.6rem;border:1px solid var(--rule);border-radius:var(--radius);background:var(--bg2);width:min(1240px,calc(100vw - 2rem));position:relative;left:50%;transform:translateX(-50%)}}
table.cat{{border-collapse:separate;border-spacing:0;width:100%;min-width:900px;font-size:.88rem;table-layout:fixed}}
table.cat col.c-prio{{width:6.5%}}table.cat col.c-date{{width:11%}}table.cat col.c-item{{width:40%}}table.cat col.c-shelf{{width:17.5%}}table.cat col.c-sc{{width:7%}}table.cat col.c-cls{{width:4%}}
table.cat th{{position:sticky;top:0;z-index:1;background:var(--bg2);color:var(--muted);font-family:var(--mono);font-weight:normal;font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;text-align:left;padding:.65rem .7rem;border-bottom:1px solid var(--rule);white-space:nowrap;cursor:pointer;user-select:none}}
table.cat th:hover{{color:var(--head)}}
table.cat th[aria-sort=descending]::after{{content:" \\25BE";color:var(--gold)}}table.cat th[aria-sort=ascending]::after{{content:" \\25B4";color:var(--gold)}}
table.cat th.sc,table.cat td.sc,table.cat th.cls,table.cat td.cls,table.cat th.seen,table.cat td.seen,table.cat td.prio,table.cat th.prio{{text-align:center}}
table.cat td{{padding:.6rem .7rem;border-bottom:1px solid var(--rule);vertical-align:top}}
tr.e{{cursor:pointer;transition:background .15s}}
tr.e:hover td{{background:color-mix(in srgb,var(--gold) 7%,transparent)}}
tr.e[aria-expanded=true] td{{background:color-mix(in srgb,var(--gold) 12%,transparent);border-bottom-color:transparent}}
tr.e:nth-of-type(4n+1) td{{background:color-mix(in srgb,var(--ink) 2.5%,transparent)}}
td.prio b{{font-family:var(--display);font-size:1.35rem;color:var(--gold);font-weight:normal}}
td.date{{font-family:var(--mono);font-size:.76rem;color:var(--ink2)}}td.date .num{{display:block;color:var(--muted);font-size:.68rem;margin-top:.2rem}}
td.item b{{color:var(--head);display:block}}
td.item .sub{{display:block;font-size:.8rem;color:var(--muted);margin-top:.15rem;line-height:1.4}}
.noted.out{{color:var(--green);border-color:color-mix(in srgb,var(--green) 50%,transparent)}}
.noted{{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;color:var(--muted);border:1px solid var(--rule);border-radius:999px;padding:.05rem .45rem;vertical-align:middle;margin-left:.3rem}}
td.shelf{{font-size:.76rem;color:var(--ink2);overflow-wrap:anywhere}}
.dots{{display:inline-flex;gap:3px}}.dots i{{width:9px;height:9px;border-radius:50%;background:var(--rule);display:inline-block}}
.dots i.on{{background:var(--gold)}}.dots.diff i.on{{background:var(--red)}}
.badge{{display:inline-block;min-width:1.5rem;padding:.1rem .45rem;border-radius:6px;font-family:var(--mono);font-size:.72rem;font-weight:bold}}
.badge.A{{background:var(--green-bg);color:var(--green)}}.badge.B{{background:var(--amber-bg);color:var(--amber)}}.badge.C{{background:var(--red-bg);color:var(--red)}}
.seen.img{{color:var(--blue);font-size:.7em;vertical-align:middle}}.seen.cat{{color:var(--muted);font-size:.8em;vertical-align:middle}}
tr.d td{{padding:0 1.2rem 1rem 1.2rem;background:color-mix(in srgb,var(--gold) 12%,transparent)}}
.det{{display:grid;gap:.35rem;font-size:.86rem;color:var(--ink2);max-width:62rem}}
.det b{{color:var(--head);font-weight:600}}
.legend{{font-family:var(--mono);font-size:.72rem;color:var(--muted);margin:.4rem 0 1rem;display:flex;flex-wrap:wrap;gap:.4rem 1.2rem}}
.nojs .jsonly{{display:none}}
.ko{{display:block;font-size:.8rem;color:var(--ink2);margin-top:.25rem;line-height:1.4}}
.ko i{{font-style:normal;font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;padding:.02rem .4rem;border-radius:999px;margin-right:.3rem}}
.ko i.k{{background:var(--green-bg);color:var(--green)}}.ko i.o{{background:var(--amber-bg);color:var(--amber)}}
.det .kn b{{color:var(--green)}}.det .op b{{color:var(--amber)}}.asof{{font-family:var(--mono);font-size:.7rem;color:var(--muted)}}
.state .cols{{display:grid;grid-template-columns:1fr 1fr;gap:1rem}}
.state .card{{background:var(--panel);border:1px solid var(--rule);border-radius:var(--radius);padding:.6rem 1.1rem .8rem}}
.state .card.wide{{margin-top:1rem}}.state h3{{margin:.4rem 0 .5rem}}
.state summary{{cursor:pointer;font-family:var(--mono);font-size:.78rem;color:var(--gold)}}
ul.sl{{font-size:.84rem;padding-left:1.1rem;max-height:32rem;overflow-y:auto}}ul.sl li{{margin:.3rem 0}}.d{{color:var(--muted);font-size:.78rem}}
table.gone{{border-collapse:collapse;font-size:.84rem;width:100%}}table.gone td,table.gone th{{border-bottom:1px solid var(--rule);padding:.35rem .5rem;text-align:left;vertical-align:top}}
#hashnote{{background:var(--amber-bg);border:1px solid var(--amber);border-radius:var(--radius);padding:.6rem 1rem;margin:1rem 0}}
@media (max-width:700px){{table.cat{{min-width:760px}}.state .cols{{grid-template-columns:1fr}}}}
</style>
</head>
<body id="top" class="nojs">
<!-- site:nav -->

<section class="hero">
  <p class="kicker">Gallica · DECODE · cryptiana fine print · calendars · Cryptoole · {min(e['year'] for e in E if e['year'])}–{max(e['year'] for e in E if e['year'])} · {len(counted)} open targets · {len(E) - len(counted)} noted · {n_gone} moved out to <a href="writeups.html">write-ups</a> · status as of {fmt_day(AS_OF)} · unvalidated</p>
  <h1>The Unsolved Catalogue</h1>
  <p class="sub">What is still in cipher in the digitised diplomatic volumes, and nobody has read. The first entries came from the French volumes on Gallica; the rest ({n_dec}) from the DECODE database, every ciphertext record it marks non-decrypted or partly decrypted, grouped into letters and series and checked against this repository's own targets and Tomokiyo's list. A sweep of 22 Sept 2026 added candidates for new solves and outside reads (tagged <em>new 22 Sept</em>): DECODE records never classified, letters Tomokiyo calls undeciphered while naming a key, Gallica notices and the printed calendars. On 14 Oct 2026 open items were pulled from Satoru&rsquo;s <a href="https://cryptoole.satoru.net/" rel="noopener">Cryptoole</a> index (DECODE, Tomokiyo&rsquo;s unsolved list) and checked against the repository; the ones not already here or solved elsewhere were added with source <em>Cryptoole</em>, so a few now come from Tomokiyo&rsquo;s list. Each entry is scored 1–5 for <b>historical importance</b> (what the text could add), <b>solvability</b> (odds of a full reading with the material online) and <b>difficulty</b> (the technical work), and the <b>priority</b> is a weighted blend you can reweight. Class <b>A</b> means siblings with decipherment in the same volume, <b>B</b> a partial key or known family in print, <b>C</b> no key and no sibling. Entries read, partly read, resolved or found already in print here are taken out of the catalogue and written up (<a href="writeups.html">write-ups</a>; <a href="#gone">look up an old number</a>); those attempted here without a reading stay, tagged <b>attempted, open</b>.</p>
  <p class="sub">Scores are judgements from catalogue descriptions and the literature, not from the leaves: {n_img} of {n_all} entries have been viewed on the image, and each carries the check that would confirm it is open. Data: <a href="https://github.com/dbourdeau/cyphersolver/blob/main/catalogue.json" rel="noopener">catalogue.json</a> · text: <a href="https://github.com/dbourdeau/cyphersolver/blob/main/CATALOGUE.md" rel="noopener">CATALOGUE.md</a>.</p>
  <p class="meta">Daniel Bourdeau · September 2026</p>
</section>

<main>
<div id="hashnote" hidden></div>
{state}
<h2>The catalogue</h2>
<div class="ctl jsonly">
  <div class="row">
    <label>Search <input type="search" id="q" placeholder="name, place, shelfmark, year…" aria-label="Search the catalogue"></label>
    <label>importance <input type="range" id="w_imp" min="0" max="100" value="{int(W['importance']*100)}"><span class="wv" id="v_imp"></span></label>
    <label>solvability <input type="range" id="w_sol" min="0" max="100" value="{int(W['solvability']*100)}"><span class="wv" id="v_sol"></span></label>
    <label>ease <input type="range" id="w_eas" min="0" max="100" value="{int(W['ease']*100)}"><span class="wv" id="v_eas"></span></label>
    <button type="button" class="chip" id="reset">reset</button>
  </div>
  {facet('cls', 'Class', ['A', 'B', 'C'])}
  {facet('period', 'Period', periods)}
  {facet('region', 'Region', regions)}
  {facet('source', 'Source', sources)}
  {facet('seen', 'Seen', ['image', 'catalogue'])}
  {facet('counted', 'Set', ['counted', 'also noted'])}
  {facet('outcome', 'Outcome', ['open', 'attempted, open'])}
  <div class="count" id="count"></div>
</div>
<div class="legend"><span>click a column to sort, a row to expand</span><span>● viewed on the image</span><span>◇ catalogue description only</span><span>gold dots importance / solvability</span><span>red dots difficulty</span></div>

<div class="tw"><table class="cat" id="cat">
<colgroup><col class="c-prio"><col class="c-date"><col class="c-item"><col class="c-shelf"><col class="c-sc"><col class="c-sc"><col class="c-sc"><col class="c-cls"></colgroup>
<thead><tr>
<th class="prio" data-sort="prio" aria-sort="descending">Priority</th><th data-sort="year">Date</th><th data-sort="title">Item</th><th>Shelfmark</th>
<th class="sc" data-sort="importance">Import.</th><th class="sc" data-sort="solvability">Solvab.</th><th class="sc" data-sort="difficulty">Difficulty</th><th class="cls" data-sort="cls">Class</th>
</tr></thead>
<tbody>
{"".join(row(e) for e in ordered)}
</tbody></table></div>

<h2 id="gone">Numbers that have left the catalogue</h2>
<p>{n_gone} catalogue numbers as of {fmt_day(AS_OF)}, with the write-ups that took them out and the day each landed. <i>(part)</i> marks a split entry: that piece has an outcome, and any piece still open stays in the table above under its number.</p>
<div style="overflow-x:auto"><table class="gone"><thead><tr><th>No.</th><th>Write-up</th><th>Outcome</th><th>Landed</th></tr></thead><tbody>{gone_rows}</tbody></table></div>

<h2>How the scores were set</h2>
<p><b>Importance</b> asks what a full reading would add: 5 for a first-hand report of a major event by a principal witness (du Bellay in London 1529, Lanssac at the Polish election), 2 for routine business. <b>Solvability</b> asks whether the material online is enough: 5 when deciphered siblings of the same hand and year sit in the same volume, 1 for one short letter in an unknown language. <b>Difficulty</b> is the technical work at the keyboard: 1 for aligning a known sibling, 5 for a statistics-only attack on a large homophonic nomenclator. The default priority weights importance {W['importance']}, solvability {W['solvability']} and ease {W['ease']} (ease is 6 minus difficulty), rescaled to 0–10; move the sliders to see the order change. Every score is a judgement made before viewing the leaf, so treat the order as a work plan, not a finding.</p>
<p><b>Checked:</b> catalogue descriptions and item numbering; presence or absence of a decipherment item in each volume; shelfmarks from the IIIF manifests; fr. 16127 and fr. 3484 f. 34 on the image. For the DECODE entries: the record metadata and notes, key records from the same archive series, overlap with this repository's targets and with Tomokiyo's list (27 groups dropped as solved or already tracked). <b>Not checked:</b> the other leaves; Tomokiyo's François I article; the Scheurer, Savasse and Mousset editions; any DECODE image. Entries tagged <i>rule-scored</i> were scored by a script from DECODE's metadata (a key in the series or on the leaf, length, language, who wrote to whom) and not yet reviewed by hand. <b>User must verify</b> each entry on the image and in the literature before attacking it.</p>
</main>
<!-- site:footer -->
<script id="catdata" type="application/json">{data_js}</script>
<script>
(function(){{
document.body.classList.remove('nojs');
var D=JSON.parse(document.getElementById('catdata').textContent),E=D.entries,byId={{}};E.forEach(function(e){{byId[e.id]=e;}});
var tb=document.querySelector('#cat tbody'),rows={{}};
Array.prototype.forEach.call(tb.querySelectorAll('tr.e'),function(r){{rows[r.dataset.id]={{e:r,d:tb.querySelector('tr.d[data-for="'+r.dataset.id+'"]')}};}});
var state={{q:'',sort:'prio',dir:-1,w:{{imp:D.weights.importance,sol:D.weights.solvability,eas:D.weights.ease}},f:{{}}}};
function prio(e){{var w=state.w,t=w.imp+w.sol+w.eas||1;var v=(w.imp*e.importance+w.sol*e.solvability+w.eas*(6-e.difficulty))/t;return Math.round((v-1)/4*100)/10;}}
function match(e){{var f=state.f;for(var k in f){{if(!f[k].length)continue;var v=k==='counted'?(e.counted?'counted':'also noted'):k==='outcome'?(e.outcome||'open'):e[k];if(f[k].indexOf(v)<0)return false;}}
 if(state.q){{var h=(e.title+' '+e.correspondents+' '+e.place+' '+e.shelfmark+' '+e.why+' '+e.status+' '+e.region+' '+e.language+' '+e.date+' '+e.year).toLowerCase();if(h.indexOf(state.q)<0)return false;}}return true;}}
function key(e){{var s=state.sort;if(s==='prio')return prio(e)-((e.outcome&&e.outcome.indexOf('attempted')!==0)?100:0);if(s==='seen')return e.seen==='image'?1:0;if(s==='cls'||s==='title')return e[s];return +e[s];}}
function render(){{var L=E.filter(match);L.sort(function(a,b){{var x=key(a),y=key(b);if(x<y)return -1*state.dir;if(x>y)return 1*state.dir;return a.id-b.id;}});
 var shown={{}};L.forEach(function(e){{var r=rows[e.id];r.e.querySelector('td.prio b').textContent=prio(e).toFixed(1);tb.appendChild(r.e);tb.appendChild(r.d);r.e.hidden=false;r.d.hidden=r.e.getAttribute('aria-expanded')!=='true';shown[e.id]=1;}});
 E.forEach(function(e){{if(!shown[e.id]){{rows[e.id].e.hidden=true;rows[e.id].d.hidden=true;}}}});
 document.getElementById('count').textContent=L.length+' of '+E.length+' entries';
 document.getElementById('v_imp').textContent=state.w.imp.toFixed(2);document.getElementById('v_sol').textContent=state.w.sol.toFixed(2);document.getElementById('v_eas').textContent=state.w.eas.toFixed(2);
 Array.prototype.forEach.call(document.querySelectorAll('#cat th[data-sort]'),function(h){{h.setAttribute('aria-sort',h.dataset.sort===state.sort?(state.dir<0?'descending':'ascending'):'none');}});}}
function toggle(r){{var open=r.getAttribute('aria-expanded')==='true';r.setAttribute('aria-expanded',open?'false':'true');rows[r.dataset.id].d.hidden=open;}}
Array.prototype.forEach.call(tb.querySelectorAll('tr.e'),function(r){{r.addEventListener('click',function(ev){{if(ev.target.closest('a'))return;toggle(r);}});r.addEventListener('keydown',function(ev){{if(ev.key==='Enter'||ev.key===' '){{ev.preventDefault();toggle(r);}}}});}});
Array.prototype.forEach.call(document.querySelectorAll('#cat th[data-sort]'),function(h){{h.addEventListener('click',function(){{var s=h.dataset.sort;if(state.sort===s)state.dir=-state.dir;else{{state.sort=s;state.dir=(s==='id'||s==='year'||s==='title'||s==='cls'||s==='difficulty')?1:-1;}}render();}});}});
Array.prototype.forEach.call(document.querySelectorAll('.chip[data-facet]'),function(b){{b.addEventListener('click',function(){{var k=b.dataset.facet,v=b.dataset.val;state.f[k]=state.f[k]||[];var i=state.f[k].indexOf(v);if(i<0)state.f[k].push(v);else state.f[k].splice(i,1);b.setAttribute('aria-pressed',i<0?'true':'false');render();}});}});
document.getElementById('q').addEventListener('input',function(ev){{state.q=ev.target.value.trim().toLowerCase();render();}});
[['w_imp','imp'],['w_sol','sol'],['w_eas','eas']].forEach(function(p){{document.getElementById(p[0]).addEventListener('input',function(ev){{state.w[p[1]]=ev.target.value/100;render();}});}});
document.getElementById('reset').addEventListener('click',function(){{state.q='';state.sort='prio';state.dir=-1;state.w={{imp:D.weights.importance,sol:D.weights.solvability,eas:D.weights.ease}};state.f={{}};document.getElementById('q').value='';document.getElementById('w_imp').value=state.w.imp*100;document.getElementById('w_sol').value=state.w.sol*100;document.getElementById('w_eas').value=state.w.eas*100;Array.prototype.forEach.call(document.querySelectorAll('.chip[data-facet]'),function(b){{b.setAttribute('aria-pressed','false');}});render();}});
var qm=/[?&]q=([^&#]+)/.exec(location.search);if(qm){{var qv=decodeURIComponent(qm[1].replace(/\\+/g,' '));document.getElementById('q').value=qv;state.q=qv.trim().toLowerCase();}}
render();
var G={gone_js};
var hm=/^#e(\\d+)$/.exec(location.hash);if(hm&&!rows[hm[1]]&&G[hm[1]]){{var hn=document.getElementById('hashnote');hn.innerHTML='Catalogue no. '+hm[1]+' is no longer open: '+G[hm[1]].map(function(x){{var t=x[0].replace(/&/g,'&amp;').replace(/</g,'&lt;');return x[1]?'<a href="'+x[1]+'.html">'+t+'</a>':t;}}).join(' · ');hn.hidden=false;hn.scrollIntoView();}}
if(hm&&rows[hm[1]]){{var r0=rows[hm[1]].e;if(r0.getAttribute('aria-expanded')!=='true')toggle(r0);r0.scrollIntoView({{block:'center'}});}}
}})();
</script>
</body>
</html>
'''
    (HERE / 'catalogue.html').write_text(page, encoding='utf-8')
    print('wrote catalogue.html', len(page), 'entries', len(E))


if __name__ == '__main__':
    update_md()
    build_html()
    import subprocess, sys
    subprocess.run([sys.executable, '_build_site.py'], check=True, cwd=pathlib.Path(__file__).parent)
