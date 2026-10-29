"""Backfill `access` and `access_note` on catalogue.json entries that have no `access` yet (28 Oct 2026).

    python research/archive_sweep_2026-10/access_backfill.py            # dry run: counts + access_uncertain.md
    python research/archive_sweep_2026-10/access_backfill.py --write    # write catalogue.json

Signals, from the entry's own fields only (nothing is fetched):
- online: seen = image(s)/viewed, needs_archive_scan "no", a Gallica ark, an image link (Gallica, e-codices, DECODE
  record, IIIF ...), or text saying images/scans are online or digitised (not when hedged: "check whether ...").
  Links to printed catalogues and calendars (archive.org, HathiTrust) do not count: they show the description,
  not the ciphertext;
- archive: needs_archive_scan "yes", or text saying not digitised / not scanned / no images / physical only / scan
  order / reproduction request / reading room.
One side only -> that value with a note quoting the evidence. Both sides or neither -> left as it is and listed in
access_uncertain.md for a person to decide. Entries that already carry `access` are never touched.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

ARCHIVE = re.compile(
    r"not (?:yet )?(?:digiti[sz]ed|scanned|online|imaged|filmed)|no (?:online )?(?:images?|scans?|digiti[sz]ation|"
    r"digital (?:copy|images?)|viewer)(?! needed)|images? (?:are )?not (?:online|available|digiti[sz]ed)|"
    r"physical(?: only)?\b|availability PHYSICAL|scan[- ]?(?:order|request|on[- ]demand)|order(?:ing)? (?:a )?"
    r"(?:scans?|copies|photos?|photographs|reproductions?|digiti[sz]ation)|reproduction (?:order|request)|"
    r"reading[- ]room|in situ|archive (?:visit|trip)|needs? (?:the )?archive|ask the (?:library|archive)|"
    r"only on microfilm|microfilm only|offline|order\b[^.;]{0,40}\b(?:images|scans|copies|reproductions|photos)|"
    r"ask (?:the )?(?:archiv\w*|librar\w*|bibliot\w*|record office|state archives?|staatsarchiv\w*)|write to (?:the )?archiv|"
    r"request (?:a )?(?:copy|copies|scans|images|photos|reproductions?|digiti[sz]ation)|"
    r"(?:copy|copies|reproduction|digiti[sz]ation|scan) request", re.I)
ONLINE = re.compile(
    r"images? (?:are |is )?(?:online|on (?:DECODE|Gallica|PARES|the record|e-codices|Europeana|the viewer))|"
    r"scans? (?:are )?(?:online|on DECODE)|digiti[sz]ed|\bIIIF\b|on Gallica|Gallica (?:ark|images|scans|viewer)|"
    r"e-codices|images on DECODE|DECODE (?:images|scans)|viewed (?:the )?(?:images?|scans?)|"
    r"online (?:images|scans|facsimile|viewer)|facsimile online", re.I)
HEDGE = re.compile(r"(?:whether|if|check|unclear|unknown|may be|might be|perhaps|probably|find|look for)\b[^.;]{0,40}$", re.I)
HEDGE_AFTER = re.compile(r"^[^.;]{0,25}\b(?:if any|not found|not located|\?)", re.I)
IMAGE_HOSTS = re.compile(r"gallica\.bnf\.fr/ark|e-codices|de-crypt\.org|digi\.vatlib|iiif|bdh-rd\.bne\.es|"
                         r"bvpb\.mcu\.es|europeana\.eu/.+/item|digitale-sammlungen|"
                         r"manuscripts\.bl\.uk|bl\.uk/manuscripts|onb\.ac\.at|mdz-nbn|e-rara|dfg-viewer|"
                         r"/images/|imagesonline|archives-nationales.culture.gouv.fr/.*/media", re.I)
SEEN_ONLINE = re.compile(r"^(?:images?|viewed|partly|images and transcriptions.*)$", re.I)


def evidence(e):
    text = ' '.join(str(e.get(k) or '') for k in ('folio_note', 'status', 'verify', 'access_note', 'prior_art'))
    on, off = [], []
    if SEEN_ONLINE.match(e.get('seen') or ''):
        on.append(f"seen: {e['seen']}")
    nas = e.get('needs_archive_scan')
    if nas == 'no': on.append('needs_archive_scan: no')
    if nas == 'yes': off.append('needs_archive_scan: yes')
    if e.get('ark'): on.append('Gallica ark ' + e['ark'])
    for l in e.get('links') or []:
        if IMAGE_HOSTS.search(l.get('href') or ''):
            on.append(f"link {l.get('label') or ''} ({l['href']})"); break
    for m in ARCHIVE.finditer(text):
        off.append(snip(text, m))
    masked = ARCHIVE.sub(' ', text)            # "not digitised" must not count as "digitised"
    for m in ONLINE.finditer(masked):
        if not (HEDGE.search(masked[max(0, m.start() - 60):m.start()]) or HEDGE_AFTER.search(masked[m.end():m.end() + 40])):   # "check whether the scans are online"
            on.append(snip(masked, m))
    return on, off


def snip(t, m, w=60):
    a, b = max(0, m.start() - w), min(len(t), m.end() + w)
    return ('...' if a else '') + re.sub(r'\s+', ' ', t[a:b]).strip() + ('...' if b < len(t) else '')


def main(write):
    path = os.path.join(ROOT, 'catalogue.json')
    cat = json.load(open(path, encoding='utf-8'))
    n = {'archive': 0, 'online': 0, 'uncertain': 0, 'kept': 0}
    unc = []
    for e in cat['entries']:
        if e.get('access'):
            n['kept'] += 1
            continue
        on, off = evidence(e)
        if off and not on:
            e['access'] = 'archive'
            e.setdefault('access_note', 'not online (backfilled 28 Oct 2026 from the entry: ' + off[0][:160] + ')')
            n['archive'] += 1
        elif on and not off:
            e['access'] = 'online'
            e.setdefault('access_note', 'online (backfilled 28 Oct 2026 from the entry: ' + on[0][:160] + ')')
            n['online'] += 1
        else:
            n['uncertain'] += 1
            unc.append((e, on, off))
    print(n)
    out = ['# Catalogue entries whose archive access could not be decided (28 Oct 2026)', '',
           'From `access_backfill.py`: the entry\'s own fields gave either no access evidence or evidence both ways.',
           'Set `access` ("archive" or "online") and `access_note` by hand after a look at the links.', '',
           f'{sum(1 for u in unc if u[1] and u[2])} with conflicting evidence, {sum(1 for u in unc if not (u[1] or u[2]))} with none.', '']
    cell = lambda s: (s or '').replace('|', '/').replace('\n', ' ')[:140]

    def table(rows, signals):
        head = '| # | Item | Shelfmark | ' + ('Online signal | Archive signal | ' if signals else '') + 'Links |'
        res = [head, '|' + '---|' * (head.count('|') - 1)]
        for e, on, off in sorted(rows, key=lambda u: u[0]['id']):
            links = ' '.join(f"[{(l.get('label') or 'link')[:30]}]({l['href']})" for l in (e.get('links') or [])[:2] if l.get('href'))
            sig = f"{cell(on[0] if on else '')} | {cell(off[0] if off else '')} | " if signals else ''
            res.append(f"| {e['id']} | {cell(e['title'])[:90]} | {cell(e['shelfmark'])[:80]} | {sig}{links} |")
        return res + ['']

    out += ['## Conflicting evidence', ''] + table([u for u in unc if u[1] and u[2]], True)
    out += ['## No evidence, grouped by holding', '',
            'Groups where the item is known only from a printed calendar or catalogue (CSP, L&P, Clarendon, Lope de Soria)',
            'usually point to an original that is not online; one decision per group is often enough.', '']
    groups = {}
    for u in unc:
        if not (u[1] or u[2]):
            groups.setdefault(re.split(r'[,(;:]', u[0]['shelfmark'])[0].strip()[:60] or '(no shelfmark)', []).append(u)
    for g, rows in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        out += [f'### {g} ({len(rows)})', ''] + table(rows, False)
    open(os.path.join(HERE, 'access_uncertain.md'), 'w', encoding='utf-8').write('\n'.join(out))
    if write:
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(cat, fh, ensure_ascii=False, indent=1)
            fh.write('\n')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main('--write' in sys.argv)
