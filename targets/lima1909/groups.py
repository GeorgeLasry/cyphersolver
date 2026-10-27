"""Venceslau de Lima's code telegrams to King Manuel II, Nov-Dec 1909 (ANTT PT/TT/CAM/M09, catalogue 409).

    python groups.py        writes code_values.tsv; the printed output is kept in groups_output.txt

T holds the eight coded telegrams strip line by strip line: clear words as strings, and every code group as
(group, value, flag, note), where the value is the pencil gloss the receiver wrote above the group (the decode of
the time). Flags: '' gloss clear; '?' gloss or group doubtful, used in the reading with a mark; 'x' no usable gloss,
not read; 'ours' no gloss on this occurrence, value ours (from another occurrence or the context). A trailing '-' or
leading '-' on a value marks our split of one glossed word over two groups.

The script (standard library only) checks the groups against the *_transcription.txt files, writes
code_values.tsv, and runs the controls: taxed word counts, consistency of repeated groups, the one-part/two-part
order test, and a comparison with the codes of the sibling folders.
"""
import collections, pathlib, random, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent

T = {
 'm0001': [  # Lisbon -> Madrid (Palacio Real), 12 Nov 1909, handwritten Spanish palace form; clear with 4 groups
  ["Reitero minhas felicitações á Vossa Magestade pelo caloroso acolhimento ahi recebido e que entre nos tem "
   "produzido os amais grata impressão",
   ("05764", "Tudo", "?", "first figure may be read s or 0"), ("21269", "continua sem novidade", "", ""),
   ("80054", "Escrevo", "?", "fourth figure unclear"), ("99924", "Windsor", "", ""),
   "beijo as mãos a Vossa Magestade. Wenceslau de Lima."]],
 'm0005': [  # Lisbon -> Paris, no. 425, 48 words, 30 Nov 1909, 12.30 am
  [("33453", "Confidencial", "", ""), ("10887", "paragem", "", ""), ("63900", "Bussaco", "", ""),
   ("40848", "teve", "", ""), ("41024", "inconveniente", "", ""), ("04", ",", "", ""), ("10353", "por isso", "", ""),
   ("52854", "insis-", "", ""), ("98828", "-to", "", ""), ("94794", "vantagem", "?", "third figure overwritten"),
   ("57624", "vinda", "", ""), ("50808", "directa", "", ""), ("66266", "sah-", "", ""),
   ("781??", "-indo", "?", "group cut at the strip edge")],
  [("94243", "d'ahi", "", ""), ("36467", "no", "", ""), ("41966", "rapido", "", ""), ("43243", "da", "", ""),
   ("42277", "noite", "", ""), ("06", ".", "", ""), ("89274", "Vasconcellos", "", ""), ("45433", "Porto", "", ""),
   ("01794", "insta", "", ""), ("46523", "pela", "", ""), ("79456", "resposta", "", ""), ("28573", "que", "", ""),
   ("99211", "muito", "", ""), ("75137", "peço", "", "")],
  [("00327", "a", "", ""), ("25584", "V. M.", "", ""), "BEIJO AS MAOS DE VOSSA NAGESTADE .= WENCESLAU DE [LIMA]"]],
 'm0007': [  # Lisbon -> Paris, no. 43, 122 words, 2 Dec 1909, 12.55 am, via Eastern
  ["= AGRADECO O TELEGRAMMA DE VOSSA MAJESTADE E SUA CONCORDANCIA COM"],
  ["OS ALVITRES PROPOSTOS", ("70606", "hora", "", ""), ("28140", "chegada", "", ""), ("91731", "Lisbôa", "", ""),
   ("80124", "1 hora", "", ""), ("93148", "e", "", ""), ("64124", "um", "", ""), ("82633", "quarto", "", ""),
   ("43243", "da", "", ""), ("11598", "tarde", "", ""), ("06", ".", "", "")],
  [("03481", "mais cêdo", "?", "light pencil"), ("34878", "terá", "", "light pencil"),
   ("41024", "inconveniente", "", "light pencil"), ("46523", "pela", "", ""), ("73027", "passagem", "", ""),
   ("01748", "em", "", ""), ("06777", "Pampilhosa", "", ""), ("93148", "e", "", ""), ("49113", "Coimbra", "", ""),
   ("49600", "cêdo", "", ""), ("05123", "de", "", ""), ("99251", "mais", "", ""), ("06", ".", "", "")],
  [("20481", "mais tarde", "", ""), ("58538", "torna-", "", "gloss 'tornaria' spans 58538 and 28787"),
   ("28787", "-ria", "", "same split as chega-ria in m0011"), ("47841", "a marcha", "", ""),
   ("41024", "inconveniente-", "", ""), ("67031", "-mente", "", ""), ("35184", "lenta", "", ""), ("06", ".", "", ""),
   "MUITO AGRADECERIA VOSSA MAJESTADE"],
  ["[M]E DISSESSE SE SE DIGNA RECEBER COMPRIMENTOS A ENTRADA EM PORTUGAL EM VILLAR"],
  ["FORMOSO ONDE MUITO DESEJAM PRESTAR LH OS DEPOIS NENHUNS OUTROS TERA POR SER DE"],
  ["NOITE E PARA PODER DESCANCAR ATE A PAMPILHOSA ONDE CHEGA AS 8 HORAS DA MANHA"],
  ["ALMOCO ENTRE SANTAREM E LISBOA", ("02183", "Das", "", ""),
   ("50667", "[?]", "x", "circled; the receiver wrote '(? uma palavra indecifravel)'"), ("93148", "e", "", ""),
   ("87231", "meia", "", ""), ("18507", "ás", "", ""), ("80124", "uma hora", "", ""), ("93148", "e", "", "")],
  [("64124", "um", "", ""), ("82633", "quarto", "", ""), "BEIJO AS MAOS DE VOSSA MAGESTADE = WENCESLAU DE LIMA"]],
 'm0009': [  # Lisbon -> Paris, no. 141, 68 words, 30 Nov 1909, 10.30 am, via Eastern
  [("13341", "Falta de", "?", "perhaps a garbled 10341 falta"), ("84456", "resposta ao telegramma", "", ""),
   ("05123", "de", "", ""), ("19586", "sabbado", "", ""), ("84656", "relativo", "", ""),
   ("86853", "comboios", "", ""), ("05123", "de", "", ""), ("22596", "regresso", "", ""),
   ("68520", "causa", "", ""), ("48367", "o maior", "", "")],
  [("63178", "transtorno", "", ""), ("04184", "Lembro", "", ""), ("28573", "que", "", ""),
   ("01953", "depois de amanhã", "", ""), ("07658", "é", "", ""), ("25367", "o", "", ""), ("20768", "dia", "", ""),
   ("43243", "da", "", ""), ("88117", "partida", "", ""), ("05123", "de", "", "")],
  [("25584", "V. M.", "", ""), ("93148", "e", "", ""), ("62021", "nada", "", ""), ("94201", "está", "", ""),
   ("56911", "fixado", "", ""), ("70283", "por", "?", ""), ("10341", "falta", "", ""), ("60201", "essa", "", ""),
   ("76224", "indicação", "", ""), ("28573", "que", "", "")],
  [("99211", "muito", "", ""), ("75137", "peço", "", ""), ("45853", "com toda urgencia", "", ""),
   ("06", ".", "", ""), ("89274", "Vasconcellos", "", ""), ("45433", "Porto", "", ""), ("40848", "tem", "", ""),
   ("02848", "telegraphado", "", ""), ("18703", "[comp..são?]", "x", "gloss unclear"),
   ("10586", "[Th..?]", "x", "gloss unclear")],
  [("01021", "na", "", ""), ("24686", "hypothese", "", ""), ("41966", "rapido", "", ""),
   ("24357", "Norte", "", ""), ("15771", "mas", "?", ""), ("10341", "falta", "", ""), ("91033", "decisão", "", ""),
   "DE VOSSA MAGESTADE A"],
  ["QUEM BEIJM AS MAOS .= WENCESLAU DE LIMA .="]],
 'm0011': [  # Lisbon -> Paris, no. 105, 113 words, 27 Nov 1909, 5.25 pm; m0011 lines 1-3, m0012 lines 4-9
  [("01748", "Em", "?", "margin gloss 'Em combina[ção]' over 01748 and 78853"),
   ("78853", "combinação", "?", "end of the margin gloss faint"), ("68173", "com o", "", ""),
   ("45433", "Porto", "", ""), ("93148", "e", "", ""), ("65048", "Serpa", "", ""), ("01287", "assent-", "", ""),
   ("83437", "-ámos", "", ""), ("29573", "que o", "?", "28573 que, garbled?"),
   ("04481", "mais conveniente", "?", ""), ("40048", "seria", "", ""), ("64708", "tomar", "", ""),
   ("55977", "ahi", "", "")],
  [("25367", "o", "", ""), ("595191", "[?]", "x", "six figures, underlined, no gloss: garbled"),
   ("53243", "da noite", "", ""), ("67218", "7 horas", "", ""), ("50633", "40", "", ""),
   ("53561", "minutos", "", ""), ("47853", "com toda", "", ""), ("50763", "commodidade", "", ""),
   ("23628", "tam", "", ""), ("26430", "bem", "", ""), ("11847", "ou", "", ""), ("32101", "melhor", "", "")],
  [("28573", "que", "", ""), ("24928", "Sud-Express", "", ""), ("93148", "e", "", ""), ("55504", "vir", "", ""),
   ("61407", "até", "", ""), ("10231", "Medi-", "", "gloss 'medi'"),
   ("01021", "-na", "", "gloss 'na': Medi-na"), ("70007", "onde", "", ""), ("34878", "teria", "", ""),
   ("86853", "comboio", "", ""), ("9581", "especial", "?", "four figures, underlined: 95181 mutilated")],
  [("28573", "que", "", ""), ("26140", "chega-", "", ""), ("28787", "-ria", "", ""), ("00327", "a", "", ""),
   ("91731", "Lisbôa", "", ""), ("36347", "ás", "", ""), ("50167", "11 horas", "", ""),
   ("87311", "manhã", "", ""), ("11847", "ou", "", ""), ("20481", "mais tarde", "", ""),
   ("70836", "se assim", "", ""), ("22503", "convier", "", "")],
  [("06", ".", "", ""), ("53558", "Supprim-", "", ""), ("18166", "-ia", "", ""), ("61836", "se", "", ""),
   ("32288", "d'esta", "", ""), ("91941", "forma", "", ""), ("10887", "paragem", "", ""), ("36467", "no", "", ""),
   ("34470", "caminho", "", ""), ("01748", "em", "", ""), ("30301", "Luso", "", "")],
  [("87054", "incommoda", "", ""), ("93148", "e", "", ""), ("05123", "de", "", ""),
   ("38951", "mau effeito", "", ""), ("06", ".", "", ""), ("93048", "serviço", "", ""), ("46523", "pela", "", ""),
   ("9194?", "forma", "?", "last figure under a struck gloss; 91941?"), ("28573", "que", "", ""),
   ("95224", "indico", "", ""), ("99251", "mais", "", ""), ("26430", "bem", "", ""),
   ("79853", "combinado", "", "")],
  [("06", ".", "", ""), ("85178", "[Tratando?]", "x", "gloss faint"), ("70706", "[rendoso?]", "x", "gloss faint"),
   ("52763", "commodo", "", ""), ("01748", "em", "", ""),
   ("48696", "Hen[daya?]", "?", "gloss 'Hen..', most likely Hendaye on the Paris-Medina line"),
   ("43243", "[dep..?]", "x", "gloss looks like 'dep..'; 43243 is 'da' four times elsewhere"),
   ("95940", "já", "", ""), ("36347", "ás", "", ""), ("79057", "8 horas", "", ""), ("93148", "e", "", ""),
   ("64628", "tanto", "?", ""), ("93148", "e", "", "")],
  [("01748", "em", "", ""), ("10231", "Medi-", "", ""), ("01021", "-na", "", ""), ("45967", "para o", "", ""),
   ("75098", "trem", "", ""), ("95181", "especial", "", ""), ("73693", "perto", "", ""),
   ("67218", "7 horas", "", ""), ("53243", "da noite", "", ""), ("06", ".", "", ""),
   ("19977", "aguardando", "?", "gloss partly faint"), ("25584", "V. M.", "", "")],
  [("76777", "para", "", ""), ("80063", "dar ordens", "", ""), ("74573", "que são", "", ""),
   ("93094", "urgentes", "", ""), "= W . DE LIMA ,-"]],
 'm0014': [  # Lisbon -> Paris, no. 25, 49 words, 28 Nov 1909, 12.30 pm
  [("04184", "Lembro", "", ""), ("00327", "a", "", ""), ("25584", "V. M.", "", ""), ("28573", "que", "", ""),
   ("76958", "tendo", "", ""), ("19073", "Pres. Republica", "", ""), ("85243", "dado", "", ""),
   ("93186", "G. C. Legião", "", "Grã-Cruz da Legião [de Honra]"), ("00327", "a", "", ""),
   ("35530", "Bocage", "", ""), ("64156", "importar", "", ""), ("31158", "ser", "", "")],
  [("48627", "amavel", "", ""), ("86083", "com", "", ""), ("06930", "Bri-", "", ""), ("88667", "-and", "", ""),
   ("93148", "e", "", ""), ("29153", "não deixar", "", ""), ("82291", "má impressão", "", ""),
   ("28428", "sobretudo", "", "gloss 'sobre tudo'"), ("71171", "não haver", "", ""),
   ("14478", "desigualdade", "", ""), ("01748", "em", "", ""), ("62656", "relação", "", "")],
  [("28997", "ao que", "", ""), ("61836", "se", "", ""), ("96791", "fez", "", ""), ("01748", "em", "", ""),
   ("15164", "Inglaterra", "", ""), ("93148", "e", "", ""), ("14556", "Hespanha", "", ""),
   "BEIJO AS MAOS DE VCSSA MAGESTADE"],
  [". = WENCESLAU DE LIMA"]],
 'm0018': [  # Lisbon -> Paris, no. 24, 110 words, 28 Nov 1909, 12.25 pm; m0018 lines 1-5, m0016 lines 6-8
  [("81958", "Tendo sido", "", ""), ("76628", "tão", "", ""), ("45187", "affect[uoso]", "", ""),
   ("76204", "nosso", "", ""), ("93397", "acolhimento", "", ""), ("01748", "em", "", ""),
   ("75896", "França", "", ""), ("55887", "parece", "", ""), ("52483", "conveniente", "", ""),
   ("65538", "tornar", "", ""), ("45930", "brinde", "", ""), ("21344", "jantar", "?", "gloss unclear")],
  [("99251", "mais", "", ""), ("47050", "caloroso", "", ""), ("06", ".", "", ""), ("29967", "Por isso", "", ""),
   ("79373", "convem", "", ""), ("36467", "no", "", ""), ("88163", "primeiro", "", ""),
   ("23553", "periodo", "", ""), ("00327", "a", "", ""), ("38806", "seguir", "", ""), ("00327", "a", "", ""),
   ("37608", "sympathia", "", "")],
  [("34737", "accrescentar", "", ""), ("93148", "e", "", ""), ("38437", "amizade", "", ""),
   ("36467", "no", "", ""), ("70806", "segundo", "", ""), ("23553", "periodo", "", ""), ("00327", "a", "", ""),
   ("38806", "seguir", "", ""), ("00327", "a", "", ""), ("69958", "tend-", "", "gloss 'tend'"),
   ("66931", "-es", "", "gloss 'es'"), ("78401", "feito", "", "")],
  [("44118", "dizer", "", ""), ("95523", "pelo", "", ""), ("93397", "acolhimento", "", ""),
   ("63573", "que nos", "", ""), ("72998", "dispensa", "", ""), ("00327", "a", "", ""), ("36021", "nação", "", ""),
   ("78896", "franceza", "", ""), ("01021", "na", "", ""), ("84798", "sua", "", ""), ("02256", "grande", "", ""),
   ("93148", "e", "", "")],
  [("11430", "bella", "", ""), ("32410", "capital", "", ""), ("01021", "na", "", ""), ("84798", "sua", "", ""),
   ("55974", "intellectual", "", ""), ("96887", "Paris", "", ""), ("06", ".", "", ""), ("96047", "ao", "", ""),
   ("18878", "3º", "", ""), ("23553", "periodo", "", ""), ("00327", "a", "", ""), ("38806", "seguir", "", "")],
  [("14761", "entre", "", ""), ("67433", "Portugal", "", ""), ("93148", "e", "", ""), ("00327", "a", "", ""),
   ("75896", "França", "", ""), ("90974", "intercalar", "", ""), ("93148", "e", "", ""),
   ("90977", "ainda", "", ""), ("95523", "pelo", "", ""), ("76251", "maior", "", ""),
   ("33511", "estreit-", "", ""), ("05437", "-amento", "", "")],
  [("19183", "das suas", "", ""), ("62656", "relações", "", ""), ("87836", "se houver", "", ""),
   ("36467", "no", "", ""), ("45930", "brinde", "", ""), ("19073", "do P. Republica", "", ""),
   ("14723", "qualquer", "", ""), ("95583", "cousa", "", ""), ("95181", "especial", "", ""),
   ("82381", "fazer", "", ""), ("01021", "na", "", ""), ("79456", "resposta", "", "")],
  [("00327", "a", "", ""), ("12838", "devida", "", ""), ("62587", "allusão", "", ""),
   ("33125", "[?]", "x", "underlined, no gloss"), ("39998", "discreta", "", ""), ("93148", "e", "", ""),
   ("18803", "prudente", "", ""), "BEIJO AS MAOS DE VOSSA MAJESTADE"],
  ["= WENCESLAU DE LIMA ,-"]],
 'm0020': [  # Lisbon -> Paris, no. 325, 93 words (pencilled 83), 30 Nov 1909, 12.30 pm
  [("33453", "Confidencial", "", ""), ("57887", "Parece conveniente", "?", "'conveniente' in the margin; 55887 = parece"),
   ("28573", "que", "", ""), ("25584", "V. M.", "", ""), ("97904", "só", "", ""), ("00327", "a", "", ""),
   ("08396", "São", "", ""), ("50380", "Carlos", "", ""), ("01021", "na", "", ""), ("42277", "noite", "", ""),
   ("00228", "do dia", "", ""), ("43243", "da", "", ""), ("29140", "chegada", "", "28140 chegada in m0007")],
  [("06", ".", "", ""), ("83636", "[o Rojo?]", "x", "gloss read 'o Rojo', 'o Rozo' or 'o Bojo'"),
   ("71881", "me", "", ""), ("86898", "disse se", "", ""), ("05068", "inconveniencia", "?", "gloss faint"),
   ("19313", "posso", "?", "gloss 'posso' or 'pouco'"), ("51443", "contar com", "", ""),
   ("19864", "isso", "", ""), ("06", ".", "", ""), ("28628", "Tambem", "", ""), ("55887", "parece", "", ""),
   ("99251", "mais", "", ""), ("02274", "vantajoso", "?", "")],
  [("28573", "que", "", ""), ("25584", "V. M.", "", ""), ("84123", "dê", "", ""), ("12036", "recepção", "", ""),
   ("01021", "na", "", ""), ("84161", "estação", "", ""), ("55967", "para o que", "", ""),
   ("72296", "haverá", "", ""), ("07486", "sala", "", ""), ("68483", "conveniente-", "", ""),
   ("07053", "preparada", "", "gloss 'convenientemente preparada' over 68483 07053"), ("19864", "isso", "", ""),
   ("65538", "tornar-", "", "")],
  [("40817", "-á", "", ""), ("12036", "recepção", "", ""), ("99251", "mais", "", ""), ("66271", "facil", "", ""),
   ("93148", "e", "", ""), ("32101", "melhor", "", ""), ("93148", "e", "", ""),
   ("55478", "desembaraçar-", "", ""), ("40817", "-á", "", ""), ("93048", "serviço", "", ""),
   ("29140", "chegada", "", ""), ("01021", "na", "", ""), ("04053", "preparação", "", "")],
  [("10977", "Aguardo", "?", "19977 aguardando in m0011?"), ("45418", "determinação", "?", ""),
   ("25584", "V. M.", "", ""), ("99211", "muito", "", ""), ("75137", "peço", "", ""), ("25584", "V. M.", "", ""),
   ("84798", "sua", "", ""), ("79456", "resposta", "", ""), ("46523", "pela", "", ""),
   ("84727", "necessidade", "", ""), ("05123", "de", "", ""), ("70857", "ordenar", "", ""),
   ("93048", "serviço", "", "")],
  ["BEIJO AS MAOS DE VCSSA MAGESTADE .= WENCESLAU DE LIMA +"]],
}

