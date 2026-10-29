"""candidates_draft.json (build_candidates.py) + hand-checked rows -> candidates.json."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(D, 'candidates_draft.json'), encoding='utf-8'))
for r in rows:
    for k in [k for k in r if k.startswith('_')]:
        del r[k]
    if 'Commonwealth' in r['shelfmark'] or 'Clarendon' in r['shelfmark']:
        r['status'] += (' Royalist cipher traffic (Nicholas/Hyde/Ross/Pile); research/ia_meta/candidates.json has an aggregate row for the 1655-56 Commonwealth letters, '
                        'so on merge this item-level row should replace or sit under that aggregate, not duplicate it.')
        r['prior_art'] = ('open (checked 28 Oct 2026: calendar text only; Hyde-Barwick key is a different system, see targets/hyde/NOTES.md; '
                          'Bodleian Clarendon MSS / Nicholas Papers not searched for a key)')

for r in rows:
    if 'Burlamachi' in r['title']:
        r['correspondents'] = 'Philip Burlamachi to [Sir Edward Conway?] (cipher note may belong to the neighbouring entry 59 or 60; check)'
        r['title'] = 'Burlamachi / Woodford group, 12 July 1620: letter partly in cipher, calendared as undeciphered (CSP Domestic James I 1619-23, p. 171)'
        r['verify'] = 'Check which of entries 58-60 carries the cipher note (OCR window ambiguous), then the TNA SP 14 original.'
    if 'armada on the coast of Ireland' in r['folio_note']:
        r['year'] = 1574; r['date'] = '14 Jun 1574'
        r['title'] = 'Declaration of Irish loyalty to the Catholic cause, with the Spanish armada on the Irish coast; "a considerable portion not deciphered" (CSP Foreign Elizabeth 1572-74)'
        r['correspondents'] = 'Irish lords (?) -> Philip II (?) ; London copy'
        r['why'] = 'An Irish-Spanish approach of 1574 whose ciphered portion the editor could not read.'; r['importance'] = 4
    if 'Melun' in r['folio_note']:
        r['year'] = 1560; r['date'] = '9 Aug 1560 (Melun)'; r['correspondents'] = 'unknown (letter signed, from Melun) -> unknown'
        r['title'] = 'Letter from Melun with a few words in cipher, undeciphered (CSP Foreign Elizabeth 1560-61, Scotland/France, 9 Aug 1560)'
manual = [
 dict(year=1594, date='28 Feb 1594', title='Anonymous cipher letter on the coronation of Henri IV, "Undeciphered", HMC Salisbury (Cecil) MSS Part IV',
      correspondents='unknown -> Sir Robert Cecil (probably; addressee not checked)', place='unknown', language='French (one clear sentence; rest cipher)', region='England',
      period='1589-1598',
      shelfmark='Historical Manuscripts Commission, Calendar of the MSS of the Marquis of Salisbury at Hatfield House, Part IV (1892), CIPHER LETTER 1594 Feb. 28, printed p. 484-485 (index: "Cipher letters undeciphered; 484, 55?"); Hatfield House, Cecil Papers',
      folio_note='1 p. in cipher; only the sentence "Le Roi fut sacre hier ... il a pris l\'ordre du Saint Esprit" is in clear. Calendar note reads "Undeciphered. 1 p."',
      cls='C', status='HMC calendar (Part IV, 1892) says undeciphered. Found in the archive.org/BSB copy 11576077bsb text. Cecil Papers are on Hatfield House microfilm/CP online (Cecil Papers). Not checked whether the Cecil Papers hold a decipher.',
      why='A Henri IV coronation-day (27 Feb 1594, Chartres) report to Cecil in an unread cipher; might pair with Bruce/Moody/Standen cipher sets of 1594.',
      importance=3, solvability=2, difficulty=4,
      score_note='Scored from the printed calendar text during the Oct 2026 HathiTrust sweep (research/hathitrust/); not viewed',
      verify='Open the Part IV volume at p. 484-485 (HathiTrust or archive.org 11576077bsb); then the Cecil Papers entry (CP 25/?) via the Hatfield microfilm / British Online Archives for the image; compare with Part IV index "Cipher letters undeciphered" second reference.',
      links=[dict(label='BSB/archive.org scan of HMC Salisbury Part IV (1892)', href='https://archive.org/details/11576077bsb'),
             dict(label='HathiTrust catalogue search (volume id not resolved: Cloudflare block)', href='https://catalog.hathitrust.org/Search/Home?lookfor=Calendar+of+the+manuscripts+of+the+Marquis+of+Salisbury+Part+IV&type=title')],
      seen='catalogue', source='HathiTrust sweep',
      prior_art='open (checked 28 Oct 2026: printed calendar text of Part IV only; no web search for this item)'),
 dict(year=1595, date='12 Jun 1595 (Brussels)', title='Letter from Brussels with last paragraph in cipher, "undeciphered" (CSP Domestic Elizabeth 1595-97, p. 56)',
      correspondents='unknown (Catholic exile in Brussels) -> unknown', place='Brussels', language='English', region='England', period='1589-1598',
      shelfmark='CSP Domestic Elizabeth 1595-97 (Green, 1869), p. 56 (entry just before no. 67 John Du Port); archive.org cu31924091775282 / calendarofdome04greauoft; TNA SP 12',
      folio_note='1.5 pp.; last paragraph in cipher',
      cls='C', status='Calendar says "the last paragraph in cipher, undeciphered". The Spanish/boors and Cardinal of Austria news fixes the date June 1595.',
      why='Intelligence from the Spanish Netherlands on the Cardinal Archduke Albert\'s arrival, ciphered tail unread.',
      importance=2, solvability=1, difficulty=4,
      score_note='Scored from the printed calendar text during the Oct 2026 HathiTrust sweep (research/hathitrust/); not viewed',
      verify='Read the entry at p. 56 to get sender/recipient and the TNA SP 12 piece; check Tomokiyo for the sender\'s cipher.',
      links=[dict(label='archive.org copy of the calendar volume', href='https://archive.org/details/cu31924091775282'),
             dict(label='HathiTrust catalogue search (volume id not resolved: Cloudflare block)', href='https://catalog.hathitrust.org/Search/Home?lookfor=Calendar+of+state+papers+domestic+Elizabeth+1595-1597&type=title')],
      seen='catalogue', source='HathiTrust sweep',
      prior_art='open (checked 28 Oct 2026: calendar text only)'),
]
rows += manual
json.dump(rows, open(os.path.join(D, 'candidates.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(rows))
