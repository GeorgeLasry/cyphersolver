"""Check George Lasry's 18 Oct 2026 keys for fasc. 2 against this folder's own transcriptions.

For each piece: his key table (an image of cut signs on his page) is matched sign by sign to our token names
by hand (the KEYS dict below, one comment per doubtful identification); our tokens are deciphered with it and
aligned (edit distance) with the plaintext of his decryption. A token agrees when the letter his key gives it
is the letter it aligns to in his reading. Prints agreement per piece and the disagreements.

    python targets/siena1421/verify_lasry.py [no17 no11 ...]
"""
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")

# ---------------------------------------------------------------------------------------------------------
# No. 17 (R4805). Our transcription: transcripts/no17.txt (agent A, 24 Sept). His key: key_no17_R4805.png.
# Cipher segments between our clear words, in order, with the matching span of his decryption.
NO17_SEGMENTS = [
    ("c b 1 6 4 c 0 5o c DIV k 9 5 y 0 3 PHI 5 SS 3 6 1 0 4 TT u DIV h LAM p LAM h 5 BOX 4 6 HBAR "
     "6 0 4 y 6 6 9 p LAM f 0 3 HL u h u f 6 c LAM",
     "el Mustetto l'à a certe promessioni di non so che vescovadi per li nipoti"),
    ("L SIG 5 p 9 c 0 6 u p 9 HL DIV y 5 3 p LAM h 7 k 0 p LAM h 9 f 6 HL u y u 3 y 9 HL 0 y 6 4 0 p LAM "
     "f u c LAM EQ LAM 9 h DIV SS 0 3 HBAR 6 9 f 5 3 0 h c 9 p 6",
     "o a date vi dà lo Cardinale di Napoli circa le cose di Pitigiano perché v'à parentado"),
    ("9 h y 6 0 4 c 9 c 6 y 6 4 7 p 0 k 7 y 6 h c 0 4 TT 7",
     "anco è stato cosa de la contessa"),
    ("0 3 y h 6 EQ 1 6 6 y h u f 9 3 r HBAR 7 DIV h 0 4 TT 9 h 9 r^ w LAM n 9 q c DIV b 6 9 1 6 3 r",
     "erano giovani pare che aon essa n'abbi facto lo amore"),
    ("1 0 6 1 6 DIV b SQ h p 6 HL 6 9 6 0 3 r k y bl e x u N_ 4 c 3 0 h m h u 9 3 r h 6 BOX 6 u 6 9 p^ 9 "
     "6 u c 5o^ 6 9 3 u 9 DOT h 0 4 u 9 h 6 HL 9 4 TT 9 5o 4 SS 3 9 c LAM y 5 3 0 b DIV h 0 4 PHI 3 6 y 6 h "
     "c 9 p 6",
     "Otto volendo lo avere lco stren niare non vi vada vittuaria né siano lassate praticare lo nestro contado"),
]
# His table (columns A..V), our sign names. 6 = his O "6<" (25) and V "6" (12): our transcription did not split
# them, so 6 counts as o or v. 1 = his M "1" (3) and his bold O "1" (2). HBAR = his nomenclature sign "che".
# Matched by shape and then by occurrence count: our 7 (5) = the open variant of his A "9" (our 9 + 7 = 32, his 34);
# our y (14) = his C pair (10 + 3); our SS (3) = his P "+δ" (3); our 5o + 5o^ (3) = his T "ārō" (3).
# (A first pass had 7 = c, SS = t, 5o = p: 89.0%.)
NO17_KEY = {
    "9": "a", "5": "a", "7": "a", "r^": "b", "w": "b", "y": "c", "p": "d", "p^": "d",
    "0": "e", "r": "e", "SQ": "e", "n": "f", "EQ": "g", "u": "i", "LAM": "i",
    "HL": "l", "b": "l", "k": "l", "1": "mo", "h": "n", "BOX": "n", "6": "ov", "DIV": "o",
    "f": "p", "SS": "p", "3": "r", "4": "s", "TT": "s", "c": "t", "5o": "t", "5o^": "t", "PHI": "t", "SIG": "t",
    "HBAR": "che",
}


