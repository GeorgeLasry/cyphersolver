"""b08: normalise the writer's spelling in the '## Reading' body of the malsburg1637 readings (whole words only).

    python b08_norm.py <reading.md> [...]

The map is printed into nothing: the header of each reading names the normalisation and the forms are listed in the
re-read log. Only spelling changes; a word the figures do not give is never added. Idempotent.
"""
import re, sys, pathlib

MAP = {
    'sobalt': 'sobald', 'alhir': 'alhier', 'nunmer': 'nunmehr', 'amoch': 'annoch', 'Feit': 'Feind', 'Feint': 'Feind',
    'Feints': 'Feinds', 'Feintshalber': 'Feindshalber', 'dach': 'dass', 'besetz': 'besetzt', 'schleinig': 'schleunig',
    'Widerkunft': 'Wiederkunft', 'brinen': 'bringen', 'uberlant': 'überland', 'muchen': 'möchten', 'izo': 'itzo',
    'Felt': 'Feld', 'balt': 'bald', 'wil': 'will', 'unt': 'und', 'Lant': 'Land', 'Wint': 'Wind', 'gentzlichen': 'gäntzlichen',
    'taglich': 'täglich', 'gefwret': 'geführet', 'abgefurt': 'abgeführt', 'aussfurlich': 'ausführlich',
    'Guarnison': 'Garnison', 'Coniuction': 'Coniunction', 'sin': 'sein', 'di': 'die', 'zen': 'den', 'dech': 'des',
    'Schade': 'Schaden', 'Wege': 'Wege', 'konen': 'können', 'Stucke': 'Stücke', 'Stuck': 'Stück', 'uber': 'über',
    'ubereilen': 'übereilen', 'Brucke': 'Brücke', 'musten': 'müssten', 'mussen': 'müssen', 'wurde': 'würde',
    'wurden': 'würden', 'Hulffe': 'Hülffe', 'konte': 'könnte', 'zwolff': 'zwölff', 'zwolf': 'zwölf',
    'zwolfpfundige': 'zwölfpfündige', 'nemen': 'nehmen', 'abnemen': 'abnehmen', 'einzunemen': 'einzunehmen',
    'Aussnemung': 'Aussnehmung', 'Volcker': 'Völcker', 'Volckern': 'Völckern', 'Commendo': 'Commando',
    'deichte': 'deuchte', 'andeiten': 'andeuten', 'angedeitet': 'angedeutet', 'Deitschlant': 'Deutschland',
    'Gemuht': 'Gemüth', 'ruhigerm': 'ruhigerem', 'Fritmachen': 'Friedmachen', 'nirgent': 'nirgend', 'leizten': 'letzten',
    'kurtzlich': 'kürtzlich', 'Stilstants': 'Stillstands', 'irer': 'ihrer', 'iren': 'ihren', 'ire': 'ihre',
    'Tragons': 'Dragoner', 'Verhinderlich': 'verhinderlich', 'Weg': 'Weg', 'Garnisonen': 'Garnisonen',
    'newe': 'neue', 'newen': 'neuen', 'Werbungen': 'Werbungen', 'bestimte': 'bestimmte', 'bestimten': 'bestimmten',
    'Hoffstat': 'Hofstatt', 'füret': 'führet', 'mitt': 'mit', 'nitt': 'nit', 'hatt': 'hat', 'Kugel': 'Kugel',
    'mittbringen': 'mitbringen', 'auff': 'auf', 'Fal': 'Fall', 'al': 'all', 'hette': 'hätte', 'hetten': 'hätten',
    'weill': 'weil', 'Viell': 'Viel', 'viell': 'viel', 'seher': 'eher', 'beisammn': 'beisammen', 'Begeren': 'begehren',
    'begeren': 'begehren', 'begert': 'begehrt', 'Befelch': 'Befehl', 'unterth': 'unterthänig', 'fuglicher': 'füglicher',
    'Zudeme': 'Zudem', 'deme': 'dem', 'damm': 'dann', 'Damm': 'Dann', 'dan': 'dann', 'Dan': 'Dann', 'wen': 'wenn',
    'Wen': 'Wenn', 'ohn': 'ohne', 'one': 'ohne', 'biel': 'viel', 'steet': 'steht', 'sein': 'sein',
    'notturfftigen': 'nothdürfftigen', 'Schieffe': 'Schiffe', 'lavettiret': 'lavetiret', 'Clevischen': 'Clevischen',
}

def main(files):
  for f in files:
    p = pathlib.Path(f)
    t = p.read_text(encoding='utf8')
    m = re.search(r'(^## Reading[^\n]*\n)(.*?)(?=^## |\Z)', t, re.S | re.M)
    body = m.group(2)
    n = [0]

    def sub(mm):
        w = mm.group(0)
        if w in MAP and MAP[w] != w:
            n[0] += 1
            return MAP[w]
        return w
    # whole words not inside [ ], { } or < > marks
    out = re.sub(r'(?<![\[\{<\w?])[^\W\d_]+(?![\w\]\}>])', sub, body)
    p.write_text(t[:m.start(2)] + out + t[m.end(2):], encoding='utf8')
    print(f, n[0], 'words normalised')


if __name__ == '__main__':
    main(sys.argv[1:])
