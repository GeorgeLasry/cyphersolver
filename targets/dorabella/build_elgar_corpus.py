"""Extract Elgar's own words from Dora Powell, Edward Elgar: Memories of a Variation (1937;
archive.org in.ernet.dli.2015.155431, src/memories1937/memories.txt): his letters to the Penny
family (salutation to signature) and the quoted speech, which is mostly his. Writes
src/elgar_register.txt, the local file behind the lang/ source 'en-elgar-powell1937'.
Leakage of Dora's narration is unavoidable at the edges of the matches."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(HERE, 'src', 'memories1937', 'memories.txt'), encoding='utf-8').read()
letters = re.findall(r'((?:My )?[Dd]ear (?:Dorabella|Miss Penny|Dora|Mrs\. Penny)[\s\S]{20,3000}?'
                     r'(?:E\.\s?E\.|EDWARD ELGAR|EDWASD ELGAR|Ed\. ?Elgar|Yours ever[^\n]*|E\. ELGAR))', t)
speech = re.findall(r'‘([^’]{3,600})’', t, flags=re.S)
body = '\n\n'.join(letters) + '\n\n' + '\n'.join(speech)
body = re.sub(r'\n\s*\d{1,3}\s*\n', '\n', body)          # page numbers
body = re.sub(r'-\s*\n\s*', '', body)                     # OCR line-end hyphens
open(os.path.join(HERE, 'src', 'elgar_register.txt'), 'w', encoding='utf-8').write(body)
print(len(letters), 'letters,', len(speech), 'speeches,', len(body), 'chars')
