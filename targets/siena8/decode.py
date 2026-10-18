"""No. 8 (R4797): apply the key rebuilt from the contemporary decipherment on the same sheet to the slip.
Usage: python targets/siena8/decode.py   (prints each cipher run deciphered, beside the memorandum's words)"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
KEY = {'T': 'e', 'z': 'e', '2': 'a', '5': 'a', 'Z': 'o', 'F': 'f', 'W': 'r', 'L': 'l', '+': 'c', 'c': 'h',
       'Y': 'i', 'P': 'p', 'Q': 't', 'N': 'g', 'PHI': 'n', '7': 'd', '9': 'u', 'I': 'm', 'S': 's', 'q': 'q',
       'U': 'u', 'DM': '[duca di Milano]', 'VN': '[Viniziani]'}
# the memorandum's last paragraph, run by run (clear catchwords of the slip left out)
MEMO = ["le|ggiere e capitagli e legha fral duca di Milano el marchese di Ferrara a fa|re",
        "a Viniziani e sua legha",
        "el duca di Milano aveva dato la donna Biancha a misser Leonello figlolo del marchese",
        "e no puo manchare che questo udrete grandissimi facti"]
def runs():
    return [l.split() for l in (HERE / 'transcripts' / 'no08.tok').read_text(encoding='utf-8').splitlines() if l.strip()]
def decode(toks):
    return ''.join(KEY.get(t, '?') for t in toks)
if __name__ == '__main__':
    n = 0
    for toks, memo in zip(runs(), MEMO):
        n += len(toks)
        print(f'{len(toks):3d} signs  cipher: {decode(toks)}\n            memo:   {memo}\n')
    print('cipher signs:', n, '| distinct:', len({t for r in runs() for t in r}))
