"""b16: modernise the spelling of a vich1511 reading (orthography only: u/v/b, ss, z/c, x/j, f/h, y/i, n/m before p/b),
word by word, keeping brackets and punctuation. The build file keeps the figures' own spelling.
python b16_vich_modern.py <in> <out>   (or import modern())"""
import re, sys

WORDS = {  # whole-word replacements (lower case); spelling only, no change of form
    'ia': 'ya', 'y': 'y', 'dezir': 'decir', 'dize': 'dice', 'dizen': 'dicen', 'dizia': 'decía', 'dezia': 'decía',
    'deziades': 'decíades', 'dixo': 'dijo', 'hazer': 'hacer', 'fazer': 'hacer', 'hazerlo': 'hacerlo', 'haze': 'hace',
    'hazian': 'hacían', 'hazia': 'hacía', 'haziase': 'hacíase', 'hazedmelo': 'hacedmelo', 'fiziessen': 'hiciesen',
    'fiziesse': 'hiciese', 'hiziesse': 'hiciese', 'hiziessen': 'hiciesen', 'fizo': 'hizo', 'fecho': 'hecho',
    'escreuir': 'escribir', 'escreuiades': 'escribíades', 'escreuia': 'escribía', 'escreuistes': 'escribistes',
    'escriuieron': 'escribieron', 'escrito': 'escrito', 'scriuir': 'escribir', 'enbiado': 'enviado', 'enbiar': 'enviar',
    'embiar': 'enviar', 'embiado': 'enviado', 'agora': 'ahora', 'assi': 'así', 'assimismo': 'asimismo', 'quexan': 'quejan',
    'exercito': 'ejército', 'dexar': 'dejar', 'dexe': 'deje', 'estaua': 'estaba', 'estauan': 'estaban',
    'estauades': 'estábades', 'auia': 'había', 'hauia': 'había', 'aueys': 'habéis', 'haueys': 'habéis', 'auer': 'haber',
    'hauer': 'haber', 'hauemos': 'habemos', 'havemos': 'habemos', 'haver': 'haber', 'haveys': 'habéis', 'havia': 'había',
    'tengays': 'tengáis', 'trateys': 'tratéis', 'mireys': 'miréis', 'direys': 'diréis', 'hareys': 'haréis',
    'sabeys': 'sabéis', 'teneys': 'tenéis', 'veys': 'veis', 'podeys': 'podéis', 'deveys': 'debéis', 'deve': 'debe',
    'deven': 'deben', 'devia': 'debía', 'devemos': 'debemos', 'enpresa': 'empresa', 'conplir': 'cumplir',
    'compliria': 'cumpliría', 'absentes': 'ausentes', 'comienco': 'comienzo', 'desauentaia': 'desventaja',
    'peruirtiessen': 'pervirtiesen', 'visorrey': 'visorrey', 'cosa': 'cosa', 'gelo': 'gelo', 'uos': 'vos',
    'nro': 'nuestro', 'muger': 'mujer', 'iusta': 'justa', 'iusticia': 'justicia', 'iunto': 'junto', 'iuntos': 'juntos',
    'yglesia': 'iglesia', 'yglesias': 'iglesias', 'ynglaterra': 'Inglaterra', 'reyno': 'reino', 'reynos': 'reinos',
    'ayuda': 'ayuda', 'leuar': 'llevar', 'lleuar': 'llevar', 'lleuo': 'llevó', 'dubda': 'duda', 'cibdad': 'ciudad',
    'efectue': 'efectúe', 'sienpre': 'siempre', 'tienpo': 'tiempo', 'canpo': 'campo', 'onbre': 'hombre',
    'onbres': 'hombres', 'nonbre': 'nombre', 'cunplir': 'cumplir', 'cunplan': 'cumplan', 'cumplan': 'cumplan',
    # appended by the N.60 fork (b16)
    'comigo': 'conmigo', 'perjuyzio': 'perjuicio', 'huuiere': 'hubiere', 'huuiesse': 'hubiese', 'huuiese': 'hubiese',
    'hauer': 'haber', 'oy': 'hoy', 'ueynte': 'veinte', 'veynte': 'veinte', 'escriuo': 'escribo', 'escriuen': 'escriben',
    'enbiastes': 'enviastes', 'enbian': 'envían', 'enbie': 'envíe', 'enuie': 'envíe', 'enuiassen': 'enviasen',
    'enbiada': 'enviada', 'destruycion': 'destrucción', 'destruyda': 'destruida', 'contribuyr': 'contribuir',
    'deuese': 'débese', 'trabajays': 'trabajáis', 'trabajeys': 'trabajéis', 'quiteys': 'quitéis',
    'aparteys': 'apartéis', 'pongays': 'pongáis', 'digays': 'digáis', 'dexeys': 'dejéis', 'perdays': 'perdáis',
    'respondays': 'respondáis', 'podeys': 'podéis', 'respondereys': 'responderéis', 'podreys': 'podréis',
    'deuo': 'debo', 'deue': 'debe', 'deuen': 'deben', 'deuemos': 'debemos', 'uiniendo': 'viniendo',
    'malissimamente': 'malísimamente', 'grandissimo': 'grandísimo', 'grandissima': 'grandísima',
    'constantissimamente': 'constantísimamente', 'excessiuo': 'excesivo', 'quexoso': 'quejoso',
    'fizistes': 'hicistes', 'fiziesse': 'hiciese', 'desfiziesse': 'deshiciese', 'proueystes': 'proveístes',
    'uiessedes': 'viesedes', 'pudiessedes': 'pudiesedes', 'estoruar': 'estorbar', 'estoruarlo': 'estorbarlo',
    'enderecar': 'enderezar', 'cismaticos': 'cismáticos', 'hereticos': 'heréticos', 'caher': 'caer',
    'afloxasse': 'aflojase', 'afloxar': 'aflojar', 'afloxare': 'aflojaré', 'dixere': 'dijere',
    'matto': 'mató', 'agrauiaren': 'agraviaren', 'dizia': 'decía', 'dezis': 'decís', 'dezir': 'decir',
    'Gurs': 'Gurs', 'expressamente': 'expresamente', 'possession': 'posesión', 'posession': 'posesión',
    'continuen': 'continúen', 'continua': 'continúa', 'ruego': 'ruego', 'gouernacion': 'gobernación',
    'conseruacion': 'conservación', 'deuemos': 'debemos', 'ludouico': 'Ludovico',
    # appended for N.45 (b16)
    'faziendo': 'haciendo',
    'fagamos': 'hagamos',
    'fagan': 'hagan',
    'faga': 'haga',
    'fagays': 'hagáis',
    'fazed': 'haced',
    'fazedmelo': 'hacedmelo',
    'fize': 'hice',
    'fiziesse': 'hiciese',
    'fazen': 'hacen',
    'faze': 'hace',
    'fara': 'hará',
    'fare': 'haré',
    'faria': 'haría',
    'fazerse': 'hacerse',
    'faziendose': 'haciéndose',
    'hazerla': 'hacerla',
    'hazerse': 'hacerse',
    'concluyr': 'concluir',
    'concluyrla': 'concluirla',
    'concluyreys': 'concluiréis',
    'concluya': 'concluya',
    'destruyr': 'destruir',
    'restituyr': 'restituir',
    'estorvar': 'estorbar',
    'estorvaran': 'estorbarán',
    'estorvarme': 'estorbarme',
    'escrevistes': 'escribistes',
    'escrevis': 'escribís',
    'escrevays': 'escribáis',
    'escrevidme': 'escribidme',
    'escrevia': 'escribía',
    'escrive': 'escribe',
    'escrito': 'escrito',
    'buelva': 'vuelva',
    'havian': 'habían',
    'havran': 'habrán',
    'havra': 'habrá',
    'haya': 'haya',
    'haia': 'haya',
    'yr': 'ir',
    'yrse': 'irse',
    'trabajeys': 'trabajéis',
    'apreteys': 'apretéis',
    'procurareys': 'procuraréis',
    'acabareys': 'acabaréis',
    'suplicays': 'suplicáis',
    'pongays': 'pongáis',
    'mireys': 'miréis',
    'tuvieredes': 'tuviéredes',
    'desveleys': 'desveléis',
    'dividirnos': 'dividirnos',
    'complido': 'cumplido',
    'complira': 'cumplirá',
    'sobreaviso': 'sobre aviso',
    'dessearia': 'desearía',
    'possible': 'posible',
    'possession': 'posesión',
    'criacion': 'creación',
    'Geronimo': 'Gerónimo',
    'Coluna': 'Colonna',
    'Treviso': 'Treviso',
    'Padua': 'Padua',
    'prioradgo': 'priorazgo',
    'pudieredes': 'pudiéredes',
    'tomeys': 'toméis',
    'experimentados': 'experimentados',
    'enbie': 'envíe',
    'embie': 'envíe',
    'escusar': 'excusar',
    'dexeys': 'dejéis',
    'dexara': 'dejará',
    'dexe': 'deje',
    # appended for N.45 (b16): the intervocalic-u rule turned the diphthong ue into ve (luego -> lvego)
    'luego': 'luego',
    'nueve': 'nueve',
    'nuestra': 'nuestra',
    'nuestro': 'nuestro',
    'nuestras': 'nuestras',
    'nuestros': 'nuestros',
    'nuevo': 'nuevo',
    'nuevos': 'nuevos',
    'nueva': 'nueva',
    'nuevas': 'nuevas',
    'prueva': 'prueba',
    'Coluna': 'Colonna',
    'coluna': 'Colonna',
    'esperiencia': 'experiencia',
    'governar': 'gobernar',
    'governarse': 'gobernarse',
    'pued': 'puede',
    'eceto': 'excepto',
}

