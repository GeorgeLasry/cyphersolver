# Brief: transcribe Van Reede's code passages exactly (KHA A35-1232, A32-549; 1796-1807)

Folder: C:\Users\dbour\cypher\targets\reede1796. Fetch each page at full size:
  curl -sL -A "Mozilla/5.0 Chrome/120" -o full/<id>.jpg "https://cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/original/"
(mkdir full first). View in horizontal strips (python PIL crops of about 1/6 page height at full width, saved in
your scratch folder, Read tool); zoom to 2x on the number lines: the small marks matter.

Arend Willem van Reede writes to the Hereditary Prince (later Willem I) in French. Code passages are groups of
1-4 digits, often written in black over faint brown invisible-ink text (ignore the brown text, but note it).

Notation, one group per item, space separated, exactly as written:
- N.p.q   a number followed by small numbers joined by dots or commas (keep them as .p.q)
- k)N     a small number written top-left of N (often with a slash: k/N)
- N^k     a small number top-right of N (often after a bracket "(k")
- N/k     a small number written under N (a fraction-like stroke)
- underline under the whole number: N_ ; under one digit d (1-based): N{u3}; double/triple: {uu3} {uuu3}
- prime or accent above/after a digit: N{'3}; bar over: N{bar} ; '+' : N{+}
- unreadable: ?
Write any clear word inside a run as [word].

For each passage:

    # id <id> run <k>  <date/heading if any>
    BEFORE: <clear words before, up to 12>
    CT: <groups>
    AFTER: <clear words after, up to 12>
    PT: <any decipherment written over or after the run, else none>

ASCII only. Append each block as soon as done. Final reply: per page, runs, groups, notes on the marks.
