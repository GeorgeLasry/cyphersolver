"""Turn raw_hits.json (extract.py) into candidates.json in the archive-sweep format. Run after extract.py."""
import json, re, os, difflib, sys
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
raw = json.load(open(os.path.join(D, 'raw_hits.json'), encoding='utf-8'))

# archive.org id -> (calendar label, year, region, language, place hint, period)
SER = {
 'cu31924091770432': ('CSP Domestic, Commonwealth, 1655-56', 1656, 'England', 'English', 'Paris/Cologne (royalist correspondence)', '1651-1700'),
 'cu31924091770440': ('CSP Domestic, Commonwealth, 1656-57', 1656, 'England', 'English', 'unknown', '1651-1700'),
 'cu31924091770473': ('CSP Domestic, Commonwealth, 1659-60', 1659, 'England', 'French', 'unknown', '1651-1700'),
 'cu31924091770424': ('CSP Domestic, Commonwealth, 1655', 1655, 'England', 'English', 'unknown', '1651-1700'),
 'abd6186.0008.001.umich.edu': ('CSP Domestic, Commonwealth, 1655', 1655, 'England', 'English', 'unknown', '1651-1700'),
 'calendarofstatep0000mary': ('CSP Domestic, Commonwealth, 1659-60', 1659, 'England', 'French', 'unknown', '1651-1700'),
 'cu31924091775274': ('CSP Domestic, Edward VI-James I, Addenda/Eliz. 1591-94', 1593, 'England', 'English', 'unknown', '1589-1598'),
 'cu31924091775373': ('CSP Domestic, Elizabeth, 1588-91', 1590, 'England', 'English', 'unknown', '1589-1598'),
 'cu31924091775282': ('CSP Domestic, Elizabeth, 1595-97', 1595, 'England', 'English', 'unknown', '1589-1598'),
 'statepapersmary07greauoft': ('CSP Domestic, Elizabeth Addenda 1566-79', 1572, 'England', 'English', 'unknown', '1560-1589'),
 'calendarofstatep0000mary_h2k1': ('CSP Domestic, James I, 1603-10', 1603, 'England', 'English', 'unknown', '1598-1610'),
 'calendarofstatep0000mary_l0t0': ('CSP Domestic, James I, 1619-23', 1620, 'England', 'English', 'unknown', '1611-1650'),
 'calendarofstatep00lond': ('CSP Foreign, Edward VI, 1547-53', 1551, 'England', 'English', 'unknown', '1497-1559'),
 'calendarstatepa00igoog': ('CSP Foreign, Mary, 1553-58', 1555, 'England', 'English', 'unknown', '1497-1559'),
 'calendarofstatep00grea_0': ('CSP Foreign, Elizabeth, 1569-71', 1570, 'England', 'English', 'unknown', '1560-1589'),
 'calendarofstatep0000vari_o6f2': ('CSP Foreign, Elizabeth, 1572-74', 1572, 'England', 'English', 'unknown', '1560-1589'),
 '10278871bsb': ('CSP Foreign, Elizabeth, 1560-61', 1560, 'England', 'English', 'unknown', '1560-1589'),
 'calendarofclaren03bodluoft': ('Calendar of the Clarendon State Papers (Bodleian), vol. 3', 1656, 'England', 'English', 'unknown', '1651-1700'),
 'calendarofstatep0000mary_o4k2': ('CSP Domestic, Commonwealth, 1655-56', 1656, 'England', 'English', 'unknown', '1651-1700'),
 'calendarofstatep0000mary_w3y6': ('CSP Domestic, Commonwealth, 1659-60', 1659, 'England', 'French', 'unknown', '1651-1700'),
 '11576093bsb': ('CSP Domestic, Commonwealth, 1659-60', 1659, 'England', 'French', 'unknown', '1651-1700'),
 '11576088bsb': ('CSP Domestic, Commonwealth, 1655', 1655, 'England', 'English', 'unknown', '1651-1700'),
 'calendarofstatep0000mary_k8k8': ('CSP Domestic, Commonwealth, 1657-58', 1657, 'England', 'English', 'unknown', '1651-1700'),
 'calendarofstatep0000mary_c3j1': ('CSP Domestic, Commonwealth, 1655', 1655, 'England', 'English', 'unknown', '1651-1700'),
 'abd6186.0009.001.umich.edu': ('CSP Domestic, Commonwealth (vol. abd6186.0009)', None, 'England', 'English', 'unknown', '1651-1700'),
 'calendarofstatep12grea': ('CSP Domestic, Commonwealth (vol. calendarofstatep12grea)', None, 'England', 'English', 'unknown', '1651-1700'),
 'cu31924091770465': ('CSP Domestic, Commonwealth (vol. cu31924091770465)', None, 'England', 'English', 'unknown', '1651-1700'),
 'cu31924091770457': ('CSP Domestic, Commonwealth (vol. cu31924091770457)', None, 'England', 'English', 'unknown', '1651-1700'),
 'calendarofstatep09grea_0': ('CSP Foreign, Elizabeth (vol. calendarofstatep09grea_0)', None, 'England', 'English', 'unknown', '1560-1589'),
 'calendarofstatep10grea': ('CSP Foreign, Elizabeth (vol. calendarofstatep10grea)', None, 'England', 'English', 'unknown', '1560-1589'),
 'calendarofmanusc04grea': ('HMC Salisbury (Cecil) MSS, Part IV (1590-94)', 1594, 'England', 'unknown', 'unknown', '1589-1598'),
 '11576077bsb': ('HMC Salisbury (Cecil) MSS, Part IV (1590-94)', 1594, 'England', 'unknown', 'unknown', '1589-1598'),
 'calendarofstatep0000vari_q2n4': ('CSP Foreign, Edward VI, 1547-53', 1551, 'England', 'English', 'unknown', '1497-1559'),
}
HATHI_SEARCH = 'https://catalog.hathitrust.org/Search/Home?lookfor={}&type=title'

