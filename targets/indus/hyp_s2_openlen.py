"""Session-2 loop 6: lines that open with an opener (set 539) are longer: the opener is a heading added to a full text."""
import s2kit as K
from scipy.stats import mannwhitneyu

TITLE = 'opener lines are longer'
REG = '''Openers (set 539: 104 491 692 817 820 853 861 920 on A) head a line (`hyp_s2_openlen.py`).

- **OL1** On A, lines opening with an opener are longer than other lines (Mann-Whitney p < 0.05).
- **OL2** The same on B, using A's openers.
- Progress rule: OL1 and OL2. (Set 230-279 already studied the heading; if this only re-finds the heading unit, it is
  recorded as consistency.)'''
SUMMARY = ''
OP = {'104', '491', '692', '817', '820', '853', '861', '920'}


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S in (('OL1', 'A', DA), ('OL2', 'B', DB)):
        a = [len(t) for t in S if t[0] in OP]
        b = [len(t) for t in S if t[0] not in OP]
        p = mannwhitneyu(a, b, alternative='greater').pvalue if a and b else 1
        ok = p < 0.05
        rd.rec(key, 'opener lines longer, %s' % name, 'mean %.2f (%d) against %.2f (%d), p = %.4g' % (sum(a) / max(1, len(a)), len(a), sum(b) / max(1, len(b)), len(b), p), ok)
        out.append(ok)
    SUMMARY = 'opener lines longer on A %s, B %s; the heading unit (sets 230-279) already covers it: consistency.' % tuple(out)
    return False  # registered as consistency: the heading is a known unit
