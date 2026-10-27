"""Rebuild the documents, texts and outcome of profile.json from the sample files (27 Oct 2026). Run from the target folder."""
import json, re

p = 'profile.json'
d = json.load(open(p, encoding='utf8'))
base = dict(year=1791, country="Poland-Lithuania", route="St Petersburg -> Warsaw", language="Polish",
            cleartext_in_document="separate passages", places={"from": "St Petersburg", "to": "Warsaw"})


def tr(notes):
    return {"by": "llm from images", "source": "AGAD agadd2 image server, full-size slides", "image_quality": "good", "notes": notes}


meas = {'001': (2202, 671), '002': (724, 324), '003': (214, 138), '032': (732, 329), '037': (567, 283), '039': (417, 257), '045': (642, 329)}
info = {
    '001': ("4 Jan 1791", "k. 2-5v (img 0002-0007)", 7, "ZbPop 421 item 088 (k. 297, 301) is the clear text of this date; short for 2,202 groups, not checked.", "not read"),
    '002': ("7 Jan 1791", "k. 6-7 (img 0008-0009)", 3, "Cabinet decipherment, ZbPop 421 item 090, k. 302-303 (img 0380-0381), 'reçu le 19.'; aligned group by group (align/002.tsv).", "read"),
    '003': ("11 Jan 1791", "k. 8-13 (img 0010-0017)", 11, "ZbPop 421 item 091 (7 images), not transcribed.", "not read"),
    '032': ("22 Apr 1791", "k. 111-112 (img 0158-0159)", 3, "Cabinet decipherment, ZbPop 421 k. 30-31 (img 0040-0041), 'reçu le 4. Mai'; aligned (align/032.tsv).", "read"),
    '037': ("6 May 1791", "k. 126 (img 0178-0179)", 2, "Cabinet decipherment, ZbPop 421 k. 48 (img 0060-0061), 'reçu le 17.'; aligned (align/037.tsv).", "read"),
    '039': ("13 May 1791", "k. 129 (img 0182-0183)", 2, "Cabinet decipherment, ZbPop 421 k. 52 (img 0065-0066), 'reçu le 24.'; aligned (align/039.tsv).", "read"),
    '045': ("31 May 1791", "k. 147 (img 0206-0207)", 2, "Cabinet decipherment, ZbPop 421 k. 77-78 (img 0098-0099), 'reçu ce 11. Juin'; aligned (align/045.tsv).", "read"),
}
tnotes = {
    '001': "Not cross-checked against a decipherment.",
    '003': "First page only (img 0010).",
    '002': "One cipher line (0009 right L09) dropped in the first pass, restored when the alignment showed clear text with no groups against it.",
    '032': "The closed q-like 4: '1990' is 1490 (by), settled by the decipherment.",
    '037': "Code B throughout; opens 3381z 3285.",
    '039': "First paragraph code B (indicator 3283), second paragraph code A in a smaller hand (indicator 4000).",
    '045': "Code A, then '4000 1775 3285 1269' and code B for the last paragraph; cursive page where 8 and 0 are hard to separate.",
}
docs = []
for k in ['002', '032', '037', '039', '045']:
    dt, sh, pg, src, rd = info[k]
    t, dd = meas[k]
    docs.append(dict(id=f"ZbPop5-{k}", shelfmark=f"AGAD Warszawa, Zbiór Popielów 5, {sh}", date=dt, **base, pages=pg,
                     plaintext={"location": ["separate collection"], "source": src},
                     length={"tokens": t, "distinct": dd, "unit": "code groups", "measured": True, "file": f"transcription/groups_{k}.txt"},
                     transcription=tr(tnotes[k]), read=rd))
d['documents'] = docs
d['title'] = ("Deboli (St Petersburg) to King Stanisław August, cipher despatches of 1791 "
              "(AGAD Zbiór Popielów 5; decipherments in Zbiór Popielów 421; catalogue 420)")
s = d['system']
s['summary'] = ("Two Polish syllabic codes of about 2,200 numbered groups and above (code A from January 1791, code B the "
                "code of Deboli's 1792 Danzig letters), switched inside a despatch by indicator groups above 3,000, "
                "with a clear French salutation and closing.")
