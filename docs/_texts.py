"""Full texts on every reading (George Lasry, 22 Oct 2026).

A target classed "read" or "read in part" lists, in profile.json outcome.texts, the transcription and the decryption of
every document it reports on, and in outcome.key_file the key it used when the project recovered, extended or
corrected it. Paths are relative to the target folder (or http(s) URLs, discouraged: a copy in the folder survives).

  "texts": [{"doc": "<documents[].id>", "label": "R1072, 6 Jan 1757 (optional)",
             "transcription": "transcr/R1072.txt", "decryption": "read/R1072.md",
             "translation": "read/R1072_en.md", "summary": "One or two sentences on what the document says."}],
  "key_file": "key_X.tsv"          (or a list)
  "texts_withheld": "reason"         when the texts must not be republished (the owner asked); exempts the target

One entry may cover several documents ("doc": ["a", "b"]) when one file holds them all. The site builder renders a
"Full texts" section from it (short files inline, long ones linked); docs/_check_writeup.py refuses a reading
without it. texts_problems() is the shared check.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
READING = ('read', 'read in part')
KEY_WORK = ('key recovered', 'key extended or corrected')


def listify(v):
    return [] if v in (None, '') else v if isinstance(v, list) else [v]


def needs_texts(profile):
    return ((profile or {}).get('outcome') or {}).get('class') in READING


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
        for kind in ('transcription', 'decryption', 'translation'):
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


def summary_missing(profile):
    """True when no document entry carries a summary of its contents (a nudge, not a refusal)."""
    return needs_texts(profile) and not any(t.get('summary') for t in ((profile.get('outcome') or {}).get('texts') or []))
