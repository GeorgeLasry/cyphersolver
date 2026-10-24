"""Latin word unigram + bigram counts from the repo's la-gutenberg corpus. Letters kept as printed (u/v, i/j both allowed),
with a j->i copy so either spelling fits; Horace tags that W. is known to use are added."""
import re, sys, pickle, collections
text = open(sys.argv[1], encoding='utf-8', errors='replace').read().lower()
text = re.sub(r"[àáâä]", "a", text); text = re.sub(r"[èéêë]", "e", text); text = re.sub(r"[ìíîï]", "i", text)
text = re.sub(r"[òóôö]", "o", text); text = re.sub(r"[ùúûü]", "u", text)
words = re.findall(r"[a-z]+", text)
uni = collections.Counter(words); bi = collections.Counter(zip(words, words[1:]))
for w, c in list(uni.items()):
    if 'j' in w: uni[w.replace('j', 'i')] += c
    if 'v' in w: uni[w.replace('v', 'u')] += c // 2
print("tokens", len(words), "types", len(uni))
extra = "qui fit maecenas ut nemo quam sibi sortem conamur tenues grandia dum pudor quid dignum tanto feret hic promissor hiatu parturient montes nascetur ridiculus mus horatius horatii flaccus carmina sermones satirae epistulae".split()
for w in extra:
    if uni[w] < 30: uni[w] = 30
pickle.dump((uni, bi), open("lm_la.pkl", "wb"))
print("latin vocab", len(uni))
