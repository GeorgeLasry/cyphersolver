"""Build word unigram + bigram counts from the repo's en-gutenberg corpus; add Oxford/legal/name vocabulary."""
import re, sys, pickle, collections
src = sys.argv[1]
text = open(src, encoding='utf-8', errors='replace').read().lower()
# possessives: "conington's" -> "coningtons"  (W. wrote CONINGTONS LECTURES)
text = re.sub(r"(\w)['\u2019]s\b", r"\1s", text)
words = re.findall(r"[a-z]+", text)
uni = collections.Counter(words)
bi = collections.Counter(zip(words, words[1:]))
print("tokens", len(words), "types", len(uni), "bigram types", len(bi))
# curated additions (count ~ a moderately common word in 3M tokens)
extra = """conington coningtons jowett jowetts shirley shirleys hertford balliol oxford oxon horace juvenal virgil homer plato
satires satire motto mottoes mottos newdigate gaisford craven ireland latin greek verse verses essay essays prize prizes
scholarship scholarships exhibition exhibitioner examination examinations examiners examiner examined examine lectures lecture lectured
tutor tutors proctor proctors dean warden provost rector principal fellow fellows fellowship commem commemoration convocation
congregation collections schools moderations mods greats viva undergraduate undergraduates freshman commoner commoners scholar scholars
demy servitor bursar chapel quad gaudy eights torpids term terms michaelmas hilary trinity easter vacation vac matriculated matriculation
residence rusticated gated sconced plucked honours divinity rudiments responsions smalls littlego degree bachelor
dodgson worcester wadham oriel merton magdalen exeter lincoln queens jesus pembroke corpus brasenose university johns wyndham worsley
stanley liddell pusey keble newman ruskin arnold clough sellar chancellor chancellors vice
deposition affidavit witness oath sworn declare declaration testimony evidence perjury forgery libel slander plagiarism authorship author
sum summer repeated candidate candidates adopted disclosed previously posted holidays christian anonymous anonymously pseudonym
hall college colleges party garden cap gown mortarboard tassel bonfire wine wines breakfast supper rooms staircase porter lodge
maecenas qui fit nemo ut
cambridge eton harrow rugby winchester westminster charterhouse shrewsbury
england london standard times paper advertisement column communication intelligible inst
died dying dead death deathbed will codicil executor executors legacy heir heirs bequest
xamn xamination examn exam exams examd xn xtian xt xmas schol scholp coll colls univ undergrad lect lects prof mem memb sec secy vol pp
moderations collections responsions divinity schools greats mods smalls littlego viva
michaelmas hilary lent easter trinity act long vac vacation
persius aeschylus sophocles euripides aristophanes thucydides herodotus livy tacitus cicero lucretius catullus propertius ovid pindar theocritus
ireland craven hertford gaisford newdigate chancellors latin greek english essay poem verse elegiacs hexameters iambics prose composition
proxime accessit honourable mention first second third class fourth pass plucked gulfed
""".split()
for w in extra:
    if uni[w] < 40: uni[w] = 40
pickle.dump((uni, bi), open("lm.pkl", "wb"))
with open("vocab.tsv", "w", encoding="utf-8") as f:
    for w, c in uni.most_common():
        f.write(f"{w}\t{c}\n")
print("vocab written", len(uni))
