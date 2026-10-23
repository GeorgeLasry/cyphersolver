"""Re-read brief (REREAD_BRIEF.md), batch b18: caprile1520 (R1139, R1136).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b18_caprile.py <step>      step = texts | gaps | outcome | steps
Helpers: b18_caprile_fetch.py (DECODE record files to the scratchpad), b18_caprile_lines.py (line strips),
b18_caprile_beam.py (key21 decode with each token's value).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

T = 'caprile1520'

NOTE = {
    'R1139': "Re-read 22-23 Oct 2026 (b18): no decipherment, clear copy or print exists (DECODE record and neighbours R1135-R1140 opened, Somogyi 2025, Vestigia V1922). Read on the image at 2.2x, five labels corrected (R1139_corrections.tsv), key21 values only; partial reading R1139_reading.md with translation R1139_en.md: 'bel belo li go fato moto deli danari del suo debito, come mi dise meser [?a] Alfonso' and 'parlaremo a longo sopra ciò ...' read, but the body scores 0.18 clean (2/11; 0.45 on explicit holes). Open: the figures 4 8 1 7 and 1 7, the sign 4 and single signs p+ and q+ (no key material: every text in this key already used), L02 and L07-L08 stretches.",
    'R1136': "Re-read 22-23 Oct 2026 (b18): no decipherment, clear copy or print exists (DECODE record and neighbours, Somogyi 2025, Vestigia V1876). Read on contrast-stretched strips at 2x, pass-4 labels confirmed; partial reading R1136_reading.md with translation R1136_en.md ('a in gran presia [...] a Buda, et dicono eser conclusi', 'potrà far al custode par questa via de Ungaria'), but 0 of 9 sentences clean. Open: the stained left third of L01-L03 (illegible) and stretches turning on signs key21 cannot settle (QB/8, c/CE/e, AMP/EL, 4, 1 7), no further text in this key (no key material).",
}
FIELDS = {
    'R1139': {'transcription': ['caprile1521_transcription.txt', 'r1139_pass4.txt', 'R1139_transcription_b18.txt'],
              'decryption': ['pass3_r1136_r1139.md', 'beam21_r1139_pass4.txt', 'R1139_reading.md']},
    'R1136': {'decryption': ['pass3_r1136_r1139.md', 'beam21_r1136_pass5.txt', 'R1136_reading.md']},
}
GAPS = [
    {'item': "R1136 L01-L03 left third under the stain (about 6 signs) and R1139 L10 end",
     'blocker': 'illegible',
     'detail': "stain over the signs on the only image; re-checked on contrast-stretched strips 22-23 Oct 2026"},
    {'item': "R1139 figures '4 8 1 7' (L01) and '1 7' (L02; also R1136 L06)",
     'blocker': 'no-key-material',
     'detail': "tested as letters and as numerals (3 Oct 2026) and as 4 = e, 1 = v, 1 7 = ve (22-23 Oct 2026, R1139_reread_log.md): no value holds across every occurrence; no code list exists"},
    {'item': "R1139 unread stretches (L02 middle, L03 'a le ma [...] custode', L07 end to L08 start) and the single signs p+, q+ and the sign 4",
     'blocker': 'no-key-material',
     'detail': "signs legible and labelled on 2.2x strips (b18); their values are not in key21, and the five texts in this key (R1136, R1138, R1139, V1920, V1921) are all used; partial reading R1139_reading.md scores 0.18 clean"},
    {'item': "R1136 unread stretches (every sentence)",
     'blocker': 'no-key-material',
     'detail': "pass-4 labels confirmed on 2x contrast-stretched strips (b18); the breaks turn on signs key21 cannot separate or value (QB/8, c/CE/e, AMP/EL, 4, 1 7; pass 5 look-alike table and pass 6 pen shapes failed) and no further text in this key exists; partial reading R1136_reading.md scores 0.0 clean"},
    {'item': "V1921, 5 of 166 signs",
     'blocker': 'illegible',
     'detail': "K PHI at the torn page edge; two minims with no key value; one probable slip"},
]
STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b18): DECODE R1135-R1140 record pages and every linked file re-fetched with the shared cookie into the session scratchpad (b18_caprile_fetch.py): page images only, no attachment, transcription or comment; Somogyi 2025 searched again (she deciphers only R1138/V1920); MTA copies omit the cipher. No existing text of R1136 or R1139.", 'result': 'failed'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "R1139 cipher slip re-read on quarter-line strips at 2.2x of IMG_R1139_I5752_P2 (b18_caprile_lines.py): five labels corrected (p+ L03, q+ L04, EL for CE and D for B in L05, 'q+ PHI o 1 1' at the end of L07; R1139_corrections.tsv, R1139_transcription_b18.txt). R1136 re-read on contrast-stretched strips at 2x of IMG_R1136_I5740_P1: pass-4 labels confirmed, none changed.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'hypothesis', 'technique': ['key matching', 'contextual inference'], 'what': "Per-token key21 decode (b18_caprile_beam.py) and proposals tested across every occurrence: 4 = e (works in 'come' and before 'credo', fails in 'de 4 8 1 7' and R1136 L05/L10/L12), 1 = v ('in vero'; fails in '1 7'), 1 7 = ve (R1136 'cosi ve ne tenir'; fails in R1139 L01), CE = p ('in presto'; CE = o 72 times). None adopted.", 'result': 'failed'},
    {'date': '2026-10-22', 'kind': 'reading', 'technique': ['key matching', 'language-model scoring'], 'what': "Partial readings written word by word against the signs, with translations (R1139_reading.md/_en.md, R1136_reading.md/_en.md): new at key values 'bel belo li go fato moto' (o o = b, D = b), 'et se i bisionran danari in [?presto], per andar ve ne darò', 'a in gran presia [...] a Buda, et dicono eser conclusi', 'par questa via de Ungaria'. Clean-sentence share of the bodies: R1139 0.18 (2/11; 0.45 on explicit holes), R1136 0.0 (0/9). Both stay decoded, not read; blockers no-key-material and illegible.", 'result': 'failed'},
]


def texts():
    for d in ('R1139', 'R1136'):
        p = load(T)
        e = [x for x in p['outcome']['texts'] if x.get('doc') == d]
        assert len(e) == 1, d
        e = e[0]
        assert e.get('state') == 'decoded, not read'
        e['note'] = NOTE[d]
        e.update(FIELDS[d])
        save(T, p); print('note', d)


def gaps():
    p = load(T)
    p['outcome']['gaps'] = GAPS[:1]
    save(T, p)
    for g in GAPS[1:]:
        p = load(T); p['outcome']['gaps'].append(g); save(T, p)
    print('gaps')


def outcome():
    p = load(T)
    p['outcome']['notes'] = p['outcome']['notes'] + " 22-23 Oct 2026, re-read (b18): R1139 and R1136 re-read on the images with no existing text to follow; partial readings and translations written (R1139_reading.md, R1136_reading.md), below the sentence bar (0.18 and 0.0); both stay decoded, not read, blockers no-key-material and illegible."
    save(T, p); print('notes')


def steps():
    for s in STEPS:
        p = load(T); p['solution'].append(s); save(T, p)
    print('steps')


if __name__ == '__main__':
    {'texts': texts, 'gaps': gaps, 'outcome': outcome, 'steps': steps}[sys.argv[1]]()
