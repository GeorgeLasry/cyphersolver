"""b16 (wotton1585): targeted edits of profile.json after the 22 Oct 2026 re-read (layout kept: each changed one-line
object is re-serialised on its own line, everything else untouched; the result must parse)."""
import json, pathlib, re
P = pathlib.Path(__file__).resolve().parent.parent.parent / 'targets' / 'wotton1585' / 'profile.json'
s = P.read_text(encoding='utf-8')
d0 = json.loads(s)


def D(o):
    return json.dumps(o, ensure_ascii=False)


TOK = {'R4841': (883, 29), 'R4842': (1088, 41), 'R4843': (895, 33)}
REV = {
 'R4841': ('A', "Wotton's own clear draft transcribed in full from the four DECODE images (texts/R4841_transcription.txt, struck words and interlineations marked) and read in its last state; b16_wotton_align.py: of 594 reading words/codes 581 are carried by the transcription in order or as interlineations, the other 13 are modernised spellings of words in it (towarde, continew, hable ...); supplied words bracketed. Holes: one illegible word ('with a [..] heart'); 'premoveable'/'stick' doubtful. Code 3 glossed the Queen of England from the drafts (sense, flagged)."),
 'R4842': ('B', "Wotton's own clear draft transcribed in full from the four DECODE images (texts/R4842_transcription.txt) and read in its last state; 726 of 749 reading words/codes carried by the transcription, the other 23 modernised spellings. The heavily revised passage on embarking the Scots (p2.05-p2.09) and two short interlineations are partly illegible and left [..]; codes 27 and 11 open; 'Jamington' doubtful."),
 'R4843': ('B', "Wotton's own clear draft transcribed in full from the four DECODE images (texts/R4843_transcription.txt) and read in its last state; 642 of 663 reading words/codes carried, the other 21 modernised spellings or the expanded abbreviation Arb: (Arbroath). The commissioners passage (p2.10-p2.17) is heavily revised and read only in its legible last state; initials L. B., L. H., S. J. H., S. not expanded; codes 27, 32, 36 open."),
}
for t in d0['outcome']['texts']:
    doc = t['doc']
    old = D(t)
    assert old in s, doc
    n = {k: v for k, v in t.items() if k != 'note'}
    n['transcription'] = f'texts/{doc}_transcription.txt'
    n['state'] = 'read'
    n['reading'] = f'texts/{doc}_reading.md'
    n['translation'] = f'texts/{doc}_en.md'
    g, note = REV[doc]
    n['reading_review'] = {'grade': g, 'by': 'Claude Opus 5.5', 'date': '2026-10-22', 'note': note}
    s = s.replace(old, D(n))
for dd in d0['documents']:
    doc = dd['id']
    for k, new in (('length', {'tokens': TOK[doc][0], 'unit': 'words', 'measured': True, 'file': f'texts/{doc}_transcription.txt'}),
                   ('transcription', {'by': 'llm from images', 'source': 'Authenticated DECODE scans (main checkout decode/%s_p1-p4.jpg, about 4800x6837).' % doc,
                                      'corrections': 0, 'image_quality': 'good',
                                      'notes': 'Full diplomatic transcription made 22 Oct 2026 (batch b16) in strips and zooms at native resolution: texts/%s_transcription.txt. Measured with --drop-first (struck words included); %d tokens carry a digit (name codes, dates, folio numbers).' % (doc, TOK[doc][1])})):
        old = D(dd[k])
        assert old in s, (doc, k)
        s = s.replace(old, D(new), 1)
