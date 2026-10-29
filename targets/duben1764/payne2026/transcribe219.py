"""Expand manually read image-219 grid; each row has nine values, each column 72.
Not an OCR or a decipherment. Question marks preserve doubtful readings.
"""
from pathlib import Path
columns = [
'''a|ab|ac|ad|af|ag|ai|al|am
an|ap|ar|as|at|au|aux|able|avre?
ant|ation,aution?|av|b|ba|be|bi|bo|bu
bl|ble,s|bli|c|ca|ce|ci|co|cu
cha|che|chi|ch|ces|cette|com|comme|con
d|da|de|di|do|du|dou|dra|dre
des|dit|e|eb|ec|ed|e,ea|ef|eg
ei|el|em|en|ent|ep|er|es|en''',
'''et|et|eu|ev|ex|ez|ence|ette,s|eur
eux|f|fa|fe|fi|fo|fou|fu|fr
g|ga|ge|ge|gi|go|gou|gu|gt?
gn|gr|gen|ger|get,git?|h|ha|he|hi
ho|hu|hom|hon|heur,e|j|ja|ib|ie
id|ie|ier,iere|if|ig|il|im|in|il
jo|jou|im|ir|is|it|ite|iu|iv
ion|ien|l|la|le|les|li|lo|lou''',
'''lu|lui|m|ma|me|de|mi|mo|mou
mu|ment|mais|n|na|ne|ni|no|nou
nu|nce,nci|nde|ns|nse,nsi|nt|nte|o|ob
oc|od|of|og|oi|pible?|ol|om|on
on|op|or|os|ot|oui,oit|ou|ouw?|ov
oient|oit|ou|p|pa|pe|pi|po|pou
pu|pl|pr|var|ver|q|qua|que|qui
quo|qu|r|ra|re|ri|ro,rou|ru|rre''',
'''rner|rd,rt|rde,rte|rme|ren|s|sa|se|si
so|sou|su|sp|squ|st|ste|stion|spe,s
sion,tion|t|ta|te|ti,tie|to|tou|tu|tr
ten|tio,tion|ture|u|ub|ue|ud|ue|uf
ug|ul|um|un|une|up|ur|us|ut
ute,ude|v|va|ve|vo?|vou|vu|ver|ven
x|xa|xe,ce|xi,ci|xo,co|xu,cu|y|ya|z
za|ze|zi,ji|Distinctions|Virgule|point_avec_la_virgule|deux_points|point|a_linea''',
'''apostrophe|accent_aigu|accent_grave|parenthese|Nombres|1|2|3|4
5|6|7|8|9|0|00|000|0000
Million,s|Noms|Accord|addresse|affe?|admi,ami|Angleterre|appare?|argent
arrive,er|assure|atten|avon|audience|Autriche|aveu|averti|avis
avoir,s,t|authori|artille|ambassade|archiduc|aiguillon|Bal|bar|baron_de
bartlemy_Mr_de?|barry_Madame_de|berg,bocr?|berlin|brandebourg|breteuil|bernsdorff|bielke|bunoe?
billet,s|brieg|brauille?|but,e|bon,ne|capa,ble,cite|car|caractere|cause
caution|commis|commun|conclu|condition,s|confi|connoi|conseil|conse''',
'''Chan|Chancell|charge,r|conte|conven|corr|Cour|Constant|cour,t
Consider|Credit|chavc,chavi?|Chatelet_de|Chat?|Choiseul_le_duc_de|Comte_le|Creutz|Comte_d'Ulson?
Dan,s|depeche|di,t|dire|don,ner|drottning|duc,e,s|dauphin,e|duie?
den,der|Entre,ee|envoye,r|exped|eau,x|excepe?|etre,est,sera|etat,s|Eheslad?
Empereur,l'|exce|est|Espagne|faire,fait,s|ferme,te|fin|fon|for,t
fontainebleau|Fersen_le_Cte|Filosofow|franc|Fredric|Friesendorff|garant,ie|gener|grand
gleichen|goodricke|guines|Hazard|holl|herr|hesse|han,har|hor
jalou|jamais|insinue,e|inter|intrig|instrue|ils|il,y,a|kaunitz''',
'''Lan|Len|liberte|luy|Ministre|Monsieur|Madame|mal|man
mar|mais|Modene_de|nation|nego|non|parti|patrie|pour
point|porte|porte_la|pret,e|pres|publi|pechlin|qualite|question
St_Priest_Mr_de|Prince_le|Pul?|restitu|ridau?|rud,e|russe,ie|Ribbing_Mr_de|Roi_le
Reine_la|Stock|Suede|Suive,s|Sophie_Albertine|Scheffer|Sinclair|Schwerin|Senat_le
Suret|Sparre|Sprengporten|Ser|Virgule|visite|Votre|Vous|Versailles
sa_underlined|se_underlined|te_underlined|ve_underlined|a_underlined|c_underlined|d_underlined|e_underlined|f_underlined
g_underlined|hi_underlined|k_underlined|l_underlined|m_underlined|n_underlined|r_underlined|s|ta,tz?'''
]
r=Path(__file__).resolve().parent
out=['# Image219 complete-grid transcription attempt, 504 entries.',
'# Primary image: https://sok.riksarkivet.se/bildvisning/A0073297_00219',
'# ? = doubtful visual reading; comma = variants written at one label.',
'# Underscores join words; _underlined distinguishes marked variants.',
'# Heading words (Distinctions, Nombres, Noms) retain their own printed labels.',
'# 163: earlier mo struck out, replaced by de; 147: earlier name struck out, replaced by luy.',
'# This key has NOT yielded a validated reading of the target cipher.']
for c,col in enumerate(columns,1):
 rows=[row.split('|') for row in col.splitlines()]
 assert len(rows)==8 and all(len(row)==9 for row in rows),(c,[len(row) for row in rows])
 for a,row in enumerate(rows,1):
  for b,value in enumerate(row,1):out.append(f'{a}{b}{c} {value}')
(r/'key219.txt').write_text('\n'.join(out)+'\n')
p=r/'key_samples.tsv'; lines=p.read_text().splitlines();correct={171:'ai',181:'al',191:'am',211:'an',221:'ap',231:'ar',241:'as'}
for i,line in enumerate(lines):
 cells=line.split('\t')
 if cells[0]=='219' and int(cells[1]) in correct:
  cells[2]=correct[int(cells[1])];cells[4]='Corrected on full-resolution reinspection';lines[i]='\t'.join(cells)
p.write_text('\n'.join(lines)+'\n')
print('Wrote',len(out)-7,'entries;',sum('?' in line for line in out[7:]),'doubtful readings')
