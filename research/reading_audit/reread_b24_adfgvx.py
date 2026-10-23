"""Re-read brief (REREAD_BRIEF.md), batch b24: adfgvx (residue entry: 3 partial + 10 open messages).

    python research/reading_audit/reread_b24_adfgvx.py split|outcome|steps
Helpers: b24_adfgvx_217.py (known-plaintext check of the 2026 p. 217 decipherment), b24_adfgvx_vgada.py (VGADA
against Baertl's 2017 text). The residue entry's state/note go through set_state.py.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

T = 'adfgvx'
P217 = {
    'doc': 'p217',
    'label': 'Childs p. 217 (DXXXG GVXAX ..., 27 Nov 1918), one of the ten open messages',
    'transcription': 'msgs.txt',
    'decryption': 'texts/p217_b24_check.txt',
    'reading': 'texts/p217_reading.md',
    'translation': 'texts/p217_en.md',
    'summary': "An English cruiser has put in at Sevastopol on the 24th; an Allied squadron follows on the 26th. Decipherment published by 'prinz' on 17 Sept 2026 (keyword TRUPPENVERSCHIEBUNG, a key Childs lists for later use), checked here against the figures: the 85 plaintext letters map one to one onto the 85 ADFGVX pairs (23 pairs, 23 letters, no conflict).",
    'language': 'de',
    'state': 'read',
    'reading_review': {'grade': 'B', 'by': 'Claude Opus 5.5', 'date': '2026-10-22',
                       'note': "Read 23 Oct 2026 (b24) from the decipherment reported in Sept 2026 ('prinz', The Neuron 18 Sept 2026), verified as known plaintext (b24_adfgvx_217.py): with transposition keyword TRUPPENVERSCHIEBUNG the 170 received letters give 85 pairs that map one to one onto the 85 letters (23 distinct each, no conflict), and the 23 cells fall into a keyword-shaped square (T R U P E 4 / N . S C 2 H). Every letter carried by its pair. Two telegraphic sentences; body 0.50 clean (1/2: 'einlieg', 'sewastopol' not in the word list), explicit holes 1.00. The same transposition and cells give noise on the nine other open messages."},
}


def split():
    p = load(T)
    texts = p['outcome']['texts']
    i = [k for k, t in enumerate(texts) if t.get('state') == 'decoded, not read'][0]
    texts[i]['label'] = "the same file: three messages read only in part (p. 164 F-G-X, p. 164 VFGAG, VGADA p. 215) and nine with no reading (pp. 73, 152, 153 VFVAX and AXVAA, 158, 170, 176 GGDAA, 189, 198); p. 217 is now its own entry"
    save(T, p)
    p = load(T)
    texts = p['outcome']['texts']
    i = [k for k, t in enumerate(texts) if t.get('state') == 'decoded, not read'][0]
    texts[i]['summary'] = "Twelve of the 22 residue messages: three give fragments (Temesvar, Mirco; the Entente fleet at Kertsch with New Zealand, English and French divisions, VGADA, partial reading in texts/vgada_partial_reading.md); nine have no reading, because no known key fits them and several carry marked transmission gaps."
    save(T, p)
    p = load(T)
    p['outcome']['texts'].append(P217)
    save(T, p)
    p = load(T)
    p['documents'] = p.get('documents', [])
    print('split')


def outcome():
    p = load(T)
    p['outcome']['gaps'] = [
        {'item': 'nine open messages (pp. 73, 152, 153 x2, 158, 170, 176 GGDAA, 189, 198; 1,320 letters)', 'blocker': 'no-key-material',
         'detail': "no known key fits: the fourteen period keys, Lasry's CHI key, and (b24) the TRUPPENVERSCHIEBUNG transposition with the 23 cells recovered from p. 217 all give noise; key-free recovery is out of reach at 84-240 letters"},
        {'item': 'three partly read messages (p. 164 F-G-X, p. 164 VFGAG, VGADA p. 215)', 'blocker': 'needs-physical-access',
         'detail': "transmission gaps (44, 44 and 11 marked letters; Norbert notes the transcript also lacks a whole line of p. 164); VGADA (b24): 97 of 129 letters carried by both cells, 20 of Baertl's 2017 letters contradict the received cells, so his text is part emendation; Childs's book pages would show whether the transcript dropped more"},
    ]
    save(T, p)
    p = load(T)
    p['outcome']['notes'] = p['outcome']['notes'] + " 23 Oct 2026 (b24): p. 217 read from the decipherment reported in Sept 2026 ('prinz', keyword TRUPPENVERSCHIEBUNG), verified here as known plaintext (85 pairs, one-to-one); VGADA's 2017 reading checked letter by letter (20 of Baertl's letters against the cells): stays partial."
    save(T, p)
    print('outcome')


STEPS = [
    {'date': '2026-10-23', 'kind': 'literature search', 'what': "Re-read (REREAD_BRIEF, b24): searched for readings of the residue messages published after 2017. Found a decipherment of a 27 Nov 1918 message of about 170 letters posted by 'prinz' on 17 Sept 2026 (reported by The Neuron, 18 Sept 2026, and news sites): keyword TRUPPENVERSCHIEBUNG, plaintext 'EIN ENGLISCHER KREUZER EINLIEG X SEWASTOPOL X S4STEN X EIN GESCHWADER DER X ALLIIERTEN FOLGT 26STEN X'. Childs p. 217 has 170 letters.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'control', 'technique': ['plaintext matching', 'key matching'], 'what': "Known-plaintext check on p. 217 (b24_adfgvx_217.py): the transposition by TRUPPENVERSCHIEBUNG turns the 170 received letters into 85 pairs that map one to one onto the 85 plaintext letters (23 distinct pairs, 23 distinct letters, no conflict), and the recovered cells form a keyword-shaped square (T R U P E 4 / N . S C 2 H). Accepted; texts/p217_reading.md and _en.md. The same transposition and cells applied to the nine other open messages give noise.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'control', 'technique': ['plaintext matching'], 'what': "VGADA (Childs p. 215): Norbert's two inserted groups with the Nov 22-24 key reproduce his raw decrypt exactly; aligned letter by letter with Baertl's 2017 corrected text (b24_adfgvx_vgada.py): 97 of 129 letters carried by both cells, 11 by one, 1 by none, 20 of Baertl's letters contradict the received cells and only 5 of those are one-cell errors ('S4N' twice where he reads '24N'; p. 217 has 'S4STEN' too). Partial reading kept (texts/vgada_partial_reading.md, 0.00 clean); stays decoded, not read.", 'result': 'partial'},
    {'date': '2026-10-23', 'kind': 'solver', 'technique': ['simulated annealing', 'language-model scoring'], 'what': "VGADA residual search with the three length-22 keys and two free edits (gaps.py anneal, 6 restarts) before Norbert's edits were applied: noise (-7.4 per letter); his group insertions at the marked gap and after group 43 are what make it decrypt.", 'result': 'failed'},
]


if __name__ == '__main__':
    w = sys.argv[1]
    if w == 'split': split()
    elif w == 'outcome': outcome()
    elif w == 'steps':
        for s in STEPS:
            p = load(T); p['solution'].append(s); save(T, p)
        print('steps')
