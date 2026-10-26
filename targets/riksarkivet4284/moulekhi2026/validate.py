"""Offline deterministic reproduction and retrospective controls (Python 3.9+).

No fitted model, accepted split corrections, network access, or input writes.
The excerpt score is deliberately labelled post-selection; it is not accuracy.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import re
import statistics

ROOT = Path(__file__).resolve().parent
SEED = 428424
REPEATS = 1000
# These excerpts were already inspected before this protocol was written.
EXCERPTS = (
    ([28], "nobisetpatriaesecurum"),
    ([33, 34], "beflitaederatdetmotteskee"),
    ([45, 46], "arfwingarsomförsinawennerochförwanter"),
    ([50, 51], "communiceramedederfördennagången"),
)


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(name):
    result = []
    for number, raw in enumerate((ROOT / name).read_text(encoding="utf-8-sig").splitlines(), 1):
        if raw.startswith("## IMG_R4284_I25751_P_hi.jpeg right"):
            break
        if not raw.strip() or raw.startswith("#"):
            continue
        result.append((number, re.findall(
            r"\[[^]]*\]|\d+\?*|\?+", re.sub(r"\([^)]*\)", "", raw)
        )))
    return result


def render(token, key):
    if token.startswith("["):
        return " " + token + " "
    return key.get(token, "<" + token + ">") if "?" not in token else "<" + token + ">"


def decode(source, key):
    counts = Counter()
    output = []
    for number, tokens in source:
        for token in tokens:
            category = (
                "clear_spans" if token.startswith("[") else
                "uncertain_numeric" if "?" in token else
                "assigned_numeric" if token in key else
                "unresolved_numeric"
            )
            counts[category] += 1
        output.append({"line": number, "literal": "".join(render(t, key) for t in tokens)})
    denominator = sum(value for category, value in counts.items() if category != "clear_spans")
    return {
        "counts": dict(counts), "numeric_denominator": denominator,
        "alphabet_coverage": counts["assigned_numeric"] / denominator if denominator else None,
        "accuracy": None,
        "accuracy_reason": "No independently adjudicated reference plaintext.",
        "literal_lines": output,
    }


def excerpt_positions(source, key):
    """Locate fixed post-selected excerpts without including any clear text."""
    by_line = dict(source)
    selected = []
    for line_numbers, expected in EXCERPTS:
        symbols = [token for line in line_numbers for token in by_line[line]]
        chars, coordinates = [], []
        for index, token in enumerate(symbols):
            # Unknown, clear-script and ambiguous tokens are barriers.
            char = key.get(token, "")
            chars.append(char if len(char) == 1 else "|")
            coordinates.append(index)
        text = "".join(chars)
        if text.count(expected) != 1:
            raise ValueError("Excerpt is absent or non-unique")
        start = text.index(expected)
        selected.append({
            "lines": line_numbers, "expected": expected,
            "indices": coordinates[start:start + len(expected)],
        })
    return selected


def score(source, key, selected):
    by_line = dict(source)
    correct = total = 0
    for excerpt in selected:
        tokens = [token for line in excerpt["lines"] for token in by_line[line]]
        for index, expected in zip(excerpt["indices"], excerpt["expected"]):
            correct += key.get(tokens[index]) == expected
            total += 1
    return correct, total


def permute_labels(key, rng):
    """Preserve value coverage and each letter's number of homophones."""
    values = sorted(key, key=int)
    labels = [key[value] for value in values]
    rng.shuffle(labels)
    return dict(zip(values, labels))


def shuffle_positions(source, key, rng):
    """Shuffle only mapped numeric positions within each line.

    Clear spans, uncertain tokens and unmapped groups stay at their positions.
    Line lengths and per-line mapped-token multisets are unchanged.
    """
    result = []
    for number, tokens in source:
        changed = tokens.copy()
        positions = [index for index, token in enumerate(tokens) if token in key]
        values = [tokens[index] for index in positions]
        rng.shuffle(values)
        for index, value in zip(positions, values):
            changed[index] = value
        result.append((number, changed))
    return result


