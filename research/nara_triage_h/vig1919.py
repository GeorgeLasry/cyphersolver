"""Quick tests on the AEF Siberia field message of 9 July 1919 (M917 roll 9, frame 963)."""
import itertools, collections, string
CT = ("LJEQE WJJOM RFAHN OVLBO RDIWK RTAIU IISBE EVOIT HQFES TUCMA HNUJB NPFET WSPII SLLFO AMLUW DLVUI "
      "RPHFO XEYMJ XPQMB IFPOR ADMMC FMEBX EATCN TIMJJ OVDNR SPUUT MEKSM NCFRA RAYXK BYXBR XXKOX XALYX").replace(' ', '')
EN = dict(zip(string.ascii_uppercase, [8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,.15,.77,4.0,2.4,6.7,7.5,1.9,.1,6.0,6.3,9.1,2.8,.98,2.4,.15,2.0,.07]))
def ic(s):
    c = collections.Counter(s); n = len(s); return sum(v*(v-1) for v in c.values())/(n*(n-1))
print(len(CT), 'IC', round(ic(CT), 4))
for p in range(1, 16):
    cols = [CT[i::p] for i in range(p)]
    print(p, round(sum(ic(c) for c in cols)/p, 4))
def solve(p, beaufort=False):
    key = ''
    for i in range(p):
        col = CT[i::p]; best = None
        for k in range(26):
            if beaufort: pt = ''.join(chr((k - (ord(ch)-65)) % 26 + 65) for ch in col)
            else: pt = ''.join(chr((ord(ch)-65-k) % 26 + 65) for ch in col)
            sc = sum(EN[ch] for ch in pt)
            if best is None or sc > best[0]: best = (sc, k)
        key += chr(best[1]+65)
    if beaufort: pt = ''.join(chr(((ord(key[i % p])-65) - (ord(ch)-65)) % 26 + 65) for i, ch in enumerate(CT))
    else: pt = ''.join(chr((ord(ch)-ord(key[i % p])) % 26 + 65) for i, ch in enumerate(CT))
    return key, pt
for p in range(2, 13):
    for b in (False, True):
        k, pt = solve(p, b); print(p, 'beau' if b else 'vig', k, pt[:80])