def _word(w, fragment=False):
    lo = w.lower()
    if lo in WORDS and not fragment: r = WORDS[lo]
    else:
        r = lo
        r = re.sub(r'ss', 's', r)
        r = re.sub(r'ç', 'z', r)
        r = re.sub(r'z(?=[ei])', 'c', r)
        r = re.sub(r'(?<=[aeiou])u(?=[aeiou])', 'v', r)          # intervocalic u = v
        r = re.sub(r'^u(?=[aeiou])', 'v', r)
        r = re.sub(r'aua(?=(n|s|des|mos)?$)', 'aba', r)         # imperfect -aua -> -aba
        r = re.sub(r'aba(?=(n|s|mos)?$)', 'aba', r)
        r = re.sub(r'ava(?=(n|s|mos)?$)', 'aba', r)
        r = re.sub(r'x(?=[aeiou])', 'j', r) if lo not in ('maximiliano', 'exemplo') else r
        r = re.sub(r'n(?=[pb])', 'm', r)
        r = re.sub(r'eys$', 'éis', r); r = re.sub(r'ays$', 'áis', r)
    if w[:1].isupper(): r = r[:1].upper() + r[1:]
    return r

def modern(text):
    out = []
    for tok in re.split(r'(\[[^\]]*\]|[^\W\d_]+)', text):
        if tok.startswith('[?'): out.append('[?' + _word(tok[2:-1]) + ']') if re.fullmatch(r'\[\?[^\W\d_]+\]', tok) else out.append(tok)
        elif tok.startswith('['): out.append(tok)
        elif re.fullmatch(r'[^\W\d_]+', tok or '-'):
            prev = next((o for o in reversed(out) if o), '')
            frag = prev.endswith(']')
            out.append(_word(tok, fragment=frag))
        else: out.append(tok)
    return ''.join(out)

if __name__ == '__main__':
    open(sys.argv[2], 'w', encoding='utf-8').write(modern(open(sys.argv[1], encoding='utf-8').read()))
