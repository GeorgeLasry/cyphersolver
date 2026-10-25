# crib_reading.py: the reading lines (earlier notation) rewritten where the Terrateig crib changes the decode;
# writes work/reading_v1c.md from work/reading_v1_old_notation.md. renotate.py then converts it to the current
# notation. Run from the vich1515 folder.
import re
NEW = {
 1: "[?] esta haueros [?escrito] estos dias con diuerso[s]",
 5: "[?escrito] por [?mar], no las [?] [?] [?] y ahunque las [?]s que por los del",
 6: "uuestras letras [?] [?] no son para hauer [?plazer] con",
 9: "contenido en [?ellas], digo que no puedo dexar de estar",
 10: "muy malcontento de uer que por la soberui[a] y [?loau-]",
 11: "ra de suycos de no querer esperar a que nuestro exercito se iuntase con [?ellos]",
 12: "[?] y por la remision es mi uisorrey y capitan general de tardar tanto en",
 13: "iuntarse se hayan puesto todas las cosas de Italia en el pe-",
 14: "ligro, que oy estan [?pero] para con uos [?] mucho [?mas] marauillado",
 15: "y peor contento estoi de uer la flaqueza del papa",
 16: "y [?quan] determinado esta de concertarse con franceses, no",
 17: "guardando en ello lo que esta capitulado, que ninguno de",
 18: "los confederados no pueda hazer paz ni tregua con ningu-",
 19: "[n] principe sin sabiduria y uoluntad de todos los confederados, y pues en esto ha",
 20: "quebrado la dicha capitulacion, no espero [?que] en",
 21: "ninguna otra cosa la ha de guardar, ahunque [?el] uos haya, como dezis",
 22: "prometido que asentara la dicha paz con Francia sin peri-",
 23: "uizyo de las captulaciones que con el emperador y comi-",
 24: "go tiene asentadas y assimismo guardara lo que por la capi-",
 26: "toda uez que el emperador y yo y suycos quisieremos [?resistir] [?]",
 27: "rey de francia y entender en [?echarle] de Italia [?el] ayudara para ello como",
 28: "por la dicha [?capitulacion] es obligado, porque esta paz que",
 29: "quiere asentar con franceses, la haze por fuerca y pu-",
 30: "ra necesidad de todo esto como [?]e dicho, yo no creo ni creere sino",
 31: "lo que por [?] [?] [?] [?antes] uos al papa no le haueys de",
 32: "asomar [?ni] [?dezir] [?palabra] ninguna de esto sino [?solo] esfor-",
 34: "beruia y lo aura de suycos hauemos [?] no desmay[?]",
 36: "ni [?] [?] que damos tantos principes [?xpianos] y en",
 39: "quisiese ofender, y [?pues] con es ayuda de Dios y de tantos principes [?]",
 48: "y que [?pues] suycos [?] [?] y es emperador [?] que uerna",
 53: "[?] [?] [?] ganara haziendo lo [?] tanto de lo",
 55: "que si alg[?] [?] [?] de hauer con [?el] rey de francia [?]",
 57: "ni dar al rey de francia ni poder [?meior] hazer lo que qui-",
 58: "siere en Italia y [?] que lo ha ya [?] apoderarse del [?] [?] [?]",
 61: "ia, por poder meior [?hazer] lo que quisiere es toda la",
 85: "en [?diuina] clemencia, que [?] la [?] que tenemos [?] la",
 63: "[?] y que por esto me paresce que es ninguna [?me] su [?] deue escu-",
 64: "char ninguna [?paz] del rey de francia sino asentando la todos los confederado[s] [?] iuntame-",
 69: "[?] Luys de Francia muerto por medio del [?] de Pauia, que no",
 70: "[?solo] no la guardo, [?antes] puso con [?ella] [?] [?] necesidad al papa y a [?obligado]",
 71: "yglia, y nacio della la cisma y todas [?las] necesidades y tra-",
 72: "baios que [?] [?] [?lo] [?] no pudi [?] [?el] rey de francia [?] si la",
 73: "dicha [?paz] [?] no se asentara, y que [?] [?] su [?] que por per-",
 77: "que estoi dello muy malcontento del dicho mi uisorrey [?antes] que [?] [?]",
 78: "[?nuestro] [?senor] [?] lo [?] por prouar si [?somos]",
 79: "constantes [?] seruirle en la dicha santa [?empresa]",
 82: "[?fuercas] y con [?mas] union y conformidad la dicha nuestra",
 83: "santisim[a] liga, ni que con es ayuda de Dios [?nuestro] [?senor]",
 90: "drentados de la dicha [?] y que yo perseuerando como pe-",
 91: "rseuero en la dicha liga y cumpliendo lo que por mi",
 92: "parte soy obligado, [?he] escrito al dicho mi uisorrey y capitan general [?repre-]",
 93: "[?hendiendole] grauemente de la dicha su neglige-",
 96: "y que assimismo le [?he] enbiado a [?] que si los dichos suycos",
 103: "charlos de Italia con es ayuda de Dios [?nuestro] [?senor], y que assimismo [?he] es-",
 104: "crito al emperador rogandole que uenga [?] [?] ninguna",
 105: "[?] en la dicha [?empresa] como lo ha [?enbiado]",
 110: "parte en la dicha nuestra santisima liga, y hagan y procur-",
 116: "y a la prosecucion de la dicha [?empresa], y a [?esta] pro-",
 119: "ni [?] los y como [?] sino [?] [?] [?]",
 120: "a la dicha [?empresa] [?] [?] [?] [?ella] [?] [?] [?me] [?]",
}
t = open('work/reading_v1_old_notation.md').read()
a = t.index('```') + 3; b = t.index('```', a)
out = []
for l in t[a:b].split('\n'):
    m = re.match(r'(\s*)(\d+)(\s{2})(.*)', l)
    if m and int(m.group(2)) in NEW: l = m.group(1) + m.group(2) + m.group(3) + NEW[int(m.group(2))]
    out.append(l)
