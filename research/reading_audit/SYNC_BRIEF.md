# Site sync after the reading audit (23 Oct 2026)

The 22-23 Oct reading audit changed what many targets claim: documents moved between `read` and `decoded, not
read`, classes and fractions changed, readings and keys were corrected, decipherments were found, spelling was
restored. `sync_targets.tsv` lists the 137 targets whose class, fraction or number of read documents differs from
`origin/main`. The site page of each must now say exactly what the profile and NOTES say, no more.

Read first: `.claude/skills/writeup/SKILL.md` (sections 1 and 2: the page, the manifest), `README.md` Conventions
(the read bar, outcome method words), `CLAUDE.md`. The profile and the target's NOTES.md (latest dated blocks) are
the source of truth; never change a profile to fit a page.

## Per target in your list (pages only)

1. Open `targets/<folder>/profile.json`, NOTES.md (the 22-23 Oct blocks), and `docs/<slug>.html` (the slug is the
   page name; find it in `docs/_build_site.py` PAGES or by grep).
2. Make the page true to the profile:
   * the headline claim and status line: class (read / read in part / not read), the fraction read, the outcome
     method in George Lasry's words (`docs/_methods.py`); never "read" or "solved" alone as an outcome word
     (`python docs/_check_terms.py <slug>` must pass);
   * every document the page presents as read is `read` in the profile; documents now `decoded, not read` are
     described as such, with the note's reason and the partial reading labelled as partial;
   * new findings that the audit made (a decipherment found on DECODE, a printed edition, a key correction, a
     corrected attribution or date) get a sentence each, crediting the source;
   * quoted reading excerpts must match the current reading files word for word (spelling restored, holes marked);
     replace any quote that no longer matches;
   * keep image credits (`data-credit`) and the cipher snip; do not add images.
   * if a target no longer reads at all (class `not read`), the page says so plainly in its first paragraph and
     keeps the attempt's account.
3. Do not edit README.md, SOLVED_CATALOGUE.md, SOLVED_RANKING.md, catalogue.json, decode_updates/queue.json,
   docs/index.html or `_build_site.py`, and do not rebuild: one later pass does those for all targets together.
4. Never touch fr. 3029 / fr. 3092 pages or files (withheld). If a target has no page, list it and move on.
5. Write long HTML edits with the Edit tool. Stage nothing, commit nothing, no helper agents.

Reply as a table: folder / page / what changed on the page / anything the page cannot say yet (and why).