s['nomenclator'] = {"present": True, "kinds": ["syllables", "common words", "titles", "names"]}
s['nulls'] = {"present": True}
s['word_division'] = "none"
s['sibling_key'] = "the 1792 Danzig letters (ZbPop 415) use code B"
c = d['conditions']
c['inputs'] = ["images", "known plaintext"]
c['sessions'] = 2
c['last_date'] = "2026-10-27"
c['tools'] = ["AGAD online inventories", "AGAD agadd2 image server", "web search", "PIL crops", "image-reading subagents",
              "group-by-group alignment (subagents)", "scripts/consistency.py"]
done = {x['what'][:40] for x in d['solution']}
for st in [
    {"date": "2026-10-27", "kind": "verification", "technique": ["plaintext matching"],
     "what": "Pairing checked for 1788-1792 (pairings_1788-1792.txt) and one pair per year compared: 1792 confirmed (951 ... 1578 = Odpisuiąc na list WKrMości), 1790 likely (Deputacyi twice), 1789 same code family, 1788 a different code.", "result": "worked"},
    {"date": "2026-10-27", "kind": "transcription",
     "what": "Transcribed despatches 032, 037, 039, 045 (cipher and ZbPop 421 decipherment); a dropped cipher line of 002 (0009R L09) found and restored.", "result": "worked"},
    {"date": "2026-10-27", "kind": "reading", "technique": ["plaintext matching", "repeat/pattern analysis", "manual reconstruction"],
     "what": "Aligned the five sample despatches group by group with their decipherments: 3,048 of 3,082 groups given a value (98.9%); two codes found, code B being the 1792 Danzig code, switched by indicator groups 3283/3285/4000.", "result": "worked"},
    {"date": "2026-10-27", "kind": "verification", "technique": ["statistical test"],
     "what": "Value consistency of repeated groups across the sample: 83.3% (code A, 1,757 occurrences) and 84.4% (code B, 762) carry their commonest value; the rest are mostly syllable-split guesses.", "result": "worked"},
]:
    if st['what'][:40] not in done:
        d['solution'].append(st)


def read_share(f):
    txt = open('transcription/' + f, encoding='utf8').read()
    body = ' '.join(l for l in txt.split('\n') if l and not l.startswith('#') and not l.startswith('{'))
    w = re.sub(r'\{[^}]*\}', '', body).split()
    return round(1 - sum('[?]' in x for x in w) / len(w), 3)


labels = {'002': "Despatch 002, 7 Jan 1791", '032': "Despatch 032 (Nr 10), 22 Apr 1791", '037': "Despatch 037 (Nr 15), 6 May 1791",
          '039': "Despatch 039 (Nr 17), 13 May 1791", '045': "Despatch 045 (Nr 23), 31 May 1791"}
clear = {'002': 'zbpop421_090_clear_1791-01-07.txt', '032': 'zbpop421_032_clear.txt', '037': 'zbpop421_037_clear.txt',
         '039': 'zbpop421_039_clear.txt', '045': 'zbpop421_045_clear.txt'}
cip = {'002': 'zbpop5_001-003.txt', '032': 'zbpop5_032.txt', '037': 'zbpop5_037.txt', '039': 'zbpop5_039.txt', '045': 'zbpop5_045.txt'}
summ = {
    '002': "Deboli comments on the Sejm's quarrel over the new oath, which Petersburg laughs at; England and Prussia still wait for an answer on the status quo, Alopeus has said in Berlin that the Empress is ready for extremities but will take no dictation, and Potemkin is thought to be dragging things out; couriers from Golitsyn and Vorontsov; Count Starhemberg's journey and complaint about the Połąga customs.",
    '032': "Deboli has sent his despatch to the Deputation under the banker Schultz's cover and confesses his office has become hateful to him amid the endless quarrels at home; war preparations in England, the perplexity of Goltz and Whitworth, and a Spanish declaration in Berlin advising against war, with Spain said to promise a diversion in Russia's favour if England joins the Turkish war.",
    '037': "No Berlin courier yet; England and Prussia are thought to want their fleet at sea before proposing an ultimatum; the Spanish envoy Gálvez argues Russia should be handled gently, which Deboli finds hard to square with Russia's aims on Ochakov and the Black Sea; Nassau flatters Gálvez and the Empress sends him a sable fur; a new Dutch envoy.",
    '039': "Ten days after the Constitution of 3 May 1791: it was just the time for what the King did; raise the army to 100,000; Petersburg credits Marshal Potocki; the second half of the despatch to the Deputation is enciphered in the Deputation's cipher; court gossip on the Saxon marriage plans, Goltz's supposed part, and fear of Potemkin's designs.",
    '045': "Deboli begins corresponding with Vice-Chancellor Chreptowicz; Petersburg thinks the Revolution well founded but reports displeasure in Berlin, and Goltz has cooled towards him; Dresden's hesitation and Helbig's instructions on the Elector's answer; Potemkin promises Fawkener a favourable answer before the Empress has seen the note.",
}
texts = []
for k in ['002', '032', '037', '039', '045']:
    texts.append({"doc": f"ZbPop5-{k}", "label": labels[k] + " (cipher ZbPop 5; decipherment ZbPop 421)", "summary": summ[k],
                  "state": "read", "language": "pl",
                  "transcription": f"transcription/{cip[k]}", "contemporary": f"transcription/{clear[k]}",
                  "decryption": f"transcription/{clear[k]}", "translation": f"texts/{k}_en.md",
                  "reading_review": {"grade": "A", "by": "Claude Opus 5.5", "date": "2026-10-27",
                                     "note": "The contemporary decipherment, transcribed from ZbPop 421 and aligned group by group with the cipher (align/" + k + ".tsv); reads as coherent Polish, translated into English; uncertain words marked [?]."},
                  "read_share": read_share(clear[k])})
