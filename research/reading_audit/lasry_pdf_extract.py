"""Extract one of George Lasry's per-item report PDFs (24 Oct 2026) into targets/<target>/lasry/report/.

His instruction (24 Oct 2026): the decryption, the translation and the reconstructed key must be on the target's page,
immediately visible, in a format as close to the PDF as possible. This script turns the PDF into files the site
builder renders (docs/_build_site.py, lasry_report_html): the page shows them at the top of the body, in the PDF's order.

    python -I research/reading_audit/lasry_pdf_extract.py <pdf> <target>      write targets/<target>/lasry/report/
    python -I research/reading_audit/lasry_pdf_extract.py --map               all rows of lasry_pdf_map.tsv

Writes (the PDF is untrusted data: it is parsed, never executed):
    <pdf name>.pdf          the PDF as received, unchanged
    ATTRIBUTION.md          who made it, when it was received, the licence note
    summary.md              title, Contents, status line, the labelled fields (Ciphertext-only, Sender, Recipient,
                            Year, Key, Ciphertext, ...), the Gallica links
    excerpt.md              each excerpt, with its folio label and its manuscript-line image(s)
    translation_excerpt.md  the translation of each excerpt
    readable.md             "Readable text": the full text by folio (## <folio>); **bold** as in the PDF, where the
                            bold marks the deciphered passages
    key.md                  only when the key is given as text (a page headed "Key ...")
    images/                 key_N.<ext> (the key tables before the excerpts), leaf_N.<ext> (manuscript lines),
                            other_N.<ext> (e.g. a printed page after the readable text)
    images.json             one record per image: file, kind, page, caption, w, h
"""
import json, pathlib, re, shutil, sys

import pymupdf

ROOT = pathlib.Path(__file__).resolve().parents[2]
MAP = ROOT / 'research' / 'reading_audit' / 'lasry_pdf_map.tsv'
RECEIVED = '2026-10-24'
FOOTER = 7.0          # font size of the running footer ("Title  n / N")


def is_bold(span): return 'Bold' in span['font'] or bool(span['flags'] & 16)


def items(doc):
    """The PDF as a stream of ('line', page, size, [(text, bold)], bbox) and ('img', page, xref, bbox)."""
    out = []
    for pn, page in enumerate(doc):
        xrefs = {tuple(round(v) for v in i['bbox']): i['xref'] for i in page.get_image_info(xrefs=True)}
        links = [(pymupdf.Rect(l['from']), l['uri']) for l in page.get_links() if l.get('uri')]
        for b in page.get_text('dict', sort=True)['blocks']:
            if b['type'] == 1:
                bb = tuple(round(v) for v in b['bbox'])
                xr = xrefs.get(bb) or next((x for k, x in xrefs.items() if all(abs(a - c) < 3 for a, c in zip(k, bb))), None)
                out.append(('img', pn + 1, xr, b['bbox']))
                continue
            for l in b['lines']:
                spans = [s for s in l['spans'] if s['text']]
                if not spans: continue
                size = max(s['size'] for s in spans)
                if size < FOOTER: continue
                uris = [u for r, u in links if r.intersects(pymupdf.Rect(l['bbox']))]
                segs, prev = [], None
                for s in spans:      # a visible gap between two spans is a word space the PDF does not encode
                    if prev and s['bbox'][0] - prev['bbox'][2] > 0.15 * s['size'] \
                            and not prev['text'].endswith(' ') and not s['text'].startswith(' '):
                        segs.append((' ', is_bold(prev) and is_bold(s)))
                    segs.append((s['text'], is_bold(s))); prev = s
                out.append(('line', pn + 1, size, segs, l['bbox'], uris))
    return out


def text_of(segs): return ''.join(t for t, _ in segs)


def md(segs):
    """Segments to markdown, bold runs merged and their edge spaces moved outside the markers."""
    runs = []
    for t, b in segs:
        if runs and runs[-1][1] == b: runs[-1][0] += t
        else: runs.append([t, b])
    out = ''
    for t, b in runs:
        if b and t.strip():
            lead, core, trail = re.match(r'^(\s*)(.*?)(\s*)$', t, re.S).groups()
            out += f'{lead}**{core}**{trail}'
        else: out += t
    return out.replace('****', '')


def join_lines(lines):
    """Lines of one paragraph to one string: segments joined with a space, a hyphen at a line end kept as is."""
    segs = []
    for l in lines:
        if segs:
            last = segs[-1][0]
            if not last.endswith((' ', '-')) and not l[0][0].startswith(' '): segs.append((' ', segs[-1][1] and l[0][1]))
        segs.extend(l)
    return md(segs).strip()


