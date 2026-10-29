"""Archive access for the largest undecided groups, settled by checking each entry's links (28 Oct 2026).

    python research/archive_sweep_2026-10/access_groups.py            # dry run
    python research/archive_sweep_2026-10/access_groups.py --write    # write catalogue.json and research/leads.json

What was checked, per host:
- francearchives.gouv.fr facomponent pages (fetched in a browser; scripts are refused): online when the page shows
  the IIIF viewer (ANOM images) or the access note "document numérisé"; otherwise no viewer is linked.
- archivinformationssystem.at (HHStA): no record carries a digitisation field or image; reading room only.
- gams.uni-graz.at kuse edition: facsimile + IIIF viewer (entry 516).
- catalog.archives.gov: proxy/records/search?naId=<id> -> digitalObjects (all linked records have 329-1,416 images).
- Digital Bodleian search: MS Tanner 62 and MS Eng. lett. d. 37 not found; MS Clarendon only vols. 128 and 155.
- TNA SP 53 / SP 63: originals imaged only in Gale's State Papers Online (subscription), not on TNA Discovery.
Not settled: AGS (PARES answered 429 Too Many Requests), IMH Academia Sinica (catalog.digitalarchives.tw blocks
this IP, browser included), and NARA entries linked only to printed editions (634, 635, 641).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATE = '28 Oct 2026'

FA_ONLINE = {'081b520c51251465e455fe0eef1b5da8f604fe08': 'IIIF viewer (ANOM images)',
             '192fca363ec4d92bb1b7db8cf826d13c82e353ca': 'IIIF viewer (ANOM images)',
             '246c20ac168f80a9584955043ceb760e228d2029': 'IIIF viewer (ANOM images)',
             '89b1a695b08fed97b6694c2befc4dd351755b9c8': 'IIIF viewer (ANOM images)',
             'b9a6451ece7b0f272aa9896771bfa52d3883f927': 'IIIF viewer (ANOM images)',
             '20409c543d169eee5e9482fe6108a1b5bf02fb64': '"document numérisé"',
             '59d9030f7243585500e96dca1119f3ab56358d2f': '"document numérisé"',
             '981fb09cc409d3dd8837b45b29d5bc2d264f9a19': '"document numérisé"',
             'd8938010dfe31f140338a7c374c4ddf8d9381fec': '"document numérisé"',
             'e44100f6fab69aead0ea31697d4d939bd6202e03': '"document numérisé"'}
NARA_DIGITISED = {'188609418': 329, '213803757': 1058, '27128808': 798, '27133946': 796, '27140577': 839,
                  '27158076': 1324, '27179174': 972, '574876562': 929, '87662081': 1416}
BODLEIAN = {476: 'MS Eng. lett. d. 37 not found on Digital Bodleian', 479: 'MS Tanner 62 not on Digital Bodleian'}
CLARENDON = 'Digital Bodleian has only MS Clarendon 128 and 155; the 1650s Clarendon State Papers are not imaged'
TNA_SP = 'TNA SP original: imaged only in Gale State Papers Online (subscription), not on Discovery'


# Second pass (28 Oct 2026), checked one by one:
# - Houghton (HOLLIS, fetched in a browser): only hou01430c00499 links a digital object (FHCL.HOUGH:38447771); the
#   others carry only the generic Houghton links; hou01502 is a microfilm.
# - MHS collection guides: Sargent (fa0261) is a microfilm edition, Kimball-Griswold (fa0549) has no digital copies.
# - AGAD 435: scan album on agadd2 for sygn. 279a.
# Not settled: AGS (PARES still 429), BN Portugal (Manuscriptorium shows nothing without a login), Riksarkivet
# (CAPTCHA), RAH Salazar (bot check), MHS fa0271/fa0153 ("some documents digitised", which ones not said),
# AGAD 436/437 (inventory XML only), Riksarkivet 1126/1127 (printed edition only).
BY_ID = {
    1285: ('online', 'Houghton digital object urn-3:FHCL.HOUGH:38447771'),
    1281: ('archive', 'HOLLIS record has no digital object; Houghton reading room or imaging request'),
    1282: ('archive', 'HOLLIS record has no digital object; Houghton reading room or imaging request'),
    1283: ('archive', 'HOLLIS records have no digital object; Houghton reading room or imaging request'),
    1284: ('archive', 'HOLLIS record has no digital object; Houghton reading room or imaging request'),
    1286: ('archive', 'Houghton holds a microfilm; no digital object in HOLLIS'),
    1294: ('archive', 'MHS microfilm edition only (Winthrop Sargent Papers guide, which has a "Cipher Key" section)'),
    1295: ('archive', 'MHS collection guide lists no digital copies'),
    435: ('online', 'scan album on agadd2 (APP 335 sygn. 279a)'),
}


def decide(e):
    """Return (access, note) or None when the links do not settle it."""
    if e['id'] in BY_ID:
        a, note = BY_ID[e['id']]
        return a, f'{note} (checked {DATE})'
    links = [l.get('href') or '' for l in e.get('links') or []]
    shelf = e.get('shelfmark') or ''
    fa = [re.search(r'facomponent/([0-9a-f]{40})', h).group(1) for h in links if 'francearchives' in h and 'facomponent/' in h]
    if fa:
        on = [f'{h[:8]}: {FA_ONLINE[h]}' for h in fa if h in FA_ONLINE]
        if on:
            return 'online', f'FranceArchives record shows images ({"; ".join(on)}) (checked {DATE})'
        return 'archive', f'FranceArchives record has no viewer and no "numérisé" note; check the AN/ANOM site before ordering (checked {DATE})'
    if any('gams.uni-graz.at' in h for h in links):
        return 'online', f'facsimile in the GAMS (Graz) digital edition (checked {DATE})'
    if any('archivinformationssystem.at' in h for h in links) or 'hungaricana.hu' in ' '.join(links):
        return 'archive', f'HHStA: AIS record has no digitised images; reading room or scan order (checked {DATE})'
    nara = [re.search(r'/id/(\d+)', h).group(1) for h in links if 'catalog.archives.gov/id/' in h]
    if nara:
        n = [f'naId {i}: {NARA_DIGITISED[i]} images' for i in nara if i in NARA_DIGITISED]
        if n:
            return 'online', f'NARA catalogue file digitised ({"; ".join(n)}) (checked {DATE})'
    if e['id'] in BODLEIAN:
        return 'archive', f'{BODLEIAN[e["id"]]}; reproduction order (checked {DATE})'
    if shelf.startswith('Bodleian Library, Clarendon State Papers'):
        return 'archive', f'{CLARENDON} (checked {DATE})'
    if re.match(r'TNA,? (?:State Papers (?:Ireland|Scotland)|SP 29)', shelf):
        return 'archive', f'{TNA_SP} (checked {DATE})'
    return None


GROUPS = ['Archives nationales', 'HHStA Wien', 'AGS', 'NARA RG 59', 'Academia Sinica IMH Archives', 'Bodleian Library',
          'TNA', "Archives nationales d'outre-mer", 'Biblioteca Nacional de Portugal', 'Houghton Library', 'Riksarkivet',
          'Real Academia de la Historia', 'TNA SP 29', 'Massachusetts Historical Society', 'AGAD Warszawa']


def main(write):
    files = [('catalogue.json', 'entries'), (os.path.join('research', 'leads.json'), 'leads')]
    left = []
    for rel, key in files:
        path = os.path.join(ROOT, rel)
        data = json.load(open(path, encoding='utf-8'))
        n = {'archive': 0, 'online': 0}
        for e in data[key]:
            if e.get('access'):
                continue
            g = re.split(r'[,(;:]', e.get('shelfmark') or '')[0].strip()[:60]
            if g not in GROUPS:
                continue
            d = decide(e)
            if d is None:
                left.append((rel, g, e))
                continue
            e['access'], e['access_note'] = d
            n[d[0]] += 1
        print(rel, n)
        if write:
            with open(path, 'w', encoding='utf-8') as fh:
                json.dump(data, fh, ensure_ascii=False, indent=1)
                fh.write('\n')
    print('left in these groups:', len(left))
    for rel, g, e in sorted(left, key=lambda x: (x[1], x[2]['id'])):
        print(f"  {g:32} {e['id']:5} {rel.split(os.sep)[-1]:15} {e['title'][:70]}")


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main('--write' in sys.argv)