# ---------------------------------------------------------------------------------------------------------
# No. 11 (R4800). Our transcription: transcripts/no11.txt (agent B, 24 Sept). His key: key_no11_R4800.png.
# Our two blocks (L6 tail + C1-C4; D1-D5) are his two runs, line for line.
NO11_SEGMENTS = [
    ("SL3 G HASH 3 1 QB2 PLUS "
     "II D A S REV3 RHO O PLUS 3 N G HASH II S OMEGA OBAR D SL2 ODAG QB2 Q OSTEM SL2 PERP OMEGA DAG2 PLUS O PI HASH S DAG2 II OMEGA PI PERP PLUS ODAG QB2 2 HASH3 OBAR B DAG2 3 S OMEGA TAU "
     "PI QB2 REV3 PLUS O DAG2 S ZX PLUS O P PERP QB1 TAU PLUS O DAG2 M^n NX OBAR OMEGA O PLUS 3 OMEGA TAU QB1 A O B O G II O PLUS QB1 PLUS O DAG2 S DAG2 6 PI Q QB3 O PLUS 3 7 S OMEGA "
     "DAG2 PLUS O O PLUS II QB1 NX PLUS O 3 OMEGA SL2 II NX C PERP SL3 PLUS O DAG2 NX II DAG2 II A 3 7 HASH PERP NX OSTEM QB1 OBAR N II QB2 PI OBAR II ODAG II A PLUS O OMEGA O PLUS RHO "
     "ODAG O 6 DAG2 RHO HASH3 RHO D A OBAR Q PERP SL2 ODAG PLUS O ODAG M^n G Q O PLUS II DAG2 S C 3 6 QB1 3 N II QB1 OBAR 4 II OMEGA TAU QB1 PLUS O P B II 8 S E TAU G HASH",
     "et a quelo di Faenza che si contenteranno et egli stieno nele tere loro et mandino dua squadre per uno "
     "e di gente d'arme in campo Et maraviglomi di Faenza havendo hauto lo aviso che date più dì fa di ma non el sapevo"),
    ("8^dot 7 DOT G HASH G Q PLUS O HASH3 B 3 2 OMEGA TAU DAG2 7 3 PERP M^n A II OMEGA DOT 3 1 DOT N DAG2 II OMEGA SL2 QB2 B SL2 ODAG TAU QB2 II 7 PERP OMEGA OBAR II 2 ODAG D B 3 M^n QB2 SL3 Q C^tick 3 "
     "ODOT II DAG2 RHO O PLUS OBAR REV3 S D HASH3 DAG2 QB1 PLUS O DAG2 QB1 II DAG2 3 SL2 ODAG QB2 PLUS O DAG2 A TAU HASH3 PLUS O OMEGA DAG2 3 PLUS O DAG2 3 6 S ZX OBAR B 6 S QB1 "
     "A 3 2 OBAR A TAU B DAG2 QB1 OBAR SL2 PERP OMEGA DOT 8 O DOT ODAG A TAU NX 3 OMEGA OBAR O PLUS II DAG2 NX PLUS O OSTEM HASH3 NX S PI RHO QB2 DAG2 OMEGA O N II OMEGA HASH 3 "
     "O PLUS Q NX II OMEGA O PLUS D DOT TAILP DOT 4 OBAR P 3 OBAR QB1 A SL2 II DAG2 OSTEM C S QB1 D 6 S B DAG2 QB2 2 S OMEGA DAG2 3 PLUS O DAG2 4 OBAR REV3 QB2 C PLUS O DAG2 "
     "HASH3 II DAG2 PLUS O DAG2 Q PERP OMEGA D Q A D QB1 HASH Q II ODOT OBAR RHO 6 3 S PI PLUS O QB2 DAG2 O PLUS 3 DAG2 II E S PI PLUS O II EQ TAU ODOT II",
     "Del signor Giovan Francescho da Gonzagha si è spicato dile altre pratiche et volentieri verà a servigi vostri "
     "con huomini d'arme il meno et no fanti domanda milia ducati per queste genti et mille per la persona sua "
     "et Bacio viene et diravene a boca"),
]
# Before tokens are read, the pairs his table lists as nulls are joined: "G HASH" = his 'g#' (4), ". 3 1 ." and
# the opening "3 1" = his '31' (2), "8^dot 7" = his '87' (1); the numerals ". 8 O ." (80) and ". TAILP ." (7) are
# figures in his reading, not letters.
NO11_MERGE = [("8^dot 7", "NULL"), ("G HASH", "NULL"), ("DOT 3 1 DOT", "NULL"), ("SL3 NULL 3 1", "SL3 NULL NULL"),
              ("DOT 8 O DOT", "NUM"), ("DOT TAILP DOT", "NUM")]