# taxed words in the header of each Paris form (m0001 is a Madrid palace form without a count)
HEADER = {'m0005': 48, 'm0007': 122, 'm0009': 68, 'm0011': 113, 'm0014': 49, 'm0018': 110, 'm0020': 93}
HEADER_NOTE = {'m0009': "the office noted '(Correction suivra pour mot qui manque)'",
               'm0020': 'the receiver pencilled 83 above the 93'}
ADDRESS = 9  # address words, not on these faces: one constant for all forms (the only free parameter)
SHORT = {'04', '06'}  # punctuation groups: 04 comma, 06 full stop


def code(doc):
    return [it for line in T[doc] for it in line if isinstance(it, tuple)]


def clear_words(doc):
    n = 0
    for line in T[doc]:
        for it in line:
            if isinstance(it, str):
                n += sum(1 for w in it.split() if re.search(r'[^\W_]', w))
    return n


def bare(g):
    return g.rstrip('?')


def transcription_groups(doc):
    out = []
    for line in (HERE / f'{doc}_transcription.txt').read_text(encoding='utf-8').splitlines():
        if line.lstrip().startswith('#'):
            continue
        out += [t.strip('.=,') for t in line.split() if re.fullmatch(r'=?\d[\d?]{1,5}[.,]?', t)]
    return out


