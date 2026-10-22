"""Full texts on every reading (George Lasry, 22 Oct 2026).

A reading (classed "read" or "read in part", or "already solved" with a reading method) lists, in profile.json outcome.texts, the transcription and the decryption of
every document it reports on, and in outcome.key_file the key it used when the project recovered, extended or
corrected it. Paths are relative to the target folder (or http(s) URLs, discouraged: a copy in the folder survives).

  "texts": [{"doc": "<documents[].id>", "label": "R1072, 6 Jan 1757 (optional)",
             "transcription": "transcr/R1072.txt", "decryption": "read/R1072.md",
             "reading": "read/R1072_reading.md (optional: the decryption as sentences)",
             "translation": "read/R1072_en.md", "language": "fr",
             "state": "read | decoded, not read | not prose",
             "summary": "One or two sentences on what the document says."}],
  "key_file": "key_X.tsv"          (or a list)
  "texts_withheld": "reason"         when the texts must not be republished (the owner asked); exempts the target

One entry may cover several documents ("doc": ["a", "b"]) when one file holds them all. The site builder renders a
"Full texts" section from it (short files inline, long ones linked); docs/_check_writeup.py refuses a reading
without it. texts_problems() is the shared check.

A reading must read (George Lasry, 22 Oct 2026, on matignon1586): "the LLM can build coherent sentences - that can
later be translated to English ... It is OK to have a few holes, but not holes in almost every sentence."
reading_problems() is that check, per entry:

  state "read" (default)    the decryption scores at or above MARGINAL on docs/_check_reading.py (sentences with at
                            most one hole in ten words), or a reader has recorded reading_review {grade A|B, by, date};
                            and it carries an English translation unless language is "en"
  state "decoded, not read" a mechanical decode shown for checking, not counted as a reading; no translation needed
  state "not prose"         a key sheet, code list, worksheet, numbers or names; say what in note
A target classed "read" may not hold a "decoded, not read" entry.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
READING = ('read', 'read in part')
NOT_READINGS = ('not solved', 'not applicable')   # methods that mean no reading exists
KEY_WORK = ('key recovered', 'key extended or corrected')


def listify(v):
    return [] if v in (None, '') else v if isinstance(v, list) else [v]


def needs_texts(profile):
    """A reading: classed read / read in part, or already solved elsewhere with a reading method (from an existing
    decipherment, a known or external key, plaintext ...): the text was deciphered, so it is shown (22 Oct 2026)."""
    o = (profile or {}).get('outcome') or {}
    if o.get('class') in READING: return True
    return o.get('class') == 'already solved' and o.get('method') not in NOT_READINGS and bool(o.get('method'))


def texts_problems(folder_path, profile):
    """Problems with outcome.texts / key_file for a reading; [] when fine or when the target is not a reading."""
    if not needs_texts(profile): return []
    o = profile.get('outcome') or {}
    if o.get('texts_withheld'): return []          # e.g. fr3029/fr3092: Lasry asked (22 Sept 2026) not to republish
    probs = []
    texts = o.get('texts') or []
    if not texts:
        return ['no outcome.texts: list the transcription and decryption of every document (George Lasry, 22 Oct 2026)']
    docs = [d.get('id') for d in profile.get('documents') or [] if d.get('id')]
    covered = {x for t in texts for x in listify(t.get('doc'))}
    if 'all' not in covered:
        missing = [d for d in docs if d not in covered]
        if missing: probs.append('documents without texts: ' + ', '.join(missing[:8]) + (' ...' if len(missing) > 8 else ''))
    for t in texts:
        label = '/'.join(listify(t.get('doc'))) or '?'
        for kind in ('transcription', 'decryption'):
            files = listify(t.get(kind))
            if not files: probs.append(f'{label}: no {kind} file')
        for kind in ('transcription', 'decryption', 'reading', 'translation'):
            for f in listify(t.get(kind)):
                if not str(f).startswith('http') and not (folder_path / f).exists():
                    probs.append(f'{label}: {kind} file {f} does not exist')
    contrib = o.get('contribution') or []
    if any(c in KEY_WORK for c in contrib):
        keys = listify(o.get('key_file'))
        if not keys: probs.append('no outcome.key_file although the key was recovered, extended or corrected')
        for f in keys:
            if not str(f).startswith('http') and not (folder_path / f).exists():
                probs.append(f'key file {f} does not exist')
    return probs


def entry_state(t):
    return t.get('state') or 'read'


def reading_problems(folder_path, profile, score=True):
    """Problems with the readability of a reading's texts (George Lasry, 22 Oct 2026): [] when fine.
    Returns (hard, soft): hard refuses the write-up, soft is a warning."""
    if not needs_texts(profile): return [], []
    o = profile.get('outcome') or {}
    if o.get('texts_withheld'): return [], []
    hard, soft = [], []
    states = [entry_state(t) for t in o.get('texts') or []]
    if o.get('class') == 'read' and 'decoded, not read' in states:
        hard.append('classed "read" but an entry is "decoded, not read": a reading must read throughout')
    if states and all(s == 'decoded, not read' for s in states):
        hard.append('every entry is "decoded, not read": this is not a reading (class it as not solved / attempted, open)')
    cr = None
    for t in o.get('texts') or []:
        label = t.get('label') or '/'.join(map(str, listify(t.get('doc')))) or '?'
        st = entry_state(t)
        if st == 'not prose':
            if not t.get('note'): soft.append(f'{label}: "not prose" without a note saying what it is')
            continue
        if st == 'decoded, not read': continue
        if not listify(t.get('translation')) and (t.get('language') or '').lower() != 'en':
            hard.append(f'{label}: no English translation (outcome.texts[].translation; or language "en")')
        rv = t.get('reading_review') or {}
        if not score or rv.get('grade') in ('A', 'B'): continue
        if cr is None:
            import _check_reading as cr
        best = None
        for f in listify(t.get('decryption')) + listify(t.get('reading')):
            fp = folder_path / f
            if str(f).startswith('http') or not fp.is_file() or fp.suffix.lower() in ('.pdf', '.json'): continue
            r = cr.score_text(fp.read_text(encoding='utf-8', errors='ignore'), lang=(t.get('language') or None))
            if r['shape'] == 'other script': best = ('n/a', r); break
            if best is None or (r['clean_share'] or 0) > (best[1]['clean_share'] or 0): best = (f, r)
        if best is None or best[0] == 'n/a':
            if best and not rv: soft.append(f'{label}: not in the Latin alphabet, so not scored: record reading_review after reading it')
            continue
        share = best[1]['clean_share'] or 0
        if share < cr.MARGINAL:
            hard.append(f'{label}: holes in most sentences ({share:.0%} of sentences clean in {best[0]}, bar {cr.MARGINAL:.0%}): '
                        f're-read it, mark it state "decoded, not read", or record reading_review if a reader finds it coherent')
        elif share < cr.READABLE or best[1]['shape'] != 'reading':
            soft.append(f'{label}: {share:.0%} of sentences clean, shape {best[1]["shape"]} (readable: {cr.READABLE:.0%}, prose)')
    return hard, soft


def summary_missing(profile):
    """True when no document entry carries a summary of its contents (a nudge, not a refusal)."""
    if ((profile or {}).get('outcome') or {}).get('texts_withheld'): return False
    return needs_texts(profile) and not any(t.get('summary') for t in ((profile.get('outcome') or {}).get('texts') or []))