o = d['outcome']
o.update({
    "method": "read from existing decipherment",
    "method_basis": "The cabinet's contemporary fair-copy decipherments survive as AGAD Zbiór Popielów 421 (catalogued as Deboli's clear letters); five despatches were transcribed and aligned with them group by group (98.9% of 3,082 groups).",
    "contribution": ["transcription", "catalogue correction"],
    "class": "already solved", "key": "partial",
    "verification": ["contemporary decipherment"],
    "codes_open": {"open": 34, "total": "unknown", "tokens_open": 34},
    "key_file": "align/code_table_039_045.tsv",
    "notes": "Sample of 5 of 105 despatches; the other decipherments exist in ZbPop 421 and are not transcribed here. Two codes in use. The pairing extends to catalogue 417-421 (1792 confirmed; 1789-1790 same code; 1788 a different code).",
    "texts": texts,
    "gaps": [
        {"item": "Despatches 004-105 other than 032, 037, 039, 045 (98 items)", "blocker": "not-attempted",
         "detail": "decipherments exist in ZbPop 421 and the pairing is established; cipher and decipherment not transcribed in this session"},
        {"item": "Despatches 001 and 003 (cipher transcribed in full / first page only)", "blocker": "not-attempted",
         "detail": "ZbPop 421 item 088 for 4 Jan looks short for 2,202 groups; 003's decipherment (item 091) not transcribed"},
        {"item": "Despatches 014 (18 Feb) and 019 (8 Mar)", "blocker": "not-attempted",
         "detail": "no ZbPop 421 partner by date or number; undated items 003 and 039 of ZbPop 421 not checked"},
        {"item": "34 groups of the sample with no place in the decipherment", "blocker": "open-codes",
         "detail": "marked ? in align/; mostly single groups where cipher and decipherment differ"},
    ],
    "credits": [{"who": "contemporary", "role": "key or decipherment used",
                 "note": "the royal cabinet's fair-copy decipherments, AGAD Zbiór Popielów 421 (catalogued as Deboli's clear letters)"}],
})
o['fraction_read'] = "unknown"   # of the 105 despatches; the five checked give 3,048 of 3,082 groups (0.989)
o['fraction_read_method'] = "measured"
o['parts'] = [{"label": "1791 cipher despatches: 5 of 105 transcribed and aligned with the contemporary decipherment (3,048 of 3,082 groups)",
               "method": "read from existing decipherment", "extent": "partial"}]
o['fraction_read_source'] = ("27 Oct 2026: cipher groups of the five aligned despatches (002, 032, 037, 039, 045) that take a value from the "
                             "contemporary decipherment, counted in align/*.tsv: 3,044 values + 4 indicators of 3,082 groups (groups_NNN.txt, "
                             "measured with docs/_check_profile.py --measure). Despatches 001 (2,202 groups) and 003 (first page, 214) are "
                             "transcribed but not checked against a decipherment and are left out of the documents; the other 100 despatches "
                             "are listed as a gap.")
with open(p, 'w', encoding='utf8') as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(o['fraction_read'], [t['read_share'] for t in texts])
