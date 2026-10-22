"""Targeted text edits to a profile.json for the relabel brief (list relabel_2, 22 Oct 2026).

Keeps the file's layout: inserts or replaces only the lines it changes (no reload-and-dump).

  from relabel_edit_r2 import Prof
  p = Prof('fiesque1567')
  p.entry(i, state='decoded, not read', language='fr', note='...')   # i = index in outcome.texts
  p.outcome('class', 'read in part'); p.outcome('fraction_read', 0.05, after='class')
  p.step('what ...', result='failed')
  p.save()   # then: python docs/_check_profile.py <folder>
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _scan_value_end(s, i):
    """s[i] starts a JSON value; return the index just after it."""
    return i + len(json.dumps(json.JSONDecoder().raw_decode(s[i:])[0])) if False else \
        i + _raw_len(s, i)


def _raw_len(s, i):
    dec = json.JSONDecoder()
    _, end = dec.raw_decode(s, i)
    return end - i


def _top_key(s, st, key):
    """Value span of top-level `key` in the object starting at s[st] == '{'."""
    dec = json.JSONDecoder(); ws = re.compile(r'[\s,]*')
    i = st + 1
    while True:
        i = ws.match(s, i).end()
        if s[i] == '}': raise KeyError(key)
        k, i = dec.raw_decode(s, i)
        i = re.compile(r'\s*:\s*').match(s, i).end()
        _, e = dec.raw_decode(s, i)
        if k == key: return i, e
        i = e


class Prof:
    def __init__(self, folder):
        self.path = ROOT / 'targets' / folder / 'profile.json'
        raw = self.path.read_bytes().decode('utf-8')
        self.crlf = '\r\n' in raw
        self.s = raw.replace('\r\n', '\n')
        self.ea = not any(ord(c) > 127 for c in self.s)

    def dumps(self, v):
        return json.dumps(v, ensure_ascii=self.ea)

    # -- locate outcome.texts entries -------------------------------------------------------------
    def _texts_span(self):
        o = self.s.index('"outcome"')
        t = self.s.index('"texts"', o)
        a = self.s.index('[', t)
        return a, a + _raw_len(self.s, a)

    def _entries(self):
        a, b = self._texts_span()
        out, i, dec = [], a + 1, json.JSONDecoder()
        while True:
            m = re.compile(r'\s*,?\s*').match(self.s, i)
            i = m.end()
            if self.s[i] == ']': break
            v, end = dec.raw_decode(self.s, i)
            out.append((i, end, v))
            i = end
        return out

    def entry(self, idx, **fields):
        st, en, v = self._entries()[idx]
        body = self.s[st:en]
        for k, val in fields.items():
            if k in v:   # replace the existing top-level value in place
                vs, ve = _top_key(self.s, st, k)
                self.s = self.s[:vs] + self.dumps(val) + self.s[ve:]
            else:
                if '\n' not in body.strip():   # one-line entry
                    close = st + body.rstrip().rindex('}')
                    self.s = self.s[:close] + ', "%s": %s' % (k, self.dumps(val)) + self.s[close:]
                else:   # expanded entry: insert after the label line (or the first key line)
                    m = re.search(r'\n([ \t]*)"label"\s*:', body) or re.search(r'\n([ \t]*)"', body)
                    ind = m.group(1)
                    ls = st + m.start() + 1
                    vs = ls + len(m.group(0)) - 1
                    # end of that key's value
                    q = re.compile(r'"[^"]*"\s*:\s*').match(self.s, ls + len(ind))
                    ve = q.end() + _raw_len(self.s, q.end())
                    ins = ',\n%s"%s": %s' % (ind, k, self.dumps(val))
                    self.s = self.s[:ve] + ins + self.s[ve:]
            st, en, v = self._entries()[idx]
            body = self.s[st:en]
        return self

    # -- outcome scalars -------------------------------------------------------------------------
    def outcome(self, key, val, after=None):
        o = self.s.index('"outcome"')
        ob = self.s.index('{', o)
        oe = ob + _raw_len(self.s, ob)
        seg = self.s[ob:oe]
        # only top-level keys of outcome: find with matching indent of "class"
        m = re.search(r'\n([ \t]*)"class"\s*:', seg)
        ind = m.group(1) if m else None
        pat = (r'\n%s"%s"\s*:\s*' % (re.escape(ind), re.escape(key))) if ind is not None else (r'"%s"\s*:\s*' % re.escape(key))
        m2 = re.search(pat, seg)
        if m2:
            vs = ob + m2.end()
            ve = vs + _raw_len(self.s, vs)
            self.s = self.s[:vs] + self.dumps(val) + self.s[ve:]
            return self
        a = re.search(r'\n%s"%s"\s*:\s*' % (re.escape(ind), re.escape(after or 'class')), seg)
        vs = ob + a.end()
        ve = vs + _raw_len(self.s, vs)
        self.s = self.s[:ve] + ',\n%s"%s": %s' % (ind, key, self.dumps(val)) + self.s[ve:]
        return self

    # -- solution step ---------------------------------------------------------------------------
    def step(self, what, result='failed', technique=('language-model scoring', 'statistical test')):
        k = self.s.index('"solution"')
        a = self.s.index('[', k)
        b = a + _raw_len(self.s, a)
        seg = self.s[a:b]
        last_close = seg.rstrip()[:-1].rstrip()   # up to the last entry's closing brace
        lc = a + len(last_close)
        # last entry start
        ls = seg.rfind('\n', 0, len(last_close))
        line = seg[ls + 1:len(last_close)]
        st = {'date': '2026-10-22', 'kind': 'verification', 'what': what, 'result': result,
              'technique': list(technique)}
        if line.strip().startswith('{') and line.strip().endswith('}'):   # compact one-line steps
            ind = line[:len(line) - len(line.lstrip())]
            ins = ',\n%s%s' % (ind, self.dumps(st))
        else:
            ind = line[:len(line) - len(line.lstrip())]          # indent of the closing brace
            ki = ind + ' ' * (len(ind) - len(ind.rstrip(' ')) and 0)
            # key indent: look at the line before the closing brace
            prev = seg[:ls].rsplit('\n', 1)[1]
            kind = prev[:len(prev) - len(prev.lstrip())]
            if prev.lstrip().startswith(']'):
                kind = kind  # closing of an array value at key indent
            step_ind = kind[:len(kind) - (len(kind) - len(ind))] if len(kind) > len(ind) else ind
            unit = kind[len(ind):] or ' '
            body = json.dumps(st, indent=len(unit), ensure_ascii=self.ea)
            body = '\n'.join(ind + l for l in body.split('\n'))
            ins = ',\n' + body
        self.s = self.s[:lc] + ins + self.s[lc:]
        return self

    def save(self):
        json.loads(self.s)
        out = self.s.replace('\n', '\r\n') if self.crlf else self.s
        self.path.write_bytes(out.encode('utf-8'))


def review(grade, note):
    return {'grade': grade, 'by': 'Claude (reading audit)', 'date': '2026-10-22', 'note': note}