# Shape and count identifications (his column, his count / our count):
NO11_KEY = {
    "II": "a",        # A 'll' 30 / 30
    "D": "aq",        # A 'δ' 7 + Q 'd.' 2 / 9
    "6": "uv",        # U/V '6=' 7 / 7
    "O PLUS": "d",    # D 'o+' 12: our "O PLUS" (two-token signs are taken whole by the alignment)
    "ODAG": "h",      # H 'ϭ‡' 8 / 10
    "RHO": "o",       # O 'φo' 9 / 7
    "OSTEM": "i",     # I 'φ.' 4 / 4
    "C^tick": "p",
    "OBAR": "aiz",    # A 'o-' 5 + I 'o-' 11 + Z 'o-' 3 / 17
    "EQ": "b", "SL2": "c", "ODOT": "c",
    "PLUS O": "e", "S": "e", "QB2": "e", "QB3": "e",   # E '+o' 23 (our PLUS O), 'S' 18, 'q‡' 13, 'q‡‡' 2
    "N": "f", "2": "g", "7": "g", "3": "i", "Q": "is",  # I 'q.' 4 + S 'q.' 5 / 10
    "HASH3": "l", "REV3": "l", "P": "l", "NX": "m", "4": "m", "OMEGA": "n", "PI": "n",
    "TAU": "o", "PERP": "o", "C": "p", "8": "p", "ZX": "r", "QB1": "rd",  # R + D double-barred q 9 + 5 / 15
    "B": "s", "DAG2": "trp",  # T '≠' 22 + R '±' 10 + P 'Ŧ' 3 / 33
    "HASH": "t",      # T '#' 3, after the four 'g#' nulls are taken out
    "A": "uv", "E": "uv",
    "NULL": "", "M^n": "", "SL3": "", "NUM": "",
    # D, OP, ODAG, RHO, OSTEM, C^tick, HASH were set after a first alignment (66.7% with them unidentified);
    # left unidentified: PLUS and O standing alone, G
}

# ---------------------------------------------------------------------------------------------------------
# R4794 = his "no. 5". Our transcription: transcripts/r4794.txt (24 Sept). His key: key_no05_R4794.png.
# The number codes 44, 26, 67, 74 are figures in his reading; his supplied [d'] and [n] are left out.
R4794_SEGMENTS = [
    (" ".join(l for l in open(__file__.replace("verify_lasry.py", "transcripts/r4794.txt"), encoding="utf-8")
              .read().splitlines() if not l.startswith("#")),
     "Di alcuni pezzi i artigliaria 44 di 26 Le Signorie Vostre come so faranno si governin con prudentia "
     "perché ancho 67 ha qualche impressio non è la mente che Vostre Signorie s'intendino col presente 74 di 26"),
]
R4794_MERGE = [("4 4", "CODE"), ("2 6", "CODE"), ("6 7", "CODE"), ("7 4", "CODE")]
R4794_KEY = {
    "M": "a", "C.": "a", "I": "a",       # A 'ɱ' 7 / 7, 'C.' 3 / 3, 'ꟷI' 1 / 1
    "U.": "c",                           # C 'Ʊ.' 8 / 9
    "N.": "d", "W.": "d",                # D 'ɑ.' 4 / 4, 'W.' 1 / 1
    "LAM": "e", "R3": "e", "C": "e",     # E 'Λ' 11 / 12, 'Э' 9 / 9, 'C' 1 / 1
    "RC": "f", "O": "g", "7": "g",       # F 'Ↄ' 1; G 'O' 3, '7' 1
    "J": "i", "D": "i", "T": "i",        # I 'Ͻ-' 16 / 16, 'd' 3 / 3, 'T' 2 / 2
    "L": "l", "P": "l", "A": "m",        # L '⊥' 3 / 2, 'þ' 3 / 3; M 'α' 2 / ours 11
    "S": "n", "K": "n",                  # N 'ʊ̄' 16 / 16, '⊢' 2 / 3
    "LAM.": "o", "R": "o", "SH": "o",    # O 'Λ.' 11 / 10, 'Я' 2 / 2, 'Ш' 1 / 1
    "V.": "p", "7.": "q", "E.": "s", "H4": "s", "E3": "t", "PI": "uv", "B": "z", "TH": "z",
    "CODE": "",
    # not matched by shape: N (4), LT (2), G (2), U (1), and our A (11) against his M 'α' (2)
}
# His table has no H and no R column, though his reading has h 7 times and r 11 times; our A (11) aligns with r
# every time, N (4) with h. With those two values added (and nothing else), r4794b:
R4794_KEY_B = dict(R4794_KEY, A="r", N="h")


