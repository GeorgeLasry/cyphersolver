# rounds_reading.py: reading and English lines changed by the improvement rounds after the Terrateig crib. Run from
# the vich1515 folder after crib_reading.py; patches work/reading_v1c.md and work/translation_en_v1c.md in place
# (earlier notation), which renotate.py then converts.
import re

READING = {   # line: [(old text, new text), ...]
    # round 1
    10: [('[?loau-]', 'locu-')],                 # OT at 10.24 (image): locura
    26: [('[?resistir] [?]', 'resistir al')],    # PHI at 26.25 (image); sifa = al (crib)
    27: [('[?echarle]', 'echarle')],             # PSI = l (crib)
    # round 2
    7: [('[?ellas] [?antes]', 'ellas pero')],
    8: [('ner [?] dias', 'ner muchos dias')],
    14: [('[?pero]', 'pero')],
    31: [('lo que por [?] [?] [?] [?antes] uos', 'lo que por obra uiere [?] pero uos')],
    42: [('[?antes] al fin', 'pero al fin')],
    44: [('y que [?] tengo', 'y que assi tengo')],
    48: [('suycos [?] [?] y es', 'suycos quieren tornar a [?uenir] y es')],
    53: [('haziendo lo [?] tanto', 'haziendo lo assi tanto')],
    55: [('alg[?] [?] [?] de hauer', 'alguna [?] [?] de hauer')],
    58: [('apoderarse del [?] [?] [?]', 'apoderarse del estado [?] [?]')],
    62: [('que ha [?] [?] que desean', 'que ha muchos anos que desean')],
    63: [('[?] y que por esto', 'quieren y que por esto')],
    67: [('y al [?] de la', 'y al estado de la')],
    70: [('[?antes] puso', 'pero puso')],
    77: [('uisorrey [?antes] que [?] [?]', 'uisorrey pero que [?pues] [?]')],
    78: [('[?] lo [?] por prouar', 'assi lo [?] por prouar')],
    94: [('que de [?]', 'que de [?aqui]')],
    95: [('de [?] [?] tal', 'de [?] otro tal')],
    99: [('dilacion alg[?] se', 'dilacion alguna se')],
    101: [('como la [?] y', 'como la defension y')],
    112: [('como la [?] y', 'como la defension y')],
    114: [('faltando [?los] [?] [?confederados]', 'faltando [?los] otros [?confederados]')],
    115: [('a la [?] de', 'a la defension de')],
    121: [('alg[?] y', 'alguna y')],
    122: [('[?cartas]', 'uias')],
    # round 3
    54: [('considere [?]', 'considere bien')],
    73: [('y que [?] [?] su [?]', 'y que [?mire] bien su [?]')],
}
ENGLISH = {
    10: [('[?mad-]', 'mad-')],
    26: [('[?resist] [?]', 'resist')],
    27: [('[?throw him]', 'throw him')],
    7: [('[?them] [?before]', 'them, but')],
    8: [('have [?] days ago letters', 'have for many days letters')],
    14: [('[?but]', 'but')],
    31: [('what by [?] [?] [?] [?before]; you', 'what I see in deed [?]; but you')],
    42: [('[?rather] in the end', 'but in the end')],
    44: [('and that [?] I hold', 'and that so I hold')],
    48: [('the Swiss [?] [?] and', 'the Swiss want to return to [?come] and')],
    53: [('by doing what [?] so much', 'by doing it so, so much')],
    55: [('that if some[?] [?] [?] to have', 'that if any [?] [?] to have')],
    58: [('to seize the [?] [?] [?]', 'to seize the state [?] [?]')],
    62: [('[?] [?] that', 'for many years')],
    63: [('[?] and that for this', 'want it, and that for this')],
    67: [('to the [?] of the Church', 'to the state of the Church')],
    70: [('[?but] put', 'but put')],
    77: [('viceroy [?before] that [?] [?]', 'viceroy, but that [?since] [?]')],
    78: [('[?] it [?] to prove', 'so it [?] to prove')],
    94: [('from [?]', 'from [?here]')],
    95: [('from [?] [?] such', 'from [?] another such')],
    99: [('without some delay [?] [?] with', 'without any delay [?] with')],
    101: [('as the [?] and', 'as the defence and')],
    112: [('as the [?] and', 'as the defence and')],
    114: [('failing [?the] [?] [?confederates]', 'failing [?the] other [?confederates]')],
    115: [('the [?] of [?]', 'the defence of [?]')],
    121: [('some [?] and', 'any, and')],
    122: [('[?letters]', 'ways')],
    54: [('he consider [?]', 'he consider well')],
    73: [('and that [?] [?] his [?]', 'and that [?he look] well to his [?]')],
}


def patch(path, edits):
    t = open(path).read(); a = t.index('```') + 3; b = t.index('```', a)
    out = []
    for l in t[a:b].split('\n'):
        m = re.match(r'(\s*)(\d+)(\s{2})(.*)', l)
        if m and int(m.group(2)) in edits:
            body = m.group(4)
            for old, new in edits[int(m.group(2))]:
                assert old in body, (path, m.group(2), old)
                body = body.replace(old, new, 1)
            l = m.group(1) + m.group(2) + m.group(3) + body
        out.append(l)
    open(path, 'w').write(t[:a] + '\n'.join(out) + t[b:])


patch('work/reading_v1c.md', READING)
patch('work/translation_en_v1c.md', ENGLISH)
print('reading lines patched:', len(READING), '; English lines:', len(ENGLISH))
