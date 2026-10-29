"""Build docs/archives.html: the requests a volunteer can take to an archive or a library, from ../archive_requests.json.

The ledger is seeded from the "blocker: needs-physical-access" gaps in targets/*/NOTES.md by
tools/seed_archive_requests.py and kept by hand after that (status, history, volunteer). The page groups the requests by
archive, since people volunteer for the archive they live near or travel to, and gives each one an "I can do this" link
that opens the archive-visit issue form with the request filled in.

Called from _build_site.py before the pages are processed, like further.html, so it gets the nav and footer.
"""
import html, json, pathlib, re
from urllib.parse import urlencode

HERE = pathlib.Path(__file__).parent
LEDGER = HERE.parent / 'archive_requests.json'
REPO = 'https://github.com/dbourdeau/cyphersolver'
KIND = {'visit': ('reading room', 'Go to the reading room and look at, or photograph, the original.'),
        'order': ('order', 'Ask the archive for a scan or a reproduction: an email or an order form, sometimes a fee.'),
        'library': ('library', 'A printed book or a database behind a login: a university library card or a subscription is enough.')}
STATUS = {'open': 'open', 'claimed': 'taken', 'requested': 'asked the archive', 'received': 'images in hand',
          'closed': 'gap closed', 'unavailable': 'not available'}
LIVE = ('open', 'claimed', 'requested')


def esc(t):
    return html.escape(str(t or ''), quote=False)


def attr(t):
    return html.escape(str(t or ''), quote=True)


def load():
    return json.loads(LEDGER.read_text(encoding='utf-8'))['requests'] if LEDGER.is_file() else []


def pages_by_folder(pages):
    out = {}
    for p in pages:
        for f in p.get('folders') or []: out.setdefault(f, p)
    return out


def issue_url(r):
    q = {'template': 'archive-visit.yml', 'title': f'Archive request: {r["id"]} ({r["archive"]})', 'request': r['id'],
         'archive': ', '.join(x for x in (r['archive'], r.get('shelfmark')) if x and x != 'unknown')}
    return f'{REPO}/issues/new?' + urlencode(q)


def who(r):
    v = r.get('volunteer') or {}
    if not v.get('name'): return ''
    return f' · {esc(v["name"])}{(", " + esc(v["month"])) if v.get("month") else ""}'


def target_link(r, bypage):
    t = r.get('target')
    if not t: return '<span class="tgt">general</span>'
    p = bypage.get(t)
    if p: return f'<a class="tgt" href="{p["slug"]}.html">{re.sub(r"<[^>]+>", "", p["label"] or p["slug"])}</a>'
    return f'<a class="tgt" href="{REPO}/tree/main/targets/{t}" rel="noopener">{esc(t)}</a>'


def row(r, bypage):
    k = r['kind']
    issue = f' · <a href="{REPO}/issues/{r["issue"]}" rel="noopener">issue #{r["issue"]}</a>' if r.get('issue') else ''
    act = (f'<a class="take" href="{attr(issue_url(r))}" rel="noopener">I can do this</a>' if r['status'] == 'open' else
           f'<span class="st st-{r["status"]}">{STATUS.get(r["status"], r["status"])}</span>')
    why = f'<span class="why2">{esc(r["why"])}</span>' if r.get('why') else ''
    shelf = f'<span class="sm">{esc(r["shelfmark"])}</span>' if r.get('shelfmark') else ''
    text = ' '.join(x for x in (r['id'], r.get('target') or '', r['archive'], r.get('city', ''), r.get('shelfmark', ''),
                                r['need'], r.get('why', ''), KIND[k][0])).lower()
    return (f'<li class="rq" data-kind="{k}" data-status="{r["status"]}" data-q="{attr(text)}">'
            f'<div class="hd"><span class="id">{r["id"]}</span><span class="kd kd-{k}">{KIND[k][0]}</span>{target_link(r, bypage)}{shelf}</div>'
            f'<p class="nd">{esc(r["need"])}</p>{why}'
            f'<div class="ft">{act}{who(r)}{issue}</div></li>')


def groups(reqs):
    g = {}
    for r in reqs: g.setdefault((r['archive'], r.get('city') or ''), []).append(r)
    last = ('A library or database', 'unknown')
    return sorted(g.items(), key=lambda kv: (kv[0][0] in last, -sum(r['status'] in LIVE for r in kv[1]), kv[0][0]))