def extract(pdf, target):
    pdf = pathlib.Path(pdf)
    doc = pymupdf.open(pdf)
    out = ROOT / 'targets' / target / 'lasry' / 'report'
    if out.exists(): shutil.rmtree(out)
    (out / 'images').mkdir(parents=True)
    shutil.copyfile(pdf, out / pdf.name)
    stream = items(doc)

    # --- sections: summary (to "Excerpt and Translation" / "Manuscript lines"), excerpts (to "Readable text"), readable
    def find(pred, start=0):
        return next((i for i in range(start, len(stream)) if stream[i][0] == 'line' and pred(stream[i])), None)
    i_ex = find(lambda x: text_of(x[3]).strip() in ('Excerpt and Translation', 'Excerpt', 'Manuscript lines'))
    i_rd = find(lambda x: text_of(x[3]).strip() == 'Readable text')
    if i_ex is None: i_ex = i_rd
    if i_rd is None: raise SystemExit(f'{pdf.name}: no "Readable text" heading')
    summary, excerpts, readable = stream[:i_ex], stream[i_ex:i_rd], stream[i_rd + 1:]

    images, counts = [], {'key': 0, 'leaf': 0, 'other': 0}
    seen = {}
    def save_img(it, kind, caption):
        xr = it[2]
        if xr is None: return None
        if xr in seen: return seen[xr]
        counts[kind] += 1
        info = doc.extract_image(xr)
        ext = info.get('ext', 'png')
        if info.get('smask') or ext not in ('png', 'jpeg', 'jpg'):
            pix = pymupdf.Pixmap(doc, xr)
            if pix.alpha or pix.n > 3: pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            data, ext = pix.tobytes('png'), 'png'
        else: data = info['image']
        ext = 'jpg' if ext == 'jpeg' else ext
        name = f'{kind}_{counts[kind]}.{ext}'
        (out / 'images' / name).write_bytes(data)
        rec = dict(file=f'images/{name}', kind=kind, page=it[1], caption=caption, w=info.get('width'), h=info.get('height'))
        images.append(rec); seen[xr] = rec
        return rec

    # --- summary.md
    title = text_of(summary[0][3]).strip() if summary else pdf.stem
    fields, contents, status, links, extra, cur = [], '', '', [], [], None
    for it in summary[1:]:
        if it[0] == 'img':
            save_img(it, 'key', 'Key reconstructed by George Lasry'); continue
        segs, uris = it[3], it[5]
        txt = text_of(segs).strip()
        if uris:
            for u in uris:
                if u not in [x[1] for x in links]: links.append((txt, u))
            continue
        if segs[0][1] and ':' in segs[0][0]:          # "Label:" in bold, then the value
            label = segs[0][0].strip().rstrip(':').strip()
            val = text_of(segs[1:]).strip()
            if label == 'Contents': cur = ['Contents', val]; contents = cur
            else: cur = [label, val]; fields.append(cur)
            continue
        if cur is not None and not status and cur is contents and not re.search(r'transcribed|deciphered|Transcribed|Deciphered', txt):
            cur[1] += ' ' + txt; continue
        if not status and re.search(r'transcribed|deciphered', txt, re.I):
            status = txt; cur = None; continue
        if cur is not None: cur[1] += ' ' + txt
        else: extra.append(txt)
    # split "Gallica f40r Gallica f43r" style link lines: one line per link, labelled by the folio in the URL
    gl = []
    for txt, u in links:
        m = re.search(r'/f(\d+)\.item', u)
        gl.append((u, m.group(1) if m else ''))
    lab = [x for x in re.findall(r'(f\d+[rv]|p\d+)', ' '.join(t for t, _ in links))]
    S = [f'# {title}', '', f'Source: George Lasry, report PDF `{pdf.name}` (received {RECEIVED}), page 1.', '']
    if contents: S += [f'**Contents:** {contents[1].strip()}', '']
    if status: S += [status, '']
    for k, v in fields: S.append(f'- **{k}:** {re.sub(r"\s+", " ", v).strip()}')
    for t in extra: S.append(f'- {t}')
    S.append('')
    for n, (u, view) in enumerate(gl):
        S.append(f'- Gallica {lab[n] if n < len(lab) else ""} (view {view}): <{u}>'.replace('  ', ' '))
    (out / 'summary.md').write_text('\n'.join(S).rstrip() + '\n', encoding='utf-8')
    meta = dict(title=title, contents=contents[1].strip() if contents else '', status=status,
                fields=[[k, re.sub(r'\s+', ' ', v).strip()] for k, v in fields], extra=extra,
                gallica=[dict(label=lab[n] if n < len(lab) else '', view=v, url=u) for n, (u, v) in enumerate(gl)],
                pdf=pdf.name, received=RECEIVED)

    # --- excerpts: "Excerpt" / folio label / image(s) / text / "Translation" / text, repeated
    pairs, cur, mode, pending_imgs, para = [], None, None, [], []
    def flush():
        nonlocal para
        if cur is not None and para and mode in ('ex', 'tr'):
            cur[mode].append(join_lines(para))
        para = []
    last_y = None
    for it in excerpts:
        if it[0] == 'img':
            flush()
            rec = save_img(it, 'leaf', '')
            if rec and rec not in pending_imgs: pending_imgs.append(rec)
            continue
        txt, size = text_of(it[3]).strip(), it[2]
        if txt in ('Excerpt and Translation', 'Manuscript lines'): flush(); mode = None; continue
        if txt == 'Excerpt':
            flush(); cur = dict(folio='', ex=[], tr=[], imgs=list(pending_imgs)); pending_imgs = []
            pairs.append(cur); mode = 'ex'; continue
        if txt == 'Translation': flush(); mode = 'tr'; continue
        if size < 9.5 and cur is not None and mode == 'ex' and not cur['ex'] and not para:   # the folio label
            cur['folio'] = (cur['folio'] + ' ' + txt).strip(); continue
        if cur is None: continue
        if pending_imgs: cur['imgs'] += pending_imgs; pending_imgs = []
        y = it[4][1]
        if para and last_y is not None and y - last_y > 1.9 * size: flush()
        para.append(it[3]); last_y = it[4][3]
    flush()
    for p in pairs:
        for r in p['imgs']:
            if not r['caption']: r['caption'] = p['folio']
    E = [f'# {title}: excerpt', '', f'George Lasry, report PDF `{pdf.name}`, "Excerpt and Translation".', '']
    T = [f'# {title}: translation of the excerpt', '', f'George Lasry, report PDF `{pdf.name}`, "Excerpt and Translation".', '']
    for n, p in enumerate(pairs, 1):
        h = f'## Excerpt {n}' + (f' ({p["folio"]})' if p['folio'] else '')
        E += [h, ''] + [f'![{p["folio"]}]({r["file"]})' for r in p['imgs']] + ([''] if p['imgs'] else []) + sum(([x, ''] for x in p['ex']), [])
        T += [h.replace('Excerpt', 'Translation', 1), ''] + sum(([x, ''] for x in p['tr']), [])
    (out / 'excerpt.md').write_text('\n'.join(E).rstrip() + '\n', encoding='utf-8')
    (out / 'translation_excerpt.md').write_text('\n'.join(T).rstrip() + '\n', encoding='utf-8')
    meta['excerpts'] = [dict(folio=p['folio'], excerpt=p['ex'], translation=p['tr'], images=[r['file'] for r in p['imgs']]) for p in pairs]

    # --- readable.md: size >= 15 a title (#), 12-15 a folio or part heading (##), body paragraphs by vertical gaps
    R = [f'<!-- George Lasry, report PDF {pdf.name} (received {RECEIVED}), "Readable text". Bold as in the PDF. -->', '']
    para, last, last_pg, keylines, in_key = [], None, None, [], False
    def rflush():
        nonlocal para
        if para: R.extend([join_lines(para), ''])
        para = []
    for it in readable:
        if it[0] == 'img':
            rflush()
            # caption: the next small line below the image
            rec = save_img(it, 'other', '')
            if rec: R.extend([f'![{rec["kind"]}]({rec["file"]})', ''])
            continue
        txt, size, bb = text_of(it[3]).strip(), it[2], it[4]
        if rec_caption(images, it): continue
        if size >= 15: rflush(); R.extend([f'# {txt}', '']); in_key = False; last = None; continue
        if size >= 12:
            rflush(); in_key = txt.lower().startswith('key'); R.extend([f'## {txt}', '']); last = None; continue
        if in_key: keylines.append(txt)
        same_page = last is not None and last_pg == it[1]
        if para and same_page and (bb[1] - last[3] > 0.9 * size or bb[1] < last[1]): rflush()   # a page break joins
        para.append(it[3]); last = bb; last_pg = it[1]
    rflush()
    (out / 'readable.md').write_text('\n'.join(R).rstrip() + '\n', encoding='utf-8')
    if keylines: (out / 'key.md').write_text(f'# {title}: key\n\n' + '\n'.join(keylines) + '\n', encoding='utf-8')
    meta['images'] = images
    (out / 'images.json').write_text(json.dumps(images, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'report.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'ATTRIBUTION.md').write_text(
        f'# Attribution\n\n`{pdf.name}` is George Lasry\'s report on this item ("{title}"), sent to Daniel Bourdeau on '
        f'{RECEIVED} with the instruction that the decryption, the translation and the reconstructed key be shown on '
        'the item\'s page. The decipherment, the translation and the key reconstruction are his (made with ChatGPT '
        'Astra 6 and Anthropic Opus 5.5). The manuscript images are from the Bibliothèque nationale de France, via '
        'Gallica. The other files in this folder were extracted from the PDF by '
        '`research/reading_audit/lasry_pdf_extract.py`, without editing.\n', encoding='utf-8')
    return meta


def rec_caption(images, it):
    """A small line right under an 'other' image is its caption."""
    if not images or images[-1]['kind'] != 'other' or images[-1]['caption']: return False
    if it[2] < 9.5 and images[-1]['page'] == it[1]:
        images[-1]['caption'] = text_of(it[3]).strip(); return True
    return False


if __name__ == '__main__':
    if sys.argv[1:2] == ['--map']:
        src = pathlib.Path(sys.argv[2])
        for row in MAP.read_text(encoding='utf-8').splitlines()[1:]:
            pdf, target = row.split('\t')[:2]
            if not target or target.startswith('?'): continue
            m = extract(src / pdf, target)
            print(target, len(m['excerpts']), 'excerpts', len(m['images']), 'images')
    else:
        m = extract(sys.argv[1], sys.argv[2])
        print(sys.argv[2], len(m['excerpts']), 'excerpts', len(m['images']), 'images', m['title'])
