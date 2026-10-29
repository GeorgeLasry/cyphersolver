"""Harvest Calames (ABES) via its EadSearch.aspx web service (found in pub/javascript/calames.js).
Fields tried per term: fullText, titre, indexSimple(typeIndex=sujet). Writes calames_hits.jsonl (one record per hit)."""
import json, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

BASE = 'https://calames.abes.fr/prod/EadSearch.aspx'
TERMS = ['chiffre', 'chiffré', 'chiffrée', 'chiffrées', 'chiffrés', 'chifre', 'chifres', 'chiffres', 'déchiffrement',
         'déchiffré', 'déchiffrée', 'écriture secrète', 'alphabet chiffré', 'lettre chiffrée', 'en chiffre',
         'clef du chiffre', 'clé du chiffre', 'cifra', 'cifrada', 'cryptographie', 'cryptogramme', 'chiffrement',
         'nomenclateur', 'nomenclature chiffrée', 'caractères secrets', 'écriture chiffrée', 'chiffres secrets',
         'dépêche chiffrée', 'chifré', 'chifrée', 'chifrées', 'notae', 'cryptographique', 'cypher', 'cipher', 'notes tironiennes']
FIELDS = ['fullText', 'titre', 'indexSimple']


def get(params, tries=4):
    url = BASE + '?Query=Rech&' + params
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            return urllib.request.urlopen(req, timeout=90).read().decode('utf-8', 'replace')
        except Exception as e:
            time.sleep(3 * (i + 1))
    return ''


def parse(xml):
    out = []
    xml = xml.replace('�', '?')
    try:
        root = ET.fromstring(xml)
    except Exception:
        return out, 0
    cnt = 0
    for a in root.findall('a'):
        cnt = int(a.get('count', 0))
        b = a.find('b')
        rec = {k: a.get(k) for k in ('id', 'bibId', 'inventaire', 'level', 'cle', 'cleFullText')}
        if b is not None:
            ut = b.find('unittitle')
            rec['title'] = ''.join(ut.itertext()).strip() if ut is not None else ''
            rec['subjects'] = [s.get('normal') for s in b.iter('subject') if s.get('normal')]
            ud = b.find('unitdate')
            rec['date'] = (ud.text or '') if ud is not None else ''
            rec['datenorm'] = ud.get('normal') if ud is not None else ''
            rec['extent'] = (b.find('extent').text or '') if b.find('extent') is not None else ''
            for u in b.findall('unitid'):
                rec['unitid_' + (u.get('type') or 'x')] = ''.join(u.itertext()).strip()
        out.append(rec)
    return out, cnt


def main():
    seen = {}
    log = open('calames_counts.txt', 'w', encoding='utf-8')
    for field in FIELDS:
        for term in TERMS:
            params = field + '=' + urllib.parse.quote(term)
            if field == 'indexSimple':
                params += '&typeIndex=sujet'
            frm, step, total = 1, 100, None
            n = 0
            while total is None or frm <= total:
                xml = get(f'{params}&from={frm}&to={frm + step - 1}')
                recs, cnt = parse(xml)
                if total is None:
                    total = cnt
                if not recs:
                    break
                for r in recs:
                    r.setdefault('hit_terms', [])
                    key = r['id'] + '|' + (r.get('cle') or '')
                    if key not in seen:
                        seen[key] = r
                    seen[key]['hit_terms'].append(f'{field}:{term}')
                n += len(recs)
                frm += step
                if total and n >= 3000:
                    break
            msg = f'{field}\t{term}\tcount={total}\tfetched={n}\tunique_total={len(seen)}'
            print(msg); log.write(msg + '\n'); log.flush()
            with open('calames_hits.json', 'w', encoding='utf-8') as fh:
                json.dump(list(seen.values()), fh, ensure_ascii=False)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
