"""b34: apply the sessa1524 key values added after pass 15 (passes 16, 17, b23; sessa1524/key_working.md) to the
(b) lines of targets/sessa1523/reading_r9660.txt, read only; writes targets/sessa1523/reading_r9660_b34.txt and
prints, per new value, the R9660 contexts it lands in (to check it reads in every occurrence).

    python research/reading_audit/b34_sessa_apply.py
"""
import re, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / 'targets/sessa1523/reading_r9660.txt'
OUT = ROOT / 'targets/sessa1523/reading_r9660_b34.txt'
# value, source pass; 'T' = tentative/sense-only in sessa1524 (flag), 'A' = attested by a contemporary decipherment
V = {
 'ruc': ('dicho', 'A16'), 'li': ('mi', 'A16'), 'Jac': ('obliga', 'A16'), 'le': ('me', 'A16'), 'net': ('halla', 'A16'),
 'nuh': ('grande', 'A16'), 'kch': ('mal', 'A16'), 'cap': ('tem', 'A16'), 'lec': ('mos', 'A16'), 'dug': ('sabi', 'A16'),
 'doh': ('sabe', 'A16'), 'yol': ('aqui', 'A16'), 'sud': ('datario', 'A16'), 'pand': ('buena', 'A16'), 'Jur': ('parte', 'A16'),
 'kun': ('duque', 'A16'), 'hay': ('aunque', 'T16'), 'cuq': ('tengo', 'T16'), 'tig': ('contra', 'T16'), 'gat': ('esto', 'T16'),
 'yod': ('amigo', 'T16'), 'quf': ('enemigo', 'T16'), 'kuc': ('liga', 'T16'), 'fed': ('rey de Francia', 'T16'),
 'xir': ('cardenal', 'T16'), 'lot': ('nuncio', 'T16'), 'pof': ('exercito', 'T16'), 'cex': ('trata', 'T16'),
 'lin': ('necesidad', 'T16'), 'bun': ('visorrey', 'T16'), 'kin': ('manda', 'T16'), 'qus': ('este', 'T16'),
 'guf': ('puede', 'T16'), 'vih': ('cerca', 'T16'), 'lef': ('parece', 'T16'), 'Jus': ('pasa', 'T16'), 'sus': ('pasa', 'T16'),
 'him': ('poco', 'T16'), 'hoz': ('dich', 'T16'), 'nah': ('govierno', 'T16'),
 'cas': ('tien', 'T17'), 'var': ('agora', 'T17'), 'rac': ('dize', 'T17'), 'pam': ('paga', 'T17'), 'Jir': ('paga', 'T17'),
 'xoc': ('socorr', 'T17'), 'leg': ('mucho', 'T17'), 'sur': ('parte', 'T17'), 'len': ('buen', 'T17'), 'lon': ('buen', 'T17'),
 '3ar': ('aca', 'T17'), 'yer': ('Florencia', 'T17'), 'gig': ('quisie', 'T17'), 'nuf': ('gente', 'T17'), 'rul': ('dia', 'T17'),
 'foh': ('ha', 'T17'), 'Jam': ('llam', 'T17'), 'yeg': ('antes', 'T17'), 'cer': ('ten', 'T17'), 'fe': ('fue', 'T17'),
 'pus': ('florentines', 'T17'), 'sir': ('supli', 'T17'), 'kif': ('Lombardia', 'T17'), 'luc': ('parte', 'T17'),
 'qu': ('o', 'T17'), 'gob': ('ello', 'T17'), 'gul': ('si', 'T17'), 'cox': ('cobra', 'T17'), 'hut': ('primer', 'T17'),
 'gal': ('embia', 'Ab23'), 'hog': ('querria', 'Ab23'), 'kaz': ('mente', 'Ab23'), 'reb': ('dezi', 'Tb23'),
 'dis': ('servido', 'Tb23'), 'lar': ('miento', 'Tb23'), 'gom': ('quatro', 'Tb23'),
}
BR = re.compile(r'\[([^\]\s=?]+)\]')
lines = SRC.read_text(encoding='utf-8').splitlines()
ctx = collections.defaultdict(list); out = []; open_left = collections.Counter(); n_open = 0
for ln in lines:
    if re.match(r'\s*\d+\s*b\s', ln):
        def sub(m):
            g = m.group(1)
            if g in V:
                ctx[g].append(ln.strip()[:150]); return '[%s=%s]' % (g, V[g][0])
            return m.group(0)
        ln2 = BR.sub(sub, ln)
        for m in BR.finditer(ln2): open_left[m.group(1)] += 1
        out.append(ln2)
    else:
        out.append(ln)
OUT.write_text('\n'.join(out) + '\n', encoding='utf-8')
print('new values landing in R9660:', sum(len(v) for v in ctx.values()), 'occurrences of', len(ctx), 'groups')
for g in sorted(ctx, key=lambda g: -len(ctx[g])):
    print('==', g, V[g], len(ctx[g]))
    for c in ctx[g]: print('    ', c)
print('still bracketed (open) in b-lines:', sum(open_left.values()), 'tokens,', len(open_left), 'distinct')
print(open_left.most_common(40))
