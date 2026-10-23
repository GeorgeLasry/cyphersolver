"""b16: per-sentence view of _check_reading's judgement (holes marked *), failing sentences only unless -a.
python b16_sents.py <reading> [lang] [-a]"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'docs'))
import _check_reading as C
args = [a for a in sys.argv[1:] if a != '-a']; allv = '-a' in sys.argv
raw = open(args[0], encoding='utf-8').read(); lang = args[1] if len(args) > 1 else 'es'
text = C.CODE.sub(' CODEWORD ', C.clean_text(raw)); lex = C.lexicon(lang)
sys.stdout.reconfigure(encoding='utf-8')
for s in C.sentences(text):
    ws = [(w, g) for tok in s for w, g in C.words_of(tok)]
    h = [g or (w != 'codeword' and w not in lex) for w, g in ws]
    ok = sum(h) <= max(1, len(ws) // 10)
    if allv or not ok:
        print(('OK ' if ok else 'XX ') + f'{sum(h)}/{len(ws)} ' + ' '.join(w + ('*' if x else '') for (w, g), x in zip(ws, h)))
