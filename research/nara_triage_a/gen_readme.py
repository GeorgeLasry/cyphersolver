"""Fill the per-publication coverage table into README.md (between the COVERAGE markers) from coverage.tsv."""
import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__))

# Conclusions for the publications that held real code or phrase leads (everything else: default below).
NOTES = {
    'M30': 'Code runs 1791-1821 (T. Pinckney, King, Rush). Pinckney 1793 decoded ("Explication of the Cyphers", '
           'vol. 3 fr. 0179); King 1796-1800 printed (King, Life, italics in cipher); Rush 1817-21 interlinear '
           '(JQA code). **Row: Delacroix to Létombe 1797 (vol. 5 fr. 0244-0245), French code, undecoded.** 1898 '
           'clipping of the Jameson Raid telegrams ("some code words left undeciphered", vol. 193 fr. 0199): printed, '
           'British; not kept. 1867-1906: telegram forms "received in cipher" = clear decodes.',
    'M34': 'Code runs 1789-1819. Short 1789-90 and Livingston/Monroe 1803 (JQA code, Louisiana) in Founders/ASP; XYZ '
           'envoys 1797-98 (vol. 8, ~30 frames pure code, unknown code) printed in ASP; Armstrong 1804-10 in '
           'targets/armstrong; Barlow 1811 (vol. 16 fr. 0011) interlinear. **Row: Crawford 1813-14 (vol. 17), JQA '
           'code, no decode on film.** Gallatin 1816-19: a few short runs with words, not pursued. Later frames: '
           'tables, French gazettes.',
    'M31': 'Code runs 1792-1840. Carmichael/Short 1792-95 and Smith/Humphreys: interlinear (vol. 6 fr. 0018-0019) or '
           'Founders; Pinckney 1803-05 (Pinckney code, targets/erving1807aug key); Erving 1805-07 (repo). **Row: '
           'Anthony Morris 1813-15 (vol. 12), unknown code, undecoded.** Appleton 1823 located (vol. 22 fr. 0134) '
           'and Everett 1825 located (vol. 25 fr. 0114, ~445 groups, JQA code): both already catalogued. 1840 (vol. '
           '33): interlinear. Later: Spanish debt tables, telegram forms.',
    'M35': 'JQA code throughout: vol. 1 (1808-11) and vol. 2 (1811-15, targets/jqa) printed by Ford; 1820 (vol. 8 fr. '
           '0180) and Dallas 1836 (vol. 13 fr. 0219) interlinear. 1816-18: exchange-rate tables. No row.',
    'M97': 'JQA code 1823-39. Poinsett 1825-29 printed decoded in Manning 1925 vol. 3 (cipher in small capitals). '
           '**Row: Powhatan Ellis 1836 and 1839 (vols. 7-9), pure code, readable with the repo table; Manning IAA '
           'vol. 8 unchecked.** Post-1840: tables, telegram decodes.',
    'M37': 'Poinsett 1813 (catalogued) located at roll 2 fr. 0093; **row: Poinsett 14 June 1814 (fr. 0097-0099)**. '
           'Other agents: no code frames.',
    'M121': 'Sumter 1809-13 (vol. 1A fr. 0035-0038): interlinear decode; 1830 (vol. 8): one short run. Rest tables.',
    'M42': 'Murray 1797-1801: decoded interlinear (targets/murray1801). No row.',
    'M43': 'Humphreys 1790-93 (Founders); W. L. Smith 1797-98 (vol. 4 fr. 0152) interlinear. No row.',
    'M44': '1799-1801 JQA Berlin (printed, Ford); 1835-1906 German statistical and budget tables. No row.',
    'M9': 'Lear, Cap Français 1802 (roll 4 fr. 0009-0013): code, decoded by Madison and by the Madison Papers editors '
          '(key in the Lear papers). Rest consular returns.',
    'M23': 'Lear, Algiers 1806-08: short runs only; Madison-era, Founders. No row.',
    'T260': 'Orleans 1806 (roll 8 fr. 0008-0011): John Graham to Madison 2 Jan 1806, code with Wagner\'s interlinear '
            'decode: **key lead for targets/graham1806**. Other frames: militia returns.',
    'T33': 'Colombia 1826-30 (roll 5 fr. 0140, JQA code): Manning 1925 vol. 2 prints the Colombia despatches with '
           'decodes; 1837-42 no code frames. Rest Diario Oficial tables. No row.',
    'M77': 'Instruction books: clear copies; flagged frames are despatch-number acknowledgements and indexes; '
           '"undeciphered group" (1897) and "could not decipher" (1869, 1871) are telegram transmission faults. No row.',
    'M179': 'Miscellaneous letters: tables, census and weather returns, invoices. Wilkinson 1813 coded message carries '
            'its decipherment (catalogue description). 1799 Astrea French consular cipher already in research/'
            'nara_catalog. "Could not be deciphered" hits are handwriting/telegram notes. No row.',
    'M40': 'Domestic letters: indexes. Vol. 22 fr. 0270 (1827): the Department says decipherments are "bound in '
           'volumes with the originals" (method note). No row.',
    'T1171': 'Codebooks of the Department of State 1867-1876 (naId 417267710): the 1867 code itself, digitised. '
             'Key lead, no ciphertext.',
    'M17': 'Registers of despatches: "Cipher requested / could not decipher" (Italy 1882) = transmission fault.',
    'M90': '1897 "distorted word we could not decipher": telegram fault, clear text. No row.',
    'T52': '1885 and 1902 "not decipherable" = missing code book / garble notes on decoded telegrams. No row.',
    'T157': '1905 Warsaw consul cable "could not be deciphered" (transmission, after 1904 codes). Rest tobacco tables.',
    '-': 'Non-microfilm file units in the slice: mostly passport applications (mirror-image OCR), Lincoln-death '
         'messages, internee cards; the 1814 Crittenden table. No code.',
}
DEFAULT = 'Flagged frames are tables, forms, invoices, gazettes or OCR noise; phrase hits are telegram boilerplate ' \
          'or decoded "telegram received in cipher" forms. No undecoded code run.'


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'coverage.tsv'), encoding='utf-8'), delimiter='\t'))
    out = ['| pub | series | items | flagged frames (table/code/mixed/prose/few) | phrase hits (kept) | conclusion |',
           '|---|---|---|---|---|---|']
    for r in rows:
        series = r['series'].split('>')[-1].strip()
        out.append(f"| {r['pub']} | {series} | {r['items']} | {r['frames']} ({r['table']}/{r['code']}/{r['mixed']}/"
                   f"{r['prose']}/{r['few']}) | {r['phrase_hits']} ({r['phrase_kept']}) | {NOTES.get(r['pub'], DEFAULT)} |")
    p = os.path.join(HERE, 'README.md')
    txt = open(p, encoding='utf-8').read()
    txt = re.sub(r'<!-- COVERAGE -->.*<!-- /COVERAGE -->', lambda m: '<!-- COVERAGE -->\n' + '\n'.join(out) +
                 '\n<!-- /COVERAGE -->', txt, flags=re.S)
    open(p, 'w', encoding='utf-8').write(txt)
    print(len(rows), 'publications')


if __name__ == '__main__':
    main()