def norm(w):
    return ''.join(c for c in unicodedata.normalize('NFD', w.lower()) if c.isalpha())


def rank(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0] * len(xs)
    for k, i in enumerate(o):
        r[i] = k
    return r


def rho(a, b):
    ra, rb = rank(a), rank(b); n = len(a)
    return 1 - 6 * sum((x - y) ** 2 for x, y in zip(ra, rb)) / (n * (n * n - 1))


def sibling_groups(folder):
    out = []
    for f in sorted((HERE.parent / folder).glob('*_transcription.txt')):
        for line in f.read_text(encoding='utf-8').splitlines():
            if line.lstrip().startswith('#'):
                continue
            out += [t.strip('.?,=') for t in line.split() if re.fullmatch(r'=?\d{4,6}[.?,]*', t)]
    return out


if __name__ == '__main__':
    # 1. the groups in T are the groups of the transcription files
    print('1. groups.py against the transcription files')
    for doc in T:
        a = [bare(g) for g, *_ in code(doc)]
        b = [bare(g) for g in transcription_groups(doc)]
        print(f'  {doc}: {len(a)} code items, transcription {len(b)}: {"same" if a == b else "DIFFERENT"}')

    # 2. taxed word count: code items + clear words + address = header figure
    print('\n2. taxed word count (code items + clear words + address %d) against the form header' % ADDRESS)
    for doc, hdr in HEADER.items():
        c, w = len(code(doc)), clear_words(doc)
        tot = c + w + ADDRESS
        print(f'  {doc}: {c} + {w} + {ADDRESS} = {tot}, header {hdr}' + ('  match' if tot == hdr else f'  off by {hdr - tot}')
              + (f'; {HEADER_NOTE[doc]}' if doc in HEADER_NOTE else ''))

    # 3. code values
    tab = collections.defaultdict(list)
    for doc in T:
        for g, v, f, n in code(doc):
            tab[bare(g)].append((v, doc, f, n))
    rows = ['group\tvalue(s)\toccurrences\ttelegrams\tflags\tnote']
    for g in sorted(tab):
        vals = sorted(set(v for v, *_ in tab[g]))
        rows.append('\t'.join([g, ' | '.join(vals), str(len(tab[g])), ','.join(sorted(set(d for _, d, _, _ in tab[g]))),
                               ''.join(sorted(set(f[0] for _, _, f, _ in tab[g] if f))),
                               '; '.join(sorted(set(n for *_, n in tab[g] if n)))]))
    (HERE / 'code_values.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    tokens = sum(len(v) for v in tab.values())
    unread = [(g, d) for g, occ in tab.items() for v, d, f, _ in occ if f == 'x']
    print(f'\n3. code values: {len(tab)} distinct groups, {tokens} code items; written to code_values.tsv')
    print(f'  not read (flag x): {len(unread)} items, {len(set(g for g, _ in unread))} groups: '
          + ', '.join(f'{g} ({d})' for g, d in unread))
    print(f'  read: {tokens - len(unread)} / {tokens} = {(tokens - len(unread)) / tokens:.3f}')
    for doc in T:
        c = code(doc); x = sum(1 for it in c if it[2] == 'x')
        print(f'    {doc}: {len(c) - x} / {len(c)} = {(len(c) - x) / len(c):.3f}')
    multi = {g: sorted(set(v.strip('-') for v, *_ in occ)) for g, occ in tab.items()}
    multi = {g: vs for g, vs in multi.items() if len(vs) > 1}
    print('  repeated groups with more than one value form (inflection, phrasing, or an open point):')
    for g, vs in sorted(multi.items()):
        print(f'    {g}: {" | ".join(vs)}')

    # 4. one-part or two-part? rank correlation of group number and alphabetical order of the value
    clean = {}
    for g, occ in tab.items():
        for v, d, f, n in occ:
            if len(g) == 5 and g.isdigit() and f == '' and norm(v):
                clean.setdefault(g, norm(v))
    items = sorted(clean.items())
    a = [int(k) for k, _ in items]; b = [v for _, v in items]
    r = rho(a, b)
    random.seed(1)
    sims = [rho(a, random.sample(b, len(b))) for _ in range(2000)]
    share = sum(abs(s) >= abs(r) for s in sims) / len(sims)
    print(f'\n4. order test over {len(items)} cleanly glossed five-figure groups: Spearman rho = {r:.3f}; '
          f'2000 shuffles: max |rho| {max(abs(s) for s in sims):.3f}, share >= |rho| {share:.2f}')
    first = collections.defaultdict(set)
    for k, v in items:
        first[k[0]].add(v[0])
    print('  initial letters of the values under each first figure:')
    for d in '0123456789':
        print(f'    {d}: {"".join(sorted(first[d]))}')

    # 5. the sibling folders: shared groups, and how many a telegram in this code would be expected to share
    own = {g for g in tab if len(g) >= 4 and g not in SHORT}
    hits = tot = 0
    for doc in T:
        others = {bare(g) for d in T if d != doc for g, *_ in code(d)} - SHORT
        mine = [bare(g) for g, *_ in code(doc) if bare(g) not in SHORT]
        hits += sum(g in others for g in mine); tot += len(mine)
    rate = hits / tot
    print(f'\n5. leave-one-telegram-out: {hits} of {tot} code groups of a telegram recur in the other seven '
          f'(rate {rate:.2f})')
    freq = collections.Counter(bare(g) for d in T for g, *_ in code(d) if bare(g) not in SHORT)
    top = [g for g, _ in freq.most_common(10)]
    s10 = sum(freq[g] for g in top) / sum(freq.values())
    print(f'  the ten commonest groups ({", ".join(f"{g} {tab[g][0][0]}" for g in top)}) make up {s10:.2f} of the '
          f'code groups; a smaller, topic-free rate than the one above')
    for folder in ('carlos1903', 'manuel1910', 'sabugosa1910', 'hintze1903'):
        sib = [g for g in sibling_groups(folder) if g not in SHORT]
        if not sib:
            print(f'  {folder}: no transcriptions found'); continue
        shared = sorted(set(sib) & own)
        exp = rate * len(sib)
        print(f'  {folder}: {len(sib)} groups, shared with this code: {shared or "none"}; '
              f'expected if the same code {exp:.1f}, P(none) about {(1 - rate) ** len(sib):.1e}; '
              f'P(none of the ten commonest) about {(1 - s10) ** len(sib):.1e}')