def summarize(values, observed):
    ordered = sorted(values)
    return {
        "replicates": len(values), "minimum": min(values), "maximum": max(values),
        "mean": statistics.mean(values), "median": statistics.median(values),
        "empirical_95th_percentile": ordered[int(0.95 * (len(values) - 1))],
        "replicates_at_least_observed": sum(value >= observed for value in values),
        "inference": "Descriptive only; post-selected score, not a confirmatory p-value.",
    }


def validate():
    key = load("key.json")["alphabet"]
    original = rows("original_transcription.txt")
    reviewed = rows("reviewed_transcription.txt")
    # Exclude the known repeated line from all control trials.
    control_source = [(n, tokens) for n, tokens in reviewed if n != 16]
    selected = excerpt_positions(control_source, key)
    observed, total = score(control_source, key, selected)
    key_rng, order_rng = random.Random(SEED), random.Random(SEED + 1)
    label_scores, order_scores = [], []
    for _ in range(REPEATS):
        label_scores.append(score(control_source, permute_labels(key, key_rng), selected)[0])
        order_scores.append(score(shuffle_positions(control_source, key, order_rng), key, selected)[0])
    continuation = [(n, tokens) for n, tokens in reviewed if 49 <= n <= 52]
    groups = load("group_decisions.json")
    return {
        "protocol": "Retrospective validation v1; specified 2026-10-24 after plaintext inspection",
        "original": decode(original, key),
        "reviewed": decode(reviewed, key),
        "reviewed_without_repeated_line16": decode(control_source, key),
        "continuation_49_52": {
            "status": "Previously inspected passage; NOT held-out.",
            **decode(continuation, key),
        },
        "group_classifications": dict(Counter(g["classification"] for g in groups)),
        "independently_verified_coherent_tokens": None,
        "independently_verified_scribal_slips": None,
        "flagged_anomaly_sites": load("anomalies.json"),
        "controls": {
            "seed_label_shuffle": SEED, "seed_position_shuffle": SEED + 1,
            "repetitions_per_control": REPEATS,
            "metric": "Exact character matches at fixed post-selected excerpt positions",
            "observed_matching_positions": observed, "scored_positions": total,
            "excerpts": selected,
            "label_shuffle": summarize(label_scores, observed),
            "within_line_position_shuffle": summarize(order_scores, observed),
            "raw_label_shuffle_scores": label_scores,
            "raw_position_shuffle_scores": order_scores,
            "coverage_warning": "Both controls preserve coverage: coverage cannot distinguish keys.",
            "bias_warning": (
                "Excerpts were selected from readable output. No independent language/coherence "
                "score or multiple-candidate search correction; no novelty/accuracy inference."
            ),
        },
        "independent_transcription": {
            "completed_lines": 0, "required_numeric_lines": 41,
            "status": "Pending independent blind image transcription; ledger is not a transcription.",
        },
    }


def check_integrity():
    manifest = load("manifest.json")
    actual = {p.name for p in ROOT.iterdir() if p.is_file() and p.name != "manifest.json"}
    if actual != set(manifest["files"]):
        raise ValueError("Unexpected or missing package files")
    for name, expected in manifest["files"].items():
        if sha(ROOT / name) != expected:
            raise ValueError("File fingerprint mismatch: " + name)
    return "PASS: package file set and SHA-256 fingerprints"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    report = validate()
    if args.check:
        report["integrity"] = check_integrity()
        stored = load("validation_results.json")
        if {k: v for k, v in report.items() if k != "integrity"} != stored:
            raise ValueError("Generated results differ from recorded results")
    if args.summary:
        for section in ("original", "reviewed", "reviewed_without_repeated_line16", "continuation_49_52"):
            report[section].pop("literal_lines")
        for field in ("raw_label_shuffle_scores", "raw_position_shuffle_scores", "excerpts"):
            report["controls"].pop(field)
    print(json.dumps(report, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