PIECES = {"r4794": (R4794_SEGMENTS, R4794_KEY, R4794_MERGE), "r4794b": (R4794_SEGMENTS, R4794_KEY_B, R4794_MERGE), "no17": (NO17_SEGMENTS, NO17_KEY, []), "no11": (NO11_SEGMENTS, NO11_KEY, NO11_MERGE)}

IGNORE = {"DOT"}  # points around numerals, not substitution signs


def letters(s):
    s = unicodedata.normalize("NFD", s.lower())
    return [c for c in s if "a" <= c <= "z"]


def align(tokens, key, plain):
    """Edit-distance alignment of token readings (sets of letters, or a multi-letter code) to plain letters."""
    # expand codes ("che") into one unit that consumes len(code) plain letters
    n, m = len(tokens), len(plain)
    INF = 10 ** 9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0] = list(range(m + 1))
    for i in range(1, n + 1):
        D[i][0] = i
        B[i][0] = "del"
    for j in range(1, m + 1):
        B[0][j] = "ins"
    for i in range(1, n + 1):
        t = tokens[i - 1]
        val = key.get(t)
        for j in range(1, m + 1):
            best, how = D[i - 1][j] + 1, "del"          # our token with no plaintext letter (null / extra)
            if D[i][j - 1] + 1 < best:
                best, how = D[i][j - 1] + 1, "ins"      # his letter with no token of ours
            if val and len(val) > 1 and val not in ("mo", "ov") and j >= len(val):
                c = 0 if "".join(plain[j - len(val):j]) == val else 1
                if D[i - 1][j - len(val)] + c < best:
                    best, how = D[i - 1][j - len(val)] + c, ("code", c)
            c = 0.5 if val is None else (0 if plain[j - 1] in val else 1)
            if D[i - 1][j - 1] + c < best:
                best, how = D[i - 1][j - 1] + c, ("sub", c)
            pair = " ".join(tokens[i - 2:i]) if i >= 2 else None
            if pair in key and D[i - 2][j - 1] + (0 if plain[j - 1] in key[pair] else 1) < best:
                best, how = D[i - 2][j - 1] + (0 if plain[j - 1] in key[pair] else 1), ("pair", 0)
            D[i][j], B[i][j] = best, how
    i, j, out = n, m, []
    while i > 0 or j > 0:
        how = B[i][j]
        if how == "del":
            out.append((tokens[i - 1], None)); i -= 1
        elif how == "ins":
            out.append((None, plain[j - 1])); j -= 1
        elif how[0] == "pair":
            out.append((tokens[i - 2] + " " + tokens[i - 1], plain[j - 1])); i -= 2; j -= 1
        elif how[0] == "code":
            L = len(key[tokens[i - 1]])
            out.append((tokens[i - 1], "".join(plain[j - L:j]))); i -= 1; j -= L
        else:
            out.append((tokens[i - 1], plain[j - 1])); i -= 1; j -= 1
    return out[::-1]


def run(name):
    segs, key, merges = PIECES[name]
    tot = agree = nomap = 0
    extra, missing, bad = [], [], []
    for toks, his in segs:
        toks = " " + toks + " "
        for a, b in merges:
            toks = toks.replace(" " + a + " ", " " + b + " ")
        toks = re.sub(r"PLUS O", "PO", toks) if "PO" in key else toks
        toks = [t for t in toks.split() if t not in IGNORE and key.get(t) != ""]
        al = align(toks, key, letters(his))
        for t, p in al:
            if t is None:
                missing.append(p)
                continue
            tot += 1
            v = key.get(t)
            if p is None:
                extra.append(t)
            elif v is None:
                nomap += 1
                bad.append((t, "?", p))
            elif p in v or p == v:
                agree += 1
            else:
                bad.append((t, v, p))
        print("  ours: " + " ".join(key.get(t, "?") if t else "-" for t, p in al))
        print("  his : " + " ".join(p if p else "-" for t, p in al))
    print(f"{name}: {tot} tokens; {agree} agree ({100 * agree / tot:.1f}%); {len(bad)} read differently "
          f"({nomap} with no sign in his table); {len(extra)} of ours have no letter in his reading; "
          f"{len(missing)} of his letters have no token of ours")
    if bad:
        print("  differences (our sign, his key, his reading):", bad)
    if extra:
        print("  ours without a letter:", extra)
    return tot, agree


