"""Verify the contributed CTTS transcription and full-letter edition.

Run with Python 3. No nonstandard packages are required.
"""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import hashlib
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent


def check():
    data = json.loads((ROOT / "edition.json").read_text(encoding="utf-8"))
    colors = [s.split(";") for s in (ROOT / "ctts/colors.txt").read_text().splitlines()]
    key = {}
    for line in (ROOT / "ctts/key.txt").read_text().splitlines():
        if " - " in line:
            labels, value = line.split(" - ")
            for label in labels.split("|"):
                assert label not in key, f"Duplicate key label: {label}"
                key[label] = value.lower()
    source = []
    for line in (ROOT / "ctts/positions.txt").read_text().splitlines():
        if not line.strip():
            continue
        x, y, w, h, c = line.split()
        source.append((float(x), float(y), float(w), float(h), int(c)))
    actual, cipher = [], Counter()
    edited, letter_text = [], []
    tr = (ROOT / "ctts/transcription.txt").read_text().splitlines()[1:-1]
    dc = (ROOT / "ctts/decryption.txt").read_text().splitlines()[1:-1]
    assert len(data["rows"]) == len(tr) == len(dc) == 11
    clear_count = 0
    for row, transcribed, decrypted in zip(data["rows"], tr, dc):
        boxes = row["boxes"]
        assert transcribed.endswith(";")
        assert transcribed[:-1].split(";") == [b["label"] for b in boxes]
        assert decrypted.split() == [b["value"] for b in boxes]
        for b in boxes:
            rect = tuple(b[k] for k in ("x", "y", "w", "h", "c"))
            actual.append(rect)
            assert colors[b["c"]][1] == b["label"]
            assert key[b["label"]] == b["value"]
            if b["label"] == "[Plaintext]":
                clear_count += 1
            else:
                cipher[b["label"]] += 1
                icon = ROOT / "ctts/icons" / (colors[b["c"]][0] + ".png")
                assert icon.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"), str(icon)
        covered, parts = [], []
        for s in row["segments"]:
            a, b = s["tokens"]
            covered += list(range(a, b+1))
            selected = boxes[a-1:b]
            if s["kind"] == "clear":
                assert all(x["label"] == "[Plaintext]" for x in selected)
            else:
                assert s["kind"] == "cipher"
                assert all(x["label"] != "[Plaintext]" for x in selected)
                assert s["text"].replace(" ", "") == "".join(x["value"] for x in selected)
            parts.append(s["text"])
        assert covered == list(range(1, len(boxes)+1)), f"Coverage: line {row['line']}"
        joined = " ".join(parts)
        letter_text.append(joined)
        edited.append(f'{row["line"]}|{joined}')
    assert Counter(actual) == Counter(source), "Position/edition geometry mismatch"
    assert (ROOT / "edited.txt").read_text(encoding="utf-8") == "\n".join(edited) + "\n"
    raw_lines = (ROOT / "cipher_tokens.txt").read_text().splitlines()
    assert len(raw_lines) == 11
    for row, raw in zip(data["rows"], raw_lines):
        assert raw.split()[0] == f'L{row["line"]:02d}:'
        assert raw.split()[1:] == [b["label"] for b in row["boxes"] if b["label"] != "[Plaintext]"]
    assert len(actual) == 438 and clear_count == 10 and sum(cipher.values()) == 428 and len(cipher) == 52
    assert sum(n for label, n in cipher.items() if key[label] == "?") == 29
    assert len([label for label in cipher if key[label] == "?"]) == 12

    class EditionHTML(HTMLParser):
        def __init__(self):
            super().__init__()
            self.in_line = False
            self.current = ""
            self.lines = []
            self.images = []
            self.sections = 0
            self.strong = False
            self.in_number = False
            self.runs = []
            self.kind_text = []
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "section":
                self.sections += 1
            if tag == "img":
                self.images.append(attrs)
            if tag == "p" and attrs.get("class") == "letter-line":
                self.in_line = True
                self.current = ""
                self.kind_text = []
            if self.in_line and tag == "span":
                self.in_number = True
            if self.in_line and tag == "strong":
                self.strong = True
        def handle_endtag(self, tag):
            if tag == "strong":
                self.strong = False
            if tag == "span":
                self.in_number = False
            if tag == "p" and self.in_line:
                self.lines.append(self.current.strip())
                self.runs.append(self.kind_text)
                self.in_line = False
        def handle_data(self, value):
            if self.in_line and not self.in_number:
                self.current += value
                if value.strip():
                    self.kind_text.append(("cipher" if self.strong else "clear", value.strip()))
    parsed = EditionHTML()
    parsed.feed((ROOT / "cryptiana/maino1446.html").read_text(encoding="utf-8"))
    assert parsed.sections == 1 and len(parsed.images) == 2
    assert parsed.lines == letter_text, "HTML letter differs from aligned edition"
    for row, runs in zip(data["rows"], parsed.runs):
        want = []
        for segment in row["segments"]:
            if want and want[-1][0] == segment["kind"]:
                want[-1] = (want[-1][0], want[-1][1] + " " + segment["text"])
            else:
                want.append((segment["kind"], segment["text"]))
        assert runs == want, f"Cipher/clear bolding mismatch: line {row['line']}"
    for image in parsed.images:
        assert image.get("alt")
        assert (ROOT / "cryptiana" / image["src"]).is_file()
    for rel, expected in json.loads((ROOT / "manifest.json").read_text())["files"].items():
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == expected, rel

    repo = ROOT.parents[2]
    if (repo / "docs/_check_profile.py").is_file():
        sys.path.insert(0, str(repo / "docs"))
        import _check_profile as profile
        proposal = json.loads((ROOT / "Codex_profile_proposal.json").read_text(encoding="utf-8"))
        errors, gaps = [], []
        profile.validate(proposal, profile.SCHEMA, "", errors, gaps)
        errors += profile.credit_errors(proposal)
        assert not errors, errors
        print(f"Proposed profile: schema and contributor checks passed ({len(gaps)} explicit unknown fields).")
    print("PASS: 438 positions; 428 cipher signs / 52 classes; 399 assigned / 29 unresolved;")
    print("all ten clear-text boxes, eleven edited lines, bold/clear HTML spans, icons, images and checksums agree.")


if __name__ == "__main__":
    check()
