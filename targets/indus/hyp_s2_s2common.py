"""Shared bits for session-2 follow-ups of set 552."""
from numerals import NUMS
SMALL = {'176', '233', '235', '240', '520', '61', '803', '806'}
LARGE = {'368', '390', '405', '407', '575', '585', '740', '900'}


def units(S, group):
    """(line, index) of a counted sign of the group standing right after a numeral."""
    return [(t, i) for t in S for i in range(1, len(t)) if t[i] in group and t[i - 1] in NUMS]