def gid(name):
    return 'a-' + re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def build_html(pages):
    reqs = load()
    bypage = pages_by_folder(pages)
    live = [r for r in reqs if r['status'] in LIVE]
    n = {s: sum(r['status'] == s for r in reqs) for s in STATUS}
    nk = {k: sum(r['kind'] == k for r in live) for k in KIND}
    G = groups(live)
    places = len({a for (a, _), _ in G if a not in ('A library or database', 'unknown')})
    toc = ''.join(f'<li><a href="#{gid(a)}">{esc(a)}</a>{f" <span>{esc(c)}</span>" if c else ""} <b>{len(rs)}</b></li>' for (a, c), rs in G)
    secs = ''.join(
        f'<section class="arch" id="{gid(a)}"><h3>{esc("Archive not yet identified" if a == "unknown" else a)}'
        f'{f" <span class=city>{esc(c)}</span>" if c else ""}<span class="n">{len(rs)}</span></h3>'
        f'<ul class="rqs">{"".join(row(r, bypage) for r in sorted(rs, key=lambda r: (r["status"] != "open", r["id"])))}</ul></section>'
        for (a, c), rs in G)
    done = [r for r in reqs if r['status'] not in LIVE]
    done_html = (f'<ul class="rqs done">{"".join(row(r, bypage) for r in sorted(done, key=lambda r: r["history"][-1]["date"], reverse=True))}</ul>'
                 if done else '<p class="none">None yet. The first photograph that closes a gap will be listed here, with its volunteer.</p>')
    kinds = ''.join(f'<li><span class="kd kd-{k}">{lab}</span> {desc} <b>{nk[k]}</b></li>' for k, (lab, desc) in KIND.items())
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>To the Archive — {len(live)} open requests</title>
<meta name="description" content="{len(live)} pieces of historical cipher letters that only an archive or a library can supply: leaves to photograph, reproductions to order, books to look up. Take one on.">
<link rel="stylesheet" href="style.css">
</head>
<body id="top" class="nojs">
<!-- site:nav -->

<section class="hero">
  <p class="kicker">{len(live)} open requests · {places} archives · {n["claimed"] + n["requested"]} under way · {n["received"] + n["closed"]} done</p>
  <h1>To the <span class="stk">Archive<a class="sticker arc" href="#list" title="Pick a request below"><span><b>Go<br>Look!</b><small>pick a request</small></span></a></span></h1>
  <p class="sub">Some readings stop where the scans stop: a line lost in the binding, a leaf nobody photographed, a decipherment filed in a volume that was never digitised, a book behind a login. Each request below is one of those gaps. If you live near the archive, travel past it, or have a library card that reaches the book, you can close it.</p>
  <ol class="steps"><li><b>1</b>find an archive you can reach</li><li><b>2</b>click &ldquo;I can do this&rdquo;</li><li><b>3</b>look, photograph or order</li><li><b>4</b>send the images; you are credited</li></ol>
</section>

<main>
<ul class="kinds">{kinds}</ul>

<div class="qbar jsonly" id="list">
  <input type="search" id="q" placeholder="Search: archive, city, shelfmark, cipher…" aria-label="Search the requests">
  <span class="kf" role="group" aria-label="Kind"><button type="button" data-k="" aria-pressed="true">all</button><button type="button" data-k="visit" aria-pressed="false">reading room</button><button type="button" data-k="order" aria-pressed="false">order</button><button type="button" data-k="library" aria-pressed="false">library</button></span>
  <span class="count" id="count"></span>
</div>
<details class="toc"><summary>By archive ({len(G)})</summary><ul>{toc}</ul></details>
{secs}

<h2 id="done">Done</h2>
{done_html}

<h2>How it works</h2>
<p>Click <b>I can do this</b> on a request. It opens a short form on GitHub with the request filled in: say how you will do it (visit, order, library) and roughly when, by month. The request is then marked as taken on this page, so two people do not go for the same leaf. When you have the images or the text, send them on the same issue, or by <a href="contribute.html#email">email</a> if you do not use GitHub. Say whether the images may be shown on the site; they are always credited to you and to the archive.</p>
<p>Before photographing, check the archive&rsquo;s rules: most reading rooms allow it without flash, some ask for a form or a fee. A phone photograph of the whole page, flat, with the folio number visible, is enough for most requests; for a line in the gutter, one more of the page edge. Do not cut or mark anything to see better: say what you could not see and that closes the request too.</p>
<p>Something not listed? Use the same form to propose a request. Each one here comes from a write-up&rsquo;s notes, its &ldquo;Remaining gaps&rdquo;, where the gap is marked as needing the archive; the list is rebuilt with the site. The ledger is <a href="{REPO}/blob/main/archive_requests.json" rel="noopener">archive_requests.json</a>. Credit works as for every contribution: <a href="contribute.html">contribute</a>.</p>
</main>
<!-- site:footer -->
<script>
(function(){{
document.body.classList.remove('nojs');
var rows=[].slice.call(document.querySelectorAll('li.rq')),secs=[].slice.call(document.querySelectorAll('section.arch')),q=document.getElementById('q'),c=document.getElementById('count'),bs=[].slice.call(document.querySelectorAll('.kf button')),k='';
function render(){{var s=q.value.trim().toLowerCase(),n=0,t=0;rows.forEach(function(r){{if(r.closest('.done'))return;t++;var ok=(!s||r.dataset.q.indexOf(s)>=0)&&(!k||r.dataset.kind===k);r.hidden=!ok;if(ok)n++;}});
 secs.forEach(function(x){{x.hidden=!x.querySelector('li.rq:not([hidden])');}});c.textContent=n+' of '+t+' requests';}}
bs.forEach(function(b){{b.addEventListener('click',function(){{k=b.dataset.k;bs.forEach(function(x){{x.setAttribute('aria-pressed',x===b?'true':'false');}});render();}});}});
q.addEventListener('input',render);render();
}})();
</script>
</body>
</html>
'''
    (HERE / 'archives.html').write_text(page, encoding='utf-8')
    return len(live)


def requests_for(folder):
    """Open requests of one target, for the link from its further page."""
    return [r for r in load() if r.get('target') == folder and r['status'] in LIVE]
