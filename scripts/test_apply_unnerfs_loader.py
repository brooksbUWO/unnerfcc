#!/usr/bin/env python3
"""Tests for apply-unnerfs.py's _load_rules(): the JSON-catalog loader that
replaces the old in-source RULES dict literal.

Run: python -m pytest scripts/test_apply_unnerfs_loader.py -q (from unnerfcc/)
Loads apply-unnerfs.py by file path (its name has a hyphen, so it is not a
plain importable module) and calls _load_rules() directly against a temp
rules/ directory built per test. Unit-level: the loader is a function, not a
CLI, so no subprocess is needed here.
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "apply-unnerfs.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("apply_unnerfs", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["apply_unnerfs"] = mod
    spec.loader.exec_module(mod)
    return mod


MOD = _load_module()


def _write_rule_file(rules_dir: Path, rule_id: str, rules: list, filename: str = None) -> Path:
    data = {"id": rule_id, "rules": rules}
    path = rules_dir / (filename or f"{rule_id}.json")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return path


def _one_rule(description="d", stock=None, unnerf=None):
    return {
        "description": description,
        "stock": stock if stock is not None else ["stock line"],
        "unnerf": unnerf if unnerf is not None else ["unnerf line"],
    }


# --- Test 1: a valid single-rule file loads to the .md-suffixed key ---

def test_single_rule_file_loads_to_md_suffixed_key(tmp_path):
    _write_rule_file(tmp_path, "my-id", [_one_rule()])
    result = MOD._load_rules(tmp_path)
    assert list(result.keys()) == ["my-id.md"]
    assert len(result["my-id.md"]) == 1
    rule = result["my-id.md"][0]
    assert rule.stock == "stock line"
    assert rule.unnerf == "unnerf line"
    assert rule.description == "d"


# --- Test 2: a body stored as a line array round-trips; a trailing "" reconstructs one trailing newline ---

def test_body_line_array_round_trips_with_trailing_newline(tmp_path):
    _write_rule_file(tmp_path, "trail-id", [
        _one_rule(stock=["line one", "line two", ""], unnerf=["single line", ""]),
    ])
    result = MOD._load_rules(tmp_path)
    rule = result["trail-id.md"][0]
    assert rule.stock == "line one\nline two\n"
    assert rule.unnerf == "single line\n"


# --- Test 3: a file with two rules loads them in array order, not re-sorted ---

def test_two_rules_load_in_array_order(tmp_path):
    _write_rule_file(tmp_path, "multi-id", [
        _one_rule(description="first", stock=["z stock"], unnerf=["z unnerf"]),
        _one_rule(description="second", stock=["a stock"], unnerf=["a unnerf"]),
    ])
    result = MOD._load_rules(tmp_path)
    rules = result["multi-id.md"]
    assert len(rules) == 2
    assert rules[0].description == "first"
    assert rules[1].description == "second"


# --- Test 4: malformed JSON exits nonzero and names the file path ---

def test_malformed_json_exits_loud(tmp_path):
    bad = tmp_path / "broken.json"
    with open(bad, "w", encoding="utf-8", newline="\n") as f:
        f.write("{not valid json")
    with pytest.raises(SystemExit) as exc_info:
        MOD._load_rules(tmp_path)
    msg = str(exc_info.value)
    assert "error:" in msg
    assert str(bad) in msg


# --- Test 5: id/filename mismatch exits nonzero and names both values ---

def test_id_filename_mismatch_exits_loud(tmp_path):
    _write_rule_file(tmp_path, "declared-id", [_one_rule()], filename="different-name.json")
    with pytest.raises(SystemExit) as exc_info:
        MOD._load_rules(tmp_path)
    msg = str(exc_info.value)
    assert "error:" in msg
    assert "declared-id" in msg
    assert "different-name" in msg


# --- Test 6: empty stock, non-string description, non-list stock, empty rules array each exit nonzero ---

def test_empty_stock_exits_loud(tmp_path):
    _write_rule_file(tmp_path, "empty-stock-id", [_one_rule(stock=[])])
    with pytest.raises(SystemExit):
        MOD._load_rules(tmp_path)


def test_non_string_description_exits_loud(tmp_path):
    _write_rule_file(tmp_path, "bad-desc-id", [_one_rule(description=123)])
    with pytest.raises(SystemExit):
        MOD._load_rules(tmp_path)


def test_stock_not_a_list_exits_loud(tmp_path):
    rule_id = "stock-not-list-id"
    data = {"id": rule_id, "rules": [{"description": "d", "stock": "not a list", "unnerf": ["u"]}]}
    path = tmp_path / f"{rule_id}.json"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with pytest.raises(SystemExit):
        MOD._load_rules(tmp_path)


def test_empty_rules_array_exits_loud(tmp_path):
    _write_rule_file(tmp_path, "empty-rules-id", [])
    with pytest.raises(SystemExit):
        MOD._load_rules(tmp_path)


# --- Test 7: an unknown extra key on a rule object loads without error ---

def test_unknown_extra_key_is_ignored(tmp_path):
    rule_id = "provenance-id"
    data = {
        "id": rule_id,
        "rules": [
            {"description": "d", "stock": ["s"], "unnerf": ["u"], "provenance": "v2.1.258 bucket-analysis"},
        ],
    }
    path = tmp_path / f"{rule_id}.json"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
    result = MOD._load_rules(tmp_path)
    assert result[f"{rule_id}.md"][0].description == "d"


# --- Regression checks: the three silent-failure modes RESEARCH.md names ---
# (Task 4: loader-contract regression checks on the untouched surfaces)

def test_loader_key_set_matches_baseline_ids_with_md_suffix():
    """Pitfall 4 guard: a loader that forgets to re-append .md makes every
    rule target a nonexistent path. Compare the live loader's key set
    against the recorded pre-refactor baseline dump's id set, each with
    .md appended."""
    baseline_path = (
        HERE.parent.parent
        / ".claude" / "workspace" / "runs" / "2026-09-02T0043" / "scratchpad"
        / "dump-rules-baseline-76b4f43.json"
    )
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline_keys = {f"{row['id']}.md" for row in baseline}
    live_keys = set(MOD.RULES.keys())
    assert live_keys == baseline_keys


def test_only_flag_resolves_exactly_one_file():
    """The --only contract still resolves: --only <id>.md --dry-run reports
    work for exactly that one file and reports no missing file. --only
    compares against the .md-suffixed key, so this proves the suffix
    survived the refactor."""
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--only", "agent-auto-mode-rule-reviewer.md", "--dry-run"],
        cwd=str(HERE.parent),
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Files processed : 1" in proc.stdout
    assert "Missing files   : 0" in proc.stdout


def test_no_loaded_body_contains_a_cr_character():
    """A stray CR makes content.replace(rule.stock, rule.unnerf, 1) silently
    fail to match; guard the whole live catalog against it."""
    for filename, rules in MOD.RULES.items():
        for rule in rules:
            assert "\r" not in rule.stock, filename
            assert "\r" not in rule.unnerf, filename


# --- Cases A-D: malformed shapes that must fail loudly, not raise AttributeError ---
# (fix-01 review: these five shapes escape today's validation and either crash
# with an uncaught AttributeError or silently load a corrupting rule.)


def test_non_object_top_level_exits_loud_case_a(tmp_path):
    """Case A: a rules/<id>.json file whose top-level JSON value is a list,
    not an object. Today: data.get("id") raises AttributeError because a
    list has no .get method. Expected: SystemExit with an error: message
    naming this file."""
    bad = tmp_path / "case-a.json"
    bad.write_text(json.dumps(["not", "an", "object"]), encoding="utf-8")
    with pytest.raises(SystemExit) as exc_info:
        MOD._load_rules(tmp_path)
    msg = str(exc_info.value)
    assert "error:" in msg
    assert str(bad) in msg


def test_non_object_rule_element_exits_loud_case_b(tmp_path):
    """Case B: a rule entry inside the "rules" array that is a string, not
    an object. Today: r.get("description") raises AttributeError because a
    string has no .get method. Expected: SystemExit with an error: message
    naming this file."""
    rule_id = "case-b"
    data = {
        "id": rule_id,
        "rules": [_one_rule(), "a stray string"],
    }
    path = tmp_path / f"{rule_id}.json"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with pytest.raises(SystemExit) as exc_info:
        MOD._load_rules(tmp_path)
    msg = str(exc_info.value)
    assert "error:" in msg
    assert str(path) in msg


def test_stock_joins_to_empty_string_exits_loud_case_c(tmp_path):
    """Case C: a "stock" array holding only one empty string, e.g. [""].
    The array is non-empty and every element is a string, so today's
    isinstance checks pass and the rule loads with Rule.stock == "". An
    empty stock string matches "" in content unconditionally at apply time,
    corrupting the target file. Expected: SystemExit with an error: message
    naming this file."""
    path = _write_rule_file(tmp_path, "case-c", [_one_rule(stock=[""])])
    with pytest.raises(SystemExit) as exc_info:
        MOD._load_rules(tmp_path)
    msg = str(exc_info.value)
    assert "error:" in msg
    assert str(path) in msg


def test_body_line_with_cr_exits_loud_case_d(tmp_path):
    """Case D: a "stock" (or "unnerf") line array element that contains a
    carriage return byte. Today it loads unchanged: the CR silently breaks
    content.replace(rule.stock, rule.unnerf) at apply time because the
    working-copy file on disk never contains a literal CR mid-line.
    Expected: SystemExit with an error: message naming this file."""
    path = _write_rule_file(
        tmp_path,
        "case-d",
        [_one_rule(stock=["a line with a \r carriage return"])],
    )
    with pytest.raises(SystemExit) as exc_info:
        MOD._load_rules(tmp_path)
    msg = str(exc_info.value)
    assert "error:" in msg
    assert str(path) in msg
