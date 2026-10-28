"""Reproduce the 28 Oct 2026 alignment. No network or language-model dependencies."""
import csv, json, random, string
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def vig(text, key, enc=False, offset=0):
    out=[]; i=offset
    for c in text:
        if c in string.ascii_uppercase:
            v=ord(key[i%len(key)])-65
            out.append(chr((ord(c)-65+(v if enc else -v))%26+65)); i+=1
        else: out.append(c)
    return ''.join(out)

def main():
    data=json.loads((ROOT/'continuation.json').read_text())
    rows=[]; report=[]
    for d in data:
        raw=d['cipher_candidates'].split(); plain=d['plaintext_words'].split()
        assert len(raw)==len(plain)
        assert all(len(c)==len(p) for c,p in zip(raw,plain)), d['id']
        offset=0; agree=total=0
        for j,(c,p) in enumerate(zip(raw,plain),1):
            corrected=vig(p,d['key'],True,offset)
            decrypted=vig(c,d['key'],offset=offset)
            assert vig(corrected,d['key'],offset=offset)==p
            same=sum(a==b for a,b in zip(c,corrected)); agree+=same; total+=len(c)
            rows.append([d['id'],j,offset,c,decrypted,corrected,p,len(c)-same,
                         'direct candidate' if c==corrected else d['correction_basis']])
            offset+=len(c)
        report.append(f"{d['id']}: {agree}/{total} raw candidate letters agree; {total-agree} differences. Corrected stream is a reconstruction, not raw evidence.")
        (ROOT/(d['id']+'_decryption.txt')).write_text('\n'.join(
            f'{r[1]:02d} offset {r[2]:3d}: {r[3]} -> {r[4]} | reconstructed {r[5]} -> {r[6]} ({r[8]})'
            for r in rows if r[0]==d['id'])+'\n')
        (ROOT/(d['id']+'_cipher.txt')).write_text(d['cipher_candidates']+'\n')
        if d['id'].startswith('v196-0055'):
            c=''.join(raw); p=''.join(plain)
            for k in ['COMPLETEVICTORY','COMERETRIBUTION','MANCHESTERBLUFF','THENAVYOURPRIDE']:
                scores=[sum(a==b for a,b in zip(vig(c,k,offset=o),p)) for o in range(len(k))]
                report.append(f'{d["id"]} key control {k}: offset0 {scores[0]}/{len(c)}; best {max(scores)} at offset {scores.index(max(scores))}')
        if d['id']=='v10-0049':
            c=''.join(raw); p=''.join(plain)
            # Retrospective partition check: transcription and key were refined together.
            z=''.join(chr((ord(a)-ord(b))%26+65) for a,b in zip(c[:39],p[:39]))
            report.append('First-39 C-P stream: '+z)
            pred=vig(p,d['key'],True)
            report.append(f'Remaining 55 letters: {sum(a==b for a,b in zip(c[39:],pred[39:]))}/{len(c[39:])} agree (retrospective check, not independent holdout).' )
            candidates=['COMPLETEVICTORY','COMERETRIBUTION','MANCHESTERBLUFF','OURNAVYOURPRIDE',d['key']]
            for k in candidates:
                scores=[sum(a==b for a,b in zip(vig(c,k,offset=o),p)) for o in range(len(k))]
                report.append(f'{k}: best {max(scores)}/{len(c)}, offset {scores.index(max(scores))}; offset 0 {scores[0]}')
            rng=random.Random(681)
            random_scores=[]
            for _ in range(1000):
                k=''.join(rng.choice(string.ascii_uppercase) for _ in range(15))
                random_scores.append(sum(a==b for a,b in zip(vig(c,k),p)))
            report.append(f'1000 random 15-letter keys, offset 0: max {max(random_scores)}/{len(c)}')
            control='THE ARMY NEEDS TIME TO REST AND REFORM BEFORE IT CAN MARCH EAST TO JOIN THE OTHER TROOPS AGAIN'
            assert vig(vig(control,d['key'],True),d['key'])==control
            report.append('Synthetic encipher/decipher round-trip: PASS (arithmetic control only; no ciphertext-only solver claim).')
    with (ROOT/'continuation_alignment.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['doc','word','offset','raw_candidate','raw_decryption','reconstructed_cipher','plaintext','differences','basis']);w.writerows(rows)
    (ROOT/'continuation_controls.txt').write_text('\n'.join(report)+'\n')
    print('\n'.join(report))

if __name__=='__main__': main()
