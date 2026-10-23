"""v5a (23 Oct 2026): write affry1757/read/<R>_reading.md from the Fagel register text (v5a_affry_reg.py output),
with a header saying what it rests on and the substitutions listed in SUBS (figures over a register slip).
    python research/reading_audit/v5a_affry_write.py"""
import pathlib, textwrap
ROOT = pathlib.Path(__file__).resolve().parents[2]
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5')
L = {
 'R1076': ('7 January 1757 (no. 124)', 'inv. 5186 scans 16R-17L (margin "No 124. Dat: 7. Janvier 1757. A: à R:")',
           'checked line by line against the scans 23 Oct 2026 (v5)', '229 of the 396 keyed groups stand at the register\'s word (0.578; shuffled key values 0.106, max 0.154). The aligner leaves page 1 of the cipher (groups 0-156) unplaced, but its keyed decode follows the register\'s 17L text in order by eye ("il n\'a cessé de ce moment-là de travailler, et a déterminé le convoi ... de quatre vaisseaux d\'escorte sans la tempête ... je ne peux vous dépeindre ... je vous répète avec vérité que je leur dois ma conduite et les succès"). Three register stretches have no matching run of keyed groups: "prés de soixante Batimens ... chargés dans le Texel" (compressed in the alignment), and "lui dire, et y declarer ... qu\'il se char[geoit]" and "donné à Belle Isle ... J\'espere Mr que vous", which fall between the cipher runs of the two DECODE pages: clear periods of the letter (read/R1076.md: "the ciphered periods of a longer letter") or cipher not imaged',
           [('et la Tempette', 'sans la Tempette', 'the register has "et la Tempette", a copyist\'s slip; the figures give "sans la tems pe te"'),
            ('je lui ai parlai', 'je lui parlai', '"ai" is struck in the register; the figures give "je lui par la i"')]),
 'R1073': ('25 January 1757 (no. 133)', 'inv. 5186 scan 42R (margin "No 133. Dat: 25. Janvier 1757. A: à R:")',
           'checked line by line against the scan by WAINUT\'s reviewer (21 Oct 2026)', '264 of the 309 keyed groups stand at the register\'s word (0.854; shuffled 0.103, max 0.136), from first group to last (12 groups without clear text)', []),
 'R1068': ('26 April 1757 (no. 172)', 'inv. 5186 scan 181L (margin "No. 172. Dat: 26. Avril 1757. A: à R:")',
           'checked against the scan (21 Oct 2026)', '46 of the 56 keyed groups stand at the register\'s word (0.821; shuffled 0.089, max 0.143); the ten others are the opening null groups and the name Starrenberg, which the cipher spells with groups the key reads "d\'A-re-m-be-r-g" (982 = st, 245 = n from this one occurrence)', []),
 'R1067': ('1 April 1757 (no. 161)', 'inv. 5186 scans 148R-150L (margin "No 161. Dat: 1. Avril 1757. A: à R:")',
           '148R and 149L checked by WAINUT\'s reviewer (21 Oct 2026), 149R and 150L checked line by line against the scans 23 Oct 2026 (v5)', '1,227 of the 1,465 keyed groups stand at the register\'s word (0.838; shuffled 0.141, max 0.153), with no unplaced stretch of five groups or more. The cipher\'s pieces are numbered No 1-No 13 and run in another order on the pages (read/R1067.md, "Order of the pieces"); the register gives the letter in its own order, which is followed here', []),
 'R1070': ('22 July 1757 (no. 210, to Bernis)', 'inv. 5186 scans 255R-256L (margin "No 210. Dat: 22. Juillet 1757. A: à B.")',
           'checked line by line against the scans 23 Oct 2026 (v5)', '249 of the 395 keyed groups stand at the register\'s word (0.630; shuffled 0.113, max 0.134). The aligner leaves groups 0-125 unplaced: they are on the DECODE image I5590, which holds the end of the letter (the DECODE page order is reversed, read/R1070.md); their keyed decode follows the register\'s last lines by eye ("...demander à cette [Princesse] une ... dans laquelle je tâcherai de lui prouver combien il lui est essentiel, et à l\'intérêt de M. le [Stadhouder] son fils, de mériter la bienveillance de Sa Majesté"). The last sentence ("Vous trouverez cijoint ...") is in clear on the cipher page too', []),
}
for r, (date, where, chk, agree, subs) in L.items():
    t = (SCR / f'reg_{r}.txt').read_text(encoding='utf-8').strip()
    for a, b, _ in subs:
        assert a in t, (r, a); t = t.replace(a, b)
    head = (f'# {r} - d\'Affry, The Hague, {date}: reading\n\n'
            f'Rests on: the contemporary clear copy of this despatch in the Fagel register, Nationaal Archief 1.10.29 {where}, '
            f'transcribed by WAINUT (21 Oct 2026, `wainut/register_clear.txt`), {chk}. The register is the deciphered text '
            f'of the same letter: with this folder\'s key (`wainut/align_register.py`, `wainut/align/{r}.tsv`), {agree}. '
            f'The reading therefore follows the register, in the clerk\'s spelling (verification 5, 23 Oct 2026); the keyed '
            f'decode it replaces is `{r}.md`.')
    if subs:
        head += ' Where the figures correct a register slip the figures are followed: ' + '; '.join(f'{c}' for _, _, c in subs) + '.'
    body = '\n'.join(textwrap.fill(p, 118) for p in [t])
    out = '\n'.join(textwrap.fill(x, 118) for x in head.split('\n\n')).replace('\n# ', '\n\n# ')
    out = textwrap.fill(f'# {r} - d\'Affry, The Hague, {date}: reading', 200) + '\n\n' + textwrap.fill(head.split('\n\n', 1)[1], 118)
    out += '\n\n## Reading\n\n' + body + '\n'
    (ROOT / 'targets/affry1757/read' / f'{r}_reading.md').write_text(out, encoding='utf-8')
    print(r, len(t.split()))