open('work/reading_v1c.md', 'w').write(t[:a] + '\n'.join(out) + t[b:])
print('lines rewritten:', len(NEW))

# the English of the same lines, with the same holes
NEW_EN = {
 1: "[?] this having [?written] to you these days by [various]",
 5: "[?written] by [?sea], not those [?] [?] [?] and although those [?]s which by those of the",
 6: "your letters [?] [?] are not for having [?pleasure] with",
 9: "is contained in [?them], I say that I cannot fail to be",
 10: "very ill-content to see that through the prid[e] and [?mad-]",
 11: "ness of the Swiss of not wishing to wait for our army to join with [?them]",
 12: "[?] and through the remissness of my viceroy and captain general in delaying so long in",
 13: "joining up, all the affairs of Italy have been put in the dan-",
 14: "ger in which they are today, [?but] towards you [?] much [?more] amazed",
 15: "and less content am I to see the weakness of the Pope",
 16: "and [?how] determined he is to come to terms with the French, not",
 17: "keeping in it what is agreed by the capitulation, that none of",
 18: "the confederates may make peace or a truce with an-",
 19: "[y] prince without the knowledge and will of all the confederates; and since in this he has",
 20: "broken the said capitulation, I do not hope [?that] in",
 21: "any other thing he will keep it, although [?he] may have, as you say,",
 22: "promised that he would settle the said peace with France without prej-",
 23: "udice to the capitulations he has with the Emperor and with",
 24: "me settled, and likewise he would keep what by the capi-",
 26: "each time that the Emperor and I and the Swiss would wish to [?resist] [?]",
 27: "the King of France and undertake to [?throw him] out of Italy, [?he] would help for it, as",
 28: "by the said [?capitulation] he is bound, because this peace that",
 29: "he wants to settle with the French he makes by force and pure",
 30: "necessity: of all this, as I [?]ave said, I do not believe nor will believe but",
 31: "what by [?] [?] [?] [?before]; you must not to the Pope",
 32: "hint [?nor] [?say] [?word] any of this, but [?only] to encou-",
 34: "and madness of the Swiss we have [?] not [?lose heart]",
 36: "nor [?] [?] that we give so many [?Christian] princes and in",
 39: "to harm him, and [?since] with this help of God and of so many princes [?]",
 48: "and that [?since] the Swiss [?] [?] and the Emperor [?] that he will come",
 53: "[?] [?] [?] he will gain by doing what [?] so much of what",
 55: "that if some[?] [?] [?] to have with [?the] King of France [?]",
 57: "nor give the King of France the power [?better] to do what he",
 58: "wishes in Italy and [?] that he has already [?] to seize the [?] [?] [?]",
 61: "urch, so as the better to [?do] what he wishes in all the",
 85: "in [?divine] clemency, that [?] the [?] that we have [?] the",
 63: "[?] and that for this it seems to me that it is none [?me] his [?] must lis-",
 64: "ten to no [?peace] of the King of France except by settling it all the confederate[s] [?] jointly",
 69: "[?] Louis of France dead through the [?] of Pavia, who not",
 70: "[?only] did not keep it, [?but] put with [?it] [?] [?] necessity to the Pope and to [?bound]",
 71: "the Church, and from it was born the schism and all [?the] necessities and tri-",
 72: "bulations that [?] [?] [?] [?] could not [?] [?the] King of France [?] if the",
 73: "said [?peace] [?] will not be settled; and that [?] [?] his [?] that through per-",
 77: "that I am of it very ill-content with my said viceroy [?before] that [?] [?]",
 78: "[?our] [?Lord] [?] it [?] to prove whether [?we are]",
 79: "constant [?] in serving Him in the said holy [?enterprise],",
 82: "[?forces] and with [?more] union and conformity the said our",
 83: "[most holy] league, nor that with this help of God [?our] [?Lord]",
 90: "ened by the said [?], and that I, persevering as I per-",
 91: "severe in the said league and fulfilling what on my",
 92: "part I am bound to, [?have] written to my said viceroy and captain general [?repri-]",
 93: "[?manding him] gravely for his said neglig-",
 96: "and that likewise I [?have] sent him to [?] that if the said Swiss",
 103: "thrown out of Italy with this help of God [?our] [?Lord]; and that likewise [?I have]",
 104: "written to the Emperor begging him to come [?] [?] none",
 105: "[?] in the said [?enterprise], as he has [?sent]",
 110: "part in the said our most holy league, they act and endea-",
 116: "and the pursuit of the said [?enterprise], and to [?this] pur-",
 119: "nor [?] them and as [?] but [?] [?] [?]",
 120: "to the said [?enterprise] [?] [?] [?] [?it] [?] [?] [?me] [?]",
}
t = open('work/translation_en_v1_old_notation.md').read()
a = t.index('```') + 3; b = t.index('```', a)
out = []
for l in t[a:b].split('\n'):
    m = re.match(r'(\s*)(\d+)(\s{2})(.*)', l)
    if m and int(m.group(2)) in NEW_EN: l = m.group(1) + m.group(2) + m.group(3) + NEW_EN[int(m.group(2))]
    out.append(l)
open('work/translation_en_v1c.md', 'w').write(t[:a] + '\n'.join(out) + t[b:])
hole = re.compile(r'\[\?[^\]]*\]')
bad = [n for n in NEW if len(hole.findall(NEW[n])) != len(hole.findall(NEW_EN[n]))]
print('English lines rewritten:', len(NEW_EN), '; hole-count mismatches:', bad)