rows, seen = [], []
for x in raw:
    if x['vol'] not in SER or x['span'] >= 2000: continue
    if re.match(r'\s*\d+\. Ciphers?', x['note']): continue
    cal, yr, region, lang, place, period = SER[x['vol']]
    if 'Edward VI' in cal or 'James I, 1603' in cal or 'Part IV' in cal or 'Elizabeth, 1569-71' in cal or 'Clarendon' in cal and False: continue
    if cal.startswith('CSP Foreign, Elizabeth, 1560') and 'small portion' in x['note']: continue
    if 'Addenda 1566-79' in cal and x['entry'] != '59': continue
    if 'Edward VI-James I, Addenda/Eliz. 1591-94' in cal and 'Baxter' not in x['note'] and 'Hunt' not in x['note'] and 'Bristowe' not in x['note'] and 'Phelippes' not in x['note']: continue
    if yr is None:
        ys = [int(v) for v in x['years'] if v.isdigit()]
        yr = ys[-1] if ys else 0
    head = x['note'][:200]
    tail = x['note'][-150:]
    sig = re.sub(r'[^a-z]', '', (x['note'][:120] + x['note'][-80:]).lower())
    if any(difflib.SequenceMatcher(None, sig, s).ratio() > 0.8 for s, c in seen): continue
    seen.append((sig, cal))
    m = re.match(r'\s*\d+\.\s+(.{3,70}?\bto\b.{2,50}?)[.,]\s', x['note'])
    corr = m.group(1).strip() if m else 'unknown'
    if re.match(r'(A |Has |Do not |Pres\. )', corr): corr = 'unknown'
    cn = re.search(r'\[[^\]]*(?:cypher|cipher|decyph|deciph)[^\]]*\]?', tail, re.I)
    note = cn.group(0)[:160] if cn else tail[-110:]
    date = re.sub(r'\s+', ' ', x['date']) if x['date'] else 'undated in OCR'
    rows.append(dict(
        year=yr, date=f"{date} (calendar of {cal})" if x['date'] else f"{yr} (date not captured)",
        title=f"{corr}: letter partly in cipher, calendared as undeciphered ({cal})",
        correspondents=corr if corr != 'unknown' else 'unknown',
        place=place, language=lang, region=region, period=period,
        shelfmark=f"{cal}, entry {x['entry'] or '(no. not captured)'}, printed p. {x['page'] or '?'}; archive.org {x['vol']} (Hathi copy to be located); original in The National Archives SP / Bodleian",
        folio_note=f"Calendar note: {note}",
        cls='C', status=f"Printed calendar says cipher not deciphered ({note}). Not checked against the original or other editions; no DECODE check made (calendar entry, not a DECODE record).",
        why='Cipher text in a calendared state-papers letter that the editor could not read; may carry intelligence not otherwise printed.',
        importance=(3 if ('Elizabeth' in cal or 'Clarendon' in cal or 'Foreign' in cal) else 2), solvability=1, difficulty=4,
        score_note='Scored from the printed calendar text during the Oct 2026 HathiTrust sweep (research/hathitrust/); not viewed',
        verify='Open the volume on HathiTrust or archive.org, go to the entry, then the TNA original (SP series) to see whether the cipher is legible and whether a key or deciphering sibling exists.',
        links=[dict(label='archive.org copy of the calendar volume', href=f"https://archive.org/details/{x['vol']}"),
               dict(label='HathiTrust catalogue search (volume id not resolved: babel/catalog blocked by Cloudflare)', href=HATHI_SEARCH.format(cal.replace(' ', '+')))],
        seen='catalogue', source='HathiTrust sweep',
        prior_art='open (checked 28 Oct 2026: only the calendar text of this edition; no web search for individual item)',
        _raw_head=head, _raw_tail=tail, _vol=x['vol'], _leaf=x['leaf']))
json.dump(rows, open(os.path.join(D, 'candidates_draft.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(rows))
for i, r in enumerate(rows):
    print(i, r['year'], r['correspondents'][:50], '|', r['shelfmark'][:70], '|', r['folio_note'][:100])
