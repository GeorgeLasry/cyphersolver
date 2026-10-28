"""GPT-2 rescoring of the n-gram decode: coordinate ascent over uncertain slots.

For each slot with more than one candidate, every candidate is put into the running text (a window
of about 40 words of context on each side) and scored with GPT-2; the slot takes the best
(LM score + prior). Two sweeps over the text.
"""
import sys, os, re, math, torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import decode as D

MODEL = os.environ.get('GPT', 'gpt2-medium')
tok = GPT2TokenizerFast.from_pretrained(MODEL)
gpt = GPT2LMHeadModel.from_pretrained(MODEL).eval()
torch.set_num_threads(os.cpu_count())


@torch.no_grad()
def score(texts):
    enc = tok([tok.bos_token + t for t in texts], return_tensors='pt', padding=True)
    out = gpt(**enc).logits.log_softmax(-1)
    ids, mask = enc.input_ids, enc.attention_mask
    lp = out[:, :-1].gather(2, ids[:, 1:, None])[..., 0] * mask[:, 1:]
    return lp.sum(1).tolist()


tok.pad_token = tok.eos_token
tok.padding_side = 'right'


def rescore(words, opts, prior_w=1.0, sweeps=2, ctx=30, k=15):
    words = list(words)
    for _ in range(sweeps):
        for i, op in enumerate(opts):
            if len(op) < 2:
                continue
            cand = op[:k]
            lo, hi = max(0, i - ctx), min(len(words), i + ctx // 2)
            texts = [' '.join(words[lo:i] + [w] + words[i + 1:hi]) for w, _ in cand]
            s = score(texts)
            best = max(range(len(cand)), key=lambda j: s[j] + prior_w * cand[j][1])
            words[i] = cand[best][0]
    return words


def run(lines, M):
    sl = [s for line in lines for s in D.slots(line)]
    words = []
    for line in lines:
        words += D.beam(D.slots(line), M)
    opts = [D.options(s, M) for s in sl]
    return rescore(words, opts)


if __name__ == '__main__':
    CHU = D.CHU
    wb = [os.path.join(CHU, 'wordbanks', f) for f in ('wordbank', 'wordbank.clean2', 'wordbank.miro')]
    if sys.argv[1] == 'eval':
        M = D.build('1078', wb)
        ct = open(os.path.join(CHU, 'data', 'eval', 'ciphertext.txt'), encoding='utf-8').read().splitlines()
        gold = open(os.path.join(CHU, 'data', 'eval', 'plaintext.txt'), encoding='utf-8').read()
        out = run(ct, M)
        g = re.findall(r"[A-Za-z?]+", gold.lower())
        print('accuracy %.3f' % (1 - D.edit_distance(out, g) / len(g)))
        print(' '.join(out))
    else:
        M = D.build(sys.argv[3], wb)
        lines = [l for l in open(sys.argv[2], encoding='utf-8') if D.TOK.search(l)]
        print(' '.join(run(lines, M)))