steps = [
 {"date": "2026-10-22", "kind": "access", "what": "Re-fetched DECODE records R4841-R4843 with the project cookie (research/reading_audit/b16_wotton_fetch.py): each still holds only its four page images, no transcription, decryption, key or attachment.", "result": "worked"},
 {"date": "2026-10-22", "kind": "literature search", "what": "Tried CSP Scotland viii (1914) again for a text to align with: HathiTrust ssd view behind a Cloudflare check, archive.org calendarofstatep0008vari download refused (401, lending-only), the other archive.org Boyd items are earlier volumes. Nothing printed was aligned; the drafts are the primary text.", "result": "failed"},
 {"date": "2026-10-22", "kind": "transcription", "what": "Transcribed the three drafts in full from the twelve full-resolution images, in strips and zooms (texts/R4841-R4843_transcription.txt), marking struck words, interlineations and doubtful readings; Wotton's working notes at the head of f. 167r included.", "result": "worked"},
 {"date": "2026-10-22", "kind": "reading", "technique": ["contextual inference"], "what": "Built a reading of each draft in its last state with the name code glossed in place (texts/R484x_reading.md) and a modern-English rendering (R484x_en.md); aligned word by word with the transcription (b16_wotton_align.py): every reading word is carried or is a modernised spelling; supplied words bracketed.", "result": "worked"},
 {"date": "2026-10-22", "kind": "hypothesis", "technique": ["contextual inference"], "what": "Code 3 = the Queen of England, not France: 'divert 10 from 3 ... or if the King constantly in affection towards 3, convey him into France' (R4841) and 'it can no way stand with 3 honor that I should be at that time in this country' (R4843). Sense only, four occurrences, flagged for review in texts/key.md; 9 = England ('the 9 friendship') likewise sense only.", "result": "partial"},
 {"date": "2026-10-22", "kind": "verification", "technique": ["language-model scoring"], "what": "Scored the reading bodies with _check_reading.py (header cut): R4841 0.98 (51/52 sentences), R4842 0.89 (58/65), R4843 0.91 (53/58). All three relabelled read; class not read -> read; method -> key recovered based on adjacent plaintext (the name code identified from the clear text, as before the audit); fraction_read 0 -> 1.0.", "result": "worked"},
]
m = re.search(r'(\{"date": "2026-10-22", "kind": "verification", "what": "Reading audit, per-document pass[^\n]*\})\n', s)
assert m
s = s[:m.end(1)] + ''.join(',\n  ' + D(x) for x in steps) + s[m.end(1):]
rep = [
 ('"method": "not solved"', '"method": "key recovered based on adjacent plaintext"'),
 (D(d0['outcome']['method_basis']), D("The three drafts are in clear English with a small numeric name code; the code numbers were identified from the clear text (19 Arran, 39 Master of Gray, 10 King James, 3 the Queen, 20 Maxwell) and checked where possible against CSP Scotland viii's glosses (found after the reading). The drafts were transcribed in full and read on 22 Oct 2026 (batch b16); 27, 32, 36 and 11 stay open.")),
 ('"class": "not read"', '"class": "read"'),
 (D(d0['outcome']['notes']), D(d0['outcome']['notes'] + " 22 Oct 2026, re-read (b16): the three drafts transcribed in full from the DECODE images and read (clean-sentence share 0.98, 0.89, 0.91); class -> read, method -> key recovered based on adjacent plaintext. Open: codes 27, 32, 36, 11 (no key material; CSP viii not reachable), a few illegible interlineations.")),
 ('"last_date": "2026-09-21"', '"last_date": "2026-10-22"'),
 ('"sessions": 1', '"sessions": 2'),
]
for a, b in rep:
    assert a in s, a[:60]
    s = s.replace(a, b, 1)
i = s.index('"gaps": [')
j = s.index('\n  ]', i)
gaps_new = '"gaps": [\n' + ',\n'.join('   ' + D(g) for g in [
 {"item": "Codes 27, 32, 36 and 11 unidentified", "blocker": "no-key-material", "detail": "No key on DECODE or in Tomokiyo; CSP Scotland viii, which glosses 19, 24, 39, 40, could not be reached on 22 Oct 2026 (HathiTrust Cloudflare check, archive.org lending-only). 27: favourer of the Hamiltons, Gray's colleague; 32: a place the King might flee to; 36: source of money for Gray's hundred men; 11: 'the 11 course'."},
 {"item": "A few interlineations and struck-over phrases in R4842 p2.05-p2.09 and R4843 p2.10-p2.17", "blocker": "illegible", "detail": "Read at native resolution in zooms; the last state of the revision cannot be fixed with confidence; left [..] in the readings."}])
s = s[:i] + gaps_new + s[j:]
json.loads(s)
P.write_text(s, encoding='utf-8')
print('ok')
