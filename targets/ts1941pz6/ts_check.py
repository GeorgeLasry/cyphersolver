"""Truppenschluessel (TS) checks for targets/ts1941pz6. Python standard library only.

    python ts_check.py            (prints the report; ts_check_output.txt is this output)

1. The TS rule, written from Ostwald & Weierud, "Modern Cryptanalysis of the Truppenschluessel"
   (author copy https://cryptocellar.org/pubs/mcts.pdf): single stage, consecutive plaintext pairs, no
   seriation. Two 5x5 squares without J, L (left) and R (right); p1 is looked up in L, p2 in R.
     rows differ:  c1 = R[row p1][col p2],  c2 = L[row p2][col p1]
     same row r:   c1 = R[r][col p2 + 1],   c2 = L[r][col p1 + 1]   (right neighbours, wrapping)
2. Rule control on the paper's own examples: the Fig. 2 example key, and the two 17 Sep 1941
   plaintext-ciphertext pairs with the squares of Fig. 6.
3. The 4 July 1941 ciphertext in messages.txt: lengths, and repeated strings of 6 or more letters with the
   parity of their start (a fixed two-letter substitution of consecutive pairs repeats only at equal parity).

Nothing here deciphers the pz6 messages: no key for them is known to us (see NOTES.md).
"""
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def pos(sq):
    return {ch: divmod(i, 5) for i, ch in enumerate(sq)}


def enc_pair(L, R, p1, p2):
    (r1, k1), (r2, k2) = pos(L)[p1], pos(R)[p2]
    if r1 != r2:
        return R[r1 * 5 + k2] + L[r2 * 5 + k1]
    return R[r1 * 5 + (k2 + 1) % 5] + L[r1 * 5 + (k1 + 1) % 5]


def dec_pair(L, R, c1, c2):
    (ra, ka), (rb, kb) = pos(R)[c1], pos(L)[c2]
    if ra != rb:
        return L[ra * 5 + kb] + R[rb * 5 + ka]
    return L[ra * 5 + (kb - 1) % 5] + R[ra * 5 + (ka - 1) % 5]


def encrypt(L, R, pt):
    return "".join(enc_pair(L, R, pt[i], pt[i + 1]) for i in range(0, len(pt) - 1, 2))


def decrypt(L, R, ct):
    return "".join(dec_pair(L, R, ct[i], ct[i + 1]) for i in range(0, len(ct) - 1, 2))


def rule_control():
    print("== 1. Rule control (Ostwald & Weierud, Fig. 2 and Figs. 5-6)")
    L = "HILQE" "TUARS" "BKXFG" "PWCOZ" "DVYMN"
    R = "ZNOCH" "BXAVI" "UDTGW" "MYELS" "KPQRF"
    ok = 0
    for p, exp in [("PE", "LW"), ("RT", "AF"), ("AF", "IY"), ("LW", "HX")]:
        got = enc_pair(L, R, p[0], p[1])
        ok += got == exp
        print(f"  Fig. 2 key: {p} -> {got}, paper {exp}")
    print(f"  Fig. 2: {ok}/4 as in the paper")
    L6 = "WKIZB" "OGPSF" "ENHQR" "DATLM" "VCXUY"
    R6 = "IGVBX" "DPQFS" "REYNC" "ZOLMH" "ATUKW"
    pairs = [
        ("FFZNSBQTHNCIQTHNCIXPOOAQTQAZ", "sqarfxplachxplachxistzurueqb"),
        ("TNDGLXSBYQCHBHSKYQCHBHSKRCERTIENRVOHMNGMRFENKQSAGVOHGWKZFWENBHQFA"
         "HRWZYCHAHRWZYCHTHBHPNZHSYPRCKINZGORZSENRKEUZVTPZUWAWPSZBFZNSB",
         "ceostufxhenningxhenningxnaqrxgereateanborderungheutebilxobeginspx"
         "reimannxreimannxeingetroffenxkradmelderniqtdaxplachxssxsqarfx"),
    ]
    for ct, pt in pairs:
        d = decrypt(L6, R6, ct).lower()
        agree = sum(a == b for a, b in zip(d, pt))
        form_ct = encrypt(L6, R6, pt.upper())
        print(f"  17 Sep 1941, {len(ct)} letters: {agree}/{len(pt)} letters agree with the form's plaintext")
        print(f"    decrypted: {d}")
        print(f"    form:      {pt}")
        for i in range(0, len(ct) - 1, 2):
            if d[i:i + 2] != pt[i:i + 2]:
                print(f"    pair {i // 2 + 1}: cipher {ct[i:i + 2]}, the form's plaintext gives {form_ct[i:i + 2]}"
                      f" (one-letter garble: {sum(a != b for a, b in zip(ct[i:i + 2], form_ct[i:i + 2])) == 1})")


def load_messages():
    msgs = {}
    with open(os.path.join(HERE, "messages.txt"), encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            nr, groups = line.strip().split(" ", 1)
            msgs[nr] = groups.replace(" ", "")
    return msgs


def lengths(msgs):
    print("\n== 2. Lengths (cells as printed; '-' = missing or illegible letter)")
    tot = 0
    for nr, s in msgs.items():
        tot += len(s)
        print(f"  Nr. {nr}: {len(s):4d} cells, {sum(c.isalpha() for c in s):4d} letters, {s.count('-')} '-',"
              f" {s.count('J')} J")
    print(f"  total {tot} cells")


def repeats(msgs, minlen=6):
    print(f"\n== 3. Repeated strings of {minlen} or more letters (start positions from 0, with parity)")
    where = defaultdict(list)
    for nr, s in msgs.items():
        for i in range(len(s) - minlen + 1):
            w = s[i:i + minlen]
            if "-" not in w:
                where[w].append((nr, i))
    seen = set()
    rows = []
    for w, occ in where.items():
        if len(occ) < 2:
            continue
        for x in range(len(occ)):
            for y in range(x + 1, len(occ)):
                # extend each pair of occurrences to the maximal repeat they share
                (n1, i1), (n2, i2) = occ[x], occ[y]
                s1, s2 = msgs[n1], msgs[n2]
                a, b, k = i1, i2, minlen
                while a > 0 and b > 0 and s1[a - 1] == s2[b - 1] and s1[a - 1] != "-":
                    a, b, k = a - 1, b - 1, k + 1
                while a + k < len(s1) and b + k < len(s2) and s1[a + k] == s2[b + k] and s1[a + k] != "-":
                    k += 1
                key = (s1[a:a + k], n1, a, n2, b)
                if key not in seen:
                    seen.add(key)
                    rows.append(key)
    same = 0
    for w, n1, a, n2, b in sorted(rows, key=lambda r: (-len(r[0]), r[0])):
        par = "same parity" if a % 2 == b % 2 else "DIFFERENT parity"
        same += a % 2 == b % 2
        print(f"  {w:<12} Nr. {n1}@{a} ({'even' if a % 2 == 0 else 'odd'})   Nr. {n2}@{b}"
              f" ({'even' if b % 2 == 0 else 'odd'})   {par}")
    print(f"  {same} of {len(rows)} repeats start at the same parity")


if __name__ == "__main__":
    rule_control()
    m = load_messages()
    lengths(m)
    repeats(m)
