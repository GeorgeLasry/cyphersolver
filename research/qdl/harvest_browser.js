// QDL search harvest, run in a browser tab on https://www.qdl.qa (the site returns 403 to curl/WebFetch).
// Pages through /en/search/site/<query>?page=N for each query with 5 parallel workers and collects one row per
// QDL record: url, title, snippet, ref (IOR shelfmark), dates, image count, and per query the number of page
// images whose transcription matched (or 'meta' when only the description matched).
// Dump with: copy(JSON.stringify(Object.values(__qdl.recs))) -> research/qdl/hits.json
window.__qdl = window.__qdl || {recs: {}};
const Q = ['cypher', 'cipher', 'decypher', 'decipher', 'decode', 'cyphered', '"code telegram"', '"in code"',
  '"code book"', '"code words"', '"cypher telegram"', '"code word"'];
window.__q2 = {counts: {}, queue: [], fail: [], busy: 0};

function parse2(html, q) {
  const d = new DOMParser().parseFromString(html, 'text/html');
  for (const li of d.querySelectorAll('li.search-result')) {
    const a = li.querySelector('h3 a');
    if (!a) continue;
    const url = a.href.split('?')[0];
    const txt = li.innerText.replace(/\s+/g, ' ');
    const ref = (txt.match(/Ref:\s*(.*?)\s+Date\(s\):/) || [])[1] || '';
    const dates = (txt.match(/Date\(s\):\s*(.*?)(?:\s+\d[\d,]* images? ha|$)/) || [])[1] || '';
    const imgs = (txt.match(/([\d,]+) images? in record/) || [])[1] || '';
    const hitimgs = (txt.match(/([\d,]+) images? ha(?:s|ve) your search term/) || [])[1] || '';
    const r = __qdl.recs[url] || {url, title: a.innerText.trim(),
      snippet: (li.querySelector('.search-snippet') || {}).innerText?.trim() || '', ref, dates, imgs, queries: {}};
    r.queries[q] = hitimgs || 'meta';
    __qdl.recs[url] = r;
  }
  const m = html.match(/matches in <strong>([\d,]+)<\/strong> records/);
  return m ? +m[1].replace(/,/g, '') : 0;
}

(async () => {
  for (const q of Q) {
    const h = await (await fetch('/en/search/site/' + encodeURIComponent(q))).text();
    const n = parse2(h, q);
    __q2.counts[q] = n;
    for (let p = 1; p * 10 < n; p++) __q2.queue.push([q, p]);
  }
  const worker = async () => {
    while (__q2.queue.length) {
      const [q, p] = __q2.queue.shift();
      try {
        const r = await fetch('/en/search/site/' + encodeURIComponent(q) + '?page=' + p);
        if (r.status != 200) throw r.status;
        parse2(await r.text(), q);
      } catch (e) { __q2.fail.push([q, p, String(e)]); }
    }
  };
  await Promise.all([1, 2, 3, 4, 5].map(worker));
  __q2.finished = true;
})();