if __name__ == "__main__":
    for nm in [a for a in sys.argv[1:] if a in PIECES] or ([] if sys.argv[1:] else PIECES):
        run(nm)


# ---------------------------------------------------------------------------------------------------------
# No. 20 (R4808): George Lasry's own CTTS transcription and key are in targets/siena2023/. Our independent
# transcription (agent C, 24 Sept) is in targets/siena2023/project_attempt/no20.tok, in different sign names.
# Check: align our token stream with the letters of his reading (R4808_reading.txt, bracketed name signs = '#'),
# re-estimating our-sign -> letter by majority (EM, 8 rounds, one- and two-token signs, nulls allowed), and
# report how consistently our transcription carries his reading: the share of our tokens whose aligned letter is
# the majority letter of their sign. Start: his key.txt values for the sign names that are written the same in
# both transcriptions (6 8 p = e, 7 9 f = i, 2 = c, 3 = f, 4 = b, h r = o, S = l, "f a" = o, "f o^n" = t).
def em20(rounds=8, merged=False, control=False):
    """merged=True lets a sign of ours stand for two letters (>= 20% each): our names merge some of his signs."""
    import collections, pathlib
    root = pathlib.Path(__file__).resolve().parents[1] / "siena2023"
    toks = [t for t in (root / "project_attempt" / "no20.tok").read_text(encoding="utf-8").split()
            if not t.startswith("[")]
    toks = toks[7:] if toks[:7] == "Q^o p z c b r h".split() else toks
    txt = (root / "R4808_reading.txt").read_text(encoding="utf-8")
    body = txt[txt.index("Secundo"):txt.index("Scriptum Perusii")]
    if control:  # control: the same length of his no. 23 reading, a wrong plaintext for this cipher
        other = (root / "R4811_reading.txt").read_text(encoding="utf-8")
        other = other[other.index("In primis"):]
        body = other[:len(body)]
    body = re.sub(r"\[[^\]]*\]", " # ", body)
    plain = [c for c in letters(body.replace("#", "zzhash"))]
    plain = list("".join(plain).replace("zzhash", "#"))
    key = {"6": "e", "8": "e", "p": "e", "7": "i", "9": "i", "f": "i", "2": "c", "3": "f", "4": "b",
           "h": "o", "r": "o", "S": "l", "f a": "o", "f o^n": "t", "o o": "p"}
    for r in range(rounds):
        al = align(toks, key, plain)
        cnt = collections.defaultdict(collections.Counter)
        for t, p in al:
            if t is not None:
                cnt[t][p or "-"] += 1
        new = {}
        for t, c in cnt.items():
            tot = sum(c.values())
            ls = [l for l, n in c.most_common(2 if merged else 1) if l != "-" and n >= 0.2 * tot]
            if ls:
                new[t] = "".join(ls)
        # keep the two-token groups of the start key ("o o" = his o-o, P: our agents did not record the
        # joining stroke)
        for k in ("f a", "f o^n", "o o"):
            new[k] = key[k]
        agree = sum(1 for t, p in al if t is not None and p is not None and p in key.get(t, "") )
        ntok = sum(1 for t, p in al if t is not None)
        print(f"  round {r}: {agree}/{ntok} tokens carry the letter their sign gives ({100 * agree / ntok:.1f}%)")
        key = new
    print("  our sign -> letters it aligned to:")
    for t, c in sorted(cnt.items(), key=lambda x: -sum(x[1].values())):
        print("   ", t, dict(c.most_common(4)))
    return al


if __name__ == "__main__" and "no20" in sys.argv[1:]:
    print("no20, one letter per sign of ours:")
    em20()
    print("no20, up to two letters per sign of ours:")
    em20(merged=True)
    print("control (no. 23 plaintext against our no. 20 transcription), one / two letters per sign:")
    em20(control=True)
    em20(merged=True, control=True)
