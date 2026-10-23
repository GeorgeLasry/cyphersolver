"""Re-read brief (REREAD_BRIEF.md), batch b24: army1902 (C03020059400). Targeted profile edits, one save per change.
    python research/reading_audit/reread_b24_army.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402
T = 'army1902'
p = load(T); e = [x for x in p['outcome']['texts'] if x['doc'] == 'C03020059400'][0]
e.pop('note', None); e['state'] = 'read'; save(T, p)
for k, v in [('reading', 'texts/C03020059400_reading.md'), ('translation', 'texts/C03020059400_en.md'),
             ('summary', "Division commander Inoue to the War Minister, Jan 1904: the NCOs, men, equipment and materials needed by Anchorage Command Shin (辛碇泊場司令部, the enciphered words) have been handed to the head of the Moji branch supply depot, who will report completion directly. Read with the contemporary translation filed with it (frame 0118)."),
             ('reading_review', {'grade': 'B', 'by': 'Claude Opus 5.5', 'date': '2026-10-22', 'note': "Read 23 Oct 2026 (b24): the item's frame 0118 is a contemporary translation (訳文) of the whole telegram, '辛碇泊場司令部ニ要スル下士以下及器具材料ハ門司補給廠支廠長ニ交付済。…ノ結了ハ支廠長ヨリ直接報告ノ筈'; the 12 enciphered pairs are the unit name, 10 of 12 under the 1902 table, digits re-read on frame 0119 (pair 5 '0' + a glyph read 九 that may be a cursive 四; pair 7 written 八八 for 六八). 2 of 12 kana of the cipher run rest on the translation against the figures (one on a look-alike 九/四). Two sentences, one hole (three cramped characters of the translation); _check_reading does not segment Japanese; by hand 2/2 sentences with at most one hole."})]:
    p = load(T); e = [x for x in p['outcome']['texts'] if x['doc'] == 'C03020059400'][0]; e[k] = v; save(T, p)
p = load(T)
p['outcome']['gaps'] = [g for g in p['outcome']['gaps'] if not g['item'].startswith('C03020059400')] + [
    {'item': 'C03020059400 pairs 5 and 7 (0 + 九-or-四 for ハ, 八八 for ジ) and three characters of the filed translation', 'blocker': 'illegible',
     'detail': 're-read on the JACAR scan of frames 0118-0119 (23 Oct 2026): the foot of column 1 is a glyph unlike the 九 above it; column 2 writes 八 twice; the translation is cramped after the ○'}]
save(T, p)
p = load(T)
p['solution'].append({'date': '2026-10-23', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b24): the JACAR item C03020059400 (23 frames) fetched as one PDF through the viewer's raw/ path. Frame 0118 is the filed translation (訳文) of the telegram on frame 0119: '辛碇泊場司令部ニ要スル下士以下及器具材料ハ門司補給廠支廠長ニ交付済 ○ …ノ結了ハ支廠長ヨリ直接報告ノ筈', addressed 大臣宛 井上師団長.", 'result': 'worked'})
save(T, p)
p = load(T)
p['solution'].append({'date': '2026-10-23', 'kind': 'transcription', 'technique': ['plaintext matching'], 'what': "The 12 cipher pairs re-read on frame 0119 at 400 dpi: columns 一七一〇三六一九〇? / 二八八八二九一七三一 / 一九七六, as transcribed; the last digit of pair 5 is unlike the 九 two rows above it (九 or a cursive 四: ア or ハ) and pair 7 is written 八八 (ゼ) where the translation's ジ needs 六八. Reading written from the translation with the cipher run aligned (texts/C03020059400_reading.md, _en.md); set read, grade B.", 'result': 'worked'})
save(T, p); print('ok')
