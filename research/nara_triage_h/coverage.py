"""coverage.py: coverage table (markdown) of the bulk_all groups reviewed in this slice -> coverage.md."""
import json, os, subprocess, sys, collections
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, '..', 'nara_reels', 'out')
sizes = {r[0]: r[1] for r in json.load(open(os.path.join(OUT, 'rg_sizes.json')))}
reviewed = set(open(os.path.join(H, 'reviewed.txt')).read().split())
NOTE = {
 'rg_226': 'OSS. desc 29 (all titles read: training films, crypto courses, Barcelona cipher pads, X-2 crypto file, Bern ULTRA; none digitised); word 114 (Gold File dispatch-form boilerplate "RECEIVED IN CODE OR CIPHER", War Report); frame 356 (M1934 Safehaven patent and statistics lists). 0 rows; key lead: I.G. Farben "Grundschluessel Miza" code book (M1934 r.2 f.438).',
 'rg_87': 'Secret Service daily reports (T915). All 673 phrase hits classed (639 "in cipher/cypher" = agents\' own telegrams, copied in clear; 34 "not decipher..." = illegible postmarks, coins, etc.); cipher-letter mentions grepped (106 frames) and 7 volumes fetched: Perkins 1875 counterfeiters\' cipher letters (key worked out, translations given), Drummond 1888 Gardner opium cipher telegrams (Mundy had the key), Hazen 1905 Dodson letter (read by Deputy Black), Memphis 1912 Wardner code letter (not copied), Oklahoma 1933 Tulsa letter (not copied). frame 4066/caps 189 sampled: indexes, calendars, serial numbers. 0 rows.',
 'rg_216': 'Office of Censorship: 6 desc read -> row "Secret Submissions" (naId 1266133).',
 'rg_108': 'desc: Telegrams Received in Cipher by Grant/Halleck (604437) already in nara_catalog.',
 'rg_395': 'M917 AEF Siberia: letters/caps hit on roll 9 f.963 -> row (1919 field message); word hits on roll 3 -> row (Chicherin telegram code passages); rolls 3 and 9 fetched and scanned for five-letter groups (only f.963).',
 'rg_104': 'U.S. Mint: desc -> row (Coded Telegrams 1912-44 + 1902 code key).',
 'rg_131': 'Office of Alien Property: 4 desc -> row (Duisberg Code Messages); seized code books (Mitsui, Chemnyco, Mitsubishi) noted as key leads.',
 'rg_120': 'AEF WWI: 7 desc -> row (Solution of Enemy Codes and Ciphers series); 67 word hits = Pershing cablegram series (own code, translated).',
 'rg_55': 'Virgin Islands: key lead "Chiffre dechiffrant for General Gouverneuren i West Indien" (311875940), already noted by nara_catalog.',
 'rg_126': 'Equatorial Islands 1938 coded radiograms: interlinear decode on the draft (f.243); dead end.',
 'rg_46': 'Senate: Overman subcommittee 1920 (encoded telegrams with their code book); 1860 Hoge cryptographic system proposal; no row.',
 'rg_389': 'PMG: "POW: Correspondence Ciphers in Use at POW Camps" (978563), not digitised, desc only; noted.',
 'rg_23': 'Coast Survey (M642): 70 phrase/word = telegraph tariff boilerplate.',
 'rg_392': 'Coast Artillery letters: telegram-blank boilerplate.', 'rg_128': 'Pearl Harbor JD-1 intercepts (machine, translated).',
 'rg_472': 'US Forces SE Asia (Vietnam, post-1950): out of period.',
 'rg_217': 'Southern Claims Commission (M1658/M2094): "cypher" = arithmetic in testimony; frames = claim files.',
 'rg_41': 'Customs intelligence 1918: film intertitles deleted as possible code; not cipher.',
}
rows = []
for f in sorted(os.listdir(OUT)):
    if not (f.startswith('done_') and f.endswith('_all.txt')): continue
    rg = f[5:-8]; done = len(open(os.path.join(OUT, f)).read().split())
    if done < sizes.get(rg, 10**9): continue
    c = collections.Counter()
    for l in open(os.path.join(OUT, f'{rg}_all.jsonl'), encoding='utf-8'):
        c[json.loads(l)['kind']] += 1
    rows.append((rg, c))
hit = [r for r in rows if r[1]]; nohit = [r[0] for r in rows if not r[1]]
K = ['desc', 'phrase', 'word', 'frame', 'letters', 'caps']
out = ['| record group | ' + ' | '.join(K) + ' | read / sampled, conclusion |', '|---|' + '---|' * (len(K) + 1)]
key = lambda r: (int(r[0].split('_')[1]) if r[0].split('_')[1].isdigit() else 9999)
for rg, c in sorted(hit, key=key):
    note = NOTE.get(rg, 'all desc/phrase/word read (boilerplate filtered); frame/letters/caps items listed by title and the most solid frames read: forms, tables, indexes, photos; no cipher' if rg in reviewed else 'NOT REVIEWED (completed after the last pass)')
    out.append(f'| {rg} | ' + ' | '.join(str(c.get(k, '')) for k in K) + f' | {note} |')
out.append('')
out.append(f'Complete with no hits ({len(nohit)}): ' + ', '.join(sorted(nohit, key=lambda x: key((x, 0)))))
open(os.path.join(H, 'coverage.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(hit), 'groups with hits,', len(nohit), 'without;', sum(1 for r in hit if r[0] not in reviewed), 'not reviewed')
