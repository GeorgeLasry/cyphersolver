# Draft: invitation to work on cipher families together

Status: draft, not sent. Daniel and George decide who receives it and whether it goes out.

---

Subject: Working together on whole cipher families

Dear [name],

Terence Tao's World View in *Nature* this week (22 Oct 2026) argues that AI tools should be aimed at problems too
interconnected for any one person or system, and that credit should go to understanding and process, not only to
being first. In historical cryptology our equivalent is the cipher family: one chancery's keys and the letters
written in them, scattered across archives and partly read by different people over decades.

We have grouped the cyphersolver targets into families by shared key (`research/families/FAMILIES.md`).
[Family name] has [n] letters, [r] read and [o] still open, and it rests on keys you published or hold:
[keys]. We would rather finish it with you than around you. Concretely:

- we hold back from publishing new readings in this family until you have seen them, and credit your keys and
  corrections on every page and in the DECODE updates;
- the transcriptions, keys and solution logs are open (`docs/data/`), so you can check every step without us;
- open letters and their untried leads are listed, and you can take any of them, including ones you would like to
  keep for a student.

If you would rather we leave the family alone for now, say so and we will mark it reserved.

With best wishes,
Daniel Bourdeau [and George Lasry]

---

## Families and who to ask (from FAMILIES.md; check before sending)

| family | open/total | people already on the keys |
|---|---|---|
| Lasry's French keys (GL.htm), 1529-86 | 13/19 | George Lasry, Satoshi Tomokiyo |
| BL Add MS 32264 / Dutch envoys, 1765-1803 | 8/15 | DECODE team |
| Borghesi's key, Siena/Naples 1420-1550 | 7/11 | George Lasry |

## Reserving targets for students

A target can be marked reserved in `catalogue.json` with `"reserved": "<who or why>"`. Reserved targets are left
out of automated attempts and lead lists. This is not implemented yet and needs a decision first.
