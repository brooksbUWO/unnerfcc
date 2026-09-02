#!/usr/bin/env python3
"""
apply-unnerfs.py — Re-apply every un-nerf in this repo to a system-prompts tree.

WHY THIS EXISTS
---------------
tweakcc extracts Claude Code's system prompts into editable `.md` files so they
can be hand-patched. Whenever tweakcc re-runs against a newer Claude Code
binary (new ccVersion), it overwrites every changed prompt with fresh STOCK
text — wiping any un-nerfs applied on top. This script idempotently re-applies
every un-nerf against the current working copy of `system-prompts/`, restoring
the full un-nerfed state.

USAGE
-----
    python scripts/apply-unnerfs.py                  # apply to ./system-prompts/
    python scripts/apply-unnerfs.py --dir PATH       # target another directory
    python scripts/apply-unnerfs.py --dry-run        # report without writing
    python scripts/apply-unnerfs.py --check          # exit 1 if anything would change
    python scripts/apply-unnerfs.py --only FILE      # restrict to one filename
    python scripts/apply-unnerfs.py --verbose        # include context on skipped rules

EXIT CODES
----------
    0  — no failures, no missing files
    1  — at least one rule failed to apply OR at least one file was missing
         (in --check mode, 1 also means "at least one rule would apply")
    2  — invalid invocation (e.g. --dir doesn't exist)

ADDING A NEW RULE (FOR A FUTURE CLAUDE CODE VERSION BUMP)
---------------------------------------------------------
1. Run this script first. Read the [FAIL] section — it names every file whose
   expected stock text isn't in the working copy anymore.
2. For each failure:
   a. Open the file and find the new stock text that replaced the old one.
   b. Craft the un-nerfed replacement (typically: flip brevity → thoroughness
      per the repo's README thesis).
   c. Update the relevant RULES[filename] entry: change the `stock` string to
      the new upstream text; keep or update the `unnerf` string.
3. For brand-new files (ccVersion = the new release, no predecessor): decide
   whether any un-nerf applies. Many new prompts are structured data generators
   (inbox summaries, classification outputs) where length caps are UX-driven,
   not brevity-nerf-driven — those should be left stock. Add a rule only when
   a brevity directive for *implementation*, *process*, or *thoroughness*
   (per the README's bucket taxonomy) is present.
4. Re-run the script. Confirm all entries report [APPLIED] or [SKIP].
5. Commit both the rule change and the re-applied prompt files together.

HOW A RULE WORKS
----------------
Each rule is a (stock, unnerf, description) triple keyed by filename. The
script:
  - If `stock` is present in the file → replace it (once) with `unnerf`. Result: APPLIED.
  - Else if `unnerf` is present → no-op (rule already applied earlier). Result: SKIP.
  - Else → loud failure. Result: FAIL, with the expected stock text quoted so
    the reader knows exactly what to search for and update.

This idempotency is intentional: you can run the script repeatedly, after any
tweakcc re-extract, and it will converge to the un-nerfed state regardless of
how many un-nerfs were already in place.

REPORT FORMAT (READ BY CLAUDE AND HUMANS)
-----------------------------------------
For each file:
    system-prompts/<filename>
      [APPLIED] <rule description>
      [SKIP]    <rule description>                     — already un-nerfed
      [FAIL]    <rule description>
                Expected stock text (first 200 chars):
                  '...'
                Neither stock nor unnerf text found in file.
                Action: open the file, locate the relevant passage, and update
                the rule's `stock` field in that id's rules/<id>.json to match the new wording.

And a final `=== Summary ===` block with totals + exit code.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

SCRIPT_VERSION = "1.0"
DEFAULT_PROMPTS_DIR = Path(__file__).resolve().parent.parent / "system-prompts"
RULES_DIR = Path(__file__).resolve().parent.parent / "rules"


@dataclass(frozen=True)
class Rule:
    """One un-nerf replacement: stock → unnerf."""
    stock: str          # Exact text as it appears in tweakcc-extracted STOCK
    unnerf: str         # Exact un-nerfed replacement (what HEAD should contain)
    description: str    # Short human-readable label shown in the report


@dataclass
class Result:
    """Outcome of applying one Rule to one file."""
    filename: str
    status: str                           # "applied" | "skipped" | "failed" | "missing"
    rule_description: str
    detail: Optional[str] = None          # Extra diagnostic info (for failures / missing)


# ============================================================================
# RULES — the full un-nerf inventory, loaded from unnerfcc/rules/*.json.
# ============================================================================
# Each file at RULES_DIR/<id>.json holds one prompt id's rule list:
# {"id": "<id>", "rules": [{"description", "stock", "unnerf"}, ...]}, with
# stock/unnerf stored as arrays of lines (body.split("\n")). Order within a
# multi-rule id is the array order in that id's file; order matters only
# when rules within a file could overlap textually, which does not happen
# in this catalog today. Add a new rule by editing (or creating) the id's
# JSON file directly, or through unnerfcc-reanchor's reanchor_rules.py for
# a count-asserted edit. This module never re-authors the RULES literal;
# the JSON files are the single source of truth.
# ============================================================================


def _load_rules(rules_dir: Path) -> dict[str, list[Rule]]:
    """Load the rule catalog from rules_dir/*.json, one file per prompt id.

    Fails loudly (SystemExit) on any malformed shape: bad JSON, a non-object
    top-level, a filename/id mismatch, a non-object rule entry, a non-list or
    empty stock/unnerf, a non-string description, or an empty rules array.
    Rebuilds the same dict[str, list[Rule]] shape the
    old in-source RULES literal provided, with the .md suffix re-added to
    each key so apply_rules() and --only keep working unchanged. Also rejects
    a body that joins to an empty string and a body line holding a carriage
    return, because both silently break the downstream text replace.
    """
    rules: dict[str, list[Rule]] = {}
    if not rules_dir.is_dir():
        raise SystemExit(f"error: {rules_dir}: rules directory does not exist")
    rule_files = sorted(rules_dir.glob("*.json"))
    if not rule_files:
        raise SystemExit(f"error: {rules_dir}: no *.json rule files found")
    for path in rule_files:
        pid = path.stem
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise SystemExit(f"error: malformed JSON in {path}: {e}")
        if not isinstance(data, dict):
            raise SystemExit(f"error: {path}: top-level JSON must be an object")
        if data.get("id") != pid:
            raise SystemExit(
                f"error: {path} declares id {data.get('id')!r}, filename stem is {pid!r}"
            )
        rule_entries = data.get("rules")
        if not isinstance(rule_entries, list) or not rule_entries:
            raise SystemExit(f"error: {path}: 'rules' must be a non-empty list")
        entries: list[Rule] = []
        for r in rule_entries:
            if not isinstance(r, dict):
                raise SystemExit(f"error: {path}: rule entry must be an object")
            description = r.get("description")
            if not isinstance(description, str) or not description:
                raise SystemExit(f"error: {path}: rule has a missing or non-string 'description'")
            for field in ("stock", "unnerf"):
                value = r.get(field)
                if not isinstance(value, list) or not value:
                    raise SystemExit(f"error: {path}: rule has a missing or empty list '{field}'")
                if not all(isinstance(line, str) for line in value):
                    raise SystemExit(f"error: {path}: rule field '{field}' has a non-string element")
                if not any(line for line in value):
                    raise SystemExit(f"error: {path}: rule field '{field}' is empty")
                if any("\r" in line for line in value):
                    raise SystemExit(f"error: {path}: rule field '{field}' contains a carriage return")
            entries.append(
                Rule(
                    stock="\n".join(r["stock"]),
                    unnerf="\n".join(r["unnerf"]),
                    description=description,
                )
            )
        rules[f"{pid}.md"] = entries
    return rules


RULES: dict[str, list[Rule]] = _load_rules(RULES_DIR)


# ============================================================================
# LOGIC
# ============================================================================


def apply_rules(
    prompts_dir: Path,
    *,
    dry_run: bool,
    only: Optional[str],
) -> list[Result]:
    """Apply all RULES to files under prompts_dir. Return a flat list of Results."""
    results: list[Result] = []

    for filename, rules in RULES.items():
        if only and only != filename:
            continue

        path = prompts_dir / filename
        # Slot-sequence guard. The splicer (lib/patch-prompts.mjs) binds slots
        # POSITIONALLY: it splits the edited body on the `${NAME}` markers in the
        # order the prompt's `identifiers` list gives, and rebinds the i-th marker
        # to the i-th interpolation the stock string already had, restoring the
        # bundle's own variables in place. Identity hashing never sees a variable
        # name (a slot hashes as a bare `${}`), so POSITION is the only binding
        # there is. An edit must therefore keep every `${...}` placeholder, in the
        # same order.
        #
        # Every way of violating that is a defect, and each fails differently:
        #   dropped / reordered  the marker walk can't find it -> the whole prompt
        #                        is reported LOST and never reaches the binary;
        #   duplicated           the walk is ambiguous -> also LOST;
        #   added (new name)     it isn't a marker, so it survives as LITERAL TEXT
        #                        and the prompt ships reading `${FOO}` as prose.
        # All three are caught here, at authoring time, instead of at splice time:
        # the un-nerf's placeholder sequence must equal the stock's exactly.
        var_pat = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)")
        guard_failed = False
        for rule in rules:
            stock_vars = var_pat.findall(rule.stock)
            unnerf_vars = var_pat.findall(rule.unnerf)
            if stock_vars != unnerf_vars:
                guard_failed = True
                results.append(
                    Result(
                        filename=filename,
                        status="failed",
                        rule_description=rule.description,
                        detail=(
                            f"SLOT SEQUENCE GUARD: the un-nerf must keep every "
                            f"${{...}} placeholder of its stock text, in the same "
                            f"order. stock={stock_vars} unnerf={unnerf_vars}. "
                            f"The splicer rebinds slots by position, so a dropped "
                            f"or reordered placeholder loses the whole prompt and "
                            f"an added one ships as literal text. Fix the rule's "
                            f"`unnerf` before applying."
                        ),
                    )
                )
        if guard_failed:
            continue
        if not path.exists():
            results.append(
                Result(
                    filename=filename,
                    status="missing",
                    rule_description="(file)",
                    detail=f"File not found at: {path}",
                )
            )
            continue

        # Read as bytes so we can measure CRLF contamination without Python's
        # universal-newline mode quietly normalizing on our behalf. If a file
        # got CRLF-polluted (e.g. by a previous buggy script run, or by a
        # Windows editor), normalize to LF here and track that the file will
        # need rewriting even if no rule modifies text content.
        raw = path.read_bytes().decode("utf-8")
        content = raw.replace("\r\n", "\n")
        original = content
        # If normalization alone changed bytes on disk, ensure we write back.
        had_crlf = raw != content

        for rule in rules:
            if rule.stock in content:
                content = content.replace(rule.stock, rule.unnerf, 1)
                results.append(
                    Result(
                        filename=filename,
                        status="applied",
                        rule_description=rule.description,
                    )
                )
            elif rule.unnerf in content:
                results.append(
                    Result(
                        filename=filename,
                        status="skipped",
                        rule_description=rule.description,
                        detail="already un-nerfed",
                    )
                )
            else:
                # Neither stock nor unnerf present — drift or partial state.
                stock_preview = _truncate(rule.stock, 200)
                unnerf_preview = _truncate(rule.unnerf, 200)
                drift = _drift_diagnosis(rule.stock, content)
                detail = (
                    f"Expected stock text (first 200 chars):\n"
                    f"  {stock_preview!r}\n"
                    f"Expected un-nerf text (first 200 chars, for reference):\n"
                    f"  {unnerf_preview!r}\n"
                    f"Neither was found in the file.\n"
                    f"{drift}\n"
                    f"Action: open {path} and locate the passage the rule targets. "
                    f"If upstream text drifted, update the rule's `stock` field in "
                    f"that id's rules/<id>.json file to match the new upstream wording."
                )
                results.append(
                    Result(
                        filename=filename,
                        status="failed",
                        rule_description=rule.description,
                        detail=detail,
                    )
                )

        needs_write = content != original or had_crlf
        if needs_write and not dry_run:
            # Write as bytes so Python doesn't translate LF -> CRLF on Windows.
            # The prompts repo uses LF exclusively; preserving that matters for
            # git diffs to stay small after re-applying.
            path.write_bytes(content.encode("utf-8"))
            if had_crlf and content == original:
                # No un-nerf rule touched this file, but line endings were
                # fixed. Surface that as a dedicated status so the report
                # reflects reality.
                results.append(
                    Result(
                        filename=filename,
                        status="normalized",
                        rule_description="CRLF -> LF (line-ending cleanup)",
                        detail="Fixed CRLF line endings. No rule content change.",
                    )
                )

    return results


def _drift_diagnosis(stock: str, content: str, *, context_lines: int = 2) -> str:
    """Show HOW the file drifted from the rule's expected stock.

    When neither stock nor unnerf is found, the fix needs the ACTUAL current
    wording, not just the expected wording. This locates the block in `content`
    that most resembles `stock` (difflib, stdlib) and returns a unified diff of
    expected-stock vs that block, so the drift is visible inline without opening
    the file. Returns a short message when no similar block exists (the passage
    was removed or renamed wholesale).
    """
    stock_lines = stock.splitlines(keepends=True)
    content_lines = content.splitlines(keepends=True)
    if not stock_lines or not content_lines:
        return "No overlapping content to diff (the file or the stock text is empty)."

    # Find the content window most similar to the stock block. SequenceMatcher
    # on the first stock line anchors a candidate region; then score full windows
    # around each anchor and keep the best. Bounded and deterministic.
    anchor = stock_lines[0]
    n = len(stock_lines)
    best_ratio = 0.0
    best_start = 0
    sm = difflib.SequenceMatcher()
    sm.set_seq2(stock)
    # Candidate starts: every line whose similarity to the stock's first line is
    # non-trivial. Cap the scan so a huge file cannot blow the time budget.
    for i, line in enumerate(content_lines):
        if difflib.SequenceMatcher(None, line, anchor).ratio() < 0.4:
            continue
        window = "".join(content_lines[i : i + n])
        sm.set_seq1(window)
        ratio = sm.ratio()
        if ratio > best_ratio:
            best_ratio, best_start = ratio, i

    if best_ratio < 0.3:
        return (
            "No block in the file resembles the expected stock text "
            f"(best similarity {best_ratio:.0%}). The passage was likely removed "
            "or reworded wholesale; find its replacement by meaning."
        )

    lo = max(0, best_start - context_lines)
    hi = min(len(content_lines), best_start + n + context_lines)
    actual_block = content_lines[lo:hi]
    # Strip the kept line endings so unified_diff (lineterm="") + "\n".join does
    # not double the blank lines.
    diff = difflib.unified_diff(
        [ln.rstrip("\n") for ln in stock_lines],
        [ln.rstrip("\n") for ln in actual_block],
        fromfile="rule.stock (expected)",
        tofile=f"current file (lines {lo + 1}-{hi})",
        lineterm="",
    )
    body = "\n".join(diff)
    return (
        f"Closest block in the file (similarity {best_ratio:.0%}); "
        f"diff expected-stock -> current:\n{body}"
    )


def _truncate(s: str, limit: int) -> str:
    """One-line preview of s, truncated to limit with ellipsis, newlines escaped."""
    flat = s.replace("\n", "\\n")
    if len(flat) <= limit:
        return flat
    return flat[: limit - 3] + "..."


def format_report(results: list[Result], *, dry_run: bool, verbose: bool, quiet: bool = False) -> str:
    """Produce the human+Claude-readable report.

    quiet: collapse the per-file/per-rule listing to just the Summary counts.
    FAIL / MISSING entries are ALWAYS listed even in quiet mode — they're the
    actionable ones; only the (long, repetitive) APPLIED/SKIPPED lines are hidden.
    """
    by_file: dict[str, list[Result]] = {}
    for r in results:
        by_file.setdefault(r.filename, []).append(r)

    lines: list[str] = []
    header = "=== Un-nerf re-apply report"
    if dry_run:
        header += " (DRY RUN — no files written)"
    if quiet:
        header += " (summary)"
    header += " ==="
    lines.append(header)
    lines.append("")

    for filename in sorted(by_file.keys()):
        file_results = by_file[filename]
        # In quiet mode, only surface files that have a FAIL or MISSING to fix.
        if quiet and not any(r.status in ("failed", "missing") for r in file_results):
            continue
        lines.append(f"system-prompts/{filename}")
        for r in file_results:
            if quiet and r.status not in ("failed", "missing"):
                continue
            tag = r.status.upper()
            lines.append(f"  [{tag:<8}] {r.rule_description}")
            if r.status == "failed":
                for line in (r.detail or "").splitlines():
                    lines.append(f"             {line}")
            elif r.status == "missing":
                lines.append(f"             {r.detail}")
            elif r.status == "skipped" and verbose:
                lines.append(f"             {r.detail}")
        lines.append("")

    # ---- Summary ----
    counts = {"applied": 0, "skipped": 0, "failed": 0, "missing": 0, "normalized": 0}
    for r in results:
        counts[r.status] += 1

    files_touched = len(by_file)
    files_changed = sum(
        1 for rs in by_file.values() if any(r.status == "applied" for r in rs)
    )

    lines.append("=== Summary ===")
    lines.append(f"Files processed : {files_touched}")
    lines.append(f"Files changed   : {files_changed}")
    lines.append(f"Rules applied   : {counts['applied']}")
    lines.append(f"Rules skipped   : {counts['skipped']}  (already un-nerfed; idempotent)")
    lines.append(f"Rules FAILED    : {counts['failed']}")
    lines.append(f"Missing files   : {counts['missing']}")
    if counts["normalized"]:
        lines.append(f"Line-ending fix : {counts['normalized']}  (CRLF -> LF cleanup)")

    if counts["failed"] or counts["missing"]:
        lines.append("")
        lines.append("Some rules failed or files are missing. See the per-file")
        lines.append("[FAIL] / [MISSING] entries above for next steps.")

    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    # Force UTF-8 on stdout/stderr. Windows' default cp1252 can't encode the
    # em-dashes and arrows used in rule descriptions; without this, the
    # traceback is "UnicodeEncodeError: charmap can't encode '→'".
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:
            pass  # already-reconfigured stream or not a TextIOWrapper

    parser = argparse.ArgumentParser(
        description="Re-apply the tweakcc system-prompt un-nerfs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="See the module docstring at the top of this file for full documentation.",
    )
    parser.add_argument(
        "--dir",
        type=Path,
        default=DEFAULT_PROMPTS_DIR,
        help=f"Directory of .md prompts to process (default: {DEFAULT_PROMPTS_DIR})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change but do not modify any files.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Like --dry-run, but exit 1 if ANY rule would apply (useful in CI).",
    )
    parser.add_argument(
        "--only",
        type=str,
        default=None,
        help="Restrict processing to one filename (no path, just 'foo.md').",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Include detail on [SKIP] entries too.",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Collapse the per-rule listing to just the Summary counts (FAIL/MISSING still shown).",
    )
    parser.add_argument(
        "--dump-rules",
        type=str,
        default=None,
        metavar="PATH",
        help="Write every un-nerf rule (id, stock, unnerf) as JSON to PATH and exit. "
        "Lets the rule-direct binary patcher (lib/patch-rules.mjs) drive off the rules "
        "without reconstructing .md files.",
    )
    args = parser.parse_args(argv)

    if args.dump_rules:
        import json as _json

        out = []
        for fname, rules in RULES.items():
            pid = fname[:-3] if fname.endswith(".md") else fname
            for r in rules:
                out.append(
                    {"id": pid, "stock": r.stock, "unnerf": r.unnerf, "description": r.description}
                )
        Path(args.dump_rules).write_text(_json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        print(f"dumped {len(out)} rules -> {args.dump_rules}")
        return 0

    if not args.dir.exists():
        print(f"ERROR: prompts directory not found: {args.dir}", file=sys.stderr)
        return 2
    if not args.dir.is_dir():
        print(f"ERROR: --dir is not a directory: {args.dir}", file=sys.stderr)
        return 2

    dry_run = args.dry_run or args.check
    results = apply_rules(args.dir, dry_run=dry_run, only=args.only)
    print(format_report(results, dry_run=dry_run, verbose=args.verbose, quiet=args.quiet))

    # Exit logic
    if args.check:
        # Anything that would change OR any failure -> exit 1.
        # "normalized" counts as a change because it mutates the file on disk.
        if any(
            r.status in {"applied", "failed", "missing", "normalized"}
            for r in results
        ):
            return 1
        return 0

    if any(r.status in {"failed", "missing"} for r in results):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
