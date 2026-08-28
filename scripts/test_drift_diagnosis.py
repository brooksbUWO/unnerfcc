#!/usr/bin/env python3
"""Runnable check for apply-unnerfs._drift_diagnosis (the [FAILED]-message helper).

Assert-based, stdlib only, no framework. Run: python3 test_drift_diagnosis.py
Exit 0 = all cases pass; a failing assert exits nonzero and names the case.

The helper shows HOW a rule's stock text drifted from the current file when a
splice would FAIL: it finds the closest block and diffs expected-vs-current, so
a version-upgrade session sees the real drift (e.g. a bare ${} that upstream
renamed to ${GREP_TOOL_NAME}) without opening the file.
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("apply_unnerfs", HERE / "apply-unnerfs.py")
mod = importlib.util.module_from_spec(spec)
sys.modules["apply_unnerfs"] = mod
spec.loader.exec_module(mod)
drift = mod._drift_diagnosis


def test_small_drift_shows_diff():
    stock = "Content search built on ripgrep. Prefer this over grep.\nSecond line stays.\n"
    content = "Header\nContent search built on ripgrep. Use this instead of grep.\nSecond line stays.\nFooter\n"
    out = drift(stock, content)
    assert "diff expected-stock" in out, out
    assert "Prefer this over grep" in out, out       # the expected (removed) line
    assert "Use this instead of grep" in out, out     # the current (added) line
    assert "similarity" in out, out


def test_placeholder_rename_drift():
    # The real grep-compact case: bare ${} in stock, named ${GREP_TOOL_NAME} in file.
    stock = "ripgrep via ${} results here.\n"
    content = "ripgrep via ${GREP_TOOL_NAME} results here.\n"
    out = drift(stock, content)
    assert "${GREP_TOOL_NAME}" in out, out
    assert "diff expected-stock" in out, out


def test_wholesale_removal_reports_no_block():
    stock = "A unique passage zzz qqq appearing nowhere else.\n"
    content = "Totally different.\nNothing alike.\n"
    out = drift(stock, content)
    assert "No block in the file resembles" in out, out


def test_empty_inputs_do_not_crash():
    assert "No overlapping content" in drift("", "abc\n")
    assert "No overlapping content" in drift("abc\n", "")


def main():
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"OK  {name}")
    print("ALL DRIFT-DIAGNOSIS CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
